#!/usr/bin/env python3
"""Profile the pseudoforest compiler over the complete b=9 C8 orbit.

Intended execution environment: H100 only.  This is a research diagnostic,
not part of the analytic compiler proof.
"""

from __future__ import annotations

from collections import Counter, deque
from itertools import combinations

from search_b9_c8_switch_path_20260821 import (
    ADDED,
    REMOVED,
    canonical,
    dyck_words,
    msw_row,
    neighbours,
    repeated_incidence_is_pseudoforest,
    windows,
)


def maximum_pf(factor, cap=10):
    factor = tuple(sorted(factor))
    cap = min(cap, len(factor))
    for size in range(cap, -1, -1):
        witnesses = []
        for indices in combinations(range(len(factor)), size):
            rows = tuple(factor[i] for i in indices)
            if repeated_incidence_is_pseudoforest(rows):
                witnesses.append(rows)
        if witnesses:
            return size, len(witnesses), witnesses[0]
    raise AssertionError


def shadow_stats(factor):
    mult = Counter(target for row in factor for target in windows(row, 3))
    return 84 - len(mult), sum(v * (v - 1) // 2 for v in mult.values()), max(mult.values())


def complete_orbit(start):
    queue = deque([start])
    seen = {start}
    while queue:
        state = queue.popleft()
        for nxt, _ in neighbours(state):
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
    return seen


def fmt(rows):
    return [" ".join(map(str, row)) for row in rows]


def main():
    canonical_factor = tuple(sorted({msw_row(w) for w in dyck_words(4)}))
    assert len(canonical_factor) == 14
    fixed = set(canonical_factor) - {canonical(x) for x in REMOVED}
    zero_factor = tuple(sorted(fixed | {canonical(x) for x in ADDED}))
    assert shadow_stats(zero_factor)[0] == 0

    orbit = complete_orbit(canonical_factor)
    assert len(orbit) == 3014
    pi_hist = Counter()
    joint_hist = Counter()
    best = None
    for state in orbit:
        pi, multiplicity, witness = maximum_pf(state)
        shadow = shadow_stats(state)
        pi_hist[pi] += 1
        joint_hist[(pi,) + shadow] += 1
        item = (pi, -shadow[0], -shadow[1], multiplicity, state, witness)
        if best is None or item[:4] > best[:4]:
            best = item
    assert best is not None
    print("orbit_states", len(orbit))
    print("pi_hist", sorted(pi_hist.items()))
    print("joint_pi_holes_energy_maxmult")
    for key, count in sorted(joint_hist.items()):
        print(key, count)
    for label, state in (("canonical", canonical_factor), ("zero_shadow", zero_factor)):
        pi, multiplicity, witness = maximum_pf(state)
        shadow = shadow_stats(state)
        print(
            label,
            {"pi": pi, "maximum_subsets": multiplicity, "shadow": shadow},
        )
        print(label + "_witness", fmt(witness))
    print(
        "best",
        {
            "pi": best[0],
            "shadow_holes": -best[1],
            "shadow_energy": -best[2],
            "maximum_subsets": best[3],
        },
    )
    print("best_factor", fmt(best[4]))
    print("best_witness", fmt(best[5]))
    print("B9_C8_ORBIT_PSEUDOFOREST_MAXIMA_PASS")


if __name__ == "__main__":
    main()
