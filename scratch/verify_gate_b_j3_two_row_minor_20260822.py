#!/usr/bin/env python3
"""Exact checker for the fixed-j=3 Gate-B two-row local minor."""

from __future__ import annotations

import hashlib
from fractions import Fraction
from math import factorial
from pathlib import Path

from research_gate_b_allj_boundary_averages_20260822 import falling
from research_gate_b_local_atoms_fast_venn_20260822 import local_row


def rows(r: int) -> tuple[Fraction, Fraction, Fraction, Fraction]:
    a = Fraction(
        49 * r**6
        - 523 * r**5
        + 2733 * r**4
        - 7695 * r**3
        + 10796 * r**2
        - 7196 * r
        + 1296,
        2
        * r**3
        * (r - 4)
        * (r - 3)
        * (r - 2) ** 2
        * (r - 1) ** 2
        * (r + 1) ** 2,
    )
    b = Fraction(
        147 * r**7
        - 2002 * r**6
        + 12376 * r**5
        - 43364 * r**4
        + 86273 * r**3
        - 89142 * r**2
        + 45000 * r
        - 8640,
        2
        * r**3
        * (r - 4)
        * (r - 3) ** 2
        * (r - 2) ** 2
        * (r - 1) ** 2
        * (r + 1) ** 2,
    )
    c = -Fraction(
        4 * r**5
        - 173 * r**4
        + 820 * r**3
        - 1385 * r**2
        + 1084 * r
        - 260,
        6 * r**3 * (r - 2) ** 2 * (r - 1) ** 2 * (r + 1) ** 2,
    )
    d = Fraction(
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
    )
    return a, b, c, d


def determinant(r: int) -> Fraction:
    numerator = (
        294 * r**12
        - 5327 * r**11
        + 45972 * r**10
        - 227185 * r**9
        + 671640 * r**8
        - 1273365 * r**7
        + 2059524 * r**6
        - 4190095 * r**5
        + 8018970 * r**4
        - 9937460 * r**3
        + 6936984 * r**2
        - 2534976 * r
        + 376704
    )
    denominator = (
        6
        * r**6
        * (r - 4)
        * (r - 3) ** 2
        * (r - 2) ** 4
        * (r - 1) ** 4
        * (r + 1) ** 4
    )
    return Fraction(numerator, denominator)


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

    for r in range(6, 30):
        scale = (
            2
            * r
            * factorial(r)
            * factorial(r + 1)
            * falling(r - 4, 1)
            * falling(r + 1, 1)
        )
        observed = tuple(
            Fraction(value, scale)
            for row in (local_row(r, 3, 0), local_row(r, 3, r + 3))
            for value in row
        )
        expected = rows(r)
        assert observed == expected
        a, b, c, d = expected
        assert a * d - b * c == determinant(r)
        assert determinant(r) >= Fraction(48, r**9)

    print(
        "GATE_B_J3_TWO_ROW_MINOR_PASS helper_hashes=PASS "
        "closed_rows_r=6..29=PASS determinant=PASS lower_bound=PASS"
    )


if __name__ == "__main__":
    main()
