#!/usr/bin/env python3
"""Finite audit for the Hamming-coset coherent-tour bank resolution."""

from collections import Counter
from math import ceil, log2

from verify_gate_c_all_pairing_coherent_tour_orbit_20260822 import (
    ordered_tour_support,
)


def syndrome(word, columns):
    out = 0
    for i, column in enumerate(columns):
        if word >> i & 1:
            out ^= column
    return out


def audit_b(b):
    r = ceil(log2(b + 1))
    columns = tuple(range(1, b + 1))
    assert max(columns) < 1 << r
    order = tuple(range(b))

    banks = [[] for _ in range(1 << r)]
    for state in range(1 << b):
        banks[syndrome(state, columns)].append(
            ordered_tour_support(b, order, state)
        )

    expected_states = 1 << (b - r)
    multiplicity = Counter()
    for bank in banks:
        assert len(bank) == expected_states
        seen = set()
        for tour in bank:
            assert not (seen & set(tour))
            seen.update(tour)
        assert len(seen) == b * (b - 1) * expected_states
        multiplicity.update(seen)

    expected_stratum = b * (b - 1) * 2 ** (b - 2)
    assert len(multiplicity) == expected_stratum
    assert set(multiplicity.values()) == {4}
    print(
        f"PASS: b={b} r={r} cosets={len(banks)} "
        f"bank_tours={expected_states} stratum={expected_stratum}"
    )


def audit():
    for b in (3, 5, 7, 9):
        audit_b(b)


if __name__ == "__main__":
    audit()
