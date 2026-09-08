#!/usr/bin/env python3
"""Literal replay for row-661 pivot-subproblem results (H100 only)."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

sys.path.insert(0, "scratch")
from search_q4_k17_z17_reflection_fixed_face_kissat_20260814 import read_instance
from search_q4_k17_z17_reflection_vertex_cover_patch_benders_20260814 import (
    selected_vertices,
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        while block := stream.read(1 << 20):
            digest.update(block)
    return digest.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--instance", required=True, type=Path)
    parser.add_argument("--incumbent", required=True, type=Path)
    parser.add_argument("--removal-mask", required=True)
    parser.add_argument("--manifest", required=True, type=Path)
    parser.add_argument("--pivot-report", required=True, type=Path)
    parser.add_argument("--solver-source", required=True, type=Path)
    parser.add_argument("--solver-binary", required=True, type=Path)
    parser.add_argument("--results", nargs="+", required=True, type=Path)
    parser.add_argument("--report", required=True, type=Path)
    parser.add_argument("--allow-subset", action="store_true")
    args = parser.parse_args()

    _, _, self_options, pair_options = read_instance(str(args.instance))
    incumbent = json.loads(args.incumbent.read_text(encoding="ascii"))
    vertices = selected_vertices(self_options, pair_options, incumbent)
    removal = int(args.removal_mask, 0)
    outside = [0] * 680
    for position, vertex in enumerate(vertices):
        if removal >> position & 1:
            continue
        for row in vertex[3]:
            outside[row] += 1
    free_rows = {row for row, load in enumerate(outside) if load == 0}
    if len(free_rows) != 208 or max(outside) > 1:
        raise ValueError("bad frozen F208 state")

    manifest = json.loads(args.manifest.read_text(encoding="ascii"))
    if manifest["instance"] != str(args.instance):
        raise ValueError("manifest instance mismatch")
    if int(manifest["removal_mask_hex"], 0) != removal:
        raise ValueError("manifest removal mismatch")
    branches = {tuple(branch["self_indices"]): branch
                for branch in manifest["branches"]}

    pivot_report = json.loads(args.pivot_report.read_text(encoding="ascii"))
    pivots = {}
    for branch in pivot_report["branches"]:
        self_pair = tuple(branch["self_indices"])
        if self_pair not in branches:
            raise ValueError("pivot branch absent from manifest")
        for pivot in branch["pivots"]:
            graph = pivot["subgraph"]
            if graph in pivots:
                raise ValueError("duplicate pivot subgraph")
            pivots[graph] = (self_pair, pivot)

    records = []
    certificates = []
    seen_graphs = set()
    for result_path in args.results:
        result = json.loads(result_path.read_text(encoding="ascii"))
        graph_text = result["graph"]
        if graph_text not in pivots or graph_text in seen_graphs:
            raise ValueError("unknown or duplicate result graph")
        seen_graphs.add(graph_text)
        self_pair, pivot = pivots[graph_text]
        if tuple(result["self_indices"]) != self_pair:
            raise ValueError("result self pair mismatch")
        if result["residual_rows"] != 190 or result["target_clique"] != 19:
            raise ValueError("result has wrong K19 dimensions")
        if result["status"] not in ("SAT", "UNSAT", "UNKNOWN"):
            raise ValueError("bad result status")

        pivot_index = pivot["pivot_pair_index"]
        pivot_rows = set(pair_options[pivot_index])
        if pivot_rows != set(pivot["pivot_rows"]) or 661 not in pivot_rows:
            raise ValueError("pivot payload mismatch")
        self_rows = {
            row for index in self_pair for row in self_options[index][1]
        }
        residual_rows = free_rows - self_rows - pivot_rows
        if len(residual_rows) != 190:
            raise ValueError("bad residual-row mass")
        expected_pairs = sorted(
            index for index, rows in enumerate(pair_options)
            if set(rows) <= residual_rows
        )
        graph_path = Path(graph_text)
        lines = graph_path.read_text(encoding="ascii").splitlines()
        graph_rows = set(map(int, lines[1].split("\t", 1)[1].split(",")))
        graph_pairs = []
        for line in lines[3:]:
            if not line:
                continue
            index_text, rows_text = line.split("\t", 1)
            index = int(index_text)
            rows = tuple(map(int, rows_text.split(",")))
            if rows != tuple(sorted(pair_options[index])):
                raise ValueError("subgraph column payload mismatch")
            graph_pairs.append(index)
        if graph_rows != residual_rows or graph_pairs != expected_pairs:
            raise ValueError("subgraph is not the complete pivot-conditioned bank")
        if result["pair_columns"] != len(expected_pairs):
            raise ValueError("result pair-column count mismatch")

        if result["status"] == "SAT":
            chosen = result["pair_indices"]
            if len(chosen) != 19 or len(set(chosen)) != 19:
                raise ValueError("SAT result does not have 19 distinct pairs")
            if not set(chosen) <= set(expected_pairs):
                raise ValueError("SAT result uses pair outside subgraph")
            loads = {row: 0 for row in free_rows}
            for index in self_pair:
                for row in self_options[index][1]:
                    loads[row] += 1
            for row in pivot_rows:
                loads[row] += 1
            for index in chosen:
                for row in pair_options[index]:
                    loads[row] += 1
            if set(loads.values()) != {1}:
                raise ValueError("pivot SAT result is not an exact F208 patch")
            certificates.append({
                "self_indices": list(self_pair),
                "pivot_pair_index": pivot_index,
                "pair_indices": chosen,
            })
        elif result["pair_indices"]:
            raise ValueError("non-SAT result contains a witness")
        records.append({
            "result": str(result_path),
            "result_sha256": sha256(result_path),
            "graph": graph_text,
            "graph_sha256": sha256(graph_path),
            "self_indices": list(self_pair),
            "pivot_pair_index": pivot_index,
            "status": result["status"],
            "nodes": result["nodes"],
        })

    if not args.allow_subset and seen_graphs != set(pivots):
        raise ValueError("results do not cover the full pivot partition")
    report = {
        "status": "PASS",
        "scope": "literal replay of row-661 pivot-subproblem results",
        "instance": str(args.instance),
        "instance_sha256": sha256(args.instance),
        "incumbent": str(args.incumbent),
        "incumbent_sha256": sha256(args.incumbent),
        "removal_mask_hex": hex(removal),
        "manifest": str(args.manifest),
        "manifest_sha256": sha256(args.manifest),
        "pivot_report": str(args.pivot_report),
        "pivot_report_sha256": sha256(args.pivot_report),
        "solver_source": str(args.solver_source),
        "solver_source_sha256": sha256(args.solver_source),
        "solver_binary": str(args.solver_binary),
        "solver_binary_sha256": sha256(args.solver_binary),
        "result_count": len(records),
        "results": records,
        "sat_certificates": certificates,
    }
    args.report.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n",
                           encoding="ascii")
    print(json.dumps({
        "status": "PASS",
        "result_count": len(records),
        "status_histogram": {
            status: sum(record["status"] == status for record in records)
            for status in ("SAT", "UNSAT", "UNKNOWN")
        },
        "sat_certificates": certificates,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
