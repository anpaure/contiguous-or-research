#!/usr/bin/env python3
"""Min-cost regular subgraphs of the interleaved-GK orientation matrices.

This tests whether enforcing the exact physical row/column orientation quota
costs anything beyond the unconstrained longest-top selection.  The LP is
integral by bipartite b-matching total unimodularity.  Exploratory; H100 only.
"""

from __future__ import annotations

from itertools import combinations
from math import comb
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix


def top_excess(b: int, x: tuple[int, ...], y: tuple[int, ...]) -> int:
    xs, ys = set(x), set(y)
    stack = 0
    minimum = 0
    height = 0
    for i in range(b):
        for bit in (int(i in xs), int(i in ys)):
            height += 1 if bit else -1
            minimum = min(minimum, height)
    assert height == 0
    return -minimum


def solve_one(b: int, r: int, H: int, orient_a: bool) -> tuple[float, float, int, int, int]:
    rows = list(combinations(range(b), r))
    cols = list(combinations(range(b), b - r))
    N = len(rows)
    assert N == len(cols)
    nr = max(0, (b - abs(2 * r - b) - H + 2) // 2)
    degree = nr * N // b
    assert nr * N % b == 0

    erows: list[int] = []
    ecols: list[int] = []
    weights: list[int] = []
    for i, x in enumerate(rows):
        for j, y in enumerate(cols):
            k = top_excess(b, x, y)
            is_a = k % 2 == 1
            # k=0 is harmlessly assigned to the formal B class.
            if is_a == orient_a:
                erows.append(i)
                ecols.append(j)
                weights.append(min(k, H))

    E = len(weights)
    rr = np.concatenate((np.asarray(erows), N + np.asarray(ecols)))
    cc = np.concatenate((np.arange(E), np.arange(E)))
    data = np.ones(2 * E)
    Aeq = coo_matrix((data, (rr, cc)), shape=(2 * N, E)).tocsr()
    beq = np.full(2 * N, degree, dtype=float)
    result = linprog(
        -np.asarray(weights, dtype=float),
        A_eq=Aeq,
        b_eq=beq,
        bounds=(0.0, 1.0),
        method="highs",
        options={"presolve": True},
    )
    if not result.success:
        raise RuntimeError(result.message)
    optimum = -result.fun
    assert np.max(np.abs(result.x - np.rint(result.x))) < 1e-6
    scalar = float(sum(sorted(weights, reverse=True)[: degree * N]))
    return optimum, scalar, N, degree, E


def main() -> None:
    for b in (11,):
        r = b // 2
        for H in (2,):
            total_opt = total_scalar = 0.0
            fields = []
            for oa in (True, False):
                opt, scalar, N, degree, E = solve_one(b, r, H, oa)
                total_opt += opt
                total_scalar += scalar
                fields.append(("A" if oa else "B", opt, scalar, E))
            L = comb(b, r) ** 2
            print(
                "CASE",
                b,
                r,
                H,
                "N",
                N,
                "D",
                degree,
                "FIELDS",
                fields,
                "OPT",
                total_opt,
                "SCALAR",
                total_scalar,
                "GAP",
                total_scalar - total_opt,
                "GAP/L",
                (total_scalar - total_opt) / L,
                flush=True,
            )


if __name__ == "__main__":
    main()
