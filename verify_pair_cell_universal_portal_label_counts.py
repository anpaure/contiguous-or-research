#!/usr/bin/env python3
"""Finite arithmetic replay for universal labelled pair-cell portals.

Substantial ranges belong on h100.
"""

import argparse
import math


def audit(k, q):
    assert k % 2 == 1
    R = (k + 1) // 2
    p = R - 1
    h = math.ceil(3 * math.log2(p))
    M = q + h
    assert M <= p

    for s in range(h + 1, R - q + 1):
        m = s + q - 1
        assert M <= m <= p
        for epsilon in (0, 1):
            if epsilon != ((R - m) & 1):
                continue
            a = (R - epsilon - m) // 2
            b = p - m - a
            assert a >= 0 and b >= 0 and a + b == p - m
            assert s + 2 * (q - 1) + 1 + 2 * (p - m) == k - s

    s = R - q + 1
    m = p
    epsilon = 1
    a = (R - epsilon - m) // 2
    b = p - m - a
    assert a == b == 0
    assert (s - 1) + 2 * (q - 1) == k - s

    for s in range(R - q + 2, R):
        r = R - s
        assert 1 <= r <= q - 2
        assert (s - 1) + 2 * r == k - s
        assert 2 <= q - r <= q - 1

    low = sum(math.comb(k, s) for s in range(1, h + 1))
    print(
        f"k={k} R={R} q={q} h={h} M={M} low-targets={low} PASS",
        flush=True,
    )


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("k", nargs="+", type=int)
    ap.add_argument("--q", type=int)
    args = ap.parse_args()
    for k in args.k:
        R = (k + 1) // 2
        q = args.q if args.q is not None else int(math.sqrt(R)) + 1
        audit(k, q)
