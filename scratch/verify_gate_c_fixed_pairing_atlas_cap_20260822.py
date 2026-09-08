#!/usr/bin/env python3
"""Finite audit for the universal fixed-pairing atlas cap."""

from itertools import product
from math import comb


def target(b, state, empty, double):
    """Canonical target T_(empty,double) from the exact coherent formula."""
    out = {2 * double, 2 * double + 1}
    for h in range(b):
        if h in (empty, double):
            continue
        # This is formula chi_(t,i), with an arbitrary initial transversal
        # state added.  Integer representatives are 0,...,b-1.
        bit = state[h] ^ (empty & 1) ^ int((h - double) * (empty - double) > 0)
        out.add(2 * h + bit)
    return frozenset(out)


def signature(b, middle):
    counts = tuple(int(2 * h in middle) + int(2 * h + 1 in middle)
                   for h in range(b))
    empty = tuple(h for h, count in enumerate(counts) if count == 0)
    double = tuple(h for h, count in enumerate(counts) if count == 2)
    split = tuple(h for h, count in enumerate(counts) if count == 1)
    return empty, double, split


def audit_b(b):
    q = b * (b - 1)
    atlas = set()
    for bits in product((0, 1), repeat=b):
        tour = set()
        for empty in range(b):
            for double in range(b):
                if empty == double:
                    continue
                middle = target(b, bits, empty, double)
                e, d, split = signature(b, middle)
                assert e == (empty,) and d == (double,) and len(split) == b - 2
                tour.add(middle)
                atlas.add(middle)
        assert len(tour) == q

    expected = q * 2 ** (b - 2)
    assert len(atlas) == expected
    assert comb(2 * b, b - 1) * b == comb(2 * b, b) * b * b // (b + 1)
    print(f"PASS: b={b} q={q} atlas={len(atlas)} expected={expected}")


def audit():
    for b in (3, 5, 7):
        audit_b(b)


if __name__ == "__main__":
    audit()
