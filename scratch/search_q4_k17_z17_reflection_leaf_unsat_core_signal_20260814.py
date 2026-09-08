#!/usr/bin/env python3
"""Shrink an exact patch CP UNSAT core into a column-generation signal."""

from __future__ import annotations

import argparse
import json
import sys
import time
from collections import Counter
from pathlib import Path

from ortools.sat.python import cp_model

sys.path.insert(0, "scratch")
from search_q4_k17_z17_reflection_fixed_face_kissat_20260814 import read_instance
from search_q4_k17_z17_reflection_vertex_cover_patch_benders_20260814 import (
    selected_vertices,
)
from search_q4_k17_z17_reflection_sampled_root_direct_patch_20260814 import (
    row_mask,
)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--instance", required=True)
    parser.add_argument("--incumbent", required=True)
    parser.add_argument("--removal-mask", required=True)
    parser.add_argument("--report", required=True)
    parser.add_argument("--artifact", required=True)
    parser.add_argument("--complete-row", action="append", type=int, default=[])
    parser.add_argument("--no-shrink", action="store_true")
    parser.add_argument("--conservative-all", action="store_true")
    parser.add_argument("--heuristic-full-row", action="store_true")
    parser.add_argument("--infeasible-report")
    parser.add_argument("--target-row", type=int)
    parser.add_argument("--seconds", type=float, default=10.0)
    parser.add_argument("--workers", type=int, default=1)
    parser.add_argument("--seed", type=int, default=20260814)
    args = parser.parse_args()
    started = time.time()

    _, _, self_options, pair_options = read_instance(args.instance)
    incumbent = json.loads(Path(args.incumbent).read_text())
    vertices = selected_vertices(self_options, pair_options, incumbent)
    removal = int(args.removal_mask, 0)
    if removal >> len(vertices):
        raise ValueError("removal mask has bits outside selected vertices")

    outside = [0] * 680
    for position, vertex in enumerate(vertices):
        if removal >> position & 1:
            continue
        for row in vertex[3]:
            outside[row] += 1
    if max(outside) > 1:
        raise ValueError("removal is not a defect vertex cover")
    free_rows = tuple(row for row, load in enumerate(outside) if load == 0)
    free_mask = row_mask(free_rows)
    removed = [vertices[position] for position in range(len(vertices))
               if removal >> position & 1]
    removed_groups = tuple(sorted({group for kind, _, group, _ in removed
                                   if kind == "self"}))
    removed_pairs = sum(kind == "pair" for kind, _, _, _ in removed)
    eligible_self = tuple(
        index for index, (group, rows) in enumerate(self_options)
        if group in removed_groups and not (row_mask(rows) & ~free_mask)
    )
    eligible_pairs = tuple(
        index for index, rows in enumerate(pair_options)
        if not (row_mask(rows) & ~free_mask)
    )
    row_self = {row: [] for row in free_rows}
    row_pair = {row: [] for row in free_rows}
    group_self = {group: [] for group in removed_groups}
    for local, index in enumerate(eligible_self):
        group, rows = self_options[index]
        group_self[group].append(local)
        for row in rows:
            row_self[row].append(local)
    for local, index in enumerate(eligible_pairs):
        for row in pair_options[index]:
            row_pair[row].append(local)

    labels = ([f"row:{row}" for row in free_rows]
              + [f"group:{group}" for group in removed_groups]
              + ["pair_count"])
    solve_calls = 0
    wall_sum = 0.0

    def solve(active, return_core=False):
        nonlocal solve_calls, wall_sum
        active = set(active)
        model = cp_model.CpModel()
        self_vars = [model.NewBoolVar(f"s{i}")
                     for i in range(len(eligible_self))]
        pair_vars = [model.NewBoolVar(f"p{i}")
                     for i in range(len(eligible_pairs))]
        assumptions = {}
        for label in labels:
            if label not in active:
                continue
            assumption = model.NewBoolVar(f"a_{label.replace(':', '_')}")
            assumptions[assumption.Index()] = label
            if label.startswith("row:"):
                row = int(label.split(":", 1)[1])
                variables = ([self_vars[i] for i in row_self[row]]
                             + [pair_vars[i] for i in row_pair[row]])
                model.Add(sum(variables) == 1).OnlyEnforceIf(assumption)
            elif label.startswith("group:"):
                group = int(label.split(":", 1)[1])
                model.Add(sum(self_vars[i] for i in group_self[group]) == 1
                          ).OnlyEnforceIf(assumption)
            else:
                model.Add(sum(pair_vars) == removed_pairs).OnlyEnforceIf(
                    assumption)
            model.AddAssumption(assumption)
        solver = cp_model.CpSolver()
        solver.parameters.max_time_in_seconds = args.seconds
        solver.parameters.num_search_workers = args.workers
        solver.parameters.random_seed = args.seed % 2_147_483_647
        status = solver.Solve(model)
        solve_calls += 1
        wall_sum += solver.WallTime()
        core = None
        if return_core and status == cp_model.INFEASIBLE:
            core = []
            for literal in solver.SufficientAssumptionsForInfeasibility():
                index = literal if literal >= 0 else -literal - 1
                core.append(assumptions[index])
        return status, core, solver.WallTime()

    if args.conservative_all and args.heuristic_full_row:
        raise ValueError("choose at most one full-row mode")
    if args.conservative_all:
        if not args.infeasible_report:
            raise ValueError("--conservative-all requires --infeasible-report")
        proof = json.loads(Path(args.infeasible_report).read_text())
        if (proof.get("status") != "INFEASIBLE"
                or proof.get("instance") != args.instance
                or proof.get("removal_mask_hex") != hex(removal)):
            raise ValueError("bound finite-pool INFEASIBLE report mismatch")
        sufficient_core = labels
        initial_wall = 0.0
    elif args.heuristic_full_row:
        if args.infeasible_report:
            raise ValueError("heuristic full-row mode has no INFEASIBLE premise")
        sufficient_core = labels
        initial_wall = 0.0
    else:
        initial_status, sufficient_core, initial_wall = solve(labels, True)
        if initial_status != cp_model.INFEASIBLE:
            raise ValueError("full assumption-tagged leaf is not INFEASIBLE")
    core = list(sufficient_core or labels)
    original_core_size = len(core)
    shrink_statuses = Counter()
    if (not args.no_shrink and not args.conservative_all
            and not args.heuristic_full_row):
        index = 0
        while index < len(core):
            candidate = core[:index] + core[index + 1:]
            status, _, _ = solve(candidate)
            shrink_statuses[cp_model.CpSolver().StatusName(status)] += 1
            if status == cp_model.INFEASIBLE:
                core = candidate
            elif status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
                index += 1
            else:
                raise RuntimeError("UNKNOWN while shrinking UNSAT core")

    core_rows = sorted(int(label.split(":", 1)[1]) for label in core
                       if label.startswith("row:"))
    core_groups = sorted(int(label.split(":", 1)[1]) for label in core
                         if label.startswith("group:"))
    complete_rows = set(args.complete_row)
    row_degrees = {
        row: len(row_self[row]) + len(row_pair[row]) for row in core_rows
    }
    target_candidates = [row for row in core_rows if row not in complete_rows]
    if args.target_row is not None:
        if args.target_row not in target_candidates:
            raise ValueError("forced target row is not an incomplete free row")
        target_row = args.target_row
    else:
        target_row = min(target_candidates,
                         key=lambda row: (row_degrees[row], row)) \
                     if target_candidates else None
    artifact = {
        "status": ("COLUMN_GENERATION_HEURISTIC" if target_row is not None
                   and args.heuristic_full_row else
                   "COLUMN_GENERATION_REQUIRED" if target_row is not None
                   else "CORE_ROWS_ALREADY_COMPLETE"),
        "core_mode": ("heuristic-full-row" if args.heuristic_full_row else
                      "conservative-all" if args.conservative_all else
                      "sufficient" if args.no_shrink else "inclusion-minimal"),
        "core_is_inclusion_minimal": (not args.no_shrink
                                      and not args.conservative_all
                                      and not args.heuristic_full_row),
        "has_infeasibility_premise": bool(args.infeasible_report),
        "bound_infeasible_report": args.infeasible_report,
        "instance": args.instance,
        "incumbent": args.incumbent,
        "removal_mask_hex": hex(removal),
        "removal_vertices": [position for position in range(len(vertices))
                             if removal >> position & 1],
        "free_rows_list": free_rows,
        "free_rows": len(free_rows),
        "removed_self_groups": removed_groups,
        "removed_pairs": removed_pairs,
        "eligible_self": len(eligible_self),
        "eligible_pairs": len(eligible_pairs),
        "minimal_core_labels": core,
        "minimal_core_rows": core_rows,
        "minimal_core_groups": core_groups,
        "minimal_core_has_pair_count": "pair_count" in core,
        "minimal_core_row_degrees": row_degrees,
        "known_complete_rows_for_this_free_set": sorted(complete_rows),
        "target_row": target_row,
        "target_row_degree": row_degrees.get(target_row),
        "target_selection": ("forced-priority" if args.target_row is not None
                             else "minimum-degree"),
    }
    Path(args.artifact).write_text(json.dumps(artifact, indent=2,
                                             sort_keys=True) + "\n")
    report = {
        **artifact,
        "scope": ("heuristic full-row degree expansion without an INFEASIBLE premise"
                  if args.heuristic_full_row else
                  "conservative full constraint set bound to one finite-pool INFEASIBLE patch report"
                  if args.conservative_all else
                  "sufficient assumption core of one finite-pool exact patch leaf"
                  if args.no_shrink else
                  "inclusion-minimal assumption core of one finite-pool exact patch leaf"),
        "all_constraint_count": len(labels),
        "sufficient_core_size": original_core_size,
        "minimal_core_size": len(core),
        "solve_calls": solve_calls,
        "initial_wall_time": initial_wall,
        "solver_wall_time_sum": wall_sum,
        "shrink_statuses": dict(sorted(shrink_statuses.items())),
        "artifact": args.artifact,
        "elapsed_seconds": time.time() - started,
    }
    Path(args.report).write_text(json.dumps(report, indent=2,
                                           sort_keys=True) + "\n")
    print(json.dumps({key: value for key, value in report.items()
                      if key != "free_rows_list"}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
