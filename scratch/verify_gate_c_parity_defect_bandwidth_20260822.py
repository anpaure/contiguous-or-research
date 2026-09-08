#!/usr/bin/env python3
"""Finite audit for the Gate-C parity-defect bandwidth obstruction."""

from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations
from math import comb, factorial


def mask_of(items):
    mask = 0
    for item in items:
        mask |= 1 << item
    return mask


def bracket(mask, n):
    stack = []
    zeros = []
    for position in range(n):
        if mask & (1 << position):
            stack.append(position)
        elif stack:
            stack.pop()
        else:
            zeros.append(position)
    return tuple(zeros), tuple(stack)


def repaired_factor(b):
    n = 2 * b
    flags = set()
    for chosen in combinations(range(n), b):
        middle = mask_of(chosen)
        zeros, ones = bracket(middle, n)
        if not zeros:
            continue
        p, q = ones[0], zeros[-1]
        lower = middle ^ (1 << p)
        upper = middle | (1 << q)
        if (p, q) == (n - 1, 0):
            middle = lower | 1
        flags.add((lower, middle, upper))
    assert len(flags) == comb(n, b - 1)
    return flags


def template_flags(cycle, b, phase):
    n = 2 * b
    flags = []
    for s in range(b):
        offset = (phase + s * (b + 1)) % n
        for t in range(1, b):
            indices = [
                (offset + u) % n
                for u in (*range(t, b), *range(b + 1, b + t + 1))
            ]
            middle = mask_of(cycle[index] for index in indices)
            r = (offset + b + t) % n
            p = cycle[r]
            q = cycle[(r + 1) % n]
            flags.append((middle ^ (1 << p), middle, middle | (1 << q)))
    return tuple(flags)


def same_parity_edges(cycle):
    return sum(
        cycle[index] % 2 == cycle[(index + 1) % len(cycle)] % 2
        for index in range(len(cycle))
    )


def audit_parity_support(b):
    factor = repaired_factor(b)
    for lower, middle, upper in factor:
        p = (middle ^ lower).bit_length() - 1
        q = (upper ^ middle).bit_length() - 1
        assert p % 2 != q % 2


def audit_discrepancy(b):
    n = 2 * b
    # Every balanced parity word is realizable by some Hamilton listing.
    for plus_positions in combinations(range(n), b):
        plus = set(plus_positions)
        sigma = [1 if index in plus else -1 for index in range(n)]
        defects = sum(
            sigma[index] == sigma[(index + 1) % n] for index in range(n)
        )

        # Exhaust all cyclic intervals.
        for start in range(n):
            total = 0
            for length in range(1, n + 1):
                total += sigma[(start + length - 1) % n]
                assert abs(total) <= defects + 1

        # Exhaust all coherent middle templates.
        for phase in (0, 1):
            for s in range(b):
                offset = (phase + s * (b + 1)) % n
                for t in range(1, b):
                    indices = [
                        (offset + u) % n
                        for u in (*range(t, b), *range(b + 1, b + t + 1))
                    ]
                    assert abs(sum(sigma[index] for index in indices)) <= (
                        defects + 2
                    )


def alternating_cycles(b):
    evens = tuple(range(2, 2 * b, 2))
    odds = tuple(range(1, 2 * b, 2))
    for odd_order in permutations(odds):
        for even_order in permutations(evens):
            cycle = [0]
            for index in range(b):
                cycle.append(odd_order[index])
                if index < b - 1:
                    cycle.append(even_order[index])
            yield tuple(cycle)


def flag_type(flag, b):
    lower, middle, upper = flag
    p = (middle ^ lower).bit_length() - 1
    q = (upper ^ middle).bit_length() - 1
    assert p % 2 != q % 2
    even_count = sum((middle >> value) & 1 for value in range(0, 2 * b, 2))
    return even_count, p % 2


