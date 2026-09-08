#!/usr/bin/env python3
"""Finite regression checks for the punctured cover-down reduction.

The mathematical note is self-contained.  This checks its exact finite
identities, selector support, and asymptotic scale arithmetic.
"""

from __future__ import annotations

from collections import Counter
from itertools import permutations
from math import comb, floor, sqrt
from random import Random


def windows(row, k):
    b = len(row)
    return {
        frozenset(row[(s + j) % b] for j in range(k))
        for s in range(b)
    }


def apply_label_swap(row, i, j):
    return tuple(j if x == i else i if x == j else x for x in row)


def check_capacity_constants():
    for r in range(64, 500):
        b = 2 * r + 1
        layer1 = comb(b, r - 1)
        for numerator in range(1, 65):
            x = numerator / 64
            if r * x < 64:
                continue
            qmax = floor(sqrt(r * x) / 4)
            for q in range(1, qmax + 1):
                layerq = comb(b, r - q)
                assert layerq >= (1 - x / 8) * layer1 - 1e-7
                assert layerq - (1 - x) * layer1 >= 7 * x * layer1 / 8 - 1e-7


def check_hole_duplicate_margins():
    rng = Random(20260822)
    for r in range(2, 5):
        b = 2 * r + 1
        rows = [(0,) + tail for tail in permutations(range(1, b))]
        for _ in range(30):
            bank = rng.sample(rows, rng.randrange(0, min(len(rows), 12) + 1))
            p = len(bank)
            for k in range(1, b):
                load = Counter()
                for row in bank:
                    load.update(windows(row, k))
                targets = [frozenset(t) for t in __import__("itertools").combinations(range(b), k)]
                holes = {target for target in targets if load[target] == 0}
                excess = {target: max(load[target] - 1, 0) for target in targets}
                assert len(holes) - sum(excess.values()) == comb(b, k) - b * p
                expected_margin = comb(b - 1, k - 1) - k * p
                for point in range(b):
                    hole_margin = sum(point in target for target in holes)
                    excess_margin = sum(
                        amount for target, amount in excess.items() if point in target
                    )
                    assert hole_margin - excess_margin == expected_margin


def signed_rank_action(base, a):
    first = apply_label_swap(base, 0, 1)
    second = apply_label_swap(base, a, a + 1)
    both = apply_label_swap(first, a, a + 1)
    return [(1, base), (-1, first), (-1, second), (1, both)]


def check_petr_turek_selectors():
    for r in range(3, 7):
        b = 2 * r + 1
        base = tuple(range(b))
        for a in range(2, r):
            signed = signed_rank_action(base, a)
            for k in range(1, b):
                action = Counter()
                for coefficient, row in signed:
                    for target in windows(row, k):
                        action[target] += coefficient
                action = Counter({target: value for target, value in action.items() if value})
                if k not in (a, b - a):
                    assert not action
                else:
                    assert len(action) == 4
                    assert sorted(action.values()) == [-1, -1, 1, 1]

            positive_overlap = len(windows(signed[0][1], r) & windows(signed[3][1], r))
            negative_overlap = len(windows(signed[1][1], r) & windows(signed[2][1], r))
            assert positive_overlap >= b - 4
            assert negative_overlap >= b - 4


def check_arc_scale_tradeoff():
    for r in [10**3, 10**4, 10**5]:
        b = 2 * r + 1
        for alpha in [0.02, 0.1, 0.25]:
            x = r ** (-alpha)
            length = max(1, round(b * sqrt(x)))
            # M/B is on the scale xb/L = sqrt(x), and promotion is o(A).
            ratio = x * b / length
            assert ratio <= 2 * sqrt(x)
            assert ratio > 0


def main():
    check_capacity_constants()
    check_hole_duplicate_margins()
    check_petr_turek_selectors()
    check_arc_scale_tradeoff()
    print("PASS: cover-down capacity, margin, selector, and flag-arc identities")


if __name__ == "__main__":
    main()
