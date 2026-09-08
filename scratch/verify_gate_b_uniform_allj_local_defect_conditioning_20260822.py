#!/usr/bin/env python3
"""Exact checker for uniform all-j conditioning of the local Gate-B bank."""

from __future__ import annotations

import hashlib
from fractions import Fraction
from math import comb, factorial
from pathlib import Path

from research_gate_b_allj_boundary_averages_20260822 import falling
from research_gate_b_allj_defect_formula_20260822 import (
    defect_rows,
    parameters,
    quadratic_hahn_sum,
)
from research_gate_b_local_atoms_fast_venn_20260822 import local_row
from research_gate_b_local_hahn_distributions_20260822 import local_distribution


H_ODD_ROWS = (
    (27840, 54490, 40322, 14656, 2755, 249, 8),
    (90190, 173845, 142873, 66867, 19526, 3544, 364, 16),
    (126443, 225672, 169743, 68904, 15810, 1924, 96),
    (92750, 143584, 88945, 27343, 4135, 244),
    (39053, 49207, 22901, 4628, 340),
    (9834, 9299, 2846, 280),
    (1467, 912, 136),
    (119, 36),
    (4,),
)

H_EVEN_X_ROWS = (
    (4525360, 10144976, 7324827, 2644354, 551539, 69776, 5301, 223, 4),
    (3125836, 7582719, 5028592, 1569184, 267951, 25825, 1322, 28),
    (852174, 2359307, 1401929, 362939, 47527, 3098, 80),
    (120432, 396813, 202416, 40713, 3632, 120),
    (10423, 38654, 15770, 2191, 100),
    (651, 2084, 606, 44),
    (24, 48, 8),
)

H_ZERO = (1950, 3308, 1977, 485, 40)
H_TWO = (143316, 158710, 67422, 13508, 1245, 40)


def polynomial(coefficients: tuple[int, ...], value: int) -> int:
    answer = 0
    for coefficient in reversed(coefficients):
        answer = answer * value + coefficient
    return answer


def h_odd(m: int, x: int) -> int:
    return sum(polynomial(row, x) * m**power for power, row in enumerate(H_ODD_ROWS))


def h_even(y: int, x: int) -> int:
    return sum(polynomial(row, y) * x**power for power, row in enumerate(H_EVEN_X_ROWS))


def parity_factor(m: int, x: int) -> int:
    if m == 0:
        return (
            2
            * (x + 4) ** 2
            * (2 * x + 7)
            * (2 * x + 9)
            * polynomial(H_ZERO, x)
        )
    if m == 2:
        return (
            4
            * (x + 5)
            * (2 * x + 9)
            * (2 * x + 11)
            * polynomial(H_TWO, x)
        )
    if m % 2:
        return -(m + 1) * (m + 3) * (m + 2 * x + 8) * h_odd(m, x)
    y = m - 4
    return -(y + 6) * (2 * x + y + 11) * (2 * x + y + 13) * h_even(y, x)


def determinant_formula(r: int, level: int) -> Fraction:
    m = level - 2
    x = r - m - 4
    numerator = (r - m) * (r - m + 1) ** 2 * parity_factor(m, x)
    denominator = (
        r**8
        * (2 * r - m)
        * (m + 1)
        * (m + 2)
        * (m + 3)
        * (r - 2)
        * (r - 1) ** 2
        * (r + 1) ** 4
        * (2 * r - m - 1)
        * (2 * r - m + 1)
    )
    return Fraction(numerator, denominator)


def closed_quadratic_sum(K: int, L: int, m: int, excess: int) -> Fraction:
    A = K - m
    D = A + L + 2
    U = Fraction(1, comb(K, m))
    V = Fraction((-1) ** m, comb(L, m))
    moment0 = Fraction(U * (L + 1) + V * (K + 1), D)
    moment1 = Fraction(
        -U * (A + 1) * (L + 1)
        + V * (K + 1) * ((m + 1) * (D + 1) - (K + 2)),
        D * (D + 1),
    )
    moment2 = (
        U
        * (L + 1)
        * (A + 1)
        * (
            Fraction(2 * (A + 2), D * (D + 1) * (D + 2))
            - Fraction(1, D * (D + 1))
        )
        + V
        * (K + 1)
        * (
            Fraction((m + 1) ** 2, D)
            - Fraction((2 * m + 3) * (K + 2), D * (D + 1))
            + Fraction(2 * (K + 2) * (K + 3), D * (D + 1) * (D + 2))
        )
    )
    auxiliary0 = (m + 1) * moment0 - moment1
    auxiliary1 = (m + 1) * moment1 - moment2
    n = K + excess
    choose1 = comb(n + 1, m + 1)
    choose2 = comb(n + 1, m + 2) if m + 2 <= n + 1 else 0
    choose3 = comb(n + 1, m + 3) if m + 3 <= n + 1 else 0
    if excess == 1:
        return (
            auxiliary1 * (choose1 + 2 * choose2 + choose3)
            + auxiliary0 * (choose2 + choose3)
        )
    return (
        auxiliary1 * (choose1 + 2 * choose2 + choose3)
        + auxiliary0 * (-choose1 + choose3)
        + Fraction((K + 3) * falling(K + 2, m), falling(K, m))
    )


