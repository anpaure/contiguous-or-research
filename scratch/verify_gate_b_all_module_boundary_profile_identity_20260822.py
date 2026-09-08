#!/usr/bin/env python3
"""Exact checks for the all-module Gate-B boundary-profile identity."""

from __future__ import annotations

from fractions import Fraction
import hashlib
from itertools import permutations
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent

EXPECTED_HELPERS = {
    "research_gate_b_allj_boundary_averages_20260822.py":
        "f3a1e3e1cff2d585e20448e077adcc71d8b63918441b5936c7bff2430d31c2df",
    "research_w2_hahn_venn_exact_20260822.py":
        "8b7916edd570e7705b9154f88e66b0922d9d0f3ac05e1c8ed874eaac695c04d4",
}
for helper_name, expected_hash in EXPECTED_HELPERS.items():
    actual_hash = hashlib.sha256((HERE / helper_name).read_bytes()).hexdigest()
    assert actual_hash == expected_hash, (helper_name, actual_hash)

sys.path.insert(0, str(HERE))

from research_gate_b_allj_boundary_averages_20260822 import (  # noqa: E402
    boundary_profile_value,
    exact_rho,
    extra_pair_numerator,
    falling,
    rank,
)
from research_w2_hahn_venn_exact_20260822 import coefficient_vectors  # noqa: E402


def brute_extra_sum(a: int, c: int, inside_size: int,
                    outside_size: int, pairs: int) -> int:
    inside = tuple(range(inside_size))
    outside = tuple(range(outside_size))
    answer = 0
    for chosen_inside in permutations(inside, pairs):
        for chosen_outside in permutations(outside, pairs):
            product = 1
            for x, y in zip(chosen_inside, chosen_outside):
                product *= int(x < a) - int(y < c)
            answer += product
    return answer


def verify_injection_polynomial() -> None:
    for inside_size in range(2, 6):
        for outside_size in range(2, 6):
            for pairs in range(0, min(2, inside_size, outside_size) + 1):
                for a in range(inside_size + 1):
                    for c in range(outside_size + 1):
                        exact = extra_pair_numerator(
                            a, c, inside_size, outside_size, pairs
                        )
                        brute = brute_extra_sum(
                            a, c, inside_size, outside_size, pairs
                        )
                        assert exact == brute


def verify_event_arithmetic() -> None:
    for r in range(5, 80):
        b = 2 * r + 1
        k = r - 2
        ell = b - k
        for level in range(2, k + 1):
            event_size = (
                (1 << level)
                * falling(k - 2, level - 2)
                * falling(ell - 2, level - 2)
            )
            tuple_count = falling(b, 2 * level)
            kappa = Fraction(
                (1 << level) * falling(k, level) * falling(ell, level),
                tuple_count,
            )
            assert Fraction(event_size, tuple_count * kappa) == Fraction(
                1, k * (k - 1) * ell * (ell - 1)
            )


def verify_exact_profiles() -> None:
    minimum_rho = Fraction(1)
    module_count = 0
    for r in range(5, 9):
        b, masks_by_size, coefficients = coefficient_vectors(r)
        k = r - 2
        ell = b - k
        exceptional = {0, 1, 2, r - 1, r, r + 3}
        for level in range(2, k + 1):
            profile = []
            for start in range(b):
                profile.append(
                    tuple(
                        boundary_profile_value(
                            b,
                            k,
                            size,
                            masks_by_size[size],
                            coefficients[name],
                            level,
                            start,
                        )
                        for size, name in ((r, "w_m"), (r - 1, "w_l"))
                    )
                )
            baseline = profile[3]
            assert all(
                profile[start] == baseline
                for start in range(b)
                if start not in exceptional
            )
            assert tuple(
                profile[0][coordinate]
                + profile[ell][coordinate]
                - profile[3][coordinate]
                for coordinate in range(2)
            ) == (0, 0)
            assert rank([list(row) for row in profile]) == 2
            assert rank([[a, c, 1] for a, c in profile]) == 3
            rho = exact_rho(profile)
            assert rho >= Fraction(1, 3 * b)
            minimum_rho = min(minimum_rho, rho)
            module_count += 1
    assert module_count == 14
    assert float(minimum_rho) > 0.049


def main() -> None:
    verify_injection_polynomial()
    verify_event_arithmetic()
    verify_exact_profiles()
    print(
        "GATE_B_ALL_MODULE_BOUNDARY_PROFILE_PASS "
        "helper_hashes=PASS injection_polynomial=PASS "
        "event_normalization_r=5..79 "
        "exact_profiles_r=5..8 modules=14 identity=PASS rho_bound=PASS"
    )


if __name__ == "__main__":
    main()
