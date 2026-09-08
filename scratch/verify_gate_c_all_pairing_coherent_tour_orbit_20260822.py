#!/usr/bin/env python3
"""Finite audit for the all-pairing coherent FIFO-tour orbit theorem."""

from collections import Counter
from fractions import Fraction
from itertools import permutations
from math import comb, factorial


def natural_tour(b, x=0):
    """Return labelled internal targets, boundaries, lower and upper tokens."""
    targets = []
    boundaries = []
    lower = []
    upper = []
    state = x
    all_bits = (1 << b) - 1
    for s in range(b):
        boundary = sum(1 << (2 * h + ((state >> h) & 1)) for h in range(b))
        boundaries.append(boundary)
        for t in range(1, b):
            doubled = (s + t) % b
            lo = 0
            for q in range(1, b):
                h = (s + q) % b
                bit = ((state >> h) & 1) ^ (q < t)
                lo |= 1 << (2 * h + bit)
            mid = lo | (1 << (2 * doubled + (1 - ((state >> doubled) & 1))))
            if t < b - 1:
                nxt = (s + t + 1) % b
                up = mid | (1 << (2 * nxt + (1 - ((state >> nxt) & 1))))
            else:
                up = mid | (1 << (2 * s + ((state >> s) & 1)))
            targets.append(((s, doubled), mid))
            lower.append(lo)
            upper.append(up)
        state ^= all_bits ^ (1 << s)
    assert state == x
    return targets, boundaries, lower, upper


def ordered_tour_support(b, order, x):
    """Internal support for an arbitrary anchored cyclic order."""
    masks = []
    state = x
    all_bits = (1 << b) - 1
    for s in range(b):
        empty = order[s]
        for t in range(1, b):
            doubled = order[(s + t) % b]
            lo = 0
            for q in range(1, b):
                h = order[(s + q) % b]
                bit = ((state >> h) & 1) ^ (q < t)
                lo |= 1 << (2 * h + bit)
            mid = lo | (1 << (2 * doubled + (1 - ((state >> doubled) & 1))))
            masks.append(mid)
        state ^= all_bits ^ (1 << empty)
    return tuple(sorted(masks))


def distance(b, a, c):
    return b - (a & c).bit_count()


def relation(first, second):
    t, i = first
    u, j = second
    if first == second:
        return "same"
    if t == u:
        return "same_empty"
    if i == j:
        return "same_double"
    if t == j and i == u:
        return "reverse"
    if (t == j) ^ (i == u):
        return "one_cross"
    assert len({t, i, u, j}) == 4
    return "disjoint"


