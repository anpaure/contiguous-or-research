#!/usr/bin/env python3
"""H100 audit of the punctured-wreath ribbon profile and scale gates."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations
from math import comb, factorial, lgamma, log


def windows(order, ell):
    b = len(order)
    return tuple(
        sum(1 << order[(i + j) % b] for j in range(ell))
        for i in range(b)
    )


def ribbon_key(x, y, s, t):
    assert not (x & y)
    assert s & ~x == 0 and t & ~y == 0
    a = ((x, s), (y, t))
    return a if a[0] < a[1] else (a[1], a[0])


def deep_ribbon_key(x, y, sx, sy):
    a = ((x, sx), (y, sy))
    return a if a[0] < a[1] else (a[1], a[0])


def enumerate_grouping(b):
    r = (b - 1) // 2
    multiplicity = Counter()
    edge_orders = {}
    ribbons = set()
    for tail in permutations(range(1, b)):
        order = (0,) + tail
        mid = windows(order, r)
        low = windows(order, r - 1)
        for dirty in range(b):
            edge = []
            for k in range(1, r + 1):
                i = (dirty + k) % b
                j = (i + r) % b
                ribbon = ribbon_key(mid[i], mid[j], low[i], low[j])
                edge.append(ribbon)
                ribbons.add(ribbon)
            key = tuple(sorted(edge))
            multiplicity[key] += 1
            edge_orders[key] = tuple(edge)
    return ribbons, multiplicity, edge_orders


def expected_gap_codegree(r, gaps):
    span = sum(gaps)
    u = r - span
    assert u >= 1
    value = u * factorial(u - 1) ** 2
    for d in gaps:
        if d >= 2:
            value *= factorial(d - 2) * factorial(d - 1)
    return value


def audit_four_graph(b, ribbons):
    r = (b - 1) // 2
    middle = [x for x in range(1 << b) if x.bit_count() == r]
    lower = [x for x in range(1 << b) if x.bit_count() == r - 1]
    edges = set()
    for x in middle:
        for y in middle:
            if x >= y or x & y:
                continue
            for ax in range(b):
                if not (x >> ax) & 1:
                    continue
                s = x ^ (1 << ax)
                for ay in range(b):
                    if not (y >> ay) & 1:
                        continue
                    t = y ^ (1 << ay)
                    edges.add(
                        tuple(sorted((('M', x), ('M', y), ('L', s), ('L', t))))
                    )
    degree = Counter()
    codegree = Counter()
    for edge in edges:
        for vertex in edge:
            degree[vertex] += 1
        for pair in combinations(edge, 2):
            codegree[pair] += 1
    assert len(edges) == len(ribbons)
    assert {degree[('M', x)] for x in middle} == {r * r * (r + 1)}
    assert {degree[('L', x)] for x in lower} == {r * (r + 1) * (r + 2)}
    assert max(codegree.values()) == r * (r + 1)
    return len(edges)


def audit_exact(b):
    r = (b - 1) // 2
    ribbons, multiplicity, edge_orders = enumerate_grouping(b)
    edges = tuple(multiplicity)
    assert len(edges) == factorial(b)
    assert set(multiplicity.values()) == {1}

    n = comb(b, r)
    expected_ribbons = n * (r + 1) * r * r // 2
    assert len(ribbons) == expected_ribbons
    audit_four_graph(b, ribbons)

    degree = Counter()
    for edge in edges:
        assert len(edge) == r
        for ribbon in edge:
            degree[ribbon] += 1
    D = 2 * factorial(r) * factorial(r - 1)
    assert set(degree.values()) == {D}

    # Direct configuration hypergraph on middle/lower target vertices.
    target_degree = Counter()
    target_codegree = Counter()
    for edge in edges:
        target_edge = set()
        for ribbon in edge:
            for x, s in ribbon:
                target_edge.add(('M', x))
                target_edge.add(('L', s))
        assert len(target_edge) == 4 * r
        for vertex in target_edge:
            target_degree[vertex] += 1
        for pair in combinations(sorted(target_edge), 2):
            target_codegree[pair] += 1
    middle = [x for x in range(1 << b) if x.bit_count() == r]
    lower = [x for x in range(1 << b) if x.bit_count() == r - 1]
    degree_middle_config = 2 * r * factorial(r) * factorial(r + 1)
    degree_lower_config = 2 * (r + 2) * factorial(r) * factorial(r + 1)
    assert {target_degree[('M', x)] for x in middle} == {
        degree_middle_config
    }
    assert {target_degree[('L', x)] for x in lower} == {
        degree_lower_config
    }
    common_disjoint_middle = 2 * (2 * r - 1) * factorial(r) ** 2
    assert {
        target_codegree[tuple(sorted((('M', x), ('M', y))))]
        for x, y in combinations(middle, 2)
        if not (x & y)
    } == {common_disjoint_middle}

    max_codegrees = {}
    for t in range(2, r + 1):
        counts = Counter(
            subset
            for edge in edges
            for subset in combinations(edge, t)
        )
        gaps_by_subset = {}
        for ordered_edge in edge_orders.values():
            for positions in combinations(range(r), t):
                subset = tuple(sorted(ordered_edge[i] for i in positions))
                gaps = tuple(
                    positions[j + 1] - positions[j] for j in range(t - 1)
                )
                old = gaps_by_subset.setdefault(subset, gaps)
                assert old == gaps
        assert counts.keys() == gaps_by_subset.keys()
        for subset, count in counts.items():
            assert count == expected_gap_codegree(r, gaps_by_subset[subset])
        got = max(counts.values())
        expected = (r - t + 1) * factorial(r - t) ** 2
        assert got == expected
        max_codegrees[t] = got

    return {
        'b': b,
        'r': r,
        'ribbons': len(ribbons),
        'directed_configurations': len(edges),
        'ribbon_degree': D,
        'max_codegrees': max_codegrees,
    }


def audit_multidepth_exact(b, H):
    r = (b - 1) // 2
    assert 1 <= H < r
    multiplicity = Counter()
    ribbons = set()
    for tail in permutations(range(1, b)):
        order = (0,) + tail
        decks = {
            ell: windows(order, ell) for ell in range(r - H, r + 1)
        }
        for dirty in range(b):
            edge = []
            for k in range(1, r + 1):
                i = (dirty + k) % b
                j = (i + r) % b
                sx = tuple(decks[r - q][i] for q in range(1, H + 1))
                sy = tuple(decks[r - q][j] for q in range(1, H + 1))
                ribbon = deep_ribbon_key(decks[r][i], decks[r][j], sx, sy)
                edge.append(ribbon)
                ribbons.add(ribbon)
            multiplicity[tuple(sorted(edge))] += 1
    edges = tuple(multiplicity)
    assert len(edges) == factorial(b)
    assert set(multiplicity.values()) == {1}

    falling = factorial(r) // factorial(r - H)
    expected_ribbons = comb(b, r) * (r + 1) * falling**2 // 2
    assert len(ribbons) == expected_ribbons
    degree = Counter(ribbon for edge in edges for ribbon in edge)
    expected_degree = 2 * r * factorial(r - H) ** 2
    assert set(degree.values()) == {expected_degree}

    max_codegrees = {}
    for t in range(2, r - H + 2):
        counts = Counter(
            subset for edge in edges for subset in combinations(edge, t)
        )
        expected = (r - t + 1) * factorial(r - H - t + 1) ** 2
        assert max(counts.values()) == expected
        max_codegrees[t] = expected
    return {
        'b': b,
        'r': r,
        'H': H,
        'ribbons': len(ribbons),
        'degree': expected_degree,
        'max_codegrees': max_codegrees,
    }


def audit_arithmetic(r):
    b = 2 * r + 1
    n_middle = comb(b, r)
    n_lower = comb(b, r - 1)
    n_ribbons = n_middle * (r + 1) * r * r // 2

    d_middle_four = r * r * (r + 1)
    d_lower_four = r * (r + 1) * (r + 2)
    c2_four = r * (r + 1)
    assert d_lower_four / d_middle_four == (r + 2) / r
    assert c2_four / d_middle_four == 1 / r

    D_group = 2 * factorial(r) * factorial(r - 1)
    C2_group = (r - 1) * factorial(r - 2) ** 2
    assert C2_group * (2 * r * (r - 1)) == D_group

    degree_middle_config = 2 * r * factorial(r) * factorial(r + 1)
    degree_lower_config = 2 * (r + 2) * factorial(r) * factorial(r + 1)
    common_disjoint_middle = 2 * (2 * r - 1) * factorial(r) ** 2
    ratio = common_disjoint_middle / degree_middle_config
    assert ratio == (2 * r - 1) / (r * (r + 1))

    max_target_disjoint_configs = n_lower // (2 * r)
    max_group_vertices_covered = r * max_target_disjoint_configs
    capacity_fraction = Fraction(max_group_vertices_covered, n_ribbons)
    ideal_capacity_fraction = Fraction(1, r * (r + 1) * (r + 2))
    assert capacity_fraction <= ideal_capacity_fraction
    # Floors are the only reason this may be strict: replacing floor(x) by x
    # changes the numerator by strictly less than r.
    assert ideal_capacity_fraction - capacity_fraction < Fraction(r, n_ribbons)

    rho = 1 / (r * (r + 1) * (r + 2))
    log_independent_expected = lgamma(b + 1) + r * log(rho)
    log_elementary_upper = log(2 * r + 1) + r * log(
        (2 * r + 1) ** 2 / (r * (r + 1) * (r + 2))
    )
    assert log_independent_expected <= log_elementary_upper

    return {
        'r': r,
        'log_D_group': log(D_group),
        'group_pair_ratio': C2_group / D_group,
        'direct_rank_scaled_pair_ratio': 4 * r * ratio,
        'capacity_fraction_of_group_vertices': float(capacity_fraction),
        'log_iid_expected_group_edges': log_independent_expected,
    }


def main():
    for b in (5, 7, 9):
        print('EXACT_PASS', audit_exact(b), flush=True)
    for b in (5, 7, 9):
        r = (b - 1) // 2
        for H in range(1, r):
            print('MULTIDEPTH_EXACT_PASS', audit_multidepth_exact(b, H), flush=True)
    for r in (4, 8, 16, 32, 64, 128, 256):
        print('ARITHMETIC_PASS', audit_arithmetic(r), flush=True)
    assert audit_arithmetic(256)['log_iid_expected_group_edges'] < log(1e-100)
    print('PASS audit_punctured_wreath_ribbon_profile_and_common_gate_20260821')


if __name__ == '__main__':
    main()
