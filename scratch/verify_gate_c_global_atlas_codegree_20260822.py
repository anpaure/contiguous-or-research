#!/usr/bin/env python3
"""Finite audit for the Gate-C global-atlas codegree theorem."""

from collections import Counter
from fractions import Fraction
from math import comb


def deck(order, length):
    b = len(order)
    return [frozenset(order[(i + j) % b] for j in range(length))
            for i in range(b)]


def distance(x, y):
    return len(x - y)


def audit(b):
    assert b >= 7 and b % 2 == 1
    h = (b - 1) // 2
    w, u, v = h - 1, 2 * h - 1, 2 * h

    alpha0 = list(range(b))
    alpha2 = ([u] + list(range(h - 2, -1, -1))
              + list(range(h, 2 * h - 1)) + [v, w])
    assert len(alpha2) == b and len(set(alpha2)) == b

    d0 = deck(alpha0, h)
    d2 = deck(alpha2, h)
    assert len(set(d0)) == len(set(d2)) == b
    assert set(d0).isdisjoint(d2)

    X = frozenset(range(0, h - 1)) | {u}
    Y = frozenset(range(h, 2 * h - 1)) | {v}
    named = [("X", X), ("Y", Y)]
    named += [
        (f"S{a}", frozenset(range(0, h - a))
         | frozenset(range(h, h + a)))
        for a in range(1, h)
    ]
    named += [
        (f"T{a}", frozenset(range(h - a + 1, h))
         | frozenset(range(h + a, 2 * h + 1)))
        for a in range(2, h)
    ]
    named += [
        ("U", frozenset({w, v}) | frozenset(range(h + 1, 2 * h - 1))),
        ("V", frozenset(range(1, h)) | {u}),
    ]
    assert len(named) == b
    assert {z for _, z in named} == set(d2)

    expected_one = {
        "X": {0, b - 2, b - 1},
        "Y": {h - 1, h, h + 1},
        "S1": {0, 1, b - 1},
        f"S{h - 1}": {h - 1, h},
        "T2": {h + 1, h + 2},
        "U": {h - 1, h + 1},
        "V": {0, 1},
    }
    expected_far = {
        "X": {h - 1},
        "Y": {0},
        "S1": {h + 1},
    }

    cross = Counter()
    for name, z in named:
        got_one = {i for i, n in enumerate(d0) if distance(z, n) == 1}
        got_far = {i for i, n in enumerate(d0) if distance(z, n) == h}
        assert got_one == expected_one.get(name, set()), (b, name, got_one)
        assert got_far == expected_far.get(name, set()), (b, name, got_far)
        for n in d0:
            cross[distance(n, z)] += 1
    assert cross[1] == 17
    assert cross[h] == 3

    family = d0 + d2
    f_counts = Counter(distance(x, y) for x in family for y in family)
    a = {p: Fraction(f_counts[p], 2 * b) for p in range(h + 1)}
    assert a[1] == 2 + Fraction(17, b)
    assert a[h] == 2 + Fraction(3, b)
    assert sum(a.values()) == 2 * b

    # Any cyclic (h+1)-deck has shell averages 1,2,...,2.
    ydeck = deck(list(range(b)), h + 1)
    y_counts = Counter(distance(x, y) for x in ydeck for y in ydeck)
    c = {q: Fraction(y_counts[q], b) for q in range(h + 1)}
    assert c[0] == 1
    assert all(c[q] == 2 for q in range(1, h + 1))

    n = {
        d: sum((a.get(p, 0) * c.get(d - p, 0)
                for p in range(h + 1)), Fraction(0))
        for d in range(b)
    }
    assert n[1] == 4 + Fraction(17, b)
    assert n[b - 1] == 4 + Fraction(6, b)

    ratios = {d: n[d] / (comb(b, d) ** 2) for d in range(1, b)}
    maximum = max(ratios.values())
    assert maximum == ratios[1] == Fraction(4 * b + 17, b ** 3)
    assert [d for d, value in ratios.items() if value == maximum] == [1]

    # Construct the actual Cartesian domain for modest b and check its
    # distance census directly against the convolution.
    if b <= 25:
        domain = [x | frozenset(b + z for z in y)
                  for x in family for y in ydeck]
        assert len(domain) == len(set(domain)) == 2 * b * b
        direct = Counter(distance(x, y) for x in domain for y in domain)
        assert all(Fraction(direct[d], len(domain)) == n[d]
                   for d in range(b))


def main():
    for b in range(7, 42, 2):
        audit(b)
    print("GATE_C_GLOBAL_ATLAS_CODEGREE_AUDIT_PASS b=7..41 odd")


if __name__ == "__main__":
    main()
