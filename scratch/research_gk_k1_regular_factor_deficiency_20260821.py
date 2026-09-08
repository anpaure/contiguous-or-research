#!/usr/bin/env python3
"""Exact H=2 obstruction diagnostic for regularizing GK chains.

For b=2h+1 and r=h, physical capacity asks us to delete an e=N/b
regular subgraph from the A-first relation.  The cheapest deletions have
top excess k=1.  This script measures the row/column Hall deficiency of
that k=1 graph.  Exploratory; H100 only.
"""

from __future__ import annotations

from collections import Counter
from itertools import combinations
from math import comb


def top_excess(b: int, xs: set[int], ys: set[int]) -> int:
    height = 0
    minimum = 0
    for i in range(b):
        height += 1 if i in xs else -1
        minimum = min(minimum, height)
        height += 1 if i in ys else -1
        minimum = min(minimum, height)
    assert height == 0
    return -minimum


def main() -> None:
    for b in (5, 7, 11, 13):
        h = (b - 1) // 2
        rows = list(combinations(range(b), h))
        cols = list(combinations(range(b), h + 1))
        N = len(rows)
        assert N == len(cols) and N % b == 0
        e = N // b
        rd = [0] * N
        cd = [0] * N
        kh = Counter()
        col_index = {y: j for j, y in enumerate(cols)}
        for i, x in enumerate(rows):
            xs = set(x)
            for j, y in enumerate(cols):
                k = top_excess(b, xs, set(y))
                kh[k] += 1
                if k == 1:
                    rd[i] += 1
                    cd[j] += 1
        row_def = sum(max(0, e - z) for z in rd)
        col_def = sum(max(0, e - z) for z in cd)
        print(
            "CASE",
            b,
            "N",
            N,
            "E",
            e,
            "K1",
            kh[1],
            "ROW_RANGE",
            (min(rd), max(rd)),
            "ROW_HIST",
            sorted(Counter(rd).items()),
            "COL_RANGE",
            (min(cd), max(cd)),
            "ROW_DEF",
            row_def,
            "COL_DEF",
            col_def,
            "MAX_DEF/N2",
            max(row_def, col_def) / (N * N),
            flush=True,
        )


if __name__ == "__main__":
    main()
