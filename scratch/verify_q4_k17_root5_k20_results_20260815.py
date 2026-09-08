#!/usr/bin/env python3
"""Replay root5 K20 branch results against the frozen leaf (H100 only)."""

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
    parser.add_argument("--instance", required=True)
    parser.add_argument("--incumbent", required=True)
    parser.add_argument("--removal-mask", required=True)
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--solver-source", required=True)
    parser.add_argument("--solver-binary", required=True)
    parser.add_argument("--results", nargs="+", required=True)
    parser.add_argument("--report", required=True)
    parser.add_argument("--allow-subset", action="store_true")
    parser.add_argument("--allow-repeat-branches", action="store_true")
    args = parser.parse_args()

    _, _, self_options, pair_options = read_instance(args.instance)
    incumbent = json.loads(Path(args.incumbent).read_text())
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

    manifest = json.loads(Path(args.manifest).read_text())
    if manifest["instance"] != args.instance or manifest["incumbent"] != args.incumbent:
        raise ValueError("manifest input paths do not match replay inputs")
    if int(manifest["removal_mask_hex"], 0) != removal:
        raise ValueError("manifest removal mask mismatch")
    if set(manifest["free_rows"]) != free_rows:
        raise ValueError("manifest free-row set mismatch")
    branches = {tuple(branch["self_indices"]): branch
                for branch in manifest["branches"]}
    records = []
    sat = None
    for result_path in map(Path, args.results):
        result = json.loads(result_path.read_text())
        self_indices = tuple(result["self_indices"])
        if self_indices not in branches:
            raise ValueError("result self branch absent from manifest")
        graph_path = Path(result["graph"])
        if str(graph_path) != branches[self_indices]["graph"]:
            raise ValueError("result graph path does not match manifest branch")
        if result["pair_columns"] != branches[self_indices]["pair_columns"]:
            raise ValueError("result/manifest pair count mismatch")
        if result["residual_rows"] != 200 or result["target_clique"] != 20:
            raise ValueError("result has wrong K20 dimensions")
        if result["status"] not in ("SAT", "UNSAT", "UNKNOWN"):
            raise ValueError("unknown result status")
        residual_rows = free_rows - {
            row for index in self_indices for row in self_options[index][1]
        }
        expected_pairs = sorted(
            index for index, rows in enumerate(pair_options)
            if set(rows) <= residual_rows
        )
        graph_lines = graph_path.read_text().splitlines()
        if len(graph_lines) < 3 or graph_lines[0] != (
            f"# self\t{self_indices[0]}\t{self_indices[1]}"
        ) or not graph_lines[1].startswith("# rows\t"):
            raise ValueError("bad graph header")
        graph_rows = set(map(int, graph_lines[1].split("\t", 1)[1].split(",")))
        graph_pairs = []
        for line in graph_lines[3:]:
            if not line:
                continue
            index_text, rows_text = line.split("\t", 1)
            index = int(index_text)
            rows = tuple(map(int, rows_text.split(",")))
            if rows != tuple(sorted(pair_options[index])):
                raise ValueError("graph column payload disagrees with frozen instance")
            graph_pairs.append(index)
        if graph_rows != residual_rows or graph_pairs != expected_pairs:
            raise ValueError("graph is not the complete self-conditioned pair bank")
        if result["status"] == "SAT":
            pair_indices = result["pair_indices"]
            if len(pair_indices) != len(set(pair_indices)) or len(pair_indices) != 20:
                raise ValueError("SAT result does not contain 20 distinct pairs")
            if not set(pair_indices) <= set(expected_pairs):
                raise ValueError("SAT result uses a pair outside its complete graph")
            loads = {row: 0 for row in free_rows}
            for index in self_indices:
                for row in self_options[index][1]:
                    if row not in loads:
                        raise ValueError("self row outside F208")
                    loads[row] += 1
            for index in pair_indices:
                for row in pair_options[index]:
                    if row not in loads:
                        raise ValueError("pair row outside F208")
                    loads[row] += 1
            if set(loads.values()) != {1}:
                raise ValueError("SAT result is not an exact F208 partition")
            sat = {"self_indices": list(self_indices), "pair_indices": pair_indices}
        elif result["pair_indices"]:
            raise ValueError("non-SAT result contains pair certificate")
        records.append({
            "result": str(result_path),
            "result_sha256": sha256(result_path),
            "graph": str(graph_path),
            "graph_sha256": sha256(graph_path),
            "self_indices": list(self_indices),
            "pair_columns": result["pair_columns"],
            "status": result["status"],
            "nodes": result["nodes"],
        })
    seen = {tuple(record["self_indices"]) for record in records}
    if len(seen) != len(records) and not args.allow_repeat_branches:
        raise ValueError("duplicate self branch in results")
    if not args.allow_subset and (len(records) != 10 or set(branches) != seen):
        raise ValueError("results do not cover all ten self branches")
    report = {
        "status": "PASS",
        "scope": ("literal replay of seeded root5 self-conditioned K20 results"
                  if args.allow_repeat_branches else
                  "literal replay of selected root5 self-conditioned K20 results"
                  if args.allow_subset else
                  "literal replay of all ten root5 self-conditioned K20 results"),
        "instance": args.instance,
        "incumbent": args.incumbent,
        "removal_mask_hex": hex(removal),
        "manifest": args.manifest,
        "manifest_sha256": sha256(Path(args.manifest)),
        "instance_sha256": sha256(Path(args.instance)),
        "incumbent_sha256": sha256(Path(args.incumbent)),
        "solver_source": args.solver_source,
        "solver_source_sha256": sha256(Path(args.solver_source)),
        "solver_binary": args.solver_binary,
        "solver_binary_sha256": sha256(Path(args.solver_binary)),
        "branch_results": records,
        "sat_certificate": sat,
    }
    Path(args.report).write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="ascii"
    )
    print(json.dumps({
        "status": "PASS",
        "branches": len(records),
        "status_histogram": {
            status: sum(record["status"] == status for record in records)
            for status in ("SAT", "UNSAT", "UNKNOWN")
        },
        "sat_certificate": sat,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
