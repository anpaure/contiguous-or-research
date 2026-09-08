#!/usr/bin/env python3
"""Exact audit for the depth-two Fisher-scale obstruction."""

from fractions import Fraction
from itertools import combinations
from math import comb


def choose(n: int, k: int) -> int:
    return comb(n, k) if 0 <= k <= n else 0


def overlap_weights(b: int, k: int) -> list[int]:
    words = [frozenset((s + t) % b for t in range(k)) for s in range(b)]
    counts = [0] * (k + 1)
    for left in words:
        for right in words:
            counts[len(left & right)] += 1
    weights = [b - 2 * k + 1] + [2] * (k - 1) + [1]
    assert counts == [b * weight for weight in weights]
    return weights


def eberlein_sum(b: int, k: int, j: int, h: int) -> int:
    return sum(
        (-1) ** (j - a)
        * choose(j, a)
        * choose(k - j, h - a)
        * choose(b - k - j, k - j - h + a)
        for a in range(j + 1)
    )


def theta(r: int, j: int) -> Fraction:
    b = 2 * r + 1
    k = r - 2
    total_targets = choose(b, k)
    weights = overlap_weights(b, k)
    answer = Fraction()
    for h in range(k + 1):
        shell = choose(k, h) * choose(b - k, k - h)
        answer += Fraction(
            b * weights[h] * eberlein_sum(b, k, j, h),
            total_targets * shell,
        )
    return answer


def harmonic_value(mask: int, j: int) -> int:
    value = 1
    for i in range(j):
        first = (mask >> (2 * i)) & 1
        second = (mask >> (2 * i + 1)) & 1
        value *= first - second
    return value


def direct_eigenvector_audit(r: int) -> None:
    b = 2 * r + 1
    k = r - 2
    targets = [sum(1 << x for x in subset) for subset in combinations(range(b), k)]
    target_count = len(targets)
    weights = overlap_weights(b, k)
    kernels = [
        Fraction(b * weights[h], target_count * choose(k, h) * choose(b - k, k - h))
        for h in range(k + 1)
    ]
    for j in range(2, k + 1):
        vector = [harmonic_value(mask, j) for mask in targets]
        expected = theta(r, j)
        assert any(vector)
        for row, mask in enumerate(targets):
            image = sum(
                kernels[(mask & other).bit_count()] * vector[column]
                for column, other in enumerate(targets)
            )
            assert image == expected * vector[row]


def main() -> None:
    for r in range(4, 36):
        b = 2 * r + 1
        k = r - 2
        target_count = choose(b, k)
        trace = Fraction()
        for j in range(k + 1):
            eigenvalue = theta(r, j)
            assert eigenvalue >= 0
            dimension = choose(b, j) - choose(b, j - 1)
            trace += dimension * eigenvalue
        assert trace == b

        top_dimension = choose(b, k) - choose(b, k - 1)
        assert top_dimension == Fraction(6 * target_count, r + 4)
        assert theta(r, k) <= Fraction(b, top_dimension)
        assert target_count >= Fraction(2 ** (2 * r + 1), 7 * (r + 1))

    direct_eigenvector_audit(4)
    direct_eigenvector_audit(5)

    calibrations = {}
    for r in (4, 5):
        b = 2 * r + 1
        k = r - 2
        target_count = choose(b, k)
        marginal = Fraction(b, target_count)
        for j in range(2, k + 1):
            calibrations[r, j] = theta(r, j) / (marginal * marginal)
    assert calibrations == {
        (4, 2): Fraction(4),
        (5, 2): Fraction(180, 7),
        (5, 3): Fraction(75, 7),
    }

    print(
        "PASS depth-two Fisher-scale obstruction: "
        "exact orbit eigenvalues, harmonic action, trace, exponential top module, "
        f"calibrations={calibrations}"
    )


if __name__ == "__main__":
    main()
