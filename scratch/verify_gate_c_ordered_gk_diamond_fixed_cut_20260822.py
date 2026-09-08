#!/usr/bin/env python3
"""Finite audit for the ordered-GK diamond fixed-cut obstruction."""

from collections import Counter
from itertools import combinations
from math import comb


def catalan(index):
    return comb(2 * index, index) // (index + 1)


def mask_of(items):
    mask = 0
    for item in items:
        mask |= 1 << item
    return mask


def bracket(mask, n):
    stack = []
    unpaired_zeros = []
    for position in range(n):
        if mask & (1 << position):
            stack.append(position)
        elif stack:
            stack.pop()
        else:
            unpaired_zeros.append(position)
    return tuple(unpaired_zeros), tuple(stack)


def gk_central_flags(b):
    n = 2 * b
    flags = []
    for chosen in combinations(range(n), b):
        middle = mask_of(chosen)
        zeros, ones = bracket(middle, n)
        if not zeros:
            continue
        p, q = ones[0], zeros[-1]
        lower = middle ^ (1 << p)
        upper = middle | (1 << q)
        flags.append((lower, middle, upper, p, q))
    assert len(flags) == comb(n, b - 1)
    return flags


def audit_gk_arc_invariant(b):
    n = 2 * b
    flags = gk_central_flags(b)
    multiplicity = Counter()
    degree = Counter()

    for lower, middle, upper, p, q in flags:
        assert q < p
        assert (p - q) % 2 == 1
        assert p % 2 != q % 2
        assert upper ^ lower == (1 << p) | (1 << q)

        # Every individual Boolean-diamond switch keeps L,U and reverses
        # the ordered coordinate arc.
        alternate = lower | (1 << q)
        assert alternate.bit_count() == b
        assert lower & alternate == lower
        assert alternate & upper == alternate
        new_p = (alternate ^ lower).bit_length() - 1
        new_q = (upper ^ alternate).bit_length() - 1
        assert (new_p, new_q) == (q, p)
        assert new_p % 2 != new_q % 2

        multiplicity[(p, q)] += 1
        degree[p] += 1
        degree[q] += 1

    for p in range(n):
        for q in range(n):
            if p > q and (p - q) % 2 == 1:
                a = (p - q - 1) // 2
                expected = catalan(a) * catalan(b - 1 - a)
            else:
                expected = 0
            assert multiplicity[(p, q)] == expected

    assert all(degree[coordinate] == catalan(b) for coordinate in range(n))
    assert sum(degree.values()) == 2 * len(flags)


def template_index_sets(b, phase):
    n = 2 * b
    for packet in range(b):
        offset = (phase + packet * (b + 1)) % n
        for time in range(1, b):
            indices = tuple(
                (offset + value) % n
                for value in (*range(time, b), *range(b + 1, b + time + 1))
            )
            start = (offset + b + time) % n
            yield packet, time, indices, start


def audit_edge_multiplicity_and_alternating_layers(b):
    n = 2 * b
    h = (b - 1) // 2
    for phase in (0, 1):
        starts = Counter()
        for _, _, indices, start in template_index_sets(b, phase):
            assert len(indices) == len(set(indices)) == b
            starts[start] += 1
            # In an alternating Hamilton listing, index parity is shore.
            expected_even = h + 1 - phase
            assert sum(index % 2 == 0 for index in indices) == expected_even
        assert len(starts) == n
        assert set(starts.values()) == {h}


def audit_interval_discrepancy(b):
    n = 2 * b
    for plus_positions in combinations(range(n), b):
        plus = set(plus_positions)
        sigma = tuple(1 if index in plus else -1 for index in range(n))
        defects = sum(
            sigma[index] == sigma[(index + 1) % n] for index in range(n)
        )

        for start in range(n):
            total = 0
            for length in range(1, n + 1):
                total += sigma[(start + length - 1) % n]
                assert abs(total) <= defects + 1

        for phase in (0, 1):
            for _, _, indices, _ in template_index_sets(b, phase):
                assert abs(sum(sigma[index] for index in indices)) <= defects + 2


def audit_band_counts(b):
    n = 2 * b
    h = (b - 1) // 2
    histogram = Counter()
    for chosen in combinations(range(n), b):
        a = sum(position % 2 == 0 for position in chosen)
        histogram[a] += 1
    assert histogram == Counter({a: comb(b, a) ** 2 for a in range(b + 1)})

    for bandwidth in range(0, b + 1):
        actual = sum(
            count for a, count in histogram.items()
            if abs(2 * a - b) <= bandwidth + 2
        )
        formula = sum(
            comb(b, a) ** 2 for a in range(b + 1)
            if abs(2 * a - b) <= bandwidth + 2
        )
        assert actual == formula
        assert actual <= (bandwidth + 3) * comb(b, h) ** 2


def main():
    for b in range(2, 11):
        audit_gk_arc_invariant(b)

    for b in range(3, 16, 2):
        audit_edge_multiplicity_and_alternating_layers(b)

    for b in range(3, 10, 2):
        audit_interval_discrepancy(b)
        audit_band_counts(b)

    print("PASS: ordered-GK fixed cut and exact arc multiplicities for 2<=b<=10")
    print("PASS: every individual central diamond reverses one fixed cross-cut pair")
    print("PASS: coherent edge multiplicities and alternating layers for odd 3<=b<=15")
    print("PASS: exhaustive balanced-word discrepancy and band counts for odd 3<=b<=9")


if __name__ == "__main__":
    main()
