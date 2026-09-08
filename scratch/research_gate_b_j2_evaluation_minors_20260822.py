#!/usr/bin/env python3
"""Search structured evaluation minors for the Gate-B j=2 difference Gram."""

from __future__ import annotations

import argparse
from fractions import Fraction
from itertools import permutations
from math import comb, prod
from math import gcd

import numpy as np

from research_gate_b_cyclic_difference_four_columns_20260822 import (
    determinant,
    rotate_mask,
    shifted_coefficients,
)
from research_w2_hahn_venn_exact_20260822 import (
    coefficient_vectors,
    gram_entry,
    superset_sums,
)


def harmonic_value(pair_sums: list[int], row: tuple[int, int, int, int]) -> int:
    a, b, c, d = row
    return (
        pair_sums[(1 << a) | (1 << c)]
        - pair_sums[(1 << a) | (1 << d)]
        - pair_sums[(1 << b) | (1 << c)]
        + pair_sums[(1 << b) | (1 << d)]
    )


def greedy_rows(values: np.ndarray) -> list[int]:
    residual = values.copy()
    selected: list[int] = []
    basis: list[np.ndarray] = []
    for _ in range(values.shape[1]):
        norms = np.einsum("ij,ij->i", residual, residual)
        index = int(np.argmax(norms))
        selected.append(index)
        vector = residual[index]
        vector = vector / np.linalg.norm(vector)
        basis.append(vector)
        residual -= np.outer(residual @ vector, vector)
    return selected


def run(r: int) -> None:
    b, masks, coefficients = coefficient_vectors(r)
    metadata = (
        (r, "c_m"),
        (r - 1, "c_l"),
        (r, "w_m"),
        (r - 1, "w_l"),
    )
    transforms: dict[str, list[int]] = {}
    difference_coefficients: dict[str, list[int]] = {}
    scales = []
    for size, name in metadata:
        shifted = shifted_coefficients(b, masks[size], coefficients[name])
        difference = [
            old - new for old, new in zip(coefficients[name], shifted)
        ]
        difference_coefficients[name] = difference
        transforms[name] = superset_sums(b, masks[size], difference)
        kappa = Fraction(4 * comb(b - 4, size - 2), comb(b, size))
        scales.append(
            float(kappa) ** 0.5
            * sum(abs(value) for value in coefficients[name])
        )

    rows = list(permutations(range(b), 4))
    integer_values = np.array(
        [
            [harmonic_value(transforms[name], row) for _, name in metadata]
            for row in rows
        ],
        dtype=object,
    )
    scaled_values = np.array(integer_values, dtype=float) / np.array(scales)
    column_gcds = []
    column_heights = []
    for column in range(4):
        values = [abs(int(row[column])) for row in integer_values]
        column_gcds.append(gcd(*values))
        column_heights.append(max(values))
    selected = greedy_rows(scaled_values)
    selected_rows = [rows[index] for index in selected]
    selected_matrix = [
        [int(value) for value in integer_values[index]] for index in selected
    ]
    selected_determinant = determinant(
        [[Fraction(value) for value in row] for row in selected_matrix]
    )

    # Check that averaging evaluations agrees with the exact Hahn Gram.
    omega = len(rows)
    for left in range(4):
        for right in range(4):
            direct = Fraction(
                sum(
                    int(row[left]) * int(row[right])
                    for row in integer_values
                ),
                omega,
            )
            exact = gram_entry(
                b,
                metadata[left][0],
                metadata[right][0],
                2,
                transforms[metadata[left][1]],
                transforms[metadata[right][1]],
            )
            assert direct == exact

    print(f"r={r} omega={omega}")
    print("gcds", *column_gcds)
    print("heights_over_gcd", *(h // g for h, g in zip(column_heights, column_gcds)))
    for row, matrix_row in zip(selected_rows, selected_matrix):
        print("row", row, *matrix_row)
    print("det", selected_determinant)
    print(
        "normalized_minor_square",
        float(selected_determinant**2)
        / (omega**4 * prod(scale * scale for scale in scales)),
    )

    fixed = (0, r - 1, r + 2, 2 * r)
    fixed_index = rows.index(fixed)
    fixed_values = [int(value) for value in integer_values[fixed_index]]
    assert fixed_values[0] == fixed_values[1] == 0
    candidates = []
    for index, row in enumerate(rows):
        values = [int(value) for value in integer_values[index]]
        if row[0] != 0 or values[0] or values[1]:
            continue
        wedge = values[2] * fixed_values[3] - values[3] * fixed_values[2]
        candidates.append((abs(wedge), row, values, wedge))
    candidates.sort(reverse=True)
    print("fixed_zero", fixed, *fixed_values)
    templates = [
        (0, r // 2, 2 * r, r + 1),
        (0, (3 * r) // 2, 2 * r, r),
        (0, 2 * r - 3, 2 * r, r),
    ]
    for template in templates:
        if len(set(template)) < 4:
            continue
        template_values = [
            int(value) for value in integer_values[rows.index(template)]
        ]
        wedge = (
            template_values[2] * fixed_values[3]
            - template_values[3] * fixed_values[2]
        )
        print("zero_template", template, *template_values, "wedge", wedge)
    for _, row, values, wedge in candidates[:8]:
        print("zero_candidate", row, *values, "wedge", wedge)
    opposite = [
        item for item in candidates if item[2][2] * item[2][3] <= 0
    ]
    for _, row, values, wedge in opposite[:4]:
        print("opposite_candidate", row, *values, "wedge", wedge)
    zero_one = [
        item for item in candidates if item[2][2] == 0 or item[2][3] == 0
    ]
    for _, row, values, wedge in zero_one[:4]:
        print("coordinate_zero_candidate", row, *values, "wedge", wedge)
    adjacent = [
        item
        for item in candidates
        if (item[1][1] - item[1][0]) % b in (1, b - 1)
        and (item[1][3] - item[1][2]) % b in (1, b - 1)
    ]
    for _, row, values, wedge in adjacent[:8]:
        print("adjacent_candidate", row, *values, "wedge", wedge)

    central_candidates = []
    for index, row in enumerate(rows):
        if row[0] != 0:
            continue
        values = [int(value) for value in integer_values[index]]
        central_candidates.append((row, values))
    for left_row, left_values in central_candidates:
        for right_row, right_values in central_candidates:
            wedge = (
                left_values[0] * right_values[1]
                - left_values[1] * right_values[0]
            )
            if abs(wedge) >= 2:
                print(
                    "central_simple",
                    left_row,
                    *left_values[:2],
                    right_row,
                    *right_values[:2],
                    "wedge",
                    wedge,
                )
                return


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("r", type=int)
    args = parser.parse_args()
    run(args.r)


if __name__ == "__main__":
    main()
