#!/usr/bin/env python3
"""Exact memoized DFS over self-group blocker branches for explicit roots.

Pair-column blocker branching is deliberately omitted.  If a group-positive
leaf has a zero row, the run stops and emits that exact free-row artifact for
conditioned pair-column generation.  Otherwise the exact patch CP leaf is
solved and the DFS continues.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, "scratch")
from search_q4_k17_z17_reflection_fixed_face_kissat_20260814 import read_instance
from search_q4_k17_z17_reflection_vertex_cover_patch_benders_20260814 import (
    selected_vertices,
)
from search_q4_k17_z17_reflection_exact_blocker_dag_benders_20260814 import (
    inclusion_minimal,
    minimal_children,
)
from search_q4_k17_z17_reflection_sampled_root_direct_patch_20260814 import (
    direct_patch,
    row_mask,
)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--instance", required=True)
    parser.add_argument("--incumbent", required=True)
    parser.add_argument("--root-mask", action="append", required=True)
    parser.add_argument("--solution", required=True)
    parser.add_argument("--report", required=True)
    parser.add_argument("--trace", required=True)
    parser.add_argument("--structural-artifact", required=True)
    parser.add_argument("--seconds-per-leaf", type=float, default=0.25)
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--seed", type=int, default=20260814)
    parser.add_argument("--max-nodes", type=int, default=1_000_000)
    parser.add_argument("--time-limit", type=float, default=900.0)
    args = parser.parse_args()
    started = time.time()
    deadline = time.monotonic() + args.time_limit

    _, _, self_options, pair_options = read_instance(args.instance)
    incumbent = json.loads(Path(args.incumbent).read_text())
    vertices = selected_vertices(self_options, pair_options, incumbent)
    roots = tuple(int(value, 0) for value in args.root_mask)
    if any(root >> len(vertices) for root in roots):
        raise ValueError("root mask has bits outside selected vertices")
    if len(set(roots)) != len(roots):
        raise ValueError("duplicate root mask")

    self_masks = [row_mask(rows) for _, rows in self_options]
    pair_masks = [row_mask(rows) for rows in pair_options]
    row_selected = [0] * 680
    group_vertex = {}
    for position, (kind, _, group, rows) in enumerate(vertices):
        bit = 1 << position
        if kind == "self":
            group_vertex[group] = position
        for row in rows:
            row_selected[row] |= bit
    group_raw = defaultdict(list)
    for _, (group, rows) in enumerate(self_options):
        blocker = 1 << group_vertex[group]
        for row in rows:
            blocker |= row_selected[row]
        group_raw[group].append(blocker)
    group_menus = {
        group: inclusion_minimal(blockers)
        for group, blockers in group_raw.items()
    }

    def missing_groups(removal: int):
        complement = ~removal
        return tuple(
            group for group, vertex in sorted(group_vertex.items())
            if removal >> vertex & 1
            and not any(not (blocker & complement)
                        for blocker in group_menus[group])
        )

    trace = open(args.trace, "w", encoding="utf-8")
    stack = [(root_number, root, 0)
             for root_number, root in reversed(tuple(enumerate(roots)))]
    memo = set()
    node_count = branch_nodes = leaf_nodes = 0
    forced_nodes = 0
    maximum_depth = maximum_stack = 0
    branch_groups = Counter()
    child_counts = Counter()
    leaf_statuses = Counter()
    solution = None
    structural = None
    status = "RUNNING"
    try:
        while stack and node_count < args.max_nodes and time.monotonic() < deadline:
            root_number, removal, depth = stack.pop()
            if removal in memo:
                continue
            memo.add(removal)
            node_count += 1
            maximum_depth = max(maximum_depth, depth)
            zero_groups = missing_groups(removal)
            if zero_groups:
                choices = []
                for group in zero_groups:
                    children = minimal_children(removal, group_menus[group])
                    if not children:
                        raise ValueError(f"zero group {group} has no blocker child")
                    choices.append((len(children),
                                    min((child ^ removal).bit_count()
                                        for child in children),
                                    group, children))
                _, _, group, children = min(choices)
                ordered = sorted(children,
                                 key=lambda child: ((child ^ removal).bit_count(),
                                                    child))
                branch_nodes += 1
                forced_nodes += len(ordered) == 1
                branch_groups[group] += 1
                child_counts[len(ordered)] += 1
                trace.write(json.dumps({
                    "event": "branch", "root_number": root_number,
                    "depth": depth, "removal_mask_hex": hex(removal),
                    "zero_groups": zero_groups, "chosen_group": group,
                    "children": [hex(child) for child in ordered],
                }, sort_keys=True) + "\n")
                for child in reversed(ordered):
                    stack.append((root_number, child, depth + 1))
                maximum_stack = max(maximum_stack, len(stack))
                continue

            summary, candidate, free_rows = direct_patch(
                self_options, pair_options, self_masks, pair_masks, vertices,
                removal, args.seconds_per_leaf, args.workers,
                args.seed + leaf_nodes,
            )
            leaf_nodes += 1
            if summary["zero_groups"]:
                raise ValueError("group-positive node replayed with a zero group")
            leaf_statuses[summary["status"]] += 1
            trace.write(json.dumps({
                "event": "leaf", "root_number": root_number,
                "depth": depth, "removal_mask_hex": hex(removal),
                "summary": summary,
            }, sort_keys=True) + "\n")
            trace.flush()
            if candidate is not None:
                solution = candidate
                Path(args.solution).write_text(json.dumps(candidate, indent=2,
                                                          sort_keys=True) + "\n")
                status = "PASS"
                break
            if summary["status"] in ("UNCOVERED_ROW", "UNCOVERED_GROUP"):
                structural = {
                    "root_number": root_number,
                    "depth": depth,
                    "removal_mask_hex": hex(removal),
                    "removal_vertices": [
                        position for position in range(len(vertices))
                        if removal >> position & 1
                    ],
                    "free_rows_list": free_rows,
                    **summary,
                }
                Path(args.structural_artifact).write_text(json.dumps(
                    structural, indent=2, sort_keys=True) + "\n")
                status = "NEEDS_COLUMNS"
                break
            if node_count % 1000 == 0:
                print(json.dumps({
                    "nodes": node_count, "leaves": leaf_nodes,
                    "memo": len(memo), "stack": len(stack),
                    "leaf_statuses": dict(leaf_statuses),
                    "elapsed": time.time() - started,
                }, sort_keys=True), file=sys.stderr, flush=True)
    finally:
        trace.close()

    if status == "RUNNING":
        if not stack:
            status = ("COMPLETE_WITH_UNKNOWN_LEAVES"
                      if leaf_statuses.get("UNKNOWN", 0)
                      else "COMPLETE_GROUP_DFS_NO_SAT")
        elif node_count >= args.max_nodes:
            status = "MAX_NODES"
        else:
            status = "TIME_LIMIT"
    report = {
        "status": status,
        "scope": "complete self-group blocker DFS above the explicit roots; pair blocker expansion only on emitted structural leaves",
        "instance": args.instance,
        "incumbent": args.incumbent,
        "roots": [hex(root) for root in roots],
        "roots_requested": len(roots),
        "nodes": node_count,
        "memo_size": len(memo),
        "remaining_stack": len(stack),
        "branch_nodes": branch_nodes,
        "forced_nodes": forced_nodes,
        "leaf_nodes": leaf_nodes,
        "leaf_statuses": dict(sorted(leaf_statuses.items())),
        "branch_groups": dict(sorted(branch_groups.items())),
        "branch_child_count_histogram": dict(sorted(child_counts.items())),
        "maximum_depth": maximum_depth,
        "maximum_stack": maximum_stack,
        "solution": args.solution if solution is not None else None,
        "structural_artifact": args.structural_artifact if structural else None,
        "elapsed_seconds": time.time() - started,
        "trace": args.trace,
    }
    Path(args.report).write_text(json.dumps(report, indent=2,
                                           sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
