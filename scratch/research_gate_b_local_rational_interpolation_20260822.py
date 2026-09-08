#!/usr/bin/env python3
"""Search rational formulas for the two decisive local-profile rows."""

from __future__ import annotations

import argparse
import sys
from fractions import Fraction
from math import factorial

sys.path.insert(0, "/tmp/gateb_sympy")
import sympy as sp
from sympy.polys.polyfuncs import rational_interpolate

from research_gate_b_allj_boundary_averages_20260822 import falling
from research_gate_b_local_atoms_fast_venn_20260822 import local_row


def normalized_rows(r: int, level: int) -> tuple[Fraction, ...]:
    scale = (
        2
        * r
        * factorial(r)
        * factorial(r + 1)
        * falling(r - 4, level - 2)
        * falling(r + 1, level - 2)
    )
    return tuple(
        Fraction(value, scale)
        for row in (local_row(r, level, 0), local_row(r, level, r + 3))
        for value in row
    )


def find_formula(
    values: list[tuple[int, Fraction]], checks: list[tuple[int, Fraction]], variable
):
    sympy_values = [(x, sp.Rational(y.numerator, y.denominator)) for x, y in values]
    for numerator_degree in range(len(values)):
        candidate = sp.factor(
            sp.cancel(rational_interpolate(sympy_values, numerator_degree, variable))
        )
        if all(
            sp.cancel(candidate.subs(variable, x))
            == sp.Rational(y.numerator, y.denominator)
            for x, y in checks
        ):
            return numerator_degree, candidate
    return None


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("level", type=int)
    parser.add_argument("--train-max", type=int, default=21)
    parser.add_argument("--check-max", type=int, default=25)
    parser.add_argument("--all-classes", action="store_true")
    parser.add_argument("--min-r", type=int, default=6)
    args = parser.parse_args()
    variable = sp.symbols("r")
    rows = []
    for r in range(max(args.min_r, args.level + 2), args.check_max + 1):
        if args.all_classes:
            scale = (
                2
                * r
                * factorial(r)
                * factorial(r + 1)
                * falling(r - 4, args.level - 2)
                * falling(r + 1, args.level - 2)
            )
            starts = (0, 1, 2, r - 1, r, r + 1, r + 2, r + 3, 3)
            value = tuple(
                Fraction(entry, scale)
                for start in starts
                for entry in local_row(r, args.level, start)
            )
        else:
            value = normalized_rows(r, args.level)
        rows.append((r, value))
        print("data", r, *(str(entry) for entry in value), flush=True)
    for coordinate in range(len(rows[0][1])):
        train = [
            (r, value[coordinate]) for r, value in rows if r <= args.train_max
        ]
        checks = [
            (r, value[coordinate]) for r, value in rows if r > args.train_max
        ]
        print("formula", coordinate, find_formula(train, checks, variable))


if __name__ == "__main__":
    main()
