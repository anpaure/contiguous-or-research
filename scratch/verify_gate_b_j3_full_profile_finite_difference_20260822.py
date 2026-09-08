#!/usr/bin/env python3
"""Exact checker for the fixed-j=3 full local-profile finite difference."""

from __future__ import annotations

import hashlib
from collections import defaultdict
from fractions import Fraction
from itertools import combinations
from math import factorial
from pathlib import Path

from research_gate_b_local_atoms_fast_venn_20260822 import (
    blocker_term_value,
    local_row,
)
from research_gate_b_zero_avoidance_local_atom_profiles_20260822 import (
    retained_boundary_edges,
)


SUPPORTS = {
    (-3, 0, 2, 5),
    (-3, 0, 4, 5),
    (-3, 0, 5, 6),
    (-3, 0, 5, 8),
    (-1, 0, 2, 5),
    (-1, 0, 4, 5),
    (-1, 0, 5, 6),
    (-1, 0, 5, 8),
    (0, 1, 2, 5),
    (0, 1, 4, 5),
    (0, 1, 5, 6),
    (0, 1, 5, 8),
    (0, 2, 3, 5),
    (0, 3, 4, 5),
    (0, 3, 5, 6),
    (0, 3, 5, 8),
}

FIXED_SUPPORTS = SUPPORTS - {
    (0, 1, 2, 5),
    (0, 1, 4, 5),
    (0, 3, 4, 5),
    (0, 3, 5, 6),
}


def atom_terms(r: int, event_start: int):
    b = 2 * r + 1
    first_root = (-2 * event_start) % b
    roots = {first_root, (first_root + 5) % b}
    edges = retained_boundary_edges(r)
    atoms = defaultdict(list)
    for number in (2, 3):
        for chosen in combinations(edges.items(), number):
            vertices = {vertex for edge, _ in chosen for vertex in edge}
            if len(vertices) != 4 or not roots <= vertices:
                continue
            support = tuple(
                sorted(((vertex - first_root + r) % b) - r for vertex in vertices)
            )
            blockers = tuple(value for _, value in chosen)
            atoms[support].append((1 if number == 2 else -1, blockers))
    assert set(atoms) == SUPPORTS
    assert sum(map(len, atoms.values())) == 20
    return dict(atoms)


def normalized_atoms(r: int, event_start: int):
    scale = 2 * r * factorial(r) * factorial(r + 1) * (r - 4) * (r + 1)
    answer = {}
    for support, terms in atom_terms(r, event_start).items():
        answer[support] = tuple(
            Fraction(
                sum(
                    sign
                    * blocker_term_value(r, shore, 3, event_start, blockers)
                    for sign, blockers in terms
                ),
                scale,
            )
            for shore in (r, r - 1)
        )
    return answer


def exceptional_rows(r: int):
    t1_u = (
        Fraction(2 * (r - 1), 3 * r**3 * (r + 1) ** 2),
        Fraction(
            2 * (2 * r**3 - 3 * r**2 - 6 * r + 4),
            r**3 * (r - 2) * (r - 1) * (r + 1) ** 2,
        ),
    )
    t2_u = (
        Fraction(1, 3 * r**3 * (r + 1) ** 2),
        Fraction(2, r**3 * (r - 1) * (r + 1)),
    )
    t1_v = (
        Fraction(1, 2 * r**3 * (r + 1) ** 2),
        Fraction(
            3 * (r - 3),
            2 * r**2 * (r - 2) * (r - 1) * (r + 1) ** 2,
        ),
    )
    t2_v = (
        Fraction(2 * (r - 1), r**3 * (r + 1) ** 2),
        Fraction(6 * (r - 3), r**2 * (r - 2) * (r + 1) ** 2),
    )
    return t1_u, t2_u, t1_v, t2_v


def difference_row(r: int):
    return (
        Fraction(8 * r - 9, 6 * r**3 * (r + 1) ** 2),
        Fraction(
            4 * r**3 - 35 * r**2 + 65 * r - 24,
            2 * r**3 * (r - 2) * (r - 1) * (r + 1) ** 2,
        ),
    )


