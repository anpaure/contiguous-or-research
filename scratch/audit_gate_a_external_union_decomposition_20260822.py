#!/usr/bin/env python3
"""Exact checks for the Gate-A root-hazard/external-union decomposition.

The theorem proved in the companion note is analytic.  This script checks
the identities on selected small simple hypergraphs and reports the exact
punctured r=3 one-row residual tangent without interpreting it as asymptotic
evidence.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations
from math import comb, factorial


def falling(x: int, m: int) -> int:
    if x < m:
        return 0
    out = 1
    for j in range(m):
        out *= x - j
    return out


def phi(d: int, c: int, m: int) -> Fraction:
    if d < m or d <= c:
        return Fraction()
    return Fraction((d - c) ** m, falling(d, m))


def punctured_edge(word: tuple[int, ...], r: int) -> frozenset[tuple[int, int]]:
    b = 2 * r + 1
    out: set[tuple[int, int]] = set()
    for shore, width in ((0, r), (1, r - 1)):
        for start in range(1, b):
            mask = 0
            for offset in range(width):
                mask |= 1 << word[(start + offset) % b]
            out.add((shore, mask))
    assert len(out) == 4 * r
    return frozenset(out)


def decomposition(
    edges: tuple[frozenset[object], ...], roots: tuple[object, ...], m: int, c: int
) -> dict[str, Fraction]:
    z_edges = len(edges)
    stars = {v: tuple(i for i, edge in enumerate(edges) if v in edge) for v in roots}
    degree = {v: len(stars[v]) for v in roots}
    conflicts = tuple(
        frozenset(j for j, other in enumerate(edges) if edge & other)
        for edge in edges
    )
    conflict_size = tuple(map(len, conflicts))

    total = sum(falling(degree[v], m) for v in roots)
    tail = sum(max(degree[v] - c, 0) ** m for v in roots)
    assert total > 0 and tail > 0
    scalar = Fraction(tail, total)

    palm_weight = {v: Fraction(falling(degree[v], m), total) for v in roots}
    external = {}
    duplicate = {}
    erosion_numerator = Fraction()

    for v in roots:
        d = degree[v]
        if d == 0:
            external[v] = Fraction()
            duplicate[v] = Fraction()
            continue
        star = frozenset(stars[v])
        external[v] = Fraction(
            sum(conflict_size[i] - d for i in star), d
        )
        if d < m:
            duplicate[v] = Fraction()
            continue
        dup_sum = Fraction()
        for g, edge in enumerate(edges):
            if v in edge:
                continue
            a = sum(g in conflicts[i] for i in star)
            dup_sum += Fraction(m * a, d) - 1 + Fraction(
                falling(d - a, m), falling(d, m)
            )
            erosion_numerator += Fraction(falling(d - a, m), total) * (
                phi(d, c, m) - phi(d - a, c, m)
            )
        duplicate[v] = dup_sum
        q_two = sum(
            falling(sum(g in conflicts[i] for i in star), 2)
            for g, edge in enumerate(edges)
            if v not in edge
        )
        assert Fraction() <= duplicate[v] <= Fraction(
            comb(m, 2) * q_two, falling(d, 2)
        )

    mean_d = sum(palm_weight[v] * degree[v] for v in roots)
    mean_e = sum(palm_weight[v] * external[v] for v in roots)
    mean_dup = sum(palm_weight[v] * duplicate[v] for v in roots)
    mean_phi = scalar
    cov_d = sum(
        palm_weight[v] * (degree[v] - mean_d) * (phi(degree[v], c, m) - mean_phi)
        for v in roots
    )
    cov_e = sum(
        palm_weight[v] * (external[v] - mean_e) * (phi(degree[v], c, m) - mean_phi)
        for v in roots
    )
    cov_dup = sum(
        palm_weight[v] * (duplicate[v] - mean_dup) * (phi(degree[v], c, m) - mean_phi)
        for v in roots
    )

    # Direct first derivative: at p=0, either no edge or one edge is marked.
    loss_tail = 0
    loss_total = 0
    for edge in edges:
        residual = tuple(other for other in edges if not (edge & other))
        new_degree = Counter(v for other in residual for v in other if v in roots)
        loss_tail += tail - sum(max(new_degree[v] - c, 0) ** m for v in roots if v not in edge)
        loss_total += total - sum(falling(new_degree[v], m) for v in roots if v not in edge)
    direct_derivative = Fraction(-loss_tail * total + tail * loss_total, total * total)
    split_derivative = -cov_d - m * cov_e + cov_dup - erosion_numerator
    assert direct_derivative == split_derivative, (
        direct_derivative,
        split_derivative,
    )
    assert cov_d >= 0

    # Check the exact conditional carrier identities by explicit enumeration
    # whenever the carrier space is small enough.
    carrier_count = sum(falling(degree[v], m) for v in roots)
    if carrier_count <= 200_000:
        for v in roots:
            d = degree[v]
            if d < m:
                continue
            sum_u = 0
            sum_dup = 0
            for carrier in permutations(stars[v], m):
                outside = [conflicts[i] - frozenset(stars[v]) for i in carrier]
                union = frozenset().union(*outside)
                sum_u += len(union)
                sum_dup += sum(map(len, outside)) - len(union)
            assert Fraction(sum_u, falling(d, m)) == m * external[v] - duplicate[v]
            assert Fraction(sum_dup, falling(d, m)) == duplicate[v]

    return {
        "Z": Fraction(z_edges),
        "A": scalar,
        "A_prime": direct_derivative,
        "cov_d": cov_d,
        "cov_external": cov_e,
        "cov_duplicate": cov_dup,
        "erosion": erosion_numerator,
    }


def exhaustive_generic_checks() -> int:
    vertices = tuple(range(5))
    all_graph_edges = tuple(frozenset(e) for e in combinations(vertices, 2))
    checked = 0
    # A deterministic collection spanning regular, connected irregular, and
    # disconnected examples; every identity is exact over Fraction.
    masks = (0b1111111111, 0b0001111111, 0b1011010110, 0b1110110101)
    for mask in masks:
        edges = tuple(edge for i, edge in enumerate(all_graph_edges) if mask >> i & 1)
        roots = tuple(v for v in vertices if sum(v in edge for edge in edges) >= 2)
        if not roots:
            continue
        ds = [sum(v in edge for edge in edges) for v in roots]
        c = min(ds) - 1
        if c < 1 or not any(d > c for d in ds):
            continue
        decomposition(edges, roots, 2, c)
        checked += 1
    return checked


def punctured_r3_check() -> dict[str, str]:
    r = 3
    b = 2 * r + 1
    base = punctured_edge(tuple(range(b)), r)
    edges = tuple(
        edge
        for word in permutations(range(b))
        if not ((edge := punctured_edge(word, r)) & base)
    )
    assert len(edges) == 578
    roots = tuple(
        (0, mask)
        for mask in range(1 << b)
        if mask.bit_count() == r and (0, mask) not in base
    )
    degrees = Counter(v for edge in edges for v in edge)
    # Integer c keeps the exact audit rational and selects a genuine upper tail.
    c = 132
    assert min(degrees[v] for v in roots) < c < max(degrees[v] for v in roots)
    answer = decomposition(edges, roots, 12, c)
    return {key: str(value) for key, value in answer.items()}


def main() -> None:
    generic = exhaustive_generic_checks()
    punctured = punctured_r3_check()
    print(
        "GATE_A_EXTERNAL_UNION_DECOMPOSITION_PASS",
        {"generic_cases": generic, "punctured_r3": punctured},
        flush=True,
    )


if __name__ == "__main__":
    main()
