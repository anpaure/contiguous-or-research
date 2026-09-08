#!/usr/bin/env python3
"""Exact replay for the j=2 six-vertex rooted-core determinant."""

from __future__ import annotations

import hashlib
import sys
from fractions import Fraction
from math import factorial
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

EXPECTED_HASHES = {
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


def closed_determinant(r: int) -> Fraction:
    from research_gate_b_j2_six_vertex_symbolic_20260822 import (
        EXPECTED_SHIFTED_23,
    )

    x = r - 23
    numerator = sum(
        coefficient * x**power
        for power, coefficient in enumerate(EXPECTED_SHIFTED_23)
    )
    denominator = (
        (r - 7)
        * (r - 6)
        * r**3
        * (r + 1)
        * product((r - offset) ** 2 for offset in range(1, 6))
    )
    return Fraction(numerator, 12 * denominator**2)


def product(values) -> int:
    answer = 1
    for value in values:
        answer *= value
    return answer


def direct_unused_radius() -> None:
    from research_gate_b_targeted_local_bank_20260822 import (
        grouped_puncture_rooted_core_row,
    )

    r = 23
    degree = 2 * r * factorial(r) * factorial(r + 1)
    corrections = {
        shift: grouped_puncture_rooted_core_row(r, 2, shift, 6)
        for shift in (r, r + 1, r + 2, r + 3)
    }
    left = tuple(
        Fraction(corrections[r][shore] - corrections[r + 1][shore], degree)
        for shore in range(2)
    )
    right = tuple(
        Fraction(corrections[r + 2][shore] - corrections[r + 3][shore], degree)
        for shore in range(2)
    )
    determinant = left[0] * right[1] - left[1] * right[0]
    assert determinant == closed_determinant(r)
    assert determinant > Fraction(1, 2**187 * r**6)


def translation_quotient_audit() -> None:
    from research_gate_b_local_atoms_fast_venn_20260822 import boundary_cell_data
    from research_gate_b_targeted_local_bank_20260822 import (
        positional_root_weights,
        positional_root_weights_cyclic,
    )
    from research_gate_b_zero_avoidance_local_atom_profiles_20260822 import (
        local_blocker_sets,
    )

    for r in (6, 7):
        b = 2 * r + 1
        for shift in (0, 3, r + 1):
            for blocker_data in local_blocker_sets(r, shift):
                sizes = tuple(value[0] for value in blocker_data)
                masks = tuple(value[2] for value in blocker_data)
                cell_sizes, _, _ = boundary_cell_data(b, shift, masks)
                for root_size in (r, r - 1):
                    assert positional_root_weights(
                        r, root_size, sizes, cell_sizes
                    ) == positional_root_weights_cyclic(
                        r, root_size, sizes, cell_sizes
                    )


def topology_census() -> None:
    from research_gate_b_targeted_local_bank_20260822 import (
        complete_bounded_blocker_sets,
        complete_bounded_rooted_core_sets,
    )

    r = 23
    expected = (621, 464, 462, 935)
    observed = []
    for shift in (r, r + 1, r + 2, r + 3):
        complete = [
            blockers
            for blockers in complete_bounded_blocker_sets(r, shift, 6)
            if any(start == 0 for _, start, _ in blockers)
        ]
        rooted = [
            blockers
            for blockers in complete_bounded_rooted_core_sets(r, shift, 6)
            if any(start == 0 for _, start, _ in blockers)
        ]
        assert len(rooted) <= len(complete)
        observed.append(len(rooted))
    assert tuple(observed) == expected


def main() -> None:
    authenticate_helpers()
    translation_quotient_audit()
    topology_census()
    # This reconstructs every degree-six grouped polynomial from seven
    # radii and validates at six unused radii, including the domain endpoint.
    from research_gate_b_j2_six_vertex_symbolic_20260822 import main as symbolic_main

    symbolic_main()
    direct_unused_radius()
    print(
        "GATE_B_J2_SIX_VERTEX_ROOTED_CORE_DETERMINANT_PASS "
        "helper_hashes=PASS translation_quotient=PASS topology=PASS "
        "degree_six_reconstruction=PASS unused_radii=PASS "
        "closed_determinant_r23=PASS lower_bound=PASS"
    )


if __name__ == "__main__":
    main()
