#!/usr/bin/env python3
"""Fail-closed audit for affine-balanced row loads and the SCD diagonal barrier."""

from __future__ import annotations

import itertools
import math
from collections import Counter
from fractions import Fraction


def is_prime(n: int) -> bool:
    return n >= 2 and all(n % d for d in range(2, math.isqrt(n) + 1))


def choose(n: int, k: int) -> int:
    return math.comb(n, k) if 0 <= k <= n else 0


def affine_sets(b: int) -> list[set[int]]:
    a = (b - 1) // 2
    return [{x for x in range(b) if (a * x) % b < r} for r in range(b + 1)]


def phase_multiplicities(b: int, q: int, s: int) -> tuple[Counter[int], int]:
    ps = affine_sets(b)
    mult: Counter[int] = Counter()
    holes = 0
    for p in range(b):
        window = {(p + j) % b for j in range(1, q + 1)}
        vals = [r + len(ps[r] & window) for r in range(b + 1)]
        assert all(vals[r + 1] - vals[r] in (1, 2) for r in range(b))
        hits = [r for r, val in enumerate(vals) if val == s]
        assert len(hits) <= 1
        if hits:
            mult[hits[0]] += 1
        else:
            holes += 1
    return mult, holes


def audit_affine_formula_and_main_ranks() -> None:
    for b in range(5, 102, 2):
        if not is_prime(b):
            continue
        h = (b - 1) // 2
        ps = affine_sets(b)
        for r in range(b + 1):
            explicit = {(-2 * y) % b for y in range(r)}
            assert ps[r] == explicit
        for q in range(1, min(15, b - 1) + 1):
            for x2 in range(-min(12, h), min(12, h) + 1):
                # Work with 2*x to respect the parity of (b+q)/2.
                if (b + q + x2) % 2:
                    continue
                s = (b + q + x2) // 2
                if not (q <= s <= b):
                    continue
                mult, holes = phase_multiplicities(b, q, s)
                assert sum(mult.values()) + holes == b
                exceptional_bound = 8 * (q + abs(x2) + 3)
                if q % 2 == 0:
                    r0 = s - q // 2
                    assert b - mult[r0] <= exceptional_bound
                    assert sum(v for r, v in mult.items() if r != r0) <= exceptional_bound
                else:
                    rm = s - (q + 1) // 2
                    rp = s - (q - 1) // 2
                    assert abs(mult[rm] - b / 2) <= exceptional_bound
                    assert abs(mult[rp] - b / 2) <= exceptional_bound
                    assert sum(v for r, v in mult.items() if r not in (rm, rp)) <= exceptional_bound


def walecki_factor_edges(b: int) -> list[tuple[int, ...]]:
    """A Hamilton decomposition of K_b, represented by cyclic vertex orders."""
    assert b % 2 == 1
    h = (b - 1) // 2
    inf = b - 1
    cycles = []
    # Standard rotational Walecki cycles on Z_(b-1) plus infinity.
    base = [inf]
    for j in range(h):
        base.extend([j, (-j - 1) % (b - 1)])
    assert len(base) == b
    for shift in range(h):
        cyc = tuple(inf if x == inf else (x + shift) % (b - 1) for x in base)
        cycles.append(cyc)
    edges = Counter()
    for cyc in cycles:
        for i in range(b):
            edges[tuple(sorted((cyc[i], cyc[(i + 1) % b])))] += 1
    assert len(edges) == choose(b, 2) and set(edges.values()) == {1}
    return cycles


def window_mult(orders: list[tuple[int, ...]], k: int) -> Counter[frozenset[int]]:
    b = len(orders[0])
    out: Counter[frozenset[int]] = Counter()
    for order in orders:
        for i in range(b):
            out[frozenset(order[(i + j) % b] for j in range(k))] += 1
    return out


