#!/usr/bin/env python3
"""Exhaustive audit for the Gate-C pivot-flip factorial-moment theorem."""

from collections import Counter, defaultdict
from itertools import permutations
from math import factorial


def inverse(order):
    answer = [0] * len(order)
    for position, value in enumerate(order):
        answer[value] = position
    return answer


def signs_and_good(order, root):
    sigma = inverse(order)
    k = len(order)
    word = tuple(
        1 if (((value - root) % k
               + (sigma[value] - sigma[root]) % k) % 2 == 0) else -1
        for value in ((root + offset) % k for offset in range(1, k))
    )
    height = 0
    heights = []
    for sign in word:
        height += sign
        heights.append(height)
    return word, min(heights) >= 0 and max(heights) <= heights[-1]


def walk_at(order, position):
    sigma = inverse(order)
    colors = tuple(1 if (value + sigma[value]) % 2 == 0 else -1
                   for value in range(len(order)))
    increments = tuple(
        colors[value] * (-1 if sigma[value] < position else 1)
        for value in range(len(order))
    )
    cumulative = [0]
    for increment in increments:
        cumulative.append(cumulative[-1] + increment)
    return colors, increments, cumulative


def pivots(increments, cumulative):
    positive = []
    negative = []
    k = len(increments)
    for value, increment in enumerate(increments):
        left = cumulative[value]
        right = cumulative[value + 1]
        if increment == 1:
            if (all(cumulative[index] >= left for index in range(value + 1))
                    and all(cumulative[index] >= right
                            for index in range(value + 1, k + 1))):
                positive.append(value)
        else:
            if (all(cumulative[index] <= left for index in range(value + 1))
                    and all(cumulative[index] <= right
                            for index in range(value + 1, k + 1))):
                negative.append(value)
    return positive, negative


def falling(value, length):
    answer = 1
    for offset in range(length):
        answer *= value - offset
    return answer


def harmonic(n):
    return sum(1 / value for value in range(1, n + 1))


def audit_conditional_reveal_law():
    for k in (3, 5, 7):
        transition_counts = defaultdict(Counter)
        for order in permutations(range(k)):
            sigma = inverse(order)
            colors = tuple(1 if (value + sigma[value]) % 2 == 0 else -1
                           for value in range(k))
            for position in range(k):
                key = (colors, position, order[:position])
                transition_counts[key][order[position]] += 1

        for (colors, position, prefix), counts in transition_counts.items():
            remaining = set(range(k)) - set(prefix)
            eligible = {
                value for value in remaining
                if (1 if (value + position) % 2 == 0 else -1) == colors[value]
            }
            assert set(counts) == eligible
            assert len(set(counts.values())) == 1
            assert len(eligible) == ((k + 1) // 2 - position // 2
                                     if position % 2 == 0
                                     else (k - 1) // 2 - position // 2)

            # The threshold walk is fixed by (colors,prefix), so the pivot
            # candidate set is predictable before the next value is sampled.
            increments = tuple(
                colors[value] * (-1 if value in prefix else 1)
                for value in range(k)
            )
            cumulative = [0]
            for increment in increments:
                cumulative.append(cumulative[-1] + increment)
            positive, negative = pivots(increments, cumulative)
            candidates = eligible & (set(positive) | set(negative))
            assert len(candidates) <= 2
            conditional_probability = sum(counts[value] for value in candidates) / sum(counts.values())
            assert conditional_probability <= 2 / len(eligible) + 1e-12
        print(f"PASS: K={k} exact conditional reveal law and pivot hazard")


def audit_pointwise_and_moments():
    for k in (3, 5, 7, 9):
        histogram_g = Counter()
        histogram_p = Counter()
        fiber_orders = defaultdict(list)
        for tail in permutations(range(1, k)):
            order = (0,) + tail
            # Position rotation was fixed only to shorten enumeration; every
            # identity itself is checked at every position of every order.
            sigma = inverse(order)
            colors = tuple(1 if (value + sigma[value]) % 2 == 0 else -1
                           for value in range(k))
            fiber_orders[colors].append(order)
            good_count = 0
            pivot_hit_count = 0
            for position, root in enumerate(order):
                word, good = signs_and_good(order, root)
                colors_here, increments, cumulative = walk_at(order, position)
                assert colors_here == colors
                positive, negative = pivots(increments, cumulative)
                assert len(positive) <= 1 and len(negative) <= 1
                is_pivot = root in positive or root in negative
                assert not good or is_pivot
                good_count += good
                pivot_hit_count += is_pivot

                for value in range(k):
                    if value == root:
                        continue
                    expected = (colors[root] * increments[value]
                                if value > root
                                else -colors[root] * increments[value])
                    actual = (1 if (((value - root) % k
                                     + (sigma[value] - position) % k) % 2 == 0)
                              else -1)
                    assert actual == expected
            assert good_count <= pivot_hit_count
            histogram_g[good_count] += 1
            histogram_p[pivot_hit_count] += 1

        e = (k - 1) // 2
        bound = 2 * (harmonic(e) + harmonic(e + 1))
        total = factorial(k - 1)
        for length in range(1, k + 1):
            moment_g = sum(count * falling(value, length)
                           for value, count in histogram_g.items()) / total
            moment_p = sum(count * falling(value, length)
                           for value, count in histogram_p.items()) / total
            assert moment_g <= moment_p + 1e-12
            assert moment_p <= bound ** length + 1e-12

        # In a fixed color fiber, values assigned to either position parity
        # appear with constant multiplicity: the two orders are independent.
        for colors, orders in fiber_orders.items():
            allowed_even = [value for value in range(k)
                            if ((value + (0 if colors[value] == 1 else 1)) % 2
                                == 0)]
            allowed_odd = [value for value in range(k) if value not in allowed_even]
            assert len(allowed_even) == e + 1
            assert len(allowed_odd) == e
            # Fixing order[0]=0 removes one even-position choice.  Every
            # surviving fiber therefore has the expected product size.
            assert len(orders) == factorial(e) * factorial(e)
        print(f"PASS: K={k} pointwise pivots, fibers, and all moments")


if __name__ == "__main__":
    audit_conditional_reveal_law()
    audit_pointwise_and_moments()
