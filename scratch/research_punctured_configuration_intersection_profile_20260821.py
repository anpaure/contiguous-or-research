#!/usr/bin/env python3
"""Exact small-r intersection profile of directed punctured-wreath edges.

Research-only diagnostic; run substantive instances on H100.  A directed
configuration is a permutation w of [2r+1].  Its edge consists of the
2r clean r-windows and the 2r clean (r-1)-windows, with cyclic start 0
deleted in both ranks.  By coordinate transitivity it suffices to compare
every edge with the identity edge.
"""

from __future__ import annotations

import argparse
from collections import Counter
from itertools import permutations
from math import comb, factorial


def windows_edge(word: tuple[int, ...], r: int) -> frozenset[tuple[int, int]]:
    b = 2 * r + 1
    answer: set[tuple[int, int]] = set()
    for k, layer in ((r, 0), (r - 1, 1)):
        for start in range(1, b):
            mask = 0
            for j in range(k):
                mask |= 1 << word[(start + j) % b]
            answer.add((layer, mask))
    assert len(answer) == 4 * r
    return frozenset(answer)


def run(r: int) -> None:
    b = 2 * r + 1
    base = windows_edge(tuple(range(b)), r)
    hist = Counter()
    vertex_hits = Counter()
    pair_sum = 0
    for word in permutations(range(b)):
        edge = windows_edge(word, r)
        overlap = len(base & edge)
        hist[overlap] += 1
        pair_sum += comb(overlap, 2)
        for vertex in base & edge:
            vertex_hits[vertex] += 1

    middle_degrees = {value for (layer, _), value in vertex_hits.items() if layer == 0}
    lower_degrees = {value for (layer, _), value in vertex_hits.items() if layer == 1}
    expected_middle = 2 * r * factorial(r) * factorial(r + 1)
    expected_lower = 2 * (r + 2) * factorial(r) * factorial(r + 1)
    assert middle_degrees == {expected_middle}
    assert lower_degrees == {expected_lower}
    assert sum(hist.values()) == factorial(b)
    print(
        "PUNCTURED_CONFIG_INTERSECTION",
        {
            "r": r,
            "b": b,
            "edge_rank": 4 * r,
            "edge_count_indexed": factorial(b),
            "intersection_hist": sorted(hist.items()),
            "internal_pair_codegree_sum": pair_sum,
            "D_middle": expected_middle,
            "D_lower": expected_lower,
            "S_over_Dmiddle": pair_sum / expected_middle,
            "S_over_rank_Dmiddle": pair_sum / (4 * r * expected_middle),
        },
        flush=True,
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--r", type=int, nargs="+", default=[2, 3, 4])
    args = parser.parse_args()
    for value in args.r:
        run(value)
