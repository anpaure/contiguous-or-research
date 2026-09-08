#!/usr/bin/env python3
"""Symbolic reconstruction of the dominant j=2 six-vertex defect bank."""

from __future__ import annotations

import multiprocessing as mp
import sys
from collections import defaultdict
from fractions import Fraction
from math import factorial, gcd, lcm

sys.path.insert(0, "scratch")


EXPECTED_SHIFTED_23 = [
    62981083599956614478115107174154240,
    83731019301859283369193624773455872,
    53503167323082065050576460728060416,
    21874508927965046394283771602943488,
    6426381234586609560264944170832256,
    1444365103196196379308996566942592,
    258170481804935360887224705464448,
    37662599276106501292922749610480,
    4566280031383604538889761516544,
    466127777416902336699609774388,
    40438710544492245034672425456,
    3001278408729229165219406704,
    191400833973788705746237666,
    10515008159209256633718591,
    498043778207751522889761,
    20322149467297451253335,
    712577696918492023585,
    21377614697429068690,
    545129461736876970,
    11706023019295518,
    208959527775844,
    3045080777091,
    35300366213,
    313170763,
    1997129,
    8152,
    16,
]


def collapsed_groups(r: int, root_size: int, shift: int) -> dict[tuple[int, int], int]:
    from research_gate_b_targeted_local_bank_20260822 import (
        puncture_j2_factor_groups,
    )

    answer: dict[tuple[int, int], int] = defaultdict(int)
    for (large_offsets, small_cells), polynomial in puncture_j2_factor_groups(
        r, root_size, shift, 6, rooted_only=True
    ).items():
        constant = 1
        for cell in small_cells:
            constant *= factorial(cell)
        answer[large_offsets] += constant * polynomial
    return dict(answer)


def subtract(
    first: dict[tuple[int, int], int], second: dict[tuple[int, int], int]
) -> dict[tuple[int, int], int]:
    answer: dict[tuple[int, int], int] = defaultdict(int)
    for key, value in first.items():
        answer[key] += value
    for key, value in second.items():
        answer[key] -= value
    return {key: value for key, value in answer.items() if value}


def sample(r: int):
    rows = []
    for root_size in (r, r - 1):
        left = subtract(
            collapsed_groups(r, root_size, r),
            collapsed_groups(r, root_size, r + 1),
        )
        right = subtract(
            collapsed_groups(r, root_size, r + 2),
            collapsed_groups(r, root_size, r + 3),
        )
        rows.append((left, right))
    return r, rows


def polynomial_add(first: list[Fraction], second: list[Fraction]) -> list[Fraction]:
    answer = [Fraction(0)] * max(len(first), len(second))
    for index, value in enumerate(first):
        answer[index] += value
    for index, value in enumerate(second):
        answer[index] += value
    while len(answer) > 1 and not answer[-1]:
        answer.pop()
    return answer


def polynomial_multiply(first: list[Fraction], second: list[Fraction]) -> list[Fraction]:
    answer = [Fraction(0)] * (len(first) + len(second) - 1)
    for i, left in enumerate(first):
        for j, right in enumerate(second):
            answer[i + j] += left * right
    return answer


def polynomial_subtract(first: list[Fraction], second: list[Fraction]) -> list[Fraction]:
    return polynomial_add(first, [-value for value in second])


def polynomial_shift(polynomial: list[Fraction], shift: int) -> list[Fraction]:
    """Return coefficients of P(x+shift)."""
    answer = [Fraction(0)]
    power = [Fraction(1)]
    for coefficient in polynomial:
        answer = polynomial_add(
            answer, [coefficient * value for value in power]
        )
        power = polynomial_multiply(power, [Fraction(shift), Fraction(1)])
    return answer


def polynomial_evaluate(polynomial: list[Fraction], value: int) -> Fraction:
    answer = Fraction(0)
    for coefficient in reversed(polynomial):
        answer = answer * value + coefficient
    return answer


def interpolate_consecutive(points: list[tuple[int, int]]) -> list[Fraction]:
    start = points[0][0]
    assert [point for point, _ in points] == list(range(start, start + len(points)))
    differences = [Fraction(value) for _, value in points]
    polynomial = [Fraction(0)]
    falling_basis = [Fraction(1)]
    factorial_value = 1
    for order in range(len(points)):
        if order:
            falling_basis = polynomial_multiply(
                falling_basis, [Fraction(-(start + order - 1)), Fraction(1)]
            )
            factorial_value *= order
        polynomial = polynomial_add(
            polynomial,
            [coefficient * differences[0] / factorial_value for coefficient in falling_basis],
        )
        differences = [
            differences[index + 1] - differences[index]
            for index in range(len(differences) - 1)
        ]
    return polynomial


