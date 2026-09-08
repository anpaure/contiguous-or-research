#!/usr/bin/env python3
"""Finite audit for the fixed-anchor Boolean square lattice theorem."""

from __future__ import annotations

from collections import Counter
from itertools import combinations

from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form


PRIMES = (2, 3, 5, 101, 1_000_003)


def mod_rank(columns, rows, prime):
    basis = {}
    for column in columns:
        vector = {i: value % prime for i, value in column.items() if value % prime}
        while vector:
            pivot = min(vector)
            if pivot not in basis:
                inverse = pow(vector[pivot], -1, prime)
                vector = {
                    i: (value * inverse) % prime
                    for i, value in vector.items()
                    if (value * inverse) % prime
                }
                basis[pivot] = vector
                break
            coefficient = vector[pivot]
            row = basis[pivot]
            for i, value in row.items():
                updated = (vector.get(i, 0) - coefficient * value) % prime
                if updated:
                    vector[i] = updated
                else:
                    vector.pop(i, None)
    return len(basis)


def anchored_columns(n, k):
    infinity = n - 1
    ground = tuple(range(n - 1))
    targets = tuple(combinations(range(n), k))
    target_id = {target: i for i, target in enumerate(targets)}
    columns = []
    for core in combinations(ground, k - 2):
        outside = tuple(x for x in ground if x not in core)
        for a in outside:
            rest = tuple(x for x in outside if x != a)
            for b, c in combinations(rest, 2):
                sets = (
                    tuple(sorted(core + (a, b))),
                    tuple(sorted(core + (a, c))),
                    tuple(sorted(core + (infinity, b))),
                    tuple(sorted(core + (infinity, c))),
                )
                columns.append(
                    {
                        target_id[sets[0]]: 1,
                        target_id[sets[1]]: -1,
                        target_id[sets[2]]: -1,
                        target_id[sets[3]]: 1,
                    }
                )
    return targets, columns


def incidence_rank(n, k, prime):
    columns = []
    for target in combinations(range(n), k):
        columns.append({i: 1 for i in target})
    return mod_rank(columns, n, prime)


def audit_case(n, k, do_snf):
    targets, columns = anchored_columns(n, k)
    expected = len(targets) - n
    ranks = tuple(mod_rank(columns, len(targets), p) for p in PRIMES)
    assert ranks == (expected,) * len(PRIMES), (n, k, ranks, expected)
    for p in PRIMES:
        expected_incidence_rank = n - 1 if k % p == 0 else n
        assert incidence_rank(n, k, p) == expected_incidence_rank, (
            n,
            k,
            p,
            expected_incidence_rank,
        )

    invariants = None
    if do_snf:
        matrix = Matrix(
            len(targets),
            len(columns),
            lambda i, j: columns[j].get(i, 0),
        )
        diagonal = smith_normal_form(matrix, domain=ZZ)
        invariants = []
        for i in range(min(diagonal.rows, diagonal.cols)):
            value = abs(int(diagonal[i, i]))
            if value:
                invariants.append(value)
        assert len(invariants) == expected, (n, k, len(invariants), expected)
        assert Counter(invariants) == Counter({1: expected}), (n, k, Counter(invariants))
    return {
        "n": n,
        "k": k,
        "targets": len(targets),
        "anchored_squares": len(columns),
        "rank": expected,
        "snf": None if invariants is None else Counter(invariants),
    }


def main():
    rows = []
    for n in range(4, 11):
        for k in range(2, n - 1):
            rows.append(audit_case(n, k, do_snf=n <= 7))
    print(
        "FIXED_ANCHOR_BOOLEAN_SQUARE_LATTICE_AUDIT_PASS",
        {
            "cases": len(rows),
            "n_max": max(row["n"] for row in rows),
            "snf_cases": sum(row["snf"] is not None for row in rows),
            "max_targets": max(row["targets"] for row in rows),
            "primes": PRIMES,
        },
    )


if __name__ == "__main__":
    main()
