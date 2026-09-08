#!/usr/bin/env python3
"""Finite audit for general antipodal-wreath Gate-C reductions."""

import sys
from collections import Counter
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


def signed_permutations(b):
    n = 2 * b
    for alpha in permutations(range(b)):
        for orientation in range(1 << b):
            pi = [0] * n
            for residue in range(b):
                pi[residue] = alpha[residue] + (
                    b if (orientation >> residue) & 1 else 0
                )
                pi[residue + b] = (pi[residue] + b) % n
            yield tuple(pi), alpha, orientation


def canonical_flag(pi, b, r, t):
    n = 2 * b
    middle = mask_of(pi[(r + offset) % n] for offset in range(b + 1) if offset != t)
    p = pi[r]
    q = pi[(r - 1) % n]
    return middle ^ (1 << p), middle, middle | (1 << q)


def prefix_member(pi, b, r, t):
    n = 2 * b
    _, middle, _ = canonical_flag(pi, b, r, t)
    p = pi[r]
    q = pi[(r - 1) % n]
    heights = [0]
    for offset in range(n):
        coordinate = (p + offset) % n
        heights.append(heights[-1] + (1 if middle & (1 << coordinate) else -1))
    assert heights[-1] == 0

    if q < p and (p, q) != (n - 1, 0):
        first_return = (q - p) % n + 1
        return (
            all(height > 0 for height in heights[1:first_return])
            and heights[first_return] == 0
            and all(height >= 0 for height in heights[first_return + 1 :])
        )
    if (p, q) == (0, n - 1):
        return all(height > 0 for height in heights[1:-1])
    return False


def phase_r_values(b, phase, t):
    n = 2 * b
    return tuple(
        (-phase - stage * (b + 1) - b - t) % n for stage in range(b)
    )


def audit_prefix_and_phase_partition():
    for b in (3, 5):
        factor = repaired_factor(b)
        for pi, _, _ in signed_permutations(b):
            for r in range(2 * b):
                for t in range(1, b):
                    assert prefix_member(pi, b, r, t) == (
                        canonical_flag(pi, b, r, t) in factor
                    )
            for t in range(1, b):
                phase_zero = set(phase_r_values(b, 0, t))
                phase_one = set(phase_r_values(b, 1, t))
                assert len(phase_zero) == len(phase_one) == b
                assert not phase_zero & phase_one
                assert phase_zero | phase_one == set(range(2 * b))
    print("PASS: exact prefix test and phase partition for full b=3,5 wreaths")


def cyclic_transitions(word):
    return sum(word[index] != word[index - 1] for index in range(len(word)))


def audit_parity_transition_formula():
    for b in (3, 5):
        for pi, alpha, orientation in signed_permutations(b):
            c_word = tuple(
                (alpha[x] + ((orientation >> x) & 1) + x) % 2
                for x in range(b)
            )
            same_edges = sum(
                pi[r] % 2 == pi[(r - 1) % (2 * b)] % 2
                for r in range(2 * b)
            )
            assert same_edges == 2 * cyclic_transitions(c_word)
    print("PASS: exact sign/parity transition identity for full b=3,5 wreaths")


def successor_breaks(alpha):
    b = len(alpha)
    return sum(
        alpha[index] != (alpha[index - 1] + 1) % b for index in range(b)
    )


def audit_block_count():
    for b in range(2, 10):
        histogram = Counter(successor_breaks(alpha) for alpha in permutations(range(b)))
        for breaks, count in histogram.items():
            if breaks == 0:
                assert count == b
            else:
                assert count <= b * comb(b, breaks) * factorial(breaks - 1)
    print("PASS: cyclic successor-block count bound for 2<=b<=9")


def wreath_spectrum(b):
    factor = repaired_factor(b)
    histogram = Counter()
    maximizers = []
    maximum = -1
    for pi, alpha, orientation in signed_permutations(b):
        total = sum(
            canonical_flag(pi, b, r, t) in factor
            for r in range(2 * b)
            for t in range(1, b)
        )
        histogram[total] += 1
        if total > maximum:
            maximum = total
            maximizers = [(alpha, orientation)]
        elif total == maximum:
            maximizers.append((alpha, orientation))
    return maximum, maximizers, histogram


def audit_spectrum():
    maximum, maximizers, histogram = wreath_spectrum(5)
    assert maximum == 30
    assert len(maximizers) == 10
    assert max(value for value in histogram if value < maximum) == 12
    print("PASS: full b=5 wreath spectrum (max 30 on 10 rotations; next 12)")

    if "--full-b7" in sys.argv:
        maximum, maximizers, histogram = wreath_spectrum(7)
        assert maximum == 70
        assert len(maximizers) == 14
        assert max(value for value in histogram if value < maximum) == 42
        print("PASS: full b=7 wreath spectrum (max 70 on 14 rotations; next 42)")


if __name__ == "__main__":
    audit_prefix_and_phase_partition()
    audit_parity_transition_formula()
    audit_block_count()
    audit_spectrum()