def observed_distribution_parameters(r: int):
    dm = 2 * r * factorial(r) * factorial(r + 1)
    K = r - 4
    rows = {
        (shore, start): local_distribution(r, shore, start)
        for shore in (r, r - 1)
        for start in (3, r + 1, r + 2)
    }
    output = []
    for shore in (r, r - 1):
        count = shore - 2
        for start in (r + 1, r + 2):
            values = {
                a: Fraction(
                    rows[(shore, 3)].get((a, count - a), 0)
                    - rows[(shore, start)].get((a, count - a), 0),
                    dm,
                )
                for a in range(K + 1)
            }
            coefficient = values[0] / (r - 3)
            residuals = tuple(
                values[a] - coefficient * (r - 3 - a) * (a + 1)
                for a in range(K + 1)
            )
            if start == r + 1 or shore == r:
                assert all(residuals[a] == 0 for a in range(K))
                output.extend((coefficient, residuals[K]))
            else:
                assert all(residuals[a] == 0 for a in range(K - 1))
                output.extend((coefficient, residuals[K - 1], residuals[K]))
    return tuple(output)


def main() -> None:
    root = Path(__file__).resolve().parent
    expected_hashes = {
        "research_gate_b_allj_defect_formula_20260822.py":
            "10f2c4ca9e77cfb88f646f5fb0631d6e9b2cc9ff32c43b8b6420c4857c13c16e",
        "research_gate_b_local_hahn_distributions_20260822.py":
            "43c7cb80173515cb8b754b0e7c8271dce985f8bab96b6d5ebdf35d2b58dd8423",
        "research_gate_b_local_atoms_fast_venn_20260822.py":
            "ac53061e70687df50e88f068e8feb517291edd9b388392aa298039d1423738fa",
        "research_gate_b_zero_avoidance_local_atom_profiles_20260822.py":
            "04c2a80507a927bfacbb9a166e094b0dcc6b55708c7f3ac24ae7fdc23bcfe765",
        "research_gate_b_allj_boundary_averages_20260822.py":
            "f3a1e3e1cff2d585e20448e077adcc71d8b63918441b5936c7bff2430d31c2df",
        "research_w2_hahn_venn_exact_20260822.py":
            "8b7916edd570e7705b9154f88e66b0922d9d0f3ac05e1c8ed874eaac695c04d4",
    }
    for name, expected in expected_hashes.items():
        assert hashlib.sha256((root / name).read_bytes()).hexdigest() == expected

    for r in range(9, 17):
        q1, e1m, q2, e2m, e1l, e2lp, e2ll = parameters(r)
        assert observed_distribution_parameters(r) == (
            q1,
            e1m,
            q2,
            e2m,
            q1,
            e1l,
            q2,
            e2lp,
            e2ll,
        )

    for K in range(5, 61):
        L = K + 5
        for m in range(K + 1):
            for excess in (1, 2):
                assert quadratic_hahn_sum(K, L, m, excess) == closed_quadratic_sum(
                    K, L, m, excess
                )

    for r in range(9, 151):
        scale = 2 * r * factorial(r) * factorial(r + 1)
        for level in range(2, r - 1):
            first, second = defect_rows(r, level)
            observed = first[0] * second[1] - first[1] * second[0]
            expected = determinant_formula(r, level)
            assert observed == expected
            assert observed
            assert abs(observed) >= Fraction(1, r**24)

            if r <= 14:
                injection_scale = (
                    scale
                    * falling(r - 4, level - 2)
                    * falling(r + 1, level - 2)
                )
                base = local_row(r, level, 3)
                direct = tuple(
                    tuple(
                        Fraction(base[index] - local_row(r, level, start)[index], injection_scale)
                        for index in range(2)
                    )
                    for start in (r + 1, r + 2)
                )
                assert direct == (first, second)

    assert all(value > 0 for row in H_ODD_ROWS for value in row)
    assert all(value > 0 for row in H_EVEN_X_ROWS for value in row)
    assert all(value > 0 for value in H_ZERO + H_TWO)

    print(
        "GATE_B_UNIFORM_ALLJ_LOCAL_DEFECT_CONDITIONING_PASS "
        "helper_hashes=PASS distributions_r=9..16=PASS "
        "quadratic_hahn_closed_form=PASS local_rows_r=9..14=PASS "
        "determinant_r=9..150=PASS parity_positivity=PASS "
        "uniform_lower_bound=PASS"
    )


if __name__ == "__main__":
    main()
