#!/usr/bin/env python3
"""Exact checks for the Gate-B j=2 local-scale obstruction note."""

from __future__ import annotations

import argparse
import hashlib
from collections import Counter, defaultdict
from fractions import Fraction
from math import factorial
from pathlib import Path

from research_gate_b_local_atoms_fast_venn_20260822 import (
    bounded_vertex_blocker_sets,
    bounded_vertex_row,
    local_row,
)
from research_gate_b_zero_avoidance_local_atom_profiles_20260822 import (
    retained_boundary_edges,
)


def closed_rows(r: int) -> tuple[Fraction, Fraction, Fraction, Fraction]:
    common = r**3 * (r - 2) ** 2 * (r - 1) ** 2 * (r + 1)
    first_denominator = common * (r - 4) * (r - 3)
    middle_0 = -Fraction(
        25 * r**6
        - 338 * r**5
        + 1820 * r**4
        - 5571 * r**3
        + 8838 * r**2
        - 5512 * r
        + 1008,
        first_denominator,
    )
    lower_0 = -Fraction(
        25 * r**6
        - 380 * r**5
        + 2281 * r**4
        - 7583 * r**3
        + 13501 * r**2
        - 10490 * r
        + 2808,
        first_denominator,
    )
    middle_ell = -Fraction(
        4 * r**5
        + 55 * r**4
        - 536 * r**3
        + 1204 * r**2
        - 710 * r
        + 28,
        3 * common,
    )
    lower_ell = -Fraction(
        4 * r**5
        + 49 * r**4
        - 641 * r**3
        + 1822 * r**2
        - 1559 * r
        + 406,
        3 * common,
    )
    return middle_0, lower_0, middle_ell, lower_ell


def determinant_formula(r: int) -> Fraction:
    numerator = (
        18 * r**10
        - 131 * r**9
        + 201 * r**8
        + 1889 * r**7
        + 53250 * r**6
        - 493848 * r**5
        + 1629447 * r**4
        - 2796178 * r**3
        + 2811252 * r**2
        - 1521944 * r
        + 330624
    )
    denominator = (
        3
        * r**6
        * (r - 4)
        * (r - 3)
        * (r - 2) ** 4
        * (r - 1) ** 4
        * (r + 1) ** 2
    )
    return Fraction(numerator, denominator)


def component_sizes(vertices: frozenset[int], edges: list[tuple[int, int]]):
    remaining = set(vertices)
    answer = []
    while remaining:
        stack = [remaining.pop()]
        size = 0
        while stack:
            vertex = stack.pop()
            size += 1
            for edge in edges:
                if vertex not in edge:
                    continue
                other = edge[0] if edge[1] == vertex else edge[1]
                if other in remaining:
                    remaining.remove(other)
                    stack.append(other)
        answer.append(size)
    return tuple(sorted(answer))


def topology_census(r: int) -> tuple[int, int, Counter]:
    event_start = 3
    edge_values = retained_boundary_edges(r)
    reverse = {value: edge for edge, value in edge_values.items()}
    terms = bounded_vertex_blocker_sets(r, event_start, 5)
    by_vertices: dict[frozenset[int], list[tuple]] = defaultdict(list)
    for term in terms:
        vertices = frozenset(vertex for value in term for vertex in reverse[value])
        by_vertices[vertices].append(term)
    signatures = Counter()
    for vertices, vertex_terms in by_vertices.items():
        induced = [edge for edge in edge_values if set(edge) <= vertices]
        signatures[
            (component_sizes(vertices, induced), len(induced), len(vertex_terms))
        ] += 1
    return len(terms), len(by_vertices), signatures


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--deep", action="store_true")
    args = parser.parse_args()

    root = Path(__file__).resolve().parent
    expected_hashes = {
        "research_gate_b_local_atoms_fast_venn_20260822.py":
            "ac53061e70687df50e88f068e8feb517291edd9b388392aa298039d1423738fa",
        "research_gate_b_zero_avoidance_local_atom_profiles_20260822.py":
            "04c2a80507a927bfacbb9a166e094b0dcc6b55708c7f3ac24ae7fdc23bcfe765",
        "research_gate_b_allj_boundary_averages_20260822.py":
            "f3a1e3e1cff2d585e20448e077adcc71d8b63918441b5936c7bff2430d31c2df",
        "research_w2_hahn_venn_exact_20260822.py":
            "8b7916edd570e7705b9154f88e66b0922d9d0f3ac05e1c8ed874eaac695c04d4",
    }
    for name, expected_hash in expected_hashes.items():
        observed_hash = hashlib.sha256((root / name).read_bytes()).hexdigest()
        assert observed_hash == expected_hash

    for r in range(6, 19):
        degree_scale = 2 * r * factorial(r) * factorial(r + 1)
        expected = closed_rows(r)
        observed = tuple(
            Fraction(value, degree_scale)
            for row in (local_row(r, 2, 0), local_row(r, 2, r + 3))
            for value in row
        )
        assert observed == expected
        a, b, c, d = expected
        determinant = a * d - b * c
        assert determinant == determinant_formula(r)
        assert determinant >= Fraction(6, r**8)

    expected_signatures = Counter(
        {
            ((2, 2), 2, 1): 10,
            ((4,), 3, 2): 6,
            ((2, 3), 3, 1): 54,
            ((5,), 4, 3): 20,
            ((5,), 4, 2): 6,
            ((5,), 5, 8): 8,
        }
    )
    for r in range(9, 81):
        terms, vertex_sets, signatures = topology_census(r)
        assert (terms, vertex_sets) == (212, 104)
        assert signatures == expected_signatures

    if args.deep:
        r = 8
        expected = {
            0: (84461184, 18108288),
            r + 3: (-15240960, 19025280),
            3: (356277888, 280143360),
        }
        for start, row in expected.items():
            assert bounded_vertex_row(r, 2, start, 5) == row

    print(
        "GATE_B_J2_LOCAL_SCALE_FIVE_VERTEX_BANK_PASS "
        "helper_hashes=PASS closed_rows=PASS determinant=PASS "
        "topology_r=9..80=PASS "
        f"deep_r8={'PASS' if args.deep else 'SKIP'}"
    )


if __name__ == "__main__":
    main()
