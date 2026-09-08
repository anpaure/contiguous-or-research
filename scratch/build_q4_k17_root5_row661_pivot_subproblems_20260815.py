#!/usr/bin/env python3
"""Partition selected K20 graphs by their unique row-661 column (H100 only)."""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    digest.update(path.read_bytes())
    return digest.hexdigest()


def read_graph(path: Path) -> tuple[tuple[int, int], tuple[int, ...], list[tuple[int, frozenset[int]]]]:
    lines = path.read_text(encoding="ascii").splitlines()
    self_pair = tuple(map(int, lines[0].split("\t")[1:]))
    rows = tuple(map(int, lines[1].split("\t", 1)[1].split(",")))
    columns = []
    for line in lines[3:]:
        if not line:
            continue
        index_text, rows_text = line.split("\t", 1)
        columns.append((int(index_text), frozenset(map(int, rows_text.split(",")))))
    return self_pair, rows, columns


def incidence_components(rows: set[int], columns: list[tuple[int, frozenset[int]]]) -> list[int]:
    parent = {row: row for row in rows}

    def root(row: int) -> int:
        while parent[row] != row:
            parent[row] = parent[parent[row]]
            row = parent[row]
        return row

    def unite(left: int, right: int) -> None:
        left, right = root(left), root(right)
        if left != right:
            parent[right] = left

    for _, column_rows in columns:
        values = list(column_rows)
        for row in values[1:]:
            unite(values[0], row)
    return sorted(Counter(root(row) for row in rows).values())


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--graph", action="append", required=True, type=Path)
    parser.add_argument("--pivot-row", type=int, default=661)
    parser.add_argument("--out-dir", required=True, type=Path)
    parser.add_argument("--report", required=True, type=Path)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)

    branch_records = []
    for graph_path in args.graph:
        self_pair, row_order, columns = read_graph(graph_path)
        rows = set(row_order)
        if len(rows) != 200 or args.pivot_row not in rows:
            raise ValueError("graph does not have the required 200-row pivot interface")
        pivots = [(index, col) for index, col in columns if args.pivot_row in col]
        records = []
        for pivot_index, pivot_rows in pivots:
            remaining = rows - set(pivot_rows)
            residual_columns = [
                (index, col) for index, col in columns
                if index != pivot_index and col.isdisjoint(pivot_rows)
            ]
            incidence = defaultdict(int)
            for _, col in residual_columns:
                for row in col:
                    incidence[row] += 1
            zero_rows = sorted(row for row in remaining if incidence[row] == 0)
            components = incidence_components(remaining, residual_columns)
            immediate_cut = bool(zero_rows) or any(size % 10 for size in components)
            subgraph = args.out_dir / (
                f"self_{self_pair[0]}_{self_pair[1]}.pivot_{pivot_index}.tsv"
            )
            with subgraph.open("w", encoding="ascii") as stream:
                stream.write(f"# self\t{self_pair[0]}\t{self_pair[1]}\n")
                stream.write("# rows\t" + ",".join(map(str, sorted(remaining))) + "\n")
                stream.write("pair_index\trows\n")
                for index, col in residual_columns:
                    stream.write(f"{index}\t" + ",".join(map(str, sorted(col))) + "\n")
            records.append({
                "pivot_pair_index": pivot_index,
                "pivot_rows": sorted(pivot_rows),
                "residual_columns": len(residual_columns),
                "minimum_row_degree": min((incidence[row] for row in remaining), default=0),
                "minimum_rows": sorted(
                    row for row in remaining
                    if incidence[row] == min((incidence[item] for item in remaining), default=0)
                ),
                "zero_rows": zero_rows,
                "component_row_sizes": components,
                "immediate_component_cut": immediate_cut,
                "subgraph": str(subgraph),
                "subgraph_sha256": sha256(subgraph),
            })
        branch_records.append({
            "self_indices": list(self_pair),
            "graph": str(graph_path),
            "graph_sha256": sha256(graph_path),
            "pivot_row": args.pivot_row,
            "pivot_count": len(pivots),
            "immediate_component_cuts": sum(r["immediate_component_cut"] for r in records),
            "residual_column_min": min(r["residual_columns"] for r in records),
            "residual_column_max": max(r["residual_columns"] for r in records),
            "minimum_degree_min": min(r["minimum_row_degree"] for r in records),
            "minimum_degree_max": max(r["minimum_row_degree"] for r in records),
            "component_count_histogram": dict(Counter(
                len(r["component_row_sizes"]) for r in records
            )),
            "pivots": records,
        })

    report = {
        "status": "PASS",
        "scope": "complete unique-row661 pivot partition and static component cuts",
        "branches": branch_records,
    }
    args.report.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="ascii")
    print(json.dumps({
        "status": "PASS",
        "branches": [
            {key: value for key, value in record.items() if key != "pivots"}
            for record in branch_records
        ],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
