#!/usr/bin/env python3
"""Finite audit of the fixed-split central-slice crossing multiplicity.

For an all-split atom E(A,alpha,beta) and a fixed reference b-set P, only
the two cyclic binary membership patterns P∩A and P∩(Omega-A) matter.  The
script exhausts their distinct sliding-window histograms and verifies that
the number of atom cells S with |S∩P| in {h,h+1} is at least 4(b-1).
This is a regression check, not the asymptotic proof.
"""

from collections import Counter, defaultdict


def window_histogram(mask: int, b: int, length: int) -> tuple[tuple[int, int], ...]:
    value = sum((mask >> j) & 1 for j in range(length))
    values = [value]
    for start in range(1, b):
        value -= (mask >> (start - 1)) & 1
        value += (mask >> ((start + length - 1) % b)) & 1
        values.append(value)
    return tuple(sorted(Counter(values).items()))


def central_pairs(
    first: tuple[tuple[int, int], ...],
    second: tuple[tuple[int, int], ...],
    h: int,
) -> int:
    return sum(
        cx * cy
        for x, cx in first
        for y, cy in second
        if x + y in (h, h + 1)
    )


def audit(b: int) -> None:
    h = (b - 1) // 2
    histograms: dict[tuple[int, int], set[tuple[tuple[int, int], ...]]] = defaultdict(set)
    for mask in range(1 << b):
        weight = mask.bit_count()
        histograms[(weight, h)].add(window_histogram(mask, b, h))
        histograms[(weight, h + 1)].add(window_histogram(mask, b, h + 1))

    best = b * b + 1
    witness = None
    for a in range(b + 1):
        for first in histograms[(a, h)]:
            for second in histograms[(b - a, h + 1)]:
                count = central_pairs(first, second, h)
                if count < best:
                    best = count
                    witness = (a, first, second)
    assert best == 4 * (b - 1), (b, best, witness)
    print("b", b, "minimum", best, "witness", witness)


def main() -> None:
    for b in range(5, 18, 2):
        audit(b)
    print("ALL_SPLIT_CENTRAL_SLICE_CROSSING_AUDIT_PASS")


if __name__ == "__main__":
    main()
