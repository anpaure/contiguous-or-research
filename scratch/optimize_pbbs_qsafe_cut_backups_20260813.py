#!/usr/bin/env python3
"""Minimize upper-colour rematerializations in the PBBS q-safe cut gate.

Given the actual complement-GK/PBBS owner factor, choose old edges to cut
so every positive run shorter than q is cut.  A backup variable for an
immediate-upper colour is charged iff all its old witnesses are cut.  The
primary objective minimizes backups; the secondary objective minimizes
cuts.  This is still only the piece-cut gate: it does not build new seams.

Substantial instances must be run on h100, not on the local Mac.
"""

from __future__ import annotations

import argparse
import json
import time
from collections import Counter

from ortools.sat.python import cp_model

from audit_pbbs_qsafe_cut_capacity_20260813 import (
    build_factor,
    factor_cycles,
    rank_slack,
    short_run_collars,
)


def solve(m: int, q: int | None, time_limit: float, workers: int) -> dict:
    started = time.time()
    n, edges, adjacency, fibres_dict = build_factor(m)
    cycles = factor_cycles(edges, adjacency)
    if q is None:
        q = rank_slack(n) + 1
    collars, run_hist = short_run_collars(cycles, n, q)
    fibres = list(fibres_dict.items())

    model = cp_model.CpModel()
    cut = [model.new_bool_var(f"c{e}") for e in range(len(edges))]
    backup = [model.new_bool_var(f"b{u}") for u in range(len(fibres))]
    for collar in collars:
        model.add(sum(cut[e] for e in collar) >= 1)
    for u, (_, fibre) in enumerate(fibres):
        # Either an old witness remains, or this colour is rematerialized.
        model.add(sum(1 - cut[e] for e in fibre) + backup[u] >= 1)

    # One backup dominates every possible cut count, giving a lexicographic
    # objective without a second solve.
    weight = len(edges) + 1
    model.minimize(weight * sum(backup) + sum(cut))

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = time_limit
    solver.parameters.num_search_workers = workers
    solver.parameters.random_seed = 1729
    solver.parameters.log_search_progress = False
    status = solver.solve(model)
    feasible = status in (cp_model.OPTIMAL, cp_model.FEASIBLE)
    cuts = [e for e in range(len(edges)) if feasible and solver.value(cut[e])]
    backups = [u for u in range(len(fibres)) if feasible and solver.value(backup[u])]

    if feasible:
        cut_set = set(cuts)
        assert all(any(e in cut_set for e in collar) for collar in collars)
        for u, (_, fibre) in enumerate(fibres):
            assert any(e not in cut_set for e in fibre) or u in backups

    backup_fibre_hist = Counter(len(fibres[u][1]) for u in backups)
    cut_upper_mult_hist = Counter(len(fibres_dict[edges[e][2]]) for e in cuts)
    return {
        "m": m,
        "n": n,
        "q": q,
        "edges": len(edges),
        "components": len(cycles),
        "short_collars": len(collars),
        "positive_run_hist": {str(k): v for k, v in sorted(run_hist.items())},
        "status": solver.status_name(status),
        "objective_bound": solver.best_objective_bound if feasible else None,
        "cuts": len(cuts) if feasible else None,
        "backups": len(backups) if feasible else None,
        "backup_fibre_hist": {str(k): v for k, v in sorted(backup_fibre_hist.items())},
        "cut_upper_multiplicity_hist": {
            str(k): v for k, v in sorted(cut_upper_mult_hist.items())
        },
        "cut_edge_ids": cuts,
        "backup_colours": [fibres[u][0] for u in backups],
        "wall_seconds": time.time() - started,
        "solver_wall_seconds": solver.wall_time,
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("m", type=int)
    ap.add_argument("--q", type=int)
    ap.add_argument("--time-limit", type=float, default=300.0)
    ap.add_argument("--workers", type=int, default=16)
    ap.add_argument("--json")
    args = ap.parse_args()
    result = solve(args.m, args.q, args.time_limit, args.workers)
    payload = json.dumps(result, indent=2, sort_keys=True)
    print(payload)
    if args.json:
        with open(args.json, "w", encoding="utf-8") as out:
            out.write(payload + "\n")


if __name__ == "__main__":
    main()
