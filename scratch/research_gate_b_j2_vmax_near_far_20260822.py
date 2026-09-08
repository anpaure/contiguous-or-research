#!/usr/bin/env python3
"""Exact near/far defect determinant for bounded local vertex banks."""

from __future__ import annotations

import multiprocessing as mp
import sys
from fractions import Fraction
from math import factorial

sys.path.insert(0, "scratch")

from research_gate_b_targeted_local_bank_20260822 import (
    grouped_puncture_correction_row,
)

R = 0
VERTICES = 0


def correction(shift: int):
    return shift, grouped_puncture_correction_row(R, 2, shift, VERTICES)


def main() -> None:
    global R, VERTICES
    R = int(sys.argv[1])
    VERTICES = int(sys.argv[2])
    b = 2 * R + 1
    shifts = sorted({0, 1, R + 2, R + 3})
    context = mp.get_context("fork")
    with context.Pool(4) as pool:
        rows = dict(pool.map(correction, shifts))
    degree = 2 * R * factorial(R) * factorial(R + 1)
    near = tuple(Fraction(rows[0][i] - rows[1][i], degree) for i in range(2))
    far = tuple(
        Fraction(rows[R + 2][i] - rows[R + 3][i], degree)
        for i in range(2)
    )
    determinant = near[0] * far[1] - near[1] * far[0]
    print(
        "r",
        R,
        "vertices",
        VERTICES,
        "near*r3",
        *(float(value * R**3) for value in near),
        "far*r2",
        *(float(value * R**2) for value in far),
        "det*r6",
        float(determinant * R**6),
        "det*r7",
        float(determinant * R**7),
        "exact",
        determinant,
    )


if __name__ == "__main__":
    main()
