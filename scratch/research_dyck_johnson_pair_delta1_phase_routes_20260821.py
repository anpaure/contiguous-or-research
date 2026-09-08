#!/usr/bin/env python3
"""Dyck-root Johnson pairs and delta-one Chung--Feller phase routes.

Research diagnostic; substantive runs are on H100 only.
"""

from __future__ import annotations

import argparse
from collections import Counter
from functools import lru_cache
from itertools import combinations

import networkx as nx

from research_c8_orbit_phase_normal_form_20260821 import canonical_layers


def key(target):
    return tuple(sorted(target))


def phase_neighbours(layer, by_phase, r):
    ground = frozenset(range(1, 2 * r + 1))
    result = {}
    for phase in range(r):
        right_set = set(by_phase[phase + 1])
        for left in by_phase[phase]:
            answer = []
            for deleted in left:
                for added in ground - left:
                    right = frozenset((left - {deleted}) | {added})
                    if right in right_set:
                        answer.append((right, deleted, added))
            result[(phase, left)] = tuple(answer)
    return result


def one_route(P, Q, neighbours, r):
    ground = frozenset(range(1, 2 * r + 1))
    assert len(P ^ Q) == 2
    u = next(iter(P - Q))
    v = next(iter(Q - P))
    destination = ground - Q

    for missing, repeated in ((u, v), (v, u)):
        target_count = tuple(
            0 if x == missing else 2 if x == repeated else 1
            for x in range(1, 2 * r + 1)
        )

        @lru_cache(maxsize=None)
        def search(phase, current, counts):
            current = frozenset(current)
            if phase == r:
                return () if current == destination and counts == target_count else None
            for right, deleted, added in neighbours[(phase, current)]:
                mutable = list(counts)
                mutable[deleted - 1] += 1
                mutable[added - 1] += 1
                if any(mutable[i] > target_count[i] for i in range(2 * r)):
                    continue
                suffix = search(phase + 1, tuple(sorted(right)), tuple(mutable))
                if suffix is not None:
                    return ((right, deleted, added),) + suffix
            return None

        route = search(0, tuple(sorted(P)), (0,) * (2 * r))
        if route is not None:
            path = (P,) + tuple(item[0] for item in route)
            return path, missing, repeated
    return None


def audit(r, enumerate_all_edges):
    layer, _, sizes = canonical_layers(r)
    assert len(set(sizes.values())) == 1
    by_phase = {
        phase: tuple(sorted((x for x, value in layer.items() if value == phase), key=key))
        for phase in range(r + 1)
    }
    roots = by_phase[0]
    root_graph = nx.Graph()
    root_graph.add_nodes_from(roots)
    for P, Q in combinations(roots, 2):
        if len(P ^ Q) == 2:
            root_graph.add_edge(P, Q)
    matching = nx.algorithms.matching.max_weight_matching(root_graph, maxcardinality=True)
    perfect = 2 * len(matching) == len(roots)
    neighbours = phase_neighbours(layer, by_phase, r)

    tested_edges = list(root_graph.edges()) if enumerate_all_edges else list(matching)
    route_count = 0
    missing_repeat_hist = Counter()
    failures = []
    route_examples = []
    for P, Q in tested_edges:
        answer = one_route(P, Q, neighbours, r)
        if answer is None:
            failures.append((key(P), key(Q)))
            continue
        path, missing, repeated = answer
        route_count += 1
        missing_repeat_hist[(missing in P, repeated in P)] += 1
        if len(route_examples) < 3:
            route_examples.append(
                {
                    "P": key(P),
                    "Q": key(Q),
                    "missing": missing,
                    "repeated": repeated,
                    "path": tuple(key(x) for x in path),
                }
            )
    return {
        "r": r,
        "Cat_r": len(roots),
        "root_edges": root_graph.number_of_edges(),
        "isolated_roots": sum(root_graph.degree(x) == 0 for x in roots),
        "maximum_matching": len(matching),
        "perfect_matching": perfect,
        "tested_edges": len(tested_edges),
        "delta1_routes": route_count,
        "failures": len(failures),
        "failure_examples": failures[:5],
        "missing_repeat_shore_hist": {str(k): v for k, v in missing_repeat_hist.items()},
        "route_examples": route_examples,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--r", type=int, nargs="+", default=[2, 4, 6])
    parser.add_argument("--all-edges", action="store_true")
    args = parser.parse_args()
    for r in args.r:
        print(
            "DYCK_JOHNSON_DELTA1_PHASE_ROUTES",
            audit(r, args.all_edges),
            flush=True,
        )


if __name__ == "__main__":
    main()
