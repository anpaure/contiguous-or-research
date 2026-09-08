#!/usr/bin/env python3
"""Literal replay of the complete F200 row-pivot campaign (H100 only)."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

sys.path.insert(0, "scratch")
from search_q4_k17_z17_reflection_fixed_face_kissat_20260814 import read_instance


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        while block := stream.read(1 << 20):
            digest.update(block)
    return digest.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--instance", required=True, type=Path)
    parser.add_argument("--patch-report", required=True, type=Path)
    parser.add_argument("--graph-manifest", required=True, type=Path)
    parser.add_argument("--pivot-report", required=True, type=Path)
    parser.add_argument("--solver-source", required=True, type=Path)
    parser.add_argument("--solver-binary", required=True, type=Path)
    parser.add_argument("--results", nargs="+", required=True, type=Path)
    parser.add_argument("--report", required=True, type=Path)
    args = parser.parse_args()

    _, _, _, pair_options = read_instance(str(args.instance))
    patch = json.loads(args.patch_report.read_text(encoding="ascii"))
    assert patch["status"] == "UNKNOWN"
    free_rows = set(patch["free_rows_list"])
    assert len(free_rows) == 200

    graph_manifest = json.loads(args.graph_manifest.read_text(encoding="ascii"))
    assert graph_manifest["status"] == "PASS"
    assert graph_manifest["instance_sha256"] == sha256(args.instance)
    assert set(graph_manifest["free_rows"]) == free_rows
    assert graph_manifest["eligible_pair_columns"] == 6962
    assert graph_manifest["minimum_rows"] == [661]
    assert graph_manifest["minimum_degree"] == 89

    pivot_report = json.loads(args.pivot_report.read_text(encoding="ascii"))
    assert pivot_report["status"] == "PASS"
    assert len(pivot_report["branches"]) == 1
    branch = pivot_report["branches"][0]
    assert branch["self_indices"] == [-1, -1]
    assert branch["pivot_row"] == 661 and branch["pivot_count"] == 89
    pivots = {item["subgraph"]: item for item in branch["pivots"]}
    assert len(pivots) == 89

    records = []
    certificates = []
    seen = set()
    for result_path in args.results:
        result = json.loads(result_path.read_text(encoding="ascii"))
        graph_text = result["graph"]
        assert graph_text in pivots and graph_text not in seen
        seen.add(graph_text)
        assert result["self_indices"] == [-1, -1]
        assert result["residual_rows"] == 190
        assert result["target_clique"] == 19
        assert result["status"] in ("SAT", "UNSAT", "UNKNOWN")

        pivot = pivots[graph_text]
        pivot_index = pivot["pivot_pair_index"]
        pivot_rows = set(pair_options[pivot_index])
        assert pivot_rows == set(pivot["pivot_rows"]) and 661 in pivot_rows
        residual_rows = free_rows - pivot_rows
        assert len(residual_rows) == 190
        expected_pairs = sorted(
            index for index, rows in enumerate(pair_options)
            if set(rows) <= residual_rows
        )

        graph_path = Path(graph_text)
        lines = graph_path.read_text(encoding="ascii").splitlines()
        assert lines[0] == "# self\t-1\t-1"
        graph_rows = set(map(int, lines[1].split("\t", 1)[1].split(",")))
        graph_pairs = []
        for line in lines[3:]:
            if not line:
                continue
            index_text, rows_text = line.split("\t", 1)
            index = int(index_text)
            rows = tuple(map(int, rows_text.split(",")))
            assert rows == tuple(sorted(pair_options[index]))
            graph_pairs.append(index)
        assert graph_rows == residual_rows
        assert graph_pairs == expected_pairs
        assert result["pair_columns"] == len(expected_pairs)

        if result["status"] == "SAT":
            chosen = result["pair_indices"]
            assert len(chosen) == len(set(chosen)) == 19
            assert set(chosen) <= set(expected_pairs)
            loads = {row: 0 for row in free_rows}
            for row in pivot_rows:
                loads[row] += 1
            for index in chosen:
                for row in pair_options[index]:
                    loads[row] += 1
            assert set(loads.values()) == {1}
            certificates.append({
                "pivot_pair_index": pivot_index,
                "pair_indices": chosen,
            })
        else:
            assert result["pair_indices"] == []
        records.append({
            "result": str(result_path),
            "result_sha256": sha256(result_path),
            "graph": graph_text,
            "graph_sha256": sha256(graph_path),
            "pivot_pair_index": pivot_index,
            "status": result["status"],
            "nodes": result["nodes"],
        })

    assert seen == set(pivots)
    report = {
        "status": "PASS",
        "scope": "literal replay of complete F200 row-661 pivot campaign",
        "instance": str(args.instance),
        "instance_sha256": sha256(args.instance),
        "patch_report": str(args.patch_report),
        "patch_report_sha256": sha256(args.patch_report),
        "graph_manifest": str(args.graph_manifest),
        "graph_manifest_sha256": sha256(args.graph_manifest),
        "pivot_report": str(args.pivot_report),
        "pivot_report_sha256": sha256(args.pivot_report),
        "solver_source": str(args.solver_source),
        "solver_source_sha256": sha256(args.solver_source),
        "solver_binary": str(args.solver_binary),
        "solver_binary_sha256": sha256(args.solver_binary),
        "result_count": len(records),
        "status_histogram": {
            status: sum(record["status"] == status for record in records)
            for status in ("SAT", "UNSAT", "UNKNOWN")
        },
        "sat_certificates": certificates,
        "results": records,
    }
    args.report.write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="ascii"
    )
    print(json.dumps({
        "status": "PASS",
        "result_count": len(records),
        "status_histogram": report["status_histogram"],
        "sat_certificates": certificates,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
