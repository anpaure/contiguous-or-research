#!/usr/bin/env python3
"""Finite audit for the three-rank linear-coset bank resolution."""

from collections import Counter, defaultdict
from math import ceil, log2
from random import Random

from verify_gate_c_all_pairing_coherent_tour_orbit_20260822 import natural_tour


def rank_targets(b, state):
    middle, _, lower, upper = natural_tour(b, state)
    return {
        b - 1: tuple(lower),
        b: tuple(mask for _, mask in middle),
        b + 1: tuple(upper),
    }


def collision_set(b, targets):
    base = targets[0]
    bad = set()
    for h in range(1, 1 << b):
        if any(set(base[rank]) & set(targets[h][rank])
               for rank in (b - 1, b, b + 1)):
            bad.add(h)
    return bad


def syndrome(x, rows):
    out = 0
    for i, row in enumerate(rows):
        out |= (((x & row).bit_count() & 1) << i)
    return out


def find_rows(b, bad):
    bound = 2 * b ** 3 + 8 * b ** 2 - 16 * b
    r = min(b, ceil(log2(2 * bound)))
    if r == b:
        return tuple(1 << i for i in range(b))
    rng = Random(10_000 + b)
    while True:
        rows = tuple(rng.randrange(1 << b) for _ in range(r))
        if all(syndrome(h, rows) for h in bad):
            return rows


def audit_b(b):
    targets = [rank_targets(b, x) for x in range(1 << b)]
    bad = collision_set(b, targets)
    bound = 2 * b ** 3 + 8 * b ** 2 - 16 * b
    assert len(bad) <= bound
    assert all((1 << i) in bad for i in range(b))
    assert all(((1 << i) | (1 << j)) in bad
               for i in range(b) for j in range(i))

    rows = find_rows(b, bad)
    assert all(syndrome(h, rows) for h in bad)
    banks = defaultdict(list)
    for x in range(1 << b):
        banks[syndrome(x, rows)].append(x)

    middle_multiplicity = Counter()
    for states in banks.values():
        for rank in (b - 1, b, b + 1):
            seen = set()
            for x in states:
                row = targets[x][rank]
                assert len(row) == len(set(row)) == b * (b - 1)
                assert not (seen & set(row))
                seen.update(row)
        for x in states:
            middle_multiplicity.update(targets[x][b])

    expected_stratum = b * (b - 1) * 2 ** (b - 2)
    assert len(middle_multiplicity) == expected_stratum
    assert set(middle_multiplicity.values()) == {4}
    minimum = min(map(len, banks.values()))
    rb = min(b, ceil(log2(2 * bound)))
    assert minimum >= 2 ** (b - rb)
    print(
        f"PASS: b={b} bad={len(bad)} rows={len(rows)} "
        f"cosets={len(banks)} bank_size={minimum}"
    )


def audit():
    for b in (3, 5, 7, 9, 11):
        audit_b(b)


if __name__ == "__main__":
    audit()
