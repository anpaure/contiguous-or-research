#!/usr/bin/env python3
"""Sample exact minimal-cover patches using direct free-row eligibility."""

from __future__ import annotations

import argparse
import itertools
import json
import random
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path

from ortools.sat.python import cp_model

sys.path.insert(0, "scratch")
from search_q4_k17_z17_reflection_fixed_face_kissat_20260814 import read_instance
from search_q4_k17_z17_reflection_vertex_cover_patch_benders_20260814 import (
    defect_graph,
    selected_vertices,
)
from search_q4_k17_z17_reflection_exact_blocker_dag_benders_20260814 import (
    component_minimal_covers,
)


def row_mask(rows) -> int:
    value = 0
    for row in rows:
        value |= 1 << row
    return value


def direct_patch(self_options, pair_options, self_masks, pair_masks,
                 vertices, removal, seconds, workers, seed):
    outside = [0] * 680
    retained = []
    for position, vertex in enumerate(vertices):
        if removal >> position & 1:
            continue
        retained.append(vertex)
        for row in vertex[3]:
            outside[row] += 1
    if max(outside) > 1:
        raise ValueError("removal is not a defect vertex cover")
    free_rows = [row for row, load in enumerate(outside) if load == 0]
    free_mask = row_mask(free_rows)
    removed = [vertices[position] for position in range(len(vertices))
               if removal >> position & 1]
    removed_groups = {group for kind, _, group, _ in removed if kind == "self"}
    removed_pairs = sum(kind == "pair" for kind, _, _, _ in removed)
    if len(free_rows) != 4 * len(removed_groups) + 10 * removed_pairs:
        raise ValueError("free-row mass mismatch")

    eligible_self = [
        index for index, (group, _) in enumerate(self_options)
        if group in removed_groups and not (self_masks[index] & ~free_mask)
    ]
    eligible_pairs = [
        index for index in range(len(pair_options))
        if not (pair_masks[index] & ~free_mask)
    ]
    row_degree = {row: 0 for row in free_rows}
    group_degree = {group: 0 for group in removed_groups}
    for index in eligible_self:
        group, rows = self_options[index]
        group_degree[group] += 1
        for row in rows:
            row_degree[row] += 1
    for index in eligible_pairs:
        for row in pair_options[index]:
            row_degree[row] += 1
    zero_rows = [row for row, degree in row_degree.items() if degree == 0]
    zero_groups = [group for group, degree in group_degree.items() if degree == 0]
    summary = {
        "cover_size": removal.bit_count(),
        "free_rows": len(free_rows),
        "removed_self_groups": len(removed_groups),
        "removed_pairs": removed_pairs,
        "eligible_self": len(eligible_self),
        "eligible_pairs": len(eligible_pairs),
        "minimum_row_degree": min(row_degree.values()),
        "maximum_row_degree": max(row_degree.values()),
        "zero_rows": zero_rows,
        "zero_groups": zero_groups,
    }
    if zero_rows:
        summary["status"] = "UNCOVERED_ROW"
        return summary, None, free_rows
    if zero_groups:
        summary["status"] = "UNCOVERED_GROUP"
        return summary, None, free_rows

    model = cp_model.CpModel()
    self_vars = {i: model.NewBoolVar(f"s{i}") for i in eligible_self}
    pair_vars = {i: model.NewBoolVar(f"p{i}") for i in eligible_pairs}
    incidence = {row: [] for row in free_rows}
    group_vars = {group: [] for group in removed_groups}
    for index, variable in self_vars.items():
        group, rows = self_options[index]
        group_vars[group].append(variable)
        for row in rows:
            incidence[row].append(variable)
    for index, variable in pair_vars.items():
        for row in pair_options[index]:
            incidence[row].append(variable)
    for variables in incidence.values():
        model.AddExactlyOne(variables)
    for variables in group_vars.values():
        model.AddExactlyOne(variables)
    model.Add(sum(pair_vars.values()) == removed_pairs)
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = seconds
    solver.parameters.num_search_workers = workers
    solver.parameters.random_seed = seed % 2_147_483_647
    solver.parameters.randomize_search = True
    status = solver.Solve(model)
    summary.update({
        "status": solver.StatusName(status),
        "wall_time": solver.WallTime(),
        "branches": solver.NumBranches(),
        "conflicts": solver.NumConflicts(),
    })
    if status not in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        return summary, None, free_rows

    chosen_self = {i for i, var in self_vars.items() if solver.Value(var)}
    chosen_pairs = {i for i, var in pair_vars.items() if solver.Value(var)}
    for kind, index, _, _ in retained:
        (chosen_self if kind == "self" else chosen_pairs).add(index)
    loads = [0] * 680
    for index in chosen_self:
        for row in self_options[index][1]: loads[row] += 1
    for index in chosen_pairs:
        for row in pair_options[index]: loads[row] += 1
    if set(loads) != {1}:
        raise ValueError("solver candidate failed exact replay")
    solution = {
        "status": "PASS", "energy": 0,
        "self_indices": sorted(chosen_self),
        "pair_indices": sorted(chosen_pairs),
    }
    return summary, solution, free_rows


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--instance", required=True)
    ap.add_argument("--incumbent", required=True)
    ap.add_argument("--solution", required=True)
    ap.add_argument("--report", required=True)
    ap.add_argument("--structural-artifact", required=True)
    ap.add_argument("--trials", type=int, default=1000)
    ap.add_argument("--seconds-per-leaf", type=float, default=0.25)
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--seed", type=int, default=20260814)
    ap.add_argument("--exclude-root-mask", action="append", default=[])
    args = ap.parse_args()
    started = time.time()
    _, _, self_options, pair_options = read_instance(args.instance)
    incumbent = json.loads(Path(args.incumbent).read_text())
    vertices = selected_vertices(self_options, pair_options, incumbent)
    loads, edges = defect_graph(vertices)
    frontiers = component_minimal_covers(vertices, edges)
    root_count = 1
    for frontier in frontiers: root_count *= len(frontier)
    all_roots = [sum(parts) for parts in itertools.product(*frontiers)]
    if len(all_roots) != root_count or len(set(all_roots)) != root_count:
        raise ValueError("minimal-cover root enumeration mismatch")
    excluded_roots = {int(value, 0) for value in args.exclude_root_mask}
    if not excluded_roots <= set(all_roots):
        raise ValueError("excluded mask is not an inclusion-minimal cover root")
    roots = [root for root in all_roots if root not in excluded_roots]
    rng = random.Random(args.seed)
    strata = defaultdict(list)
    for root in roots: strata[root.bit_count()].append(root)
    for values in strata.values(): rng.shuffle(values)
    ordered = []
    while len(ordered) < min(args.trials, root_count):
        progressed = False
        for size in sorted(strata):
            if strata[size]:
                ordered.append(strata[size].pop())
                progressed = True
                if len(ordered) == min(args.trials, root_count): break
        if not progressed: break

    self_masks = [row_mask(rows) for _, rows in self_options]
    pair_masks = [row_mask(rows) for rows in pair_options]
    outcomes = []
    counts = Counter()
    structural_written = False
    solution = None
    for trial, root in enumerate(ordered):
        outcome, candidate, free_rows = direct_patch(
            self_options, pair_options, self_masks, pair_masks, vertices,
            root, args.seconds_per_leaf, args.workers, args.seed + trial,
        )
        outcome.update({
            "trial": trial,
            "root_mask_hex": hex(root),
            "root_cover": [i for i in range(len(vertices)) if root >> i & 1],
        })
        outcomes.append(outcome)
        counts[outcome["status"]] += 1
        if not structural_written and outcome["status"] in ("UNCOVERED_ROW", "UNCOVERED_GROUP"):
            Path(args.structural_artifact).write_text(json.dumps({
                "status": outcome["status"],
                "trial": trial,
                "root_mask_hex": hex(root),
                "root_cover": outcome["root_cover"],
                "free_rows": free_rows,
                "zero_rows": outcome["zero_rows"],
                "zero_groups": outcome["zero_groups"],
            }, indent=2, sort_keys=True) + "\n")
            structural_written = True
        if candidate is not None:
            solution = candidate
            Path(args.solution).write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n")
            break
        if (trial + 1) % 100 == 0:
            print(json.dumps({"trial": trial+1, "statuses": dict(counts),
                              "elapsed": time.time()-started}, sort_keys=True),
                  file=sys.stderr, flush=True)

    report = {
        "status": "PASS" if solution is not None else "NO_CERTIFICATE_IN_SAMPLED_MINIMAL_ROOTS",
        "scope": "exact patches on stratified sampled inclusion-minimal covers only",
        "instance": args.instance,
        "incumbent": args.incumbent,
        "incumbent_energy": incumbent["energy"],
        "holes": loads.count(0),
        "defect_edges": len(edges),
        "component_frontier_counts": list(map(len, frontiers)),
        "minimal_cover_roots": root_count,
        "eligible_roots_after_exclusion": len(roots),
        "excluded_root_masks": [hex(root) for root in sorted(excluded_roots)],
        "requested_trials": args.trials,
        "tested_trials": len(outcomes),
        "status_histogram": dict(sorted(counts.items())),
        "solution": args.solution if solution is not None else None,
        "structural_artifact": args.structural_artifact if structural_written else None,
        "elapsed_seconds": time.time()-started,
        "trials": outcomes,
    }
    Path(args.report).write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps({k:v for k,v in report.items() if k != "trials"}, indent=2, sort_keys=True))


if __name__ == "__main__": main()
