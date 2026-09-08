#!/usr/bin/env python3
"""Exact atom decomposition of the fixed-j=3 far local-profile rows.

This is a research evaluator.  It groups the 22 signed local blocker terms
by their four-vertex support, evaluates each of the resulting sixteen atoms,
and normalizes by D_M (r-4)(r+1).
"""

from __future__ import annotations

import argparse
import sys
from collections import defaultdict
from fractions import Fraction
from itertools import combinations
from math import factorial

from research_gate_b_local_atoms_fast_venn_20260822 import blocker_term_value
from research_gate_b_zero_avoidance_local_atom_profiles_20260822 import (
    retained_boundary_edges,
)


Blocker = tuple[int, int, int]


def local_atoms(
    r: int, event_start: int
) -> dict[tuple[int, ...], list[tuple[int, tuple[Blocker, ...]]]]:
    """Return signed blocker terms grouped by their four-vertex support."""
    b = 2 * r + 1
    edges = retained_boundary_edges(r)
    first_root = (-2 * event_start) % b
    roots = {first_root, (first_root + 5) % b}
    atoms: dict[
        tuple[int, ...], list[tuple[int, tuple[Blocker, ...]]]
    ] = defaultdict(list)
    edge_items = list(edges.items())
    for number in (2, 3):
        for chosen in combinations(edge_items, number):
            vertices = {vertex for edge, _ in chosen for vertex in edge}
            if len(vertices) != 4 or not roots <= vertices:
                continue
            support = tuple(
                sorted(((vertex - first_root + r) % b) - r for vertex in vertices)
            )
            blockers = tuple(value for _, value in chosen)
            atoms[support].append((1 if number == 2 else -1, blockers))
    assert len(atoms) == 16
    assert sum(len(terms) for terms in atoms.values()) == 20
    return dict(atoms)


def atom_row(
    r: int,
    event_start: int,
    terms: list[tuple[int, tuple[Blocker, ...]]],
    level: int = 3,
) -> tuple[int, int]:
    return tuple(
        sum(
            sign * blocker_term_value(r, root_size, level, event_start, blockers)
            for sign, blockers in terms
        )
        for root_size in (r, r - 1)
    )


def normalized_atom_rows(
    r: int, event_start: int
) -> dict[tuple[int, ...], tuple[Fraction, Fraction]]:
    scale = 2 * r * factorial(r) * factorial(r + 1) * (r - 4) * (r + 1)
    return {
        support: tuple(Fraction(value, scale) for value in atom_row(r, event_start, terms))
        for support, terms in local_atoms(r, event_start).items()
    }


def centered_support(r: int, event_start: int, support: tuple[int, ...]) -> tuple[int, ...]:
    """Use integer offsets from the first event root in [-r,r]."""
    return support


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("r", type=int, nargs="?")
    parser.add_argument("--start", choices=("r+1", "r+2"), default="r+1")
    parser.add_argument("--scan-max", type=int)
    parser.add_argument("--train-max", type=int, default=19)
    args = parser.parse_args()
    if args.scan_max is not None:
        scan(args.scan_max, args.train_max)
        return
    if args.r is None:
        parser.error("r is required unless --scan-max is used")
    start = args.r + (1 if args.start == "r+1" else 2)
    rows = normalized_atom_rows(args.r, start)
    total = [Fraction(0), Fraction(0)]
    for support, row in sorted(rows.items(), key=lambda item: centered_support(args.r, start, item[0])):
        centered = centered_support(args.r, start, support)
        print(centered, *(str(value) for value in row))
        total[0] += row[0]
        total[1] += row[1]
    print("total", *map(str, total))


def scan(maximum_r: int, training_maximum: int) -> None:
    """Interpolate each fixed-support atom and check on held-out radii."""
    sys.path.insert(0, "/tmp/gateb_sympy")
    import sympy as sp
    from sympy.polys.polyfuncs import rational_interpolate

    variable = sp.symbols("r")
    values: dict[tuple[str, tuple[int, ...], int], list[tuple[int, Fraction]]] = defaultdict(list)
    for r in range(9, maximum_r + 1):
        for label, start in (("r+1", r + 1), ("r+2", r + 2)):
            for support, row in normalized_atom_rows(r, start).items():
                for shore, entry in enumerate(row):
                    values[(label, support, shore)].append((r, entry))
        print(f"data r={r}", flush=True)

    for key in sorted(values):
        train = [(x, sp.Rational(y.numerator, y.denominator)) for x, y in values[key] if x <= training_maximum]
        checks = [(x, sp.Rational(y.numerator, y.denominator)) for x, y in values[key] if x > training_maximum]
        found = None
        for numerator_degree in range(len(train)):
            candidate = sp.factor(sp.cancel(rational_interpolate(train, numerator_degree, variable)))
            if all(sp.cancel(candidate.subs(variable, x)) == y for x, y in checks):
                found = (numerator_degree, candidate)
                break
        print("formula", key, found)


if __name__ == "__main__":
    main()
