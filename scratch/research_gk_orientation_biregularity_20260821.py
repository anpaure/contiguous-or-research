#!/usr/bin/env python3
"""Exact row/column degree audit for split-refined alternating GK sources."""

from __future__ import annotations

import argparse
import itertools
import math
from collections import defaultdict


def top_excess(x: frozenset[int], y: frozenset[int], b: int) -> int:
    stack = 0
    unmatched_zeros = 0
    for i in range(b):
        for bit in (i in x, i in y):
            if bit:
                stack += 1
            elif stack:
                stack -= 1
            else:
                unmatched_zeros += 1
    assert stack == unmatched_zeros
    return unmatched_zeros


def audit(b: int) -> None:
    print(f"b={b}")
    ground = range(b)
    for r in range(b + 1):
        xs = [frozenset(z) for z in itertools.combinations(ground, r)]
        ys = [frozenset(z) for z in itertools.combinations(ground, b - r)]
        n = len(xs)
        assert len(ys) == n
        kval = [[top_excess(x, y, b) for y in ys] for x in xs]
        pieces = []
        for parity, label in ((1, "A"), (0, "B")):
            row = [sum(k % 2 == parity for k in line) for line in kval]
            col = [
                sum(kval[i][j] % 2 == parity for i in range(n))
                for j in range(n)
            ]
            expected = math.comb(b - 1, r if parity else r - 1) if (
                0 <= (r if parity else r - 1) <= b - 1
            ) else 0
            assert min(row) == max(row) == expected
            assert min(col) == max(col) == expected
            pieces.append(f"{label}:deg={expected}")

            irregular = []
            for threshold in range(1, b + 1):
                row_t = [
                    sum(k % 2 == parity and k >= threshold for k in line)
                    for line in kval
                ]
                col_t = [
                    sum(
                        kval[i][j] % 2 == parity and kval[i][j] >= threshold
                        for i in range(n)
                    )
                    for j in range(n)
                ]
                if min(row_t) != max(row_t) or min(col_t) != max(col_t):
                    irregular.append(
                        (threshold, min(row_t), max(row_t), min(col_t), max(col_t))
                    )
            if irregular:
                pieces.append(f"{label}:first-irregular={irregular[0]}")
            else:
                pieces.append(f"{label}:all-thresholds-regular")
        print(f"  r={r} N={n} " + " ".join(pieces))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-b", type=int, default=9)
    args = parser.parse_args()
    for b in range(1, args.max_b + 1):
        audit(b)
    print("GK ORIENTATION BIREGULARITY AUDIT: PASS")


if __name__ == "__main__":
    main()
