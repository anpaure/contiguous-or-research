#!/usr/bin/env python3
"""Rank incumbent holes by exact inclusion-minimal blocker menus (H100 only)."""

from __future__ import annotations

import argparse
import json
from collections import Counter

from search_q4_k17_z17_reflection_exact_blocker_dag_benders_20260814 import (
    blocker_catalogue,
)
from search_q4_k17_z17_reflection_fixed_face_kissat_20260814 import (
    read_instance,
)
from search_q4_k17_z17_reflection_vertex_cover_patch_benders_20260814 import (
    defect_graph,
    selected_vertices,
)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--instance", required=True)
    parser.add_argument("--incumbent", required=True)
    parser.add_argument("--limit", type=int, default=10)
    args = parser.parse_args()

    _, _, self_options, pair_options = read_instance(args.instance)
    with open(args.incumbent, encoding="ascii") as stream:
        state = json.load(stream)
    vertices = selected_vertices(self_options, pair_options, state)
    loads, edges = defect_graph(vertices)
    assert state["energy"] > 0 and state["energy"] == 2 * len(edges)
    row_selected, _, _, row_menus, _, _ = blocker_catalogue(
        self_options, pair_options, vertices
    )
    assert len(row_selected) == len(row_menus) == 680

    self_degree = [0] * 680
    pair_degree = [0] * 680
    for _, rows in self_options:
        for row in rows:
            self_degree[row] += 1
    for rows in pair_options:
        for row in rows:
            pair_degree[row] += 1
    weights = [4 if kind == "self" else 10 for kind, _, _, _ in vertices]

    holes = []
    for row, load in enumerate(loads):
        if load:
            continue
        menu = row_menus[row]
        assert row_selected[row] == 0 and menu
        cardinalities = [mask.bit_count() for mask in menu]
        masses = [
            sum(weights[position] for position in range(len(vertices))
                if mask >> position & 1)
            for mask in menu
        ]
        holes.append({
            "row": row,
            "minimal_blocker_menus": len(menu),
            "minimum_blocker_vertices": min(cardinalities),
            "minimum_blocker_mass": min(masses),
            "frozen_self_degree": self_degree[row],
            "frozen_pair_degree": pair_degree[row],
        })
    assert len(holes) == state["energy"] // 2
    holes.sort(key=lambda item: (
        item["minimal_blocker_menus"],
        -item["minimum_blocker_vertices"],
        item["frozen_pair_degree"],
        item["row"],
    ))
    minimum_menu = holes[0]["minimal_blocker_menus"]
    print(json.dumps({
        "status": "PASS",
        "energy": state["energy"],
        "holes": len(holes),
        "hardness_definition": (
            "ascending inclusion-minimal blocker-menu count, then descending "
            "minimum blocker vertex count, then ascending frozen pair degree, "
            "then row id"
        ),
        "minimum_menu_size": minimum_menu,
        "all_minimum_menu_rows": [
            item for item in holes
            if item["minimal_blocker_menus"] == minimum_menu
        ],
        "top_hard_rows": holes[:args.limit],
        "all_holes": holes,
        "hole_menu_size_histogram": dict(sorted(Counter(
            item["minimal_blocker_menus"] for item in holes
        ).items())),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
