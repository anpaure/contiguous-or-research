#!/usr/bin/env python3
"""Audit the odd-dimensional GK/complement-SCD central diamonds.

For n=2r-1 and every (r-1)-set L, let f0(L) be its upward successor in
the standard Greene--Kleitman SCD and f1(L) its upward successor in the
complement SCD.  The edge f0(L)f1(L) has lower colour L and upper colour
f0(L) union f1(L).  This script reports upper-fibre multiplicities and the
cycle decomposition of the resulting 2-regular middle-owner graph.
"""

import argparse
import itertools
from collections import Counter, defaultdict


def masks(n, rank):
    for cc in itertools.combinations(range(n), rank):
        yield sum(1 << i for i in cc)


def unmatched(word, n):
    stack = []
    free_ones = []
    for i in range(n):
        if (word >> i) & 1:
            if stack:
                stack.pop()
            else:
                free_ones.append(i)
        else:
            stack.append(i)
    return free_ones, stack


def gk_up(word, n):
    _, free_zeros = unmatched(word, n)
    assert free_zeros
    return word | (1 << free_zeros[0])


def gk_down(word, n):
    free_ones, _ = unmatched(word, n)
    assert free_ones
    return word ^ (1 << free_ones[-1])


def complement_up(word, n):
    full = (1 << n) - 1
    return full ^ gk_down(full ^ word, n)


def cycle_data(successor):
    seen = set()
    cycles = []
    cycle_of = {}
    for start in successor:
        if start in seen:
            continue
        x = start
        vertices = []
        while x not in seen:
            seen.add(x)
            cycle_of[x] = len(cycles)
            vertices.append(x)
            x = successor[x]
        assert x == start
        cycles.append(vertices)
    return cycles, cycle_of


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("r", type=int)
    args = parser.parse_args()
    r = args.r
    n = 2 * r - 1
    fibre = Counter()
    occurrence = defaultdict(list)
    successor = {}
    for lower in masks(n, r - 1):
        tail = gk_up(lower, n)
        head = complement_up(lower, n)
        assert tail != head
        assert tail not in successor
        successor[tail] = head
        upper = tail | head
        fibre[upper] += 1
        occurrence[upper].append(tail)
    upper_total = sum(1 for _ in masks(n, r + 1))
    histogram = Counter(fibre.values())
    missing = upper_total - len(fibre)
    cycles, cycle_of = cycle_data(successor)
    flexible = []
    for vertices in cycles:
        labels = [tail | successor[tail] for tail in vertices]
        flexible.append(sum(fibre[u] >= 2 for u in labels))
    print("r", r, "owners", len(successor), "uppers", upper_total,
          "covered", len(fibre), "missing", missing,
          "fibre_hist", dict(sorted(histogram.items())),
          "cycles", len(cycles), "cycle_hist", dict(sorted(Counter(map(len, cycles)).items())),
          "max_cycle", max(map(len, cycles), default=0),
          "min_flexible", min(flexible, default=0),
          "zero_flexible", sum(x == 0 for x in flexible))


if __name__ == "__main__":
    main()
