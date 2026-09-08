#!/usr/bin/env python3
"""Replay the j=2 near/far finite determinant and gap localization algebra."""

from __future__ import annotations

import hashlib
import sys
from fractions import Fraction
from itertools import combinations
from math import comb, factorial
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))


EXPECTED_HASHES = {
    "research_gate_b_j2_near_far_local_symbolic_20260822.py": "e67ae9c80fecc2abe03c84fdd07d87e874ae4fec3fbe60ad7c8bb56780298e6b",
    "research_gate_b_j2_gap6_remote_symbolic_20260822.py": "29258140628d10d751a5dd09c4a1cfb3d0b25e9dae33c3144d224c65eb319c81",
    "research_gate_b_j2_single_remote_edge_cumulant_20260822.py": "f80e904366417aed828e1fa0e158aa3f5041044f2496e6daf1f31380c1606735",
    "research_gate_b_targeted_local_bank_20260822.py": "ed599de779f6f185a13a3718cca91edeaa44461003eb19781d2a3cad6690b674",
    "research_gate_b_j2_six_vertex_symbolic_20260822.py": "1c109fcf68a1324852e62b74a81fff63a4ad4620e5ebd2080f5a9f9aee02494b",
    "research_gate_b_local_atoms_fast_venn_20260822.py": "ac53061e70687df50e88f068e8feb517291edd9b388392aa298039d1423738fa",
    "research_gate_b_zero_avoidance_local_atom_profiles_20260822.py": "04c2a80507a927bfacbb9a166e094b0dcc6b55708c7f3ac24ae7fdc23bcfe765",
    "research_gate_b_local_hahn_distributions_20260822.py": "43c7cb80173515cb8b754b0e7c8271dce985f8bab96b6d5ebdf35d2b58dd8423",
    "research_w2_hahn_venn_exact_20260822.py": "8b7916edd570e7705b9154f88e66b0922d9d0f3ac05e1c8ed874eaac695c04d4",
    "research_gate_b_allj_boundary_averages_20260822.py": "f3a1e3e1cff2d585e20448e077adcc71d8b63918441b5936c7bff2430d31c2df",
}


def authenticate_helpers() -> None:
    for name, expected in EXPECTED_HASHES.items():
        actual = hashlib.sha256((HERE / name).read_bytes()).hexdigest()
        assert actual == expected, (name, actual, expected)


def product(values) -> int:
    answer = 1
    for value in values:
        answer *= value
    return answer


def compositions(total: int, parts: int):
    for cuts in combinations(range(1, total), parts - 1):
        points = (0, *cuts, total)
        yield tuple(points[index + 1] - points[index] for index in range(parts))


def gap_majorization_audit() -> None:
    """Exhaust the only numerical inequality in the Venn-gap corollary."""
    tested = 0
    for r in range(3, 11):
        b = 2 * r + 1
        for q in range(2, min(7, b) + 1):
            for raw_gaps in compositions(b, q):
                gaps = tuple(sorted(raw_gaps, reverse=True))
                delta = sum(gaps[2:])
                if delta > r - 2 or gaps[0] > r + 2:
                    continue
                left = product(factorial(gap) for gap in gaps)
                right = factorial(r + 2) * factorial(r - 1 - delta) * factorial(delta)
                assert left <= right
                identity_left = Fraction(right, factorial(r) * factorial(r + 1))
                identity_right = Fraction(r + 2, (delta + 1) * comb(r, delta + 1))
                assert identity_left == identity_right
                tested += 1
    assert tested > 1000


def closed_local_determinant(r: int) -> Fraction:
    from research_gate_b_j2_near_far_local_symbolic_20260822 import (
        EXPECTED_SHIFTED_23,
    )

    x = r - 23
    numerator = sum(
        coefficient * x**power
        for power, coefficient in enumerate(EXPECTED_SHIFTED_23)
    )
    denominator = (
        (r - 10)
        * (r - 9)
        * r**3
        * (r + 1)
        * product((r - offset) ** 2 for offset in range(1, 9))
    )
    return Fraction(numerator, 12 * denominator**2)


def local_lower_bound_audit() -> None:
    for r in (23, 24, 29, 47, 100, 1000):
        determinant = closed_local_determinant(r)
        assert determinant > 0
        assert determinant >= Fraction(1, 2**272 * r**6)


def main() -> None:
    authenticate_helpers()
    gap_majorization_audit()
    local_lower_bound_audit()

    # Each symbolic replay reconstructs all degree-six type polynomials
    # from seven exact radii and tests six unused radii including r=23.
    from research_gate_b_j2_near_far_local_symbolic_20260822 import (
        main as local_symbolic_main,
    )
    from research_gate_b_j2_gap6_remote_symbolic_20260822 import (
        main as gap6_symbolic_main,
    )

    local_symbolic_main()
    gap6_symbolic_main()
    print(
        "GATE_B_J2_NEAR_FAR_CUMULANT_AND_GAP_LOCALIZATION_PASS "
        "helper_hashes=PASS gap_majorization=PASS local_lower_bound=PASS "
        "local_33_types=PASS gap6_first_edge=PASS unused_radii=PASS"
    )


if __name__ == "__main__":
    main()
