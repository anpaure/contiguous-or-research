#!/usr/bin/env python3
"""Exploratory exact MILP for row/column-regular constant-side H-chains."""

from __future__ import annotations

import itertools
import math
import sys

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import coo_matrix


def subsets(n: int, k: int):
    return [sum(1 << i for i in c) for c in itertools.combinations(range(n), k)]


def solve(b: int, hband: int):
    layers = [subsets(b, r) for r in range(b + 1)]
    index = [{x: i for i, x in enumerate(layer)} for layer in layers]
    full = (1 << b) - 1
    options = []
    source_options = []
    by_rxy = {}
    for r in range(hband, b - hband + 1):
        for xi, x in enumerate(layers[r]):
            for yi, y in enumerate(layers[r]):
                sid = len(source_options)
                source_options.append([])
                by_rxy[(r, xi, yi)] = sid
                missing_a = [i for i in range(b) if not (x >> i) & 1]
                present_y = [i for i in range(b) if (y >> i) & 1]
                for side, pool in ((0, missing_a), (1, present_y)):
                    for seq in itertools.permutations(pool, hband):
                        targets = []
                        xx, yy = x, y
                        for q, z in enumerate(seq, 1):
                            if side == 0:
                                xx |= 1 << z
                            else:
                                yy ^= 1 << z
                            s = xx.bit_count()
                            targets.append((q, s, index[s][xx], index[s - q][yy]))
                        vid = len(options)
                        options.append((sid, r, xi, yi, side, targets))
                        source_options[sid].append(vid)

    target_keys = []
    for q in range(1, hband + 1):
        for s in range(q, b + 1):
            t = s - q
            if t < hband or s > b - hband:
                continue
            target_keys.extend((q, s, xi, yi)
                               for xi in range(len(layers[s]))
                               for yi in range(len(layers[t])))
    target_index = {key: i for i, key in enumerate(target_keys)}
    nopt = len(options)
    nt = len(target_keys)
    nvar = nopt + nt
    rows, cols, data, lb, ub = [], [], [], [], []

    def add(coeffs, lo, hi):
        row = len(lb)
        for col, val in coeffs:
            rows.append(row); cols.append(col); data.append(val)
        lb.append(lo); ub.append(hi)

    for vids in source_options:
        add(((v, 1) for v in vids), 1, 1)

    # Exact A-side row and column degrees at every central payload.
    for r in range(hband, b - hband + 1):
        cr = math.comb(b, r)
        assert (r * cr) % b == 0
        degree = r * cr // b
        for xi in range(cr):
            vids = [v for v, (_, rr, xx, _, side, _) in enumerate(options)
                    if rr == r and xx == xi and side == 0]
            add(((v, 1) for v in vids), degree, degree)
        for yi in range(cr):
            vids = [v for v, (_, rr, _, yy, side, _) in enumerate(options)
                    if rr == r and yy == yi and side == 0]
            add(((v, 1) for v in vids), degree, degree)

    coverers = [[] for _ in target_keys]
    for v, (_, _, _, _, _, targets) in enumerate(options):
        for key in targets:
            ti = target_index.get(key)
            if ti is not None:
                coverers[ti].append(v)
    for ti, vids in enumerate(coverers):
        # y_t <= sum of selected options covering t.
        add(itertools.chain(((nopt + ti, 1),), ((v, -1) for v in vids)), -np.inf, 0)

    mat = coo_matrix((data, (rows, cols)), shape=(len(lb), nvar)).tocsr()
    c = np.zeros(nvar)
    c[nopt:] = -1
    result = milp(c, integrality=np.ones(nvar), bounds=Bounds(0, 1),
                  constraints=LinearConstraint(mat, np.array(lb), np.array(ub)),
                  options={"time_limit": 600, "mip_rel_gap": 0})
    print("RESULT", b, hband, result.success, result.status, result.message)
    print("SIZES", nopt, nt, nvar, len(lb), mat.nnz)
    if result.fun is not None:
        covered = round(-result.fun)
        print("COVER", covered, "MISS", nt - covered, "TOTAL", nt)
        if result.mip_gap is not None:
            print("GAP", result.mip_gap, "BOUND", result.mip_node_count)


if __name__ == "__main__":
    solve(int(sys.argv[1]), int(sys.argv[2]))
