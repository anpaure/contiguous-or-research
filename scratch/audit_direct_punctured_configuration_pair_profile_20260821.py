#!/usr/bin/env python3
"""Independent exact audit of the directed punctured-configuration profile.

The exhaustive part compares every permutation against the identity edge.
It checks the two degrees, every pair codegree, the pair-category inventory,
and the closed normalized sums in Theorem 5.1.  Instances through r=4 are
quick; use the OpenMP C++ census for r=5.
"""

from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations
from math import comb, factorial


Vertex = tuple[int, int]  # (layer: 0=M, 1=L, bit mask)


def edge(word: tuple[int, ...], r: int) -> tuple[Vertex, ...]:
    b = 2 * r + 1
    out: list[Vertex] = []
    for layer, k in ((0, r), (1, r - 1)):
        for start in range(1, b):
            mask = 0
            for j in range(k):
                mask |= 1 << word[(start + j) % b]
            out.append((layer, mask))
    assert len(out) == 4 * r and len(set(out)) == 4 * r
    return tuple(out)


def positional_count(k: int, h: int, a: int, b: int) -> int:
    if a == 0:
        m = b - k - h + 1
    elif a < min(k, h):
        m = 2
    else:
        assert a == min(k, h)
        m = abs(k - h) + 1
    return (b - 2) * m + int(a == min(k, h))


def pair_codegree(u: Vertex, v: Vertex, r: int) -> int:
    b = 2 * r + 1
    lu, mu = u
    lv, mv = v
    k = r if lu == 0 else r - 1
    h = r if lv == 0 else r - 1
    a = (mu & mv).bit_count()
    phi = (
        factorial(a)
        * factorial(k - a)
        * factorial(h - a)
        * factorial(b - k - h + a)
    )
    return positional_count(k, h, a, b) * phi


def expected_inventory(r: int) -> Counter[tuple[int, int, int]]:
    ans: Counter[tuple[int, int, int]] = Counter()
    for a in range(r):
        ans[(0, 0, a)] = 2 * r - 1
    ans[(1, 1, 0)] = 4 * r - 2
    for a in range(1, r - 1):
        ans[(1, 1, a)] = 2 * r - 1
    ans[(0, 1, 0)] = 6 * r - 3
    for a in range(1, r - 1):
        ans[(0, 1, a)] = 4 * r - 2
    ans[(0, 1, r - 1)] = 4 * r - 1
    return ans


def closed_normalized_parts(r: int) -> tuple[Fraction, Fraction, Fraction]:
    mm = Fraction((2 * r - 1) ** 2, r) * sum(
        (Fraction(1, comb(r, a) * comb(r + 1, a + 1)) for a in range(r)),
        start=Fraction(),
    )

    ml = Fraction()
    for a in range(r):
        if a == 0:
            n = 3 * (2 * r - 1)
        elif a == r - 1:
            n = 4 * r - 1
        else:
            n = 2 * (2 * r - 1)
        ml += Fraction(n * n, 2 * r * comb(r, a) * comb(r + 1, a + 2))

    ll = Fraction()
    for a in range(r - 1):
        n = 4 * (2 * r - 1) if a == 0 else 2 * (2 * r - 1)
        ll += Fraction(
            (r + 2) * n * n,
            4 * r * r * comb(r - 1, a) * comb(r + 2, a + 3),
        )
    return mm, ml, ll


def run(r: int) -> None:
    b = 2 * r + 1
    base = edge(tuple(range(b)), r)
    base_set = set(base)

    inventory: Counter[tuple[int, int, int]] = Counter()
    for u, v in combinations(base, 2):
        l0, l1 = sorted((u[0], v[0]))
        inventory[(l0, l1, (u[1] & v[1]).bit_count())] += 1
    assert inventory == expected_inventory(r), (inventory, expected_inventory(r))

    vertex_hits: Counter[Vertex] = Counter()
    pair_hits: Counter[tuple[Vertex, Vertex]] = Counter()
    intersection_hist: Counter[int] = Counter()
    pair_sum_from_intersections = 0

    for word in permutations(range(b)):
        overlap = sorted(base_set.intersection(edge(word, r)))
        intersection_hist[len(overlap)] += 1
        pair_sum_from_intersections += comb(len(overlap), 2)
        vertex_hits.update(overlap)
        pair_hits.update(combinations(overlap, 2))

    d_middle = 2 * r * factorial(r) * factorial(r + 1)
    d_lower = 2 * (r + 2) * factorial(r) * factorial(r + 1)
    assert {vertex_hits[v] for v in base if v[0] == 0} == {d_middle}
    assert {vertex_hits[v] for v in base if v[0] == 1} == {d_lower}

    for u, v in combinations(base, 2):
        key = tuple(sorted((u, v)))
        assert pair_hits[key] == pair_codegree(u, v, r), (
            r,
            u,
            v,
            pair_hits[key],
            pair_codegree(u, v, r),
        )

    pair_sum_from_matrix = sum(pair_hits.values())
    assert pair_sum_from_matrix == pair_sum_from_intersections
    mm, ml, ll = closed_normalized_parts(r)
    normalized = mm + ml + ll
    assert normalized == Fraction(pair_sum_from_matrix, d_middle)

    # The high-overlap skeleton is exactly the MM-disjoint and ML-containment
    # inventory.  Its complement must agree with Theorem 6.1 exactly.
    skeleton = 0
    off_skeleton = 0
    for u, v in combinations(base, 2):
        layers = {u[0], v[0]}
        a = (u[1] & v[1]).bit_count()
        on_skeleton = (u[0] == v[0] == 0 and a == 0) or (
            layers == {0, 1} and a == r - 1
        )
        if on_skeleton:
            skeleton += pair_codegree(u, v, r)
        else:
            off_skeleton += pair_codegree(u, v, r)
    skeleton_formula = Fraction((2 * r - 1) ** 2, r * (r + 1)) + Fraction(
        (4 * r - 1) ** 2, 2 * r * r
    )
    assert Fraction(skeleton, d_middle) == skeleton_formula
    assert skeleton + off_skeleton == pair_sum_from_matrix

    print(
        "DIRECT_PUNCTURED_PROFILE_PASS",
        {
            "r": r,
            "words": factorial(b),
            "D_M": d_middle,
            "D_L": d_lower,
            "pair_sum": pair_sum_from_matrix,
            "S_over_D_M": str(normalized),
            "S_over_D_M_float": float(normalized),
            "parts": tuple(map(str, (mm, ml, ll))),
            "skeleton_over_D_M": str(skeleton_formula),
            "intersection_hist": sorted(intersection_hist.items()),
        },
        flush=True,
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--r", type=int, nargs="+", default=[2, 3, 4])
    args = parser.parse_args()
    for value in args.r:
        if value < 2:
            raise SystemExit("r must be at least 2")
        run(value)

