#!/usr/bin/env python3
"""Inspect explicit missing second-shadow targets in the canonical MSW factor."""

from itertools import combinations
import sys


def dyck_masks(m):
    def rec(p, up, down, mask):
        if p == 2 * m:
            yield mask
            return
        if up < m:
            yield from rec(p + 1, up + 1, down, mask | (1 << p))
        if down < up:
            yield from rec(p + 1, up, down + 1, mask)

    yield from rec(0, 0, 0, 0)


def g(x, m):
    height = 0
    d0 = 0
    before = []
    for i in range(2 * m):
        before.append(height)
        if (x >> i) & 1:
            height += 1
        else:
            if height == 0:
                d0 += 1
            height -= 1
    touching = 0
    for i, height in enumerate(before):
        if not ((x >> i) & 1) and height in (0, 1):
            touching += 1
            if touching == d0 + 1:
                return x | (1 << i), i
    raise AssertionError


def h(x, m):
    height = 0
    u1 = 0
    before = []
    for i in range(2 * m):
        before.append(height)
        if (x >> i) & 1:
            if height == 1:
                u1 += 1
            height += 1
        else:
            height -= 1
    touching = 0
    for i, height in enumerate(before):
        if ((x >> i) & 1) and height in (0, 1):
            touching += 1
            if touching == u1:
                return x & ~(1 << i), i
    raise AssertionError


def canonical_orders(m):
    for root in dyck_masks(m):
        x = root
        omitted = []
        for _ in range(m):
            x, arrived = g(x, m)
            x, departed = h(x, m)
            omitted.extend((arrived + 1, departed + 1))
        omitted.append(2 * m + 1)
        yield [omitted[(2 * j) % (2 * m + 1)] for j in range(2 * m + 1)]


def occurrences(m, target):
    n = 2 * m + 1
    target = frozenset(target)
    hits = []
    for root, order in enumerate(canonical_orders(m)):
        for i in range(n):
            if frozenset(order[(i + j) % n] for j in range(m - 1)) == target:
                hits.append((root, i, order))
    return hits


def adjacency_profile(m, target):
    target = frozenset(target)
    n = 2 * m + 1
    profiles = {}
    maximum = -1
    example = None
    for root, order in enumerate(canonical_orders(m)):
        internal = []
        for i in range(n):
            edge = frozenset((order[i], order[(i + 1) % n]))
            if edge <= target:
                internal.append(tuple(sorted(edge)))
        if len(internal) > maximum:
            maximum = len(internal)
            example = (root, order, internal)
        profiles[len(internal)] = profiles.get(len(internal), 0) + 1
    return maximum, profiles, example


def main():
    hi = int(sys.argv[1]) if len(sys.argv) > 1 else 11
    for m in range(4, hi + 1):
        candidate = list(range(1, m - 2)) + [2 * m - 4, 2 * m - 1]
        maximum, profile, example = adjacency_profile(m, candidate)
        print(m, candidate, len(occurrences(m, candidate)), maximum, profile)
        print("  max root/order/edges", example)


if __name__ == "__main__":
    main()
