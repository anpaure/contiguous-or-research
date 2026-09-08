#!/usr/bin/env python3
"""Test whether fixed-anchor octahedral squares form a Markov basis.

Enumerates small uniform-degree fibers and their nonnegative move graph.
This tests a precise nonnegative-reachability lemma; intended for H100 only.
"""

from __future__ import annotations

import argparse
from collections import Counter, deque
from itertools import combinations, combinations_with_replacement


def anchored_moves(n, k):
    infinity = n - 1
    targets = tuple(combinations(range(n), k))
    index = {target: i for i, target in enumerate(targets)}
    moves = set()
    for core_tuple in combinations(range(n - 1), k - 2):
        core = set(core_tuple)
        outside = tuple(point for point in range(n - 1) if point not in core)
        for a in outside:
            for b, c in combinations((point for point in outside if point != a), 2):
                positive = tuple(sorted((
                    index[tuple(sorted(core | {a, b}))],
                    index[tuple(sorted(core | {infinity, c}))],
                )))
                negative = tuple(sorted((
                    index[tuple(sorted(core | {a, c}))],
                    index[tuple(sorted(core | {infinity, b}))],
                )))
                if positive != negative:
                    moves.add((positive, negative) if positive < negative
                              else (negative, positive))
    return targets, tuple(moves)


def uniform_fiber(n, k, degree):
    targets, moves = anchored_moves(n, k)
    edge_count_numerator = n * degree
    assert edge_count_numerator % k == 0
    edge_count = edge_count_numerator // k
    states = []
    for multiset in combinations_with_replacement(range(len(targets)), edge_count):
        point_degrees = [0] * n
        for target_index in multiset:
            for point in targets[target_index]:
                point_degrees[point] += 1
        if point_degrees == [degree] * n:
            counter = Counter(multiset)
            states.append(tuple(counter.get(i, 0) for i in range(len(targets))))
    state_set = set(states)
    seen = set()
    component_sizes = []
    for start in states:
        if start in seen:
            continue
        queue = deque([start])
        seen.add(start)
        size = 0
        while queue:
            state = queue.popleft()
            size += 1
            for left, right in moves:
                for donors, recipients in ((left, right), (right, left)):
                    if any(state[index] == 0 for index in donors):
                        continue
                    nxt = list(state)
                    for index in donors:
                        nxt[index] -= 1
                    for index in recipients:
                        nxt[index] += 1
                    nxt = tuple(nxt)
                    assert nxt in state_set
                    if nxt not in seen:
                        seen.add(nxt)
                        queue.append(nxt)
        component_sizes.append(size)
    return {
        "n": n,
        "k": k,
        "degree": degree,
        "edge_count": edge_count,
        "targets": len(targets),
        "moves": len(moves),
        "fiber_states": len(states),
        "components": len(component_sizes),
        "component_sizes": sorted(component_sizes, reverse=True),
    }


def main(cases):
    for raw in cases:
        n, k, degree = map(int, raw.split(","))
        print("ANCHORED_SQUARE_MARKOV", uniform_fiber(n, k, degree), flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--case", action="append", dest="cases",
                        default=["5,2,2", "6,3,2"])
    arguments = parser.parse_args()
    main(arguments.cases)
