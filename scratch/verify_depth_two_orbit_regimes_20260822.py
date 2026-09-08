#!/usr/bin/env python3
"""Exact checks for the depth-two orbit-factor regime split."""

from fractions import Fraction
from math import comb


def choose(n: int, k: int) -> int:
    return comb(n, k) if 0 <= k <= n else 0


def falling(n: int, length: int) -> int:
    answer = 1
    for offset in range(length):
        answer *= n - offset
    return answer


def shell_f(r: int, j: int) -> Fraction:
    b = 2 * r + 1
    k = r - 2
    answer = Fraction()
    for h in range(k + 1):
        eberlein = sum(
            (-1) ** (j - a)
            * choose(j, a)
            * choose(k - j, h - a)
            * choose(b - k - j, k - j - h + a)
            for a in range(j + 1)
        )
        shell = choose(k, h) * choose(b - k, k - h)
        weight = 6 if h == 0 else (1 if h == k else 2)
        answer += Fraction(b * weight * eberlein, shell)
    return answer


def hahn_f(r: int, j: int) -> Fraction:
    b = 2 * r + 1
    k = r - 2
    denominator = falling(k, j) * falling(r + 3, j)
    answer = Fraction()
    for h in range(k + 1):
        numerator = sum(
            (-1) ** (j - a)
            * choose(j, a)
            * falling(h, a)
            * falling(h + 5, a)
            * falling(k - h, j - a) ** 2
            for a in range(j + 1)
        )
        weight = 6 if h == 0 else (1 if h == k else 2)
        answer += Fraction(b * weight * numerator, denominator)
    return answer


def closed_j2(r: int) -> Fraction:
    return Fraction(
        4 * r**4 + 20 * r**3 - 73 * r**2 - 5 * r + 18,
        3 * (r + 2) * (r + 3),
    )


def closed_j3(r: int) -> Fraction:
    return Fraction(
        50 * r**3 - 155 * r**2 + 40 * r + 65,
        (r + 1) * (r + 2) * (r + 3),
    )


def top_f(r: int) -> Fraction:
    b = 2 * r + 1
    k = r - 2
    answer = Fraction()
    for t in range(k + 1):
        h = k - t
        weight = 6 if h == 0 else (1 if h == k else 2)
        answer += Fraction(weight * (-1) ** t, choose(r + 3, t))
    return b * answer


def main() -> None:
    # Independent exact forms of the same orbit scalar.
    for r in range(4, 31):
        for j in range(2, r - 1):
            assert shell_f(r, j) == hahn_f(r, j)

    for r in range(4, 61):
        assert shell_f(r, 2) == closed_j2(r)
        if r >= 5:
            assert shell_f(r, 3) == closed_j3(r)
            assert 7 * closed_j3(r) >= 55
            factorized_difference = 5 * (r - 5) * (59 * r * r + 12 * r - 5)
            numerator_difference = (
                7 * (50 * r**3 - 155 * r**2 + 40 * r + 65)
                - 55 * (r + 1) * (r + 2) * (r + 3)
            )
            assert numerator_difference == factorized_difference
        assert shell_f(r, r - 2) == top_f(r)
        assert abs(top_f(r) - (2 * r - 3)) <= Fraction(20, r)

    minima = {}
    for r in range(4, 61):
        value, level = min((shell_f(r, j), j) for j in range(2, r - 1))
        minima[r] = level
        assert value > 0
    assert all(minima[r] == r - 2 for r in range(7, 15))
    assert all(minima[r] == 3 for r in range(15, 61))
    for r in range(20, 61):
        first = max(2, (r + 9) // 10)
        last = min(r - 2, 9 * r // 10)
        assert all(shell_f(r, j) >= Fraction(r, 2) for j in range(first, last + 1))

    # Fixed-level leading constants, recorded with exact rational errors.
    for j in range(2, 11):
        value = shell_f(500, j)
        if j % 2 == 0:
            ratio = value / (500 * 500)
            assert abs(ratio - Fraction(4, j + 1)) < Fraction(1, 100)
        else:
            assert abs(value - 25 * (j - 1)) < 12

    print(
        "PASS depth-two orbit regimes: exact Hahn identity, closed j=2,3, "
        "top bound, minima top for r=7..14 and j=3 for r=15..60"
    )


if __name__ == "__main__":
    main()
