#!/usr/bin/env python3
"""Exact blocker-DAG search above every minimal defect vertex cover.

Run only on H100.  Every catalogue option C is assigned the bit mask B_C
of incumbent configurations that block it (plus the selected member of
its self group).  At removal mask R, C is eligible exactly when B_C is a
subset of R.  A free row or destroyed self group with no eligible option
gives an exact Benders branch R <- R union B_C.

The inclusion-minimal vertex covers are obtained as the product of the
defect graph's connected-component frontiers.  Every target difference
contains one of these roots.  Memoization merges the blocker expansions.
Capped runs seek a certificate; only exhaustive completion of the whole
DAG with no UNKNOWN leaves would prove the fixed face infeasible.
"""

from __future__ import annotations

import argparse
import itertools
import json
import random
import sys
import time
from collections import Counter
from pathlib import Path

sys.path.insert(0, "scratch")
from search_q4_k17_z17_reflection_fixed_face_kissat_20260814 import (
    read_instance,
)
from search_q4_k17_z17_reflection_vertex_cover_patch_benders_20260814 import (
    defect_graph,
    selected_vertices,
    solve_patch,
)


def inclusion_minimal(masks):
    ordered = sorted(set(masks), key=lambda mask: (mask.bit_count(), mask))
    kept = []
    for mask in ordered:
        if any(previous & mask == previous for previous in kept):
            continue
        kept.append(mask)
    return tuple(kept)


def blocker_catalogue(self_options, pair_options, vertices):
    row_selected = [0] * 680
    group_vertex = {}
    for position, (kind, _, group, rows) in enumerate(vertices):
        bit = 1 << position
        if kind == "self":
            group_vertex[group] = position
        for row in rows:
            row_selected[row] |= bit

    self_blockers = []
    pair_blockers = []
    row_menus = [[] for _ in range(680)]
    group_menus = [[] for _ in range(35)]
    for index, (group, rows) in enumerate(self_options):
        blocker = 1 << group_vertex[group]
        for row in rows:
            blocker |= row_selected[row]
        self_blockers.append(blocker)
        group_menus[group].append(blocker)
        for row in rows:
            row_menus[row].append(blocker)
    for index, rows in enumerate(pair_options):
        blocker = 0
        for row in rows:
            blocker |= row_selected[row]
        pair_blockers.append(blocker)
        for row in rows:
            row_menus[row].append(blocker)
    row_menus = tuple(inclusion_minimal(menu) for menu in row_menus)
    group_menus = tuple(inclusion_minimal(menu) for menu in group_menus)
    return (tuple(row_selected), tuple(self_blockers), tuple(pair_blockers),
            row_menus, group_menus, group_vertex)


def component_minimal_covers(vertices, edges):
    adjacency = {vertex: set() for vertex in range(len(vertices))}
    for left, right, _ in edges:
        adjacency[left].add(right)
        adjacency[right].add(left)
    active = {vertex for vertex, neighbors in adjacency.items() if neighbors}
    components = []
    while active:
        start = next(iter(active))
        component = {start}
        stack = [start]
        active.remove(start)
        while stack:
            vertex = stack.pop()
            for neighbor in adjacency[vertex]:
                if neighbor in active:
                    active.remove(neighbor)
                    component.add(neighbor)
                    stack.append(neighbor)
        components.append(tuple(sorted(component)))

    frontiers = []
    for component in sorted(components, key=lambda values: (len(values), values)):
        local_index = {vertex: index for index, vertex in enumerate(component)}
        local_edges = {
            tuple(sorted((local_index[left], local_index[right])))
            for left, right, _ in edges
            if left in local_index and right in local_index
        }
        covers = []
        for local_mask in range(1 << len(component)):
            if not all(local_mask >> left & 1 or local_mask >> right & 1
                       for left, right in local_edges):
                continue
            minimal = True
            for vertex in range(len(component)):
                if not (local_mask >> vertex & 1):
                    continue
                smaller = local_mask ^ (1 << vertex)
                if all(smaller >> left & 1 or smaller >> right & 1
                       for left, right in local_edges):
                    minimal = False
                    break
            if minimal:
                global_mask = 0
                for position, vertex in enumerate(component):
                    if local_mask >> position & 1:
                        global_mask |= 1 << vertex
                covers.append(global_mask)
        frontiers.append(tuple(covers))
    return tuple(frontiers)


def minimal_children(removal, menu):
    children = {removal | blocker for blocker in menu}
    children.discard(removal)
    return inclusion_minimal(children)


