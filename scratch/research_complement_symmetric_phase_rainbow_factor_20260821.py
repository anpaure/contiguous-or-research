#!/usr/bin/env python3
"""MILP diagnostic for complement-symmetric two-sided-rainbow phase factors.

For even r, choose the first r/2 transition matchings.  Mirror them by
complement and time reversal.  An edge e=(X,X') consumes the two q1 colors
T=X cap X' and (X union X')^c.  Exact coverage of these color pairs gives
both q1 color shores after mirroring, while symmetry forces endpoint
complement monodromy.  Intended execution environment: H100 only.
"""

from __future__ import annotations

import argparse
from collections import Counter
from itertools import combinations
from math import comb

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import coo_matrix

from research_c8_orbit_phase_normal_form_20260821 import canonical_layers


def candidates(r):
    assert r % 2 == 0
    layer, _, layer_sizes = canonical_layers(r)
    ground = frozenset(range(1, 2 * r + 1))
    half = r // 2
    edges = []
    for left, phase in layer.items():
        if phase >= half:
            continue
        for drop in left:
            for add in ground - left:
                right = frozenset((left - {drop}) | {add})
                if layer[right] != phase + 1:
                    continue
                lower = left & right
                mirror_lower = ground - (left | right)
                assert len(lower) == len(mirror_lower) == r - 1
                assert lower != mirror_lower
                edges.append((phase, left, right, lower, mirror_lower))
    assert set(layer_sizes.values()) == {comb(2 * r, r) // (r + 1)}
    return ground, layer, edges


def solve(r, time_limit):
    ground, layer, edges = candidates(r)
    half = r // 2
    roots = sorted(
        ((phase, target) for target, phase in layer.items() if phase < half),
        key=lambda item: (item[0], tuple(sorted(item[1]))),
    )
    arrivals = sorted(
        ((phase, target) for target, phase in layer.items() if 1 <= phase <= half),
        key=lambda item: (item[0], tuple(sorted(item[1]))),
    )
    colors = [frozenset(x) for x in combinations(sorted(ground), r - 1)]
    row_keys = (
        [("R",) + item for item in roots]
        + [("L",) + item for item in arrivals]
        + [("C", color) for color in colors]
    )
    row_id = {key: i for i, key in enumerate(row_keys)}
    matrix_rows = []
    matrix_cols = []
    matrix_data = []
    for column, (phase, left, right, color1, color2) in enumerate(edges):
        keys = (
            ("R", phase, left),
            ("L", phase + 1, right),
            ("C", color1),
            ("C", color2),
        )
        assert len(set(keys)) == 4
        for key in keys:
            matrix_rows.append(row_id[key])
            matrix_cols.append(column)
            matrix_data.append(1.0)
    matrix = coo_matrix(
        (matrix_data, (matrix_rows, matrix_cols)),
        shape=(len(row_keys), len(edges)),
    ).tocsr()
    constraint = LinearConstraint(matrix, np.ones(len(row_keys)), np.ones(len(row_keys)))
    result = milp(
        np.zeros(len(edges)),
        integrality=np.ones(len(edges)),
        bounds=Bounds(np.zeros(len(edges)), np.ones(len(edges))),
        constraints=constraint,
        options={"time_limit": time_limit, "presolve": True},
    )
    answer = {
        "r": r,
        "variables": len(edges),
        "constraints": len(row_keys),
        "status": int(result.status),
        "message": result.message,
        "success": bool(result.success),
    }
    if not result.success:
        return answer
    selected = [edge for edge, value in zip(edges, result.x) if value > 0.5]
    assert len(selected) == len(colors) // 2

    transition = {}
    lower_count = Counter()
    upper_count = Counter()
    for phase, left, right, lower, mirror_lower in selected:
        transition[(phase, left)] = right
        lower_count[lower] += 1
        lower_count[mirror_lower] += 1
        upper = left | right
        mirror_upper = ground - lower
        upper_count[upper] += 1
        upper_count[mirror_upper] += 1

        mirror_phase = r - 1 - phase
        mirror_left = ground - right
        mirror_right = ground - left
        transition[(mirror_phase, mirror_left)] = mirror_right

    assert set(lower_count.values()) == {1} and len(lower_count) == len(colors)
    upper_colors = comb(2 * r, r + 1)
    assert set(upper_count.values()) == {1} and len(upper_count) == upper_colors
    assert len(transition) == r * comb(2 * r, r) // (r + 1)

    roots0 = [target for target, phase in layer.items() if phase == 0]
    for root in roots0:
        target = root
        for phase in range(r):
            target = transition[(phase, target)]
        assert target == ground - root
    answer.update(
        {
            "selected_half_edges": len(selected),
            "lower_colors": len(lower_count),
            "upper_colors": len(upper_count),
            "root_paths": len(roots0),
            "verified_complement_monodromy": True,
        }
    )
    return answer


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--r", type=int, nargs="+", default=[2, 4, 6])
    parser.add_argument("--time-limit", type=float, default=300.0)
    args = parser.parse_args()
    for r in args.r:
        print("COMPLEMENT_SYMMETRIC_PHASE_RAINBOW", solve(r, args.time_limit), flush=True)


if __name__ == "__main__":
    main()
