#!/usr/bin/env python3
"""Enumerate exact self-group blocker children above one removal root.

This is a narrow constructive companion to the blocker DAG.  It avoids
building pair blocker menus: only the self options of currently zero groups
are needed to make the next exact Benders branch.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, "scratch")
from search_q4_k17_z17_reflection_fixed_face_kissat_20260814 import read_instance
from search_q4_k17_z17_reflection_vertex_cover_patch_benders_20260814 import (
    selected_vertices,
)
from search_q4_k17_z17_reflection_exact_blocker_dag_benders_20260814 import (
    inclusion_minimal,
)
from search_q4_k17_z17_reflection_sampled_root_direct_patch_20260814 import (
    direct_patch,
    row_mask,
)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--instance", required=True)
    parser.add_argument("--incumbent", required=True)
    parser.add_argument("--root-mask", required=True)
    parser.add_argument("--report", required=True)
    parser.add_argument("--first-child-artifact", required=True)
    parser.add_argument("--solution", required=True)
    parser.add_argument("--seconds-per-child", type=float, default=0.25)
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--seed", type=int, default=20260814)
    args = parser.parse_args()
    started = time.time()

    _, _, self_options, pair_options = read_instance(args.instance)
    incumbent = json.loads(Path(args.incumbent).read_text())
    vertices = selected_vertices(self_options, pair_options, incumbent)
    root = int(args.root_mask, 0)
    if root >> len(vertices):
        raise ValueError("root mask has bits outside the selected-vertex set")

    self_masks = [row_mask(rows) for _, rows in self_options]
    pair_masks = [row_mask(rows) for rows in pair_options]
    root_summary, root_solution, root_free = direct_patch(
        self_options, pair_options, self_masks, pair_masks, vertices, root,
        args.seconds_per_child, args.workers, args.seed,
    )
    if root_solution is not None:
        Path(args.solution).write_text(json.dumps(root_solution, indent=2,
                                                  sort_keys=True) + "\n")
        raise SystemExit("root already has an exact patch")
    zero_groups = root_summary["zero_groups"]
    if not zero_groups:
        raise ValueError("root has no zero self group")

    row_selected = [0] * 680
    group_vertex = {}
    for position, (kind, _, group, rows) in enumerate(vertices):
        bit = 1 << position
        if kind == "self":
            group_vertex[group] = position
        for row in rows:
            row_selected[row] |= bit

    options_by_group = defaultdict(list)
    for index, (group, rows) in enumerate(self_options):
        blocker = 1 << group_vertex[group]
        for row in rows:
            blocker |= row_selected[row]
        options_by_group[group].append((index, blocker))

    group_branches = {}
    group_children = {}
    for group in zero_groups:
        raw = options_by_group[group]
        distinct_blockers = set(blocker for _, blocker in raw)
        minimal_blockers = inclusion_minimal(distinct_blockers)
        children = inclusion_minimal(root | blocker
                                     for blocker in minimal_blockers)
        children = tuple(child for child in children if child != root)
        if not children:
            raise ValueError(f"zero group {group} produced no proper child")
        realizers = defaultdict(list)
        for option, blocker in raw:
            child = root | blocker
            if child in children:
                realizers[child].append(option)
        group_children[group] = children
        group_branches[str(group)] = {
            "raw_self_options": len(raw),
            "distinct_blockers": len(distinct_blockers),
            "inclusion_minimal_blockers": len(minimal_blockers),
            "inclusion_minimal_children": len(children),
            "minimum_added_vertices": min((child ^ root).bit_count()
                                            for child in children),
            "children": [
                {
                    "mask_hex": hex(child),
                    "added_vertices": [
                        position for position in range(len(vertices))
                        if (child ^ root) >> position & 1
                    ],
                    "realizing_self_option_indices": realizers[child],
                }
                for child in sorted(children,
                                    key=lambda value: ((value ^ root).bit_count(),
                                                       value))
            ],
        }

    chosen_group = min(
        zero_groups,
        key=lambda group: (
            len(group_children[group]),
            min((child ^ root).bit_count() for child in group_children[group]),
            group,
        ),
    )
    ordered_children = sorted(
        group_children[chosen_group],
        key=lambda value: ((value ^ root).bit_count(), value),
    )
    outcomes = []
    solution = None
    for child_number, child in enumerate(ordered_children):
        summary, candidate, free_rows = direct_patch(
            self_options, pair_options, self_masks, pair_masks, vertices,
            child, args.seconds_per_child, args.workers,
            args.seed + child_number + 1,
        )
        entry = {
            "child_number": child_number,
            "mask_hex": hex(child),
            "added_vertices": [
                position for position in range(len(vertices))
                if (child ^ root) >> position & 1
            ],
            "free_rows_list": free_rows,
            **summary,
        }
        outcomes.append(entry)
        if child_number == 0:
            Path(args.first_child_artifact).write_text(json.dumps({
                "root_mask_hex": hex(root),
                "chosen_zero_group": chosen_group,
                **entry,
            }, indent=2, sort_keys=True) + "\n")
        if candidate is not None:
            solution = candidate
            Path(args.solution).write_text(json.dumps(candidate, indent=2,
                                                      sort_keys=True) + "\n")
            break

    report = {
        "status": "PASS" if solution is not None else "NO_CERTIFICATE_IN_ONE_GROUP_BRANCH",
        "scope": "all inclusion-minimal blocker children of the chosen zero self group",
        "instance": args.instance,
        "incumbent": args.incumbent,
        "root_mask_hex": hex(root),
        "root_summary": root_summary,
        "root_free_rows": root_free,
        "zero_groups": zero_groups,
        "chosen_zero_group": chosen_group,
        "group_branches": group_branches,
        "tested_chosen_group_children": len(outcomes),
        "chosen_group_outcomes": outcomes,
        "solution": args.solution if solution is not None else None,
        "first_child_artifact": args.first_child_artifact,
        "elapsed_seconds": time.time() - started,
    }
    Path(args.report).write_text(json.dumps(report, indent=2,
                                           sort_keys=True) + "\n")
    print(json.dumps({key: value for key, value in report.items()
                      if key not in ("group_branches", "chosen_group_outcomes",
                                     "root_free_rows")},
                     indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
