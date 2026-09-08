#!/usr/bin/env python3
"""Sequential worker-scaling benchmark using the same fixed-temperature search."""

import argparse
import json
from pathlib import Path
import socket
import subprocess
import sys
import time


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--runner", type=Path, required=True)
    parser.add_argument("--binary", type=Path, required=True)
    parser.add_argument("--resume", type=Path, required=True)
    parser.add_argument("--directory", type=Path, required=True)
    parser.add_argument("--counts", type=int, nargs="+", default=[8, 28, 56])
    parser.add_argument("--seconds", type=int, default=12)
    args = parser.parse_args()
    if socket.gethostname().split(".")[0].lower() not in ("h100", "arboghast"):
        parser.error("heavy benchmarks are restricted to h100")
    if not 1 <= args.seconds <= 60 or any(not 1 <= n <= 60 for n in args.counts):
        parser.error("seconds must be 1..60 and counts 1..60")
    if len(set(args.counts)) != len(args.counts):
        parser.error("worker counts must be distinct")
    runner, binary, resume = (p.resolve(strict=True) for p in (args.runner, args.binary, args.resume))
    args.directory.mkdir(exist_ok=False)
    directory = args.directory.resolve()
    reports = []
    for count in args.counts:
        batch = directory / f"workers{count}"
        command = [sys.executable, str(runner), "--binary", str(binary),
                   "--directory", str(batch), "--resume", str(resume),
                   "--seconds", str(args.seconds), "--count", str(count),
                   "--seed-base", "17094001", "--weights", "5", "8", "1",
                   "0.3", "0.3", "0.8", "0.8"]
        started = time.monotonic()
        with (directory / f"workers{count}.log").open("x") as log:
            subprocess.run(command, stdout=log, stderr=subprocess.STDOUT,
                           timeout=args.seconds + 180, check=True)
        wall = time.monotonic() - started
        stats = [json.loads((batch / f"seed{17094001 + i}.stats.json").read_text())
                 for i in range(count)]
        proposals = sum(s["proposals"] for s in stats)
        report = {"workers": count, "wall_seconds": wall,
                  "evaluated_proposals": proposals,
                  "wall_proposals_per_second": proposals / wall,
                  "search_proposals_per_second": proposals / max(s["seconds"] for s in stats),
                  "command": command}
        reports.append(report)
        (directory / "summary.json").write_text(json.dumps(reports, indent=2) + "\n")
        print(json.dumps(report, sort_keys=True), flush=True)
    best = max(reports, key=lambda r: r["wall_proposals_per_second"])
    print(f"BEST workers={best['workers']} proposals_per_second={best['wall_proposals_per_second']:.0f}")


if __name__ == "__main__":
    main()
