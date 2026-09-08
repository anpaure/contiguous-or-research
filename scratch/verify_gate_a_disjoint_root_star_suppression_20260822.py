#!/usr/bin/env python3
"""Exact r=3 audit of the disjoint-cell root two-star bound."""

from fractions import Fraction
from itertools import combinations, permutations
from math import factorial


def catalogue(r):
    b = 2 * r + 1
    targets = (
        [("M", s) for s in combinations(range(b), r)]
        + [("L", s) for s in combinations(range(b), r - 1)]
    )
    target_id = {target: i for i, target in enumerate(targets)}
    rows = set()
    for word in permutations(range(b)):
        row = []
        for start in range(1, b):
            middle = tuple(
                sorted(word[(start + j) % b] for j in range(r))
            )
            lower = tuple(
                sorted(word[(start + j) % b] for j in range(r - 1))
            )
            row.append(target_id[("M", middle)])
            row.append(target_id[("L", lower)])
        rows.add(tuple(sorted(row)))
    rows = sorted(rows)
    assert len(rows) == factorial(b)
    masks = [sum(1 << u for u in row) for row in rows]
    return targets, masks


def main():
    r = 3
    targets, rows = catalogue(r)
    root = next(i for i, target in enumerate(targets) if target[0] == "M")
    root_bit = 1 << root
    star = [row for row in rows if row & root_bit]
    degree = len(star)
    assert degree == 2 * r * factorial(r) * factorial(r + 1)

    p = [
        Fraction(9, 10) if shore == "M" else Fraction(4, 5)
        for shore, _ in targets
    ]
    inverse = [1 / value for value in p]
    x = min(p)

    def weight(mask):
        value = Fraction(1)
        while mask:
            bit = mask & -mask
            value *= inverse[bit.bit_length() - 1]
            mask ^= bit
        return value

    # h[first][further] is the one-row overlap excess in (3.1).
    h = []
    rooted_r2 = []
    for first in star:
        row_h = []
        kernel_sum = Fraction(0)
        for further in star:
            overlap = (first & further) & ~root_bit
            row_h.append(weight(overlap) - 1)
            if further != first:
                t = overlap.bit_count()
                kernel_sum += x ** (-2 * t) - 1
        h.append(row_h)
        rooted_r2.append(kernel_sum / degree)
    r2 = max(rooted_r2)

    disjoint_pairs = 0
    largest = Fraction(0)
    for first_index, first in enumerate(star):
        for second_index in range(first_index + 1, degree):
            second = star[second_index]
            if first & second != root_bit:
                continue
            disjoint_pairs += 1
            total = Fraction(0)
            for further_index, further in enumerate(star):
                left = (further & first) & ~root_bit
                right = (further & second) & ~root_bit
                direct = inverse[root] * (
                    weight(left | right)
                    - weight(left)
                    - weight(right)
                    + 1
                )
                factored = (
                    inverse[root]
                    * h[first_index][further_index]
                    * h[second_index][further_index]
                )
                assert direct == factored >= 0
                total += (
                    h[first_index][further_index]
                    * h[second_index][further_index]
                )
            normalized = total / degree
            assert normalized <= r2
            largest = max(largest, normalized)

    assert disjoint_pairs == 4320
    print("r:", r)
    print("root degree:", degree)
    print("off-root-disjoint unordered pairs:", disjoint_pairs)
    print("largest normalized root two-star:", largest)
    print("R_2 bound:", r2)
    print("ratio:", float(largest / r2))
    print("PASS")


if __name__ == "__main__":
    main()
