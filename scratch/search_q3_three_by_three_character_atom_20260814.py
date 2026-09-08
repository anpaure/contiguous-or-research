#!/usr/bin/env python3
"""H100-only exact-cover search for the character-forced q=3 3x3 atom.

Normal form (by relabelling H={0,1,2,3}):
  positive: two period-8 rails centred at 0, one period-9 rail containing H;
  negative: one period-8 rail centred at each of 1,2,3.
All six decks must be simple on their shore and differ by exactly H.
"""

from __future__ import annotations

import argparse
import itertools
import json
import os
import time
from collections import Counter, defaultdict


V = 10
H = frozenset({0, 1, 2, 3})


def deck(center: int, cycle: tuple[int, ...]) -> frozenset[frozenset[int]]:
    n = len(cycle)
    return frozenset(
        frozenset((center, cycle[i], cycle[(i + 1) % n], cycle[(i + 2) % n]))
        for i in range(n)
    )


def canonical_cycles(center: int, period: int):
    available = tuple(x for x in range(V) if x != center)
    for support in itertools.combinations(available, period):
        root = min(support)
        tail = tuple(x for x in support if x != root)
        for perm in itertools.permutations(tail):
            cycle = (root,) + perm
            if cycle[1] > cycle[-1]:
                continue
            yield cycle


def rails(center: int, period: int, must_contain_h: bool | None = None):
    ans = []
    seen = set()
    for cycle in canonical_cycles(center, period):
        values = deck(center, cycle)
        if must_contain_h is not None and (H in values) != must_contain_h:
            continue
        if values in seen:
            continue
        seen.add(values)
        ans.append((cycle, values))
    return ans


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    started = time.time()

    p8 = rails(0, 8, False)
    p9 = rails(0, 9, True)
    # By the stabilizer of H and the exterior labels, period-9 H-rails with
    # centre 0 are one orbit.  Fix the canonical representative.
    canonical_cycle = tuple(range(1, V))
    canonical_values = deck(0, canonical_cycle)
    p9_choice = next((canonical_cycle, canonical_values) for _ in [0] if H in canonical_values)
    negative = {z: rails(z, 8, False) for z in (1, 2, 3)}

    print(
        f"host={os.uname().nodename} p8={len(p8)} p9_all={len(p9)} "
        + " ".join(f"n{z}={len(negative[z])}" for z in negative)
        + f" generated_seconds={time.time()-started:.3f}",
        flush=True,
    )

    # Index negative rails by an owner they contain.  For each disjoint pair
    # of positive 8-rails, recursively exact-cover its 24-owner collateral.
    by_owner = {
        z: defaultdict(list) for z in negative
    }
    for z in negative:
        for i, (_, values) in enumerate(negative[z]):
            for owner in values:
                by_owner[z][owner].append(i)

    p9_cycle, p9_values = p9_choice
    base = p9_values - {H}
    checked_pairs = 0
    for i, (cycle_i, values_i) in enumerate(p8):
        if values_i & base:
            continue
        for j in range(i + 1, len(p8)):
            cycle_j, values_j = p8[j]
            if values_j & base or values_j & values_i:
                continue
            target = frozenset(base | values_i | values_j)
            assert len(target) == 24
            checked_pairs += 1

            # Each negative centre z can only cover target owners containing z.
            options = {}
            for z in (1, 2, 3):
                eligible = set()
                for owner in target:
                    eligible.update(by_owner[z].get(owner, ()))
                options[z] = [idx for idx in eligible if negative[z][idx][1] <= target]
                if not options[z]:
                    break
            else:
                # Choose smallest candidate fibre first; the centres are roles,
                # so preserve their labels in the returned assignment.
                order = sorted((1, 2, 3), key=lambda z: len(options[z]))
                chosen = {}

                def search(depth: int, uncovered: frozenset[frozenset[int]]) -> bool:
                    if depth == 3:
                        return not uncovered
                    z = order[depth]
                    for idx in options[z]:
                        values = negative[z][idx][1]
                        if values <= uncovered:
                            chosen[z] = idx
                            if search(depth + 1, frozenset(uncovered - values)):
                                return True
                    return False

                if search(0, target):
                    plus = [(0, p9_cycle, p9_values), (0, cycle_i, values_i), (0, cycle_j, values_j)]
                    minus = [(z, *negative[z][chosen[z]]) for z in (1, 2, 3)]
                    pcov = Counter(owner for _, _, values in plus for owner in values)
                    mcov = Counter(owner for _, _, values in minus for owner in values)
                    assert set(pcov.values()) == {1} and set(mcov.values()) == {1}
                    assert pcov - mcov == Counter({H: 1}) and not (mcov - pcov)

                    def show(row):
                        center, cycle, values = row
                        return {
                            "center": center,
                            "period": len(cycle),
                            "cycle": cycle,
                            "deck": sorted(map(sorted, values)),
                        }

                    result = {
                        "host": os.uname().nodename,
                        "q": 3,
                        "ground_size": V,
                        "H": sorted(H),
                        "checked_positive_pairs": checked_pairs,
                        "plus": [show(row) for row in plus],
                        "minus": [show(row) for row in minus],
                    }
                    with open(args.output, "w", encoding="utf-8") as handle:
                        json.dump(result, handle, indent=2, sort_keys=True)
                        handle.write("\n")
                    print(f"FOUND checked_pairs={checked_pairs} output={args.output}", flush=True)
                    return
    print(f"NONE checked_pairs={checked_pairs}", flush=True)
    raise SystemExit(2)


if __name__ == "__main__":
    main()
