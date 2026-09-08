#!/usr/bin/env python3
"""H100 audit for GK orientation biregularity and max-weight d-factors."""

from __future__ import annotations

from collections import Counter
from itertools import combinations
from math import comb

import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix


def masks(b, r):
    return [sum(1 << i for i in cc) for cc in combinations(range(b), r)]


def signs(mask, b):
    return [1 if (mask >> i) & 1 else -1 for i in range(b)]


def rotmask(mask, shift, b):
    shift %= b
    if not shift:
        return mask
    allbits = (1 << b) - 1
    return ((mask << shift) & allbits) | (mask >> (b-shift))


def necklace_reps(b, r):
    seen = set()
    ans = []
    for mask in masks(b, r):
        if mask in seen:
            continue
        orbit = {rotmask(mask, s, b) for s in range(b)}
        assert len(orbit) == b
        seen.update(orbit)
        ans.append(min(orbit))
    return ans


def top_excess(x, y, t=0):
    b = len(x)
    h = 0
    mn = 0
    for i in range(b):
        h += x[i]
        mn = min(mn, h)
        h += y[(i + t) % b]
        mn = min(mn, h)
    assert h == 0
    return -mn


def rotation_minima(x, y):
    b = len(x)
    a = sum(x)
    assert sum(y) == -a
    X = [0]
    Y = [0]
    for z in x:
        X.append(X[-1] + z)
    for z in y:
        Y.append(Y[-1] + z)

    def ypref(j):
        q, s = divmod(j, b)
        return Y[s] - q * a

    def M(t):
        return min(X[i] + ypref(i + t) for i in range(b))

    MM = {t: M(t) for t in range(-1, b + 1)}
    for t in range(b):
        even_min = MM[t] - ypref(t)
        odd_min = MM[t - 1] - ypref(t)
        literal = -top_excess(x, y, t)
        assert literal == min(even_min, odd_min)
        inc = MM[t] - MM[t - 1]
        assert inc in (-1, 1)
        assert (top_excess(x, y, t) % 2 == 1) == (inc == 1)
    assert MM[b] - MM[0] == -a
    plus = sum(MM[t] - MM[t - 1] == 1 for t in range(1, b + 1))
    assert plus == b - (a + b) // 2


def audit_rotations_and_degrees(b):
    for r in range(1, b):
        XX = masks(b, r)
        YY = masks(b, b-r)
        for xmask in XX:
            x = signs(xmask, b)
            # One representative per column necklace is enough for the identity,
            # but the finite range permits every pair.
            for ymask in YY:
                rotation_minima(x, signs(ymask, b))

        rowA = Counter()
        rowB = Counter()
        colA = Counter()
        colB = Counter()
        for i, xmask in enumerate(XX):
            x = signs(xmask, b)
            for j, ymask in enumerate(YY):
                k = top_excess(x, signs(ymask, b))
                if k % 2:
                    rowA[i] += 1
                    colA[j] += 1
                else:
                    rowB[i] += 1
                    colB[j] += 1
        DA = comb(b-1, r)
        DB = comb(b-1, r-1)
        assert set(rowA.values()) == {DA} and set(colA.values()) == {DA}
        assert set(rowB.values()) == {DB} and set(colB.values()) == {DB}
    print("rotation_and_degrees", {"b": b, "PASS": True})


