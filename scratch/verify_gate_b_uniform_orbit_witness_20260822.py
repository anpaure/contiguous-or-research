#!/usr/bin/env python3
"""Exact audit for the uniform Gate-B shallow-orbit witness bound."""

from __future__ import annotations

from fractions import Fraction
from math import comb, factorial

from research_w2_hahn_venn_exact_20260822 import orbit_factor


def falling(n: int, j: int) -> int:
    if j < 0 or j > n:
        return 0
    return factorial(n) // factorial(n - j)


def h_value(interval: set[int], pairs: tuple[tuple[int, int], ...]) -> int:
    answer = 1
    for positive, negative in pairs:
        factor = int(positive in interval) - int(negative in interval)
        if factor == 0:
            return 0
        answer *= factor
    return answer


def canonical_witness(r: int, j: int) -> tuple[tuple[int, int], ...]:
    b = 2 * r + 1
    k = r - 2
    pairs = [(0, b - 1), (k - 1, k)]
    pairs.extend((i, k + i) for i in range(1, j - 1))
    return tuple(pairs)


def audit_witness_geometry() -> None:
    for r in range(4, 41):
        b = 2 * r + 1
        k = r - 2
        for j in range(2, k + 1):
            pairs = canonical_witness(r, j)
            values = []
            for start in range(b):
                interval = {(start + offset) % b for offset in range(k)}
                values.append(h_value(interval, pairs))
            assert values[0] in (-1, 1)
            assert all(value == 0 for value in values[1:])
            assert sum(values) ** 2 == 1


def audit_exact_factors() -> None:
    for r in range(4, 81):
        b = 2 * r + 1
        k = r - 2
        n = comb(b, k)
        for j in range(2, k + 1):
            denominator = falling(b, 2 * j)
            kappa = Fraction(
                (1 << j) * falling(k, j) * falling(b - k, j),
                denominator,
            )
            event = Fraction(
                (1 << j)
                * falling(k - 2, j - 2)
                * falling(b - k - 2, j - 2),
                denominator,
            )
            witness_ratio = Fraction(
                1, k * (k - 1) * (b - k) * (b - k - 1)
            )
            assert event / kappa == witness_ratio

            relative_theta = orbit_factor(r, j)
            f_value = relative_theta * b * b / n
            assert f_value >= witness_ratio
            assert relative_theta >= Fraction(n, 36 * r**6)


if __name__ == "__main__":
    audit_witness_geometry()
    audit_exact_factors()
    print("GATE_B_UNIFORM_ORBIT_WITNESS_PASS r<=80 geometry_r<=40")
