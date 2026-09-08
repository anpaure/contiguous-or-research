#!/usr/bin/env python3
"""Exact support-independent label-5 slice relaxation for q4 Profile 3.

Profile 3 has two positive period-10 rails centred at exterior label 5.
Its character t_5=-5 forces the other three positive rails to omit 5 and
all five negative rails to contain 5.  Therefore owner equality restricted
to owners containing 5 says:

  the 20 owners of the two positive centre-5 cycles
    =
  the four 5-containing owners from each of the five negative cycles.

This model ranges over all supports and cyclic orders in that slice and
enforces shore simplicity there.  INFEASIBLE rules out Profile 3 globally;
FEASIBLE only shows that the slice relaxation is insufficient.

Substantive runs belong on H100.
"""

from __future__ import annotations

import argparse
import json

from ortools.sat.python import cp_model


V = tuple(range(13))
EXTERIOR = 5

POSITIVE = (
    ("p10c5_1", 10, 5),
    ("p10c5_2", 10, 5),
)
NEGATIVE = (
    ("n10c0", 10, 0),
    ("n10c1", 10, 1),
    ("n10c2", 10, 2),
    ("n11c3", 11, 3),
    ("n11c4", 11, 4),
)


def rail_variables(model, name, period, centre, fix_five_at_zero):
    labels = [x for x in V if x != centre]
    permutation = [
        model.NewIntVar(0, 11, f"perm_{name}_{i}") for i in range(12)
    ]
    inverse = [
        model.NewIntVar(0, 11, f"pos_{name}_{labels[i]}") for i in range(12)
    ]
    model.AddInverse(permutation, inverse)

    if fix_five_at_zero:
        model.Add(permutation[0] == labels.index(EXTERIOR))
    else:
        for i in range(1, period):
            model.Add(permutation[0] < permutation[i])
    model.Add(permutation[1] < permutation[period - 1])
    for i in range(period, 11):
        model.Add(permutation[i] < permutation[i + 1])

    bit_values = [1 << x for x in labels]
    bits = []
    for i in range(period):
        bit = model.NewIntVar(1, 1 << 12, f"bit_{name}_{i}")
        model.AddElement(permutation[i], bit_values, bit)
        bits.append(bit)
    return labels, permutation, bits


def owner_code(model, name, centre, bits, start):
    period = len(bits)
    code = model.NewIntVar(0, (1 << 13) - 1, f"owner_{name}_{start}")
    model.Add(code == (1 << centre) + sum(
        bits[(start + offset) % period] for offset in range(4)
    ))
    return code


def build_model():
    model = cp_model.CpModel()
    positive_codes = []
    negative_codes = []
    rail_data = {}

    for name, period, centre in POSITIVE:
        labels, permutation, bits = rail_variables(
            model, name, period, centre, False
        )
        rail_data[name] = (labels, permutation, period)
        positive_codes.extend(
            owner_code(model, name, centre, bits, start)
            for start in range(period)
        )

    for name, period, centre in NEGATIVE:
        labels, permutation, bits = rail_variables(
            model, name, period, centre, True
        )
        rail_data[name] = (labels, permutation, period)
        negative_codes.extend(
            owner_code(model, name, centre, bits, start)
            for start in (0, period - 1, period - 2, period - 3)
        )

    assert len(positive_codes) == len(negative_codes) == 20
    model.AddAllDifferent(positive_codes)
    model.AddAllDifferent(negative_codes)
    model.Add(sum(positive_codes) == sum(negative_codes))
    matching = [model.NewIntVar(0, 19, f"match_{i}") for i in range(20)]
    model.AddAllDifferent(matching)
    for i, code in enumerate(positive_codes):
        model.AddElement(matching[i], negative_codes, code)

    return model, rail_data


def cycle_from_solver(solver, data):
    labels, permutation, period = data
    return [labels[solver.Value(permutation[i])] for i in range(period)]


def deck(centre, cycle, starts):
    n = len(cycle)
    return {
        frozenset((centre, *(cycle[(start + j) % n] for j in range(4))))
        for start in starts
    }


def solve(seconds, workers, seed):
    model, rail_data = build_model()
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = seconds
    solver.parameters.num_search_workers = workers
    solver.parameters.random_seed = seed
    status = solver.Solve(model)
    report = {
        "status": solver.StatusName(status),
        "wall_time": solver.WallTime(),
        "branches": solver.NumBranches(),
        "conflicts": solver.NumConflicts(),
        "scope": "all supports/orders in the Profile-3 owner slice containing 5",
    }
    if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        cycles = {
            name: cycle_from_solver(solver, data)
            for name, data in rail_data.items()
        }
        positive = set()
        for name, period, centre in POSITIVE:
            part = deck(centre, cycles[name], range(period))
            assert len(part) == period and not (positive & part)
            positive |= part
        negative = set()
        for name, period, centre in NEGATIVE:
            part = deck(
                centre, cycles[name], (0, period - 1, period - 2, period - 3)
            )
            assert len(part) == 4 and not (negative & part)
            negative |= part
        assert positive == negative and len(positive) == 20
        report["cycles"] = cycles
    return report


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--time-limit", type=float, default=1200.0)
    parser.add_argument("--workers", type=int, default=32)
    parser.add_argument("--seed", type=int, default=20260814)
    args = parser.parse_args()
    print(json.dumps({
        "status": "PASS",
        "report": solve(args.time_limit, args.workers, args.seed),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
