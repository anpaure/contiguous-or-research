#!/usr/bin/env python3
"""Research diagnostic for the ideal alternating two-state retirement LP.

All masses are divided by W_b=binom(2b,b).  For each retained source r the
ideal word has two persistent parity paths:

  epsilon=0: s(2u)=r+u, s(2u+1)=r+u;
  epsilon=1: s(2u)=r+u, s(2u+1)=r+u+1.

Two capacity models are reported:

* symmetric: each branch has L_r/(2 W_b);
* physical-q1: the low/high branches have respectively
  (b-r)L_r/(b W_b) and rL_r/(b W_b), the exact q=1 phase counts.

The LP variables x_(r,epsilon,q) are nonincreasing in q and obey the usual
profile quotas binom(b,s)binom(b,s-q)/W_b.  The displayed gap is the LP
optimum's loss relative to the sum of the independent layer optima for the
same ideal path capacities, hence it is already normalized by W_b.

Research-only: invoke in an environment providing NumPy/SciPy, e.g.
`uv run --with numpy --with scipy python scratch/research_...py`.
"""

from __future__ import annotations

import argparse
import math

import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix


def logchoose(n: int, k: int) -> float:
    if not 0 <= k <= n:
        return float("-inf")
    return math.lgamma(n + 1) - math.lgamma(k + 1) - math.lgamma(n - k + 1)


def solve(b: int, H: int, physical_q1_caps: bool) -> tuple[float, float, float]:
    assert b % 2 == 1 and 1 <= H < b // 2
    g = b // 4
    logW = logchoose(2 * b, b)

    # (r, epsilon, normalized capacity, profile word)
    paths: list[tuple[int, int, float, list[int]]] = []
    for r in range(g, b - g + 1):
        source = math.exp(2 * logchoose(b, r) - logW)
        for epsilon in (0, 1):
            if physical_q1_caps:
                branch_fraction = (b - r) / b if epsilon == 0 else r / b
            else:
                branch_fraction = 0.5
            cap = source * branch_fraction
            profiles = [
                r + q // 2 if q % 2 == 0 else r + (q - 1) // 2 + epsilon
                for q in range(1, H + 1)
            ]
            paths.append((r, epsilon, cap, profiles))

    nvar = len(paths) * H
    rows: list[int] = []
    cols: list[int] = []
    data: list[float] = []
    rhs: list[float] = []
    row = 0

    # Retirement monotonicity x(q+1)<=x(q).
    for i in range(len(paths)):
        for q0 in range(H - 1):
            rows.extend((row, row))
            cols.extend((i * H + q0 + 1, i * H + q0))
            data.extend((1.0, -1.0))
            rhs.append(0.0)
            row += 1

    totals: list[dict[int, float]] = [dict() for _ in range(H)]
    quotas: list[dict[int, float]] = [dict() for _ in range(H)]
    for q0 in range(H):
        q = q0 + 1
        for _, _, cap, profiles in paths:
            s = profiles[q0]
            totals[q0][s] = totals[q0].get(s, 0.0) + cap
        for s in totals[q0]:
            ids = [i for i, path in enumerate(paths) if path[3][q0] == s]
            rows.extend([row] * len(ids))
            cols.extend(i * H + q0 for i in ids)
            data.extend([1.0] * len(ids))
            quota = math.exp(logchoose(b, s) + logchoose(b, s - q) - logW)
            quotas[q0][s] = quota
            rhs.append(quota)
            row += 1

    A = coo_matrix((data, (rows, cols)), shape=(row, nvar)).tocsr()
    bounds = [(0.0, cap) for _, _, cap, _ in paths for _ in range(H)]
    result = linprog(
        -np.ones(nvar),
        A_ub=A,
        b_ub=np.asarray(rhs),
        bounds=bounds,
        method="highs",
        options={
            "dual_feasibility_tolerance": 1e-9,
            "primal_feasibility_tolerance": 1e-9,
        },
    )
    assert result.success, result.message

    separate = sum(
        min(raw, quotas[q0][s])
        for q0 in range(H)
        for s, raw in totals[q0].items()
    )
    optimum = -float(result.fun)
    violation = max(0.0, float(np.max(A @ result.x - np.asarray(rhs))))
    return separate - optimum, separate, violation


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("b", type=int, nargs="*")
    parser.add_argument("--scale", type=float, default=3.0)
    args = parser.parse_args()
    bs = args.b or [101, 251, 503, 1009]
    for b in bs:
        H = min(b // 4, max(2, int(args.scale * math.sqrt(b))))
        for physical in (False, True):
            gap, separate, violation = solve(b, H, physical)
            print(
                "IDEAL_TWO_STATE",
                "physical" if physical else "symmetric",
                "b",
                b,
                "H",
                H,
                "gap_over_W",
                gap,
                "separate_over_W",
                separate,
                "violation",
                violation,
            )


if __name__ == "__main__":
    main()
