#!/usr/bin/env python3
"""Independent replay of targeted q4/k17 reflection-pair outputs (H100)."""

from __future__ import annotations

import argparse
import itertools
import json
import math
from collections import Counter

from search_q4_k17_z17_quotient_exact_cover_20260814 import (
    K,
    canonical_orbit_mask,
    deck_masks,
    owner_orbits,
    subset_mask,
)
from search_q4_k17_z17_reflection_exact_blocker_dag_benders_20260814 import (
    blocker_catalogue,
)
from search_q4_k17_z17_reflection_fixed_face_kissat_20260814 import (
    read_instance,
)
from search_q4_k17_z17_reflection_invariant_owner_cover_20260814 import (
    reflection_action,
)
from search_q4_k17_z17_reflection_vertex_cover_patch_benders_20260814 import (
    defect_graph,
    selected_vertices,
)


def multiply_mask(mask, multiplier):
    return canonical_orbit_mask(subset_mask(
        (multiplier * value) % K
        for value in range(K) if mask >> value & 1
    ))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--instance", required=True)
    parser.add_argument("--incumbent", required=True)
    parser.add_argument("--hard-report", required=True)
    parser.add_argument("outputs", nargs="+")
    args = parser.parse_args()

    _, _, self_options, pair_options = read_instance(args.instance)
    with open(args.incumbent, encoding="ascii") as stream:
        state = json.load(stream)
    vertices = selected_vertices(self_options, pair_options, state)
    loads, edges = defect_graph(vertices)
    assert state["energy"] == 86 == 2 * len(edges)
    _, _, _, row_menus, _, _ = blocker_catalogue(
        self_options, pair_options, vertices
    )
    holes = [row for row, load in enumerate(loads) if load == 0]
    assert len(holes) == 43

    pair_degrees = [0] * 680
    frozen = set()
    for rows in pair_options:
        key = tuple(sorted(rows))
        assert len(key) == len(set(key)) == 10
        frozen.add(key)
        for row in key:
            pair_degrees[row] += 1
    assert len(frozen) == len(pair_options) == 27008
    hard_order = sorted(
        holes,
        key=lambda row: (
            len(row_menus[row]),
            -min(mask.bit_count() for mask in row_menus[row]),
            pair_degrees[row],
            row,
        ),
    )
    assert hard_order[:3] == [595, 484, 631]
    with open(args.hard_report, encoding="ascii") as stream:
        hard_report = json.load(stream)
    assert [item["row"] for item in hard_report["top_hard_rows"][:3]] == hard_order[:3]

    representatives, orbit_index = owner_orbits()
    reflection = reflection_action(representatives, orbit_index)
    nonfixed = [owner for owner in range(1430) if owner < reflection[owner]]
    assert len(nonfixed) == 680
    reduced = {}
    for row, owner in enumerate(nonfixed):
        reduced[owner] = reduced[reflection[owner]] = row

    expected_raw = math.comb(9, 5) * math.factorial(4) * (
        math.factorial(8) // math.factorial(2)
    )
    assert expected_raw == 60_963_840
    summaries = []
    target_masks = {}
    replayed_samples = 0
    for path in args.outputs:
        with open(path, encoding="ascii") as stream:
            report = json.load(stream)
        assert report["status"] == "PASS"
        row = report["target_row"]
        assert row in hard_order[:3]
        target = nonfixed[row]
        assert report["target_owner_id"] == target
        assert report["target_owner_mask"] == representatives[target]
        target_masks[row] = representatives[target]
        assert report["raw_parameter_count"] == expected_raw
        assert report["allowed_filter"] is None
        assert report["unique_pair_masks"] == (
            report["regenerated_frozen_target_masks"]
            + report["genuinely_new_pair_masks"]
        )
        frozen_target = sum(row in key for key in frozen)
        assert frozen_target == pair_degrees[row]
        assert report["frozen_unique_target_masks"] == frozen_target
        assert report["frozen_unique_target_allowed_masks"] == frozen_target
        assert report["regenerated_frozen_target_masks"] == frozen_target

        coverage = {int(key): value
                    for key, value in report["new_row_coverage"].items()}
        assert set(coverage) == set(range(680))
        assert coverage[row] == report["genuinely_new_pair_masks"]
        hole_coverage = {hole: coverage[hole] for hole in holes}
        assert all(hole_coverage.values())

        for sample in report["samples"]:
            replayed_samples += 1
            core = tuple(sample["core"])
            order = tuple(sample["order"])
            assert len(core) == len(set(core)) == 5
            assert len(order) == len(set(order)) == 10
            assert not (set(core) & set(order))
            owners = deck_masks(core, order)
            ids = tuple(
                orbit_index[canonical_orbit_mask(owner)] for owner in owners
            )
            assert list(ids) == sample["owner_ids"]
            assert len(set(ids)) == 10
            assert target in ids
            assert not (set(ids) & {reflection[owner] for owner in ids})
            rows = tuple(sorted(reduced[owner] for owner in ids))
            assert list(rows) == sample["rows"]
            assert len(set(rows)) == 10 and row in rows
            assert sample["frozen"] == (rows in frozen)

        summaries.append({
            "row": row,
            "minimal_blocker_menus": len(row_menus[row]),
            "minimum_blocker_vertices": min(
                mask.bit_count() for mask in row_menus[row]
            ),
            "frozen_pair_degree": pair_degrees[row],
            "raw_parameter_count": report["raw_parameter_count"],
            "quotient_simple_raw": report["quotient_simple_raw"],
            "reflection_disjoint_raw": report["reflection_disjoint_raw"],
            "unique_pair_masks": report["unique_pair_masks"],
            "genuinely_new_pair_masks": report["genuinely_new_pair_masks"],
            "covered_e86_holes": len(hole_coverage),
            "minimum_nontarget_hole_coverage": min(
                value for hole, value in hole_coverage.items() if hole != row
            ),
            "maximum_nontarget_hole_coverage": max(
                value for hole, value in hole_coverage.items() if hole != row
            ),
        })

    assert sorted(target_masks) == sorted(hard_order[:3])
    multiplier_links = {}
    for source, target in itertools.permutations(hard_order[:3], 2):
        multipliers = [
            multiplier for multiplier in range(1, K)
            if orbit_index[multiply_mask(target_masks[source], multiplier)]
            in (nonfixed[target], reflection[nonfixed[target]])
        ]
        assert len(multipliers) == 2
        multiplier_links[f"{source}->{target}"] = multipliers

    summaries.sort(key=lambda item: hard_order.index(item["row"]))
    assert len({item["unique_pair_masks"] for item in summaries}) == 1
    assert len({item["genuinely_new_pair_masks"] for item in summaries}) == 1
    print(json.dumps({
        "status": "PASS",
        "e86_holes": len(holes),
        "hard_rows": hard_order[:3],
        "raw_parameter_formula": "C(9,5)*4!*P(8,6)",
        "raw_parameter_count": expected_raw,
        "summaries": summaries,
        "hard_rows_share_multiplier_orbit": True,
        "multiplier_links": multiplier_links,
        "sample_witnesses_replayed": replayed_samples,
        "scope": (
            "independent reconstruction of E86 hardness, frozen pair masks, "
            "sampled physical witnesses, reflection disjointness, and all-43 "
            "hole coverage; completeness of the C++ enumeration is symbolic"
        ),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
