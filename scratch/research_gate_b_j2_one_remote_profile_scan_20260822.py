#!/usr/bin/env python3
"""Scan cyclic defect rows after the exact one-rootless-edge cumulant."""

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


SCAN_R = 0


def correction(shift: int):
    rooted = grouped_puncture_rooted_core_row(SCAN_R, 2, shift, 6)
    remote = one_remote_correction_row(SCAN_R, shift)
    return shift, tuple(rooted[index] + remote[index] for index in range(2))


def main() -> None:
    global SCAN_R
    SCAN_R = int(sys.argv[1]) if len(sys.argv) > 1 else 20
    b = 2 * SCAN_R + 1
    degree = 2 * SCAN_R * factorial(SCAN_R) * factorial(SCAN_R + 1)
    context = mp.get_context("fork")
    requested_differences = (
        [int(value) % b for value in sys.argv[2:]]
        if len(sys.argv) > 2
        else list(range(b))
    )
    needed_rows = sorted(
        set(requested_differences)
        | {(shift + 1) % b for shift in requested_differences}
    )
    with context.Pool(6) as pool:
        rows = dict(pool.map(correction, needed_rows))
    differences = {
        shift: tuple(
            Fraction(rows[shift][shore] - rows[(shift + 1) % b][shore], degree)
            for shore in range(2)
        )
        for shift in requested_differences
    }
    nonzero = [shift for shift, row in differences.items() if any(row)]
    candidates = []
    for first_index, first in enumerate(nonzero):
        for second in nonzero[first_index + 1 :]:
            left = differences[first]
            right = differences[second]
            determinant = left[0] * right[1] - left[1] * right[0]
            candidates.append((abs(determinant), determinant, first, second))
    candidates.sort(reverse=True)
    print("r", SCAN_R, "nonzero", len(nonzero))
    for shift in nonzero:
        row = differences[shift]
        print(
            "D",
            shift,
            "r2",
            *(float(value * SCAN_R**2) for value in row),
            "r3",
            *(float(value * SCAN_R**3) for value in row),
        )
    print("TOP_DETERMINANTS")
    for _, determinant, first, second in candidates[:20]:
        print(
            first,
            second,
            "det*r4",
            float(determinant * SCAN_R**4),
            "det*r5",
            float(determinant * SCAN_R**5),
            "det*r6",
            float(determinant * SCAN_R**6),
        )


if __name__ == "__main__":
    main()
