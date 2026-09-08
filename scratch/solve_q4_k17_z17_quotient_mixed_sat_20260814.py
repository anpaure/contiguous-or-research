#!/usr/bin/env python3
"""Mixed period-10/11 CNF exact cover for the q4 Z17 quotient.

Candidate pools are closed under nonzero multipliers.  Exact owner rows
automatically force b=10t period-11 columns and a=143-11t period-10
columns.  Build, solve, and decode only on H100.
"""

from __future__ import annotations

import argparse
import itertools
import json
import random
import sys
from collections import Counter

sys.path.insert(0, "scratch")
from search_q4_k17_z17_quotient_exact_cover_20260814 import (
    K, Q, R, canonical_orbit_mask, deck_masks, owner_orbits,
    translate_values,
)


def generate_period(pool_size, period, seed, orbit_index):
    rng = random.Random(seed + 1009 * period)
    candidates = []
    seen = set()
    attempts = 0
    while len(candidates) < pool_size:
        attempts += 1
        core = tuple(sorted(rng.sample(range(K), 5)))
        complement = [x for x in range(K) if x not in core]
        order = rng.sample(complement, period)
        rng.shuffle(order)
        for multiplier in range(1, K):
            moved_core = tuple(sorted(multiplier * x % K for x in core))
            moved_order = tuple(multiplier * x % K for x in order)
            edge = tuple(sorted(
                orbit_index[canonical_orbit_mask(owner)]
                for owner in deck_masks(moved_core, moved_order)
            ))
            if len(set(edge)) != period or edge in seen:
                continue
            seen.add(edge)
            candidates.append({
                "period": period,
                "core": moved_core,
                "order": moved_order,
                "edge": edge,
            })
    return candidates, attempts


def write_cnf(candidates, universe_size, cnf_path):
    incidence = [[] for _ in range(universe_size)]
    for i, candidate in enumerate(candidates, 1):
        for vertex in candidate["edge"]:
            incidence[vertex].append(i)
    assert all(incidence)
    next_variable = len(candidates) + 1
    clauses = []
    for row in incidence:
        clauses.append(tuple(row))
        sequential = list(range(next_variable, next_variable + len(row) - 1))
        next_variable += len(row) - 1
        clauses.append((-row[0], sequential[0]))
        for i in range(1, len(row) - 1):
            clauses.append((-row[i], sequential[i]))
            clauses.append((-sequential[i - 1], sequential[i]))
            clauses.append((-row[i], -sequential[i - 1]))
        clauses.append((-row[-1], -sequential[-1]))
    with open(cnf_path, "w", encoding="ascii") as stream:
        stream.write(f"p cnf {next_variable - 1} {len(clauses)}\n")
        for clause in clauses:
            stream.write(" ".join(map(str, clause)) + " 0\n")
    return next_variable - 1, len(clauses), min(map(len, incidence)), max(map(len, incidence))


def build(pool10, pool11, seed, cnf_path, map_path):
    representatives, orbit_index = owner_orbits()
    c10, a10 = generate_period(pool10, 10, seed, orbit_index)
    c11, a11 = generate_period(pool11, 11, seed, orbit_index)
    candidates = c10 + c11
    variables, clauses, minimum, maximum = write_cnf(
        candidates, len(representatives), cnf_path
    )
    with open(map_path, "w", encoding="utf-8") as stream:
        json.dump({
            "owner_orbits": len(representatives),
            "pool10": len(c10), "pool11": len(c11),
            "attempts10": a10, "attempts11": a11,
            "candidates": [
                {"period": c["period"], "core": list(c["core"]),
                 "order": list(c["order"]), "edge": list(c["edge"])}
                for c in candidates
            ],
        }, stream)
    print(json.dumps({
        "status": "BUILT", "variables": variables, "clauses": clauses,
        "pool10": len(c10), "pool11": len(c11),
        "attempts10": a10, "attempts11": a11,
        "min_degree": minimum, "max_degree": maximum,
    }, sort_keys=True))


def verify(chosen):
    owners = set()
    point = Counter()
    for candidate in chosen:
        for shift in range(K):
            core = translate_values(candidate["core"], shift)
            order = translate_values(candidate["order"], shift)
            deck = deck_masks(core, order)
            assert len(set(deck)) == candidate["period"]
            assert not (set(deck) & owners)
            owners.update(deck)
            for owner in deck:
                for x in range(K):
                    if owner >> x & 1:
                        point[x] += 1
    assert len(owners) == 24310
    assert set(point.values()) == {12870}
    return len(chosen) * K


def decode(map_path, solution_path):
    data = json.load(open(map_path, encoding="utf-8"))
    status = None
    values = []
    for line in open(solution_path, encoding="ascii", errors="ignore"):
        if line.startswith("s "): status = line.strip()
        if line.startswith("v "):
            values.extend(int(x) for x in line.split()[1:] if x != "0")
    assert status and "SATISFIABLE" in status and "UNSATISFIABLE" not in status
    indices = sorted(v - 1 for v in values if 1 <= v <= len(data["candidates"]))
    chosen = [data["candidates"][i] for i in indices]
    loads = [0] * data["owner_orbits"]
    for candidate in chosen:
        for vertex in candidate["edge"]: loads[vertex] += 1
    assert set(loads) == {1}
    counts = Counter(candidate["period"] for candidate in chosen)
    assert 10 * counts[10] + 11 * counts[11] == 1430
    assert counts[11] % 10 == 0
    rails = verify(chosen)
    print(json.dumps({
        "status": "PASS", "period_counts": dict(counts),
        "selected_rail_orbits": len(chosen), "developed_rails": rails,
        "covered_owners": 24310, "point_degree": [12870],
        "certificate": [
            {"period": c["period"], "core": c["core"],
             "order": c["order"], "quotient_edge": c["edge"]}
            for c in chosen
        ],
    }, indent=2, sort_keys=True))


def main():
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    b = sub.add_parser("build")
    b.add_argument("--pool10", type=int, default=100000)
    b.add_argument("--pool11", type=int, default=100000)
    b.add_argument("--seed", type=int, default=20260814)
    b.add_argument("--cnf", required=True); b.add_argument("--map", required=True)
    d = sub.add_parser("decode")
    d.add_argument("--map", required=True); d.add_argument("--solution", required=True)
    args = parser.parse_args()
    if args.command == "build":
        build(args.pool10, args.pool11, args.seed, args.cnf, args.map)
    else: decode(args.map, args.solution)


if __name__ == "__main__":
    main()
