#!/usr/bin/env python3
"""Batch wrapper for the optimized Hall/DM core, with exact Python fallback."""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict, deque
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scratch"))

from fast_k15_compiler_hall import maximum_matching
from sigma_multirow_linear_compiler import linear_erosion


def middle_from(path: Path) -> list[int]:
    payload = json.loads(path.read_text())
    row = payload.get("middle_path") or payload.get("middle_cycle")
    if not row and len(payload.get("middle_components", [])) == 1:
        row = payload["middle_components"][0]
    if not row:
        raise ValueError(f"{path}: no single middle path")
    return list(map(int, row))


def fixed_targets_from(path: Path | None) -> set[int]:
    if path is None:
        return set()
    payload = json.loads(path.read_text())
    if isinstance(payload, list):
        return set(map(int, payload))
    for key in ("dm_targets", "witness_targets", "targets", "zero_targets"):
        if payload.get(key):
            return set(map(int, payload[key]))
    return set()


def graph(middle: list[int], k: int, depth: int):
    allowed = linear_erosion(middle, k, depth)
    required: dict[tuple[int, ...], int] = defaultdict(int)
    for start, target in enumerate(middle):
        for bit in range(k):
            if not (target >> bit) & 1:
                continue
            carriers = tuple(
                p for p in range(start, start + depth + 1)
                if (allowed[p] >> bit) & 1
            )
            if not carriers:
                return None, [start, bit]
            required[carriers] |= 1 << bit
    middle_rank = middle[0].bit_count()
    targets = [
        value for value in range(1, 1 << k)
        if value.bit_count() < middle_rank
    ]
    index = {value: i for i, value in enumerate(targets)}
    adjacency = [[] for _ in targets]
    cells = []
    for row_depth in range(depth):
        for start in range(len(allowed) - row_depth):
            positions = tuple(range(start, start + row_depth + 1))
            masks = tuple(allowed[p] for p in positions)
            envelope = 0
            for value in masks:
                envelope |= value
            mandatory = 0
            for bits in range(1, 1 << len(positions)):
                subset = tuple(
                    positions[i] for i in range(len(positions))
                    if (bits >> i) & 1
                )
                mandatory |= required.get(subset, 0)
            ci = len(cells)
            cells.append((row_depth, start, envelope, mandatory, masks))
            target = envelope
            while target:
                ti = index.get(target)
                if (
                    ti is not None
                    and not (mandatory & ~target)
                    and all(value & target for value in masks)
                ):
                    adjacency[ti].append(ci)
                target = (target - 1) & envelope
    return (targets, cells, adjacency), None


def python_audit(source: Path, k: int, depth: int, fixed: set[int],
                 distances: bool):
    built, failure = graph(middle_from(source), k, depth)
    if built is None:
        return {
            "source": str(source), "status": "NOT_FACTORABLE",
            "structural_failure": failure,
        }
    targets, cells, adjacency = built
    left_match, right_match = maximum_matching(adjacency, len(cells))
    unmatched = [i for i, value in enumerate(left_match) if value < 0]
    zeros = [i for i, row in enumerate(adjacency) if not row]
    left_seen = set(unmatched)
    right_seen = set()
    queue = deque((0, i) for i in unmatched)
    while queue:
        side, value = queue.popleft()
        if side == 0:
            for cell in adjacency[value]:
                if cell != left_match[value] and cell not in right_seen:
                    right_seen.add(cell)
                    queue.append((1, cell))
        else:
            target = right_match[value]
            if target >= 0 and target not in left_seen:
                left_seen.add(target)
                queue.append((0, target))
    dm_targets = [targets[i] for i in sorted(left_seen)]
    dm_cells = sorted(right_seen)
    result = {
        "source": str(source),
        "status": "PASS" if not unmatched else "HALL_DEFICIENT",
        "targets": len(targets), "cells": len(cells),
        "matching": len(targets) - len(unmatched),
        "deficiency": len(unmatched), "zero_candidates": len(zeros),
        "unmatched_targets": [targets[i] for i in unmatched],
        "zero_targets": [targets[i] for i in zeros],
        "dm_left": len(left_seen), "dm_right": len(right_seen),
        "dm_targets": dm_targets, "dm_cell_indices": dm_cells,
        "dm_target_rank_histogram": dict(Counter(x.bit_count() for x in dm_targets)),
        "dm_cell_depth_histogram": dict(Counter(cells[i][0] for i in dm_cells)),
        "dm_cell_envelope_rank_histogram": dict(
            Counter(cells[i][2].bit_count() for i in dm_cells)
        ),
    }
    if fixed:
        fixed_indices = {i for i, value in enumerate(targets) if value in fixed}
        neighbours = {cell for i in fixed_indices for cell in adjacency[i]}
        result["fixed_target_count"] = len(fixed)
        result["fixed_neighbourhood"] = len(neighbours)
        if distances:
            histogram = [0, 0, 0, 0]
            for _, _, envelope, mandatory, masks in cells:
                distance = 3
                for target in fixed:
                    cost = (target & ~envelope).bit_count()
                    if cost >= distance:
                        continue
                    cost += (mandatory & ~target).bit_count()
                    if cost >= distance:
                        continue
                    cost += sum(not (value & target) for value in masks)
                    distance = min(distance, cost)
                    if not distance:
                        break
                histogram[min(distance, 3)] += 1
            result["fixed_distance_histogram"] = histogram
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path, nargs="+")
    parser.add_argument("--k", type=int, default=15)
    parser.add_argument("--depth", type=int, default=3)
    parser.add_argument("--fixed-targets-file", type=Path)
    parser.add_argument("--distance", action="store_true")
    parser.add_argument("--python", action="store_true")
    parser.add_argument(
        "--binary", type=Path,
        default=ROOT / "scratch/fast_k15_hall_dm",
    )
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    if not args.python and args.binary.is_file():
        command = [str(args.binary), "--k", str(args.k), "--depth", str(args.depth)]
        if args.fixed_targets_file:
            command += ["--fixed-targets-file", str(args.fixed_targets_file)]
        if args.distance:
            command.append("--distance")
        command += list(map(str, args.certificate))
        process = subprocess.run(command, text=True, capture_output=True)
        if process.returncode == 0:
            text = process.stdout
        else:
            print(
                f"optimized core failed ({process.returncode}); using Python fallback",
                file=sys.stderr,
            )
            args.python = True
    if args.python or not args.binary.is_file():
        fixed = fixed_targets_from(args.fixed_targets_file)
        rows = [
            python_audit(path, args.k, args.depth, fixed, args.distance)
            for path in args.certificate
        ]
        text = "".join(json.dumps(row, sort_keys=True) + "\n" for row in rows)
    if args.output:
        args.output.write_text(text)
    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
