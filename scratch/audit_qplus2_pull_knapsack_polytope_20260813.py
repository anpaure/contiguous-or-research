#!/usr/bin/env python3
"""H100 audit: corrected pull vector vs fixed q+2 cyclic block knapsack hull."""

from __future__ import annotations

import argparse
import importlib.util
import pathlib
import sys

import numpy as np
from scipy.optimize import linprog
from scipy.sparse import csc_matrix, hstack, vstack


HERE = pathlib.Path(__file__).resolve().parent
PULL = HERE / "audit_fixed_qplus2_pull_configuration_cost_20260813.py"
spec = importlib.util.spec_from_file_location("pullcost", PULL)
pullcost = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(pullcost)


def configurations(cap: int, max_size: int):
    sizes = list(range(2, max_size + 1))
    cur = [0] * len(sizes)
    out = []

    def rec(idx: int, rem: int) -> None:
        if idx == len(sizes):
            out.append(tuple(cur))
            return
        w = sizes[idx]
        for number in range(rem // w + 1):
            cur[idx] = number
            rec(idx + 1, rem - number * w)
        cur[idx] = 0

    rec(0, cap)
    return sizes, out


def gauge(k: int):
    r, d, ccore, ordinary, fixed, by_j, min_x, hb, long_gate = pullcost.costs(k)
    cap = d + 3
    max_size = d  # j<=d-1, since x_(delta,d)=0 in the odd case
    sizes, cfgs = configurations(cap, max_size)
    rows = []
    cols = []
    data = []
    for col, cfg in enumerate(cfgs):
        rows.append(0)
        cols.append(col)
        data.append(1.0)
        for idx, number in enumerate(cfg):
            if number:
                rows.append(idx + 1)
                cols.append(col)
                data.append(float(number))
    amat = csc_matrix((data, (rows, cols)), shape=(1 + len(sizes), len(cfgs)))
    y = np.array([cap * by_j[w - 2] for w in sizes], dtype=float)
    tau_col = csc_matrix(np.concatenate(([0.0], -y))[:, None])
    aeq = hstack([amat, tau_col], format="csc")
    beq = np.zeros(1 + len(sizes))
    beq[0] = 1.0
    obj = np.zeros(len(cfgs) + 1)
    obj[-1] = -1.0
    bounds = [(0.0, None)] * len(cfgs) + [(0.0, None)]
    res = linprog(obj, A_eq=aeq, b_eq=beq, bounds=bounds, method="highs")
    if not res.success:
        raise RuntimeError(res.message)
    tau = res.x[-1]
    used = int(np.count_nonzero(res.x[:-1] > 1e-9))
    return r, d, cap, len(cfgs), ordinary, fixed, tau, used, res


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--k", type=int, nargs="+", required=True)
    ap.add_argument("--dual", action="store_true")
    args = ap.parse_args()
    for k in args.k:
        r, d, cap, nc, ordinary, fixed, tau, used, res = gauge(k)
        print(
            f"k={k} R={r} d={d} N={cap} configs={nc} "
            f"C={ordinary:.12g} pureCN={fixed:.12g} "
            f"knap_tau={tau:.12g} feasible={tau >= 1-1e-8} support={used}"
        )
        if args.dual:
            print("eqlin_marginals", res.eqlin.marginals.tolist())
            print("eqlin_residual", res.eqlin.residual.tolist())


if __name__ == "__main__":
    main()
