#!/usr/bin/env python3
"""Random first-half phase matchings and their mirrored double-cycle recuts.

Research-only diagnostic; run on H100.
"""

from __future__ import annotations

import argparse
import random
from collections import Counter

import networkx as nx

from research_c8_orbit_phase_normal_form_20260821 import canonical_layers
from research_mirrored_double_cycle_recut_20260821 import (
    induced_two_wreath_factors,
    lift_johnson_path,
)


def random_bijection(lefts, rights, rng):
    graph = nx.Graph()
    left_nodes = [(0, x) for x in lefts]
    right_nodes = [(1, y) for y in rights]
    graph.add_nodes_from(left_nodes, bipartite=0)
    graph.add_nodes_from(right_nodes, bipartite=1)
    for x in lefts:
        for y in rights:
            if len(x ^ y) == 2:
                graph.add_edge((0, x), (1, y), weight=rng.random())
    matching = nx.algorithms.matching.max_weight_matching(
        graph, maxcardinality=True, weight="weight"
    )
    assert len(matching) == len(lefts)
    answer = {}
    for a, b in matching:
        if a[0] == 1:
            a, b = b, a
        assert a[0] == 0 and b[0] == 1
        answer[a[1]] = b[1]
    return answer


def random_pairs(r, rng):
    layer, _, sizes = canonical_layers(r)
    h = r // 2
    by_phase = {
        phase: sorted(
            (target for target, value in layer.items() if value == phase),
            key=lambda x: tuple(sorted(x)),
        )
        for phase in range(h + 1)
    }
    assert len(set(sizes.values())) == 1
    transitions = {
        phase: random_bijection(by_phase[phase], by_phase[phase + 1], rng)
        for phase in range(h)
    }
    half_paths = {}
    for root in by_phase[0]:
        path = [root]
        for phase in range(h):
            path.append(transitions[phase][path[-1]])
        half_paths[root] = tuple(path)
    ground = frozenset(range(1, 2 * r + 1))
    middle_to_root = {path[h]: root for root, path in half_paths.items()}
    sigma = {
        root: middle_to_root[ground - path[h]] for root, path in half_paths.items()
    }
    assert all(sigma[sigma[root]] == root and sigma[root] != root for root in sigma)
    seen = set()
    pairs = []
    for root in by_phase[0]:
        if root in seen:
            continue
        mate = sigma[root]
        seen.update((root, mate))
        def full(source):
            other = sigma[source]
            return half_paths[source] + tuple(
                ground - half_paths[other][h - u] for u in range(1, h + 1)
            )
        first = lift_johnson_path(full(root), r)
        second = lift_johnson_path(full(mate), r)
        pairs.append((root, mate, first + second))
    return pairs


def audit(r, trials, seed):
    rng = random.Random(seed)
    trial_hist = Counter()
    factor_change_hist = Counter()
    first_example = None
    for trial in range(trials):
        pairs = random_pairs(r, rng)
        simple = 0
        factors = 0
        for root, mate, cycle in pairs:
            if len(set(cycle)) != len(cycle):
                continue
            simple += 1
            witnesses, chords = induced_two_wreath_factors(cycle, r)
            if witnesses:
                factors += 1
                best = min(w["changes"] for w in witnesses)
                factor_change_hist[best] += 1
                if first_example is None:
                    first_example = {
                        "trial": trial,
                        "root": tuple(sorted(root)),
                        "mate": tuple(sorted(mate)),
                        "chords": chords,
                        "best": best,
                    }
        trial_hist[(simple, factors)] += 1
    return {
        "r": r,
        "trials": trials,
        "trial_simple_factor_hist": {str(k): v for k, v in trial_hist.items()},
        "factor_change_hist": dict(factor_change_hist),
        "first_example": first_example,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--r", type=int, nargs="+", default=[4, 6])
    parser.add_argument("--trials", type=int, default=100)
    parser.add_argument("--seed", type=int, default=20260821)
    args = parser.parse_args()
    for r in args.r:
        print(
            "RANDOM_MIRRORED_PHASE_DOUBLE_CYCLES",
            audit(r, args.trials, args.seed + r),
            flush=True,
        )


if __name__ == "__main__":
    main()
