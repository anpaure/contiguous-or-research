#!/usr/bin/env python3
"""Exact skeleton/off-skeleton experiments for the Gate-B W2 vector."""

from __future__ import annotations

import argparse
from fractions import Fraction
from itertools import combinations

from research_w2_hahn_venn_exact_20260822 import (
    cells_for_pair,
    central_schur,
    conditional_scalars,
    degree_lookup,
    gram_entry,
    interval_mask,
    masks_of_size,
    orbit_factor,
    residual_fraction,
    signature,
    superset_sums,
)


def vectors(r: int, mode: str):
    b = 2 * r + 1
    all_mask = (1 << b) - 1
    targets = []
    for size in (r, r - 1):
        targets.extend((size, start, interval_mask(b, start, size))
                       for start in range(1, b))
    target_pairs = []
    for first, second in combinations(targets, 2):
        ls, la, left = first
        rs, ra, right = second
        skeleton = ((ls != rs and ((left & right) in (left, right)))
                    or (ls == rs == r and not (left & right)))
        if mode == "skeleton" and not skeleton:
            continue
        if mode == "off" and skeleton:
            continue
        target_pairs.append((
            degree_lookup(b, r, ls, rs),
            degree_lookup(b, r - 1, ls, rs),
            cells_for_pair(all_mask, left, right),
        ))
    by_size = {size: masks_of_size(b, size) for size in (r, r - 1, r - 2)}
    out = {}
    for size, name in ((r, "c_m"), (r - 1, "c_l")):
        base = {interval_mask(b, start, size) for start in range(1, b)}
        out[name] = [int(mask in base) for mask in by_size[size]]
    for size, name, ix in ((r, "w_m", 0), (r - 1, "w_l", 1)):
        vals = []
        for root in by_size[size]:
            vals.append(sum(pair[ix].get(signature(root, pair[2]), 0)
                            for pair in target_pairs))
        out[name] = vals
    qbase = {interval_mask(b, start, r - 2) for start in range(b)}
    out["q"] = [int(mask in qbase) for mask in by_size[r - 2]]
    return b, by_size, out, len(target_pairs)


def run(r: int, mode: str):
    b, masks, coeff, npairs = vectors(r, mode)
    meta = ((r, "c_m"), (r - 1, "c_l"), (r, "w_m"),
            (r - 1, "w_l"), (r - 2, "q"))
    transforms = {name: superset_sums(b, masks[size], coeff[name])
                  for size, name in meta}
    print(f"r={r} mode={mode} pairs={npairs} "
          f"massM={sum(coeff['w_m'])} massL={sum(coeff['w_l'])}")
    for j in range(2, r - 1):
        gram = [[Fraction() for _ in range(5)] for _ in range(5)]
        for a, (sa, na) in enumerate(meta):
            for c, (sc, nc) in enumerate(meta):
                gram[a][c] = gram_entry(b, sa, sc, j,
                                        transforms[na], transforms[nc])
        alpha = residual_fraction(gram)
        a0, delta, xi = conditional_scalars(gram)
        print(f"j={j} alpha={float(alpha):.12g} a0={float(a0):.12g} "
              f"delta={float(delta):.12g} xi={float(xi):.12g} "
              f"prod={float(alpha * orbit_factor(r,j)):.12g}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("r", type=int)
    ap.add_argument("--mode", choices=("all", "skeleton", "off"), default="skeleton")
    ns = ap.parse_args()
    run(ns.r, ns.mode)
