#!/usr/bin/env python3
"""MILP-optimize one common relative origin per complementary atom pair.

Imports the exact small-b factor finder/census helpers.  Execute on H100.
"""

from collections import defaultdict
import math

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import coo_matrix

from explore_complementary_bank_full_upper_coverage_20260821 import (
    clustered_word,
    tight_factor,
    window_mask,
)


def rotate(order, shift):
    shift %= len(order)
    return order[shift:] + order[:shift]


def optimize(b):
    factors = {}
    for r in range(1, b // 2 + 1):
        factors[r] = tight_factor(b, r)
        factors[b - r] = factors[r]

    # One group contains the paired payloads r and b-r with common A/B order
    # coordinates and one common relative beta origin.
    groups = []
    for r in range(1, b // 2 + 1):
        for ia, alpha in enumerate(factors[r]):
            for ib, beta in enumerate(factors[r]):
                groups.append((r, ia, ib, alpha, beta))

    qs = list(range(1, b // 2 + 1))
    target_ids = {}
    target_list = []
    for q in qs:
        for mask in range(1 << (2 * b)):
            if mask.bit_count() == b + q:
                target_ids[(q, mask)] = len(target_list)
                target_list.append((q, mask))

    x_count = len(groups) * b
    y_count = len(target_list)
    nvar = x_count + y_count
    covers = [[] for _ in target_list]

    for gi, (r, ia, ib, alpha, beta) in enumerate(groups):
        for shift in range(b):
            x = gi * b + shift
            beta_shifted = rotate(beta, shift)
            for payload in (r, b - r):
                word = clustered_word(alpha, beta_shifted, payload)
                for q in qs:
                    seen = {
                        window_mask(word, t, b + q)
                        for t in range(b * b)
                    }
                    for mask in seen:
                        if mask.bit_count() == b + q:
                            covers[target_ids[(q, mask)]].append(x)

    rows = []
    cols = []
    data = []
    lower = []
    upper = []

    # Exactly one origin per group.
    row = 0
    for gi in range(len(groups)):
        for shift in range(b):
            rows.append(row)
            cols.append(gi * b + shift)
            data.append(1.0)
        lower.append(1.0)
        upper.append(1.0)
        row += 1

    # y_t <= sum of chosen origin variables that cover t.
    for ti, xs in enumerate(covers):
        rows.append(row)
        cols.append(x_count + ti)
        data.append(1.0)
        for x in xs:
            rows.append(row)
            cols.append(x)
            data.append(-1.0)
        lower.append(-np.inf)
        upper.append(0.0)
        row += 1

    matrix = coo_matrix((data, (rows, cols)), shape=(row, nvar)).tocsr()
    objective = np.zeros(nvar)
    objective[x_count:] = -1.0
    result = milp(
        c=objective,
        integrality=np.ones(nvar),
        bounds=Bounds(np.zeros(nvar), np.ones(nvar)),
        constraints=LinearConstraint(matrix, np.array(lower), np.array(upper)),
        options={"time_limit": 240.0, "mip_rel_gap": 0.0},
    )
    assert result.x is not None
    chosen = [int(np.argmax(result.x[gi * b : (gi + 1) * b])) for gi in range(len(groups))]
    counts = defaultdict(set)
    for gi, shift in enumerate(chosen):
        r, ia, ib, alpha, beta = groups[gi]
        beta_shifted = rotate(beta, shift)
        for payload in (r, b - r):
            word = clustered_word(alpha, beta_shifted, payload)
            for q in qs:
                counts[q].update(
                    mask
                    for t in range(b * b)
                    for mask in (window_mask(word, t, b + q),)
                    if mask.bit_count() == b + q
                )

    central = math.comb(2 * b, b)
    print("MILP", b, "success", result.success, "status", result.message)
    print(" groups", len(groups), "vars", nvar, "objective coverage", -result.fun)
    for q in qs:
        total = math.comb(2 * b, b + q)
        holes = total - len(counts[q])
        print(" q", q, "covered", len(counts[q]), "holes", holes, "holes/W", holes / central)
    print(" aggregate holes/W", sum(math.comb(2*b,b+q)-len(counts[q]) for q in qs) / central)
    print(" shifts", chosen)


if __name__ == "__main__":
    for b in (5, 7):
        optimize(b)
