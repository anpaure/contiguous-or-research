#!/usr/bin/env python3
"""Closed all-j Hahn formula for the two omitted-triple local defects."""

from __future__ import annotations

import argparse
from fractions import Fraction
from math import comb, factorial


def falling(value: int, length: int) -> int:
    answer = 1
    for offset in range(length):
        answer *= value - offset
    return answer


def choose(value: int, size: int) -> int:
    return comb(value, size) if 0 <= size <= value else 0


def falling_table(value: int, maximum: int) -> list[int]:
    answer = [1]
    for length in range(1, maximum + 1):
        answer.append(answer[-1] * (value - length + 1))
    return answer


def endpoint_hahn(K: int, L: int, m: int, inside: int, outside: int) -> Fraction:
    """The normalized signed injection polynomial e_m(inside,outside)."""
    fall_K = falling_table(K, m)
    fall_L = falling_table(L, m)
    fall_inside = falling_table(inside, m)
    fall_outside = falling_table(outside, m)
    answer = Fraction(0)
    for h in range(m + 1):
        q = m - h
        if h > inside or q > outside:
            continue
        answer += Fraction(
            (-1) ** q
            * comb(m, h)
            * fall_inside[h]
            * fall_outside[q],
            fall_K[h] * fall_L[q],
        )
    return answer


def quadratic_hahn_sum(K: int, L: int, m: int, excess: int) -> Fraction:
    """Sum (K+1-a)(a+1)e_m(a,K+excess-a), 0<=a<=K."""
    n = K + excess
    first = choose(n + 1, m + 1)
    second = choose(n + 1, m + 2)
    third = choose(n + 1, m + 3)
    fall_K = falling_table(K, m)
    fall_L = falling_table(L, m)
    facts = [1]
    for value in range(1, m + 1):
        facts.append(facts[-1] * value)
    answer = Fraction(0)
    for h in range(m + 1):
        q = m - h
        if excess == 1:
            bracket = q * first + (2 * q + 1) * second + (q + 1) * third
        elif excess == 2:
            bracket = (q - 1) * first + 2 * q * second + (q + 1) * third
        else:
            raise ValueError("excess must be one or two")
        positional_sum = facts[h] * facts[q] * (h + 1) * bracket
        if excess == 2 and q == 0:
            positional_sum += (n + 1) * falling(n, m)
        answer += Fraction(
            (-1) ** q * comb(m, h) * positional_sum,
            fall_K[h] * fall_L[q],
        )
    return answer


def parameters(r: int) -> tuple[Fraction, ...]:
    q1 = Fraction(
        4 * (r + 2) * (2 * r - 3),
        r**3 * (r - 3) * (r - 2) * (r - 1) * (r + 1),
    )
    e1_middle = -Fraction(2 * r - 3, r**3 * (r - 1) * (r + 1))
    q2 = Fraction(
        2 * (4 * r**2 + 6 * r - 15),
        r**3 * (r - 3) * (r - 2) * (r - 1) * (r + 1),
    )
    e2_middle = -Fraction(4 * r - 5, r**3 * (r - 1) * (r + 1))
    e1_lower = -Fraction(
        (r + 4) * (4 * r**2 - 13 * r + 8),
        2 * r**3 * (r - 2) * (r - 1) * (r + 1),
    )
    e2_lower_penultimate = -Fraction(
        (r - 4) * (4 * r - 5),
        r**3 * (r - 2) * (r - 1) * (r + 1),
    )
    e2_lower_last = -Fraction(
        4 * r**3 + 3 * r**2 - 36 * r + 30,
        2 * r**3 * (r - 2) * (r - 1) * (r + 1),
    )
    return (
        q1,
        e1_middle,
        q2,
        e2_middle,
        e1_lower,
        e2_lower_penultimate,
        e2_lower_last,
    )


def defect_rows(r: int, level: int) -> tuple[tuple[Fraction, Fraction], ...]:
    K = r - 4
    L = r + 1
    m = level - 2
    q1, e1m, q2, e2m, e1l, e2lp, e2ll = parameters(r)
    middle_sum = quadratic_hahn_sum(K, L, m, 2)
    lower_sum = quadratic_hahn_sum(K, L, m, 1)
    middle_endpoint = endpoint_hahn(K, L, m, K, 2)
    lower_endpoint = endpoint_hahn(K, L, m, K, 1)
    lower_penultimate = endpoint_hahn(K, L, m, K - 1, 2)
    first = (
        q1 * middle_sum + e1m * middle_endpoint,
        q1 * lower_sum + e1l * lower_endpoint,
    )
    second = (
        q2 * middle_sum + e2m * middle_endpoint,
        q2 * lower_sum
        + e2lp * lower_penultimate
        + e2ll * lower_endpoint,
    )
    return first, second


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("r", type=int)
    parser.add_argument("level", type=int)
    args = parser.parse_args()
    first, second = defect_rows(args.r, args.level)
    determinant = first[0] * second[1] - first[1] * second[0]
    print("first", *first)
    print("second", *second)
    print("determinant", determinant, float(determinant * args.r**8))


if __name__ == "__main__":
    main()
