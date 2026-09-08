#!/usr/bin/env python3
"""Sample exact vertex-cover patches of a reflection-face incumbent.

Run only on H100. Selected configurations are vertices, and each doubly
loaded owner row is an edge. Removing a vertex cover R leaves outside load
at most one. The zero-load set F_R is then solved exactly, with one self
replacement per destroyed group and the same number of reflected pairs.

For any exact solution S*, R=S\\S* is a vertex cover and S*\\S exactly
covers F_R, so enumeration of all covers is a complete decomposition.
This program samples varied minimal covers and controlled supersets; a
capped negative run is not an infeasibility proof.
"""

from __future__ import annotations

import argparse
import json
import random
from pathlib import Path

from ortools.sat.python import cp_model

from search_q4_k17_z17_reflection_fixed_face_kissat_20260814 import (
    read_instance,
)


def selected_vertices(self_options, pair_options, state):
    vertices = []
    for index in state["self_indices"]:
        group, rows = self_options[index]
        vertices.append(("self", index, group, rows))
    for index in state["pair_indices"]:
        vertices.append(("pair", index, None, pair_options[index]))
    assert len(vertices) == 89
    return vertices


def defect_graph(vertices):
    row_vertices = [[] for _ in range(680)]
    for vertex, (_, _, _, rows) in enumerate(vertices):
        for row in rows:
            row_vertices[row].append(vertex)
    loads = list(map(len, row_vertices))
    assert max(loads) <= 2
    edges = []
    for row, incident in enumerate(row_vertices):
        if len(incident) == 2:
            edges.append((incident[0], incident[1], row))
    energy = sum((load - 1) ** 2 for load in loads)
    assert energy == 2 * len(edges)
    assert loads.count(0) == len(edges)
    return loads, edges


def random_minimal_cover(edges, vertex_count, rng):
    uncovered = set(range(len(edges)))
    incident_edges = [[] for _ in range(vertex_count)]
    for edge_index, (left, right, _) in enumerate(edges):
        incident_edges[left].append(edge_index)
        incident_edges[right].append(edge_index)
    cover = set()
    while uncovered:
        edge_index = rng.choice(tuple(uncovered))
        left, right, _ = edges[edge_index]
        left_degree = sum(index in uncovered for index in incident_edges[left])
        right_degree = sum(index in uncovered for index in incident_edges[right])
        if rng.random() < 0.72:
            chosen = left if left_degree > right_degree else right
            if left_degree == right_degree:
                chosen = rng.choice((left, right))
        else:
            chosen = left if left_degree < right_degree else right
            if left_degree == right_degree:
                chosen = rng.choice((left, right))
        cover.add(chosen)
        uncovered.difference_update(incident_edges[chosen])
    order = list(cover)
    rng.shuffle(order)
    for vertex in order:
        proposed = cover - {vertex}
        if all(left in proposed or right in proposed
               for left, right, _ in edges):
            cover = proposed
    return cover


def patch_instance(self_options, pair_options, vertices, cover):
    retained = [vertex for position, vertex in enumerate(vertices)
                if position not in cover]
    outside_loads = [0] * 680
    for _, _, _, rows in retained:
        for row in rows:
            outside_loads[row] += 1
    assert max(outside_loads) <= 1
    free_rows = {row for row, load in enumerate(outside_loads) if load == 0}
    removed = [vertices[position] for position in sorted(cover)]
    removed_groups = {
        group for kind, _, group, _ in removed if kind == "self"
    }
    removed_pair_count = sum(kind == "pair" for kind, _, _, _ in removed)
    assert len(free_rows) == 4 * len(removed_groups) + 10 * removed_pair_count
    eligible_self = [
        index for index, (group, rows) in enumerate(self_options)
        if group in removed_groups and set(rows) <= free_rows
    ]
    eligible_pairs = [
        index for index, rows in enumerate(pair_options)
        if set(rows) <= free_rows
    ]
    return (retained, free_rows, removed_groups, removed_pair_count,
            eligible_self, eligible_pairs)


