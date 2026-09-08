#!/usr/bin/env python3
"""Exact checks for an ideal alternating-orientation retirement flow."""

from __future__ import annotations

from fractions import Fraction
from math import comb


def c(b: int, k: int) -> int:
    return comb(b, k) if 0 <= k <= b else 0


def even_quota(b: int, r: int, u: int) -> int:
    return c(b, r + u) * c(b, r - u)


def odd_quota(b: int, r: int, u: int) -> int:
    # Profile s=r+u receives B-first source r and A-first source r-1.
    return c(b, r + u) * c(b, r - u - 1)


def ae(b: int, r: int, u: int) -> Fraction:
    e = even_quota(b, r, u)
    return Fraction(e * (b - r - u), b - 2 * u)


def be(b: int, r: int, u: int) -> Fraction:
    e = even_quota(b, r, u)
    return Fraction(e * (r - u), b - 2 * u)


def ao(b: int, r: int, u: int) -> Fraction:
    e = even_quota(b, r, u)
    return Fraction(e * (b - r - u), b + 2 * u + 1)


def bo(b: int, r: int, u: int) -> Fraction:
    e = even_quota(b, r, u)
    return Fraction(e * (r - u), b + 2 * u + 1)


def main() -> None:
    bad_a = []
    bad_b = []
    bad_upper = []
    bad_lower = []
    for b in range(5, 102, 2):
        for u in range(0, b // 4):
            for r in range(u + 1, b - u):
                assert ae(b, r, u) + be(b, r, u) == even_quota(b, r, u)
                assert ao(b, r - 1, u) + bo(b, r, u) == odd_quota(b, r, u)
                assert ao(b, r, u) <= ae(b, r, u)
                assert bo(b, r, u) <= be(b, r, u)
                if u + 1 < b // 2 and r >= u + 2 and r <= b - u - 2:
                    if ae(b, r, u + 1) > ao(b, r, u):
                        bad_a.append((b, u, r, ae(b, r, u + 1) / ao(b, r, u)))
                    if be(b, r, u + 1) > bo(b, r, u):
                        bad_b.append((b, u, r, be(b, r, u + 1) / bo(b, r, u)))
                    cur_avg = Fraction(even_quota(b, r - 1, u) + even_quota(b, r, u), 2)
                    nxt_avg = Fraction(even_quota(b, r - 1, u + 1) + even_quota(b, r, u + 1), 2)
                    oq = odd_quota(b, r, u)
                    if oq > cur_avg:
                        bad_upper.append((b, u, r, Fraction(oq, 1) / cur_avg))
                    if oq < nxt_avg:
                        bad_lower.append((b, u, r, Fraction(oq, 1) / nxt_avg))
    print("BAD_A", bad_a[:20], len(bad_a))
    print("BAD_B", bad_b[:20], len(bad_b))
    print("BAD_SYM_UPPER", bad_upper[:20], len(bad_upper))
    print("BAD_SYM_LOWER", bad_lower[:20], len(bad_lower))


if __name__ == "__main__":
    main()
