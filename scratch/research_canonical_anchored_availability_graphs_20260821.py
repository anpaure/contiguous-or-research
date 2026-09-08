#!/usr/bin/env python3
"""Canonical fixed-anchor Johnson availability graphs from legal C8 switches.

For every non-anchor pivot a, builds G_a on (k-1)-sets B using every C8
square currently legal in the canonical MSW factor whose pivot contains the
fixed appended label.  Intended execution: H100 only.
"""

from __future__ import annotations

import argparse
import math
from collections import Counter, defaultdict
from itertools import combinations

from research_b9_c8_current_lattice_20260821 import (
    dyck_words,
    msw_row,
    switches,
    windows,
)


class UnionFind:
    def __init__(self, items):
        self.parent = {item: item for item in items}
        self.size = {item: 1 for item in items}

    def find(self, item):
        root = item
        while self.parent[root] != root:
            root = self.parent[root]
        while self.parent[item] != item:
            nxt = self.parent[item]
            self.parent[item] = root
            item = nxt
        return root

    def union(self, left, right):
        left = self.find(left)
        right = self.find(right)
        if left == right:
            return
        if self.size[left] < self.size[right]:
            left, right = right, left
        self.parent[right] = left
        self.size[left] += self.size[right]

    def component_sizes(self):
        counts = Counter(self.find(item) for item in self.parent)
        return sorted(counts.values(), reverse=True)


def current_of_pair(old_pair, new_pair, k):
    old = Counter(target for row in old_pair for target in windows(row, k))
    new = Counter(target for row in new_pair for target in windows(row, k))
    new.subtract(old)
    return {target: value for target, value in new.items() if value}


def anchored_edge(current, anchor, k):
    if sorted(current.values()) != [-1, -1, 1, 1]:
        return None
    support = tuple(current)
    core = set.intersection(*(set(target) for target in support))
    if len(core) != k - 2 or anchor in core:
        return None
    pivot = set.union(*(set(target) for target in support)) - core
    if len(pivot) != 4 or anchor not in pivot:
        return None
    anchored = tuple(target for target in support if anchor in target)
    nonanchored = tuple(target for target in support if anchor not in target)
    if len(anchored) != 2 or len(nonanchored) != 2:
        return None
    extra_common = (set(nonanchored[0]) & set(nonanchored[1])) - core
    if len(extra_common) != 1:
        return None
    a = next(iter(extra_common))
    vertices = []
    for target in anchored:
        vertex = frozenset(set(target) - {anchor})
        if len(vertex) != k - 1 or a in vertex:
            return None
        vertices.append(vertex)
    if len(set(vertices)) != 2:
        return None
    assert current[anchored[0]] == -current[anchored[1]]
    assert current[nonanchored[0]] == -current[nonanchored[1]]
    return a, tuple(sorted(vertices, key=lambda item: tuple(sorted(item))))


