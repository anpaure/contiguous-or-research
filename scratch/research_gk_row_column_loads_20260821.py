#!/usr/bin/env python3
"""Exact small-b row/column diagnostics for interleaved GK orientation classes.

At a fixed split r, rows are A-subsets and columns are B-subsets.  We record
the row/column degree distributions of the A-first/B-first classes and of
top-excess threshold classes.  Exploratory only; run on H100.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations


def top_excess(bits: list[int]) -> int:
    stack: list[int] = []
    matched = [False] * len(bits)
    for i, bit in enumerate(bits):
        if bit:
            stack.append(i)
        elif stack:
            j = stack.pop()
            matched[i] = matched[j] = True
    return sum(1 for i, bit in enumerate(bits) if not matched[i] and not bit)


def first_add(bits: list[int]) -> int | None:
    stack: list[int] = []
    matched = [False] * len(bits)
    for i, bit in enumerate(bits):
        if bit:
            stack.append(i)
        elif stack:
            j = stack.pop()
            matched[i] = matched[j] = True
    zeros = [i for i, bit in enumerate(bits) if not matched[i] and not bit]
    return zeros[-1] if zeros else None


def main() -> None:
    for b in range(3, 12, 2):
        Asets = {r: list(combinations(range(b), r)) for r in range(b + 1)}
        print("B", b)
        for r in range(max(0, b // 2 - 2), min(b, b // 2 + 2) + 1):
            rows = Asets[r]
            cols = Asets[b - r]
            row_a: dict[tuple[int, ...], int] = defaultdict(int)
            col_a: dict[tuple[int, ...], int] = defaultdict(int)
            row_thr: dict[int, dict[tuple[int, ...], int]] = {
                q: defaultdict(int) for q in range(1, min(5, b) + 1)
            }
            col_thr: dict[int, dict[tuple[int, ...], int]] = {
                q: defaultdict(int) for q in range(1, min(5, b) + 1)
            }
            k_hist: Counter[int] = Counter()
            for x in rows:
                xs = set(x)
                for y in cols:
                    ys = set(y)
                    bits = []
                    for i in range(b):
                        bits.extend((int(i in xs), int(i in ys)))
                    k = top_excess(bits)
                    k_hist[k] += 1
                    if k % 2 == 1:
                        row_a[x] += 1
                        col_a[y] += 1
                    for q in row_thr:
                        if k >= q:
                            row_thr[q][x] += 1
                            col_thr[q][y] += 1

            def span(vals: dict[tuple[int, ...], int], universe: list[tuple[int, ...]]) -> tuple[int, int, int]:
                vv = [vals[z] for z in universe]
                return min(vv), max(vv), len(set(vv))

            print(
                " R",
                r,
                "ROWS",
                len(rows),
                "COLS",
                len(cols),
                "A_ROW",
                span(row_a, rows),
                "A_COL",
                span(col_a, cols),
                "K",
                sorted(k_hist.items()),
            )
            for q in row_thr:
                print(
                    "  Q",
                    q,
                    "ROW",
                    span(row_thr[q], rows),
                    "COL",
                    span(col_thr[q], cols),
                )

            # Candidate cyclic proof of the exact orientation degree: for
            # every fixed X,Y, rotate only the B coordinates and count the
            # A-first shifts.
            if b <= 9:
                for x in rows:
                    xs = set(x)
                    for y in cols:
                        ys = set(y)
                        acount = 0
                        first_a_indices: list[int] = []
                        for sh in range(b):
                            ysh = {(j + sh) % b for j in ys}
                            bits = []
                            for i in range(b):
                                bits.extend((int(i in xs), int(i in ysh)))
                            if top_excess(bits) % 2 == 1:
                                acount += 1
                                fa = first_add(bits)
                                assert fa is not None and fa % 2 == 0
                                first_a_indices.append(fa // 2)
                        if acount != b - r:
                            print("ROTATION_FAIL", b, r, x, y, acount, b - r)
                            raise AssertionError
                        if sorted(first_a_indices) != sorted(set(range(b)) - xs):
                            print("FIRST_A_BIJECTION_FAIL", b, r, x, y, first_a_indices)
                            raise AssertionError
                print("  ROTATION_IDENTITY_PASS", b, r)


if __name__ == "__main__":
    main()
