#!/usr/bin/env python3
"""CP-SAT companion for mixed period-10/11 Z17 quotient covers."""

from __future__ import annotations

import argparse
import json
import sys

from ortools.sat.python import cp_model

sys.path.insert(0, "scratch")
from search_q4_k17_z17_quotient_exact_cover_20260814 import owner_orbits
from solve_q4_k17_z17_quotient_mixed_sat_20260814 import generate_period, verify


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pool10", type=int, default=50000)
    parser.add_argument("--pool11", type=int, default=50000)
    parser.add_argument("--t", type=int, required=True, choices=range(14))
    parser.add_argument("--time-limit", type=float, default=600.0)
    parser.add_argument("--workers", type=int, default=64)
    parser.add_argument("--seed", type=int, default=20260814)
    args = parser.parse_args()

    representatives, orbit_index = owner_orbits()
    c10, attempts10 = generate_period(args.pool10, 10, args.seed, orbit_index)
    c11, attempts11 = generate_period(args.pool11, 11, args.seed, orbit_index)
    candidates = c10 + c11
    incidence = [[] for _ in representatives]
    for i, candidate in enumerate(candidates):
        for vertex in candidate["edge"]: incidence[vertex].append(i)
    assert all(incidence)

    model = cp_model.CpModel()
    selected = [model.NewBoolVar(f"column_{i}") for i in range(len(candidates))]
    for row in incidence: model.AddExactlyOne(selected[i] for i in row)
    model.Add(sum(selected[len(c10):]) == 10 * args.t)
    model.Add(sum(selected[:len(c10)]) == 143 - 11 * args.t)

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = args.time_limit
    solver.parameters.num_search_workers = args.workers
    solver.parameters.random_seed = args.seed
    status = solver.Solve(model)
    report = {
        "status": solver.StatusName(status), "t": args.t,
        "pool10": len(c10), "pool11": len(c11),
        "attempts10": attempts10, "attempts11": attempts11,
        "min_degree": min(map(len, incidence)),
        "max_degree": max(map(len, incidence)),
        "wall_time": solver.WallTime(), "branches": solver.NumBranches(),
        "conflicts": solver.NumConflicts(),
    }
    if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        chosen = [candidate for i, candidate in enumerate(candidates)
                  if solver.Value(selected[i])]
        rails = verify(chosen)
        report.update({
            "selected_rail_orbits": len(chosen), "developed_rails": rails,
            "period10": sum(c["period"] == 10 for c in chosen),
            "period11": sum(c["period"] == 11 for c in chosen),
            "certificate": [
                {"period": c["period"], "core": list(c["core"]),
                 "order": list(c["order"]),
                 "quotient_edge": list(c["edge"])} for c in chosen
            ],
        })
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__": main()
