#!/usr/bin/env python3
"""Exact finite audit for coordinate-necklace/wreath compatibility."""

from __future__ import annotations

import itertools
import math


PRIMES = (5, 7, 11, 13)


def translate(mask: int, d: int, b: int) -> int:
    ans = 0
    for x in range(b):
        if (mask >> x) & 1:
            ans |= 1 << ((x + d) % b)
    return ans


def interval_mask(a: int, d: int, r: int, b: int) -> int:
    return sum(1 << ((a + j * d) % b) for j in range(r))


def audit(b: int, r: int) -> None:
    masks = [sum(1 << x for x in c) for c in itertools.combinations(range(b), r)]
    compatible = set()
    for mask in masks:
        tight_steps = []
        for d in range(1, b):
            tight = (mask ^ translate(mask, d, b)).bit_count() == 2
            interval = any(mask == interval_mask(a, d, r, b) for a in range(b))
            assert tight == interval, (b, r, mask, d)
            if tight:
                tight_steps.append(d)
        if tight_steps:
            compatible.add(mask)
            d = tight_steps[0]
            order = tuple((j * d) % b for j in range(b))
            deck = {
                sum(1 << order[(end - q) % b] for q in range(r))
                for end in range(b)
            }
            necklace = {translate(mask, s, b) for s in range(b)}
            assert deck == necklace

    assert len(compatible) == b * (b - 1) // 2, (b, r, len(compatible))
    necklaces = {
        min(translate(mask, s, b) for s in range(b))
        for mask in masks
    }
    good_necklaces = {
        min(translate(mask, s, b) for s in range(b))
        for mask in compatible
    }
    assert len(necklaces) == math.comb(b, r) // b
    assert len(good_necklaces) == (b - 1) // 2


def main() -> None:
    rows = 0
    for b in PRIMES:
        for r in range(2, b - 1):
            audit(b, r)
            rows += 1
            print(f"b={b} r={r} PASS")
    print(f"AUDIT COORDINATE NECKLACE/WREATH: PASS rows={rows}")


if __name__ == "__main__":
    main()