def audit_window_moments() -> None:
    for b in (5, 7):
        orders = walecki_factor_edges(b)
        cr = choose(b, 2)
        for k in range(1, b):
            mult = window_mult(orders, k)
            assert sum(mult.values()) == cr
            universe = [frozenset(x) for x in itertools.combinations(range(b), k)]
            rho = cr / choose(b, k)
            second = sum(mult[u] ** 2 for u in universe) / choose(b, k)
            var = second - rho * rho
            support = sum(mult[u] > 0 for u in universe) / choose(b, k)
            target = universe[0]
            vals = []
            for perm in itertools.permutations(range(b)):
                inv = [0] * b
                for old, new in enumerate(perm):
                    inv[new] = old
                pre = frozenset(inv[x] for x in target)
                vals.append(mult[pre])
            mean_brute = sum(vals) / len(vals)
            var_brute = sum((v - mean_brute) ** 2 for v in vals) / len(vals)
            assert abs(mean_brute - rho) < 1e-12
            assert abs(var_brute - var) < 1e-12
            assert abs(sum(v == 0 for v in vals) / len(vals) - (1 - support)) < 1e-12
            assert support <= min(1.0, rho) + 1e-12
            if rho <= 1:
                assert var + 1e-12 >= rho * (1 - rho)


def scd_distance_bound(b: int, r: int) -> int:
    m = min(r, b - r)
    cr = choose(b, r)
    # K=r*C_r/b is integral whenever the conditional tight factor exists.
    assert cr % b == 0
    krow = r * cr // b
    ans = 0
    for a in range(m + 1):
        na = choose(b, a) - choose(b, a - 1)
        desired = cr - choose(b, a - 1)
        ans += na * abs(desired - krow)
    return ans


def audit_scd_distance() -> None:
    rows = []
    for b in (11, 31, 61, 101, 251, 509, 1009):
        if not is_prime(b):
            continue
        r = (b - 1) // 2
        dist = scd_distance_bound(b, r)
        ratio = dist / choose(b, r) ** 2
        rows.append((b, ratio))
        assert ratio > 0.20
    assert rows[-1][1] > 0.245
    print("SCD_DISTANCE", rows)


def audit_scd_forced_switches() -> None:
    for b in range(3, 16, 2):
        for a in range((b - 1) // 2 + 1):
            for c in range((b - 1) // 2 + 1):
                lo, hi = max(a, c), min(b - a, b - c)
                ranks = list(range(lo, hi + 1))
                feasible = []
                for bits in itertools.product((0, 1), repeat=len(ranks)):
                    # 1=A, 0=B.  Interior q=1 targets forbid B then A.
                    if any(bits[i] == 0 and bits[i + 1] == 1 for i in range(len(bits) - 1)):
                        continue
                    # Unequal-bottom boundary targets force the wider side.
                    if a < c and bits[-1] != 1:
                        continue
                    if a > c and bits[0] != 0:
                        continue
                    feasible.append(bits)
                assert feasible
                if a < c:
                    assert feasible == [tuple(1 for _ in ranks)]
                elif a > c:
                    assert feasible == [tuple(0 for _ in ranks)]
                else:
                    # Exactly one A-to-B threshold, including the two constants.
                    assert len(feasible) == len(ranks) + 1

        h = (b - 1) // 2
        ch = choose(b, h)
        assert 2 * h * ch * ch // b == (b - 1) * ch * ch // b
        assert ch * ch - 2 * h * ch * ch // b == ch * ch // b


def audit_profile_diagnostics() -> None:
    rows = []
    for b in (101, 251, 509, 1009, 2003):
        if not is_prime(b):
            continue
        q = 2 * max(1, round(math.sqrt(b) / 2))
        # A fixed left-shoulder profile d approximately -1/2 for c approximately 1.
        center2 = b + q
        s = round(center2 / 2 - math.sqrt(b) / 2)
        mult, _ = phase_multiplicities(b, q, s)
        r0 = s - q // 2
        minor_num = sum(m * choose(b, r) ** 2 for r, m in mult.items() if r != r0)
        profile = choose(b, s) * choose(b, s - q)
        minor_ratio = float(Fraction(minor_num, b * profile))
        alpha = float(Fraction(choose(b, r0), choose(b, s)))
        rows.append((b, q, s, mult[r0], minor_ratio, alpha))
    print("AFFINE_PROFILE", rows)


def main() -> None:
    audit_affine_formula_and_main_ranks()
    audit_window_moments()
    audit_scd_distance()
    audit_scd_forced_switches()
    audit_profile_diagnostics()
    print("PASS affine-balanced factor row-load and SCD diagonal audit")


if __name__ == "__main__":
    main()
