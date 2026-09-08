#!/usr/bin/env python3
"""Run CP-SAT exact cover on a prebuilt Z17 candidate-map JSON (H100)."""

import argparse
import json
import sys

from ortools.sat.python import cp_model

sys.path.insert(0, "scratch")
from solve_q4_k17_z17_quotient_mixed_sat_20260814 import verify


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--map", required=True)
    parser.add_argument("--time-limit", type=float, default=900)
    parser.add_argument("--workers", type=int, default=32)
    parser.add_argument("--seed", type=int, default=20260814)
    args = parser.parse_args()
    data = json.load(open(args.map, encoding="utf-8"))
    candidates = data["candidates"]
    incidence = [[] for _ in range(data["owner_orbits"])]
    for i, candidate in enumerate(candidates):
        for vertex in candidate["edge"]: incidence[vertex].append(i)
    model = cp_model.CpModel()
    selected = [model.NewBoolVar(f"column_{i}") for i in range(len(candidates))]
    for row in incidence: model.AddExactlyOne(selected[i] for i in row)
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = args.time_limit
    solver.parameters.num_search_workers = args.workers
    solver.parameters.random_seed = args.seed
    status = solver.Solve(model)
    report = {
        "status": solver.StatusName(status), "candidate_pool": len(candidates),
        "min_degree": min(map(len, incidence)), "max_degree": max(map(len, incidence)),
        "wall_time": solver.WallTime(), "branches": solver.NumBranches(),
        "conflicts": solver.NumConflicts(),
    }
    if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        chosen = [candidate for i, candidate in enumerate(candidates)
                  if solver.Value(selected[i])]
        rails = verify(chosen)
        counts = {p: sum(c["period"] == p for c in chosen) for p in (10, 11)}
        report.update({
            "period_counts": counts, "selected_rail_orbits": len(chosen),
            "developed_rails": rails, "covered_owners": 24310,
            "point_degree": [12870], "certificate": [
                {"period": c["period"], "core": c["core"],
                 "order": c["order"], "quotient_edge": c["edge"]}
                for c in chosen],
        })
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__": main()
