#!/usr/bin/env python3
"""Finite audit for pairing--defect incidence and the local tour bank."""

from fractions import Fraction
from itertools import combinations
from math import comb, factorial, ceil, log2


def pairings(items):
    items = tuple(items)
    if not items:
        yield ()
        return
    x = items[0]
    for j in range(1, len(items)):
        y = items[j]
        rest = items[1:j] + items[j + 1:]
        for tail in pairings(rest):
            yield ((x, y),) + tail


def defect_one(pairing, middle):
    inside = sum(x in middle and y in middle for x, y in pairing)
    outside = sum(x not in middle and y not in middle for x, y in pairing)
    return inside == outside == 1


def formula(b, d):
    a = b - d
    return factorial(a) * factorial(d) * (
        a * d * (a * d - 1) + (a * (a - 1) + d * (d - 1)) // 4
    )


def formula_integral(b, d):
    a = b - d
    return factorial(a) * factorial(d) * (
        4 * a * d * (a * d - 1) + a * (a - 1) + d * (d - 1)
    ) // 4


def audit_pairings(b):
    universe = tuple(range(2 * b))
    all_pairings = tuple(pairings(universe))
    base = frozenset(range(b))
    degree = sum(defect_one(p, base) for p in all_pairings)
    claimed_degree = comb(b, 2) ** 2 * factorial(b - 2)
    assert degree == claimed_degree == formula_integral(b, 0)

    actual = []
    for d in range(b + 1):
        other = frozenset(range(b - d)) | frozenset(range(b, b + d))
        count = sum(defect_one(p, base) and defect_one(p, other)
                    for p in all_pairings)
        assert count == formula_integral(b, d), (b, d, count)
        actual.append(count)

    ratios = [Fraction(actual[d], degree) for d in range(1, (b - 1) // 2 + 1)]
    if b >= 7:
        assert max(ratios) == Fraction(5 * (b - 2), b * b)
    elif b == 5:
        assert max(ratios) == Fraction(16, 25)
    else:
        assert max(ratios) == Fraction(5, 9)

    stratum = b * (b - 1) * 2 ** (b - 2)
    W = comb(2 * b, b)
    assert Fraction(degree, len(all_pairings)) == Fraction(stratum, W)
    print(f"PASS pairing census: b={b} pairings={len(all_pairings)} degree={degree}")


def syndrome(word, columns):
    out = 0
    for i, col in enumerate(columns):
        if word >> i & 1:
            out ^= col
    return out


def audit_code(b):
    r = ceil(log2(b + 1))
    columns = tuple(range(1, b + 1))
    code = [x for x in range(1 << b) if syndrome(x, columns) == 0]
    for x, y in combinations(code, 2):
        assert (x ^ y).bit_count() >= 3
    assert len(code) >= 2 ** (b - r)
    print(f"PASS code bank: b={b} r={r} size={len(code)}")


def audit():
    for b in (3, 5, 7):
        audit_pairings(b)
        audit_code(b)


if __name__ == "__main__":
    audit()
