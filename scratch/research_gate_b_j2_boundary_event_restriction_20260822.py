#!/usr/bin/env python3
"""Exact j=2 restriction to unique-shallow-window boundary endpoint states."""

from __future__ import annotations

import argparse
from fractions import Fraction
from math import factorial
from collections import Counter

import numpy as np

from research_w2_hahn_venn_exact_20260822 import (
    coefficient_vectors,
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


def rational_rank(matrix: list[list[int]]) -> int:
    work = [[Fraction(value) for value in row] for row in matrix]
    rows = len(work)
    columns = len(work[0]) if rows else 0
    rank = 0
    for column in range(columns):
        pivot = next((i for i in range(rank, rows) if work[i][column]), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        value = work[rank][column]
        work[rank] = [entry / value for entry in work[rank]]
        for row in range(rows):
            if row == rank:
                continue
            multiple = work[row][column]
            if multiple:
                work[row] = [
                    work[row][j] - multiple * work[rank][j]
                    for j in range(columns)
                ]
        rank += 1
        if rank == rows:
            break
    return rank


def run(r: int, show: bool) -> None:
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
    constraints = [row[:4] for row in values]
    assert all(row[4] == 1 for row in values)
    rank = rational_rank(constraints)
    augmented_rank = rational_rank([row[:4] + [1] for row in values])

    array = np.array(constraints, dtype=float)
    constant = np.ones(b)
    projection, *_ = np.linalg.lstsq(array, constant, rcond=None)
    residual = constant - array @ projection
    relative_residual = float(residual @ residual / b)
    print(
        f"r={r} b={b} rank={rank} augmented_rank={augmented_rank} "
        f"mean_square_residual={relative_residual:.12g}"
    )
    profile = [(row[2], row[3]) for row in values]
    baseline, multiplicity = Counter(profile).most_common(1)[0]
    deviations = [
        (t, pair[0] - baseline[0], pair[1] - baseline[1])
        for t, pair in enumerate(profile)
        if pair != baseline
    ]
    wedges = []
    for i, left in enumerate(deviations):
        for right in deviations[i + 1 :]:
            wedge = left[1] * right[2] - left[2] * right[1]
            wedges.append((abs(wedge), left, right, wedge))
    wedges.sort(reverse=True)
    print(
        f"baseline_multiplicity={multiplicity} baseline={baseline} "
        f"exceptions={len(deviations)}"
    )
    for _, left, right, wedge in wedges[:3]:
        print("deviation_wedge", left, right, wedge)
    if show:
        degree_scale = 2 * r * factorial(r) * factorial(r + 1)
        for t, row in enumerate(values):
            print(
                "state",
                t,
                row[0],
                row[1],
                Fraction(row[2], degree_scale),
                Fraction(row[3], degree_scale),
                row[4],
            )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("r", type=int)
    parser.add_argument("--show", action="store_true")
    args = parser.parse_args()
    run(args.r, args.show)


if __name__ == "__main__":
    main()
