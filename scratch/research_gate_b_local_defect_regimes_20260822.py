#!/usr/bin/env python3
"""Interpolate exact Gate-B local omitted-triple defect regimes."""

from __future__ import annotations

import argparse
import sys
from fractions import Fraction
from math import factorial

from research_gate_b_allj_boundary_averages_20260822 import falling
from research_gate_b_local_atoms_fast_venn_20260822 import local_row
from research_gate_b_local_hahn_distributions_20260822 import local_distribution


def values(r: int, level: int) -> tuple[Fraction, ...]:
    scale = (
        2
        * r
        * factorial(r)
        * factorial(r + 1)
        * falling(r - 4, level - 2)
        * falling(r + 1, level - 2)
    )
    base, first, second = (
        tuple(Fraction(entry, scale) for entry in local_row(r, level, start))
        for start in (3, r + 1, r + 2)
    )
    defect_first = tuple(base[index] - first[index] for index in range(2))
    defect_second = tuple(base[index] - second[index] for index in range(2))
    determinant = (
        defect_first[0] * defect_second[1]
        - defect_first[1] * defect_second[0]
    )
    return (*defect_first, *defect_second, determinant)


def main() -> None:
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--fixed-level", type=int)
    group.add_argument("--top-offset", type=int)
    parser.add_argument("--min-r", type=int, default=9)
    parser.add_argument("--train-max", type=int, default=18)
    parser.add_argument("--check-max", type=int, default=22)
    parser.add_argument("--distribution-parameters", action="store_true")
    args = parser.parse_args()

    sys.path.insert(0, "/tmp/gateb_sympy")
    import sympy as sp
    from sympy.polys.polyfuncs import rational_interpolate

    rows = []
    for r in range(args.min_r, args.check_max + 1):
        level = (
            args.fixed_level
            if args.fixed_level is not None
            else r - 2 - args.top_offset
        )
        if not 2 <= level <= r - 2:
            continue
        row = (
            distribution_parameters(r)
            if args.distribution_parameters
            else values(r, level)
        )
        rows.append((r, row))
        print("data", r, level, *(str(entry) for entry in row), flush=True)

    variable = sp.symbols("r")
    for coordinate in range(len(rows[0][1])):
        train = [
            (r, sp.Rational(row[coordinate].numerator, row[coordinate].denominator))
            for r, row in rows
            if r <= args.train_max
        ]
        checks = [
            (r, sp.Rational(row[coordinate].numerator, row[coordinate].denominator))
            for r, row in rows
            if r > args.train_max
        ]
        found = None
        for degree in range(len(train)):
            candidate = sp.factor(
                sp.cancel(rational_interpolate(train, degree, variable))
            )
            if all(
                sp.cancel(candidate.subs(variable, r)) == value
                for r, value in checks
            ):
                found = (degree, candidate)
                break
        print("formula", coordinate, found)


def distribution_parameters(r: int) -> tuple[Fraction, ...]:
    """Quadratic coefficients and endpoint defects for C1,C2 on both shores."""
    dm = 2 * r * factorial(r) * factorial(r + 1)
    k_pool = r - 4
    rows = {
        (shore, start): local_distribution(r, shore, start)
        for shore in (r, r - 1)
        for start in (3, r + 1, r + 2)
    }
    answer = []
    for shore in (r, r - 1):
        root_count = shore - 2
        for start in (r + 1, r + 2):
            values_by_inside = {
                inside: Fraction(
                    rows[(shore, 3)].get((inside, root_count - inside), 0)
                    - rows[(shore, start)].get((inside, root_count - inside), 0),
                    dm,
                )
                for inside in range(k_pool + 1)
            }
            coefficient = values_by_inside[0] / (r - 3)
            polynomial = lambda inside: coefficient * (r - 3 - inside) * (inside + 1)
            residuals = tuple(
                values_by_inside[inside] - polynomial(inside)
                for inside in range(k_pool + 1)
            )
            cutoff = k_pool - (0 if start == r + 1 or shore == r else 1)
            assert all(residuals[inside] == 0 for inside in range(cutoff))
            if start == r + 1 or shore == r:
                assert all(residuals[inside] == 0 for inside in range(k_pool))
                answer.extend((coefficient, residuals[k_pool]))
            else:
                assert all(residuals[inside] == 0 for inside in range(k_pool - 1))
                answer.extend((coefficient, residuals[k_pool - 1], residuals[k_pool]))
    return tuple(answer)


if __name__ == "__main__":
    main()
