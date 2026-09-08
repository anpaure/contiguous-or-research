#!/usr/bin/env python3
"""Reviewed-source runner only; compile the reviewed C++ separately on h100.

One immutable literal snapshot, one fixed Dinic decision and certificate replay.
Driver CPU5 + child CPU115 <= aggregate CPU120. No retry or alternate input.
"""
import argparse
import hashlib
import json
from pathlib import Path
import resource
import shutil
import signal
import socket
import subprocess
import time

EXPECTED_SHA = "0b166713d18f9ba4d064b07575c17068008954ac808313359c5fd0bf5dfe24d7"
CAPS = dict(aggregate_cpu_seconds=120, driver_cpu_seconds=5,
            mathematical_child_cpu_seconds=115, wall_seconds=150,
            address_space_bytes=2*1024**3, individual_file_bytes=512*1024**2)


def dump(path, value):
    path.write_text(json.dumps(value, sort_keys=True, indent=2) + "\n")


def digest(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        while block := f.read(1024*1024):
            h.update(block)
    return h.hexdigest()


def child_limits():
    resource.setrlimit(resource.RLIMIT_CPU, (CAPS["mathematical_child_cpu_seconds"],)*2)
    resource.setrlimit(resource.RLIMIT_AS, (CAPS["address_space_bytes"],)*2)
    resource.setrlimit(resource.RLIMIT_FSIZE, (CAPS["individual_file_bytes"],)*2)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--word", type=Path, required=True)
    p.add_argument("--source", type=Path, required=True)
    p.add_argument("--binary", type=Path, required=True)
    p.add_argument("--out", type=Path, required=True)
    a = p.parse_args()
    assert socket.gethostname().split(".")[0] == "arboghast", "h100 only"
    # Keep the hard ceiling high enough for the child to inherit CPU115;
    # tighten the driver's hard ceiling immediately after the child is forked.
    resource.setrlimit(resource.RLIMIT_CPU, (CAPS["driver_cpu_seconds"],
                                          CAPS["aggregate_cpu_seconds"]))
    resource.setrlimit(resource.RLIMIT_AS, (CAPS["address_space_bytes"],)*2)
    resource.setrlimit(resource.RLIMIT_FSIZE, (CAPS["individual_file_bytes"],)*2)
    began = time.monotonic()
    cpu_began = time.process_time()
    a.out.mkdir(parents=True, exist_ok=False)
    running = None

    def timed_out(_signum, _frame):
        if running is not None and running.poll() is None:
            running.kill()
        raise TimeoutError("whole-run wall limit")

    signal.signal(signal.SIGALRM, timed_out)
    signal.alarm(CAPS["wall_seconds"])
    try:
        raw = a.word.read_bytes()
        sha = hashlib.sha256(raw).hexdigest()
        if sha != EXPECTED_SHA:
            raise ValueError("fixed input raw SHA mismatch: " + sha)
        # The C++ reads this exact checked snapshot, never a changing input path.
        snapshot = a.out / "input_k21_upper353297.word"
        snapshot.write_bytes(raw)
        (a.out / "runner.py").write_bytes(Path(__file__).read_bytes())
        (a.out / "checker.cpp").write_bytes(a.source.read_bytes())
        shutil.copyfile(a.binary, a.out / "checker.bin")
        (a.out / "checker.bin").chmod(0o700)
        provenance = dict(status="RUNNING_NOT_CERTIFIED", input_sha256=sha,
                          cpp_source_sha256=digest(a.out / "checker.cpp"),
                          runner_source_sha256=digest(Path(__file__)),
                          binary_sha256=digest(a.out / "checker.bin"), resource_caps=CAPS,
                          hostname=socket.gethostname())
        dump(a.out / "run_started.json", provenance)
        remaining = 148 - (time.monotonic() - began)
        if remaining <= 0:
            raise TimeoutError("preparation exhausted wall allowance")
        with (a.out / "run.log").open("wb") as log:
            running = subprocess.Popen([str((a.out / "checker.bin").resolve()), str(snapshot.resolve()),
                                        str(a.out.resolve())], stdout=log,
                                       stderr=subprocess.STDOUT, preexec_fn=child_limits)
            resource.setrlimit(resource.RLIMIT_CPU, (CAPS["driver_cpu_seconds"],)*2)
            try:
                code = running.wait(timeout=remaining)
            except subprocess.TimeoutExpired:
                running.kill()
                running.wait()
                raise TimeoutError("mathematical child wall allowance")
        if code != 0:
            status = "INCONCLUSIVE_RESOURCE_LIMIT" if code < 0 or code == 3 else "ERROR_NOT_CERTIFIED"
            dump(a.out / "run_failure.json", dict(status=status, child_returncode=code,
                                                  resource_caps=CAPS))
            raise SystemExit(2)
        certificate = json.loads((a.out / "candidate_hall_certificate.json").read_text())
        expected_status = "PASS_FIXED_GRAPH_AND_INDEPENDENT_CERTIFICATE_REPLAY"
        if certificate.get("status") != expected_status:
            raise ValueError("child omitted final independent replay certificate")
        usage = resource.getrusage(resource.RUSAGE_CHILDREN)
        child_cpu = usage.ru_utime + usage.ru_stime
        driver_cpu = time.process_time() - cpu_began
        report = dict(provenance, status=expected_status, child_returncode=code,
                      result=certificate, child_cpu_seconds=child_cpu,
                      driver_cpu_seconds=driver_cpu,
                      aggregate_cpu_seconds=child_cpu+driver_cpu,
                      elapsed_wall_seconds=time.monotonic()-began,
                      scope="One pinned three-cycle candidate graph; no word search, retry, alternate cut, or simultaneous cap assignment.")
        dump(a.out / "run_complete.json", report)
        lines = []
        for path in sorted(a.out.iterdir()):
            if path.is_file() and path.name != "SHA256SUMS":
                lines.append(digest(path) + "  " + path.name)
        (a.out / "SHA256SUMS").write_text("\n".join(lines) + "\n")
        print(json.dumps(dict(status=report["status"],
                              edges=certificate["graph_edges"],
                              flow=certificate["maximum_weighted_flow"],
                              deficiency=certificate["physical_hall_deficiency"],
                              aggregate_cpu_seconds=report["aggregate_cpu_seconds"],
                              elapsed_wall_seconds=report["elapsed_wall_seconds"])), flush=True)
    except (MemoryError, TimeoutError) as e:
        if running is not None and running.poll() is None:
            running.kill()
            running.wait()
        dump(a.out / "run_failure.json", dict(status="INCONCLUSIVE_RESOURCE_LIMIT",
                                              exception=repr(e), resource_caps=CAPS))
        raise
    except Exception as e:
        if running is not None and running.poll() is None:
            running.kill()
            running.wait()
        dump(a.out / "run_failure.json", dict(status="ERROR_NOT_CERTIFIED",
                                              exception=repr(e), resource_caps=CAPS))
        raise
    finally:
        if running is not None and running.poll() is None:
            running.kill()
            running.wait()


if __name__ == "__main__":
    main()
