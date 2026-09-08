#!/usr/bin/env python3
"""Finite audit of long-arc degrees, multiplicities, and pair codegrees.

Intended execution environment: H100 only.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import permutations
from math import factorial


def falling(n, k):
    answer = 1
    for j in range(k):
        answer *= n - j
    return answer


def windows(word, k, ell):
    return tuple(frozenset(word[i : i + k]) for i in range(ell))


def predicted(r, ell):
    dm = ell * factorial(r) * falling(r + 1, ell - 1)
    dl = ell * factorial(r - 1) * falling(r + 2, ell)
    mm = {}
    ll = {}
    ml = {}
    for d in range(1, ell):
        mm[d] = (
            2 * (ell - d) * factorial(d) ** 2 * factorial(r - d)
            * falling(r + 1 - d, ell - 1 - d)
        )
        ll[d] = (
            2 * (ell - d) * factorial(d) ** 2 * factorial(r - 1 - d)
            * falling(r + 2 - d, ell - d)
        )
    ml[1] = (2 * ell - 1) * factorial(r - 1) * falling(r + 1, ell - 1)
    for d in range(2, ell + 1):
        ml[d] = (
            (2 * ell - 2 * d + 1) * factorial(d) * factorial(d - 1)
            * factorial(r - d) * falling(r - d + 2, ell - d)
        )
    return dm, dl, mm, ll, ml


def audit(r, ell):
    b = 2 * r + 1
    length = r + ell - 1
    edge_mult = Counter()
    degree_m = Counter()
    degree_l = Counter()
    degree_q = {q: Counter() for q in range(1, r)}
    pair_mm = Counter()
    pair_ll = Counter()
    pair_ml = Counter()
    for word in permutations(range(b), length):
        middle = windows(word, r, ell)
        lower = windows(word, r - 1, ell)
        edge_mult[(frozenset(middle), frozenset(lower))] += 1
        for target in middle:
            degree_m[target] += 1
        for target in lower:
            degree_l[target] += 1
        for q in degree_q:
            for target in windows(word, r - q, ell):
                degree_q[q][target] += 1
        for i in range(ell):
            for j in range(i + 1, ell):
                pair_mm[frozenset((middle[i], middle[j]))] += 1
                pair_ll[frozenset((lower[i], lower[j]))] += 1
        for x in middle:
            for y in lower:
                pair_ml[(x, y)] += 1

    dm, dl, mm, ll, ml = predicted(r, ell)
    assert set(degree_m.values()) == {dm}
    assert set(degree_l.values()) == {dl}
    assert set(edge_mult.values()) == {factorial(r - ell)}
    for q, degree in degree_q.items():
        dq = ell * factorial(r - q) * falling(r + q + 1, ell + q - 1)
        assert set(degree.values()) == {dq}
    for pair, value in pair_mm.items():
        x, y = tuple(pair)
        d = len(x - y)
        assert value == mm[d]
    for pair, value in pair_ll.items():
        x, y = tuple(pair)
        d = len(x - y)
        assert value == ll[d]
    for (x, y), value in pair_ml.items():
        d = len(x - y)
        assert value == ml[d]
    return {
        "r": r,
        "ell": ell,
        "words": falling(b, length),
        "edges": len(edge_mult),
        "multiplicity": factorial(r - ell),
        "D_M": dm,
        "D_L": dl,
        "max_pair": max(
            max(pair_mm.values(), default=0),
            max(pair_ll.values(), default=0),
            max(pair_ml.values(), default=0),
        ),
    }


def main():
    # The largest case has (7)_5=2520 words; all pair tables are literal.
    summaries = []
    for r in range(2, 4):
        for ell in range(1, r + 1):
            summaries.append(audit(r, ell))
    print("LONG_ARC_Q1_PROFILE_ALL_DEPTH_GATE_AUDIT_PASS", summaries)


if __name__ == "__main__":
    main()