def targeted_close_cover(self_options, pair_options, vertices, cover, rng):
    """Greedily add the least retained blockers of a structural zero."""
    self_by_row = [[] for _ in range(680)]
    pair_by_row = [[] for _ in range(680)]
    for index, (_, rows) in enumerate(self_options):
        for row in rows:
            self_by_row[row].append(index)
    for index, rows in enumerate(pair_options):
        for row in rows:
            pair_by_row[row].append(index)
    selected_group_vertex = {
        group: position
        for position, (kind, _, group, _) in enumerate(vertices)
        if kind == "self"
    }
    expansion_steps = 0
    while expansion_steps < len(vertices):
        (retained, free_rows, removed_groups, _,
         eligible_self, eligible_pairs) = patch_instance(
            self_options, pair_options, vertices, cover
        )
        free = set(free_rows)
        row_degree = {row: 0 for row in free}
        eligible_by_group = {group: 0 for group in removed_groups}
        for index in eligible_self:
            group, rows = self_options[index]
            eligible_by_group[group] += 1
            for row in rows:
                row_degree[row] += 1
        for index in eligible_pairs:
            for row in pair_options[index]:
                row_degree[row] += 1

        zero_rows = [row for row, degree in row_degree.items() if degree == 0]
        zero_groups = [group for group, degree in eligible_by_group.items()
                       if degree == 0]
        if not zero_rows and not zero_groups:
            return cover, expansion_steps, None

        occupant = [-1] * 680
        for position, (_, _, _, rows) in enumerate(vertices):
            if position in cover:
                continue
            for row in rows:
                assert occupant[row] < 0
                occupant[row] = position

        candidate_blockers = []
        if zero_groups:
            group = rng.choice(zero_groups)
            candidates = [("self", index)
                          for index, (candidate_group, _) in enumerate(self_options)
                          if candidate_group == group]
        else:
            row = rng.choice(zero_rows)
            candidates = ([('self', index) for index in self_by_row[row]] +
                          [('pair', index) for index in pair_by_row[row]])
        for kind, index in candidates:
            if kind == "self":
                group, rows = self_options[index]
            else:
                group, rows = None, pair_options[index]
            blockers = {occupant[row] for row in rows if occupant[row] >= 0}
            if kind == "self":
                group_vertex = selected_group_vertex[group]
                if group_vertex not in cover:
                    blockers.add(group_vertex)
            if not blockers:
                continue
            blocker_mass = sum(4 if vertices[position][0] == "self" else 10
                               for position in blockers)
            candidate_blockers.append((blocker_mass, len(blockers), blockers))
        if not candidate_blockers:
            return cover, expansion_steps, "NO_BLOCKER_BRANCH"

        # Superset blocker choices are dominated at this Benders node.
        distinct = {frozenset(blockers): (mass, count, blockers)
                    for mass, count, blockers in candidate_blockers}
        minimal = []
        keys = list(distinct)
        for blockers in keys:
            if any(other < blockers for other in keys):
                continue
            minimal.append(distinct[blockers])
        minimal.sort(key=lambda item: (item[0], item[1]))
        best_mass = minimal[0][0]
        low_cost = [item for item in minimal
                    if item[0] <= best_mass + (10 if rng.random() < 0.35 else 0)]
        _, _, chosen = rng.choice(low_cost[:min(12, len(low_cost))])
        old_size = len(cover)
        cover.update(chosen)
        assert len(cover) > old_size
        expansion_steps += 1
    return cover, expansion_steps, "EXPANSION_LIMIT"


