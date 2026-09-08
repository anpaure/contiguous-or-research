#!/usr/bin/env python3
"""Finite replay for minimum 3-hit period-(2q+1) core schedules.

Substantial ranges should be run on h100.
"""

import argparse
import itertools
import math


def cyclic_blocks(n, length):
    return [frozenset((i + j) % n for j in range(length)) for i in range(n)]


def formula_avoid(q, ell):
    t = q - ell
    return ell * t * (t + 1) // 2 + t * (t + 1) * (2 * t + 1) // 6


def audit(q):
    n = 2 * q + 1
    q_blocks = cyclic_blocks(n, q)
    schedules = [
        frozenset(e)
        for e in itertools.combinations(range(n), 3)
        if all(set(e) & block for block in q_blocks)
    ]
    expected = n * math.comb(q + 1, 2) // 3
    assert len(schedules) == expected

    for ell in range(1, q):
        j = frozenset(range(ell))
        avoid = sum(not (e & j) for e in schedules)
        assert avoid == formula_avoid(q, ell), (q, ell, avoid)

        plus = frozenset({n - 1, 0, q})
        minus = frozenset({n - 2, n - 1, q - 1})
        assert plus in schedules and minus in schedules
        assert plus & j == {0}
        assert not (minus & j)

    print(f"q={q} schedules={len(schedules)} PASS", flush=True)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("q", nargs="+", type=int)
    args = ap.parse_args()
    for q in args.q:
        audit(q)
