#!/usr/bin/env python3
"""Audit diamonds formed by predecessors from two GK scan conventions."""

from __future__ import annotations

import argparse
import collections
import itertools


def free_ones(mask: int, order: list[int]) -> list[int]:
    stack: list[int] = []
    paired: set[int] = set()
    for i in order:
        if (mask >> i) & 1:
            stack.append(i)
        elif stack:
            j = stack.pop()
            paired.add(i)
            paired.add(j)
    return [i for i in order if ((mask >> i) & 1) and i not in paired]


def masks_of_weight(n: int, r: int):
    for comb in itertools.combinations(range(n), r):
        x = 0
        for i in comb:
            x |= 1 << i
        yield x


def shifted_order(n: int, shift: int, reverse: bool) -> list[int]:
    if reverse:
        return [(shift - j) % n for j in range(n)]
    return [(shift + j) % n for j in range(n)]


def audit(m: int) -> None:
    n = 2 * m + 1
    uppers = list(masks_of_weight(n, m + 2))
    for delta in range(n):
        lowers = collections.Counter()
        owners0 = collections.Counter()
        owners1 = collections.Counter()
        same = 0
        missing = 0
        order0 = shifted_order(n, 0, False)
        order1 = shifted_order(n, delta, True)
        for upper in uppers:
            f0 = free_ones(upper, order0)
            f1 = free_ones(upper, order1)
            if not f0 or not f1:
                missing += 1
                continue
            p, q = f0[0], f1[0]
            if p == q:
                same += 1
                continue
            a = upper ^ (1 << p)
            b = upper ^ (1 << q)
            lower = upper ^ (1 << p) ^ (1 << q)
            owners0[a] += 1
            owners1[b] += 1
            lowers[lower] += 1
        joint = collections.Counter(owners0)
        joint.update(owners1)
        print(
            "m", m,
            "delta", delta,
            "selected", sum(lowers.values()),
            "same", same,
            "missing", missing,
            "lower_max", max(lowers.values(), default=0),
            "A_max", max(owners0.values(), default=0),
            "B_max", max(owners1.values(), default=0),
            "owner_max", max(joint.values(), default=0),
            "lower_dups", sum(v - 1 for v in lowers.values()),
        )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("m", nargs="+", type=int)
    args = parser.parse_args()
    for m in args.m:
        audit(m)


if __name__ == "__main__":
    main()
