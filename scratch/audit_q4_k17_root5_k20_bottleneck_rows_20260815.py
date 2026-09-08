#!/usr/bin/env python3
"""Exact row-degree priorities for selected root5 K20 branches (H100 only)."""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import defaultdict
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
        index_text, row_text = line.split("\t", 1)
        columns.append((int(index_text), frozenset(map(int, row_text.split(",")))))
    return self_pair, rows, columns


def branch_map(manifest: dict) -> dict[tuple[int, int], Path]:
    return {
        tuple(branch["self_indices"]): Path(branch["graph"])
        for branch in manifest["branches"]
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", required=True, type=Path)
    parser.add_argument("--previous-manifest", type=Path)
    parser.add_argument("--self-pair", action="append", required=True)
    parser.add_argument("--report", required=True, type=Path)
    args = parser.parse_args()

    manifest = json.loads(args.manifest.read_text(encoding="ascii"))
    graphs = branch_map(manifest)
    previous_graphs = None
    if args.previous_manifest:
        previous_graphs = branch_map(json.loads(
            args.previous_manifest.read_text(encoding="ascii")
        ))

    requested = []
    for text in args.self_pair:
        pair = tuple(map(int, text.split(",")))
        if len(pair) != 2 or pair not in graphs:
            raise ValueError(f"unknown self pair {text}")
        requested.append(pair)

    records = []
    for self_pair in requested:
        graph_path = graphs[self_pair]
        parsed_pair, rows, columns = read_graph(graph_path)
        if parsed_pair != self_pair or len(rows) != 200 or len(set(rows)) != 200:
            raise ValueError("malformed current graph")
        incidence: dict[int, list[int]] = defaultdict(list)
        for index, column_rows in columns:
            for row in column_rows:
                incidence[row].append(index)
        if set(incidence) != set(rows):
            raise ValueError("current graph has an uncovered row")

        old_degree = {row: 0 for row in rows}
        previous_columns = 0
        previous_graph_sha = None
        if previous_graphs is not None:
            old_path = previous_graphs[self_pair]
            old_pair, old_rows, old_columns = read_graph(old_path)
            if old_pair != self_pair or set(old_rows) != set(rows):
                raise ValueError("previous graph has different branch rows")
            previous_columns = len(old_columns)
            previous_graph_sha = sha256(old_path)
            for _, column_rows in old_columns:
                for row in column_rows:
                    old_degree[row] += 1

        ranked = sorted(rows, key=lambda row: (len(incidence[row]), row))
        degrees = [len(incidence[row]) for row in rows]
        minimum = min(degrees)
        bottom = [
            {
                "row": row,
                "degree": len(incidence[row]),
                "added_degree": len(incidence[row]) - old_degree[row],
            }
            for row in ranked[:20]
        ]
        records.append({
            "self_indices": list(self_pair),
            "graph": str(graph_path),
            "graph_sha256": sha256(graph_path),
            "pair_columns": len(columns),
            "previous_pair_columns": previous_columns,
            "previous_graph_sha256": previous_graph_sha,
            "minimum_row_degree": minimum,
            "minimum_rows": [row for row in rows if len(incidence[row]) == minimum],
            "canonical_branch_row": ranked[0],
            "canonical_branch_options": len(incidence[ranked[0]]),
            "degree_sum": sum(degrees),
            "degree_min": minimum,
            "degree_max": max(degrees),
            "bottom_twenty_rows": bottom,
        })

    report = {
        "status": "PASS",
        "scope": "exact current-pool pair-column incidence degrees for selected self-conditioned K20 branches",
        "manifest": str(args.manifest),
        "manifest_sha256": sha256(args.manifest),
        "previous_manifest": str(args.previous_manifest) if args.previous_manifest else None,
        "previous_manifest_sha256": sha256(args.previous_manifest) if args.previous_manifest else None,
        "branches": records,
    }
    args.report.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="ascii")
    print(json.dumps({
        "status": "PASS",
        "branches": [
            {
                "self_indices": record["self_indices"],
                "pair_columns": record["pair_columns"],
                "minimum_row_degree": record["minimum_row_degree"],
                "minimum_rows": record["minimum_rows"],
                "bottom_twenty_rows": record["bottom_twenty_rows"],
            }
            for record in records
        ],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
