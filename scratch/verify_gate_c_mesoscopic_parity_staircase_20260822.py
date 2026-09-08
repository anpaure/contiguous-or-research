#!/usr/bin/env python3
"""Finite checks for the mesoscopic Gate-C parity staircase theorem."""

from collections import Counter
from itertools import permutations
from math import comb, exp, factorial


def alternating_word(b):
    return tuple(1 if index % 2 == 0 else -1 for index in range(2 * b))


def staircase_word(b, j):
    assert b % 2 == 1 and 4 * j <= b - 1
    word = list(alternating_word(b))
    for step in range(j):
        position = 4 * step + 1
        word[position] *= -1
        word[position + b] *= -1
    return tuple(word)


def template_occurrences(word):
    """Original (phase,stage,t) coherent-template census."""
    n = len(word)
    b = n // 2
    occurrences = []
    for phase in (0, 1):
        for stage in range(b):
            offset = (phase + stage * (b + 1)) % n
            for t in range(1, b):
                indices = tuple(
                    (offset + value) % n
                    for value in (*range(t, b), *range(b + 1, b + t + 1))
                )
                p = (offset + b + t) % n
                c = (offset + b) % n
                occurrences.append((p, c, indices))
    return occurrences


def endpoint_occurrences(word):
    """Endpoint p and deleted strict-interior point c census."""
    n = len(word)
    b = n // 2
    occurrences = []
    for p in range(n):
        interval = tuple((p - b + value) % n for value in range(b + 1))
        for c in interval[1:-1]:
            indices = tuple(index for index in interval if index != c)
            occurrences.append((p, c, indices))
    return occurrences


def same_edges(word):
    return sum(
        word[index] == word[(index + 1) % len(word)]
        for index in range(len(word))
    )


def level_census(word):
    n = len(word)
    b = n // 2
    census = Counter()
    for p in range(n):
        if word[p] == word[(p + 1) % n]:
            continue
        interval = [(p - b + value) % n for value in range(b + 1)]
        level = sum(word[index] for index in interval)
        census[level, word[p]] += 1
    return census


def brute_histogram(word):
    n = len(word)
    histogram = Counter()
    for p, c, indices in endpoint_occurrences(word):
        if word[p] == word[(p + 1) % n]:
            continue
        discrepancy = sum(word[index] for index in indices)
        histogram[discrepancy, word[p]] += 1
    return histogram


def formula_histogram(b, j):
    levels = Counter()
    levels[2 * j, 1] = (b - 4 * j + 3) // 2
    levels[2 * j, -1] = (b - 4 * j + 1) // 2
    levels[-2 * j, 1] = (b - 4 * j + 1) // 2
    levels[-2 * j, -1] = (b - 4 * j + 3) // 2
    for step in range(1, j):
        level = -2 * j + 4 * step
        levels[level, 1] = 2
        levels[level, -1] = 2

    histogram = Counter()
    for (level, endpoint_sign), count in levels.items():
        plus_interior = (b - 1 + level) // 2
        minus_interior = (b - 1 - level) // 2
        histogram[level - 1, endpoint_sign] += count * plus_interior
        histogram[level + 1, endpoint_sign] += count * minus_interior
    return levels, histogram


def audit_endpoint_bijection():
    for b in range(3, 16, 2):
        words = [alternating_word(b)]
        if b >= 5:
            words.append(staircase_word(b, 1))
        for word in words:
            original = Counter(template_occurrences(word))
            endpoint = Counter(endpoint_occurrences(word))
            assert original == endpoint
            assert len(original) == 2 * b * (b - 1)
    print("PASS: endpoint--deletion bijection for odd 3<=b<=15")


