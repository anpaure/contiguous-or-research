#!/usr/bin/env python3
"""Deterministic synthetic replay for the exact disjoint-column solver."""

from __future__ import annotations

import argparse
import hashlib
import json
import random
import subprocess
from pathlib import Path


def exact_cover(rows: int, columns: list[int]) -> bool:
    full = (1 << rows) - 1
    incident = [[] for _ in range(rows)]
    for index, mask in enumerate(columns):
        for row in range(rows):
            if mask >> row & 1:
                incident[row].append(index)

    memo: dict[int, bool] = {}

    def visit(used: int) -> bool:
        if used == full:
            return True
        if used in memo:
            return memo[used]
        available_rows = [row for row in range(rows) if not (used >> row & 1)]
        row = min(
            available_rows,
            key=lambda item: sum(not (columns[index] & used) for index in incident[item]),
        )
        for index in incident[row]:
            mask = columns[index]
            if not (mask & used) and visit(used | mask):
                memo[used] = True
                return True
        memo[used] = False
        return False

    return visit(0)


def mask_of(values: list[int]) -> int:
    result = 0
    for value in values:
        result |= 1 << value
    return result


def write_case(path: Path, rows: int, columns: list[int]) -> None:
    with path.open("w", encoding="utf-8") as stream:
        stream.write("# self\t1\t2\n")
        stream.write("# rows\t" + ",".join(map(str, range(rows))) + "\n")
        stream.write("pair_index\trows\n")
        for index, mask in enumerate(columns):
            values = [row for row in range(rows) if mask >> row & 1]
            assert len(values) == 10
            stream.write(f"{100000 + index}\t" + ",".join(map(str, values)) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--binary", required=True, type=Path)
    parser.add_argument("--work-dir", required=True, type=Path)
    args = parser.parse_args()
    args.work_dir.mkdir(parents=True, exist_ok=True)

    rng = random.Random(20260815)
    cases: list[tuple[str, int, list[int]]] = []

    sat20 = [mask_of(list(range(10))), mask_of(list(range(10, 20)))]
    for _ in range(12):
        sat20.append(mask_of(rng.sample(range(20), 10)))
    cases.append(("planted_sat20", 20, sat20))

    unsat20 = []
    for _ in range(16):
        unsat20.append(mask_of([0] + rng.sample(range(1, 20), 9)))
    cases.append(("common_row_unsat20", 20, unsat20))

    disconnected_sat30 = []
    for start in (0, 10, 20):
        block = list(range(start, start + 10))
        disconnected_sat30.extend([mask_of(block), mask_of(block)])
    cases.append(("component_sat30", 30, disconnected_sat30))

    component_unsat30 = []
    for start in (0, 15):
        block = list(range(start, start + 15))
        for shift in range(15):
            component_unsat30.append(mask_of([block[(shift + j) % 15] for j in range(10)]))
    cases.append(("component_mod10_unsat30", 30, component_unsat30))

    for case_index in range(24):
        rows = 30 if case_index < 16 else 40
        count = 24 if rows == 30 else 30
        columns = []
        seen = set()
        while len(columns) < count:
            mask = mask_of(rng.sample(range(rows), 10))
            if mask not in seen:
                seen.add(mask)
                columns.append(mask)
        if case_index % 4 == 0:
            for start in range(0, rows, 10):
                columns.append(mask_of(list(range(start, start + 10))))
        cases.append((f"random_{case_index:02d}", rows, columns))

    records = []
    aggregate = hashlib.sha256()
    for name, rows, columns in cases:
        expected = exact_cover(rows, columns)
        graph = args.work_dir / f"{name}.tsv"
        result = args.work_dir / f"{name}.json"
        write_case(graph, rows, columns)
        completed = subprocess.run(
            [str(args.binary), str(graph), "30", str(result)],
            text=True,
            capture_output=True,
            check=False,
        )
        if completed.returncode not in (0, 3):
            raise RuntimeError(f"{name}: solver exit {completed.returncode}: {completed.stderr}")
        payload = json.loads(result.read_text(encoding="utf-8"))
        actual = payload["status"] == "SAT"
        if payload["status"] == "UNKNOWN":
            raise AssertionError(f"{name}: unexpected timeout")
        if actual != expected:
            raise AssertionError(f"{name}: expected {expected}, got {payload['status']}")
        if actual:
            chosen = payload["pair_indices"]
            chosen_masks = [columns[index - 100000] for index in chosen]
            union = 0
            for mask in chosen_masks:
                if union & mask:
                    raise AssertionError(f"{name}: non-disjoint SAT witness")
                union |= mask
            if union != (1 << rows) - 1:
                raise AssertionError(f"{name}: incomplete SAT witness")
        digest = hashlib.sha256(graph.read_bytes()).hexdigest()
        aggregate.update(bytes.fromhex(digest))
        records.append({"name": name, "rows": rows, "columns": len(columns),
                        "status": payload["status"], "graph_sha256": digest})

    output = {
        "status": "PASS",
        "scope": "synthetic brute-force equivalence for exact disjoint-column solver",
        "case_count": len(records),
        "aggregate_graph_sha256": aggregate.hexdigest(),
        "cases": records,
    }
    print(json.dumps(output, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
