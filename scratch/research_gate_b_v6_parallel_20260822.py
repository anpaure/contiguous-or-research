#!/usr/bin/env python3
"""Parallel exact calibration of the six-vertex puncture defect bank."""

from __future__ import annotations

import multiprocessing as mp
import sys
import time
from fractions import Fraction
from math import factorial

sys.path.insert(0, "scratch")


def calculate(r: int):
    from research_gate_b_targeted_local_bank_20260822 import (
        grouped_puncture_rooted_core_row,
    )

    started = time.time()
    degree = 2 * r * factorial(r) * factorial(r + 1)
    corrections = {
        shift: tuple(
            Fraction(value, degree)
            for value in grouped_puncture_rooted_core_row(r, 2, shift, 6)
        )
        for shift in (r, r + 1, r + 2, r + 3)
    }
    left = tuple(
        corrections[r][shore] - corrections[r + 1][shore]
        for shore in range(2)
    )
    right = tuple(
        corrections[r + 2][shore] - corrections[r + 3][shore]
        for shore in range(2)
    )
    determinant = left[0] * right[1] - left[1] * right[0]
    return r, time.time() - started, left, right, determinant


def main() -> None:
    values = [int(value) for value in sys.argv[1:]] or list(range(10, 16))
    context = mp.get_context("fork")
    with context.Pool(min(len(values), 6)) as pool:
        for r, seconds, left, right, determinant in pool.imap_unordered(
            calculate, values
        ):
            print(
                r,
                "seconds",
                round(seconds, 3),
                "left*r2",
                *(float(value * r**2) for value in left),
                "right*r2",
                *(float(value * r**2) for value in right),
                "det*r6",
                float(determinant * r**6),
                "det*r7",
                float(determinant * r**7),
                "left_exact",
                *(str(value) for value in left),
                "right_exact",
                *(str(value) for value in right),
                "exact",
                determinant,
                flush=True,
            )


if __name__ == "__main__":
    main()
