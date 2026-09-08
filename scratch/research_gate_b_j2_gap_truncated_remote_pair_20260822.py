#!/usr/bin/env python3
"""Near/far determinant after a gap-truncated single-rootless-edge cumulant."""

from __future__ import annotations

import multiprocessing as mp
import sys
from fractions import Fraction
from math import factorial

sys.path.insert(0, "scratch")

from research_gate_b_j2_single_remote_edge_cumulant_20260822 import (
    one_remote_correction_row,
)
from research_gate_b_targeted_local_bank_20260822 import (
    grouped_puncture_rooted_core_row,
)

R = 0
MAXIMUM_DEFECT = 0


def correction(shift: int):
    rooted = grouped_puncture_rooted_core_row(R, 2, shift, 6)
    remote = one_remote_correction_row(R, shift, MAXIMUM_DEFECT)
    return shift, tuple(rooted[index] + remote[index] for index in range(2))


def main() -> None:
    global R, MAXIMUM_DEFECT
    R = int(sys.argv[1])
    MAXIMUM_DEFECT = int(sys.argv[2])
    shifts = (0, 1, R + 2, R + 3)
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
        "defect",
        MAXIMUM_DEFECT,
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
