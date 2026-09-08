#!/usr/bin/env python3
"""Exact arithmetic checks for the W2 delocalization/transfer constants."""

from fractions import Fraction
from math import comb, isqrt


def verify_constants() -> None:
    assert 3888 == 3 * 3**4 * 4**2
    assert 3888 == 36**2 * 3

    # Squaring verifies the exact rearrangement of
    # epsilon/(1-epsilon) <= 1/(12 sqrt(3) r^3).
    for r in range(5, 1000):
        denominator_without_surd_squared = 432 * r**6
        assert denominator_without_surd_squared == (12 * r**3) ** 2 * 3


def verify_dimension_and_coarse_bounds() -> None:
    for r in range(5, 501):
        b = 2 * r + 1
        k = r - 2
        ell = r + 3
        n = comb(b, k)
        assert b <= 3 * r
        assert k * (k - 1) <= r**2
        assert ell * (ell - 1) <= 4 * r**2
        exact_denominator = (
            3 * b**4 * (k * (k - 1) * ell * (ell - 1)) ** 2
        )
        assert exact_denominator <= 3888 * r**12
        for level in range(2, k + 1):
            dimension = comb(b, level) - comb(b, level - 1)
            assert 0 < dimension <= comb(b, level) <= n


def verify_integer_square_constant() -> None:
    # sqrt(3888)=36 sqrt(3); this guards the reported l_infinity constant.
    assert isqrt(3888 // 3) == 36
    assert 36**2 * 3 == 3888


def main() -> None:
    verify_constants()
    verify_dimension_and_coarse_bounds()
    verify_integer_square_constant()
    print(
        "GATE_B_W2_DELOCALIZED_INVERSE_TRANSFER_THRESHOLD_PASS "
        "scalar_constant=3888 dimension_bound_r=5..500 "
        "threshold_constant=12sqrt3 linfinity_constant=36sqrt3"
    )


if __name__ == "__main__":
    main()
