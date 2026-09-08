#!/usr/bin/env python3
"""Synthetic truth-table and Kissat replay for pivot exact-one CNFs."""

from __future__ import annotations

import argparse
import hashlib
import json
import random
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, "scratch")
from build_q4_k17_root5_pivot_exactone_cnf_20260815 import encode


def mask(values: list[int]) -> int:
    result = 0
    for value in values:
        result |= 1 << value
    return result


def brute_cover(rows: int, columns: list[int]) -> bool:
    full = (1 << rows) - 1
    incident = [[] for _ in range(rows)]
    for index, column in enumerate(columns):
        for row in range(rows):
            if column >> row & 1:
                incident[row].append(index)
    memo = set()

    def visit(used: int) -> bool:
        if used == full:
            return True
        if used in memo:
            return False
        row = min(
            (item for item in range(rows) if not (used >> item & 1)),
            key=lambda item: sum(not (columns[index] & used) for index in incident[item]),
        )
        for index in incident[row]:
            if not columns[index] & used and visit(used | columns[index]):
                return True
        memo.add(used)
        return False

    return visit(0)


def write_graph(path: Path, rows: int, columns: list[int]) -> None:
    with path.open("w", encoding="ascii") as stream:
        stream.write("# self\t1\t2\n")
        stream.write("# rows\t" + ",".join(map(str, range(rows))) + "\n")
        stream.write("pair_index\trows\n")
        for index, column in enumerate(columns):
            values = [row for row in range(rows) if column >> row & 1]
            stream.write(f"{1000 + index}\t" + ",".join(map(str, values)) + "\n")


def sinz_truth_table() -> None:
    for degree in range(1, 9):
        primary = list(range(1, degree + 1))
        if degree == 1:
            clauses = [primary]
            auxiliary = []
        else:
            auxiliary = list(range(degree + 1, 2 * degree))
            clauses = [primary, [-primary[0], auxiliary[0]]]
            for index in range(1, degree - 1):
                clauses.extend((
                    [-primary[index], auxiliary[index]],
                    [-auxiliary[index - 1], auxiliary[index]],
                    [-primary[index], -auxiliary[index - 1]],
                ))
            clauses.append([-primary[-1], -auxiliary[-1]])
        for primary_bits in range(1 << degree):
            extendable = False
            for auxiliary_bits in range(1 << len(auxiliary)):
                values = {}
                for index, variable in enumerate(primary):
                    values[variable] = bool(primary_bits >> index & 1)
                for index, variable in enumerate(auxiliary):
                    values[variable] = bool(auxiliary_bits >> index & 1)
                if all(any(values[abs(literal)] == (literal > 0)
                           for literal in clause) for clause in clauses):
                    extendable = True
                    break
            if extendable != (primary_bits.bit_count() == 1):
                raise AssertionError(f"Sinz truth-table failure at degree {degree}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--kissat", required=True, type=Path)
    parser.add_argument("--work-dir", required=True, type=Path)
    args = parser.parse_args()
    args.work_dir.mkdir(parents=True, exist_ok=True)
    sinz_truth_table()

    rng = random.Random(20260815)
    cases = []
    sat20 = [mask(list(range(10))), mask(list(range(10, 20)))]
    sat20.extend(mask(rng.sample(range(20), 10)) for _ in range(10))
    cases.append(("sat20", 20, sat20))
    cases.append(("unsat20", 20,
                  [mask([0] + rng.sample(range(1, 20), 9)) for _ in range(14)]))
    for case_index in range(10):
        rows = 30
        columns = []
        seen = set()
        while len(columns) < 22:
            column = mask(rng.sample(range(rows), 10))
            if column not in seen:
                seen.add(column)
                columns.append(column)
        if case_index % 3 == 0:
            columns.extend(mask(list(range(start, start + 10)))
                           for start in range(0, rows, 10))
        cases.append((f"random_{case_index:02d}", rows, columns))

    records = []
    aggregate = hashlib.sha256()
    for name, rows, columns in cases:
        expected = brute_cover(rows, columns)
        graph = args.work_dir / f"{name}.tsv"
        cnf = args.work_dir / f"{name}.cnf"
        mapping = args.work_dir / f"{name}.map.json"
        write_graph(graph, rows, columns)
        metadata = encode(graph, cnf, mapping)
        completed = subprocess.run(
            [str(args.kissat), str(cnf)], text=True, capture_output=True,
            timeout=15, check=False,
        )
        sat = "s SATISFIABLE" in completed.stdout
        unsat = "s UNSATISFIABLE" in completed.stdout
        if not (sat ^ unsat) or sat != expected:
            raise AssertionError(f"{name}: Kissat/brute mismatch")
        if sat:
            model = set()
            for line in completed.stdout.splitlines():
                if line.startswith("v "):
                    model.update(int(item) for item in line.split()[1:] if int(item) > 0)
            selected = [index for index in range(1, metadata["primary_variables"] + 1)
                        if index in model]
            used = 0
            for variable in selected:
                column = columns[variable - 1]
                if used & column:
                    raise AssertionError(f"{name}: overlapping model columns")
                used |= column
            if used != (1 << rows) - 1:
                raise AssertionError(f"{name}: incomplete model")
        digest = hashlib.sha256(cnf.read_bytes()).hexdigest()
        aggregate.update(bytes.fromhex(digest))
        records.append({"name": name, "rows": rows, "columns": len(columns),
                        "status": "SAT" if sat else "UNSAT", "cnf_sha256": digest})

    print(json.dumps({
        "status": "PASS",
        "scope": "Sinz degree1..8 truth tables plus Kissat/brute exact-cover equivalence",
        "case_count": len(records),
        "aggregate_cnf_sha256": aggregate.hexdigest(),
        "cases": records,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
