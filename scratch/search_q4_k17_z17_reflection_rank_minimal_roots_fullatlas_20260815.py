#!/usr/bin/env python3
"""Rank a stratified read-only sample of minimal defect covers by leaf structure."""

from __future__ import annotations

import argparse
import itertools
import json
import random
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, "scratch")
from search_q4_k17_z17_reflection_fixed_face_kissat_20260814 import read_instance
from search_q4_k17_z17_reflection_vertex_cover_patch_benders_20260814 import (
    defect_graph,
    selected_vertices,
)
from search_q4_k17_z17_reflection_exact_blocker_dag_benders_20260814 import (
    component_minimal_covers,
)


def row_mask(rows):
    value = 0
    for row in rows:
        value |= 1 << row
    return value


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--instance", required=True)
    parser.add_argument("--incumbent", required=True)
    parser.add_argument("--trials", type=int, default=1000)
    parser.add_argument("--seed", type=int, default=20260816)
    parser.add_argument("--exclude-root-mask", action="append", default=[])
    parser.add_argument("--artifact", required=True)
    parser.add_argument("--report", required=True)
    args = parser.parse_args()
    started = time.time()

    _, _, self_options, pair_options = read_instance(args.instance)
    incumbent = json.loads(Path(args.incumbent).read_text())
    vertices = selected_vertices(self_options, pair_options, incumbent)
    _, edges = defect_graph(vertices)
    frontiers = component_minimal_covers(vertices, edges)
    all_roots = [sum(parts) for parts in itertools.product(*frontiers)]
    if len(all_roots) != len(set(all_roots)):
        raise ValueError("minimal root enumeration is not unique")
    excluded = {int(value, 0) for value in args.exclude_root_mask}
    if not excluded <= set(all_roots):
        raise ValueError("excluded root is not inclusion-minimal")

    strata = defaultdict(list)
    for root in all_roots:
        if root not in excluded:
            strata[root.bit_count()].append(root)
    rng = random.Random(args.seed)
    for values in strata.values():
        rng.shuffle(values)
    sampled = []
    while len(sampled) < min(args.trials, len(all_roots) - len(excluded)):
        progress = False
        for size in sorted(strata):
            if not strata[size]:
                continue
            sampled.append(strata[size].pop())
            progress = True
            if len(sampled) == args.trials:
                break
        if not progress:
            break

    self_masks = [row_mask(rows) for _, rows in self_options]
    pair_masks = [row_mask(rows) for rows in pair_options]
    outcomes = []
    zero_group_histogram = Counter()
    evaluated_zero_group_roots = 0
    for trial, removal in enumerate(sampled):
        outside = [0] * 680
        for position, vertex in enumerate(vertices):
            if removal >> position & 1:
                continue
            for row in vertex[3]:
                outside[row] += 1
        if max(outside) > 1:
            raise ValueError("sampled removal is not a defect vertex cover")
        free_rows = tuple(row for row, load in enumerate(outside) if load == 0)
        free_mask = row_mask(free_rows)
        removed = [vertices[position] for position in range(len(vertices))
                   if removal >> position & 1]
        removed_groups = sorted({group for kind, _, group, _ in removed
                                 if kind == "self"})
        removed_pairs = sum(kind == "pair" for kind, _, _, _ in removed)
        if len(free_rows) != 4 * len(removed_groups) + 10 * removed_pairs:
            raise ValueError("free-row mass mismatch")

        group_degrees = {group: 0 for group in removed_groups}
        eligible_self = []
        for index, ((group, _), mask) in enumerate(zip(self_options, self_masks)):
            if group in group_degrees and not (mask & ~free_mask):
                eligible_self.append(index)
                group_degrees[group] += 1
        zero_groups = sorted(group for group, degree in group_degrees.items()
                             if degree == 0)
        zero_group_histogram[len(zero_groups)] += 1
        outcome = {
            "trial": trial,
            "root_mask_hex": hex(removal),
            "cover_size": removal.bit_count(),
            "free_rows": len(free_rows),
            "removed_self_groups": removed_groups,
            "removed_pairs": removed_pairs,
            "eligible_self": len(eligible_self),
            "zero_groups": zero_groups,
        }
        if zero_groups:
            outcomes.append(outcome)
            continue

        evaluated_zero_group_roots += 1
        row_degrees = {row: 0 for row in free_rows}
        for index in eligible_self:
            for row in self_options[index][1]:
                row_degrees[row] += 1
        eligible_pairs = 0
        for rows, mask in zip(pair_options, pair_masks):
            if mask & ~free_mask:
                continue
            eligible_pairs += 1
            for row in rows:
                row_degrees[row] += 1
        zero_rows = sorted(row for row, degree in row_degrees.items()
                           if degree == 0)
        outcome.update({
            "eligible_pairs": eligible_pairs,
            "zero_rows": zero_rows,
            "minimum_row_degree": min(row_degrees.values()),
            "maximum_row_degree": max(row_degrees.values()),
            "free_rows_list": free_rows,
        })
        outcomes.append(outcome)
        if (trial + 1) % 100 == 0:
            print(json.dumps({"trial": trial + 1,
                              "zero_group_roots": evaluated_zero_group_roots,
                              "elapsed": time.time() - started}, sort_keys=True),
                  file=sys.stderr, flush=True)

    candidates = [outcome for outcome in outcomes
                  if not outcome["zero_groups"]]
    if not candidates:
        raise ValueError("sample contains no zero-group root")
    candidates.sort(key=lambda item: (
        len(item["zero_rows"]),
        -item["free_rows"],
        -item["minimum_row_degree"],
        -item["eligible_pairs"],
        -item["cover_size"],
        item["root_mask_hex"],
    ))
    best = candidates[0]
    artifact = {
        "status": "FALLBACK_ROOT_CANDIDATE",
        "scope": "read-only structural ranking; no exact patch solve",
        "instance": args.instance,
        "incumbent": args.incumbent,
        "seed": args.seed,
        "sampled_roots": len(sampled),
        "excluded_root_masks": [hex(root) for root in sorted(excluded)],
        **best,
    }
    Path(args.artifact).write_text(json.dumps(artifact, indent=2,
                                             sort_keys=True) + "\n")
    report = {
        "status": "PASS",
        "scope": artifact["scope"],
        "instance": args.instance,
        "incumbent": args.incumbent,
        "minimal_cover_roots": len(all_roots),
        "sampled_roots": len(sampled),
        "excluded_root_masks": artifact["excluded_root_masks"],
        "zero_group_count_histogram": dict(sorted(zero_group_histogram.items())),
        "evaluated_zero_group_roots": evaluated_zero_group_roots,
        "candidate_artifact": args.artifact,
        "best": best,
        "top20": candidates[:20],
        "elapsed_seconds": time.time() - started,
    }
    Path(args.report).write_text(json.dumps(report, indent=2,
                                           sort_keys=True) + "\n")
    print(json.dumps({key: value for key, value in report.items()
                      if key not in ("top20", "best")}, indent=2,
                     sort_keys=True))
    print(json.dumps(best, sort_keys=True))


if __name__ == "__main__":
    main()