def audit_alternating_orbit(b):
    h = (b - 1) // 2
    qsize = b * (b - 1)
    support_count = factorial(b) * factorial(b - 1)
    assert sum(1 for _ in alternating_cycles(b)) == support_count

    degrees = [Counter(), Counter()]
    middles = [set(), set()]
    for cycle in alternating_cycles(b):
        assert same_parity_edges(cycle) == 0
        for phase in (0, 1):
            flags = template_flags(cycle, b, phase)
            assert len(flags) == len(set(flags)) == qsize
            type_histogram = Counter(flag_type(flag, b) for flag in flags)
            expected_a = h + 1 - phase
            assert type_histogram == Counter({
                (expected_a, 0): qsize // 2,
                (expected_a, 1): qsize // 2,
            })
            degrees[phase].update(flags)
            middles[phase].update(flag[1] for flag in flags)

    central_layer_size = comb(b, h) ** 2
    for phase in (0, 1):
        expected_a = h + 1 - phase
        assert len(middles[phase]) == central_layer_size
        assert all(
            sum((middle >> value) & 1 for value in range(0, 2 * b, 2))
            == expected_a
            for middle in middles[phase]
        )
        expected_flag_count = (
            comb(b, expected_a) ** 2
            * (expected_a ** 2 + (b - expected_a) ** 2)
        )
        assert len(degrees[phase]) == expected_flag_count
        for flag, degree in degrees[phase].items():
            a, p_parity = flag_type(flag, b)
            denominator = (
                comb(b, a) ** 2
                * (a ** 2 if p_parity == 0 else (b - a) ** 2)
            )
            expected_degree = support_count * (qsize // 2) // denominator
            assert degree == expected_degree

    factor = repaired_factor(b)
    actual_total = sum(
        degrees[phase][flag]
        for phase in (0, 1)
        for flag in factor
    )
    actual_mean = Fraction(actual_total, 2 * support_count)

    g = Counter(flag_type(flag, b) for flag in factor)
    formula_mean = Fraction(0)
    for phase in (0, 1):
        a = h + 1 - phase
        formula_mean += Fraction(
            qsize * g[(a, 0)],
            4 * comb(b, a) ** 2 * a ** 2,
        )
        formula_mean += Fraction(
            qsize * g[(a, 1)],
            4 * comb(b, a) ** 2 * (b - a) ** 2,
        )
    assert actual_mean == formula_mean
    assert actual_mean <= Fraction(2 * b, b - 1)
    return actual_mean


def audit_overlap_bound(b):
    n = 2 * b
    factor = repaired_factor(b)
    h = (b - 1) // 2
    qsize = b * (b - 1)
    if b == 3:
        cycles = [(0, *tail) for tail in permutations(range(1, n))]
    else:
        cycles = [
            tuple(range(n)),
            tuple(reversed(range(n))),
            tuple(range(0, n, 2)) + tuple(range(1, n, 2)),
        ]
    for cycle in cycles:
        assert len(set(cycle)) == n
        defects = same_parity_edges(cycle)
        for phase in (0, 1):
            overlap = sum(
                flag in factor for flag in template_flags(cycle, b, phase)
            )
            assert overlap <= qsize - h * defects


def audit_band_count(b):
    h = (b - 1) // 2
    n = 2 * b
    middle_masks = [
        mask_of(chosen) for chosen in combinations(range(n), b)
    ]
    for K in range(0, min(b, 8)):
        actual = sum(
            abs(
                2 * sum((middle >> value) & 1 for value in range(0, n, 2))
                - b
            ) <= K + 2
            for middle in middle_masks
        )
        formula = sum(
            comb(b, a) ** 2
            for a in range(b + 1)
            if abs(2 * a - b) <= K + 2
        )
        assert actual == formula
        assert formula <= (K + 3) * comb(b, h) ** 2


def main():
    for b in range(2, 9):
        audit_parity_support(b)
    for b in range(2, 9):
        audit_discrepancy(b)
    for b in range(3, 10, 2):
        audit_band_count(b)
    means = {}
    for b in (3, 5):
        means[b] = audit_alternating_orbit(b)
    for b in (3, 5, 7, 9):
        audit_overlap_bound(b)

    print("PASS: D* parity support for 2<=b<=8")
    print("PASS: all balanced parity words and coherent templates for 2<=b<=8")
    print("PASS: alternating orbit degrees and means", means)
    print("PASS: universal overlap loss for exact b=3 and deterministic b=5,7,9 cases")


if __name__ == "__main__":
    main()