def solve_patch(self_options, pair_options, vertices, cover,
                seconds, workers, seed):
    (retained, free_rows, removed_groups, removed_pair_count,
     eligible_self, eligible_pairs) = patch_instance(
        self_options, pair_options, vertices, cover
    )
    incidence = {row: [] for row in free_rows}
    model = cp_model.CpModel()
    self_variables = {
        index: model.NewBoolVar(f"self_{index}") for index in eligible_self
    }
    pair_variables = {
        index: model.NewBoolVar(f"pair_{index}") for index in eligible_pairs
    }
    groups = {group: [] for group in removed_groups}
    for index, variable in self_variables.items():
        group, rows = self_options[index]
        groups[group].append(variable)
        for row in rows:
            incidence[row].append(variable)
    for index, variable in pair_variables.items():
        for row in pair_options[index]:
            incidence[row].append(variable)
    summary = {
        "cover_size": len(cover),
        "free_rows": len(free_rows),
        "removed_self_groups": len(removed_groups),
        "removed_pairs": removed_pair_count,
        "eligible_self": len(eligible_self),
        "eligible_pairs": len(eligible_pairs),
        "minimum_row_degree": min(map(len, incidence.values())),
        "maximum_row_degree": max(map(len, incidence.values())),
    }
    if any(not variables for variables in incidence.values()):
        summary["status"] = "UNCOVERED_ROW"
        return summary, None
    if any(not variables for variables in groups.values()):
        summary["status"] = "UNCOVERED_GROUP"
        return summary, None
    for variables in incidence.values():
        model.AddExactlyOne(variables)
    for variables in groups.values():
        model.AddExactlyOne(variables)
    model.Add(sum(pair_variables.values()) == removed_pair_count)
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
        return summary, None
    chosen_self = {
        index for index, variable in self_variables.items()
        if solver.Value(variable)
    }
    chosen_pairs = {
        index for index, variable in pair_variables.items()
        if solver.Value(variable)
    }
    for kind, index, _, _ in retained:
        (chosen_self if kind == "self" else chosen_pairs).add(index)
    assert len(chosen_self) == 35 and len(chosen_pairs) == 54
    loads = [0] * 680
    for index in chosen_self:
        for row in self_options[index][1]:
            loads[row] += 1
    for index in chosen_pairs:
        for row in pair_options[index]:
            loads[row] += 1
    assert set(loads) == {1}
    state = {
        "status": "PASS",
        "energy": 0,
        "self_indices": sorted(chosen_self),
        "pair_indices": sorted(chosen_pairs),
    }
    return summary, state


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--instance", required=True)
    parser.add_argument("--incumbent", required=True)
    parser.add_argument("--solution", required=True)
    parser.add_argument("--trials", type=int, default=120)
    parser.add_argument("--seconds-per-trial", type=float, default=5)
    parser.add_argument("--workers", type=int, default=12)
    parser.add_argument("--seed", type=int, default=20260814)
    args = parser.parse_args()
    _, _, self_options, pair_options = read_instance(args.instance)
    state = json.load(open(args.incumbent, encoding="utf-8"))
    vertices = selected_vertices(self_options, pair_options, state)
    loads, edges = defect_graph(vertices)
    assert state["energy"] == 2 * len(edges)
    rng = random.Random(args.seed)
    report = {
        "status": "NO_CERTIFICATE_IN_CAPPED_COVERS",
        "incumbent_energy": state["energy"],
        "holes": loads.count(0),
        "double_edges": len(edges),
        "trials": [],
    }
    seen = set()
    all_endpoints = frozenset(
        vertex for left, right, _ in edges for vertex in (left, right)
    )
    for trial in range(args.trials):
        if trial == 0:
            cover = set(all_endpoints)
        else:
            cover = random_minimal_cover(edges, len(vertices), rng)
            band = trial * 4 // max(1, args.trials)
            maximum_extra = (0, 2, 6, 14)[min(3, band)]
            extra_count = rng.randrange(maximum_extra + 1)
            available = list(set(range(len(vertices))) - cover)
            rng.shuffle(available)
            cover.update(available[:extra_count])
        initial_cover_size = len(cover)
        cover, expansion_steps, closure_error = targeted_close_cover(
            self_options, pair_options, vertices, cover, rng
        )
        signature = tuple(sorted(cover))
        if signature in seen:
            continue
        seen.add(signature)
        if closure_error is not None:
            report["trials"].append({
                "trial": trial,
                "initial_cover_size": initial_cover_size,
                "cover_size": len(cover),
                "expansion_steps": expansion_steps,
                "status": closure_error,
            })
            continue
        outcome, solution = solve_patch(
            self_options, pair_options, vertices, cover,
            args.seconds_per_trial, args.workers, args.seed + trial,
        )
        outcome["trial"] = trial
        outcome["initial_cover_size"] = initial_cover_size
        outcome["expansion_steps"] = expansion_steps
        report["trials"].append(outcome)
        if solution is None:
            continue
        Path(args.solution).write_text(
            json.dumps(solution, indent=2, sort_keys=True) + "\n",
            encoding="ascii",
        )
        report.update({
            "status": "PASS",
            "winning_trial": trial,
            "solution": args.solution,
            "selected_self_columns": 35,
            "selected_paired_configurations": 54,
        })
        break
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
