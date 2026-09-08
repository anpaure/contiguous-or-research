#!/usr/bin/env python3
"""Research probe for exact half-step histogram recurrences (H100 only)."""

from __future__ import annotations

import argparse
import math


def lc(n: int, k: int) -> float:
    if not 0 <= k <= n:
        return float("-inf")
    return math.lgamma(n + 1) - math.lgamma(k + 1) - math.lgamma(n - k + 1)


def lse(xs: list[float]) -> float:
    if not xs:
        return float("-inf")
    m = max(xs)
    return m + math.log(sum(math.exp(x - m) for x in xs))


def ihist(u: int, ell: int, j: int) -> int:
    if ell <= 0 or j <= 0:
        return 0
    z = min(u, ell)
    if j < z:
        return 2
    if j == z:
        return abs(u - ell) + 1
    return 0


def neven(b: int, u: int, k: int, d: int) -> int:
    if d == 0:
        if k == 0:
            return b - u
        return b - 2 * u - 2 * k + 1
    return ihist(u, k, d) + ihist(u, k + 1, d)


def nodd(b: int, u: int, k: int, d: int) -> int:
    h = (b - 1) // 2
    if k == 0:
        return h - u if d == 0 else h + u + 1 if d == 1 else 0
    D = min(u, k) + 1
    if d == 0:
        return h - u - k
    if d == 1:
        return h - u - k + 3
    if 2 <= d < D:
        return 4
    if d == D:
        return 2 * (abs(u - k) + 1)
    return 0


def rho_even(b: int, u: int, K: int) -> float:
    h = (b - 1) // 2
    qlog = lc(b, h + 1 + K + u) + lc(b, h + 1 + K - u)
    terms = []
    for k in range(K + 1):
        d = K - k
        n = neven(b, u, k, d)
        if n:
            terms.append(math.log(n) + 2 * lc(b, h + 1 + k))
    lr = lse(terms) - math.log(b) - qlog
    return min(1.0, math.exp(-lr)) if lr < 745 else 0.0


def rho_odd(b: int, u: int, K: int) -> float:
    h = (b - 1) // 2
    qlog = lc(b, h + 1 + K + u) + lc(b, h + K - u)
    if K == 0:
        terms = [math.log(2 * (h - u)) + 2 * lc(b, h + 1)]
    else:
        terms = []
        for k in range(K + 1):
            d = K - k
            n = nodd(b, u, k, d)
            if n:
                terms.append(math.log(n) + 2 * lc(b, h + 1 + k))
    lr = lse(terms) - math.log(b) - qlog
    return min(1.0, math.exp(-lr)) if lr < 745 else 0.0


def scan(b: int, H: int, Kmax: int) -> None:
    re: dict[tuple[int, int], float] = {}
    ro: dict[tuple[int, int], float] = {}
    for u in range(1, H // 2 + 2):
        for K in range(Kmax + 3):
            re[u, K] = rho_even(b, u, K)
            ro[u, K] = rho_odd(b, u, K)
    long_names = [f"long_o_t{t}_j1" for t in range(1, 11)]
    stats = {x: (-1.0, None) for x in ["align_e", "align_o", "def_e", "def_o", "four_e_0", "four_e_1", "four_e_2", "four_o_0", "four_o_1", "four_o_2", "adj_eo_in", "adj_eo_out", "adj_oe_in", "adj_oe_out", "odd_defect_min_violation"] + long_names}
    def put(name: str, d: float, data) -> None:
        if d > stats[name][0]:
            stats[name] = (d, data)
    for u in range(1, (H - 2) // 2 + 1):
        for K in range(Kmax + 1):
            put("align_e", re[u + 1, K] - re[u, K], (u, K, re[u, K], re[u + 1, K]))
            put("align_o", ro[u + 1, K] - ro[u, K], (u, K, ro[u, K], ro[u + 1, K]))
            put("def_e", re[u + 1, K + 1] - re[u, K], (u, K, re[u, K], re[u + 1, K + 1]))
            put("def_o", ro[u + 1, K + 1] - ro[u, K], (u, K, ro[u, K], ro[u + 1, K + 1]))
            put("odd_defect_min_violation", min(re[u + 1, K], ro[u + 1, K + 1]) - ro[u, K], (u, K, ro[u, K], re[u + 1, K], ro[u + 1, K + 1]))
            if 2 * u + 4 <= H:
                for j in range(3):
                    put(f"four_e_{j}", re[u + 2, K + j] - re[u, K], (u, K, re[u, K], re[u + 2, K + j]))
                    put(f"four_o_{j}", ro[u + 2, K + j] - ro[u, K], (u, K, ro[u, K], ro[u + 2, K + j]))
            for tt in range(1, 11):
                if 2 * (u + tt) + 1 <= H:
                    put(f"long_o_t{tt}_j1", ro[u + tt, K + 1] - ro[u, K], (u, K, ro[u, K], ro[u + tt, K + 1]))
    for u in range(1, H // 2 + 1):
        for K in range(Kmax + 1):
            put("adj_eo_in", ro[u, K] - re[u, K], (u, K, re[u, K], ro[u, K]))
            put("adj_eo_out", ro[u, K + 1] - re[u, K], (u, K, re[u, K], ro[u, K + 1]))
            if K >= 1 and 2 * u + 2 <= H:
                put("adj_oe_in", re[u + 1, K - 1] - ro[u, K], (u, K, ro[u, K], re[u + 1, K - 1]))
            if 2 * u + 2 <= H:
                put("adj_oe_out", re[u + 1, K] - ro[u, K], (u, K, ro[u, K], re[u + 1, K]))
    print("SCAN", b, H, Kmax)
    for name, val in stats.items():
        d = val[0]
        print(name, val, "b*d", b * d, "b2/q*d", (b * b / max(1, (2 * val[1][0] + 1))) * d if val[1] else None, "sqrtb*d", math.sqrt(b) * d)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("b", type=int)
    ap.add_argument("H", type=int, nargs="?")
    ap.add_argument("Kmax", type=int, nargs="?")
    z = ap.parse_args()
    H = z.H or int(math.sqrt(z.b * math.log(z.b)))
    Kmax = z.Kmax or 3 * H
    assert 2 * (H + Kmax) < (z.b - 1) // 2
    scan(z.b, H, Kmax)


if __name__ == "__main__":
    main()
