#!/usr/bin/env python3
"""Classify the multiplier -1 quotient of a frozen Z17 owner pool.

Run only on H100.  This is a structural audit, not a cover solver.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter

import sys

sys.path.insert(0, "scratch")
from search_q4_k17_z17_quotient_exact_cover_20260814 import (
    K,
    canonical_orbit_mask,
    owner_orbits,
)


def reflect_mask(mask: int) -> int:
    reflected = 0
    for value in range(K):
        if mask >> value & 1:
            reflected |= 1 << ((-value) % K)
    return canonical_orbit_mask(reflected)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--map", required=True)
    args = parser.parse_args()
    data = json.load(open(args.map, encoding="utf-8"))
    representatives, orbit_index = owner_orbits()
    assert len(representatives) == data["owner_orbits"] == 1430

    reflection = tuple(
        orbit_index[reflect_mask(mask)] for mask in representatives
    )
    assert all(reflection[reflection[v]] == v for v in range(1430))
    fixed_vertices = {v for v in range(1430) if reflection[v] == v}
    vertex_orbits = sum(
        1 for v in range(1430) if v <= reflection[v]
    )

    candidates = data["candidates"]
    edge_index = {
        tuple(candidate["edge"]): index
        for index, candidate in enumerate(candidates)
    }
    assert len(edge_index) == len(candidates)
    partner = []
    missing = []
    for index, candidate in enumerate(candidates):
        reflected_edge = tuple(sorted(reflection[v] for v in candidate["edge"]))
        mate = edge_index.get(reflected_edge)
        partner.append(mate)
        if mate is None:
            missing.append(index)
    assert not missing
    assert all(partner[partner[i]] == i for i in range(len(candidates)))

    self_columns = [i for i, mate in enumerate(partner) if mate == i]
    paired_orbits = [
        (i, mate) for i, mate in enumerate(partner)
        if i < mate
    ]
    overlapping_pairs = [
        (i, mate) for i, mate in paired_orbits
        if set(candidates[i]["edge"]) & set(candidates[mate]["edge"])
    ]
    usable_pairs = [
        (i, mate) for i, mate in paired_orbits
        if not (set(candidates[i]["edge"]) & set(candidates[mate]["edge"]))
    ]

    fixed_coverage = Counter()
    fixed_signatures = Counter()
    for index in self_columns:
        covered = tuple(sorted(set(candidates[index]["edge"]) & fixed_vertices))
        fixed_coverage.update(covered)
        fixed_signatures[len(covered)] += 1

    uncovered_fixed = sorted(fixed_vertices - set(fixed_coverage))
    print(json.dumps({
        "status": "PASS",
        "map": args.map,
        "owner_vertices": 1430,
        "fixed_owner_vertices": len(fixed_vertices),
        "owner_reflection_orbits": vertex_orbits,
        "columns": len(candidates),
        "self_reflecting_columns": len(self_columns),
        "paired_column_orbits": len(paired_orbits),
        "overlapping_paired_orbits_unusable_in_invariant_cover": len(overlapping_pairs),
        "usable_paired_orbits": len(usable_pairs),
        "self_column_fixed_vertex_histogram": dict(sorted(fixed_signatures.items())),
        "fixed_vertex_min_self_degree": min(fixed_coverage.values(), default=0),
        "fixed_vertex_max_self_degree": max(fixed_coverage.values(), default=0),
        "uncovered_fixed_vertices": uncovered_fixed,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
