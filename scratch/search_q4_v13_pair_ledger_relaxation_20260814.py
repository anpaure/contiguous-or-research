#!/usr/bin/env python3
"""Exact pair-incidence relaxation of the q4 V13 named-owner gate.

Each rail is represented by a canonical cyclic order on its 10 or 11
selected noncentre labels.  Equality of named 5-owner decks implies exact
equality of every 2-subset incidence row, with the ten target pairs having
surplus one.  This script enforces that necessary pair ledger but not the
full 5-owner ledger.  Thus INFEASIBLE is a support-independent named-owner
obstruction; FEASIBLE is only a relaxation certificate.

Substantive runs belong on H100.
"""

from __future__ import annotations

import argparse
import itertools
import json
from collections import Counter, defaultdict

from ortools.sat.python import cp_model

from search_q4_near_c_five_by_five_v13_atom_20260814 import (
    TARGET,
    V,
    rails_for,
    rails_for_mass5,
)


def pair_coefficient(period: int, left: int, right: int) -> int:
    """Number of cyclic 4-windows containing two positions."""
    distance = min((left - right) % period, (right - left) % period)
    return max(0, 4 - distance)


def build_pair_model(rails):
    model = cp_model.CpModel()
    selected = {}
    permutations = {}
    positions = {}
    pair_count = {}

    for r, rail in enumerate(rails):
        centre = rail["center"]
        period = rail["period"]
        labels = [x for x in V if x != centre]
        label_index = {x: i for i, x in enumerate(labels)}

        permutation = [
            model.NewIntVar(0, 11, f"perm_{rail['name']}_{i}")
            for i in range(12)
        ]
        inverse = [
            model.NewIntVar(0, 11, f"pos_{rail['name']}_{labels[i]}")
            for i in range(12)
        ]
        model.AddInverse(permutation, inverse)
        permutations[r] = permutation
        for x in labels:
            positions[r, x] = inverse[label_index[x]]
            selected[r, x] = model.NewBoolVar(f"sel_{rail['name']}_{x}")
            model.Add(positions[r, x] < period).OnlyEnforceIf(selected[r, x])
            model.Add(positions[r, x] >= period).OnlyEnforceIf(
                selected[r, x].Not()
            )

        # Canonical rotation and reversal of the selected cyclic order.
        for i in range(1, period):
            model.Add(permutation[0] < permutation[i])
        model.Add(permutation[1] < permutation[period - 1])
        # Hole order carries no information.
        for i in range(period, 11):
            model.Add(permutation[i] < permutation[i + 1])

        allowed = [
            (left, right, pair_coefficient(period, left, right))
            if left < period and right < period else (left, right, 0)
            for left in range(12) for right in range(12) if left != right
        ]
        for x, y in itertools.combinations(labels, 2):
            count = model.NewIntVar(0, 3, f"pair_{rail['name']}_{x}_{y}")
            model.AddAllowedAssignments(
                [positions[r, x], positions[r, y], count], allowed
            )
            pair_count[r, frozenset((x, y))] = count

    # Exact point ledger, hence exact binary support layer.
    for x in V:
        terms = []
        for r, rail in enumerate(rails):
            if rail["center"] == x:
                terms.append(rail["sign"] * rail["period"])
            else:
                terms.append(rail["sign"] * 4 * selected[r, x])
        model.Add(sum(terms) == (1 if x in TARGET else 0))

    # Exchange identical rail slots once at support level.
    groups = defaultdict(list)
    for r, rail in enumerate(rails):
        groups[(rail["sign"], rail["period"], rail["center"])].append(r)
    support_code = {
        r: sum((1 << x) * (1 - selected[r, x])
               for x in V if x != rails[r]["center"])
        for r in range(len(rails))
    }
    for group in groups.values():
        for left, right in zip(group, group[1:]):
            model.Add(support_code[left] <= support_code[right])

    # The signed pair projection of the named-owner equation.
    for x, y in itertools.combinations(V, 2):
        pair = frozenset((x, y))
        terms = []
        for r, rail in enumerate(rails):
            if rail["center"] in pair:
                other = y if rail["center"] == x else x
                terms.append(rail["sign"] * 4 * selected[r, other])
            else:
                terms.append(rail["sign"] * pair_count[r, pair])
        model.Add(sum(terms) == (1 if pair <= TARGET else 0))

    return model, selected, permutations


def extract_and_verify(solver, rails, selected, permutations):
    supports = {}
    cycles = {}
    signed_pairs = Counter()
    signed_points = Counter()
    for r, rail in enumerate(rails):
        labels = [x for x in V if x != rail["center"]]
        permutation = [labels[solver.Value(value)] for value in permutations[r]]
        cycle = permutation[:rail["period"]]
        support = {x for x in labels if solver.Value(selected[r, x])}
        assert support == set(cycle)
        assert cycle[0] == min(cycle) and cycle[1] < cycle[-1]
        supports[rail["name"]] = sorted(support)
        cycles[rail["name"]] = cycle

        signed_points[rail["center"]] += rail["sign"] * rail["period"]
        for x in support:
            signed_points[x] += rail["sign"] * 4
            signed_pairs[frozenset((rail["center"], x))] += rail["sign"] * 4
        for x, y in itertools.combinations(support, 2):
            left, right = cycle.index(x), cycle.index(y)
            signed_pairs[frozenset((x, y))] += (
                rail["sign"] * pair_coefficient(rail["period"], left, right)
            )

    assert [signed_points[x] for x in V] == [1] * 5 + [0] * 8
    assert {
        pair: value for pair, value in signed_pairs.items() if value
    } == {
        frozenset(pair): 1 for pair in itertools.combinations(TARGET, 2)
    }
    return supports, cycles


def solve(case, rails, seconds, workers, seed, log_search):
    model, selected, permutations = build_pair_model(rails)
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = seconds
    solver.parameters.num_search_workers = workers
    solver.parameters.random_seed = seed
    solver.parameters.log_search_progress = log_search
    status = solver.Solve(model)
    report = {
        "case": case,
        "status": solver.StatusName(status),
        "wall_time": solver.WallTime(),
        "branches": solver.NumBranches(),
        "conflicts": solver.NumConflicts(),
        "scope": "necessary point-plus-pair ledger",
    }
    if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        supports, cycles = extract_and_verify(
            solver, rails, selected, permutations
        )
        report["supports"] = supports
        report["cycles"] = cycles
    return report


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--branch", choices=("mass4", "mass5"), required=True)
    parser.add_argument("--mass5-profile", type=int, choices=range(1, 7))
    parser.add_argument("--cancel-period", type=int, choices=(10, 11))
    parser.add_argument("--cancel-type", choices=("A", "B", "C", "X"))
    parser.add_argument("--time-limit", type=float, default=1200.0)
    parser.add_argument("--workers", type=int, default=32)
    parser.add_argument("--seed", type=int, default=20260814)
    parser.add_argument("--log-search", action="store_true")
    args = parser.parse_args()

    if args.branch == "mass5":
        if args.mass5_profile is None:
            parser.error("--mass5-profile is required for mass5")
        case = f"mass5_profile_{args.mass5_profile}"
        rails = rails_for_mass5(args.mass5_profile)
    else:
        if args.cancel_period is None or args.cancel_type is None:
            parser.error("--cancel-period and --cancel-type are required for mass4")
        case = f"mass4_p{args.cancel_period}_{args.cancel_type}"
        rails = rails_for(args.cancel_period, args.cancel_type)

    print(json.dumps({
        "status": "PASS",
        "report": solve(
            case, rails, args.time_limit, args.workers, args.seed,
            args.log_search,
        ),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
