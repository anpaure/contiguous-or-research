#!/usr/bin/env python3
"""Measure GK-prefix alignment of dummy-deleted canonical MSW rows.

Input is the output of dump_msw_orders for semilength b.  Its stored row
uses the step-two interval convention, so we first convert it to the actual
cyclic interval order, cut immediately after the dummy, and inspect the b+1
dummy-free rank-b windows.  Research-only; run on H100.
"""

from __future__ import annotations

from collections import Counter
import argparse
import sys


def additions(n: int, source: frozenset[int]) -> tuple[int, ...]:
    bits = [i in source for i in range(n)]
    stack: list[int] = []
    matched = [False] * n
    for i, bit in enumerate(bits):
        if bit:
            stack.append(i)
        elif stack:
            j = stack.pop()
            matched[i] = matched[j] = True
    return tuple(
        reversed([i for i in range(n) if not matched[i] and not bits[i]])
    )


def cut_real_order(stored: list[int], b: int, reverse: bool) -> list[int]:
    n = 2 * b + 1
    actual = [stored[(2 * i) % n] for i in range(n)]
    if reverse:
        actual = [actual[0]] + list(reversed(actual[1:]))
    at = actual.index(2 * b)
    actual = actual[at:] + actual[:at]
    assert actual[0] == 2 * b
    return actual[1:]


def score(order: list[int], b: int, H: int) -> tuple[int, int, int, Counter[int]]:
    total = 0
    good = 0
    full_sources = 0
    matched_hist: Counter[int] = Counter()
    for t in range(b + 1):
        source = frozenset(order[t : t + b])
        aa = additions(2 * b, source)
        available = order[t + b :]
        claim = min(H, len(aa), len(available))
        total += claim
        m = 0
        while m < claim and available[m] == aa[m]:
            m += 1
        good += m
        matched_hist[m] += 1
        if m == min(H, len(aa)):
            full_sources += 1
    return total, good, full_sources, matched_hist


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("b", type=int)
    parser.add_argument("--H", type=int, default=0)
    args = parser.parse_args()
    b = args.b
    H = args.H or b
    totals = [0, 0, 0]
    hist: Counter[int] = Counter()
    rows = 0
    for line in sys.stdin:
        if not line.strip():
            continue
        stored = [int(x) - 1 for x in line.split()]
        assert len(stored) == 2 * b + 1
        options = []
        for rev in (False, True):
            order = cut_real_order(stored, b, rev)
            options.append(score(order, b, H))
        best = max(options, key=lambda z: (z[1], z[2]))
        totals[0] += best[0]
        totals[1] += best[1]
        totals[2] += best[2]
        hist.update(best[3])
        rows += 1
    print(
        "MSW_GK",
        "B",
        b,
        "H",
        H,
        "ROWS",
        rows,
        "SOURCES",
        rows * (b + 1),
        "CLAIM_INCIDENCES",
        totals[0],
        "GOOD_PREFIX_INCIDENCES",
        totals[1],
        "GOOD_FRACTION",
        totals[1] / max(1, totals[0]),
        "FULL_SOURCES",
        totals[2],
        "FULL_FRACTION",
        totals[2] / max(1, rows * (b + 1)),
        "MATCH_HIST",
        sorted(hist.items()),
    )


if __name__ == "__main__":
    main()
