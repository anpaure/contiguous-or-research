#!/usr/bin/env python3
"""Exact/numerical conditioning diagnostics for the local atom profiles."""

from __future__ import annotations

import argparse
from fractions import Fraction
from math import factorial, log, sqrt

from research_gate_b_allj_boundary_averages_20260822 import falling
from research_gate_b_local_atoms_fast_venn_20260822 import local_profile


def run(r: int, levels: list[int]) -> None:
    for level in levels:
        profile = local_profile(r, level)
        ell = r + 3
        scale = (
            2
            * r
            * factorial(r)
            * factorial(r + 1)
            * falling(r - 4, level - 2)
            * falling(r + 1, level - 2)
        )
        first, second = profile[0], profile[ell]
        determinant = Fraction(
            first[0] * second[1] - first[1] * second[0], scale**2
        )
        aa = sum(Fraction(x * x, scale**2) for x, _ in profile)
        bb = sum(Fraction(y * y, scale**2) for _, y in profile)
        ab = sum(Fraction(x * y, scale**2) for x, y in profile)
        af, bf, cf = float(aa), float(bb), float(ab)
        least = (af + bf - sqrt((af - bf) ** 2 + 4 * cf * cf)) / 2
        singular = sqrt(max(0.0, least))
        print(
            f"r={r} j={level} det={float(determinant):.12g} "
            f"det_power={-log(float(determinant))/log(r):.8g} "
            f"smin={singular:.12g} "
            f"smin_power={-log(singular)/log(r):.8g}"
        )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("r", type=int)
    parser.add_argument("levels", type=int, nargs="*")
    args = parser.parse_args()
    levels = args.levels or sorted(
        {2, 3, max(2, (args.r - 2) // 2), args.r - 3, args.r - 2}
    )
    run(args.r, [level for level in levels if 2 <= level <= args.r - 2])


if __name__ == "__main__":
    main()
