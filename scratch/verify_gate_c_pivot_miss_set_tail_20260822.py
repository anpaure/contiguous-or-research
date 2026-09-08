#!/usr/bin/env python3
"""Exact finite audit for the direct pivot miss-set tail."""

from collections import Counter
from itertools import permutations
from math import comb, factorial

from verify_gate_c_single_root_ballot_law_and_moment_gate_20260822 import good_count


def elementary_symmetric(values):
    coefficients = [1] + [0] * len(values)
    for value in values:
        for degree in range(len(values), 0, -1):
            coefficients[degree] += value * coefficients[degree - 1]
    return coefficients


def audit():
    for k in (3, 5, 7, 9):
        e = (k - 1) // 2
        pool_sizes = []
        for position in range(k):
            if position % 2 == 0:
                pool_sizes.append(e + 1 - position // 2)
            else:
                pool_sizes.append(e - position // 2)
        assert sum(pool_sizes) == (e + 1) ** 2
        assert factorial(e + 1) * factorial(e) == __import__("math").prod(pool_sizes)
        symmetric = elementary_symmetric(pool_sizes)

        normalized_histogram = Counter(
            good_count((0,) + tail) for tail in permutations(range(1, k))
        )
        for misses in range(k):
            exact_linear_count = k * sum(
                count for good, count in normalized_histogram.items()
                if good >= k - misses
            )
            exact_bound = (comb(k, e + 1) * 2 ** (k - misses)
                           * symmetric[misses])
            closed_bound = (4 ** k * ((e + 1) ** 2 / 2) ** misses
                            / factorial(misses))
            assert exact_linear_count <= exact_bound
            assert exact_bound <= closed_bound + 1e-9
        print(f"PASS: K={k} exact census and every miss-set bound")


if __name__ == "__main__":
    audit()
