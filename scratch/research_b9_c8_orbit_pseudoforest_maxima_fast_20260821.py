#!/usr/bin/env python3
"""Fast exact profile of pseudoforest maxima over the b=9 C8 orbit.

This is a research diagnostic.  It uses the row-only form of the
pseudoforest test: a repeated target with d selected owners contributes
d-1 to the cyclomatic demand of the row component containing its owners.
"""

from __future__ import annotations

import argparse
from collections import Counter
from itertools import combinations
from multiprocessing import Pool

from research_b9_c8_orbit_pseudoforest_maxima_20260821 import (
    ADDED,
    REMOVED,
    canonical,
    complete_orbit,
    dyck_words,
    fmt,
    msw_row,
    shadow_stats,
    windows,
)


SUBSET_MASKS = {
    size: tuple(sum(1 << i for i in indices) for indices in combinations(range(14), size))
    for size in range(15)
}


def is_pseudoforest(subset: int, repeated_owner_masks: tuple[int, ...]) -> bool:
    parent = list(range(14))

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x: int, y: int) -> None:
        x, y = find(x), find(y)
        if x != y:
            parent[y] = x

    active = []
    for owner_mask in repeated_owner_masks:
        owners = owner_mask & subset
        if owners & (owners - 1):
            active.append(owners)
            first_bit = owners & -owners
            first = first_bit.bit_length() - 1
            rest = owners ^ first_bit
            while rest:
                bit = rest & -rest
                union(first, bit.bit_length() - 1)
                rest ^= bit

    row_count = [0] * 14
    demand = [0] * 14
    remaining = subset
    while remaining:
        bit = remaining & -remaining
        row_count[find(bit.bit_length() - 1)] += 1
        remaining ^= bit
    for owners in active:
        first = (owners & -owners).bit_length() - 1
        demand[find(first)] += owners.bit_count() - 1
    return all(demand[root] <= row_count[root] for root in range(14))


def maximum_pf_fast(factor, cap: int = 10):
    factor = tuple(sorted(factor))
    target_owners = {}
    for index, row in enumerate(factor):
        for target in windows(row, 3):
            target_owners[target] = target_owners.get(target, 0) | (1 << index)
    repeated = tuple(mask for mask in target_owners.values() if mask & (mask - 1))

    cap = min(cap, len(factor))
    for size in range(cap, -1, -1):
        witnesses = []
        for subset in SUBSET_MASKS[size]:
            if is_pseudoforest(subset, repeated):
                witnesses.append(tuple(factor[i] for i in range(14) if subset >> i & 1))
        if witnesses:
            return size, len(witnesses), witnesses[0]
    raise AssertionError


def analyze_state(state):
    pi, multiplicity, witness = maximum_pf_fast(state)
    return state, pi, multiplicity, witness, shadow_stats(state)


def main(workers: int):
    canonical_factor = tuple(sorted({msw_row(w) for w in dyck_words(4)}))
    fixed = set(canonical_factor) - {canonical(x) for x in REMOVED}
    zero_factor = tuple(sorted(fixed | {canonical(x) for x in ADDED}))
    orbit = complete_orbit(canonical_factor)
    assert len(orbit) == 3014

    pi_hist = Counter()
    joint_hist = Counter()
    best = None
    states = tuple(orbit)
    if workers == 1:
        analyses = map(analyze_state, states)
    else:
        pool = Pool(workers)
        analyses = pool.imap_unordered(analyze_state, states, chunksize=4)
    for state, pi, multiplicity, witness, shadow in analyses:
        pi_hist[pi] += 1
        joint_hist[(pi,) + shadow] += 1
        item = (pi, -shadow[0], -shadow[1], multiplicity, state, witness)
        if best is None or item[:4] > best[:4]:
            best = item
    if workers != 1:
        pool.close()
        pool.join()
    assert best is not None

    print("orbit_states", len(orbit))
    print("pi_hist", sorted(pi_hist.items()))
    print("joint_pi_holes_energy_maxmult")
    for key, count in sorted(joint_hist.items()):
        print(key, count)
    for label, state in (("canonical", canonical_factor), ("zero_shadow", zero_factor)):
        pi, multiplicity, witness = maximum_pf_fast(state)
        print(label, {"pi": pi, "maximum_subsets": multiplicity, "shadow": shadow_stats(state)})
        print(label + "_witness", fmt(witness))
    print("best", {
        "pi": best[0],
        "shadow_holes": -best[1],
        "shadow_energy": -best[2],
        "maximum_subsets": best[3],
    })
    print("best_factor", fmt(best[4]))
    print("best_witness", fmt(best[5]))
    print("B9_C8_ORBIT_PSEUDOFOREST_MAXIMA_FAST_PASS")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=16)
    arguments = parser.parse_args()
    main(arguments.workers)
