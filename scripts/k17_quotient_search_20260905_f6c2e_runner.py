#!/usr/bin/env python3
"""Bounded h100-only batch of independently seeded single-thread searches."""
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
    parser.add_argument("--resume", type=Path)
    parser.add_argument("--phase", choices=("initial", "shadows", "repair"), default="initial")
    parser.add_argument("--weights", type=float, nargs=7,
                        metavar=("RES", "U1", "L2", "U2", "L3", "HOT", "COLD"))
    parser.add_argument("--moves", type=int, help="optional per-worker proposal-attempt cap")
    args = parser.parse_args()
    if not 1 <= args.count <= 60 or not 1 <= args.seconds <= 3600:
        parser.error("count must be 1..60 and seconds 1..3600")
    if args.moves is not None and args.moves < 1:
        parser.error("moves must be positive")
    if args.weights and (any(value < 0 for value in args.weights[:5])
                         or any(value <= 0 for value in args.weights[5:])):
        parser.error("weights must be nonnegative and temperatures positive")
    if socket.gethostname().split(".")[0].lower() not in ("h100", "arboghast"):
        parser.error("heavy runs are restricted to h100")
    binary = args.binary.resolve(strict=True)
    resume = args.resume.resolve(strict=True) if args.resume else None
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
    if args.phase == "shadows":
        settings = [
            (2.5, 4.0, 1.0, 0.4, 0.4, 1.5, 0.05),
            (3.0, 4.0, 1.2, 0.5, 0.5, 1.0, 0.02),
            (1.5, 3.0, 1.0, 0.4, 0.4, 2.4, 0.10),
            (4.0, 4.0, 2.0, 0.5, 0.5, 3.0, 0.12),
            (5.0, 8.0, 1.0, 0.3, 0.3, 0.8, 0.02),
            (2.5, 4.0, 1.5, 1.0, 1.0, 1.5, 0.08),
            (2.5, 6.0, 2.0, 0.8, 0.8, 4.0, 0.15),
            (2.5, 4.0, 1.0, 0.4, 0.4, 5.0, 0.08),
        ]
    elif args.phase == "repair":
        settings = [
            (5.0, 8.0, 1.0, 0.3, 0.3, 0.8, 0.02),
            (5.0, 8.0, 1.0, 0.5, 0.5, 0.5, 0.01),
            (8.0, 8.0, 1.0, 0.7, 0.7, 1.0, 0.02),
            (4.0, 6.0, 1.0, 0.5, 0.5, 0.7, 0.02),
            (5.0, 8.0, 1.0, 0.3, 0.3, 1.2, 0.03),
            (6.0, 10.0, 1.0, 0.5, 0.5, 0.6, 0.01),
            (5.0, 8.0, 1.0, 0.8, 0.8, 0.8, 0.02),
            (4.0, 6.0, 1.0, 0.5, 0.5, 1.5, 0.03),
        ]
    if args.weights:
        settings = [args.weights]
    env = dict(os.environ, OMP_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1", MKL_NUM_THREADS="1")
    jobs = []
    try:
        for i in range(args.count):
            seed = args.seed_base + i
            prefix = directory / f"seed{seed}"
            command = [str(binary), "--seed", str(seed), "--seconds", str(args.seconds), "--output", str(prefix)]
            if resume:
                command.extend(["--resume", str(resume)])
            if args.moves is not None:
                command.extend(["--moves", str(args.moves)])
            for name, value in zip(("res", "u1", "l2", "u2", "l3", "hot", "cold"), settings[i % len(settings)]):
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