def factorial_ratio_polynomials(
    offsets: tuple[int, int],
) -> tuple[list[Fraction], list[Fraction]]:
    numerator = [Fraction(1)]
    denominator = [Fraction(0), Fraction(2)]
    for offset, base_offset in zip(offsets, (0, 1)):
        if offset <= base_offset:
            for step in range(offset + 1, base_offset + 1):
                denominator = polynomial_multiply(
                    denominator, [Fraction(step), Fraction(1)]
                )
        else:
            for step in range(base_offset + 1, offset + 1):
                numerator = polynomial_multiply(
                    numerator, [Fraction(step), Fraction(1)]
                )
    return numerator, denominator


def denominator_factor_counts(offsets: tuple[int, int]) -> dict[int, int]:
    counts: dict[int, int] = defaultdict(int)
    counts[0] += 1
    for offset, base_offset in zip(offsets, (0, 1)):
        assert offset <= base_offset
        for step in range(offset + 1, base_offset + 1):
            counts[step] += 1
    return dict(counts)


def factor_count_polynomial(counts: dict[int, int]) -> list[Fraction]:
    answer = [Fraction(1)]
    for shift, multiplicity in sorted(counts.items()):
        for _ in range(multiplicity):
            answer = polynomial_multiply(
                answer, [Fraction(shift), Fraction(1)]
            )
    return answer


def integer_content_normalize(polynomial: list[Fraction]) -> tuple[int, list[int]]:
    common_denominator = 1
    for value in polynomial:
        common_denominator = lcm(common_denominator, value.denominator)
    integers = [int(value * common_denominator) for value in polynomial]
    content = 0
    for value in integers:
        content = gcd(content, abs(value))
    return common_denominator // content, [value // content for value in integers]


def rational_series_at_infinity(
    numerator: list[Fraction], denominator: list[Fraction], maximum_power: int
) -> dict[int, Fraction]:
    numerator_degree = len(numerator) - 1
    denominator_degree = len(denominator) - 1
    shift = denominator_degree - numerator_degree
    top = list(reversed(numerator))
    bottom = list(reversed(denominator))
    quotient = [Fraction(0)] * (maximum_power - shift + 1)
    for degree in range(len(quotient)):
        value = top[degree] if degree < len(top) else Fraction(0)
        for previous in range(degree):
            if degree - previous < len(bottom):
                value -= quotient[previous] * bottom[degree - previous]
        quotient[degree] = value / bottom[0]
    return {
        shift + index: value
        for index, value in enumerate(quotient)
        if value
    }


def add_series(
    first: dict[int, Fraction], second: dict[int, Fraction]
) -> dict[int, Fraction]:
    answer = defaultdict(Fraction)
    for exponent, value in first.items():
        answer[exponent] += value
    for exponent, value in second.items():
        answer[exponent] += value
    return {exponent: value for exponent, value in answer.items() if value}


def multiply_series(
    first: dict[int, Fraction],
    second: dict[int, Fraction],
    maximum_power: int,
) -> dict[int, Fraction]:
    answer = defaultdict(Fraction)
    for first_exponent, first_value in first.items():
        for second_exponent, second_value in second.items():
            exponent = first_exponent + second_exponent
            if exponent <= maximum_power:
                answer[exponent] += first_value * second_value
    return {exponent: value for exponent, value in answer.items() if value}


