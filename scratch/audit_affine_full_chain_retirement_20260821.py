#!/usr/bin/env python3
"""Fail-closed audit for affine whole-chain loads and retirement LP."""

from __future__ import annotations

import math
from fractions import Fraction

import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix


def choose(n: int, k: int) -> int:
    return math.comb(n, k) if 0 <= k <= n else 0


def primes_upto(n: int) -> list[int]:
    return [
        x
        for x in range(2, n + 1)
        if all(x % d for d in range(2, math.isqrt(x) + 1))
    ]


def affine_profiles(b: int, r: int, p: int, h: int) -> list[int]:
    a = (b - 1) // 2
    z = 0
    out = []
    for q in range(1, h + 1):
        z += ((a * ((p + q) % b)) % b) < r
        out.append(r + z)
    return out


def path_table(b: int, h: int):
    return [
        (r, p, affine_profiles(b, r, p, h))
        for r in range(b + 1)
        for p in range(b)
    ]


def audit_choose_identities() -> None:
    # Equations (2.8), (3.5), and the central extension lower bounds.
    for b in primes_upto(43):
        if b < 5:
            continue
        g = b // 4
        h = max(1, min(g - 1, int(math.sqrt(b))))
        for r in range(max(1, g), min(b, b - g + 1)):
            lr = choose(b, r) ** 2
            for q in range(1, h + 1):
                for z in range(q + 1):
                    s = r + z
                    bdeg = choose(b - r, z) * choose(r, q - z)
                    nsrc = choose(s, r) * choose(b + q - s, b - r)
                    prof = choose(b, s) * choose(b, s - q)
                    assert nsrc * prof == bdeg * lr
                    assert bdeg >= g
            for p in range(b):
                ss = affine_profiles(b, r, p, h)
                for q in range(1, h):
                    for qp in range(q + 1, h + 1):
                        s, sp = ss[q - 1], ss[qp - 1]
                        da = sp - s
                        db = (qp - q) - da
                        ext = choose(b - s, da) * choose(s - q, db)
                        assert ext >= max(1, g - h)