def factor_optimum(b, r, H, orient):
    XX = masks(b, r)
    YY = masks(b, b-r)
    N = len(XX)
    es = []
    long_row_degrees = Counter()
    for i, xmask in enumerate(XX):
        x = signs(xmask, b)
        for j, ymask in enumerate(YY):
            k = top_excess(x, signs(ymask, b))
            if (k % 2 == 1) == (orient == "A"):
                es.append((i, j, min(k, H)))
                if k >= 2:
                    long_row_degrees[i] += 1
    D = comb(b-1, r) if orient == "A" else comb(b-1, r-1)
    defect = abs(2*r-b)
    nr = max(0, (b-defect-H+2)//2)
    d = nr*N//b
    assert nr*N % b == 0 and len(es) == N*D and d <= D
    rr = []
    cc = []
    vv = []
    for e, (i, j, _) in enumerate(es):
        rr.extend((i, N+j))
        cc.extend((e, e))
        vv.extend((1, 1))
    Aeq = coo_matrix((vv, (rr, cc)), shape=(2*N, len(es))).tocsr()
    res = linprog(
        -np.array([w for _, _, w in es], dtype=float),
        A_eq=Aeq,
        b_eq=np.full(2*N, d, dtype=float),
        bounds=(0, 1),
        method="highs",
    )
    assert res.success
    assert np.max(np.abs(res.x - np.rint(res.x))) < 1e-7
    factor = int(round(-res.fun))
    weights = sorted((w for _, _, w in es), reverse=True)
    uncon = sum(weights[:N*d])
    return uncon-factor, long_row_degrees


def audit_factors():
    expected = {
        (5,2,2,"A"): 2,
        (5,2,2,"B"): 0,
        (7,3,2,"A"): 28,
        (7,3,2,"B"): 0,
        (7,3,3,"A"): 194,
        (7,3,3,"B"): 109,
        (9,4,3,"A"): 2238,
        (9,4,3,"B"): 1425,
    }
    rows = []
    for key, want in expected.items():
        extra, deg = factor_optimum(*key)
        assert extra == want, (key, extra, want)
        rows.append((key, extra))
        if key == (7,3,2,"A"):
            # Include rows of degree zero, absent from the Counter.
            vals = [deg[i] for i in range(comb(7,3))]
            assert min(vals) == 0 and max(vals) == 19
    print("factor_optima", rows, "PASS")


def audit_necklace_diagonals(b, r, H, expected_loss):
    RX = necklace_reps(b, r)
    RY = necklace_reps(b, b-r)
    N = comb(b, r)
    defect = abs(2*r-b)
    nr = max(0, (b-defect-H+2)//2)
    full = {"A": 0, "B": 0}
    kept = {"A": 0, "B": 0}
    degree = {"A": Counter(), "B": Counter()}
    for ax, x in enumerate(RX):
        for by, y in enumerate(RY):
            vals = {"A": [], "B": []}
            for t in range(b):
                diagonal = []
                parity = set()
                for s in range(b):
                    xm = rotmask(x, s, b)
                    ym = rotmask(y, s+t, b)
                    k = top_excess(signs(xm,b), signs(ym,b))
                    parity.add(k % 2)
                    diagonal.append(min(k,H))
                assert len(parity) == 1
                orient = "A" if next(iter(parity)) else "B"
                vals[orient].append((sum(diagonal), t))
            assert len(vals["A"]) == b-r and len(vals["B"]) == r
            for orient in ("A", "B"):
                full[orient] += sum(w for w,_ in vals[orient])
                take = sorted(vals[orient], reverse=True)[:nr]
                kept[orient] += sum(w for w,_ in take)
                for _, t in take:
                    for s in range(b):
                        degree[orient][(ax,s,0)] += 1
                        degree[orient][(by,(s+t)%b,1)] += 1
    want_degree = nr*(N//b)
    for orient in ("A","B"):
        assert set(degree[orient].values()) == {want_degree}
        assert full[orient]-kept[orient] == expected_loss[orient]
    print("necklace_diagonal", {"b":b,"r":r,"H":H,
                                  "loss":{o:full[o]-kept[o] for o in "AB"},
                                  "PASS":True})


def main():
    for b in (3, 5, 7):
        audit_rotations_and_degrees(b)
    audit_factors()
    audit_necklace_diagonals(5,2,2,{"A":22,"B":0})
    audit_necklace_diagonals(7,3,2,{"A":208,"B":0})
    audit_necklace_diagonals(7,3,3,{"A":558,"B":262})
    audit_necklace_diagonals(9,4,3,{"A":6056,"B":2804})
    print("ALL GK ORIENTATION BIRegularity / D-FACTOR CHECKS PASSED")


if __name__ == "__main__":
    main()
