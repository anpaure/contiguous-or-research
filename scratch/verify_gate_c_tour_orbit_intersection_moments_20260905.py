#!/usr/bin/env python3
"""Finite audit for the coherent-tour orbit moment note.

The orbit identities are double-counting theorems.  This checker constructs
the completed word, verifies all support sizes in the clean range, checks
the two central distance censuses, and evaluates the exact factorial-moment
sums appearing in Section 3.
"""

from collections import Counter
from fractions import Fraction
from math import comb


def completed_word(b: int):
    bits = [0] * b
    word = []
    current = {2 * j + bits[j] for j in range(b)}
    internal = []
    middle = []
    for s in range(b):
        queue = [(s + i) % b for i in range(b)]
        for k in range(1, b):
            doubled = (s + k) % b
            letter = 2 * doubled + (bits[doubled] ^ 1)
            word.append(letter)
            current.add(letter)
            front = queue.pop(0)
            current.remove(2 * front + bits[front])
            if front != s:
                bits[front] ^= 1
            target = frozenset(current)
            internal.append(target)
            middle.append(target)

        letter = 2 * s + bits[s]
        word.append(letter)
        current.add(letter)
        front = queue.pop(0)
        current.remove(2 * front + bits[front])
        bits[front] ^= 1
        middle.append(frozenset(current))

    assert bits == [0] * b
    assert len(word) == b * b
    assert len(set(internal)) == b * (b - 1)
    assert len(set(middle)) == b * b
    return word, internal, middle


def distance_census(family):
    return Counter(len(a - z) for a in family for z in family)


def expected_internal_census(b: int):
    out = Counter()
    out[0] = b * (b - 1)
    out[1] = b * (b * b - 5) // 2
    for r in range(2, b - 2):
        out[r] = b * (b * b + (1 if r % 2 == 0 else -3))
    out[b - 2] = b * (b + 1) * (3 * b - 5) // 2
    out[b - 1] = 2 * b * b
    return out


def expected_completed_census(b: int):
    out = Counter()
    out[0] = b * b
    out[1] = b * (b * b + 4 * b - 1) // 2
    for r in range(2, b - 2):
        out[r] = b * ((b + 1) ** 2 if r % 2 == 0 else b * b + 2 * b - 1)
    out[b - 2] = b * (b + 1) * (3 * b - 1) // 2
    out[b - 1] = 4 * b * b
    return out


def check(b: int):
    word, internal, middle = completed_word(b)
    doubled = word + word
    for ell in range(2, 2 * b - 2):
        support = {
            frozenset(doubled[start : start + ell])
            for start in range(b * b)
        }
        expected = b * (ell + 1) if ell <= b - 1 else b * b
        assert len(support) == expected

        if ell <= b - 2:
            noncrossing = {}
            crossing = set()
            for packet in range(b):
                for offset in range(b):
                    target = frozenset(
                        doubled[packet * b + offset : packet * b + offset + ell]
                    )
                    pair_support = frozenset(value // 2 for value in target)
                    if offset + ell <= b:
                        noncrossing.setdefault(pair_support, set()).add(target)
                    else:
                        crossing.add(target)
            assert len(noncrossing) == b
            assert all(len(fibre) == 2 for fibre in noncrossing.values())
            assert len(crossing) == b * (ell - 1)
            assert crossing.isdisjoint(set().union(*noncrossing.values()))

    internal_hist = distance_census(internal)
    completed_hist = distance_census(middle)
    assert internal_hist == expected_internal_census(b)
    assert completed_hist == expected_completed_census(b)

    w = comb(2 * b, b)
    first_internal = Fraction(len(internal) ** 2, w)
    second_internal = sum(
        Fraction(count * count, w * comb(b, r) ** 2)
        for r, count in internal_hist.items()
        if r
    )
    first_completed = Fraction(len(middle) ** 2, w)
    second_completed = sum(
        Fraction(count * count, w * comb(b, r) ** 2)
        for r, count in completed_hist.items()
        if r
    )
    assert first_internal == Fraction((b * (b - 1)) ** 2, w)
    assert first_completed == Fraction(b**4, w)
    assert second_internal > 0
    assert second_completed > 0


def main():
    for b in range(5, 32, 2):
        check(b)
    print(
        "PASS: all clean-rank support sizes, both central distance censuses, "
        "and exact two-tour factorial-moment sums for odd 5<=b<=31"
    )


if __name__ == "__main__":
    main()
