#!/usr/bin/env python3
"""Build Sinz exact-one CNFs for row-661 pivot graphs (H100 only)."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    digest.update(path.read_bytes())
    return digest.hexdigest()


def parse_graph(path: Path) -> tuple[tuple[int, int], list[int], list[tuple[int, tuple[int, ...]]]]:
    lines = path.read_text(encoding="ascii").splitlines()
    self_pair = tuple(map(int, lines[0].split("\t")[1:]))
    rows = list(map(int, lines[1].split("\t", 1)[1].split(",")))
    columns = []
    for line in lines[3:]:
        if not line:
            continue
        index_text, rows_text = line.split("\t", 1)
        columns.append((int(index_text), tuple(map(int, rows_text.split(",")))))
    return self_pair, rows, columns


def encode(path: Path, cnf_path: Path, map_path: Path) -> dict:
    self_pair, rows, columns = parse_graph(path)
    if len(rows) % 10 or len(rows) != len(set(rows)):
        raise ValueError("bad residual-row interface")
    row_position = {row: position for position, row in enumerate(rows)}
    incidence = [[] for _ in rows]
    for variable, (_, column_rows) in enumerate(columns, start=1):
        if len(column_rows) != 10 or len(set(column_rows)) != 10:
            raise ValueError("bad ten-set column")
        for row in column_rows:
            incidence[row_position[row]].append(variable)
    if any(not variables for variables in incidence):
        raise ValueError("uncovered residual row")

    clauses: list[list[int]] = []
    next_variable = len(columns) + 1
    auxiliary_ranges = []
    for variables in incidence:
        clauses.append(list(variables))
        if len(variables) == 1:
            auxiliary_ranges.append(None)
            continue
        auxiliary = list(range(next_variable, next_variable + len(variables) - 1))
        next_variable += len(auxiliary)
        auxiliary_ranges.append([auxiliary[0], auxiliary[-1]])
        clauses.append([-variables[0], auxiliary[0]])
        for index in range(1, len(variables) - 1):
            clauses.append([-variables[index], auxiliary[index]])
            clauses.append([-auxiliary[index - 1], auxiliary[index]])
            clauses.append([-variables[index], -auxiliary[index - 1]])
        clauses.append([-variables[-1], -auxiliary[-1]])

    with cnf_path.open("w", encoding="ascii") as stream:
        stream.write(f"p cnf {next_variable - 1} {len(clauses)}\n")
        for clause in clauses:
            stream.write(" ".join(map(str, clause)) + " 0\n")
    mapping = {
        "status": "PASS",
        "scope": "Sinz exact-one encoding of one pivot-conditioned K19 instance",
        "graph": str(path),
        "graph_sha256": sha256(path),
        "self_indices": list(self_pair),
        "rows": rows,
        "pair_indices": [index for index, _ in columns],
        "primary_variables": len(columns),
        "auxiliary_variables": next_variable - 1 - len(columns),
        "variables": next_variable - 1,
        "clauses": len(clauses),
        "target_clique": len(rows) // 10,
        "row_degrees": [len(variables) for variables in incidence],
        "auxiliary_ranges": auxiliary_ranges,
        "cnf": str(cnf_path),
        "cnf_sha256": sha256(cnf_path),
    }
    map_path.write_text(json.dumps(mapping, indent=2, sort_keys=True) + "\n",
                        encoding="ascii")
    return mapping


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--graph-dir", required=True, type=Path)
    parser.add_argument("--out-dir", required=True, type=Path)
    parser.add_argument("--manifest", required=True, type=Path)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    records = []
    for graph in sorted(args.graph_dir.glob("*.tsv")):
        cnf = args.out_dir / f"{graph.stem}.cnf"
        mapping = args.out_dir / f"{graph.stem}.map.json"
        records.append(encode(graph, cnf, mapping))
    if not records:
        raise ValueError("no pivot graphs")
    manifest = {
        "status": "PASS",
        "scope": "complete Sinz exact-one CNF bank for row-661 pivot partition",
        "graph_dir": str(args.graph_dir),
        "record_count": len(records),
        "variable_min": min(record["variables"] for record in records),
        "variable_max": max(record["variables"] for record in records),
        "clause_min": min(record["clauses"] for record in records),
        "clause_max": max(record["clauses"] for record in records),
        "records": records,
    }
    args.manifest.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n",
                             encoding="ascii")
    print(json.dumps({key: value for key, value in manifest.items() if key != "records"},
                     indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
