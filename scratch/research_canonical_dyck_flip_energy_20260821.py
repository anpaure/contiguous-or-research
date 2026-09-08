#!/usr/bin/env python3
"""Weighted energy drift on the canonical Dyck adjacent-flip C8 graph.

Uses the exact empirical/theorem candidate that every adjacent 10->01 Dyck
flip is one legal canonical two-row C8 switch.  Intended execution: H100.
"""

from __future__ import annotations

import argparse
import math
from collections import Counter

from research_b9_c8_current_lattice_20260821 import (
    dyck_words,
    msw_row,
    switches,
    windows,
)


def energy(counter):
    return sum(value * (value - 1) // 2 for value in counter.values())


def audit_r(r):
    n = 2 * r + 1
    k = r - 1
    words = tuple(dyck_words(r))
    word_set = set(words)
    rows = {word: msw_row(word) for word in words}
    row_shadow = {word: Counter(windows(rows[word], k)) for word in words}
    shadow = Counter()
    for counter in row_shadow.values():
        shadow.update(counter)

    edges = []
    adjacent_candidates = 0
    for word in words:
        for position in range(2 * r - 1):
            if word[position:position + 2] != "10":
                continue
            mate = word[:position] + "01" + word[position + 2:]
            if mate not in word_set:
                continue
            adjacent_candidates += 1
            alternates = switches(rows[word], rows[mate], r)
            if not alternates:
                continue
            assert len(alternates) == 1, (r, word, mate, len(alternates))
            old = row_shadow[word] + row_shadow[mate]
            new = Counter(target for row in alternates[0]
                          for target in windows(row, k))
            current = new.copy()
            current.subtract(old)
            current = Counter({target: value for target, value in current.items()
                               if value})
            assert sorted(current.values()) == [-1, -1, 1, 1]
            delta = sum(
                (shadow[target] + value) * (shadow[target] + value - 1) // 2
                - shadow[target] * (shadow[target] - 1) // 2
                for target, value in current.items()
            )
            edges.append((word, mate, delta))

    expected_edges = (2 * r - 1) * math.comb(2 * r - 4, r - 2) // (r - 1)
    assert len(edges) == expected_edges, (r, len(edges), expected_edges)
    improving = [(left, right, -delta) for left, right, delta in edges if delta < 0]
    delta_histogram = Counter(delta for _, _, delta in edges)
    degree = Counter()
    for left, right, gain in improving:
        degree[left] += 1
        degree[right] += 1
    total_gain = sum(gain for _, _, gain in improving)
    maximum_degree = max(degree.values(), default=0)
    guaranteed_gain = total_gain / maximum_degree if maximum_degree else 0
    exact_matching_gain = None
    if len(words) <= 20_000:
        import networkx as nx
        graph = nx.Graph()
        for left, right, gain in improving:
            graph.add_edge(left, right, weight=gain)
        matching = nx.max_weight_matching(graph, weight="weight")
        exact_matching_gain = sum(graph[left][right]["weight"]
                                  for left, right in matching)
    A = math.comb(n, r)
    N = math.comb(n, k)
    gap = energy(shadow) - (A - N)
    return {
        "r": r,
        "rows": len(words),
        "edges": len(edges),
        "adjacent_dyck_flip_candidates": adjacent_candidates,
        "improving_edges": len(improving),
        "delta_histogram": dict(delta_histogram),
        "total_improving_gain": total_gain,
        "improving_max_degree": maximum_degree,
        "base_gap": gap,
        "konig_gain": guaranteed_gain,
        "exact_max_weight_matching_gain": exact_matching_gain,
        "exact_post_matching_ratio_A_over_r": (
            None if exact_matching_gain is None
            else (gap - exact_matching_gain) / (A / r)
        ),
        "post_konig_gap": gap - guaranteed_gain,
        "post_konig_ratio_A_over_r": (gap - guaranteed_gain) / (A / r),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--r-min", type=int, default=3)
    parser.add_argument("--r-max", type=int, default=9)
    arguments = parser.parse_args()
    for rank in range(arguments.r_min, arguments.r_max + 1):
        print("CANONICAL_DYCK_FLIP_ENERGY", audit_r(rank), flush=True)
