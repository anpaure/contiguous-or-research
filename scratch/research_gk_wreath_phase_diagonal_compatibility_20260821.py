#!/usr/bin/env python3
"""Exact monochromatic physical phase diagonals for GK orientations in wreath decks."""

from __future__ import annotations

import argparse
import itertools
from collections import Counter


def windows(order: tuple[int, ...], size: int) -> tuple[int, ...]:
    b = len(order)
    out = []
    for end in range(b):
        mask = 0
        for q in range(size):
            mask |= 1 << order[(end - q) % b]
        out.append(mask)
    assert len(set(out)) == b
    return tuple(out)


def top_excess(xmask: int, ymask: int, b: int) -> int:
    stack = 0
    unmatched = 0
    for i in range(b):
        for bit in ((xmask >> i) & 1, (ymask >> i) & 1):
            if bit:
                stack += 1
            elif stack:
                stack -= 1
            else:
                unmatched += 1
    assert stack == unmatched
    return unmatched


def audit(b: int) -> dict[str, object]:
    r = (b - 1) // 2
    orders = [(0,) + p for p in itertools.permutations(range(1, b))]
    adecks = [windows(o, r) for o in orders]
    bdecks = [windows(o, b - r) for o in orders]
    amasks = sorted({x for deck in adecks for x in deck})
    bmasks = sorted({y for deck in bdecks for y in deck})
    orient = {(x, y): top_excess(x, y, b) & 1 for x in amasks for y in bmasks}

    hist = Counter()
    agreement_hist = Counter()
    best_agreement = (-1, None)
    good_phase_hist = Counter()
    best_good_phases = (-1, None)
    maximum = (-1, -1)
    examples: dict[tuple[int, int], tuple[tuple[int, ...], tuple[int, ...]]] = {}
    for ai, ad in enumerate(adecks):
        for bi, bd in enumerate(bdecks):
            mono = [0, 0]
            rank_map = lambda x: ((b - 1) // 2 * x) % b
            tau = [1 if rank_map(x) < r else 0 for x in range(b)]
            agreement = 0
            mono_value: list[int | None] = []
            for phase in range(b):
                phase_values = [orient[(ad[i], bd[(phase - i) % b])] for i in range(b)]
                agreement += sum(v == tau[phase] for v in phase_values)
                vals = set(phase_values)
                if len(vals) == 1:
                    mono[next(iter(vals))] += 1
                    mono_value.append(next(iter(vals)))
                else:
                    mono_value.append(None)
            key = (mono[1], mono[0])  # A, B
            hist[key] += 1
            if min(key) > min(maximum) or (min(key) == min(maximum) and sum(key) > sum(maximum)):
                maximum = key
            examples.setdefault(key, (orders[ai], orders[bi]))
            agreement_hist[agreement] += 1
            if agreement > best_agreement[0]:
                best_agreement = (agreement, (orders[ai], orders[bi]))
            good_phases = max(
                sum(mono_value[p] == tau[(p + shift) % b] for p in range(b))
                for shift in range(b)
            )
            good_phase_hist[good_phases] += 1
            if good_phases > best_good_phases[0]:
                best_good_phases = (good_phases, (orders[ai], orders[bi]))

    return {
        "b": b,
        "r": r,
        "orders_each": len(orders),
        "pairs": len(orders) ** 2,
        "hist": dict(sorted(hist.items())),
        "best_balanced": maximum,
        "best_example": examples[maximum],
        "agreement_hist": dict(sorted(agreement_hist.items())),
        "best_agreement": best_agreement,
        "good_phase_hist": dict(sorted(good_phase_hist.items())),
        "best_good_phases": best_good_phases,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--b", type=int, nargs="+", default=[3, 5, 7])
    args = parser.parse_args()
    for b in args.b:
        print(audit(b), flush=True)


if __name__ == "__main__":
    main()
