#!/usr/bin/env python3
"""Finite checks for the growing-rank wreath residual obstruction note.

Run computationally only on H100.  Exhaustively enumerates oriented cyclic
orders (rotation fixed at zero) for small b and verifies degree/codegree
formulas, the balanced-slice transversal, and exact weighted point balance.
"""

from __future__ import annotations

import argparse
import itertools
from collections import Counter
from fractions import Fraction
from math import comb, factorial


def masks_of_rank(b: int, r: int):
    for s in itertools.combinations(range(b), r):
        yield sum(1 << x for x in s)


def windows(order, r: int):
    b = len(order)
    return tuple(
        sum(1 << order[(i + j) % b] for j in range(r)) for i in range(b)
    )


def check(b: int, r: int, a: int) -> None:
    assert 1 <= r <= b // 2
    layer = tuple(masks_of_rank(b, r))
    degree = Counter()
    codegree = Counter()
    decks = []
    for tail in itertools.permutations(range(1, b)):
        deck = windows((0,) + tail, r)
        decks.append(deck)
        for s in deck:
            degree[s] += 1
        for s, t in itertools.combinations(deck, 2):
            codegree[tuple(sorted((s, t)))] += 1
    D = factorial(r) * factorial(b - r)
    assert set(degree.values()) == {D}

    by_distance = {}
    for s, t in itertools.combinations(layer, 2):
        d = (s ^ t).bit_count() // 2
        val = codegree[tuple(sorted((s, t)))]
        by_distance.setdefault(d, set()).add(val)
    q = b - 2 * r
    for d in range(1, r):
        expected = 2 * factorial(d) ** 2 * factorial(r - d) * factorial(b - r - d)
        assert by_distance[d] == {expected}, (b, r, d, by_distance[d], expected)
    expected_disjoint = (q + 1) * factorial(r) ** 2 * factorial(q)
    assert by_distance[r] == {expected_disjoint}

    A = (1 << a) - 1
    mu = Fraction(a * r, b)
    lo = mu.numerator // mu.denominator
    levels = {lo} if mu.denominator == 1 else {lo, lo + 1}
    K = {s for s in layer if (s & A).bit_count() in levels}
    F = set(layer) - K
    for deck in decks:
        assert any(s in K for s in deck)
        assert not all(s in F for s in deck)

    z = {s: Fraction((s & A).bit_count()) - mu for s in F}
    A1 = sum(z.values(), Fraction())
    A2 = sum((v * v for v in z.values()), Fraction())
    lam = -A1 / A2
    weights = {s: Fraction(1) + lam * z[s] for s in F}
    assert min(weights.values()) >= 0
    point_loads = []
    for x in range(b):
        point_loads.append(sum((w for s, w in weights.items() if s >> x & 1), Fraction()))
    assert len(set(point_loads)) == 1

    print(
        f"PASS b={b} r={r} a={a} M={comb(b,r)} D={D} "
        f"q={q} codegrees={[(d,next(iter(v))) for d,v in sorted(by_distance.items())]} "
        f"K={len(K)} F={len(F)} lambda={lam} weighted_mass={sum(weights.values())}"
    )


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-b", type=int, default=9)
    args = ap.parse_args()
    for b in range(5, args.max_b + 1, 2):
        for r in range(max(2, b // 2 - 2), b // 2 + 1):
            check(b, r, b // 2)


if __name__ == "__main__":
    main()
