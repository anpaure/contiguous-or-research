#!/usr/bin/env python3
"""Finite exact checks for the coordinate-necklace GK diagonal obstruction.

The asymptotic input in the note is analytic (the capped bridge-area
small-deviation lemma).  This checker verifies every finite combinatorial
identity around that input: literal GK tops, the bridge lower bound,
orientation constancy on a diagonal, necklace accounting, and
Gamma = R_diag - R_un.
"""

from __future__ import annotations

from itertools import combinations
from math import comb


def subsets(b: int, r: int):
    return [frozenset(c) for c in combinations(range(b), r)]


def rotate(s, t: int, b: int):
    return frozenset((i - t) % b for i in s)


def necklace_reps(b: int, r: int):
    seen = set()
    reps = []
    for x in subsets(b, r):
        if x in seen:
            continue
        orb = {rotate(x, t, b) for t in range(b)}
        assert len(orb) == b
        seen.update(orb)
        reps.append(min(orb, key=lambda z: tuple(sorted(z))))
    assert len(seen) == comb(b, r)
    return reps


def top_excess(b: int, x, z) -> int:
    """Literal alternating word A(x), B(Y), where Y is complement of z."""
    height = 0
    minimum = 0
    for i in range(b):
        height += 1 if i in x else -1
        minimum = min(minimum, height)
        height += -1 if i in z else 1
        minimum = min(minimum, height)
    assert height == 0
    return -minimum


def bridge_heights(b: int, x, z):
    d = [0]
    for i in range(b):
        d.append(d[-1] + int(i in x) - int(i in z))
    assert d[-1] == 0
    mn = min(d[:-1])
    return [v - mn for v in d[:-1]]


def diagonal(b: int, H: int, x, z, t: int):
    zt = rotate(z, t, b)
    hs = bridge_heights(b, x, zt)
    tops = []
    for s in range(b):
        xs = rotate(x, s, b)
        zs = rotate(zt, s, b)
        k = top_excess(b, xs, zs)
        tops.append(k)
        assert k >= 2 * hs[s]
    assert len({k & 1 for k in tops}) == 1
    cost = sum(min(k, H) for k in tops)
    assert cost >= 2 * sum(min(h, H / 2) for h in hs)
    return tops[0] & 1, cost, tops


def check_split(b: int, r: int, H: int):
    allsets = subsets(b, r)
    reps = necklace_reps(b, r)
    N = len(allsets)
    n = max(0, (b - abs(2 * r - b) - H + 2) // 2)
    assert n <= min(r, b - r)

    # Literal global edge lists, with parity 1=A and 0=B.
    global_weights = {0: [], 1: []}
    for x in allsets:
        for z in allsets:
            k = top_excess(b, x, z)
            global_weights[k & 1].append(min(k, H))
    assert len(global_weights[1]) == (b - r) * N * N // b
    assert len(global_weights[0]) == r * N * N // b

    total = {0: 0, 1: 0}
    fdiag = {0: 0, 1: 0}
    block_deleted = 0
    for x in reps:
        for z in reps:
            vals = {0: [], 1: []}
            for t in range(b):
                parity, cost, _ = diagonal(b, H, x, z, t)
                vals[parity].append(cost)
            assert len(vals[1]) == b - r
            assert len(vals[0]) == r
            deleted_here = 0
            for parity in (0, 1):
                total[parity] += sum(vals[parity])
                fdiag[parity] += sum(sorted(vals[parity], reverse=True)[:n])
                deleted_here += sum(sorted(vals[parity])[: len(vals[parity]) - n])
            p = b - 2 * n
            allcosts = sorted(vals[0] + vals[1])
            assert deleted_here >= sum(allcosts[:p])
            block_deleted += deleted_here

    # Every source edge appears exactly once in a block diagonal.
    for parity in (0, 1):
        assert total[parity] == sum(global_weights[parity])

    U = {}
    Run = {}
    Rdiag = {}
    Gamma = {}
    K = n * N * N // b
    for parity in (0, 1):
        U[parity] = sum(sorted(global_weights[parity], reverse=True)[:K])
        Run[parity] = total[parity] - U[parity]
        Rdiag[parity] = total[parity] - fdiag[parity]
        Gamma[parity] = U[parity] - fdiag[parity]
        assert Gamma[parity] == Rdiag[parity] - Run[parity]
        assert Gamma[parity] >= 0
    assert block_deleted == sum(Rdiag.values())
    return {
        "b": b,
        "r": r,
        "H": H,
        "N": N,
        "n": n,
        "R_un": {"A": Run[1], "B": Run[0]},
        "R_diag": {"A": Rdiag[1], "B": Rdiag[0]},
        "Gamma": {"A": Gamma[1], "B": Gamma[0]},
    }


def main():
    rows = []
    for b, H in ((3, 2), (5, 2), (7, 3)):
        for r in range(1, b):
            rows.append(check_split(b, r, H))
    for row in rows:
        print(row)
    print("PASS audit_coordinate_necklace_diagonal_gk_cost_20260821")


if __name__ == "__main__":
    main()
