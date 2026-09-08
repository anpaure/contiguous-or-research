#!/usr/bin/env python3
"""Exact checks for the four-column cyclic and j=2 boundary reduction."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from math import factorial
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from research_w2_hahn_venn_exact_20260822 import (  # noqa: E402
    cells_for_pair,
    coefficient_vectors,
    interval_mask,
    superset_sums,
)
from research_gate_b_j2_structured_values_fast_20260822 import (  # noqa: E402
    harmonic_pair_degree_sum,
)


P0 = (
    Fraction(-176, 3), Fraction(-98, 3), Fraction(183), Fraction(-90),
    Fraction(18), Fraction(-4), Fraction(-4, 3), Fraction(2, 3),
)
P1 = (
    Fraction(-8, 3), Fraction(-386, 3), Fraction(229), Fraction(-89),
    Fraction(27), Fraction(-8), Fraction(-4, 3), Fraction(2, 3),
)
P2 = (
    Fraction(-106), Fraction(189), Fraction(-218, 3), Fraction(16, 3),
    Fraction(0), Fraction(-4, 3), Fraction(2, 3),
)
P3 = (
    Fraction(188), Fraction(-66), Fraction(13, 6), Fraction(-8, 3),
    Fraction(-2, 3), Fraction(2, 3),
)
N_POLYNOMIAL = tuple(
    Fraction(value, 6)
    for value in (
        64480, -131368, 58176, 19768, -10495, -6937,
        5092, -1210, -28, 138, -54, 8,
    )
)
SIX_N_SHIFTED = (
    4249152, 14751576, 22656960, 20632488, 12471117, 5263911,
    1582220, 338502, 50540, 5018, 298, 8,
)


def harmonic_value(pair_sums: list[int], row: tuple[int, int, int, int]) -> int:
    a, b, c, d = row
    return (
        pair_sums[(1 << a) | (1 << c)]
        - pair_sums[(1 << a) | (1 << d)]
        - pair_sums[(1 << b) | (1 << c)]
        + pair_sums[(1 << b) | (1 << d)]
    )


def rank(matrix: list[list[int]]) -> int:
    work = [[Fraction(value) for value in row] for row in matrix]
    row_count = len(work)
    column_count = len(work[0])
    answer = 0
    for column in range(column_count):
        pivot = next(
            (row for row in range(answer, row_count) if work[row][column]),
            None,
        )
        if pivot is None:
            continue
        work[answer], work[pivot] = work[pivot], work[answer]
        value = work[answer][column]
        work[answer] = [entry / value for entry in work[answer]]
        for row in range(row_count):
            if row == answer:
                continue
            multiple = work[row][column]
            if multiple:
                work[row] = [
                    work[row][j] - multiple * work[answer][j]
                    for j in range(column_count)
                ]
        answer += 1
    return answer


def exact_rho(profile: list[tuple[int, int]]) -> Fraction:
    g00 = sum(a * a for a, _ in profile)
    g01 = sum(a * b for a, b in profile)
    g11 = sum(b * b for _, b in profile)
    h0 = sum(a for a, _ in profile)
    h1 = sum(b for _, b in profile)
    determinant = g00 * g11 - g01 * g01
    projection = Fraction(
        g11 * h0 * h0 - 2 * g01 * h0 * h1 + g00 * h1 * h1,
        determinant,
    )
    return (Fraction(len(profile)) - projection) / len(profile)


def polynomial_value(coefficients, value: int) -> Fraction:
    answer = Fraction()
    for coefficient in reversed(coefficients):
        answer = answer * value + coefficient
    return answer


def polynomial_multiply(left, right):
    answer = [Fraction()] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            answer[i + j] += x * y
    return tuple(answer)


def polynomial_subtract(left, right):
    answer = [Fraction()] * max(len(left), len(right))
    for i in range(len(answer)):
        answer[i] = (
            left[i] if i < len(left) else Fraction()
        ) - (
            right[i] if i < len(right) else Fraction()
        )
    while len(answer) > 1 and not answer[-1]:
        answer.pop()
    return tuple(answer)


def polynomial_shift(coefficients, amount: int):
    from math import comb

    answer = [Fraction()] * len(coefficients)
    for degree, coefficient in enumerate(coefficients):
        for new_degree in range(degree + 1):
            answer[new_degree] += (
                coefficient
                * comb(degree, new_degree)
                * amount ** (degree - new_degree)
            )
    return tuple(answer)


def local_phi(r: int, root_size: int, missing_size: int,
              other_size: int, other_start: int, t: int) -> int:
    b = 2 * r + 1
    k = r - 2
    all_mask = (1 << b) - 1
    points = (t, (t - 1) % b, (t + k - 1) % b, (t + k) % b)
    missing = interval_mask(b, 0, missing_size)
    other = interval_mask(b, other_start % b, other_size)
    return harmonic_pair_degree_sum(
        b,
        root_size,
        missing_size,
        other_size,
        cells_for_pair(all_mask, missing, other),
        points,
    )


def local_deviation(r: int, root_size: int, t: int) -> int:
    b = 2 * r + 1
    k = r - 2
    if t == 0:
        specifications = [
            (missing_size, other_size, other_start)
            for missing_size in (r, r - 1)
            for other_size, other_start in (
                (r, k), (r, b - 2), (r - 1, k), (r - 1, b - 1)
            )
        ]
    elif t == 1:
        specifications = [
            (r - 1, r, 1),
            (r - 1, r, r + 2),
            (r - 1, r - 1, 1),
            (r - 1, r - 1, r + 3),
        ]
    else:
        raise ValueError("only the two certificate states are required")
    return -sum(
        local_phi(r, root_size, missing_size, other_size, other_start, t)
        for missing_size, other_size, other_start in specifications
    )


def direct_interval_value(
    b: int, size: int, points: tuple[int, int, int, int], retained: bool
) -> int:
    starts = range(1, b) if retained else range(b)
    total = 0
    for start in starts:
        interval = {(start + offset) % b for offset in range(size)}
        a, c, d, e = points
        total += (int(a in interval) - int(c in interval)) * (
            int(d in interval) - int(e in interval)
        )
    return total


def verify_symbolic_boundary() -> None:
    for r in range(4, 101):
        b = 2 * r + 1
        k = r - 2
        for t in range(b):
            state = (t, (t - 1) % b, (t + k - 1) % b, (t + k) % b)
            assert direct_interval_value(b, k, state, False) == 1
            assert direct_interval_value(b, r, state, True) == 0
            assert direct_interval_value(b, r - 1, state, True) == 0


def verify_finite_hahn() -> None:
    expected_rho = {
        4: (0.0569, 0.0571),
        5: (0.0550, 0.0552),
        6: (0.0537, 0.0539),
        7: (0.0519, 0.0521),
        8: (0.0497, 0.0500),
        9: (0.0474, 0.0477),
    }
    for r in range(4, 10):
        b = 2 * r + 1
        k = r - 2
        _, masks, coefficients = coefficient_vectors(r)
        metadata = (
            (r, "c_m"),
            (r - 1, "c_l"),
            (r, "w_m"),
            (r - 1, "w_l"),
            (k, "q"),
        )
        transforms = {
            name: superset_sums(b, masks[size], coefficients[name])
            for size, name in metadata
        }
        states = [
            (t, (t - 1) % b, (t + k - 1) % b, (t + k) % b)
            for t in range(b)
        ]
        values = [
            [harmonic_value(transforms[name], state) for _, name in metadata]
            for state in states
        ]
        assert all(row[0] == row[1] == 0 and row[4] == 1 for row in values)
        profile = [(row[2], row[3]) for row in values]
        assert rank([list(row) for row in profile]) == 2
        assert rank([[a, b_value, 1] for a, b_value in profile]) == 3
        common, multiplicity = Counter(profile).most_common(1)[0]
        assert multiplicity == b - 6
        if r >= 5:
            deviations = [
                (profile[t][0] - common[0], profile[t][1] - common[1])
                for t in range(3)
            ]
            assert deviations[0] == (
                deviations[1][0] + deviations[2][0],
                deviations[1][1] + deviations[2][1],
            )
        rho = exact_rho(profile)
        lower, upper = expected_rho[r]
        assert lower < float(rho) < upper
        u0, u1, u3 = profile[0], profile[1], profile[3]
        determinant = (
            (u0[0] - u3[0]) * (u1[1] - u3[1])
            - (u0[1] - u3[1]) * (u1[0] - u3[0])
        )
        assert determinant > 0
        degree_scale = 2 * r * factorial(r) * factorial(r + 1)
        scaled = Fraction(determinant * r**4, degree_scale**2)
        if r >= 7:
            assert scaled > Fraction(3, 2)


def verify_local_formulas() -> None:
    # First verify the polynomial determinant identity symbolically.
    derived_numerator = polynomial_subtract(
        polynomial_multiply(polynomial_multiply(P0, P3), (-1, 1)),
        polynomial_multiply(P1, P2),
    )
    assert derived_numerator == N_POLYNOMIAL
    assert tuple(6 * value for value in polynomial_shift(N_POLYNOMIAL, 4)) == (
        tuple(Fraction(value) for value in SIX_N_SHIFTED)
    )
    assert all(value > 0 for value in SIX_N_SHIFTED)

    # Replay the independent local Venn aggregation well beyond the data
    # used when the formulas were first guessed.
    tested = list(range(5, 36)) + [40, 50]
    for r in tested:
        degree_scale = 2 * r * factorial(r) * factorial(r + 1)
        q0 = r**3 * (r + 1) * (r - 1) ** 2 * (r - 2) ** 2
        q2 = r**3 * (r + 1) * (r - 1) ** 2 * (r - 2)
        q3 = r**3 * (r + 1) * (r - 1) * (r - 2)
        actual = (
            Fraction(local_deviation(r, r, 0), degree_scale),
            Fraction(local_deviation(r, r - 1, 0), degree_scale),
            Fraction(local_deviation(r, r, 1), degree_scale),
            Fraction(local_deviation(r, r - 1, 1), degree_scale),
        )
        expected = (
            polynomial_value(P0, r) / q0,
            polynomial_value(P1, r) / q0,
            polynomial_value(P2, r) / q2,
            polynomial_value(P3, r) / q3,
        )
        assert actual == expected
        determinant = actual[0] * actual[3] - actual[1] * actual[2]
        denominator = r**6 * (r + 1) ** 2 * (r - 1) ** 4 * (r - 2) ** 3
        assert determinant == polynomial_value(N_POLYNOMIAL, r) / denominator
        assert determinant >= Fraction(1, 14000 * r**4)


def main() -> None:
    verify_symbolic_boundary()
    verify_finite_hahn()
    verify_local_formulas()
    # The proof of Theorem 1.1 is algebraic.  Avoid pretending that a finite
    # numerical loop proves it; the exact boundary and Hahn claims are what
    # this checker certifies.
    print(
        "GATE_B_FOUR_COLUMN_CYCLIC_J2_BOUNDARY_PASS "
        "symbolic_boundary_r=4..100 exact_Hahn_r=4..9 "
        "restricted_rank=2 augmented_rank=3 six_exceptions=PASS "
        "local_formulas_r=5..35,40,50 determinant_bound=PASS"
    )


if __name__ == "__main__":
    main()