def main() -> None:
    training = list(range(60, 67))
    validation = [23, 29, 47, 67, 68, 70]
    values = training + validation
    context = mp.get_context("fork")
    with context.Pool(6) as pool:
        samples = dict(pool.map(sample, values))

    polynomials: list[list[dict[tuple[int, int], list[Fraction]]]] = [
        [{}, {}],
        [{}, {}],
    ]
    all_keys = set()
    for r in training:
        for shore in range(2):
            for side in range(2):
                all_keys.update(samples[r][shore][side])

    for shore in range(2):
        for side in range(2):
            for key in sorted(all_keys):
                points = [
                    (r, samples[r][shore][side].get(key, 0))
                    for r in training
                ]
                polynomial = interpolate_consecutive(points)
                assert len(polynomial) <= 7
                polynomials[shore][side][key] = polynomial

    # Validate the reconstructed grouped values, not merely the final sum.
    for r in validation:
        for shore in range(2):
            for side in range(2):
                for key in all_keys | set(samples[r][shore][side]):
                    points = [
                        (value, samples[value][shore][side].get(key, 0))
                        for value in training
                    ]
                    polynomial = interpolate_consecutive(points)
                    assert polynomial_evaluate(polynomial, r) == samples[r][shore][side].get(key, 0)

    row_series: list[list[dict[int, Fraction]]] = [[{}, {}], [{}, {}]]
    for shore in range(2):
        for side in range(2):
            series: dict[int, Fraction] = {}
            for key, polynomial in polynomials[shore][side].items():
                ratio_numerator, ratio_denominator = factorial_ratio_polynomials(key)
                numerator = polynomial_multiply(polynomial, ratio_numerator)
                series = add_series(
                    series,
                    rational_series_at_infinity(
                        numerator, ratio_denominator, 12
                    ),
                )
            row_series[shore][side] = series

    first_product = multiply_series(row_series[0][0], row_series[1][1], 12)
    second_product = multiply_series(row_series[1][0], row_series[0][1], 12)
    determinant_series = add_series(
        first_product,
        {exponent: -value for exponent, value in second_product.items()},
    )

    common_counts: dict[int, int] = defaultdict(int)
    for key in all_keys:
        for shift, multiplicity in denominator_factor_counts(key).items():
            common_counts[shift] = max(common_counts[shift], multiplicity)
    common_denominator_without_two = factor_count_polynomial(dict(common_counts))
    row_numerators: list[list[list[Fraction]]] = [[[], []], [[], []]]
    for shore in range(2):
        for side in range(2):
            numerator = [Fraction(0)]
            for key, polynomial in polynomials[shore][side].items():
                term_counts = denominator_factor_counts(key)
                quotient_counts = {
                    shift: multiplicity - term_counts.get(shift, 0)
                    for shift, multiplicity in common_counts.items()
                    if multiplicity - term_counts.get(shift, 0)
                }
                numerator = polynomial_add(
                    numerator,
                    polynomial_multiply(
                        polynomial, factor_count_polynomial(quotient_counts)
                    ),
                )
            # Every factorial ratio has the same scalar denominator 2.
            row_numerators[shore][side] = numerator

    determinant_numerator = polynomial_subtract(
        polynomial_multiply(row_numerators[0][0], row_numerators[1][1]),
        polynomial_multiply(row_numerators[1][0], row_numerators[0][1]),
    )
    while len(determinant_numerator) > 1 and not determinant_numerator[-1]:
        determinant_numerator.pop()
    scale, primitive_numerator = integer_content_normalize(determinant_numerator)
    shifted_23 = polynomial_shift(
        [Fraction(value) for value in primitive_numerator], 23
    )
    assert dict(common_counts) == {
        -7: 1,
        -6: 1,
        -5: 2,
        -4: 2,
        -3: 2,
        -2: 2,
        -1: 2,
        0: 3,
        1: 1,
    }
    assert scale == 3
    assert len(primitive_numerator) - 1 == 26
    assert primitive_numerator[-1] == 16
    assert all(value > 0 for value in shifted_23)
    assert [int(value) for value in shifted_23] == EXPECTED_SHIFTED_23
    print("keys", len(all_keys))
    for name, series in (
        ("left_r", row_series[0][0]),
        ("left_l", row_series[1][0]),
        ("right_r", row_series[0][1]),
        ("right_l", row_series[1][1]),
    ):
        print(name + "_series", sorted(series.items())[:9])
    print("determinant_series", sorted(determinant_series.items())[:10])
    assert determinant_series.get(6) == Fraction(4, 3)
    assert not any(determinant_series.get(exponent, 0) for exponent in range(6))
    print("limit_r6_det", determinant_series[6])
    print("common_denominator_degree", len(common_denominator_without_two) - 1)
    print("primitive_numerator_degree", len(primitive_numerator) - 1)
    print("primitive_scale_denominator", scale)
    print("primitive_numerator_coefficients_low_to_high", primitive_numerator)
    print("shifted_23_coefficients_low_to_high", [int(value) for value in shifted_23])
    print("shifted_23_all_positive", all(value > 0 for value in shifted_23))
    print("J2_SIX_VERTEX_SYMBOLIC_PASS")


if __name__ == "__main__":
    main()
