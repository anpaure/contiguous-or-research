#!/usr/bin/env python3
"""Run one bounded exact Algorithm-X decision for every K20 branch."""

from __future__ import annotations

import argparse
import concurrent.futures
import json
import subprocess
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--graph-dir", required=True, type=Path)
    parser.add_argument("--out-dir", required=True, type=Path)
    parser.add_argument("--binary", required=True, type=Path)
    parser.add_argument("--seconds", required=True, type=float)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    graphs = sorted(args.graph_dir.glob("*.tsv"))
    if not graphs:
        raise ValueError("no branch graphs")

    def run_one(item: tuple[int, Path]) -> dict:
        job, graph = item
        result = args.out_dir / f"{graph.stem}.result.json"
        output = args.out_dir / f"{graph.stem}.h100.out"
        with output.open("w", encoding="ascii") as stream:
            completed = subprocess.run(
                [str(args.binary), str(graph), str(args.seconds), str(result)],
                stdout=stream,
                stderr=subprocess.STDOUT,
                check=False,
            )
        payload = json.loads(result.read_text(encoding="ascii"))
        if payload["status"] not in ("SAT", "UNSAT", "UNKNOWN"):
            raise ValueError("bad solver status")
        return {
            "job": job,
            "graph": str(graph),
            "result": str(result),
            "output": str(output),
            "status": payload["status"],
            "nodes": payload["nodes"],
            "exit_code": completed.returncode,
        }

    with concurrent.futures.ThreadPoolExecutor(max_workers=len(graphs)) as pool:
        records = list(pool.map(run_one, enumerate(graphs)))
    summary = {
        "status": "PASS",
        "scope": "bounded exact monolithic Algorithm-X over every full-atlas K20 branch",
        "graphs": len(graphs),
        "seconds_per_branch": args.seconds,
        "records": records,
        "status_histogram": {
            status: sum(record["status"] == status for record in records)
            for status in ("SAT", "UNSAT", "UNKNOWN")
        },
    }
    (args.out_dir / "summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="ascii"
    )
    print(json.dumps({
        "status": "PASS",
        "graphs": len(graphs),
        "status_histogram": summary["status_histogram"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
