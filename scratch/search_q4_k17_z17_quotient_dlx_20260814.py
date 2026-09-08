#!/usr/bin/env python3
"""Randomized Algorithm-X companion for the q4 Z17 quotient cover.

It regenerates the deterministic rail-column pool used by the CP-SAT
search and seeks 143 disjoint 10-edges covering all 1430 owner orbits.
Substantive runs belong on H100.
"""

from __future__ import annotations

import argparse
import json
import random
import sys
import time

sys.path.insert(0, "scratch")
from search_q4_k17_z17_quotient_exact_cover_20260814 import (
    PERIOD,
    generate_candidates,
    owner_orbits,
    verify_development,
)


def exact_cover(candidates, universe_size, seed, node_limit, seconds):
    full = (1 << universe_size) - 1
    masks = [sum(1 << v for v in candidate["edge"])
             for candidate in candidates]
    incidence = [[] for _ in range(universe_size)]
    for i, candidate in enumerate(candidates):
        for v in candidate["edge"]:
            incidence[v].append(i)
    rng = random.Random(seed)
    for row in incidence:
        rng.shuffle(row)

    selected = []
    nodes = 0
    deadline = time.monotonic() + seconds

    def recurse(uncovered):
        nonlocal nodes
        nodes += 1
        if nodes > node_limit or time.monotonic() > deadline:
            return None
        if not uncovered:
            return tuple(selected)
        if uncovered.bit_count() != PERIOD * (143 - len(selected)):
            return None

        covered = full ^ uncovered
        scan = uncovered
        best = None
        while scan:
            bit = scan & -scan
            v = bit.bit_length() - 1
            feasible = [i for i in incidence[v] if not (masks[i] & covered)]
            if not feasible:
                return None
            if best is None or len(feasible) < len(best):
                best = feasible
                if len(best) == 1:
                    break
            scan ^= bit

        rng.shuffle(best)
        # Prefer columns whose other vertices currently have fewer choices.
        def score(i):
            total = 0
            for v in candidates[i]["edge"]:
                total += sum(1 for j in incidence[v]
                             if not (masks[j] & covered))
            return total
        best.sort(key=score)
        for i in best:
            selected.append(i)
            answer = recurse(uncovered ^ masks[i])
            if answer is not None:
                return answer
            selected.pop()
        return None

    answer = recurse(full)
    return answer, nodes, [len(row) for row in incidence]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pool-size", type=int, default=20000)
    parser.add_argument("--seed", type=int, default=20260814)
    parser.add_argument("--node-limit", type=int, default=2_000_000)
    parser.add_argument("--time-limit", type=float, default=600.0)
    args = parser.parse_args()

    representatives, orbit_index = owner_orbits()
    candidates, attempts = generate_candidates(
        args.pool_size, args.seed, orbit_index
    )
    selected, nodes, degrees = exact_cover(
        candidates, len(representatives), args.seed,
        args.node_limit, args.time_limit,
    )
    report = {
        "status": "FEASIBLE" if selected is not None else "UNKNOWN",
        "pool_size": len(candidates),
        "candidate_attempts": attempts,
        "nodes": nodes,
        "min_degree": min(degrees),
        "max_degree": max(degrees),
    }
    if selected is not None:
        chosen = [candidates[i] for i in selected]
        rails, owners, point = verify_development(chosen)
        report.update({
            "selected_rail_orbits": len(chosen),
            "developed_rails": rails,
            "covered_owners": owners,
            "point_degree": sorted(set(point.values())),
            "certificate": [
                {"core": list(candidate["core"]),
                 "order": list(candidate["order"]),
                 "quotient_edge": list(candidate["edge"])}
                for candidate in chosen
            ],
        })
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