def audit_r(r):
    n = 2 * r + 1
    k = r - 1
    anchor = n
    rows = tuple(sorted(msw_row(word) for word in dyck_words(r)))
    shadow = Counter(target for row in rows for target in windows(row, k))
    switch_cache = {}
    currents = {}
    current_pairs = {}
    row_pair_count = 0
    alternate_pair_count = 0
    for left, right in combinations(rows, 2):
        row_pair_count += 1
        old_pair = tuple(sorted((left, right)))
        alternates = switches(left, right, r)
        alternate_pair_count += len(alternates)
        for new_pair in alternates:
            current = current_of_pair(old_pair, new_pair, k)
            key = tuple(sorted((tuple(sorted(target)), value)
                               for target, value in current.items()))
            negative = tuple(sorted((target, -value) for target, value in key))
            canonical_key = min(key, negative)
            currents[canonical_key] = current
            current_pairs[canonical_key] = old_pair

    ground = tuple(range(1, n))
    graphs = {}
    for a in ground:
        vertices = tuple(frozenset(vertex)
                         for vertex in combinations((x for x in ground if x != a),
                                                    k - 1))
        graphs[a] = UnionFind(vertices)

    anchored_currents = 0
    edge_sets = defaultdict(set)
    for current in currents.values():
        parsed = anchored_edge(current, anchor, k)
        if parsed is None:
            continue
        anchored_currents += 1
        a, edge = parsed
        edge_sets[a].add(edge)
        graphs[a].union(*edge)

    all_targets = tuple(frozenset(target)
                        for target in combinations(range(1, n + 1), k))
    bad_targets = {target for target in all_targets
                   if shadow[target] == 0 or shadow[target] >= 3}
    touched_bad = bad_targets & set().union(
        *(set(current) for current in currents.values())
    ) if currents else set()
    bad_incidence = Counter()
    improving = 0
    neutral = 0
    worsening = 0
    best_delta = None
    total_improving_gain = 0
    improving_row_degree = Counter()
    for key, current in currents.items():
        delta = sum(
            (shadow[target] * value + value * (value - 1) // 2)
            for target, value in current.items()
        )
        # Since value is +/-1, use the direct collision-energy check to
        # avoid relying on a signed-binomial shorthand.
        direct_delta = sum(
            (shadow[target] + value) * (shadow[target] + value - 1) // 2
            - shadow[target] * (shadow[target] - 1) // 2
            for target, value in current.items()
        )
        assert delta == direct_delta
        best_delta = delta if best_delta is None else min(best_delta, delta)
        improving += delta < 0
        neutral += delta == 0
        worsening += delta > 0
        if delta < 0:
            total_improving_gain += -delta
            left, right = current_pairs[key]
            improving_row_degree[left] += 1
            improving_row_degree[right] += 1
        for target in set(current) & bad_targets:
            bad_incidence[target] += 1

    component_hist = Counter()
    isolated_total = 0
    component_excess = 0
    edge_hist = Counter()
    largest_hist = Counter()
    per_a = {}
    for a in ground:
        sizes = graphs[a].component_sizes()
        component_hist[len(sizes)] += 1
        isolated = sum(size == 1 for size in sizes)
        isolated_total += isolated
        component_excess += len(sizes) - 1
        edge_hist[len(edge_sets[a])] += 1
        largest_hist[sizes[0]] += 1
        per_a[a] = {
            "edges": len(edge_sets[a]),
            "components": len(sizes),
            "isolated": isolated,
            "largest": sizes[0],
            "size_hist": dict(Counter(sizes)),
        }

    A = math.comb(n, r)
    N = len(all_targets)
    base_energy = sum(value * (value - 1) // 2 for value in shadow.values())
    base_gap = base_energy - (A - N)
    improving_max_degree = max(improving_row_degree.values(), default=0)
    konig_gain_lower_bound = (0 if improving_max_degree == 0 else
                              total_improving_gain / improving_max_degree)
    return {
        "r": r,
        "rows": len(rows),
        "row_pairs": row_pair_count,
        "legal_alternate_pairs": alternate_pair_count,
        "distinct_currents": len(currents),
        "anchored_currents": anchored_currents,
        "bad_targets": len(bad_targets),
        "touched_bad_targets": len(touched_bad),
        "untouched_bad_targets": len(bad_targets - touched_bad),
        "bad_current_degree_hist": dict(Counter(bad_incidence.values())),
        "improving_neutral_worsening_currents": (improving, neutral, worsening),
        "best_energy_delta": best_delta,
        "base_energy_gap": base_gap,
        "total_improving_gain": total_improving_gain,
        "improving_max_row_degree": improving_max_degree,
        "konig_matching_gain_lower_bound": konig_gain_lower_bound,
        "post_konig_gap_upper_bound": base_gap - konig_gain_lower_bound,
        "post_konig_gap_over_A_div_r": ((base_gap - konig_gain_lower_bound)
                                         / (A / r)),
        "vertices_per_Ga": math.comb(n - 2, k - 1),
        "component_excess": component_excess,
        "component_excess_over_A_div_r": component_excess / (A / r),
        "isolated_total": isolated_total,
        "component_count_hist_over_a": dict(component_hist),
        "edge_count_hist_over_a": dict(edge_hist),
        "largest_component_hist_over_a": dict(largest_hist),
        "per_a": per_a,
    }


def main(r_min, r_max):
    for r in range(r_min, r_max + 1):
        print("CANONICAL_ANCHORED_AVAILABILITY", audit_r(r), flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--r-min", type=int, default=3)
    parser.add_argument("--r-max", type=int, default=6)
    arguments = parser.parse_args()
    main(arguments.r_min, arguments.r_max)