def structural_branch(removal, row_selected, row_menus,
                      group_menus, group_vertex):
    best = None
    best_label = None
    complement = ~removal
    for row, selected_mask in enumerate(row_selected):
        if selected_mask & complement:
            continue
        if any(not (blocker & complement) for blocker in row_menus[row]):
            continue
        children = minimal_children(removal, row_menus[row])
        key = (len(children), min((child ^ removal).bit_count()
                                  for child in children), row)
        if best is None or key < best[0]:
            best = (key, children)
            best_label = ("row", row)
            if key[0] == 1:
                break
    if best is None or best[0][0] > 1:
        for group, vertex in group_vertex.items():
            if not (removal >> vertex & 1):
                continue
            if any(not (blocker & complement) for blocker in group_menus[group]):
                continue
            children = minimal_children(removal, group_menus[group])
            key = (len(children), min((child ^ removal).bit_count()
                                      for child in children), 680 + group)
            if best is None or key < best[0]:
                best = (key, children)
                best_label = ("group", group)
                if key[0] == 1:
                    break
    if best is None:
        return None, ()
    return best_label, best[1]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--instance", required=True)
    parser.add_argument("--incumbent", required=True)
    parser.add_argument("--solution", required=True)
    parser.add_argument("--report", required=True)
    parser.add_argument("--max-nodes", type=int, default=500_000)
    parser.add_argument("--max-leaves", type=int, default=20_000)
    parser.add_argument("--time-limit", type=float, default=900)
    parser.add_argument("--seconds-per-leaf", type=float, default=1)
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--seed", type=int, default=20260814)
    args = parser.parse_args()

    _, _, self_options, pair_options = read_instance(args.instance)
    incumbent = json.load(open(args.incumbent, encoding="utf-8"))
    vertices = selected_vertices(self_options, pair_options, incumbent)
    _, edges = defect_graph(vertices)
    (row_selected, _, _, row_menus,
     group_menus, group_vertex) = blocker_catalogue(
        self_options, pair_options, vertices
    )
    frontiers = component_minimal_covers(vertices, edges)
    root_count = 1
    for frontier in frontiers:
        root_count *= len(frontier)
    assert root_count > 0
    rng = random.Random(args.seed)
    shuffled_frontiers = []
    for frontier in frontiers:
        values = list(frontier)
        rng.shuffle(values)
        shuffled_frontiers.append(values)
    roots = (sum(parts) for parts in itertools.product(*shuffled_frontiers))

    deadline = time.monotonic() + args.time_limit
    memo = set()
    stack = []
    root_position = 0
    nodes = leaves = infeasible_leaves = unknown_leaves = 0
    forced_nodes = branching_nodes = 0
    maximum_stack = 0
    status = "CAPPED"
    solution_state = None

    while (nodes < args.max_nodes and leaves < args.max_leaves
           and time.monotonic() < deadline):
        if not stack:
            try:
                stack.append(next(roots))
            except StopIteration:
                status = ("EXHAUSTED_WITH_UNKNOWN_LEAVES"
                          if unknown_leaves
                          else "EXHAUSTED_ROOT_DAG")
                break
            root_position += 1
        removal = stack.pop()
        if removal in memo:
            continue
        memo.add(removal)
        nodes += 1
        label, children = structural_branch(
            removal, row_selected, row_menus, group_menus, group_vertex
        )
        if children:
            if len(children) == 1:
                forced_nodes += 1
            else:
                branching_nodes += 1
            ordered = sorted(children,
                             key=lambda child: ((child ^ removal).bit_count(),
                                                child), reverse=True)
            stack.extend(ordered)
            maximum_stack = max(maximum_stack, len(stack))
            continue

        leaves += 1
        outcome, candidate = solve_patch(
            self_options, pair_options, vertices,
            {position for position in range(len(vertices))
             if removal >> position & 1},
            args.seconds_per_leaf, args.workers,
            (args.seed + leaves) % 2_147_483_647,
        )
        leaf_status = outcome["status"]
        infeasible_leaves += leaf_status == "INFEASIBLE"
        unknown_leaves += leaf_status == "UNKNOWN"
        if candidate is not None:
            status = "PASS"
            solution_state = candidate
            Path(args.solution).write_text(
                json.dumps(candidate, indent=2, sort_keys=True) + "\n",
                encoding="ascii",
            )
            break

        # An infeasible exact patch at R only rules out target difference
        # exactly R. Any strict target superset contains at least one still
        # retained selected configuration, so singleton expansion is the
        # complete fallback branch. Structural blockers will immediately
        # compress most descendants.
        remaining = [position for position in range(len(vertices))
                     if not (removal >> position & 1)]
        rng.shuffle(remaining)
        stack.extend(removal | (1 << position) for position in remaining)
        maximum_stack = max(maximum_stack, len(stack))

        if nodes % 10_000 == 0:
            print(json.dumps({
                "nodes": nodes, "memo": len(memo), "leaves": leaves,
                "roots_started": root_position, "stack": len(stack),
                "elapsed": args.time_limit - max(0, deadline-time.monotonic()),
            }, sort_keys=True), file=sys.stderr, flush=True)

    report = {
        "status": status,
        "incumbent_energy": incumbent["energy"],
        "defect_edges": len(edges),
        "component_frontier_counts": list(map(len, frontiers)),
        "minimal_cover_roots": root_count,
        "roots_started": root_position,
        "memoized_nodes": len(memo),
        "nodes": nodes,
        "forced_nodes": forced_nodes,
        "branching_nodes": branching_nodes,
        "structurally_positive_leaves": leaves,
        "infeasible_leaves": infeasible_leaves,
        "unknown_leaves": unknown_leaves,
        "maximum_stack": maximum_stack,
        "row_menu_size_histogram": dict(sorted(Counter(
            map(len, row_menus)
        ).items())),
        "group_menu_size_histogram": dict(sorted(Counter(
            map(len, group_menus)
        ).items())),
        "solution": args.solution if solution_state is not None else None,
    }
    Path(args.report).write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="ascii"
    )
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
