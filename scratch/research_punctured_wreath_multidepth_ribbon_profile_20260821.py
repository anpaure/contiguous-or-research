#!/usr/bin/env python3
"""Exact small-b profile for depth-H ribbons grouped by punctured wreaths.

Run only on H100.  A depth-H flag at a clean rank-r window remembers the
same-start prefix windows of ranks r-1,...,r-H, equivalently the ordered
last H labels of that rank-r window.  A ribbon pairs the two flags at one
of the r disjoint opposite-window pairs after a dirty window is removed.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations, permutations
from math import comb, factorial


def windows(order: tuple[int, ...], ell: int) -> tuple[int, ...]:
    b = len(order)
    return tuple(
        sum(1 << order[(i + j) % b] for j in range(ell)) for i in range(b)
    )


def flag(mid: int, chains: tuple[int, ...]):
    assert all(s & ~mid == 0 for s in chains)
    return (mid, chains)


def ribbon_key(f, g):
    assert not (f[0] & g[0])
    return (f, g) if f[0] < g[0] else (g, f)


def enumerate_profile(b: int, H: int):
    r = (b - 1) // 2
    assert 1 <= H <= r - 1
    edge_mult = Counter()
    ribbons = set()
    pair_distance = {}

    for tail in permutations(range(1, b)):
        order = (0,) + tail
        decks = {ell: windows(order, ell) for ell in range(r - H, r + 1)}
        mid = decks[r]
        for dirty in range(b):
            rr = []
            for k in range(1, r + 1):
                i = (dirty + k) % b
                j = (i + r) % b
                fi = flag(mid[i], tuple(decks[r - q][i] for q in range(1, H + 1)))
                fj = flag(mid[j], tuple(decks[r - q][j] for q in range(1, H + 1)))
                rib = ribbon_key(fi, fj)
                rr.append(rib)
                ribbons.add(rib)
            key = tuple(sorted(rr))
            edge_mult[key] += 1
            for a, c in combinations(range(r), 2):
                pair = tuple(sorted((rr[a], rr[c])))
                d = c - a
                old = pair_distance.setdefault(pair, d)
                assert old == d

    edges = list(edge_mult)
    degree = Counter()
    codegree = Counter()
    for edge in edges:
        for x in edge:
            degree[x] += 1
        for pair in combinations(edge, 2):
            codegree[pair] += 1
    return ribbons, edges, edge_mult, degree, codegree, pair_distance


def audit(b: int, H: int):
    r = (b - 1) // 2
    ribbons, edges, mult, degree, codegree, distance = enumerate_profile(b, H)
    assert len(edges) == factorial(b)
    assert set(mult.values()) == {1}
    expected_ribbons = comb(b, r) * (r + 1) // 2
    for j in range(H):
        expected_ribbons *= (r - j) ** 2
    assert len(ribbons) == expected_ribbons
    expected_degree = 2 * r * factorial(r - H) ** 2
    assert set(degree.values()) == {expected_degree}

    by_distance = defaultdict(set)
    for pair, value in codegree.items():
        by_distance[distance[pair]].add(value)
    higher = {}
    for t in range(2, r + 1):
        counter = Counter(
            subset for edge in edges for subset in combinations(edge, t)
        )
        value = max(counter.values(), default=0)
        higher[t] = value
        if t <= r - H + 1:
            expected = (r - t + 1) * factorial(r - H - t + 1) ** 2
            assert value == expected, (b, H, t, value, expected)
    print(
        'PASS',
        {
            'b': b,
            'r': r,
            'H': H,
            'ribbons': len(ribbons),
            'group_edges': len(edges),
            'degree': expected_degree,
            'higher_max': higher,
            'pair_by_distance': {d: sorted(v) for d, v in sorted(by_distance.items())},
        },
        flush=True,
    )


if __name__ == '__main__':
    for bb in (5, 7, 9):
        rr = (bb - 1) // 2
        for hh in range(1, rr):
            audit(bb, hh)
