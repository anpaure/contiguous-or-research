#!/usr/bin/env python3
"""Exact r=4 check of the full-exposure zero-avoidance boundary quotient."""

from fractions import Fraction
import hashlib
from itertools import permutations
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
HELPER = "verify_exposure_zero_avoidance_decomposition_20260822.py"
EXPECTED = "a06326573b3ba46e5e3dd724918d5c4917d385cbaa8e9aa7ed480a28315686ab"
assert hashlib.sha256((HERE / HELPER).read_bytes()).hexdigest() == EXPECTED
sys.path.insert(0, str(HERE))
import verify_exposure_zero_avoidance_decomposition_20260822 as base  # noqa: E402


def profile(coefficients: list[int], size: int) -> list[int]:
    answer = []
    masks = base.SUBSETS[size]
    for start in range(base.B):
        inside_left = start
        outside_left = (start - 1) % base.B
        inside_right = (start + base.K - 1) % base.B
        outside_right = (start + base.K) % base.B
        total = 0
        for mask, coefficient in zip(masks, coefficients):
            left = ((mask >> inside_left) & 1) - ((mask >> outside_left) & 1)
            right = ((mask >> inside_right) & 1) - ((mask >> outside_right) & 1)
            total += coefficient * left * right
        answer.append(total)
    return answer


def rho(left: list[int], right: list[int]) -> Fraction:
    g00 = sum(value * value for value in left)
    g01 = sum(a * b for a, b in zip(left, right))
    g11 = sum(value * value for value in right)
    h0 = sum(left)
    h1 = sum(right)
    determinant = g00 * g11 - g01 * g01
    projection = Fraction(
        g11 * h0 * h0 - 2 * g01 * h0 * h1 + g00 * h1 * h1,
        determinant,
    )
    return (Fraction(base.B) - projection) / base.B


def main() -> None:
    identity = tuple(range(base.B))
    base_middle, base_lower = base.retained(identity)
    middle_count = len(base.SUBSETS[base.R])
    base_mask = sum(1 << index for index in base_middle)
    base_mask |= sum(1 << (middle_count + index) for index in base_lower)

    vectors = {}
    for shore, size in (("m", base.R), ("l", base.R - 1)):
        length = len(base.SUBSETS[size])
        vectors[f"degree_{shore}"] = [0] * length
        vectors[f"one_{shore}"] = [0] * length
        vectors[f"exposure_{shore}"] = [0] * length
        vectors[f"zero_{shore}"] = [0] * length

    for word in permutations(range(base.B)):
        middle, lower = base.retained(word)
        configuration = sum(1 << index for index in middle)
        configuration |= sum(1 << (middle_count + index) for index in lower)
        overlap = (configuration & base_mask).bit_count()
        duplicate = max(0, overlap - 1)
        for shore, indices in (("m", middle), ("l", lower)):
            for index in indices:
                vectors[f"degree_{shore}"][index] += 1
                vectors[f"one_{shore}"][index] += overlap
                vectors[f"exposure_{shore}"][index] += duplicate
                vectors[f"zero_{shore}"][index] += overlap == 0

    for shore in ("m", "l"):
        assert all(
            e == one - degree + zero
            for e, one, degree, zero in zip(
                vectors[f"exposure_{shore}"],
                vectors[f"one_{shore}"],
                vectors[f"degree_{shore}"],
                vectors[f"zero_{shore}"],
            )
        )

    one_m = profile(vectors["one_m"], base.R)
    one_l = profile(vectors["one_l"], base.R - 1)
    degree_m = profile(vectors["degree_m"], base.R)
    degree_l = profile(vectors["degree_l"], base.R - 1)
    exposure_m = profile(vectors["exposure_m"], base.R)
    exposure_l = profile(vectors["exposure_l"], base.R - 1)
    zero_m = profile(vectors["zero_m"], base.R)
    zero_l = profile(vectors["zero_l"], base.R - 1)

    assert one_m == one_l == degree_m == degree_l == [0] * base.B
    assert exposure_m == zero_m
    assert exposure_l == zero_l
    exact_rho = rho(zero_m, zero_l)
    expected_rho = Fraction(2565702871466, 20425156452891)
    assert exact_rho == expected_rho

    ell = base.B - base.K
    event_size = 4
    tuple_count = base.B * (base.B - 1) * (base.B - 2) * (base.B - 3)
    kappa = Fraction(
        4 * base.K * (base.K - 1) * ell * (ell - 1), tuple_count
    )
    assert Fraction(event_size, tuple_count * kappa) == Fraction(
        1, base.K * (base.K - 1) * ell * (ell - 1)
    )
    print(
        "GATE_B_FULL_EXPOSURE_ZERO_AVOIDANCE_BOUNDARY_PASS "
        "helper_hash=PASS pointwise_decomposition=PASS "
        "one_blocker_profile=ZERO exposure_equals_avoidance=PASS "
        f"rho={exact_rho}"
    )


if __name__ == "__main__":
    main()
