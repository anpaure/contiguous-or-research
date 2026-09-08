#!/usr/bin/env python3
"""Exact finite arithmetic checks for the all-offset token rounding note.

Run only on H100.  This checks the integer token counts, containment
biregularity identity, pair-load formulae, and the claimed beta envelope.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb, isqrt, log


def check_prime(b: int) -> None:
    g = b // 4
    H = min(g // 2 - 1, max(1, isqrt(b * max(1, int(log(b))))))
    for q in range(1, H + 1):
        beta = Fraction(1, comb(g, q))
        max_pair = Fraction(0)
        for r in range(g, b - g + 1):
            L = comb(b, r) ** 2
            for z in range(q + 1):
                n = b - r - q + 1 if z == 0 else r - q + 1 if z == q else 2
                assert n > 0
                Q = Fraction(n * L, b)
                assert Q.denominator == 1
                Dc = comb(b - r, z) * comb(r, q - z)
                assert Dc >= comb(g, z) * comb(g, q - z) >= comb(g, q)
                s = r + z
                P = comb(b, s) * comb(b, s - q)
                N = comb(s, r) * comb(b + q - s, b - r)
                assert L * Dc == P * N
                # Worst rho is one.  Exact three pair-load envelopes:
                source_target = Fraction(n, b * Dc)
                token_source = Fraction(1, L)
                token_target = Fraction(1, P)
                max_pair = max(max_pair, source_target, token_source, token_target)
            assert sum(
                b - r - q + 1 if z == 0 else r - q + 1 if z == q else 2
                for z in range(q + 1)
            ) == b
        assert max_pair <= beta
    print(f"PASS exact b={b} g={g} H={H}")


def asymptotic_table() -> None:
    for b in (101, 1009, 10007, 100003, 1000003):
        g = b // 4
        H = (b * log(b)) ** 0.5
        q1 = b ** (-1 / 3) * log(b) ** 4
        tail = H * b ** (-2 / 3) * log(b) ** 4
        print(f"b={b} q1_proxy={q1:.6g} tail_proxy={tail:.6g}")


if __name__ == "__main__":
    for b in (11, 13, 17, 23, 31, 43, 101, 251):
        check_prime(b)
    asymptotic_table()
