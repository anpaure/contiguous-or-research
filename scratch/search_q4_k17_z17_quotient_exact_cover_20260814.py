#!/usr/bin/env python3
"""Search a Z17-invariant q4 rank-9 owner factor by quotient exact cover.

Every nontrivial 9-subset orbit under translation has size 17, so the
rank-9 layer has 1430 quotient vertices.  A period-10 pure rail whose ten
owners lie in distinct translation orbits gives one 10-edge.  An exact
cover by 143 such edges develops to a factor of all 24,310 owners.

All substantive runs belong on H100.
"""

from __future__ import annotations

import argparse
import itertools
import json
import random
from collections import Counter

from ortools.sat.python import cp_model


K = 17
R = 9
Q = 4
CORE_SIZE = 5
PERIOD = 10
FULL_MASK = (1 << K) - 1


def rotate_mask(mask, shift):
    shift %= K
    return ((mask << shift) | (mask >> (K - shift))) & FULL_MASK


def canonical_orbit_mask(mask):
    return min(rotate_mask(mask, shift) for shift in range(K))


def subset_mask(values):
    return sum(1 << value for value in values)


def translate_values(values, shift):
    return tuple((value + shift) % K for value in values)


def deck_masks(core, order):
    core_mask = subset_mask(core)
    n = len(order)
    return tuple(
        core_mask | subset_mask(order[(start + offset) % n]
                                for offset in range(Q))
        for start in range(n)
    )


def owner_orbits():
    representatives = {
        canonical_orbit_mask(subset_mask(owner))
        for owner in itertools.combinations(range(K), R)
    }
    assert len(representatives) == 1430
    ordered = tuple(sorted(representatives))
    return ordered, {mask: i for i, mask in enumerate(ordered)}


def generate_candidates(pool_size, seed, orbit_index):
    rng = random.Random(seed)
    candidates = []
    seen_edges = set()
    attempts = 0
    while len(candidates) < pool_size:
        attempts += 1
        core = tuple(sorted(rng.sample(range(K), CORE_SIZE)))
        complement = [x for x in range(K) if x not in core]
        support = rng.sample(complement, PERIOD)
        rng.shuffle(support)
        owners = deck_masks(core, support)
        edge = tuple(sorted(
            orbit_index[canonical_orbit_mask(owner)] for owner in owners
        ))
        if len(set(edge)) != PERIOD or edge in seen_edges:
            continue
        seen_edges.add(edge)
        candidates.append({
            "core": core,
            "order": tuple(support),
            "edge": edge,
        })
    return candidates, attempts


def generate_group_closed_candidates(pool_size, seed, orbit_index):
    """Generate whole multiplier orbits of quotient columns."""
    rng = random.Random(seed)
    candidates = []
    seen_edges = set()
    attempts = 0
    while len(candidates) < pool_size:
        attempts += 1
        core = tuple(sorted(rng.sample(range(K), CORE_SIZE)))
        complement = [x for x in range(K) if x not in core]
        support = rng.sample(complement, PERIOD)
        rng.shuffle(support)
        for multiplier in range(1, K):
            moved_core = tuple(sorted((multiplier * x) % K for x in core))
            moved_order = tuple((multiplier * x) % K for x in support)
            owners = deck_masks(moved_core, moved_order)
            edge = tuple(sorted(
                orbit_index[canonical_orbit_mask(owner)] for owner in owners
            ))
            if len(set(edge)) != PERIOD or edge in seen_edges:
                continue
            seen_edges.add(edge)
            candidates.append({
                "core": moved_core,
                "order": moved_order,
                "edge": edge,
            })
    return candidates, attempts


def solve_cover(candidates, universe_size, seconds, workers, seed):
    incidence = [[] for _ in range(universe_size)]
    for i, candidate in enumerate(candidates):
        for vertex in candidate["edge"]:
            incidence[vertex].append(i)
    if any(not row for row in incidence):
        return "UNCOVERED_VERTEX", None, incidence, None

    model = cp_model.CpModel()
    chosen = [model.NewBoolVar(f"edge_{i}") for i in range(len(candidates))]
    for row in incidence:
        model.AddExactlyOne(chosen[i] for i in row)
    model.Add(sum(chosen) == universe_size // PERIOD)

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = seconds
    solver.parameters.num_search_workers = workers
    solver.parameters.random_seed = seed
    status = solver.Solve(model)
    if status not in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        return solver.StatusName(status), None, incidence, solver
    selected = [i for i, value in enumerate(chosen) if solver.Value(value)]
    return solver.StatusName(status), selected, incidence, solver


def verify_development(selected_candidates):
    owners = set()
    point = Counter()
    rail_count = 0
    for candidate in selected_candidates:
        core = candidate["core"]
        order = candidate["order"]
        for shift in range(K):
            rail_count += 1
            shifted_core = translate_values(core, shift)
            shifted_order = translate_values(order, shift)
            assert len(set(shifted_core)) == CORE_SIZE
            assert len(set(shifted_order)) == PERIOD
            assert not (set(shifted_core) & set(shifted_order))
            deck = deck_masks(shifted_core, shifted_order)
            assert len(set(deck)) == PERIOD
            assert not (set(deck) & owners)
            owners.update(deck)
            for owner in deck:
                assert owner.bit_count() == R
                for point_label in range(K):
                    if owner >> point_label & 1:
                        point[point_label] += 1
    assert rail_count == 143 * 17 == 2431
    assert len(owners) == 24310
    assert len(owners) == sum(1 for _ in itertools.combinations(range(K), R))
    assert set(point.values()) == {12870}
    return rail_count, len(owners), point


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pool-size", type=int, default=50000)
    parser.add_argument("--time-limit", type=float, default=1200.0)
    parser.add_argument("--workers", type=int, default=64)
    parser.add_argument("--seed", type=int, default=20260814)
    parser.add_argument("--group-closed", action="store_true")
    args = parser.parse_args()

    representatives, orbit_index = owner_orbits()
    generator = (generate_group_closed_candidates if args.group_closed
                 else generate_candidates)
    candidates, attempts = generator(args.pool_size, args.seed, orbit_index)
    status, selected, incidence, solver = solve_cover(
        candidates, len(representatives), args.time_limit,
        args.workers, args.seed,
    )
    report = {
        "status": status,
        "owner_orbits": len(representatives),
        "candidate_pool": len(candidates),
        "candidate_attempts": attempts,
        "min_vertex_degree": min(map(len, incidence)),
        "max_vertex_degree": max(map(len, incidence)),
    }
    if solver is not None:
        report.update({
            "wall_time": solver.WallTime(),
            "branches": solver.NumBranches(),
            "conflicts": solver.NumConflicts(),
        })
    if selected is not None:
        selected_candidates = [candidates[i] for i in selected]
        rails, owners, point = verify_development(selected_candidates)
        report.update({
            "selected_rail_orbits": len(selected_candidates),
            "developed_rails": rails,
            "covered_owners": owners,
            "point_degree": sorted(set(point.values())),
            "certificate": [
                {"core": list(candidate["core"]),
                 "order": list(candidate["order"]),
                 "quotient_edge": list(candidate["edge"])}
                for candidate in selected_candidates
            ],
        })
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
