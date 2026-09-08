#!/usr/bin/env python3
"""Symbolic near/far j=2 determinant for the local <=6-vertex bank."""

from __future__ import annotations

import multiprocessing as mp
import sys
from collections import defaultdict
from fractions import Fraction
from math import factorial

sys.path.insert(0, "scratch")

from research_gate_b_j2_six_vertex_symbolic_20260822 import (
    add_series,
    denominator_factor_counts,
    factor_count_polynomial,
    factorial_ratio_polynomials,
    integer_content_normalize,
    interpolate_consecutive,
    multiply_series,
    polynomial_add,
    polynomial_evaluate,
    polynomial_multiply,
    polynomial_shift,
    polynomial_subtract,
    rational_series_at_infinity,
)
from research_gate_b_targeted_local_bank_20260822 import (
    puncture_j2_factor_groups,
)


EXPECTED_SHIFTED_23 = [
    4879302165098587130178407895697767116328271872000,
    10418836712359730502268108374962675806477143244800,
    10821723411603219756330719548450827588423936245760,
    7284671057128420424450002380296060215147487035392,
    3572533175454373094057917812636180502733835629568,
    1360406211079774857416293749990375318508400891904,
    418638307308295855469400195468462471592018927872,
    106984746515332412820012510670520362656122966016,
    23155107302993587077489946141411571589906898944,
    4307248884501709536205867059318761818833509536,
    696454015218466098581245760020452234677292880,
    98757737134945312538646761464789878634110896,
    12367575620817162417747564889237481548731364,
    1375503654956603018031275156691076131786850,
    136469545458289462205785902317205620834716,
    12120795218380225270348028548451500649040,
    966331545077770682754310262301522609550,
    69294261365458380903851565739483250437,
    4475585443413186427689350381472343950,
    260578553411308374844647229702017735,
    13679789684461779556100247435748920,
    647369901151670196992941959915478,
    27593020498217064073661625953124,
    1057816441529317991807422874828,
    36400333471714234440156816760,
    1121249085255499694925044238,
    30808598953171545690748928,
    751757426126284259092386,
    16198929662894343538736,
    306087047607228353730,
    5026925281795765752,
    70948510689294668,
    847962843502330,
    8415287035765,
    67480822562,
    420101503,
    1905076,
    5598,
    8,
]


def collapsed(r: int, root_size: int, shift: int):
    answer = defaultdict(int)
    for (large, small), value in puncture_j2_factor_groups(
        r, root_size, shift, 6, rooted_only=False
    ).items():
        constant = 1
        for cell in small:
            constant *= factorial(cell)
        answer[large] += constant * value
    return dict(answer)


def difference(first, second):
    answer = defaultdict(int)
    for key, value in first.items():
        answer[key] += value
    for key, value in second.items():
        answer[key] -= value
    return {key: value for key, value in answer.items() if value}


def sample(r: int):
    rows = []
    for root_size in (r, r - 1):
        near = difference(collapsed(r, root_size, 0), collapsed(r, root_size, 1))
        far = difference(
            collapsed(r, root_size, r + 2),
            collapsed(r, root_size, r + 3),
        )
        rows.append((near, far))
    return r, rows


def main() -> None:
    training = list(range(60, 67))
    validation = [23, 29, 47, 67, 70]
    context = mp.get_context("fork")
    with context.Pool(6) as pool:
        samples = dict(pool.map(sample, training + validation))
    keys = set()
    for r in training:
        for shore in range(2):
            for side in range(2):
                keys.update(samples[r][shore][side])
    polynomials = [[{}, {}], [{}, {}]]
    for shore in range(2):
        for side in range(2):
            for key in keys:
                points = [
                    (r, samples[r][shore][side].get(key, 0))
                    for r in training
                ]
                polynomial = interpolate_consecutive(points)
                assert len(polynomial) <= 7
                polynomials[shore][side][key] = polynomial
                for r in validation:
                    assert polynomial_evaluate(polynomial, r) == samples[r][shore][side].get(
                        key, 0
                    )
    row_series = [[{}, {}], [{}, {}]]
    for shore in range(2):
        for side in range(2):
            series = {}
            for key, polynomial in polynomials[shore][side].items():
                ratio_numerator, ratio_denominator = factorial_ratio_polynomials(key)
                series = add_series(
                    series,
                    rational_series_at_infinity(
                        polynomial_multiply(polynomial, ratio_numerator),
                        ratio_denominator,
                        12,
                    ),
                )
            row_series[shore][side] = series
    determinant = add_series(
        multiply_series(row_series[0][0], row_series[1][1], 12),
        {
            exponent: -value
            for exponent, value in multiply_series(
                row_series[1][0], row_series[0][1], 12
            ).items()
        },
    )
    common_counts = defaultdict(int)
    for key in keys:
        for shift, multiplicity in denominator_factor_counts(key).items():
            common_counts[shift] = max(common_counts[shift], multiplicity)
    row_numerators = [[[], []], [[], []]]
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
            row_numerators[shore][side] = numerator
    determinant_numerator = polynomial_subtract(
        polynomial_multiply(row_numerators[0][0], row_numerators[1][1]),
        polynomial_multiply(row_numerators[1][0], row_numerators[0][1]),
    )
    while len(determinant_numerator) > 1 and not determinant_numerator[-1]:
        determinant_numerator.pop()
    scale, primitive = integer_content_normalize(determinant_numerator)
    shifted = polynomial_shift([Fraction(value) for value in primitive], 23)
    assert determinant.get(6) == Fraction(2, 3)
    assert determinant.get(7) == Fraction(23, 6)
    assert not any(determinant.get(exponent, 0) for exponent in range(6))
    assert dict(common_counts) == {
        -10: 1,
        -9: 1,
        -8: 2,
        -7: 2,
        -6: 2,
        -5: 2,
        -4: 2,
        -3: 2,
        -2: 2,
        -1: 2,
        0: 3,
        1: 1,
    }
    assert scale == 3
    assert len(primitive) - 1 == 38
    assert primitive[-1] == 8
    assert [int(value) for value in shifted] == EXPECTED_SHIFTED_23
    assert all(value > 0 for value in shifted)
    print("keys", len(keys))
    for name, series in (
        ("near_r", row_series[0][0]),
        ("near_l", row_series[1][0]),
        ("far_r", row_series[0][1]),
        ("far_l", row_series[1][1]),
    ):
        print(name, sorted(series.items())[:9])
    print("determinant", sorted(determinant.items())[:10])
    print("common_counts", sorted(common_counts.items()))
    print("scale", scale, "primitive_degree", len(primitive) - 1)
    print("primitive", primitive)
    print("shifted_23", [int(value) for value in shifted])
    print("shifted_all_positive", all(value > 0 for value in shifted))
    print("NEAR_FAR_LOCAL_SYMBOLIC_PASS")


if __name__ == "__main__":
    main()
