#!/usr/bin/env python3
"""Exact finite audit for the marked-gap/local-hexagon capacity theorem.

Research-only.  Run on H100.

The proof in the accompanying note is analytic.  This checker audits:

* the exact Catalan and marked-gap arithmetic;
* the every-second wreath slot formula for all normalized omitted words
  through b=9;
* every three-edge alternating reconnection of one or two abstract b-cycles
  for b=7,9 which again has only b-cycles, checking the 6q direct-odd and
  3q projected-transition collar bounds.

The abstract reconnection census intentionally omits Kneser-edge legality.
That makes it a stronger audit of the purely cycle-theoretic collar count;
ambient-graph legality only removes reconnections.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, permutations
from math import comb


def catalan(r: int) -> int:
    return comb(2 * r, r) // (r + 1)


def edge(x: int, y: int) -> tuple[int, int]:
    assert x != y
    return (x, y) if x < y else (y, x)


def canonical_path(path: tuple[int, ...]) -> tuple[int, ...]:
    rev = tuple(reversed(path))
    return min(path, rev)


def wreath_vertices(order: tuple[int, ...]) -> tuple[int, ...]:
    b = len(order)
    r = (b - 1) // 2
    return tuple(
        sum(1 << order[(i + 2 * j + 1) % b] for j in range(r))
        for i in range(b)
    )


def audit_arithmetic() -> None:
    for r in range(3, 1001):
        b = 2 * r + 1
        aa = comb(b, r)
        cc = catalan(r)
        kk = (2 * r - 3) * catalan(r - 2)
        nn = comb(b, r - 1)
        assert aa == b * cc
        assert Fraction(nn, aa) == Fraction(r, r + 2)
        assert Fraction(kk, aa) == Fraction(
            r * (r + 1), 4 * (2 * r - 1) * (2 * r + 1)
        )
        for s in (3, 6):
            threshold = Fraction(kk, s) - Fraction(2 * aa, s * (r + 2))
            # Any integer T below this exact threshold leaves a positive hole.
            if threshold > 0:
                tt = (threshold.numerator - 1) // threshold.denominator
                assert kk - s * tt - Fraction(2 * aa, r + 2) > 0
    print("ARITHMETIC_PASS", {"r_max": 1000}, flush=True)


def audit_wreath_slots(b: int) -> None:
    r = (b - 1) // 2
    full = (1 << b) - 1
    checked = 0
    for tail in permutations(range(1, b)):
        order = (0,) + tail
        vv = wreath_vertices(order)
        assert len(set(vv)) == b
        assert all(x.bit_count() == r for x in vv)
        for i in range(b):
            assert not (vv[i] & vv[(i + 1) % b])
            assert (full ^ (vv[i] | vv[(i + 1) % b])).bit_count() == 1
        for q in range(1, r):
            for i in range(b):
                actual = full
                for j in range(q + 1):
                    actual &= vv[(i - 2 * j) % b]
                expected = sum(
                    1 << order[(i + d) % b]
                    for d in range(1, 2 * r - 2 * q, 2)
                )
                assert actual == expected
                assert actual.bit_count() == r - q
                # Reversal of the same even segment uses the same vertices.
                reverse = full
                for j in range(q + 1):
                    reverse &= vv[(i - 2 * q + 2 * j) % b]
                assert reverse == actual
        checked += 1
    print(
        "WREATH_SLOT_PASS",
        {"b": b, "normalized_words": checked},
        flush=True,
    )


def cycle_edges(cycles: tuple[tuple[int, ...], ...]) -> frozenset[tuple[int, int]]:
    return frozenset(
        edge(cycle[i], cycle[(i + 1) % len(cycle)])
        for cycle in cycles
        for i in range(len(cycle))
    )


def cycles_from_edges(
    edges: frozenset[tuple[int, int]],
) -> tuple[tuple[int, ...], ...]:
    adj: dict[int, list[int]] = {}
    for x, y in edges:
        adj.setdefault(x, []).append(y)
        adj.setdefault(y, []).append(x)
    assert all(len(nbr) == 2 for nbr in adj.values())
    unseen = set(adj)
    cycles = []
    while unseen:
        start = min(unseen)
        first = min(adj[start])
        path = [start]
        prev, cur = start, first
        while cur != start:
            path.append(cur)
            nxt = adj[cur][0] if adj[cur][0] != prev else adj[cur][1]
            prev, cur = cur, nxt
        assert len(set(path)) == len(path)
        unseen.difference_update(path)
        cycles.append(tuple(path))
    return tuple(cycles)


def path_segments(
    cycles: tuple[tuple[int, ...], ...], length: int
) -> frozenset[tuple[int, ...]]:
    assert length >= 1
    out = set()
    for cycle in cycles:
        assert length < len(cycle)
        for i in range(len(cycle)):
            path = tuple(cycle[(i + j) % len(cycle)] for j in range(length + 1))
            out.add(canonical_path(path))
    assert len(out) == sum(len(cycle) for cycle in cycles)
    return frozenset(out)


def perfect_matchings(points: tuple[int, ...]):
    if not points:
        yield frozenset()
        return
    x = points[0]
    for j in range(1, len(points)):
        y = points[j]
        rest = points[1:j] + points[j + 1 :]
        for matching in perfect_matchings(rest):
            yield matching | {edge(x, y)}


def union_is_c6(
    old: frozenset[tuple[int, int]], new: frozenset[tuple[int, int]]
) -> bool:
    if old & new:
        return False
    both = old | new
    adj: dict[int, list[int]] = {}
    for x, y in both:
        adj.setdefault(x, []).append(y)
        adj.setdefault(y, []).append(x)
    if len(adj) != 6 or any(len(nbr) != 2 for nbr in adj.values()):
        return False
    start = next(iter(adj))
    seen = {start}
    stack = [start]
    while stack:
        x = stack.pop()
        for y in adj[x]:
            if y not in seen:
                seen.add(y)
                stack.append(y)
    return len(seen) == 6


def audit_three_cut(b: int, number_cycles: int) -> None:
    r = (b - 1) // 2
    cycles = tuple(
        tuple(c * b + j for j in range(b)) for c in range(number_cycles)
    )
    ff = cycle_edges(cycles)
    old_direct = {
        q: path_segments(cycles, 2 * q) for q in range(1, r)
    }
    old_projected = {
        q: path_segments(cycles, q) for q in range(1, r)
    }
    alternating = 0
    wreath_legal = 0
    for removed_tuple in combinations(sorted(ff), 3):
        removed = frozenset(removed_tuple)
        endpoints = tuple(x for e in removed for x in e)
        if len(set(endpoints)) != 6:
            continue
        endpoints = tuple(sorted(endpoints))
        for inserted in perfect_matchings(endpoints):
            if not union_is_c6(removed, inserted):
                continue
            if inserted & ff:
                continue
            alternating += 1
            new_edges = (ff - removed) | inserted
            new_cycles = cycles_from_edges(frozenset(new_edges))
            if any(len(cycle) != b for cycle in new_cycles):
                continue
            wreath_legal += 1
            for q in range(1, r):
                new_direct = path_segments(new_cycles, 2 * q)
                assert len(old_direct[q] - new_direct) <= 6 * q
                assert len(new_direct - old_direct[q]) <= 6 * q
                new_projected = path_segments(new_cycles, q)
                assert len(old_projected[q] - new_projected) <= 3 * q
                assert len(new_projected - old_projected[q]) <= 3 * q
    assert alternating > 0
    assert wreath_legal > 0
    print(
        "THREE_CUT_PASS",
        {
            "b": b,
            "cycles": number_cycles,
            "alternating_reconnections": alternating,
            "wreath_legal": wreath_legal,
        },
        flush=True,
    )


if __name__ == "__main__":
    audit_arithmetic()
    for bb in (5, 7, 9):
        audit_wreath_slots(bb)
    for bb in (7, 9):
        for kk in (1, 2):
            audit_three_cut(bb, kk)
    print("CATALAN_C6_MARKED_GAP_REPAIR_CAPACITY_AUDIT_PASS", flush=True)
