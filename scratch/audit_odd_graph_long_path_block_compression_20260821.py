#!/usr/bin/env python3
"""Exact finite audit for the rainbow-hole odd-graph path reduction.

Research-only.  Run on H100.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations, permutations
from math import comb, factorial


def falling(n: int, j: int) -> int:
    return factorial(n) // factorial(n - j)


def vertices(b: int, r: int) -> tuple[int, ...]:
    return tuple(x for x in range(1 << b) if x.bit_count() == r)


def hole(b: int, x: int, y: int) -> int:
    assert not (x & y)
    z = ((1 << b) - 1) ^ (x | y)
    assert z.bit_count() == 1
    return z.bit_length() - 1


def windows(order: tuple[int, ...], r: int) -> tuple[int, ...]:
    b = len(order)
    return tuple(
        sum(1 << order[(i + j) % b] for j in range(r)) for i in range(b)
    )


def canonical_path(path: tuple[int, ...]) -> tuple[int, ...]:
    rev = tuple(reversed(path))
    return min(path, rev)


def rainbow_paths(b: int, r: int, s: int) -> set[tuple[int, ...]]:
    vv = vertices(b, r)
    nbr = {x: tuple(y for y in vv if not (x & y)) for x in vv}
    out: set[tuple[int, ...]] = set()

    def extend(path: tuple[int, ...], colors: frozenset[int]) -> None:
        if len(path) == s:
            out.add(canonical_path(path))
            return
        x = path[-1]
        for y in nbr[x]:
            if len(path) >= 2 and y == path[-2]:
                continue
            c = hole(b, x, y)
            if c in colors:
                continue
            extend(path + (y,), colors | {c})

    for x in vv:
        extend((x,), frozenset())
    return out


def wreath_segments(b: int, r: int, s: int) -> Counter[tuple[int, ...]]:
    out: Counter[tuple[int, ...]] = Counter()
    for tail in permutations(range(1, b)):
        order = (0,) + tail
        if order[1] > order[-1]:
            continue
        ww = windows(order, r)
        cycle = tuple(ww[(t * r) % b] for t in range(b))
        for start in range(b):
            path = tuple(cycle[(start + j) % b] for j in range(s))
            out[canonical_path(path)] += 1
    return out


def audit_paths(b: int) -> None:
    r = (b - 1) // 2
    n = comb(b, r)
    for s in range(2, r + 2):
        paths = rainbow_paths(b, r, s)
        wreath = wreath_segments(b, r, s)
        alpha = (s - 1) // 2
        beta = (s - 2) // 2
        ff = falling(r, alpha) * falling(r, beta)
        expected_q = n * (r + 1) * ff // 2
        expected_extensions = factorial(r - alpha) * factorial(r - beta)
        assert paths == set(wreath)
        assert set(wreath.values()) == {expected_extensions}
        assert len(paths) == expected_q

        degree = Counter(x for path in paths for x in path)
        assert set(degree.values()) == {s * (r + 1) * ff // 2}

        codegree = Counter(
            tuple(sorted(pair))
            for path in paths
            for pair in combinations(path, 2)
        )
        expected_max = (s - 1) * ff
        assert max(codegree.values()) == expected_max
        for (x, y), value in codegree.items():
            q = (x & y).bit_count()
            candidates = []
            for t in range(1, s):
                qt = r - t // 2 if t % 2 == 0 else (t - 1) // 2
                if qt == q:
                    candidates.append(t)
            assert len(candidates) == 1
            t = candidates[0]
            expected = (
                (r + 1)
                * ff
                * (s - t)
                // (comb(r, q) * comb(r + 1, r - q))
            )
            assert value == expected
        print(
            "PATH_PASS",
            {
                "b": b,
                "r": r,
                "s": s,
                "paths": len(paths),
                "degree": next(iter(degree.values())),
                "max_codegree": max(codegree.values()),
            },
            flush=True,
        )


def audit_counterexample(r: int) -> None:
    assert r >= 4
    b = 2 * r + 1
    aa = set(range(r))
    bb = set(range(r, 2 * r))
    z = 2 * r
    a = 0
    d = r
    path_sets = (
        aa,
        bb,
        aa - {a} | {z},
        bb - {d} | {a},
        aa - {a} | {d},
    )
    path = tuple(sum(1 << x for x in part) for part in path_sets)
    assert all(not (x & y) for x, y in zip(path, path[1:]))
    assert all(path[i] != path[i + 2] for i in range(3))
    colors = [hole(b, x, y) for x, y in zip(path, path[1:])]
    assert colors == [z, a, d, z]
    print("COUNTEREXAMPLE_PASS", {"r": r, "holes": colors}, flush=True)


def audit_blocks(b: int) -> None:
    r = (b - 1) // 2
    n = comb(b, r)
    for s in range(2, 2 * r + 1):
        if 2 * r % s or 2 * r // s < 2:
            continue
        k = 2 * r // s
        alpha = (s - 1) // 2
        beta = (s - 2) // 2
        q_s = n * (r + 1) * falling(r, alpha) * falling(r, beta) // 2
        expected_degree = (
            k * factorial(r - alpha) * factorial(r - beta)
        )
        expected_adjacent = (k - 1) * factorial(r - s + 1) ** 2

        multiplicity = Counter()
        degree = Counter()
        codegree = Counter()
        adjacent_pairs: set[tuple[tuple[int, ...], tuple[int, ...]]] = set()
        for tail in permutations(range(1, b)):
            order = (0,) + tail
            if order[1] > order[-1]:
                continue
            ww = windows(order, r)
            for dirty in range(b):
                cycle = tuple(ww[(dirty + t * r) % b] for t in range(b))
                clean = cycle[1:]
                blocks = tuple(
                    canonical_path(clean[j * s : (j + 1) * s])
                    for j in range(k)
                )
                key = tuple(sorted(blocks))
                multiplicity[key] += 1
                for block in blocks:
                    degree[block] += 1
                for pair in combinations(blocks, 2):
                    codegree[tuple(sorted(pair))] += 1
                for j in range(k - 1):
                    adjacent_pairs.add(tuple(sorted((blocks[j], blocks[j + 1]))))

        assert max(multiplicity.values()) == 1
        assert len(degree) == q_s
        assert set(degree.values()) == {expected_degree}
        assert {codegree[pair] for pair in adjacent_pairs} == {
            expected_adjacent
        }
        print(
            "BLOCK_PASS",
            {
                "b": b,
                "r": r,
                "s": s,
                "rank": k,
                "vertices": len(degree),
                "edges": len(multiplicity),
                "degree": expected_degree,
                "adjacent_codegree": expected_adjacent,
            },
            flush=True,
        )


if __name__ == "__main__":
    for rr in (4, 5, 8):
        audit_counterexample(rr)
    for odd_b in (5, 7, 9):
        audit_paths(odd_b)
        audit_blocks(odd_b)
