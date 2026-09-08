#!/usr/bin/env python3
"""Exact small-b profile for flagged ribbons in punctured wreaths.

Run only on H100.  A punctured wreath configuration consists of a cyclic
order and one dirty rank-r window.  Pair the remaining 2r windows into the
r disjoint opposite pairs used by the paired-Kneser auxiliary hypergraph.
Attach to each endpoint the rank-(r-1) prefix window at the same start.
The resulting four-object flag (X,Y,S,T), S subset X and T subset Y, is a
``ribbon''.  This script measures the r-uniform grouping hypergraph on
ribbons and the underlying fixed-rank four-part incidence hypergraph.
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


def ribbon_key(x: int, y: int, s: int, t: int):
    assert not (x & y)
    assert s & ~x == 0 and t & ~y == 0
    assert x.bit_count() == y.bit_count() == s.bit_count() + 1 == t.bit_count() + 1
    return ((x, s), (y, t)) if x < y else ((y, t), (x, s))


def enumerate_profile(b: int):
    r = (b - 1) // 2
    edge_mult = Counter()
    config_records = []
    all_ribbons = set()
    four_edges = set()
    pair_distance = {}

    for tail in permutations(range(1, b)):
        order = (0,) + tail
        # Keep both directions.  The unoriented wreath has the same middle
        # and lower decks after reversal, but its canonical pairing of each
        # clean middle endpoint with the prefix lower window changes.  Thus
        # the ribbon-grouping object is genuinely directed.
        mid = windows(order, r)
        low = windows(order, r - 1)
        for dirty in range(b):
            rr = []
            for k in range(1, r + 1):
                i = (dirty + k) % b
                j = (i + r) % b
                f = ribbon_key(mid[i], mid[j], low[i], low[j])
                rr.append(f)
                all_ribbons.add(f)
                four_edges.add((mid[i], mid[j], low[i], low[j]))
            key = tuple(sorted(rr))
            edge_mult[key] += 1
            config_records.append((order, dirty, key))
            for a, c in combinations(range(r), 2):
                pair = tuple(sorted((rr[a], rr[c])))
                d = c - a
                old = pair_distance.setdefault(pair, d)
                assert old == d

    edges = list(edge_mult)
    degree = Counter()
    codegree = Counter()
    pair_examples = defaultdict(list)
    for edge in edges:
        for f in edge:
            degree[f] += 1
        for pair in combinations(edge, 2):
            codegree[pair] += 1
            if len(pair_examples[pair]) < 2:
                pair_examples[pair].append(edge)

    return all_ribbons, edges, edge_mult, degree, codegree, pair_distance, four_edges


def audit_four_graph(b: int, ribbons):
    r = (b - 1) // 2
    middle = [x for x in range(1 << b) if x.bit_count() == r]
    lower = [x for x in range(1 << b) if x.bit_count() == r - 1]
    deg = Counter()
    cod = Counter()
    canonical_edges = set()
    for x in middle:
        for y in middle:
            if x >= y or x & y:
                continue
            for sx in range(b):
                if not (x >> sx) & 1:
                    continue
                s = x ^ (1 << sx)
                for ty in range(b):
                    if not (y >> ty) & 1:
                        continue
                    t = y ^ (1 << ty)
                    e = (('M', x), ('M', y), ('L', s), ('L', t))
                    canonical_edges.add(tuple(sorted(e)))
    for edge in canonical_edges:
        for v in edge:
            deg[v] += 1
        for pair in combinations(edge, 2):
            cod[pair] += 1
    middle_degrees = {deg[('M', x)] for x in middle}
    lower_degrees = {deg[('L', s)] for s in lower}
    assert middle_degrees == {r * r * (r + 1)}
    assert lower_degrees == {r * (r + 1) * (r + 2)}
    assert max(cod.values()) <= r * (r + 1)
    # Every abstract four-edge is realized by some directed punctured-wreath
    # configuration, and a ribbon is exactly such a four-edge with the
    # endpoint attachment remembered.
    assert len(ribbons) == len(canonical_edges)
    return {
        'edges': len(canonical_edges),
        'middle_degree': next(iter(middle_degrees)),
        'lower_degree': next(iter(lower_degrees)),
        'max_codegree': max(cod.values()),
        'max_ratio_to_min_degree': max(cod.values()) / min(min(middle_degrees), min(lower_degrees)),
    }


def audit(b: int):
    r = (b - 1) // 2
    ribbons, edges, mult, degree, codegree, pair_distance, four_edges = enumerate_profile(b)
    assert len(edges) <= factorial(b)
    assert len(set(degree.values())) == 1
    expected_degree = 2 * factorial(r) * factorial(r - 1)
    assert set(degree.values()) == {expected_degree}
    expected_pair = (r - 1) * factorial(r - 2) ** 2
    assert max(codegree.values(), default=0) == expected_pair
    higher = {}
    for t in range(3, r + 1):
        counts = Counter(
            subset for edge in edges for subset in combinations(edge, t)
        )
        value = max(counts.values(), default=0)
        expected = (r - t + 1) * factorial(r - t) ** 2
        assert value == expected
        higher[t] = value
    four = audit_four_graph(b, ribbons)
    hist = Counter(codegree.values())
    by_distance = defaultdict(set)
    for pair, value in codegree.items():
        by_distance[pair_distance[pair]].add(value)
    print(
        'PASS',
        {
            'b': b,
            'r': r,
            'ribbons': len(ribbons),
            'group_edges': len(edges),
            'ribbon_degree': next(iter(degree.values())),
            'max_pair_codegree': max(codegree.values(), default=0),
            'normalized_max_pair': max(codegree.values(), default=0) / next(iter(degree.values())),
            'higher_max_codegrees': higher,
            'pair_codegree_hist': sorted(hist.items()),
            'pair_codegree_by_distance': {
                d: sorted(values) for d, values in sorted(by_distance.items())
            },
            'four_graph': four,
        },
        flush=True,
    )


if __name__ == '__main__':
    for bb in (5, 7, 9):
        audit(bb)
