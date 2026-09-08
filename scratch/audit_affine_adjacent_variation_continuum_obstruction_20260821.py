#!/usr/bin/env python3
"""Fail-closed audit for the affine adjacent-variation continuum obstruction."""

from __future__ import annotations

import math


def choose(n: int, k: int) -> int:
    return math.comb(n, k) if 0 <= k <= n else 0


def exact_F_even(b: int, u: int, K: int) -> int:
    assert b % 2 and K >= 2 and K % 2 == 0 and K <= 2 * u
    h = (b - 1) // 2
    v = K // 2
    L = lambda j: choose(b, h + 1 + j) ** 2
    A = h + 1 - u - K
    return 2 * A * L(K) + 4 * sum(L(j) for j in range(v + 1, K)) + (u - v + 3) * L(v)


def exact_F_odd(b: int, u: int, K: int) -> int:
    assert b % 2 and K >= 2 and K % 2 == 0 and K <= 2 * u
    h = (b - 1) // 2
    v = K // 2
    L = lambda j: choose(b, h + 1 + j) ** 2
    A = h - u - K
    return A * L(K) + (A + 4) * L(K - 1) + 4 * sum(L(j) for j in range(v, K - 1))


def bits(b: int, r: int) -> list[int]:
    h = (b - 1) // 2
    return [int((h * x) % b < r) for x in range(b)]


def literal_F(b: int, q: int, s: int) -> int:
    out = 0
    for r in range(b + 1):
        word = bits(b, r)
        lr = choose(b, r) ** 2
        for p in range(b):
            z = sum(word[(p + j) % b] for j in range(1, q + 1))
            if r + z == s:
                out += lr
    return out


def audit_exact_formulas_and_joint_counts() -> None:
    checks = 0
    for b in [19, 25, 31, 41]:
        h = (b - 1) // 2
        for u in range(2, min(6, h // 3)):
            for K in range(2, min(2 * u, h // 3) + 1, 2):
                se = h + 1 + u + K
                so = h + 1 + u + K
                assert literal_F(b, 2 * u, se) == exact_F_even(b, u, K)
                assert literal_F(b, 2 * u + 1, so) == exact_F_odd(b, u, K)

                r = h + 1 + K
                word = bits(b, r)
                joint = 0
                for p in range(b):
                    z = sum(word[(p + j) % b] for j in range(1, 2 * u + 1))
                    if z == u and word[(p + 2 * u + 1) % b] == 0:
                        joint += 1
                assert joint == h - u - K
                checks += 1
    print("EXACT_FORMULA_AND_JOINT_CHECKS", checks)


def lc(n: int, k: int) -> float:
    if not 0 <= k <= n:
        return float("-inf")
    return math.lgamma(n + 1) - math.lgamma(k + 1) - math.lgamma(n - k + 1)


def logsumexp(xs: list[float]) -> float:
    m = max(xs)
    return m + math.log(sum(math.exp(x - m) for x in xs))


def rho_pair(b: int, u: int, K: int) -> tuple[float, float]:
    h = (b - 1) // 2
    v = K // 2
    le = []
    A = h + 1 - u - K
    le.append(math.log(2 * A) + 2 * lc(b, h + 1 + K))
    for j in range(v + 1, K):
        le.append(math.log(4) + 2 * lc(b, h + 1 + j))
    le.append(math.log(u - v + 3) + 2 * lc(b, h + 1 + v))
    logFe = logsumexp(le)

    lo = []
    A = h - u - K
    lo.append(math.log(A) + 2 * lc(b, h + 1 + K))
    lo.append(math.log(A + 4) + 2 * lc(b, h + K))
    for j in range(v, K - 1):
        lo.append(math.log(4) + 2 * lc(b, h + 1 + j))
    logFo = logsumexp(lo)

    logPe = lc(b, h + 1 + K + u) + lc(b, h + 1 + K - u)
    logPo = lc(b, h + 1 + K + u) + lc(b, h + K - u)
    re = min(1.0, math.exp(math.log(b) + logPe - logFe))
    ro = min(1.0, math.exp(math.log(b) + logPo - logFo))
    return re, ro


def audit_continuum_convergence() -> None:
    rows = []
    errors = []
    for b in [10007, 40009, 160001, 640001]:
        root = math.sqrt(b)
        u = round(0.70 * root)
        K = 2 * round(0.55 * root)
        alpha = u / root
        beta = K / root
        re, ro = rho_pair(b, u, K)
        scaled = root * (ro - re)
        predicted = math.exp(-4 * alpha * alpha) * (
            (alpha - beta / 2) * math.exp(3 * beta * beta) - 4 * alpha
        )
        assert ro > re
        errors.append(abs(scaled - predicted))
        rows.append((b, u, K, scaled, predicted))
    assert all(errors[j + 1] < errors[j] for j in range(len(errors) - 1))
    assert errors[-1] < 0.025
    print("CONTINUUM_CONVERGENCE", rows)


def audit_finite_rectangle_contribution() -> None:
    rows = []
    for b in [10007, 40009, 160001]:
        root = math.sqrt(b)
        h = (b - 1) // 2
        logW = lc(2 * b, b)
        total = 0.0
        cells = 0
        for u in range(math.ceil(0.70 * root), math.floor(0.75 * root) + 1):
            lo = math.ceil(1.10 * root)
            if lo % 2:
                lo += 1
            hi = math.floor(1.20 * root)
            for K in range(lo, hi + 1, 2):
                re, ro = rho_pair(b, u, K)
                assert ro > re
                source = math.exp(2 * lc(b, h + 1 + K) - logW)
                total += (2 * (h - u - K) / b) * source * (ro - re)
                cells += 1
        assert total > 0
        rows.append((b, cells, total))
    print("FINITE_RECTANGLE_LOWER_SUM", rows)


def main() -> None:
    audit_exact_formulas_and_joint_counts()
    audit_continuum_convergence()
    audit_finite_rectangle_contribution()
    print("PASS affine adjacent-variation continuum obstruction audit")


if __name__ == "__main__":
    main()
