#!/usr/bin/env python3
"""Finite arithmetic/rank audit for the abstract C8 current theorem.

The proof in the theorem note is integral and does not depend on this audit.
Intended execution: H100 only.
"""

from __future__ import annotations

import argparse
import math
from itertools import combinations


def catalan(r: int) -> int:
    return math.comb(2 * r, r) // (r + 1)


def modular_rank(columns, row_count: int, prime: int) -> int:
    basis = {}
    for column in columns:
        vector = {row: value % prime for row, value in column.items()
                  if value % prime}
        while vector:
            pivot = min(vector)
            if pivot not in basis:
                inverse = pow(vector[pivot], prime - 2, prime)
                basis[pivot] = {
                    row: value * inverse % prime
                    for row, value in vector.items()
                }
                break
            scale = vector[pivot]
            for row, value in basis[pivot].items():
                new_value = (vector.get(row, 0) - scale * value) % prime
                if new_value:
                    vector[row] = new_value
                elif row in vector:
                    del vector[row]
    assert all(0 <= pivot < row_count for pivot in basis)
    return len(basis)


def square_columns(n: int, k: int):
    targets = tuple(combinations(range(n), k))
    index = {target: position for position, target in enumerate(targets)}
    answers = {}
    for core_tuple in combinations(range(n), k - 2):
        core = set(core_tuple)
        outside = tuple(point for point in range(n) if point not in core)
        for four in combinations(outside, 4):
            a, b, c, d = four
            for pairing in (
                ((a, b), (c, d)),
                ((a, c), (b, d)),
                ((a, d), (b, c)),
            ):
                (u, v), (x, y) = pairing
                sets = (
                    tuple(sorted(core | {u, x})),
                    tuple(sorted(core | {v, y})),
                    tuple(sorted(core | {u, y})),
                    tuple(sorted(core | {v, x})),
                )
                column = {
                    index[sets[0]]: 1,
                    index[sets[1]]: 1,
                    index[sets[2]]: -1,
                    index[sets[3]]: -1,
                }
                key = tuple(sorted(column.items()))
                negative = tuple(sorted((row, -value)
                                        for row, value in column.items()))
                answers[min(key, negative)] = column
    columns = tuple(answers.values())
    for column in columns:
        assert sum(column.values()) == 0
        for point in range(n):
            assert sum(value for row, value in column.items()
                       if point in targets[row]) == 0
    return len(targets), columns


def audit_lattices(n_max: int):
    cases = 0
    for n in range(4, n_max + 1):
        for k in range(2, n - 1):
            target_count, columns = square_columns(n, k)
            expected = target_count - n
            ranks = {
                prime: modular_rank(columns, target_count, prime)
                for prime in (2, 3, 5, 1_000_003)
            }
            assert set(ranks.values()) == {expected}, (n, k, ranks, expected)
            cases += 1
    return cases


def audit_wreath_arithmetic(r_max: int):
    for r in range(2, r_max + 1):
        n = 2 * r + 1
        k = r - 1
        m = catalan(r)
        A = n * m
        N = math.comb(n, k)
        E = A - N
        d = k * m - math.comb(n - 1, k - 1)
        assert A == math.comb(n, r)
        assert E * (r + 2) == 2 * n * m
        assert d * (r + 2) == 2 * k * m
        assert n * d == k * E
        assert 0 <= E <= N


def main(n_max: int, r_max: int):
    cases = audit_lattices(n_max)
    audit_wreath_arithmetic(r_max)
    print("ABSTRACT_C8_CURRENT_LATTICE_AUDIT_PASS", {
        "lattice_cases": cases,
        "n_max": n_max,
        "wreath_r_max": r_max,
        "primes": (2, 3, 5, 1_000_003),
    })


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--n-max", type=int, default=10)
    parser.add_argument("--r-max", type=int, default=100)
    arguments = parser.parse_args()
    main(arguments.n_max, arguments.r_max)
