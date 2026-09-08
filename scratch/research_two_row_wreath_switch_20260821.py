#!/usr/bin/env python3
"""Check and profile the dimension-free 2x2 cyclic-window trade."""

from __future__ import annotations

import argparse
from collections import Counter
from itertools import product


def rows(r):
    a, b, c, d = range(4)
    P = tuple(range(4, 4 + r - 1))
    Q = tuple(range(4 + r - 1, 4 + r - 1 + r - 2))
    old = ((a, b) + P + (c, d) + Q, (c, a) + P + (d, b) + Q)
    new = ((a, c) + P + (b, d) + Q, (b, a) + P + (d, c) + Q)
    assert all(len(x) == 2 * r + 1 for x in old + new)
    return old, new


def windows(order, k):
    n = len(order)
    return tuple(
        frozenset(order[(i + j) % n] for j in range(k)) for i in range(n)
    )


def odd_edges(order, r):
    vertices = windows(order, r)
    return {
        frozenset((vertices[i], vertices[j]))
        for i in range(len(vertices))
        for j in range(i + 1, len(vertices))
        if vertices[i].isdisjoint(vertices[j])
    }


def ribbon(order, r, reverse=False):
    order = tuple(reversed(order)) if reverse else tuple(order)
    b = len(order)
    return {
        frozenset(order[(i + j) % b] for j in range(r)):
        frozenset(order[(i + j) % b] for j in range(r - 1))
        for i in range(b)
    }


def main(max_r):
    for r in range(2, max_r + 1):
        old, new = rows(r)
        old_middle = Counter(x for row in old for x in windows(row, r))
        new_middle = Counter(x for row in new for x in windows(row, r))
        assert old_middle == new_middle
        assert max(old_middle.values()) == 1
        depth = []
        for q in range(1, r):
            old_count = Counter(x for row in old for x in windows(row, r - q))
            new_count = Counter(x for row in new for x in windows(row, r - q))
            loss = old_count - new_count
            gain = new_count - old_count
            depth.append(
                (
                    q,
                    sum(loss.values()),
                    sum(gain.values()),
                    len(loss),
                    len(gain),
                )
            )
        old_edges = set().union(*(odd_edges(row, r) for row in old))
        new_edges = set().union(*(odd_edges(row, r) for row in new))
        assert len(old_edges) == len(new_edges) == 2 * (2 * r + 1)
        best_ribbon = None
        for old_bits in product((0, 1), repeat=2):
            old_map = {}
            for i in range(2):
                old_map.update(ribbon(old[i], r, bool(old_bits[i])))
            for new_bits in product((0, 1), repeat=2):
                new_map = {}
                for i in range(2):
                    new_map.update(ribbon(new[i], r, bool(new_bits[i])))
                changed = {x for x in old_map if old_map[x] != new_map[x]}
                candidate = (len(changed), old_bits, new_bits, changed)
                if best_ribbon is None or candidate[:3] < best_ribbon[:3]:
                    best_ribbon = candidate
        assert best_ribbon is not None
        old_bits, new_bits = best_ribbon[1], best_ribbon[2]
        old_maps = [ribbon(old[i], r, bool(old_bits[i])) for i in range(2)]
        new_maps = [ribbon(new[i], r, bool(new_bits[i])) for i in range(2)]
        old_owner = {x: i for i, z in enumerate(old_maps) for x in z}
        new_owner = {x: i for i, z in enumerate(new_maps) for x in z}
        changed = best_ribbon[3]
        absorb = max(
            (
                len({x, y} & changed)
                for x in old_owner
                for y in old_owner
                if x != y
                and old_owner[x] != old_owner[y]
                and new_owner[x] != new_owner[y]
            ),
            default=0,
        )
        print(
            {
                "r": r,
                "b": 2 * r + 1,
                "odd_common": len(old_edges & new_edges),
                "odd_changed_each": len(old_edges - new_edges),
                "ribbon_changed": best_ribbon[0],
                "ribbon_dirty_absorb": absorb,
                "depth": depth,
            },
            flush=True,
        )
        if r in (4, 5):
            new_owner = {
                x: (j, i)
                for j, row in enumerate(new)
                for i, x in enumerate(windows(row, r))
            }
            mapping = []
            old_owner = {
                x: (j, i)
                for j, row in enumerate(old)
                for i, x in enumerate(windows(row, r))
            }
            for j, row in enumerate(old):
                mapping.append([new_owner[x] for x in windows(row, r)])
            print("middle_mapping", r, mapping, flush=True)
            def edge_ids(row_collection):
                answer = set()
                for row in row_collection:
                    for edge in odd_edges(row, r):
                        answer.add(frozenset(old_owner[x] for x in edge))
                return answer
            oe = edge_ids(old)
            ne = edge_ids(new)
            print("odd_red", r, sorted(tuple(sorted(x)) for x in oe - ne), flush=True)
            print("odd_blue", r, sorted(tuple(sorted(x)) for x in ne - oe), flush=True)
            old_first = Counter(x for row in old for x in windows(row, r - 1))
            new_first = Counter(x for row in new for x in windows(row, r - 1))
            print(
                "q1_loss_gain",
                r,
                [sorted(x) for x in (old_first - new_first).elements()],
                [sorted(x) for x in (new_first - old_first).elements()],
                flush=True,
            )
            for q in range(2, r - 1):
                oc = Counter(x for row in old for x in windows(row, r - q))
                nc = Counter(x for row in new for x in windows(row, r - q))
                print(
                    "q_loss_gain",
                    r,
                    q,
                    [sorted(x) for x in (oc - nc).elements()],
                    [sorted(x) for x in (nc - oc).elements()],
                    flush=True,
                )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-r", type=int, default=100)
    args = parser.parse_args()
    main(args.max_r)
