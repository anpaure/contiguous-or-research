#!/usr/bin/env python3
"""Random self-lift bank followed by an exact residual pair cover (H100)."""

from __future__ import annotations

import argparse
import json
import random
import sys

from ortools.sat.python import cp_model

sys.path.insert(0, "scratch")
from build_q4_k17_z17_reflection_stochastic_instance_20260814 import make_instance
from search_q4_k17_z17_quotient_exact_cover_20260814 import verify_development


def choose_disjoint_self(groups, rng):
    order = list(range(35))
    rng.shuffle(order)
    chosen = {}
    used = set()
    for group in order:
        options = groups[group].copy()
        rng.shuffle(options)
        feasible = [i for i in options if used.isdisjoint(i[1])]
        if not feasible: return None
        # Prefer footprints whose rows have appeared least in the current
        # partial bank; all are disjoint, so random tie-breaking is enough.
        index, rows = feasible[0]
        chosen[group] = index
        used.update(rows)
    return [chosen[group] for group in range(35)], used


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--map", required=True)
    parser.add_argument("--sample", type=int, default=0)
    parser.add_argument("--trials", type=int, default=20)
    parser.add_argument("--seconds-per-trial", type=float, default=10)
    parser.add_argument("--workers", type=int, default=16)
    parser.add_argument("--seed", type=int, default=20260814)
    args = parser.parse_args()
    _, self_options, pairs = make_instance(args.map, args.sample, args.seed)
    groups = [[] for _ in range(35)]
    for i, (group, _, rows) in enumerate(self_options):
        groups[group].append((i, frozenset(rows)))
    rng = random.Random(args.seed)
    report = {"status": "NO_CERTIFICATE", "trials": []}

    for trial in range(args.trials):
        bank = None
        for _ in range(100):
            bank = choose_disjoint_self(groups, rng)
            if bank is not None: break
        if bank is None: continue
        chosen_self, used = bank
        residual = set(range(680)) - used
        eligible = [i for i, (_, rows) in enumerate(pairs)
                    if set(rows) <= residual]
        incidence = {row: [] for row in residual}
        for position, pair_index in enumerate(eligible):
            for row in pairs[pair_index][1]: incidence[row].append(position)
        if any(not row for row in incidence.values()):
            report["trials"].append({"trial": trial, "status": "UNCOVERED_ROW"})
            continue
        model = cp_model.CpModel()
        variables = [model.NewBoolVar(f"pair_{i}") for i in eligible]
        for row in incidence.values(): model.AddExactlyOne(variables[i] for i in row)
        model.Add(sum(variables) == 54)
        solver = cp_model.CpSolver()
        solver.parameters.max_time_in_seconds = args.seconds_per_trial
        solver.parameters.num_search_workers = args.workers
        solver.parameters.random_seed = args.seed + trial
        status = solver.Solve(model)
        outcome = {
            "trial": trial,
            "status": solver.StatusName(status),
            "eligible_pairs": len(eligible),
            "min_residual_degree": min(map(len, incidence.values())),
            "max_residual_degree": max(map(len, incidence.values())),
            "wall_time": solver.WallTime(),
        }
        report["trials"].append(outcome)
        if status not in (cp_model.OPTIMAL, cp_model.FEASIBLE): continue
        chosen_pairs = [eligible[i] for i, variable in enumerate(variables)
                        if solver.Value(variable)]
        assert len(chosen_pairs) == 54
        chosen = [self_options[i][1] for i in chosen_self]
        for i in chosen_pairs: chosen.extend(pairs[i][0])
        assert len(chosen) == 143
        loads = [0] * 1430
        for column in chosen:
            for vertex in column["edge"]: loads[vertex] += 1
        assert set(loads) == {1}
        normalized = [
            {"core": tuple(column["core"]),
             "order": tuple(column["order"]),
             "edge": tuple(column["edge"])} for column in chosen
        ]
        rails, owners, point = verify_development(normalized)
        report.update({
            "status": "PASS", "winning_trial": trial,
            "selected_rail_orbits": 143, "selected_self_columns": 35,
            "selected_paired_configurations": 54,
            "developed_rails": rails, "covered_owners": owners,
            "point_degree": sorted(set(point.values())),
            "certificate": [
                {"core": list(column["core"]),
                 "order": list(column["order"]),
                 "quotient_edge": list(column["edge"])}
                for column in normalized
            ],
        })
        break
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__": main()
