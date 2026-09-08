#!/usr/bin/env python3
"""Solve a fixed-GK selector mapping with OR-Tools CP-SAT."""

from __future__ import annotations

import argparse
import collections
import json
from pathlib import Path

from ortools.sat.python import cp_model


def main(path: Path, out: Path, seconds: float, workers: int,
         minimize_left: bool) -> None:
    data = json.loads(path.read_text())
    recs = data["records"]
    model = cp_model.CpModel()
    xs = [model.new_bool_var(f"x{i}") for i in range(len(recs))]
    by_u: dict[int, list[int]] = collections.defaultdict(list)
    by_l: dict[int, list[int]] = collections.defaultdict(list)
    by_b: dict[int, list[int]] = collections.defaultdict(list)
    for i, r in enumerate(recs):
        by_u[r["upper"]].append(i)
        by_l[r["lower"]].append(i)
        by_b[r["b"]].append(i)
    for ids in by_u.values():
        model.add_exactly_one(xs[i] for i in ids)
    for ids in by_l.values():
        model.add_at_most_one(xs[i] for i in ids)
    for ids in by_b.values():
        model.add_at_most_one(xs[i] for i in ids)
    if minimize_left:
        model.minimize(sum(xs[i] for i, r in enumerate(recs) if r["q"] < r["p"]))
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = seconds
    solver.parameters.num_search_workers = workers
    solver.parameters.log_search_progress = True
    status = solver.solve(model)
    chosen = [r for i, r in enumerate(recs) if solver.boolean_value(xs[i])]
    ans = {
        "status": solver.status_name(status),
        "objective": solver.objective_value if minimize_left and chosen else None,
        "best_bound": solver.best_objective_bound if minimize_left else None,
        "m": data["m"],
        "n": data["n"],
        "chosen": chosen,
    }
    out.write_text(json.dumps(ans, indent=2, sort_keys=True))
    print({"status": ans["status"], "chosen": len(chosen),
           "objective": ans["objective"], "best_bound": ans["best_bound"],
           "conflicts": solver.num_conflicts, "branches": solver.num_branches,
           "wall": solver.wall_time})


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("mapping", type=Path)
    ap.add_argument("output", type=Path)
    ap.add_argument("--seconds", type=float, default=600)
    ap.add_argument("--workers", type=int, default=32)
    ap.add_argument("--minimize-left", action="store_true")
    args = ap.parse_args()
    main(args.mapping, args.output, args.seconds, args.workers, args.minimize_left)
