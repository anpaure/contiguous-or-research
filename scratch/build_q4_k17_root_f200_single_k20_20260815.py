#!/usr/bin/env python3
"""Build the exact single K20 graph for a no-self F200 removal patch."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, "scratch")
from search_q4_k17_z17_reflection_fixed_face_kissat_20260814 import read_instance
from search_q4_k17_z17_reflection_vertex_cover_patch_benders_20260814 import selected_vertices


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--instance", required=True)
    parser.add_argument("--incumbent", required=True)
    parser.add_argument("--removal-mask", required=True)
    parser.add_argument("--graph", required=True)
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
    removed_groups = sorted({group for kind, _, group, _ in removed
                             if kind == "self"})
    removed_pairs = sum(kind == "pair" for kind, _, _, _ in removed)
    if removed_groups or removed_pairs != 20 or len(free_rows) != 200:
        raise ValueError("expected no-self/20-pair/F200 removal profile")
    eligible_pairs = [index for index, rows in enumerate(pair_options)
                      if set(rows) <= free_set]

    with open(args.graph, "w", encoding="ascii") as stream:
        stream.write("# self\t-1\t-1\n")
        stream.write("# rows\t" + ",".join(map(str, free_rows)) + "\n")
        stream.write("pair_index\trows\n")
        for index in eligible_pairs:
            stream.write(f"{index}\t" + ",".join(
                map(str, sorted(pair_options[index]))) + "\n")
    manifest = {
        "status": "PASS",
        "scope": "exact no-self K20 graph for one complete F200 leaf",
        "instance": args.instance,
        "incumbent": args.incumbent,
        "removal_mask_hex": hex(removal),
        "removed_pairs": removed_pairs,
        "removed_self_groups": removed_groups,
        "free_rows": list(free_rows),
        "pair_columns": len(eligible_pairs),
        "graph": args.graph,
    }
    Path(args.manifest).write_text(json.dumps(manifest, indent=2,
                                             sort_keys=True) + "\n")
    print(json.dumps({key: value for key, value in manifest.items()
                      if key != "free_rows"}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
