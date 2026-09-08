#!/usr/bin/env python3
"""Census cyclic-rank rules for the second endpoint after fixed GK p."""

from __future__ import annotations

import argparse
import collections
import itertools


def masks(n: int, r: int):
    for c in itertools.combinations(range(n), r):
        x = 0
        for i in c:
            x |= 1 << i
        yield x


def first_free_one(x: int, n: int) -> int:
    stack = []
    paired = set()
    for i in range(n):
        if (x >> i) & 1:
            stack.append(i)
        elif stack:
            paired.add(i)
            paired.add(stack.pop())
    return next(i for i in range(n) if ((x >> i) & 1) and i not in paired)


def audit(m: int) -> None:
    n = 2 * m + 1
    us = list(masks(n, m + 2))
    for direction in (1, -1):
        for rank in range(m + 1):
            ls = collections.Counter()
            bs = collections.Counter()
            joint = collections.Counter()
            aset = set()
            for u in us:
                p = first_free_one(u, n)
                a = u ^ (1 << p)
                aset.add(a)
                ordered = [((p + direction * j) % n) for j in range(1, n)]
                qs = [q for q in ordered if (a >> q) & 1]
                q = qs[rank]
                l = a ^ (1 << q)
                b = u ^ (1 << q)
                ls[l] += 1
                bs[b] += 1
                joint[a] += 1
                joint[b] += 1
            print("m", m, "dir", direction, "rank", rank,
                  "Lmax", max(ls.values()), "Ldups", sum(v - 1 for v in ls.values()),
                  "Bmax", max(bs.values()), "Bdups", sum(v - 1 for v in bs.values()),
                  "ownermax", max(joint.values()), "A", len(aset))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("m", nargs="+", type=int)
    args = ap.parse_args()
    for m in args.m:
        audit(m)
