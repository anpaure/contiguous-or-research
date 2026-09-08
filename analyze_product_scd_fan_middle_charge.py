#!/usr/bin/env python3
"""Analyze per-grid middle-diagonal charging for the slab-fan atlas.

Substantial runs belong on h100.
"""

import argparse
import math
from collections import defaultdict

import verify_product_scd_diagonal_slab_fan_atlas as fan


def diag_len(a, b, q):
    return max(0, min(a - 1, q) - max(0, q - b + 1) + 1)


def analyze(k):
    r, width, d = fan.parameters(k)
    h = k // 2
    rows = []
    excess = 0
    deficit = 0
    violation_weight = 0
    for u, (a, ca) in enumerate(fan.chain_types(h)):
        for v, (b, cb) in enumerate(fan.chain_types(k - h)):
            radius = r - d - 1 - u - v
            if radius < 0:
                continue
            cost = fan.grid_cost(a, b, radius, d)
            middle = diag_len(a, b, r - u - v)
            mult = ca * cb
            delta = cost - middle
            if delta > 0:
                excess += mult * delta
                violation_weight += mult
                rows.append((delta, cost, middle, u, v, a, b, radius, mult))
            else:
                deficit += mult * (-delta)
    rows.sort(reverse=True)
    print(
        f"k={k} d={d} violating-types={len(rows)} "
        f"excess/W={excess/width:.12f} deficit/W={deficit/width:.12f} "
        f"net/W={(excess-deficit)/width:.12f}"
    )
    for row in rows[:30]:
        print("  ", row)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("k", nargs="+", type=int)
    args = ap.parse_args()
    for k in args.k:
        analyze(k)
