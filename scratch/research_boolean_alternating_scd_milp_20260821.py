#!/usr/bin/env python3
"""Finite feasibility tests for alternating upper Boolean chain decompositions.

All actual runs for the research thread are made on ssh h100.
"""

from __future__ import annotations

import argparse
from collections import defaultdict
from itertools import combinations

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import coo_matrix


def masks_of_rank(n: int, k: int) -> list[int]:
    return [sum(1 << i for i in cc) for cc in combinations(range(n), k)]


def solve(b: int, H: int, prescribe_caps: bool = False):
    n = 2 * b
    layers = {q: masks_of_rank(n, b + q) for q in range(H + 1)}
    layer_sets = {q: set(vs) for q, vs in layers.items()}

    # (q, lower, upper, color), where color 0=A and 1=B.
    edges = []
    incoming = defaultdict(list)
    outgoing = defaultdict(list)
    incoming_color = defaultdict(list)
    outgoing_color = defaultdict(list)
    source_split_color = defaultdict(list)
    for q in range(1, H + 1):
        for lo in layers[q - 1]:
            for i in range(n):
                if (lo >> i) & 1:
                    continue
                hi = lo | (1 << i)
                if hi not in layer_sets[q]:
                    continue
                color = 0 if i < b else 1
                idx = len(edges)
                edges.append((q, lo, hi, color))
                incoming[(q, hi)].append(idx)
                outgoing[(q - 1, lo)].append(idx)
                incoming_color[(q, hi, color)].append(idx)
                outgoing_color[(q - 1, lo, color)].append(idx)
                if q == 1:
                    r = (lo & ((1 << b) - 1)).bit_count()
                    source_split_color[(r, color)].append(idx)

    rows, cols, data, lb, ub, names = [], [], [], [], [], []

    def add(coeffs, low, high, name):
        row = len(lb)
        for j, a in coeffs.items():
            rows.append(row)
            cols.append(j)
            data.append(a)
        lb.append(low)
        ub.append(high)
        names.append(name)

    # Cover each positive-rank vertex exactly once from below.
    for q in range(1, H + 1):
        for v in layers[q]:
            add({j: 1 for j in incoming[(q, v)]}, 1, 1, f"in_{q}_{v}")

    # A chain has at most one successor.
    for q in range(H):
        for v in layers[q]:
            add({j: 1 for j in outgoing[(q, v)]}, 0, 1, f"out_{q}_{v}")

    # Consecutive selected edges may not have the same A/B color.
    for q in range(1, H):
        for v in layers[q]:
            for color in (0, 1):
                js = incoming_color[(q, v, color)] + outgoing_color[(q, v, color)]
                add({j: 1 for j in js}, 0, 1, f"alt_{q}_{v}_{color}")

    # Optional exact first-step phase capacities for the full half-step ideal law.
    # At q=1, persistent A-first count at source split r is
    # L_r*(b-r)/(b+1); B-first is L_r*r/(b+1), generally nonintegral.
    # We only cap by floors here, making this a deliberately stringent test.
    if prescribe_caps:
        from math import comb, floor
        for r in range(b + 1):
            L = comb(b, r) ** 2
            caps = (floor(L * (b - r) / (b + 1)), floor(L * r / (b + 1)))
            for color in (0, 1):
                add({j: 1 for j in source_split_color[(r, color)]}, 0, caps[color],
                    f"cap_{r}_{color}")

    A = coo_matrix((data, (rows, cols)), shape=(len(lb), len(edges))).tocsr()
    result = milp(
        c=np.zeros(len(edges)),
        integrality=np.ones(len(edges)),
        bounds=Bounds(np.zeros(len(edges)), np.ones(len(edges))),
        constraints=LinearConstraint(A, np.array(lb), np.array(ub)),
        options={"time_limit": 300},
    )
    print({
        "b": b,
        "H": H,
        "vertices": {q: len(vs) for q, vs in layers.items()},
        "edges": len(edges),
        "constraints": len(lb),
        "caps": prescribe_caps,
        "status": result.status,
        "success": result.success,
        "message": result.message,
    })
    if result.x is not None:
        x = np.rint(result.x).astype(int)
        first = defaultdict(int)
        for j, val in enumerate(x):
            if val and edges[j][0] == 1:
                _, lo, _, color = edges[j]
                r = (lo & ((1 << b) - 1)).bit_count()
                first[(r, color)] += 1
        print("first-step orientation counts", sorted(first.items()))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--b", type=int, required=True)
    ap.add_argument("--H", type=int, required=True)
    ap.add_argument("--caps", action="store_true")
    aa = ap.parse_args()
    solve(aa.b, aa.H, aa.caps)
