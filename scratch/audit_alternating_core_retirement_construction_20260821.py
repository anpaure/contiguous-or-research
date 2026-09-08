#!/usr/bin/env python3
"""Exact audit of the alternating-core affine retirement construction."""

from __future__ import annotations

from fractions import Fraction
from math import comb, log, sqrt
import sys


def c(b: int, k: int) -> int:
    return comb(b, k) if 0 <= k <= b else 0


def L(b: int, r: int) -> int:
    return c(b, r) ** 2


def E(b: int, r: int, u: int) -> int:
    return c(b, r + u) * c(b, r - u)


def ideal(b: int, r: int, q: int, orient: int) -> Fraction:
    """orient=1 adds A at odd offsets; orient=0 adds B."""
    if q % 2 == 0:
        u = q // 2
        den = b - 2 * u
    else:
        u = (q - 1) // 2
        den = b + 2 * u + 1
    num = b - r - u if orient else r - u
    return Fraction(E(b, r, u) * num, den) if den and num >= 0 else Fraction(0)


def word(b: int, r: int) -> list[int]:
    m = (b - 1) // 2
    return [int((m * x) % b < r) for x in range(b)]


def good_counts(b: int, r: int, H: int) -> tuple[int, int]:
    w = word(b, r)
    out = [0, 0]
    for p in range(b):
        bits = [w[(p + q) % b] for q in range(1, H + 1)]
        if all(bits[j] != bits[j - 1] for j in range(1, H)):
            out[bits[0]] += 1
    return out[0], out[1]


def audit_instance(b: int, H: int) -> tuple[Fraction, Fraction]:
    g = b // 4
    caps: dict[tuple[int, int], Fraction] = {}
    xs: dict[tuple[int, int, int], Fraction] = {}
    direct_counts = 0
    for r in range(g, b - g + 1):
        d = abs(2 * r - b)
        total_good = max(0, b - d - H + 2)
        guaranteed = total_good // 2
        c0, c1 = good_counts(b, r, H)
        direct_counts += b
        assert c0 + c1 == total_good, (b, H, r, total_good, c0, c1)
        assert abs(c0 - c1) <= 1, (b, H, r, c0, c1)
        assert min(c0, c1) >= guaranteed, (b, H, r, d, guaranteed, c0, c1)
        for orient in (0, 1):
            cap = Fraction(guaranteed * L(b, r), b)
            caps[r, orient] = cap
            prev = cap
            for q in range(1, H + 1):
                value = min(cap, ideal(b, r, q, orient))
                assert value <= prev
                xs[r, orient, q] = value
                prev = value

    # The untruncated two-orientation ideal is an exact simultaneous
    # profile cover, and each orientation is a nonincreasing path.
    for r in range(b + 1):
        for orient in (0, 1):
            prev = Fraction(L(b, r) * ((b - r) if orient else r), b) if b else Fraction(0)
            for q in range(1, H + 1):
                value = ideal(b, r, q, orient)
                assert value <= prev, ("ideal monotonicity", b, H, r, orient, q, prev, value)
                prev = value
    for q in range(1, H + 1):
        full_loads: dict[int, Fraction] = {}
        for r in range(b + 1):
            for orient in (0, 1):
                s = r + (q + orient) // 2
                full_loads[s] = full_loads.get(s, Fraction(0)) + ideal(b, r, q, orient)
        for s in range(q, b + 1):
            quota = c(b, s) * c(b, s - q)
            assert full_loads.get(s, Fraction(0)) == quota, (
                "ideal quota", b, H, q, s, full_loads.get(s, 0), quota
            )

    covered = Fraction(0)
    target_total = Fraction(0)
    for q in range(1, H + 1):
        loads: dict[int, Fraction] = {}
        for r in range(g, b - g + 1):
            for orient in (0, 1):
                z = (q + orient) // 2
                s = r + z
                loads[s] = loads.get(s, Fraction(0)) + xs[r, orient, q]
        for s, load in loads.items():
            quota = c(b, s) * c(b, s - q)
            assert load <= quota, (b, H, q, s, load, quota)
        covered += sum(loads.values(), Fraction(0))
        target_total += c(2 * b, b + q)
    deficit = target_total - covered
    W = Fraction(c(2 * b, b))
    print("ALT_RET", b, H, "deficit/W", float(deficit / W), "scaled_b14", float(deficit / W * b ** 0.25), "direct", direct_counts)
    return deficit, W


def main() -> None:
    values = tuple(map(int, sys.argv[1:])) or (31, 61, 101, 151, 251)
    for b in values:
        H = min(b // 4, int(sqrt(b * log(b))))
        audit_instance(b, H)
    print("PASS alternating-core retirement construction audit")


if __name__ == "__main__":
    main()
