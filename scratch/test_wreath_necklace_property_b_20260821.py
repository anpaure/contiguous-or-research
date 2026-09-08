#!/usr/bin/env python3
"""Test 2-colourability of the translation-orbit quotient of wreath decks.

All expensive runs are intended for H100.  For prime b every nontrivial
r-subset has a translation orbit of size b, so a union of quotient vertices
is an exactly point-regular family.  A proper 2-colouring of quotient vertices
with no monochromatic wreath gives two point-regular wreath-free families.
"""

from __future__ import annotations

import argparse
import itertools
from math import comb, factorial

from pysat.solvers import Solver
from pysat.examples.rc2 import RC2
from pysat.formula import WCNF


def rotate_mask(mask: int, shift: int, b: int) -> int:
    all_bits = (1 << b) - 1
    shift %= b
    return ((mask << shift) | (mask >> (b - shift))) & all_bits


def canonical_translation(mask: int, b: int) -> int:
    return min(rotate_mask(mask, t, b) for t in range(b))


def quotient_map(b: int, r: int):
    masks = []
    for subset in itertools.combinations(range(b), r):
        mask = sum(1 << x for x in subset)
        masks.append(mask)
    reps = sorted({canonical_translation(mask, b) for mask in masks})
    rep_to_id = {rep: i for i, rep in enumerate(reps)}
    mask_to_id = {
        mask: rep_to_id[canonical_translation(mask, b)] for mask in masks
    }
    return reps, mask_to_id


def window_mask(order, start: int, r: int) -> int:
    b = len(order)
    return sum(1 << order[(start + j) % b] for j in range(r))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("b", type=int)
    ap.add_argument("r", type=int)
    ap.add_argument("--solver", default="cadical195")
    ap.add_argument("--dedup", action="store_true")
    ap.add_argument("--max-independent", action="store_true")
    args = ap.parse_args()
    b, r = args.b, args.r
    reps, mask_to_id = quotient_map(b, r)
    print(
        f"b={b} r={r} layer={comb(b,r)} quotient_vertices={len(reps)} "
        f"cyclic_orders={(factorial(b-1))}"
    )

    seen = set() if args.dedup else None
    edge_count = 0
    min_support = b
    support_hist = {}
    supports = []
    with Solver(name=args.solver) as solver:
        # Translation fixes the first symbol at 0 without losing a deck type.
        # Reversal duplicates a deck and is harmless.
        for tail in itertools.permutations(range(1, b)):
            order = (0,) + tail
            support = tuple(
                sorted(
                    {
                        mask_to_id[window_mask(order, start, r)]
                        for start in range(b)
                    }
                )
            )
            if seen is not None:
                if support in seen:
                    continue
                seen.add(support)
            edge_count += 1
            min_support = min(min_support, len(support))
            support_hist[len(support)] = support_hist.get(len(support), 0) + 1
            supports.append(support)
            clause = [x + 1 for x in support]
            solver.add_clause(clause)
            solver.add_clause([-x for x in clause])

        sat = solver.solve()
        print(
            f"quotient_edges={edge_count} min_support={min_support} "
            f"support_hist={sorted(support_hist.items())} SAT={sat}"
        )
        if sat:
            model = solver.get_model()
            positive = {i for i in range(len(reps)) if model[i] > 0}
            print(
                f"colour_sizes={len(positive)},{len(reps)-len(positive)} "
                f"positive_reps={[hex(reps[i]) for i in sorted(positive)]}"
            )

    if args.max_independent:
        formula = WCNF()
        for support in supports:
            formula.append([-(x + 1) for x in support])
        for i in range(len(reps)):
            formula.append([i + 1], weight=1)
        with RC2(formula, solver=args.solver) as rc2:
            model = rc2.compute()
            chosen = {i for i in range(len(reps)) if model[i] > 0}
            print(
                f"max_independent={len(chosen)}/{len(reps)} "
                f"chosen_reps={[hex(reps[i]) for i in sorted(chosen)]}"
            )


if __name__ == "__main__":
    main()
