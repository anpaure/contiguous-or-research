#!/usr/bin/env python3
"""Finite audit for MATH_THEOREM_CLUSTERED_PROFILE_CAPACITY_DEFICIT_20260821.md."""

import math


def choose(n, k):
    return math.comb(n, k) if 0 <= k <= n else 0


def formula_capacity(b, q, s):
    return (
        (b - s - q + 1) * choose(b, s) ** 2
        + (s - 2 * q + 1) * choose(b, s - q) ** 2
        + 2 * sum(choose(b, s - z) ** 2 for z in range(1, q))
    ) / b


def direct_phase_capacity(b, q, s):
    total = 0
    for r in range(q, b - q + 1):
        phases = set(range(r))
        count = 0
        for p in range(b):
            z = sum(((p + j) % b) in phases for j in range(1, q + 1))
            if r + z == s:
                count += 1
        total += count * choose(b, r) ** 2 / b
    return total


for b in (11, 13, 17, 23, 31):
    for q in range(1, (b - 1) // 4 + 1):
        for s in range(2 * q, b - q + 1):
            a = formula_capacity(b, q, s)
            d = direct_phase_capacity(b, q, s)
            assert abs(a - d) <= 1e-9 * max(1.0, abs(a), abs(d)), (b, q, s, a, d)
    print(f"exact capacity PASS b={b}")


for b in (101, 503, 2003, 5003, 10003):
    H = math.ceil(math.sqrt(b * math.log(b)))
    log_w = math.lgamma(2 * b + 1) - 2 * math.lgamma(b + 1)
    c = [
        math.exp(
            math.lgamma(b + 1)
            - math.lgamma(j + 1)
            - math.lgamma(b - j + 1)
            - log_w / 2
        )
        for j in range(b + 1)
    ]
    pref = [0.0]
    for y in c:
        pref.append(pref[-1] + y * y)

    deficit = 0.0
    for q in range(1, H + 1):
        for s in range(max(q, b // 4), min(b, 3 * b // 4) + 1):
            p = c[s] * c[s - q]
            t = (
                (b - s - q + 1) * c[s] ** 2
                + (s - 2 * q + 1) * c[s - q] ** 2
                + 2 * (pref[s] - pref[s - q + 1])
            ) / b
            if t < p:
                u = math.log(c[s] / c[s - q])
                assert t / p + 1e-12 >= 1 - q / b + u * u / 4, (b, q, s)
                assert abs(s - (b + q) / 2) <= (b + 1) / (2 * math.sqrt(b * q)) + 1e-9
                deficit += p - t
    print(
        f"asymptotic inequalities PASS b={b} H={H} "
        f"deficit/W={deficit:.12g} scaled={deficit*b**0.25:.12g}"
    )

print("ALL CLUSTERED PROFILE-CAPACITY CHECKS PASS")
