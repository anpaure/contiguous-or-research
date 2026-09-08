#!/usr/bin/env python3
"""Bounded parallel launcher for seeded row-661 pivot subproblems."""

from __future__ import annotations

import argparse
import concurrent.futures
import json
import subprocess
import threading
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--graph-dir", required=True, type=Path)
    parser.add_argument("--out-dir", required=True, type=Path)
    parser.add_argument("--binary", required=True, type=Path)
    parser.add_argument("--seconds", required=True, type=float)
    parser.add_argument("--workers", required=True, type=int)
    parser.add_argument("--seed-base", required=True, type=int)
    parser.add_argument("--opposite-order", action="store_true")
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    graphs = sorted(args.graph_dir.glob("*.tsv"))
    if not graphs:
        raise ValueError("no pivot graphs")
    stop = threading.Event()
    lock = threading.Lock()
    records: list[dict] = []
    slacks = (0, 2, 4, 8)

    def run_one(item: tuple[int, Path]) -> dict:
        job, graph = item
        if stop.is_set():
            record = {"job": job, "graph": str(graph), "status": "SKIPPED_AFTER_SAT"}
            with lock:
                records.append(record)
            return record
        stem = graph.stem
        result = args.out_dir / f"{stem}.result.json"
        output = args.out_dir / f"{stem}.h100.out"
        exit_path = args.out_dir / f"{stem}.exit"
        if args.opposite_order:
            desired_mode = (2, 2, 1, 2)[job % 4]
            seed = args.seed_base + 4 * job
            seed += (desired_mode - seed) % 4
            slack = tuple(reversed(slacks))[job % len(slacks)]
        else:
            seed = args.seed_base + job
            slack = slacks[job % len(slacks)]
        with output.open("w", encoding="ascii") as stream:
            completed = subprocess.run(
                [str(args.binary), str(graph), str(args.seconds), str(result),
                 str(seed), str(slack)],
                stdout=stream,
                stderr=subprocess.STDOUT,
                check=False,
            )
        exit_path.write_text(f"{completed.returncode}\n", encoding="ascii")
        payload = json.loads(result.read_text(encoding="ascii"))
        record = {
            "job": job,
            "graph": str(graph),
            "result": str(result),
            "seed": seed,
            "row_slack": slack,
            "status": payload["status"],
            "nodes": payload["nodes"],
        }
        if payload["status"] == "SAT":
            stop.set()
        with lock:
            records.append(record)
        return record

    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = [pool.submit(run_one, item) for item in enumerate(graphs)]
        for future in concurrent.futures.as_completed(futures):
            future.result()

    summary = {
        "status": "PASS",
        "scope": "bounded seeded SAT-first pass over row-661 pivot partition",
        "graphs": len(graphs),
        "workers": args.workers,
        "seconds_per_pivot": args.seconds,
        "seed_base": args.seed_base,
        "opposite_order": args.opposite_order,
        "sat_found": any(record["status"] == "SAT" for record in records),
        "records": sorted(records, key=lambda record: record["job"]),
    }
    (args.out_dir / "summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="ascii"
    )
    print(json.dumps({
        "status": "PASS",
        "graphs": len(graphs),
        "completed": len(records),
        "sat_found": summary["sat_found"],
        "status_histogram": {
            status: sum(record["status"] == status for record in records)
            for status in ("SAT", "UNSAT", "UNKNOWN", "SKIPPED_AFTER_SAT")
        },
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