def audit_staircase_census():
    for b in range(5, 64, 2):
        for j in range(1, (b - 1) // 4 + 1):
            word = staircase_word(b, j)
            n = 2 * b
            assert sum(word) == 0
            assert all(word[(index + b) % n] == -word[index] for index in range(n))
            assert same_edges(word) == 4 * j

            expected_levels, expected_histogram = formula_histogram(b, j)
            assert level_census(word) == expected_levels
            assert brute_histogram(word) == expected_histogram

            reached = {discrepancy for discrepancy, _ in expected_histogram}
            assert reached == set(range(-2 * j - 1, 2 * j + 2, 2))
            assert all(
                expected_histogram[discrepancy, sign] > 0
                for discrepancy in reached
                for sign in (-1, 1)
            )
            assert sum(expected_histogram.values()) == (2 * b - 4 * j) * (b - 1)
    print("PASS: exact staircase census for odd 5<=b<=63")


def flag_from_occurrence(labels, p, c, indices):
    middle = sum(1 << labels[index] for index in indices)
    p_coordinate = labels[p]
    q_coordinate = labels[(p + 1) % len(labels)]
    lower = middle ^ (1 << p_coordinate)
    upper = middle | (1 << q_coordinate)
    return lower, middle, upper


def flag_type(flag, b):
    lower, middle, _ = flag
    p_coordinate = (middle ^ lower).bit_length() - 1
    even_count = sum(
        (middle >> coordinate) & 1 for coordinate in range(0, 2 * b, 2)
    )
    return even_count, 1 if p_coordinate % 2 == 0 else -1


def audit_labelled_degree_b5():
    b = 5
    j = 1
    word = staircase_word(b, j)
    plus_positions = [index for index, sign in enumerate(word) if sign == 1]
    minus_positions = [index for index, sign in enumerate(word) if sign == -1]
    evens = tuple(range(0, 2 * b, 2))
    odds = tuple(range(1, 2 * b, 2))
    cross_occurrences = [
        occurrence
        for occurrence in endpoint_occurrences(word)
        if word[occurrence[0]] != word[(occurrence[0] + 1) % (2 * b)]
    ]

    degrees = Counter()
    for even_order in permutations(evens):
        for odd_order in permutations(odds):
            labels = [None] * (2 * b)
            for position, coordinate in zip(plus_positions, even_order):
                labels[position] = coordinate
            for position, coordinate in zip(minus_positions, odd_order):
                labels[position] = coordinate
            for p, c, indices in cross_occurrences:
                degrees[flag_from_occurrence(labels, p, c, indices)] += 1

    _, histogram = formula_histogram(b, j)
    type_degrees = {}
    for flag, degree in degrees.items():
        a, endpoint_sign = flag_type(flag, b)
        discrepancy = 2 * a - b
        if endpoint_sign == 1:
            expected = histogram[discrepancy, 1] * (
                factorial(a - 1) * factorial(b - a)
            ) ** 2
        else:
            expected = histogram[discrepancy, -1] * (
                factorial(a) * factorial(b - a - 1)
            ) ** 2
        assert degree == expected
        type_degrees.setdefault((a, endpoint_sign), degree)
        assert type_degrees[a, endpoint_sign] == degree

    for (a, endpoint_sign), degree in type_degrees.items():
        flag_count = comb(b, a) ** 2 * (
            a ** 2 if endpoint_sign == 1 else (b - a) ** 2
        )
        discrepancy = 2 * a - b
        assert degree * flag_count == (factorial(b) ** 2) * histogram[
            discrepancy, endpoint_sign
        ]
    print("PASS: exhaustive labelled-orbit degrees for b=5, j=1")


def audit_hypergeometric_tail():
    for b in range(3, 52, 2):
        denominator = comb(2 * b, b)
        for cutoff in range(b + 1):
            bad = sum(
                comb(b, a) ** 2
                for a in range(b + 1)
                if abs(2 * a - b) > cutoff
            )
            probability = bad / denominator
            assert probability <= 2 * exp(-(cutoff ** 2) / (8 * b)) + 1e-14
    print("PASS: hypergeometric tail audit for odd 3<=b<=51")


if __name__ == "__main__":
    audit_endpoint_bijection()
    audit_staircase_census()
    audit_labelled_degree_b5()
    audit_hypergeometric_tail()
