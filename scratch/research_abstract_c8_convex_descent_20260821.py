#!/usr/bin/env python3
"""Steepest descent under all abstract first-shadow C8 square currents.

This tests the precise conjecture that an abstract square-local minimum in
the wreath marginal fiber has zero (or O(A/r)) energy gap.  It does not test
physical two-row availability.  Intended execution: H100 only.
"""

from __future__ import annotations

import argparse
import math
import random
from collections import Counter
from itertools import combinations

from research_canonical_transposition_component_energy_20260821 import (
    dyck_words,
    msw_row,
    windows,
)


def square_moves(n, k, target_index):
    moves = set()
    for core_tuple in combinations(range(1, n + 1), k - 2):
        core = set(core_tuple)
        outside = tuple(point for point in range(1, n + 1)
                        if point not in core)
        for a, b, c, d in combinations(outside, 4):
            matchings = (
                ((a, b), (c, d)),
                ((a, c), (b, d)),
                ((a, d), (b, c)),
            )
            edge_pairs = []
            for (u, v), (x, y) in matchings:
                edge_pairs.append(tuple(sorted((
                    target_index[frozenset(core | {u, v})],
                    target_index[frozenset(core | {x, y})],
                ))))
            for left, right in combinations(edge_pairs, 2):
                if left != right:
                    moves.add((left, right) if left < right else (right, left))
    return tuple(moves)


def energy(loads):
    return sum(value * (value - 1) // 2 for value in loads)


def profile(r):
    n = 2 * r + 1
    targets = tuple(frozenset(target)
                    for target in combinations(range(1, n + 1), r - 1))
    target_index = {target: index for index, target in enumerate(targets)}
    counter = Counter()
    for word in dyck_words(r):
        counter.update(windows(msw_row(word), r - 1))
    loads = [counter[target] for target in targets]
    return targets, target_index, loads


def descend(r, seed, random_ties):
    n = 2 * r + 1
    targets, target_index, loads = profile(r)
    moves = square_moves(n, r - 1, target_index)
    rng = random.Random(seed)
    steps = 0
    while True:
        best_delta = 0
        best = []
        for left, right in moves:
            for donors, recipients in ((left, right), (right, left)):
                x, y = donors
                if loads[x] == 0 or loads[y] == 0:
                    continue
                z, w = recipients
                delta = loads[z] + loads[w] - loads[x] - loads[y] + 2
                if delta < best_delta:
                    best_delta = delta
                    best = [(donors, recipients)]
                elif delta == best_delta and delta < 0:
                    if random_ties:
                        best.append((donors, recipients))
                    elif not best:
                        best = [(donors, recipients)]
        if best_delta >= 0:
            break
        donors, recipients = rng.choice(best)
        for index in donors:
            loads[index] -= 1
        for index in recipients:
            loads[index] += 1
        steps += 1
    A = math.comb(n, r)
    N = len(targets)
    return {
        "r": r,
        "targets": N,
        "moves": len(moves),
        "steps": steps,
        "energy": energy(loads),
        "gap": energy(loads) - (A - N),
        "holes": sum(value == 0 for value in loads),
        "triples_plus": sum(value >= 3 for value in loads),
        "load_hist": dict(Counter(loads)),
    }


def main(r_min, r_max, trials):
    for r in range(r_min, r_max + 1):
        for trial in range(trials):
            print("ABSTRACT_C8_DESCENT", descend(r, trial, trials > 1),
                  flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--r-min", type=int, default=3)
    parser.add_argument("--r-max", type=int, default=5)
    parser.add_argument("--trials", type=int, default=1)
    args = parser.parse_args()
    main(args.r_min, args.r_max, args.trials)
