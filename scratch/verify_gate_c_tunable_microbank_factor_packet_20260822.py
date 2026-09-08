#!/usr/bin/env python3
"""Finite algebra checks for the tunable-microbank factor-packet note."""

from fractions import Fraction
from itertools import combinations


def factorization(b: int):
    n = 2 * b - 1
    inf = n
    factors = []
    for a in range(n):
        edges = {tuple(sorted((inf, a)))}
        for j in range(1, b):
            edges.add(tuple(sorted(((a + j) % n, (a - j) % n))))
        factors.append(edges)
    return factors


def check_factorization(b: int) -> None:
    factors = factorization(b)
    vertices = range(2 * b)
    all_edges = {tuple(e) for e in combinations(vertices, 2)}
    seen = set()
    for edges in factors:
        assert len(edges) == b
        flat = [x for edge in edges for x in edge]
        assert len(flat) == len(set(flat)) == 2 * b
        assert seen.isdisjoint(edges)
        seen |= edges
    assert seen == all_edges


def check_profiles(b: int, c: int) -> None:
    q = b * (b - 1)
    m = q * c
    same_both = c * (b - 1)
    diff_both = Fraction(c * (b - 2) * (b + 1), 4)
    same_xor = Fraction(b - 2, b)
    diff_xor = Fraction(1, 2) + Fraction(1, b * (b - 1))
    delta = Fraction(b * b - 5 * b + 2, 2 * b * (b - 1))

    assert same_xor - diff_xor == delta
    assert diff_xor + delta / (2 * b - 1) == Fraction(b, 2 * b - 1)

    packet_pair_count = same_both + (2 * b - 2) * diff_both
    assert packet_pair_count == Fraction(c * b * (b - 1) ** 2, 2)
    assert (2 * b - 1) * m * Fraction(b - 1, 2 * (2 * b - 1)) == packet_pair_count


def main() -> None:
    for b in range(5, 32, 2):
        check_factorization(b)
        # A power of two with at least two state bits, as in the theorem.
        check_profiles(b, 8)
    print("verified: round-robin factorization and exact profile identities")


if __name__ == "__main__":
    main()
