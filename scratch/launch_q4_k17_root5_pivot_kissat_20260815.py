#!/usr/bin/env python3
"""Run bounded Kissat jobs on a pivot exact-one CNF bank."""

from __future__ import annotations

import argparse
import concurrent.futures
import json
import subprocess
import threading
import time
from pathlib import Path


def parse_model(output: str, primary: int) -> set[int]:
    model = set()
    for line in output.splitlines():
        if not line.startswith("v "):
            continue
        for item in line.split()[1:]:
            literal = int(item)
            if 0 < literal <= primary:
                model.add(literal)
    return model


def verify_primary_model(mapping: dict, selected_variables: set[int]) -> list[int]:
    graph_lines = Path(mapping["graph"]).read_text(encoding="ascii").splitlines()
    columns = []
    for line in graph_lines[3:]:
        if line:
            _, rows_text = line.split("\t", 1)
            columns.append(set(map(int, rows_text.split(","))))
    selected = sorted(selected_variables)
    if len(selected) != mapping["target_clique"]:
        raise ValueError("Kissat model has wrong primary-column count")
    used = set()
    for variable in selected:
        rows = columns[variable - 1]
        if used & rows:
            raise ValueError("Kissat model has overlapping columns")
        used |= rows
    if used != set(mapping["rows"]):
        raise ValueError("Kissat model does not cover every residual row")
    return [mapping["pair_indices"][variable - 1] for variable in selected]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", required=True, type=Path)
    parser.add_argument("--out-dir", required=True, type=Path)
    parser.add_argument("--kissat", required=True, type=Path)
    parser.add_argument("--seconds", required=True, type=int)
    parser.add_argument("--workers", required=True, type=int)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    manifest = json.loads(args.manifest.read_text(encoding="ascii"))
    records = []
    lock = threading.Lock()
    stop = threading.Event()

    def run_one(item: tuple[int, dict]) -> dict:
        job, mapping = item
        if stop.is_set():
            record = {"job": job, "cnf": mapping["cnf"], "status": "SKIPPED_AFTER_SAT"}
            with lock:
                records.append(record)
            return record
        stem = Path(mapping["cnf"]).stem
        output_path = args.out_dir / f"{stem}.kissat.h100.out"
        result_path = args.out_dir / f"{stem}.result.json"
        started = time.monotonic()
        completed = subprocess.run(
            ["timeout", "--signal=TERM", "--kill-after=2", str(args.seconds),
             str(args.kissat), mapping["cnf"]],
            text=True, capture_output=True, check=False,
        )
        elapsed = time.monotonic() - started
        solver_output = completed.stdout + completed.stderr
        output_path.write_text(solver_output, encoding="ascii", errors="replace")
        if "s SATISFIABLE" in solver_output:
            status = "SAT"
            model = parse_model(solver_output, mapping["primary_variables"])
            pair_indices = verify_primary_model(mapping, model)
            stop.set()
        elif "s UNSATISFIABLE" in solver_output:
            status = "UNSAT"
            pair_indices = []
        else:
            status = "UNKNOWN"
            pair_indices = []
        result = {
            "status": status,
            "scope": "bounded Kissat on one Sinz exact-one pivot CNF",
            "graph": mapping["graph"],
            "self_indices": mapping["self_indices"],
            "residual_rows": len(mapping["rows"]),
            "pair_columns": mapping["primary_variables"],
            "target_clique": mapping["target_clique"],
            "elapsed_seconds": elapsed,
            "nodes": 0,
            "backend": "kissat",
            "backend_exit_code": completed.returncode,
            "cnf": mapping["cnf"],
            "cnf_sha256": mapping["cnf_sha256"],
            "pair_indices": pair_indices,
        }
        result_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n",
                               encoding="ascii")
        record = {
            "job": job,
            "cnf": mapping["cnf"],
            "result": str(result_path),
            "output": str(output_path),
            "status": status,
            "exit_code": completed.returncode,
            "elapsed_seconds": elapsed,
        }
        with lock:
            records.append(record)
        return record

    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = [pool.submit(run_one, item)
                   for item in enumerate(manifest["records"])]
        for future in concurrent.futures.as_completed(futures):
            future.result()

    summary = {
        "status": "PASS",
        "scope": "bounded Kissat campaign on complete pivot exact-one CNF bank",
        "manifest": str(args.manifest),
        "cnfs": len(manifest["records"]),
        "workers": args.workers,
        "seconds_per_cnf": args.seconds,
        "sat_found": any(record["status"] == "SAT" for record in records),
        "records": sorted(records, key=lambda record: record["job"]),
    }
    (args.out_dir / "summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="ascii"
    )
    print(json.dumps({
        "status": "PASS",
        "cnfs": len(manifest["records"]),
        "completed": len(records),
        "sat_found": summary["sat_found"],
        "status_histogram": {
            status: sum(record["status"] == status for record in records)
            for status in ("SAT", "UNSAT", "UNKNOWN", "SKIPPED_AFTER_SAT")
        },
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