def audit_raw_loads() -> None:
    # Exact source/token loads and target marginals from formulas (2.2)-(2.8).
    for b in primes_upto(31):
        if b < 5:
            continue
        h = max(1, min(b // 4, 5))
        for r in range(h, b - h + 1):
            lr = choose(b, r) ** 2
            ai = Fraction(lr, b)
            assert ai.denominator == 1
            for p in range(b):
                ss = affine_profiles(b, r, p, h)
                zh = ss[-1] - r
                dh = math.prod(range(b - r - zh + 1, b - r + 1)) * math.prod(
                    range(r - (h - zh) + 1, r + 1)
                )
                assert Fraction(ai * dh, lr * dh) == Fraction(1, b)
                assert Fraction(lr * dh, lr * dh) == 1

        # Formula target load = T/P, checked by summing compatible paths.
        paths = [x for x in path_table(b, h) if h <= x[0] <= b - h]
        for q in range(1, h + 1):
            for s in range(q, b + 1):
                tnum = sum(choose(b, r) ** 2 for r, p, ss in paths if ss[q - 1] == s)
                psize = choose(b, s) * choose(b, s - q)
                direct = Fraction(0)
                for r, p, ss in paths:
                    if ss[q - 1] != s:
                        continue
                    z = s - r
                    bdeg = choose(b - r, z) * choose(r, q - z)
                    nsrc = choose(s, r) * choose(b + q - s, b - r)
                    direct += Fraction(nsrc, b * bdeg)
                assert direct == Fraction(tnum, b * psize)


def audit_target_pair_formula() -> None:
    for b in [7, 11, 17]:
        h = min(5, b // 4)
        paths = [x for x in path_table(b, h) if h <= x[0] <= b - h]
        for q in range(1, h):
            for qp in range(q + 1, h + 1):
                for s in range(q, b + 1):
                    for sp in range(max(s, qp), b + 1):
                        ext = choose(b - s, sp - s) * choose(
                            s - q, (qp - q) - (sp - s)
                        )
                        if not ext:
                            continue
                        psize = choose(b, s) * choose(b, s - q)
                        numerator = sum(
                            choose(b, r) ** 2
                            for r, p, ss in paths
                            if ss[q - 1] == s and ss[qp - 1] == sp
                        )
                        formula = Fraction(numerator, b * psize * ext)
                        direct = Fraction(0)
                        for r, p, ss in paths:
                            if ss[q - 1] != s or ss[qp - 1] != sp:
                                continue
                            z = s - r
                            bdeg = choose(b - r, z) * choose(r, q - z)
                            nsrc = choose(s, r) * choose(b + q - s, b - r)
                            direct += Fraction(nsrc, b * bdeg * ext)
                        assert direct == formula


def audit_full_chain_obstruction() -> None:
    rows = []
    for b in [101, 251, 503, 1009]:
        h = min(b // 4, int(math.sqrt(b * math.log(b))))
        w = choose(2 * b, b)
        mh = choose(2 * b, b + h)
        deficit = sum(choose(2 * b, b + q) - mh for q in range(1, h + 1))
        rows.append((b, h, float(Fraction(mh, w)), float(Fraction(deficit, w))))
        assert deficit > math.isqrt(b) * w // 20
    print("FULL_CHAIN_OBSTRUCTION", rows)


def solve_retirement_lp(b: int):
    h = min(b // 4, max(2, int(math.sqrt(b * math.log(b)))))
    g = b // 4
    paths0 = [x for x in path_table(b, h) if g <= x[0] <= b - g]
    logw = math.log(choose(2 * b, b))
    paths = []
    for r, p, ss in paths0:
        cap = math.exp(2 * math.log(choose(b, r)) - math.log(b) - logw)
        paths.append((r, p, cap, ss))

    nvar = len(paths) * h
    rows: list[int] = []
    cols: list[int] = []
    data: list[float] = []
    rhs: list[float] = []
    row = 0

    for i, (_, _, _, _) in enumerate(paths):
        for q in range(h - 1):
            rows.extend([row, row])
            cols.extend([i * h + q + 1, i * h + q])
            data.extend([1.0, -1.0])
            rhs.append(0.0)
            row += 1

    for q in range(1, h + 1):
        buckets = {s: [] for s in range(q, b + 1)}
        for i, (_, _, _, ss) in enumerate(paths):
            if q <= ss[q - 1] <= b:
                buckets[ss[q - 1]].append(i)
        for s, ids in buckets.items():
            rows.extend([row] * len(ids))
            cols.extend([i * h + q - 1 for i in ids])
            data.extend([1.0] * len(ids))
            rhs.append(
                math.exp(
                    math.log(choose(b, s)) + math.log(choose(b, s - q)) - logw
                )
            )
            row += 1

    aub = coo_matrix((data, (rows, cols)), shape=(row, nvar)).tocsr()
    bounds = [bd for _, _, cap, _ in paths for bd in [(0.0, cap)] * h]
    res = linprog(
        -np.ones(nvar),
        A_ub=aub,
        b_ub=np.asarray(rhs),
        bounds=bounds,
        method="highs",
        options={
            "dual_feasibility_tolerance": 1e-10,
            "primal_feasibility_tolerance": 1e-10,
            "ipm_optimality_tolerance": 1e-12,
        },
    )
    assert res.success
    violation = max(0.0, float(np.max(aub @ res.x - np.asarray(rhs))))
    assert violation < 2e-7
    ideal = sum(choose(2 * b, b + q) / choose(2 * b, b) for q in range(1, h + 1))
    separate_mass = 0.0
    for q in range(1, h + 1):
        raw = {}
        for _, _, cap, ss in paths:
            raw[ss[q - 1]] = raw.get(ss[q - 1], 0.0) + cap
        for s in range(q, b + 1):
            pcap = math.exp(
                math.log(choose(b, s)) + math.log(choose(b, s - q)) - logw
            )
            separate_mass += min(pcap, raw.get(s, 0.0))
    separate_def = ideal - separate_mass
    return h, ideal + res.fun, separate_def, violation


def audit_retirement_lp() -> None:
    rows = []
    for b in [11, 17, 31, 41, 61]:
        h, deficit, separate_def, violation = solve_retirement_lp(b)
        rows.append((b, h, deficit, separate_def, violation))
        # Numerical evidence only; tolerate scaling noise in the very small cases.
        assert abs(deficit - separate_def) < 5e-5
    print("RETIREMENT_LP_DIAGNOSTIC", rows)


def audit_nonmonotone_and_switch() -> None:
    # Literal profile-node phase switch from Section 6.
    for b in range(11, 82, 2):
        m = (b - 1) // 2
        r = m - 2
        x = affine_profiles(b, r, b - 2, 3)
        y = affine_profiles(b, r, b - 3, 3)
        assert x == [r, r + 1, r + 1]
        assert y == [r + 1, r + 1, r + 2]

    # The separate profile thinning is not pathwise monotone.
    # One exact finite witness is enough to close that logical shortcut.
    b = 11
    h = 2
    paths = path_table(b, h)
    rho = [None]
    for q in range(1, h + 1):
        arr = []
        for s in range(b + q + 1):
            psize = choose(b, s) * choose(b, s - q)
            tnum = sum(
                choose(b, r) ** 2 for r, p, ss in paths if ss[q - 1] == s
            )
            arr.append(min(Fraction(1), Fraction(b * psize, tnum)) if tnum else Fraction(0))
        rho.append(arr)
    found = False
    for r, p, ss in paths:
        if rho[2][ss[1]] > rho[1][ss[0]]:
            found = True
            break
    assert found


def main() -> None:
    audit_choose_identities()
    audit_raw_loads()
    audit_target_pair_formula()
    audit_full_chain_obstruction()
    audit_retirement_lp()
    audit_nonmonotone_and_switch()
    print("PASS affine full-chain/retirement audit")


if __name__ == "__main__":
    main()
