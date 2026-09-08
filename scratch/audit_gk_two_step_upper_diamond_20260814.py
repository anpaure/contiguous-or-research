#!/usr/bin/env python3
"""Audit the two-step Greene--Kleitman upper-diamond selector.

For n=2m+1, every rank-(m+2) word has three more unmatched 1s than
unmatched 0s in the standard linear 10-parenthesis matching.  The GK
two-step predecessor flips the first two unmatched 1s.  This script checks
the resulting lower injection and the loads of both intermediate owners.
It also checks the four dihedral scan conventions.
"""

from __future__ import annotations

import argparse
import collections
import itertools


def transform(mask: int, n: int, reverse: bool, complement: bool) -> int:
    bits = [(mask >> i) & 1 for i in range(n)]
    if reverse:
        bits.reverse()
    if complement:
        bits = [1 - b for b in bits]
    out = 0
    for i, b in enumerate(bits):
        out |= b << i
    return out


def free_positions_10(mask: int, n: int) -> list[int]:
    """Positions unpaired by linear 10 cancellation, in scan order."""
    stack: list[int] = []
    paired = [False] * n
    for i in range(n):
        if (mask >> i) & 1:
            stack.append(i)
        elif stack:
            j = stack.pop()
            paired[i] = paired[j] = True
    return [i for i in range(n) if not paired[i]]


def selector(mask: int, n: int, reverse: bool, complement: bool):
    w = transform(mask, n, reverse, complement)
    free = free_positions_10(w, n)
    free_ones = [i for i in free if (w >> i) & 1]
    if len(free_ones) < 2:
        return None
    p, q = free_ones[:2]
    t1 = w ^ (1 << p)
    lower = t1 ^ (1 << q)
    t2 = w ^ (1 << q)
    # Transform back; the complement convention is only meaningful when
    # the transformed word still has the requested two downward flips.
    return tuple(transform(x, n, reverse, complement) for x in (lower, t1, t2))


def masks_of_weight(n: int, r: int):
    for comb in itertools.combinations(range(n), r):
        x = 0
        for i in comb:
            x |= 1 << i
        yield x


def audit(m: int) -> None:
    n = 2 * m + 1
    total = 0
    for reverse in (False, True):
        for complement in (False, True):
            lowers = collections.Counter()
            first = collections.Counter()
            second = collections.Counter()
            failures = 0
            for upper in masks_of_weight(n, m + 2):
                out = selector(upper, n, reverse, complement)
                if out is None:
                    failures += 1
                    continue
                lower, t1, t2 = out
                if lower.bit_count() != m or t1.bit_count() != m + 1 or t2.bit_count() != m + 1:
                    failures += 1
                    continue
                if not (lower & ~upper == 0 and t1 & ~upper == 0 and t2 & ~upper == 0):
                    failures += 1
                    continue
                lowers[lower] += 1
                first[t1] += 1
                second[t2] += 1
            if not reverse and not complement:
                total = sum(lowers.values())
            joint = collections.Counter(first)
            joint.update(second)
            print(
                "m", m,
                "rev", int(reverse),
                "comp", int(complement),
                "selected", sum(lowers.values()),
                "fail", failures,
                "lower_max", max(lowers.values(), default=0),
                "first_max", max(first.values(), default=0),
                "second_max", max(second.values(), default=0),
                "owner_max", max(joint.values(), default=0),
                "owner_hist", sorted(collections.Counter(joint.values()).items()),
            )
    assert total > 0


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("m", nargs="+", type=int)
    args = parser.parse_args()
    for m in args.m:
        audit(m)


if __name__ == "__main__":
    main()