def central_row(r: int):
    return (
        -Fraction(
            4 * r**5
            - 173 * r**4
            + 820 * r**3
            - 1385 * r**2
            + 1084 * r
            - 260,
            6 * r**3 * (r - 2) ** 2 * (r - 1) ** 2 * (r + 1) ** 2,
        ),
        Fraction(
            155 * r**5
            - 1233 * r**4
            + 3401 * r**3
            - 3813 * r**2
            + 1982 * r
            - 384,
            2
            * r**3
            * (r - 3)
            * (r - 2) ** 2
            * (r - 1) ** 2
            * (r + 1) ** 2,
        ),
    )


def determinant(r: int):
    polynomial = (
        4 * r**9
        + 90 * r**8
        - 722 * r**7
        + 49 * r**6
        + 12115 * r**5
        - 42338 * r**4
        + 66300 * r**3
        - 53696 * r**2
        + 20700 * r
        - 2952
    )
    return Fraction(
        polynomial,
        3
        * r**6
        * (r - 3)
        * (r - 2) ** 3
        * (r - 1) ** 3
        * (r + 1) ** 4,
    )


def translate_polynomial(coefficients: list[int], shift: int) -> list[int]:
    """Return ascending coefficients of p(x+shift)."""
    answer = [0] * len(coefficients)
    for degree, coefficient in enumerate(coefficients):
        for chosen in range(degree + 1):
            answer[chosen] += (
                coefficient
                * combinations_count(degree, chosen)
                * shift ** (degree - chosen)
            )
    return answer


def combinations_count(n: int, k: int) -> int:
    if k < 0 or k > n:
        return 0
    numerator = denominator = 1
    for offset in range(k):
        numerator *= n - offset
        denominator *= offset + 1
    return numerator // denominator


def main() -> None:
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
    for name, expected in expected_hashes.items():
        assert hashlib.sha256((root / name).read_bytes()).hexdigest() == expected

    for r in range(9, 23):
        first = normalized_atoms(r, r + 1)
        second = normalized_atoms(r, r + 2)
        assert all(first[support] == second[support] for support in FIXED_SUPPORTS)
        assert first[(0, 1, 2, 5)] == second[(0, 3, 4, 5)]
        assert first[(0, 3, 4, 5)] == second[(0, 1, 2, 5)]

        t1_u, t2_u, t1_v, t2_v = exceptional_rows(r)
        assert first[(0, 1, 4, 5)] == t1_u
        assert second[(0, 1, 4, 5)] == t2_u
        assert first[(0, 3, 5, 6)] == t1_v
        assert second[(0, 3, 5, 6)] == t2_v

        observed_difference = tuple(
            sum(row[shore] for row in second.values())
            - sum(row[shore] for row in first.values())
            for shore in range(2)
        )
        assert observed_difference == difference_row(r)

        scale = 2 * r * factorial(r) * factorial(r + 1) * (r - 4) * (r + 1)
        direct_difference = tuple(
            Fraction(after - before, scale)
            for before, after in zip(local_row(r, 3, r + 1), local_row(r, 3, r + 2))
        )
        assert direct_difference == difference_row(r)

    for r in range(9, 500):
        delta, epsilon = difference_row(r)
        c, d = central_row(r)
        assert delta * d - epsilon * c == determinant(r)
        assert determinant(r) >= Fraction(2, 3 * r**8)
        assert abs(delta) <= Fraction(4, 3 * r**4)
        assert abs(epsilon) <= Fraction(11, r**4)
        assert abs(c) <= Fraction(35, r**4)
        assert abs(d) <= Fraction(257, r**4)

    # Ascending coefficients of P(r)-4r^9, followed by the r=x+6 shift.
    remainder = [
        -2952,
        20700,
        -53696,
        66300,
        -42338,
        12115,
        49,
        -722,
        90,
    ]
    shifted = translate_polynomial(remainder, 6)
    assert shifted == [
        3182976,
        16502556,
        18789064,
        10064388,
        3054052,
        556687,
        60445,
        3598,
        90,
    ]
    assert all(coefficient > 0 for coefficient in shifted)

    print(
        "GATE_B_J3_FULL_PROFILE_FINITE_DIFFERENCE_PASS "
        "helper_hashes=PASS atom_cancellation_r=9..22=PASS "
        "exceptional_rows=PASS full_difference=PASS determinant=PASS "
        "lower_bound=PASS"
    )


if __name__ == "__main__":
    main()
