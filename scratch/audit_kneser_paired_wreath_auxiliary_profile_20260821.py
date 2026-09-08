#!/usr/bin/env python3
"""Exact finite audit for the paired-Kneser punctured-wreath profile."""

from __future__ import annotations

from collections import Counter
from itertools import combinations, permutations
from math import comb, factorial


def windows(order: tuple[int, ...], r: int) -> tuple[int, ...]:
    b = len(order)
    return tuple(
        sum(1 << order[(i + j) % b] for j in range(r)) for i in range(b)
    )


def edge_key(x: int, y: int) -> tuple[int, int]:
    return (min(x, y), max(x, y))


def enumerate_auxiliary(b: int):
    r = (b - 1) // 2
    vertices = [
        edge_key(x, y)
        for x in range(1 << b)
        if x.bit_count() == r
        for y in range(x + 1, 1 << b)
        if y.bit_count() == r and not (x & y)
    ]
    vertex_id = {e: i for i, e in enumerate(vertices)}
    multiplicity = Counter()
    target_multiplicity = Counter()
    position_distance = {}

    for tail in permutations(range(1, b)):
        order = (0,) + tail
        if order[1] > order[-1]:
            continue
        ww = windows(order, r)
        for dirty in range(b):
            target_multiplicity[
                tuple(sorted(ww[j] for j in range(b) if j != dirty))
            ] += 1
            pairs = []
            pos = []
            for k in range(1, r + 1):
                i = (dirty + k) % b
                e = edge_key(ww[i], ww[(i + r) % b])
                pairs.append(vertex_id[e])
                pos.append(k)
            key = tuple(sorted(pairs))
            multiplicity[key] += 1
            for a, c in combinations(range(r), 2):
                pair = tuple(sorted((pairs[a], pairs[c])))
                d = abs(pos[a] - pos[c])
                old = position_distance.setdefault(pair, d)
                assert old == d

    edges = list(multiplicity)
    degree = Counter()
    codegree = Counter()
    for edge in edges:
        for x in edge:
            degree[x] += 1
        for pair in combinations(edge, 2):
            codegree[pair] += 1
    return (
        vertices,
        multiplicity,
        target_multiplicity,
        edges,
        degree,
        codegree,
        position_distance,
    )


def formula_lambda(r: int, d: int) -> int:
    return (
        (r - d)
        * factorial(r - d) ** 2
        * factorial(d - 1)
        * factorial(d)
    )


def audit(b: int) -> None:
    r = (b - 1) // 2
    vertices, mult, target_mult, edges, degree, codegree, distance = (
        enumerate_auxiliary(b)
    )
    expected_edges = factorial(b) // 2
    expected_degree = r * factorial(r) ** 2
    expected_max_codegree = (r - 1) * factorial(r - 1) ** 2
    expected_overlap = sum(
        (r - d) ** 2
        * factorial(r - d) ** 2
        * factorial(d - 1)
        * factorial(d)
        for d in range(1, r)
    )

    assert len(vertices) == comb(b, r) * (r + 1) // 2
    assert len(edges) == expected_edges
    assert max(mult.values()) == 1
    assert max(target_mult.values()) == 1
    assert set(degree.values()) == {expected_degree}
    assert max(codegree.values()) == expected_max_codegree
    for pair, value in codegree.items():
        assert value == formula_lambda(r, distance[pair])
    overlap = [
        sum(codegree[pair] for pair in combinations(edge, 2)) for edge in edges
    ]
    assert set(overlap) == {expected_overlap}
    target_degree = Counter()
    target_codegree = Counter()
    for edge in target_mult:
        for x in edge:
            target_degree[x] += 1
        for pair in combinations(edge, 2):
            target_codegree[pair] += 1
    expected_target_degree = r * factorial(r) * factorial(r + 1)
    assert set(target_degree.values()) == {expected_target_degree}
    for (x, y), value in target_codegree.items():
        s = (x & y).bit_count()
        d = r - s
        assert value == (
            (2 * r - 1)
            * factorial(d) ** 2
            * factorial(s)
            * factorial(s + 1)
        )
    high_codegrees = {}
    for t in range(3, r + 1):
        counter = Counter(
            subset for edge in edges for subset in combinations(edge, t)
        )
        expected = (r - t + 1) * factorial(r - t + 1) ** 2
        assert max(counter.values()) == expected
        high_codegrees[t] = expected
    print(
        "PASS",
        {
            "b": b,
            "r": r,
            "vertices": len(vertices),
            "edges": len(edges),
            "degree": expected_degree,
            "max_codegree": expected_max_codegree,
            "higher_max_codegrees": high_codegrees,
            "overlap": expected_overlap,
            "target_degree": expected_target_degree,
            "target_codegree_max": max(target_codegree.values()),
        },
        flush=True,
    )


if __name__ == "__main__":
    for bb in (5, 7, 9):
        audit(bb)
