#!/usr/bin/env python3
"""Exact compact V13 q4 named-owner solver via position matching.

Unlike the path/owner-incidence formulation, this model gives each rail a
canonical permutation of its twelve noncentre labels.  The selected cycle
is the first 10 or 11 positions.  Every cyclic 4-window is encoded by its
13-bit owner code.  Owner simplicity is global AllDifferent on each shore,
and exact deck equality is a permutation matching between the positive
codes and the negative codes augmented by the target code.

The formulation ranges over every binary support and every cyclic order.
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
    owner_deck,
    rails_for,
    rails_for_mass5,
)


TARGET_CODE = sum(1 << x for x in TARGET)


def build_model(rails):
    model = cp_model.CpModel()
    selected = {}
    permutations = {}
    positions = {}
    owner_codes = {}
    window_contains = {}

    for r, rail in enumerate(rails):
        centre = rail["center"]
        period = rail["period"]
        labels = [x for x in V if x != centre]
        index = {x: i for i, x in enumerate(labels)}

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
            position = inverse[index[x]]
            positions[r, x] = position
            selected[r, x] = model.NewBoolVar(f"sel_{rail['name']}_{x}")
            model.Add(position < period).OnlyEnforceIf(selected[r, x])
            model.Add(position >= period).OnlyEnforceIf(selected[r, x].Not())

        # One representative of every cyclic order, modulo dihedral action.
        for i in range(1, period):
            model.Add(permutation[0] < permutation[i])
        model.Add(permutation[1] < permutation[period - 1])
        # The unused one/two-hole suffix is an unordered support complement.
        for i in range(period, 11):
            model.Add(permutation[i] < permutation[i + 1])

        bits = []
        bit_values = [1 << x for x in labels]
        for i in range(period):
            bit = model.NewIntVar(1, 1 << 12, f"bit_{rail['name']}_{i}")
            model.AddElement(permutation[i], bit_values, bit)
            bits.append(bit)

        for start in range(period):
            code = model.NewIntVar(0, (1 << 13) - 1,
                                   f"owner_{rail['name']}_{start}")
            model.Add(code == (1 << centre) + sum(
                bits[(start + offset) % period] for offset in range(4)
            ))
            owner_codes[r, start] = code
            window_positions = {
                (start + offset) % period for offset in range(4)
            }
            for x in labels:
                contains = model.NewBoolVar(
                    f"contains_{rail['name']}_{start}_{x}"
                )
                model.AddAllowedAssignments(
                    [positions[r, x], contains],
                    [(position, int(position in window_positions))
                     for position in range(12)],
                )
                window_contains[r, start, x] = contains

    # Exact point/support ledger.
    for x in V:
        terms = []
        for r, rail in enumerate(rails):
            if rail["center"] == x:
                terms.append(rail["sign"] * rail["period"])
            else:
                terms.append(rail["sign"] * 4 * selected[r, x])
        model.Add(sum(terms) == (1 if x in TARGET else 0))

    # Exchange truly identical rail slots at support level.
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

    positive_tokens = [
        (owner_codes[r, start], r, start)
        for r, rail in enumerate(rails) if rail["sign"] > 0
        for start in range(rail["period"])
    ]
    negative_tokens = [
        (owner_codes[r, start], r, start)
        for r, rail in enumerate(rails) if rail["sign"] < 0
        for start in range(rail["period"])
    ]
    positive = [code for code, _, _ in positive_tokens]
    negative = [code for code, _, _ in negative_tokens]
    assert len(positive) == len(negative) + 1

    target_constant = model.NewConstant(TARGET_CODE)
    negative_augmented = negative + [target_constant]
    model.AddAllDifferent(positive)
    model.AddAllDifferent(negative_augmented)
    model.Add(sum(positive) == sum(negative) + TARGET_CODE)

    target_flags = []
    for i, (code, r, _) in enumerate(positive_tokens):
        flag = model.NewBoolVar(f"positive_target_{i}")
        model.Add(code == TARGET_CODE).OnlyEnforceIf(flag)
        model.Add(code != TARGET_CODE).OnlyEnforceIf(flag.Not())
        if rails[r]["center"] not in TARGET:
            model.Add(flag == 0)
        else:
            start = positive_tokens[i][2]
            for x in TARGET - {rails[r]["center"]}:
                model.Add(window_contains[r, start, x] == 1).OnlyEnforceIf(flag)
        target_flags.append(flag)
    model.AddExactlyOne(target_flags)
    for code in negative:
        model.Add(code != TARGET_CODE)

    # A permutation matching is exactly equality of the two simple decks.
    matching = [
        model.NewIntVar(0, len(positive) - 1, f"match_{i}")
        for i in range(len(positive))
    ]
    model.AddAllDifferent(matching)
    for i, code in enumerate(positive):
        model.AddElement(matching[i], negative_augmented, code)
        model.Add(matching[i] == len(negative)).OnlyEnforceIf(target_flags[i])
        model.Add(matching[i] != len(negative)).OnlyEnforceIf(
            target_flags[i].Not()
        )
        positive_rail = positive_tokens[i][1]
        positive_start = positive_tokens[i][2]
        positive_centre = rails[positive_rail]["center"]
        for j, (_, negative_rail, negative_start) in enumerate(negative_tokens):
            negative_centre = rails[negative_rail]["center"]
            if positive_centre == negative_centre:
                continue
            matched = model.NewBoolVar(f"matched_{i}_{j}")
            model.Add(matching[i] == j).OnlyEnforceIf(matched)
            model.Add(matching[i] != j).OnlyEnforceIf(matched.Not())
            # Equal owners must contain both distinct rail centres.
            model.Add(selected[positive_rail, negative_centre] == 1).OnlyEnforceIf(
                matched
            )
            model.Add(selected[negative_rail, positive_centre] == 1).OnlyEnforceIf(
                matched
            )
            model.Add(
                window_contains[positive_rail, positive_start, negative_centre] == 1
            ).OnlyEnforceIf(matched)
            model.Add(
                window_contains[negative_rail, negative_start, positive_centre] == 1
            ).OnlyEnforceIf(matched)

    return model, selected, permutations, owner_codes


def extract_and_verify(solver, rails, selected, permutations):
    supports = {}
    cycles = {}
    point = Counter()
    positive = Counter()
    negative = Counter()
    for r, rail in enumerate(rails):
        labels = [x for x in V if x != rail["center"]]
        permutation = [labels[solver.Value(value)] for value in permutations[r]]
        cycle = permutation[:rail["period"]]
        support = {x for x in labels if solver.Value(selected[r, x])}
        assert support == set(cycle)
        assert cycle[0] == min(cycle) and cycle[1] < cycle[-1]
        supports[rail["name"]] = sorted(support)
        cycles[rail["name"]] = cycle

        point[rail["center"]] += rail["sign"] * rail["period"]
        for x in support:
            point[x] += rail["sign"] * 4
        deck = owner_deck(rail, cycle)
        assert len(deck) == rail["period"] == len(set(deck))
        (positive if rail["sign"] > 0 else negative).update(deck)

    assert [point[x] for x in V] == [1] * 5 + [0] * 8
    assert all(value == 1 for value in positive.values())
    assert all(value == 1 for value in negative.values())
    difference = positive.copy()
    difference.subtract(negative)
    assert {owner: value for owner, value in difference.items() if value} == {
        TARGET: 1
    }
    return supports, cycles, len(negative)


def solve(case, rails, seconds, workers, seed, log_search):
    model, selected, permutations, _ = build_model(rails)
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
        "scope": "all supports and cyclic orders; exact simple owner decks",
    }
    if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        supports, cycles, common = extract_and_verify(
            solver, rails, selected, permutations
        )
        report["supports"] = supports
        report["cycles"] = cycles
        report["common_owner_count"] = common
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
