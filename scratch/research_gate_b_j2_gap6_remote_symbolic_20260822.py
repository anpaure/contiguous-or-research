#!/usr/bin/env python3
"""Symbolic near/far determinant through rootless gap defect six."""

from __future__ import annotations

import multiprocessing as mp
import sys
from collections import defaultdict
from fractions import Fraction
from math import factorial

sys.path.insert(0, "scratch")

from research_gate_b_j2_single_remote_edge_cumulant_20260822 import (
    elementary_gap_defect,
    one_remote_edge_sets,
)
from research_gate_b_j2_six_vertex_symbolic_20260822 import (
    add_series,
    factorial_ratio_polynomials,
    interpolate_consecutive,
    multiply_series,
    polynomial_evaluate,
    polynomial_multiply,
    rational_series_at_infinity,
)
from research_gate_b_local_atoms_fast_venn_20260822 import boundary_cell_data
from research_gate_b_targeted_local_bank_20260822 import (
    j2_factor_signature,
    positional_j2_polynomial_sum,
    puncture_j2_factor_groups,
)


def collapsed_rooted(r: int, root_size: int, shift: int):
    answer = defaultdict(int)
    for (large, small), value in puncture_j2_factor_groups(
        r, root_size, shift, 6, rooted_only=True
    ).items():
        constant = 1
        for cell in small:
            constant *= factorial(cell)
        answer[large] += constant * value
    return dict(answer)


def collapsed_remote(r: int, root_size: int, shift: int):
    b = 2 * r + 1
    answer = defaultdict(int)
    for blocker_data in one_remote_edge_sets(r, shift):
        if elementary_gap_defect(r, blocker_data) > 6:
            continue
        if not any(start == 0 for _, start, _ in blocker_data):
            continue
        sizes = tuple(value[0] for value in blocker_data)
        masks = tuple(value[2] for value in blocker_data)
        cell_sizes, _, marks = boundary_cell_data(b, shift, masks)
        large, small = j2_factor_signature(r, cell_sizes, marks)
        constant = 1
        for cell in small:
            constant *= factorial(cell)
        answer[large] += (
            (-1) ** len(blocker_data)
            * constant
            * positional_j2_polynomial_sum(
                r, root_size, sizes, cell_sizes, marks
            )
        )
    return dict(answer)


def combined(r: int, root_size: int, shift: int):
    answer = defaultdict(int)
    for source in (
        collapsed_rooted(r, root_size, shift),
        collapsed_remote(r, root_size, shift),
    ):
        for key, value in source.items():
            answer[key] += value
    return {key: value for key, value in answer.items() if value}


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
        near = difference(combined(r, root_size, 0), combined(r, root_size, 1))
        far = difference(
            combined(r, root_size, r + 2),
            combined(r, root_size, r + 3),
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
    assert determinant.get(6) == Fraction(2, 3)
    assert determinant.get(7) == Fraction(23, 6)
    assert determinant.get(8) == Fraction(-181, 6)
    assert not any(determinant.get(exponent, 0) for exponent in range(6))
    print("keys", len(keys))
    for name, series in (
        ("near_r", row_series[0][0]),
        ("near_l", row_series[1][0]),
        ("far_r", row_series[0][1]),
        ("far_l", row_series[1][1]),
    ):
        print(name, sorted(series.items())[:9])
    print("determinant", sorted(determinant.items())[:10])
    print("GAP6_REMOTE_SYMBOLIC_PASS")


if __name__ == "__main__":
    main()
