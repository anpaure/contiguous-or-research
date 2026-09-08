#!/usr/bin/env python3
"""Exact finite audit of the all-split product-atom distance profile."""

from math import comb, factorial


def local_distance_census(b: int) -> list[int]:
    h = (b - 1) // 2
    base = set(range(h))
    out = [0] * (h + 1)
    for shift in range(b):
        other = {(shift + j) % b for j in range(h)}
        distance = len(base - other)
        out[distance] += 1
    return out


def audit(b: int) -> None:
    assert b >= 5 and b % 2 == 1
    h = (b - 1) // 2
    t = local_distance_census(b)
    assert t == [1] + [2] * h

    convolution = [0] * (b + 1)
    for a, na in enumerate(t):
        for c, nc in enumerate(t):
            convolution[a + c] += na * nc

    expected = [1] + [4 * min(d, b - d) for d in range(1, b)] + [0]
    assert convolution == expected
    assert sum(convolution) == b * b

    degree = factorial(b) ** 2
    ratios = []
    for d in range(1, b):
        numerator = expected[d]
        denominator = comb(b, d) ** 2
        ratios.append((numerator / denominator, d))
        # Integral codegree check from the closed formula.
        assert (degree * numerator) % denominator == 0
    maximum = max(x for x, _ in ratios)
    maximizers = {d for x, d in ratios if x == maximum}
    assert maximum == 4 / (b * b)
    assert maximizers == {1, b - 1}

    overlap = sum(
        expected[d] ** 2 / comb(b, d) ** 2 for d in range(1, b)
    )
    print(
        f"b={b:2d} h={h:2d} edge={b*b:4d} D={(degree):d} "
        f"max_ratio={maximum:.12g} overlap={overlap:.12g}"
    )


def main() -> None:
    for b in range(5, 32, 2):
        audit(b)
    print("ALL_SPLIT_PRODUCT_ATOM_PROFILE_AUDIT_PASS")


if __name__ == "__main__":
    main()
