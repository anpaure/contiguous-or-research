#!/usr/bin/env python3
"""Count split/orientation/retirement statistics in the alternating GK SCD.

Coordinate order is A_0,B_0,A_1,B_1,... . Runs belong on ssh h100.
"""

from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb


def middle_masks(n: int):
    b = n // 2
    for cc in combinations(range(n), b):
        yield sum(1 << i for i in cc)


def unmatched_positions(mask: int, n: int):
    # Pair each 0 with the nearest still-unpaired 1 to its left.
    stack = []
    paired = set()
    for i in range(n):
        if (mask >> i) & 1:
            stack.append(i)
        elif stack:
            j = stack.pop()
            paired.add(i)
            paired.add(j)
    return [i for i in range(n) if i not in paired]


def audit(b: int):
    n = 2 * b
    # A occupies even positions, B odd positions.
    stats = Counter()  # (r, first_color, q) -> surviving sources
    tops = Counter()
    bad_alt = []
    for mask in middle_masks(n):
        r = sum((mask >> (2 * j)) & 1 for j in range(b))
        uu = unmatched_positions(mask, n)
        zeros = [i for i in uu if not ((mask >> i) & 1)]
        ones = [i for i in uu if (mask >> i) & 1]
        assert len(zeros) == len(ones)
        flips = list(reversed(zeros))
        colors = [i & 1 for i in flips]  # 0=A, 1=B
        if any(colors[j] == colors[j + 1] for j in range(len(colors) - 1)):
            bad_alt.append((mask, uu, colors))
        ell = len(flips)
        tops[(r, ell)] += 1
        if ell:
            orient = colors[0]
            for q in range(1, ell + 1):
                stats[(r, orient, q)] += 1

    print({"b": b, "middle": comb(2 * b, b), "bad_alt": len(bad_alt)})
    if bad_alt:
        print("first bad", bad_alt[0])
    for q in range(1, min(b, 8) + 1):
        print("q", q)
        for r in range(b + 1):
            aa = stats[(r, 0, q)]
            bb = stats[(r, 1, q)]
            if aa or bb:
                u = q // 2
                E = comb(b, r + u) * comb(b, r - u) if q % 2 == 0 and u <= r <= b-u else None
                if q % 2 == 0:
                    ideal_a = Fraction(E * (b-r-u), b-2*u) if E and b != 2*u else Fraction(0)
                    ideal_b = Fraction(E * (r-u), b-2*u) if E and b != 2*u else Fraction(0)
                else:
                    E0 = comb(b, r + u) * comb(b, r-u) if u <= r <= b-u else 0
                    ideal_a = Fraction(E0 * (b-r-u), b+2*u+1)
                    ideal_b = Fraction(E0 * (r-u), b+2*u+1)
                print(r, aa, bb, "ideal", ideal_a, ideal_b, "diff", Fraction(aa)-ideal_a, Fraction(bb)-ideal_b)
    print("top distribution")
    for key, val in sorted(tops.items()):
        if val:
            print(key, val)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--b", type=int, required=True)
    audit(ap.parse_args().b)
