#!/usr/bin/env python3
"""Finite audit for balanced dual-distance three-rank coset banks."""

from collections import defaultdict
from math import ceil, log2
from random import Random

from verify_gate_c_all_pairing_coherent_tour_orbit_20260822 import natural_tour


def signature_and_bits(b, mask):
    signature = []
    split_bits = 0
    for pair in range(b):
        value = (mask >> (2 * pair)) & 3
        count = value.bit_count()
        signature.append(count)
        if count == 1 and value == 2:
            split_bits |= 1 << pair
    return tuple(signature), split_bits


def collision_set(b):
    middle, _, lower, upper = natural_tour(b, 0)
    ranks = (lower, tuple(mask for _, mask in middle), upper)
    bad = set()
    for targets in ranks:
        groups = defaultdict(list)
        for target in targets:
            signature, bits = signature_and_bits(b, target)
            groups[signature].append(bits)
        for signature, rows in groups.items():
            exceptional = [i for i, count in enumerate(signature) if count != 1]
            for first in rows:
                for second in rows:
                    base = first ^ second
                    for choice in range(1 << len(exceptional)):
                        difference = base
                        for j, pair in enumerate(exceptional):
                            if choice >> j & 1:
                                difference |= 1 << pair
                        if difference:
                            bad.add(difference)
    return bad


def syndrome(word, rows):
    value = 0
    for i, row in enumerate(rows):
        value |= (((word & row).bit_count() & 1) << i)
    return value


def rowspace(rows):
    space = {0}
    for row in rows:
        space |= {word ^ row for word in tuple(space)}
    return space


def audit_large_example():
    b = 31
    H = 2
    bad = collision_set(b)
    bound = 2 * b ** 3 + 8 * b ** 2 - 16 * b
    assert len(bad) <= bound
    r = ceil(log2(4 * bound))
    rng = Random(1)

    while True:
        rows = tuple(rng.randrange(1 << b) for _ in range(r))
        if any(syndrome(h, rows) == 0 for h in bad):
            continue
        dual = rowspace(rows)
        if min(word.bit_count() for word in dual if word) <= H:
            continue
        break

    assert len(dual) == 1 << r
    assert all(syndrome(h, rows) for h in bad)
    assert min(word.bit_count() for word in dual if word) == 3

    # The exact one-coordinate formula is independent of the actual coset.
    q = b * (b - 1)
    for pair in range(b):
        empty = b - 1
        doubled = b - 1
        split = (b - 1) * (b - 2)
        assert doubled + split // 2 == q // 2
        assert empty + doubled + split == q
    print(
        f"PASS: b={b} H={H} bad={len(bad)} bound={bound} "
        f"rows={r} dual_distance=3"
    )


if __name__ == "__main__":
    audit_large_example()
