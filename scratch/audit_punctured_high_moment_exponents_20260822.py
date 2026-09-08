#!/usr/bin/env python3
"""Algebra audit for the fixed high-moment polymer argument."""

from fractions import Fraction
from itertools import combinations


def prufer_trees(j: int):
    if j == 2:
        yield {(0, 1)}
        return
    from itertools import product

    for code in product(range(j), repeat=j - 2):
        degree = [1] * j
        for x in code:
            degree[x] += 1
        edges = set()
        for x in code:
            leaf = next(i for i, d in enumerate(degree) if d == 1)
            edges.add(tuple(sorted((leaf, x))))
            degree[leaf] -= 1
            degree[x] -= 1
        leaves = [i for i, d in enumerate(degree) if d == 1]
        edges.add(tuple(sorted(leaves)))
        yield edges


def audit_tree_probability(j: int) -> None:
    trees = list(prufer_trees(j))
    assert len(trees) == j ** (j - 2)
    counts = {edge: 0 for edge in combinations(range(j), 2)}
    for tree in trees:
        assert len(tree) == j - 1
        for edge in tree:
            counts[edge] += 1
    assert set(counts.values()) == {2 * len(trees) // j}


def audit_exponents(max_s: int = 30) -> None:
    for s in range(2, max_s + 1):
        alpha = Fraction(1, 6 * s)
        for j in range(3, 2 * s + 1):
            # Rooted first kernel term divided by rho^(j/2).
            rooted_first = (
                Fraction(1, 1)
                - Fraction(j, 2)
                + alpha * Fraction(3 * j * (j - 2), 2)
            )
            assert rooted_first <= 0

            # Rooted second kernel term divided by rho^(j/2).
            rooted_second = (
                Fraction(2, 1)
                - Fraction(3 * j, 2)
                + alpha * Fraction(j * (4 * j - 7), 2)
            )
            assert rooted_second < 0

            # Unrooted first/second kernel terms divided by (rx)^(-j/2).
            unrooted_first = (
                Fraction(1, 1)
                - Fraction(j, 2)
                + alpha * Fraction(j * (j - 2), 2)
            )
            unrooted_second = (
                Fraction(2, 1)
                - Fraction(3 * j, 2)
                + alpha * Fraction(j * (4 * j - 5), 2)
            )
            assert unrooted_first < 0
            assert unrooted_second < 0


def main() -> None:
    for j in range(2, 9):
        audit_tree_probability(j)
    audit_exponents()
    print("PUNCTURED_HIGH_MOMENT_EXPONENT_AUDIT_PASS")


if __name__ == "__main__":
    main()
