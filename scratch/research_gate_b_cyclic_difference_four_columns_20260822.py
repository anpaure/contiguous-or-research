#!/usr/bin/env python3
"""Research the four-column cyclic-difference coercivity bypass for Gate B.

This reuses the exact Hahn--Venn coefficient construction.  It compares the
Gram matrix of the first cyclic differences of

    c_r, c_{r-1}, W_{2,r}, W_{2,r-1}

with the diagonal matrix of the original column norms, module by module.
All Gram entries are exact rationals; floating point is used only to report
the generalized eigenvalues.
"""

from __future__ import annotations

import argparse
from fractions import Fraction

import numpy as np
from math import comb

from research_w2_hahn_venn_exact_20260822 import (
    coefficient_vectors,
    gram_entry,
    superset_sums,
)


def rotate_mask(mask: int, b: int, amount: int = 1) -> int:
    amount %= b
    all_mask = (1 << b) - 1
    return ((mask << amount) | (mask >> (b - amount))) & all_mask


def shifted_coefficients(
    b: int, masks: list[int], values: list[int], amount: int = 1
) -> list[int]:
    """Coefficient vector whose harmonic lift is the right translate Tf."""
    table = dict(zip(masks, values))
    return [table[rotate_mask(mask, b, -amount)] for mask in masks]


def exact_gram(
    b: int,
    level: int,
    metadata: tuple[tuple[int, str], ...],
    transforms: dict[str, list[int]],
) -> list[list[Fraction]]:
    n = len(metadata)
    answer = [[Fraction() for _ in range(n)] for _ in range(n)]
    for row, (left_size, left_name) in enumerate(metadata):
        for column in range(row, n):
            right_size, right_name = metadata[column]
            value = gram_entry(
                b,
                left_size,
                right_size,
                level,
                transforms[left_name],
                transforms[right_name],
            )
            answer[row][column] = value
            answer[column][row] = value
    return answer


def determinant(matrix: list[list[Fraction]]) -> Fraction:
    work = [row[:] for row in matrix]
    answer = Fraction(1)
    for column in range(len(work)):
        pivot = next(
            (row for row in range(column, len(work)) if work[row][column]),
            None,
        )
        if pivot is None:
            return Fraction()
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            answer = -answer
        value = work[column][column]
        answer *= value
        for row in range(column + 1, len(work)):
            multiple = work[row][column] / value
            for entry in range(column + 1, len(work)):
                work[row][entry] -= multiple * work[column][entry]
    return answer


def run(r: int, shifts: list[int], show_matrix: bool) -> None:
    b, masks, coefficients = coefficient_vectors(r)
    metadata = (
        (r, "c_m"),
        (r - 1, "c_l"),
        (r, "w_m"),
        (r - 1, "w_l"),
    )

    all_coefficients = dict(coefficients)
    transforms = {
        name: superset_sums(b, masks[size], all_coefficients[name])
        for size, name in metadata
    }
    current_grams = {
        level: exact_gram(b, level, metadata, transforms)
        for level in range(2, r - 1)
    }
    for shift in shifts:
        for size, name in metadata:
            shifted = shifted_coefficients(
                b, masks[size], coefficients[name], shift
            )
            all_coefficients[f"d_{name}"] = [
                old - new for old, new in zip(coefficients[name], shifted)
            ]
        difference_transforms = {
            f"d_{name}": superset_sums(
                b, masks[size], all_coefficients[f"d_{name}"]
            )
            for size, name in metadata
        }
        for level in range(2, r - 1):
            difference_metadata = tuple(
                (size, f"d_{name}") for size, name in metadata
            )
            difference = exact_gram(
                b, level, difference_metadata, difference_transforms
            )
            current_gram = current_grams[level]
            normalized = np.array(
                [
                    [
                        float(difference[i][j])
                        / float(
                            (current_gram[i][i] * current_gram[j][j])
                            ** Fraction(1, 2)
                        )
                        for j in range(4)
                    ]
                    for i in range(4)
                ]
            )
            eigenvalues = np.linalg.eigvalsh(normalized)
            l1_scales = []
            for size, name in metadata:
                kappa = Fraction(
                    (1 << level) * comb(b - 2 * level, size - level),
                    comb(b, size),
                )
                l1_scales.append(
                    float(kappa) ** 0.5
                    * sum(abs(value) for value in coefficients[name])
                )
            l1_normalized = np.array(
                [
                    [
                        float(difference[i][j])
                        / (l1_scales[i] * l1_scales[j])
                        for j in range(4)
                    ]
                    for i in range(4)
                ]
            )
            l1_eigenvalues = np.linalg.eigvalsh(l1_normalized)
            normalized_determinant = determinant(difference)
            for index in range(4):
                normalized_determinant /= current_gram[index][index]
            print(
                f"r={r} shift={shift} j={level} "
                f"detD={float(normalized_determinant):.12g} eig="
                + ",".join(f"{value:.12g}" for value in eigenvalues)
                + " l1eig="
                + ",".join(f"{value:.12g}" for value in l1_eigenvalues)
            )
            if show_matrix:
                if level == 2:
                    print(
                        "det_fraction",
                        normalized_determinant.numerator,
                        normalized_determinant.denominator,
                    )
                for row in normalized:
                    print("matrix", *(f"{value:.12g}" for value in row))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("r", type=int)
    parser.add_argument("--all-shifts", action="store_true")
    parser.add_argument("--show-matrix", action="store_true")
    args = parser.parse_args()
    if args.r < 4:
        raise SystemExit("r must be at least four")
    shifts = list(range(1, 2 * args.r + 1)) if args.all_shifts else [1]
    run(args.r, shifts, args.show_matrix)


if __name__ == "__main__":
    main()
