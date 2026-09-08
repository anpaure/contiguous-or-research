#!/usr/bin/env python3
"""Bounded h100-only batch, at most eight owned single-thread search children."""
import argparse
import json
import os
from pathlib import Path
import shlex
import socket
import subprocess
import time


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--binary", type=Path, required=True)
    parser.add_argument("--directory", type=Path, required=True)
    parser.add_argument("--seconds", type=int, default=240)
    parser.add_argument("--seed-base", type=int, default=17090501)
    parser.add_argument("--count", type=int, default=8)
    args = parser.parse_args()
    if not 1 <= args.count <= 8 or not 1 <= args.seconds <= 360:
        parser.error("count must be 1..8 and seconds 1..360")
    if socket.gethostname().split(".")[0].lower() not in ("h100", "arboghast"):
        parser.error("heavy runs are restricted to h100")
    binary = args.binary.resolve(strict=True)
    args.directory.mkdir(exist_ok=False)
    directory = args.directory.resolve()
    # Main target is residence plus U1; retain some lower/higher pressure.
    settings = [
        (1.5, 3.0, 0.5, 0.20, 0.20, 2.0, 0.12),
        (2.5, 3.0, 0.3, 0.10, 0.10, 2.4, 0.14),
        (1.0, 4.0, 0.4, 0.15, 0.15, 2.4, 0.14),
        (3.0, 2.0, 0.2, 0.10, 0.10, 2.0, 0.10),
        (1.8, 3.5, 0.8, 0.25, 0.25, 3.2, 0.20),
        (1.5, 4.0, 0.0, 0.00, 0.00, 2.0, 0.08),
        (3.5, 3.0, 0.0, 0.00, 0.00, 2.8, 0.10),
        (2.0, 3.0, 1.0, 0.40, 0.40, 3.5, 0.18),
    ]
    env = dict(os.environ, OMP_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1", MKL_NUM_THREADS="1")
    jobs = []
    try:
        for i in range(args.count):
            seed = args.seed_base + i
            prefix = directory / f"seed{seed}"
            command = [str(binary), "--seed", str(seed), "--seconds", str(args.seconds), "--output", str(prefix)]
            for name, value in zip(("res", "u1", "l2", "u2", "l3", "hot", "cold"), settings[i]):
                command.extend(["--" + name, str(value)])
            log = prefix.with_suffix(".log").open("w")
            process = subprocess.Popen(command, stdout=log, stderr=subprocess.STDOUT, env=env)
            job = dict(seed=seed, command=command, shell_command=shlex.join(command), pid=process.pid,
                       process=process, log=log, started=time.monotonic(), returncode=None)
            jobs.append(job)
            print(f"START seed={seed} pid={process.pid} command={shlex.join(command)}", flush=True)
        manifest = [{k: v for k, v in job.items() if k not in ("process", "log", "started")} for job in jobs]
        (directory / "commands.json").write_text(json.dumps(manifest, indent=2) + "\n")
        while any(job["returncode"] is None for job in jobs):
            for job in jobs:
                if job["returncode"] is not None:
                    continue
                process = job["process"]
                code = process.poll()
                if code is None and time.monotonic() - job["started"] > args.seconds + 120:
                    process.terminate()
                    try:
                        code = process.wait(timeout=10)
                    except subprocess.TimeoutExpired:
                        process.kill()
                        code = process.wait()
                if code is not None:
                    job["returncode"] = code
                    job["wall_seconds"] = time.monotonic() - job["started"]
                    job["log"].close()
                    print(f"FINISH seed={job['seed']} pid={process.pid} rc={code}", flush=True)
            time.sleep(0.25)
    finally:
        for job in jobs:
            process = job["process"]
            if process.poll() is None:
                process.terminate()
                try:
                    process.wait(timeout=10)
                except subprocess.TimeoutExpired:
                    process.kill()
                    process.wait()
            job["returncode"] = process.returncode
            job["log"].close()
        report = [{k: v for k, v in job.items() if k not in ("process", "log", "started")} for job in jobs]
        (directory / "finished.json").write_text(json.dumps(report, indent=2) + "\n")
    if any(job["returncode"] for job in jobs):
        raise SystemExit("one or more search processes failed")
    print(f"ALL_FINISHED count={len(jobs)}", flush=True)


if __name__ == "__main__":
    main()
