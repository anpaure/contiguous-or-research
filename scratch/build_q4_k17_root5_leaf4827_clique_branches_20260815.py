#!/usr/bin/env python3
"""Build the ten exact self-conditioned K20 branch graphs (H100 only)."""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, "scratch")
from search_q4_k17_z17_reflection_fixed_face_kissat_20260814 import read_instance
from search_q4_k17_z17_reflection_vertex_cover_patch_benders_20260814 import (
    selected_vertices,
)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--instance", required=True)
    parser.add_argument("--incumbent", required=True)
    parser.add_argument("--removal-mask", required=True)
    parser.add_argument("--out-dir", required=True)
    parser.add_argument("--manifest", required=True)
    args = parser.parse_args()

    _, _, self_options, pair_options = read_instance(args.instance)
    incumbent = json.loads(Path(args.incumbent).read_text())
    vertices = selected_vertices(self_options, pair_options, incumbent)
    removal = int(args.removal_mask, 0)

    outside = [0] * 680
    removed = []
    for position, vertex in enumerate(vertices):
        if removal >> position & 1:
            removed.append(vertex)
        else:
            for row in vertex[3]:
                outside[row] += 1
    if max(outside) > 1:
        raise ValueError("removal is not a defect vertex cover")
    free_rows = tuple(row for row, load in enumerate(outside) if load == 0)
    free_set = set(free_rows)
    groups = sorted({group for kind, _, group, _ in removed if kind == "self"})
    removed_pairs = sum(kind == "pair" for kind, _, _, _ in removed)
    if len(free_rows) != 4 * len(groups) + 10 * removed_pairs:
        raise ValueError("free-row mass mismatch")
    if len(groups) != 2 or removed_pairs != 20 or len(free_rows) != 208:
        raise ValueError("unexpected root5 F208 profile")

    eligible_self = [
        index for index, (group, rows) in enumerate(self_options)
        if group in groups and set(rows) <= free_set
    ]
    by_group = defaultdict(list)
    for index in eligible_self:
        by_group[self_options[index][0]].append(index)
    eligible_pairs = [
        index for index, rows in enumerate(pair_options) if set(rows) <= free_set
    ]

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    branches = []
    for left in sorted(by_group[groups[0]]):
        for right in sorted(by_group[groups[1]]):
            self_rows = set(self_options[left][1]) | set(self_options[right][1])
            if len(self_rows) != 8:
                continue
            residual_rows = tuple(row for row in free_rows if row not in self_rows)
            residual_set = set(residual_rows)
            pair_indices = [
                index for index in eligible_pairs
                if set(pair_options[index]) <= residual_set
            ]
            path = out_dir / f"self_{left}_{right}.tsv"
            with path.open("w", encoding="ascii") as stream:
                stream.write(f"# self\t{left}\t{right}\n")
                stream.write("# rows\t" + ",".join(map(str, residual_rows)) + "\n")
                stream.write("pair_index\trows\n")
                for index in pair_indices:
                    stream.write(
                        f"{index}\t" + ",".join(map(str, sorted(pair_options[index])))
                        + "\n"
                    )
            branches.append({
                "self_indices": [left, right],
                "self_rows": sorted(self_rows),
                "residual_rows": len(residual_rows),
                "pair_columns": len(pair_indices),
                "graph": str(path),
            })

    if len(branches) != 10:
        raise ValueError(f"expected ten compatible self branches, got {len(branches)}")
    manifest = {
        "status": "PASS",
        "scope": "exact ten-way self conditioning for root5 F208",
        "instance": args.instance,
        "incumbent": args.incumbent,
        "removal_mask_hex": hex(removal),
        "free_rows": list(free_rows),
        "removed_self_groups": groups,
        "removed_pairs": removed_pairs,
        "eligible_self": len(eligible_self),
        "eligible_pairs_before_self_conditioning": len(eligible_pairs),
        "branches": branches,
    }
    Path(args.manifest).write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="ascii"
    )
    print(json.dumps({key: value for key, value in manifest.items()
                      if key not in ("free_rows", "branches")},
                     indent=2, sort_keys=True))
    for branch in branches:
        print(json.dumps(branch, sort_keys=True))


if __name__ == "__main__":
    main()
