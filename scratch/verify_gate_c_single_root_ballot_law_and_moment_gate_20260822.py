#!/usr/bin/env python3
"""Finite audit for the single-root ballot law and moment reduction."""

from collections import Counter
from itertools import combinations, permutations
from math import comb, factorial


def is_two_sided_ballot(word):
    height = 0
    prefixes = []
    for sign in word:
        height += sign
        prefixes.append(height)
    return all(0 <= value <= prefixes[-1] for value in prefixes)


def word_from_normalized_inverse(sigma):
    return tuple(
        1 if sigma[offset] % 2 == offset % 2 else -1
        for offset in range(1, len(sigma))
    )


def audit_uniform_word_law():
    for k in (3, 5, 7, 9):
        e = (k - 1) // 2
        multiplicities = Counter(
            word_from_normalized_inverse((0,) + tail)
            for tail in permutations(range(1, k))
        )
        assert len(multiplicities) == comb(2 * e, e)
        assert set(multiplicities.values()) == {factorial(e) ** 2}
        for word in multiplicities:
            odd_plus = sum(word[index] == 1 for index in range(0, 2 * e, 2))
            even_plus = sum(word[index] == 1 for index in range(1, 2 * e, 2))
            assert odd_plus == even_plus
    print("PASS: exact uniform parity-balanced word law for K=3,5,7,9")


def parity_balanced_words(e):
    odd_positions = tuple(range(0, 2 * e, 2))
    even_positions = tuple(range(1, 2 * e, 2))
    for size in range(e + 1):
        for odd_plus in combinations(odd_positions, size):
            for even_plus in combinations(even_positions, size):
                chosen = set(odd_plus) | set(even_plus)
                yield tuple(1 if position in chosen else -1 for position in range(2 * e))


def audit_single_root_counts():
    expected = (1, 1, 3, 8, 21, 75, 209, 785, 2422, 8899)
    actual = []
    for e in range(1, 11):
        words = tuple(parity_balanced_words(e))
        assert len(words) == comb(2 * e, e)
        actual.append(sum(is_two_sided_ballot(word) for word in words))
    assert tuple(actual) == expected
    print("PASS: exact N_e values through e=10", actual)


def inverse(order):
    answer = [0] * len(order)
    for position, value in enumerate(order):
        answer[value] = position
    return answer


def good_count(order):
    sigma = inverse(order)
    k = len(order)
    answer = 0
    for value in range(k):
        word = tuple(
            1
            if ((sigma[(value + offset) % k] - sigma[value]) % k) % 2
            == offset % 2
            else -1
            for offset in range(1, k)
        )
        answer += is_two_sided_ballot(word)
    return answer


def falling(value, length):
    answer = 1
    for offset in range(length):
        answer *= value - offset
    return answer


def audit_factorial_moments():
    for k in (3, 5, 7, 9):
        histogram = Counter(
            good_count((0,) + tail) for tail in permutations(range(1, k))
        )
        total = factorial(k - 1)
        moments = [
            sum(count * falling(good, length) for good, count in histogram.items())
            / total
            for length in range(1, k + 1)
        ]
        assert moments[0] < 2
        assert max(moment ** (1 / length) for length, moment in enumerate(moments, 1)) < 2
        print(f"EVIDENCE K={k} histogram={dict(sorted(histogram.items()))}")
        print(f"EVIDENCE K={k} falling_moments={moments}")
    print("PASS: exact finite factorial-moment evidence through K=9")


if __name__ == "__main__":
    audit_uniform_word_law()
    audit_single_root_counts()
    audit_factorial_moments()
