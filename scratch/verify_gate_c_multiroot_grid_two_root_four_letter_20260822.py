#!/usr/bin/env python3
"""Finite audit for the multiroot-grid and two-root four-letter reduction."""

from collections import Counter
from itertools import combinations, permutations
from math import factorial


def inverse(order):
    answer = [0] * len(order)
    for position, value in enumerate(order):
        answer[value] = position
    return answer


def rooted_sign(sigma, root, value):
    k = len(sigma)
    return 1 if (
        ((value - root) % k + (sigma[value] - sigma[root]) % k) % 2 == 0
    ) else -1


def good_word(word):
    height = 0
    heights = []
    for sign in word:
        height += sign
        heights.append(height)
    return min(heights) >= 0 and max(heights) <= heights[-1]


def is_forward(word):
    height = 0
    for sign in word:
        height += sign
        if height < 0:
            return False
    return True


def is_backward(word):
    return is_forward(tuple(reversed(word)))


def audit_grid_identity():
    for k in (3, 5, 7):
        for sigma in permutations(range(k)):
            for size in range(1, min(3, k) + 1):
                for roots in combinations(range(k), size):
                    for value in range(k):
                        if value in roots:
                            continue
                        q = sigma[value]
                        z = -1 if (value + q) % 2 else 1
                        for root in roots:
                            p = sigma[root]
                            c = -1 if (root + p) % 2 else 1
                            rhs = z
                            if value < root:
                                rhs *= -1
                            if q < p:
                                rhs *= -1
                            assert c * rooted_sign(sigma, root, value) == rhs
    print("PASS: exact two-threshold grid identity through K=7")


def position_type(q, d):
    return (int(q < d), q % 2)


def audit_two_root_law_and_meanders():
    for k in (3, 5, 7):
        for u in range(1, k):
            for d in range(1, k):
                remaining_values = [v for v in range(1, k) if v != u]
                remaining_positions = [q for q in range(1, k) if q != d]
                multiplicities = Counter()
                for assigned in permutations(remaining_positions):
                    sigma = [None] * k
                    sigma[0] = 0
                    sigma[u] = d
                    for value, position in zip(remaining_values, assigned):
                        sigma[value] = position

                    type_word = tuple(position_type(sigma[v], d)
                                      for v in remaining_values)
                    multiplicities[type_word] += 1

                    c = -1 if (u + d) % 2 else 1
                    assert rooted_sign(sigma, 0, u) == c
                    assert rooted_sign(sigma, u, 0) == c
                    for value in remaining_values:
                        s = -1 if (value + sigma[value]) % 2 else 1
                        eta = -1 if sigma[value] < d else 1
                        expected = c * s * eta
                        if value < u:
                            expected *= -1
                        assert rooted_sign(sigma, u, value) == expected

                    word_zero = tuple(
                        rooted_sign(sigma, 0, value)
                        for value in range(1, k)
                    )
                    word_u = tuple(
                        rooted_sign(sigma, u, (u + offset) % k)
                        for offset in range(1, k)
                    )
                    if good_word(word_zero) and good_word(word_u):
                        interval_i = range(1, u)
                        interval_j = range(u + 1, k)
                        assert is_forward(tuple(rooted_sign(sigma, 0, v)
                                                for v in interval_i))
                        assert is_backward(tuple(rooted_sign(sigma, u, v)
                                                 for v in interval_i))
                        assert is_forward(tuple(rooted_sign(sigma, u, v)
                                                for v in interval_j))
                        assert is_backward(tuple(rooted_sign(sigma, 0, v)
                                                 for v in interval_j))

                expected = 1
                counts = Counter(position_type(q, d) for q in remaining_positions)
                for count in counts.values():
                    expected *= factorial(count)
                assert set(multiplicities.values()) == {expected}
    print("PASS: exact four-letter law, sign table, and meanders through K=7")


if __name__ == "__main__":
    audit_grid_identity()
    audit_two_root_law_and_meanders()
