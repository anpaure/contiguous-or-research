#!/usr/bin/env python3
"""Diagnostics for exact statistics controlling canonical q1 loads.

Intended execution: H100 only; used to test a Catalan-recursion lemma.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from itertools import combinations

from research_b9_c8_current_lattice_20260821 import dyck_words, msw_row, windows


def cyclic_runs(bits, value):
    n = len(bits)
    if all(bit == value for bit in bits) or all(bit != value for bit in bits):
        return int(any(bit == value for bit in bits))
    return sum(bits[i] == value and bits[i - 1] != value for i in range(n))


def gap_composition(target, n):
    chosen = sorted(target)
    gaps = []
    for index, point in enumerate(chosen):
        nxt = chosen[(index + 1) % len(chosen)]
        gaps.append((nxt - point - 1) % n)
    return tuple(sorted(gaps, reverse=True))


def audit_r(r, list_bad):
    n = 2 * r + 1
    k = r - 1
    counter = Counter()
    for word in dyck_words(r):
        counter.update(windows(msw_row(word), k))
    targets = tuple(frozenset(target)
                    for target in combinations(range(1, n + 1), k))
    by_one_runs = defaultdict(Counter)
    by_zero_runs = defaultdict(Counter)
    by_anchor = defaultdict(Counter)
    by_gap = defaultdict(Counter)
    for target in targets:
        bits = tuple(point in target for point in range(1, n + 1))
        value = counter[target]
        by_one_runs[cyclic_runs(bits, True)][value] += 1
        by_zero_runs[cyclic_runs(bits, False)][value] += 1
        by_anchor[n in target][value] += 1
        by_gap[gap_composition(target, n)][value] += 1
    bad = [(tuple(sorted(target)), counter[target]) for target in targets
           if counter[target] == 0 or counter[target] >= 3]
    return {
        "r": r,
        "load_hist": dict(Counter(counter[target] for target in targets)),
        "by_one_runs": {key: dict(value) for key, value in by_one_runs.items()},
        "by_zero_runs": {key: dict(value) for key, value in by_zero_runs.items()},
        "by_anchor": {key: dict(value) for key, value in by_anchor.items()},
        "gap_types": len(by_gap),
        "gap_types_with_deterministic_load": sum(len(hist) == 1
                                                 for hist in by_gap.values()),
        "bad": bad if list_bad else None,
    }


def main(r_min, r_max, list_bad):
    for r in range(r_min, r_max + 1):
        print("CANONICAL_Q1_LOAD_STATISTICS", audit_r(r, list_bad), flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--r-min", type=int, default=3)
    parser.add_argument("--r-max", type=int, default=6)
    parser.add_argument("--list-bad", action="store_true")
    arguments = parser.parse_args()
    main(arguments.r_min, arguments.r_max, arguments.list_bad)
