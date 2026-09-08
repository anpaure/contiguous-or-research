#!/usr/bin/env python3
"""Repair a low-energy bracelet state with hinted CP-SAT (H100 only)."""

from __future__ import annotations

import argparse
import json
import sys

from ortools.sat.python import cp_model

sys.path.insert(0, "scratch")
from build_q4_k17_z17_reflection_stochastic_instance_20260814 import make_instance
from search_q4_k17_z17_quotient_exact_cover_20260814 import verify_development


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--map", required=True)
    parser.add_argument("--state", required=True)
    parser.add_argument("--sample", type=int, default=0)
    parser.add_argument("--seed", type=int, default=20260814)
    parser.add_argument("--time-limit", type=float, default=300)
    parser.add_argument("--workers", type=int, default=32)
    parser.add_argument("--fix-stable", action="store_true")
    args = parser.parse_args()

    _, self_options, pairs = make_instance(args.map, args.sample, args.seed)
    state = json.load(open(args.state, encoding="utf-8"))
    hinted_self = set(state["self_indices"])
    hinted_pairs = set(state["pair_indices"])
    assert len(hinted_self) == 35 and len(hinted_pairs) == 54

    loads = [0] * 680
    for index in hinted_self:
        for row in self_options[index][2]: loads[row] += 1
    for index in hinted_pairs:
        for row in pairs[index][1]: loads[row] += 1
    energy = sum((load - 1) ** 2 for load in loads)
    assert energy == state["energy"]
    holes = sum(load == 0 for load in loads)
    histogram = {load: loads.count(load) for load in sorted(set(loads))}

    model = cp_model.CpModel()
    self_vars = [model.NewBoolVar(f"self_{i}") for i in range(len(self_options))]
    pair_vars = [model.NewBoolVar(f"pair_{i}") for i in range(len(pairs))]
    groups = [[] for _ in range(35)]
    incidence = [[] for _ in range(680)]
    for i, (group, _, rows) in enumerate(self_options):
        groups[group].append(self_vars[i])
        for row in rows: incidence[row].append(self_vars[i])
    for i, (_, rows) in enumerate(pairs):
        for row in rows: incidence[row].append(pair_vars[i])
    for group in groups: model.AddExactlyOne(group)
    for row in incidence: model.AddExactlyOne(row)
    model.Add(sum(pair_vars) == 54)
    for i, variable in enumerate(self_vars): model.AddHint(variable, int(i in hinted_self))
    for i, variable in enumerate(pair_vars): model.AddHint(variable, int(i in hinted_pairs))
    stable_self = [
        i for i in hinted_self
        if all(loads[row] == 1 for row in self_options[i][2])
    ]
    stable_pairs = [
        i for i in hinted_pairs
        if all(loads[row] == 1 for row in pairs[i][1])
    ]
    if args.fix_stable:
        for i in stable_self: model.Add(self_vars[i] == 1)
        for i in stable_pairs: model.Add(pair_vars[i] == 1)

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = args.time_limit
    solver.parameters.num_search_workers = args.workers
    solver.parameters.random_seed = args.seed
    solver.parameters.repair_hint = True
    solver.parameters.hint_conflict_limit = 200000
    status = solver.Solve(model)
    report = {
        "status": solver.StatusName(status),
        "hint_energy": energy,
        "hint_holes": holes,
        "hint_load_histogram": histogram,
        "self_variables": len(self_options),
        "pair_variables": len(pairs),
        "fixed_stable_self": len(stable_self) if args.fix_stable else 0,
        "fixed_stable_pairs": len(stable_pairs) if args.fix_stable else 0,
        "wall_time": solver.WallTime(),
        "branches": solver.NumBranches(),
        "conflicts": solver.NumConflicts(),
    }
    if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        chosen_self = [i for i, variable in enumerate(self_vars) if solver.Value(variable)]
        chosen_pairs = [i for i, variable in enumerate(pair_vars) if solver.Value(variable)]
        chosen = [self_options[i][1] for i in chosen_self]
        for i in chosen_pairs: chosen.extend(pairs[i][0])
        assert len(chosen_self) == 35 and len(chosen_pairs) == 54 and len(chosen) == 143
        owner_loads = [0] * 1430
        for column in chosen:
            for vertex in column["edge"]: owner_loads[vertex] += 1
        assert set(owner_loads) == {1}
        normalized = [
            {"core": tuple(column["core"]),
             "order": tuple(column["order"]),
             "edge": tuple(column["edge"])}
            for column in chosen
        ]
        rails, owners, point = verify_development(normalized)
        report.update({
            "selected_rail_orbits": len(chosen),
            "selected_self_columns": 35,
            "selected_paired_configurations": 54,
            "developed_rails": rails,
            "covered_owners": owners,
            "point_degree": sorted(set(point.values())),
            "certificate": [
                {"core": list(column["core"]),
                 "order": list(column["order"]),
                 "quotient_edge": list(column["edge"])}
                for column in normalized
            ],
        })
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__": main()
