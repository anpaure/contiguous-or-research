#!/usr/bin/env python3
"""MILP exact cover by symmetric delta-one mirrored phase paths.

Research diagnostic; run on H100 only.
"""

from __future__ import annotations

import argparse
from collections import Counter
from functools import lru_cache
from itertools import combinations

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import coo_matrix

from research_c8_orbit_phase_normal_form_20260821 import canonical_layers


def key(target):
    return tuple(sorted(target))


def candidates(r, max_routes_per_edge):
    assert r % 2 == 0
    h = r // 2
    ground = frozenset(range(1, 2 * r + 1))
    layer, _, sizes = canonical_layers(r)
    assert len(set(sizes.values())) == 1
    by_phase = {
        phase: tuple(sorted((x for x, value in layer.items() if value == phase), key=key))
        for phase in range(r + 1)
    }
    phase_sets = {phase: set(values) for phase, values in by_phase.items()}
    neighbours = {}
    for phase in range(r):
        for left in by_phase[phase]:
            answer = []
            for deleted in left:
                for added in ground - left:
                    right = frozenset((left - {deleted}) | {added})
                    if right in phase_sets[phase + 1]:
                        answer.append((right, deleted, added))
            neighbours[(phase, left)] = tuple(answer)

    roots = by_phase[0]
    answer = []
    route_count_hist = Counter()
    for P, Q in combinations(roots, 2):
        if len(P ^ Q) != 2:
            continue
        missing = next(iter(P - Q))
        repeated = next(iter(Q - P))
        target = tuple(
            0 if x == missing else 2 if x == repeated else 1
            for x in range(1, 2 * r + 1)
        )
        destination = ground - Q
        routes = []

        def search(phase, current, counts, path):
            if len(routes) >= max_routes_per_edge:
                return
            if phase == r:
                if current == destination and counts == target:
                    routes.append(tuple(path))
                return
            for right, deleted, added in neighbours[(phase, current)]:
                mutable = list(counts)
                mutable[deleted - 1] += 1
                mutable[added - 1] += 1
                if any(mutable[i] > target[i] for i in range(2 * r)):
                    continue
                search(
                    phase + 1,
                    right,
                    tuple(mutable),
                    path + [right],
                )

        search(0, P, (0,) * (2 * r), [P])
        route_count_hist[len(routes)] += 1
        seen_profiles = set()
        for path in routes:
            mate = tuple(ground - path[r - phase] for phase in range(r + 1))
            assert mate[0] == Q and mate[-1] == ground - P
            profile = tuple(
                tuple(sorted((path[phase], mate[phase]), key=key))
                for phase in range(h + 1)
            )
            if any(len(set(pair)) != 2 for pair in profile):
                continue
            if profile in seen_profiles:
                continue
            seen_profiles.add(profile)
            colors = []
            for left, right in zip(path, path[1:]):
                colors.extend((left & right, ground - (left | right)))
            answer.append(
                {
                    "roots": frozenset((P, Q)),
                    "path": path,
                    "mate": mate,
                    "profile": profile,
                    "colors": tuple(colors),
                }
            )
    return by_phase, answer, route_count_hist


def solve(r, max_routes_per_edge, time_limit, require_colors):
    by_phase, routes, route_count_hist = candidates(r, max_routes_per_edge)
    h = r // 2
    ground = frozenset(range(1, 2 * r + 1))
    row_keys = [
        ("V", phase, target)
        for phase in range(h + 1)
        for target in by_phase[phase]
    ]
    if require_colors:
        row_keys += [
            ("C", frozenset(color))
            for color in combinations(sorted(ground), r - 1)
        ]
    row_id = {row: index for index, row in enumerate(row_keys)}
    rows = []
    cols = []
    data = []
    for column, route in enumerate(routes):
        used = []
        for phase, pair in enumerate(route["profile"]):
            used.extend(("V", phase, target) for target in pair)
        if require_colors:
            used.extend(("C", color) for color in route["colors"])
        if len(set(used)) != len(used):
            # A self-collision cannot enter an exact cover.
            continue
        for row in used:
            rows.append(row_id[row])
            cols.append(column)
            data.append(1.0)
    matrix = coo_matrix(
        (data, (rows, cols)), shape=(len(row_keys), len(routes))
    ).tocsr()
    constraint = LinearConstraint(
        matrix, np.ones(len(row_keys)), np.ones(len(row_keys))
    )
    result = milp(
        np.zeros(len(routes)),
        integrality=np.ones(len(routes)),
        bounds=Bounds(np.zeros(len(routes)), np.ones(len(routes))),
        constraints=constraint,
        options={"time_limit": time_limit, "presolve": True},
    )
    selected = []
    if result.x is not None:
        selected = [index for index, value in enumerate(result.x) if value > 0.5]
    answer = {
        "r": r,
        "routes": len(routes),
        "route_count_hist": dict(route_count_hist),
        "constraints": len(row_keys),
        "require_exact_colors": require_colors,
        "status": int(result.status),
        "message": result.message,
        "selected": len(selected),
    }
    if selected:
        assert len(selected) == len(by_phase[0]) // 2
        answer["selected_root_pairs"] = [
            tuple(sorted((key(x) for x in routes[index]["roots"])))
            for index in selected
        ]
        answer["selected_paths"] = [
            tuple(key(x) for x in routes[index]["path"])
            for index in selected
        ]
        if not require_colors:
            color_load = Counter(
                color for index in selected for color in routes[index]["colors"]
            )
            answer["color_support"] = len(color_load)
            answer["color_holes"] = len(row_keys) * 0 + len(
                list(combinations(sorted(ground), r - 1))
            ) - len(color_load)
            answer["color_max_load"] = max(color_load.values())
    return answer


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--r", type=int, nargs="+", default=[2, 4])
    parser.add_argument("--max-routes-per-edge", type=int, default=100_000)
    parser.add_argument("--time-limit", type=float, default=300.0)
    parser.add_argument("--require-colors", action="store_true")
    args = parser.parse_args()
    for r in args.r:
        print(
            "DELTA1_MIRRORED_PHASE_EXACT_COVER",
            solve(r, args.max_routes_per_edge, args.time_limit, args.require_colors),
            flush=True,
        )


if __name__ == "__main__":
    main()