def expected_relation_census(b):
    ans = Counter()
    q = b * (b - 1)
    ans[("same", 0)] = q
    for d in range(1, b - 1):
        ans[("same_empty", d)] = 2 * b * (b - 1 - d)
    ans[("same_double", 1)] = b * (b - 1) * (b - 3) // 2
    ans[("same_double", b - 2)] = b * (b - 1) ** 2 // 2
    for d in range(2, b, 2):
        ans[("reverse", d)] = 2 * b
    for d in range(2, b):
        ans[("one_cross", d)] = 2 * b * (b - 1)
    for d in range(2, b - 1):
        ans[("disjoint", d)] = b * (
            b * b - 4 * b + 3 + 4 * (d // 2)
        )
    return +ans


def expected_internal_census(b):
    q = b * (b - 1)
    ans = {0: q, 1: b * (b * b - 5) // 2}
    for d in range(2, b - 2):
        ans[d] = b * (b * b + (1 if d % 2 == 0 else -3))
    ans[b - 2] = b * (b + 1) * (3 * b - 5) // 2
    ans[b - 1] = 2 * b * b
    ans[b] = 0
    return ans


def expected_full_census(b):
    ans = {0: b * b, 1: b * (b * b + 4 * b - 1) // 2}
    for d in range(2, b - 2):
        ans[d] = b * ((b + 1) ** 2 if d % 2 == 0 else b * b + 2 * b - 1)
    ans[b - 2] = b * (b + 1) * (3 * b - 1) // 2
    ans[b - 1] = 4 * b * b
    ans[b] = 0
    return ans


def audit_b(b):
    labelled, boundaries, lower, upper = natural_tour(b)
    q = b * (b - 1)
    masks = [mask for _, mask in labelled]
    assert len(labelled) == len(set(masks)) == q
    assert all(mask.bit_count() == b for mask in masks)

    # Formula (1.2), with ordinary representatives 0,...,b-1.
    for (t, i), mask in labelled:
        assert not (mask & (3 << (2 * t)))
        assert mask & (3 << (2 * i)) == 3 << (2 * i)
        for h in range(b):
            if h in (t, i):
                continue
            chi = (t + int((h - i) * (t - i) > 0)) & 1
            assert mask & (3 << (2 * h)) == 1 << (2 * h + chi)

    actual_rel = Counter()
    actual = Counter()
    for first, a in labelled:
        for second, c in labelled:
            d = distance(b, a, c)
            actual[d] += 1
            actual_rel[(relation(first, second), d)] += 1
    assert actual_rel == expected_relation_census(b), (b, actual_rel)
    expected = expected_internal_census(b)
    assert dict(actual) == {d: n for d, n in expected.items() if n}, (b, actual)
    assert sum(expected.values()) == q * q

    ratios = {
        d: Fraction(expected[d], q * comb(b, d) ** 2)
        for d in range(1, b + 1)
    }
    claimed = Fraction(b * b - 5, 2 * b * b * (b - 1))
    assert max(ratios.values()) == claimed

    # Adjacent ranks and full cycle.
    assert len(boundaries) == len(set(boundaries)) == b
    assert len(set(lower)) == len(set(upper)) == q
    assert all(mask.bit_count() == b - 1 for mask in lower)
    assert all(mask.bit_count() == b + 1 for mask in upper)
    for s in range(b):
        packet = [boundaries[s]] + masks[s * (b - 1):(s + 1) * (b - 1)] \
            + [boundaries[(s + 1) % b]]
        for i in range(1, b):
            idx = s * (b - 1) + i - 1
            assert lower[idx] == packet[i - 1] & packet[i]
            assert upper[idx] == packet[i] | packet[i + 1]
    full = masks + boundaries
    assert len(full) == len(set(full)) == b * b
    full_actual = Counter(distance(b, a, c) for a in full for c in full)
    full_expected = expected_full_census(b)
    assert dict(full_actual) == {d: n for d, n in full_expected.items() if n}
    assert sum(full_expected.values()) == b ** 4
    full_ratios = {
        d: Fraction(full_expected[d], b * b * comb(b, d) ** 2)
        for d in range(1, b + 1)
    }
    full_claimed = Fraction(b * b + 4 * b - 1, 2 * b ** 3)
    assert max(full_ratios.values()) == full_claimed

    # Every point-star and its complement fail to contain this support.
    common = (1 << (2 * b)) - 1
    union = 0
    for mask in masks:
        common &= mask
        union |= mask
    assert common == 0
    assert union == (1 << (2 * b)) - 1

    # Exact labelled orbit degrees are integral and match the closed forms.
    edge_labels = factorial(2 * b) // b
    W = comb(2 * b, b)
    degree = edge_labels * q // W
    assert degree == (b - 1) * factorial(b) ** 2
    adjacent_degree = edge_labels * q // comb(2 * b, b - 1)
    assert adjacent_degree == (b - 1) * factorial(b - 1) * factorial(b + 1)
    assert Fraction(adjacent_degree, degree) == Fraction(b + 1, b)


def audit_reversal_duplicates(b):
    supports = Counter()
    for tail in permutations(range(1, b)):
        order = (0,) + tail
        for x in range(1 << b):
            supports[ordered_tour_support(b, order, x)] += 1
    assert set(supports.values()) == {2}, (b, Counter(supports.values()))
    assert len(supports) == factorial(b - 1) * (1 << b) // 2


def main():
    for b in range(5, 32, 2):
        audit_b(b)
    for b in (3, 5):
        audit_reversal_duplicates(b)
    print("PASS: coherent-tour orbit identities verified for odd 5<=b<=31")
    print("PASS: twofold fixed-pairing support duplication verified for b=3,5")


if __name__ == "__main__":
    main()
