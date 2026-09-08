#!/usr/bin/env python3
"""Exact steepest 1-exchange descent for a fixed reflection face (H100)."""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, "scratch")
from search_q4_k17_z17_reflection_fixed_face_kissat_20260814 import (
    read_instance,
)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--instance", required=True)
    parser.add_argument("--state", required=True)
    parser.add_argument("--output-state", required=True)
    parser.add_argument("--report", required=True)
    parser.add_argument("--max-iterations", type=int, default=1000)
    args = parser.parse_args()

    _, _, self_raw, pair_raw = read_instance(args.instance)
    pair_rows = np.asarray(pair_raw, dtype=np.int16)
    self_rows = np.asarray([record[1] for record in self_raw], dtype=np.int16)
    self_groups = np.asarray([record[0] for record in self_raw], dtype=np.int16)
    group_options = [np.flatnonzero(self_groups == group) for group in range(35)]
    state = json.load(open(args.state, encoding="utf-8"))
    loads = np.zeros(680, dtype=np.int16)
    for index in state["self_indices"]:
        loads[self_rows[index]] += 1
    for index in state["pair_indices"]:
        loads[pair_rows[index]] += 1
    energy = int(((loads - 1) ** 2).sum())
    assert energy == state["energy"]
    trajectory = []
    started = time.time()

    for iteration in range(args.max_iterations):
        selected_pairs = np.zeros(len(pair_rows), dtype=bool)
        selected_pairs[state["pair_indices"]] = True
        best_pair = None
        for position, old in enumerate(state["pair_indices"]):
            reduced = loads.copy()
            reduced[pair_rows[old]] -= 1
            removal_delta = int(((reduced - 1) ** 2).sum() - energy)
            deltas = removal_delta + (2 * reduced[pair_rows] - 1).sum(axis=1)
            deltas[selected_pairs] = 100_000
            new = int(deltas.argmin())
            candidate = (int(deltas[new]), old, new, position)
            if best_pair is None or candidate < best_pair:
                best_pair = candidate

        selected_by_group = {
            self_raw[index][0]: index for index in state["self_indices"]
        }
        best_self = None
        for group in range(35):
            old = selected_by_group[group]
            reduced = loads.copy()
            reduced[self_rows[old]] -= 1
            removal_delta = int(((reduced - 1) ** 2).sum() - energy)
            options = group_options[group]
            deltas = removal_delta + (2 * reduced[self_rows[options]] - 1).sum(axis=1)
            deltas[options == old] = 100_000
            offset = int(deltas.argmin())
            new = int(options[offset])
            candidate = (int(deltas[offset]), old, new, group)
            if best_self is None or candidate < best_self:
                best_self = candidate

        if best_pair[0] <= best_self[0]:
            kind, best = "pair", best_pair
        else:
            kind, best = "self", best_self
        if best[0] >= 0:
            final_pair = {
                "delta": best_pair[0], "old": best_pair[1], "new": best_pair[2]
            }
            final_self = {
                "delta": best_self[0], "old": best_self[1], "new": best_self[2]
            }
            break

        delta, old, new, position = best
        before = energy
        if kind == "pair":
            loads[pair_rows[old]] -= 1
            loads[pair_rows[new]] += 1
            state["pair_indices"][position] = new
            state["pair_indices"].sort()
        else:
            loads[self_rows[old]] -= 1
            loads[self_rows[new]] += 1
            state["self_indices"].remove(old)
            state["self_indices"].append(new)
            state["self_indices"].sort()
        energy = int(((loads - 1) ** 2).sum())
        assert energy == before + delta
        trajectory.append({
            "iteration": iteration,
            "kind": kind,
            "removed": old,
            "added": new,
            "delta": delta,
            "energy": energy,
            "histogram": {
                str(value): int(np.count_nonzero(loads == value))
                for value in np.unique(loads)
            },
        })
    else:
        raise AssertionError("iteration cap reached")

    state["energy"] = energy
    state["status"] = "BEST"
    Path(args.output_state).write_text(
        json.dumps(state, indent=2, sort_keys=True) + "\n", encoding="ascii"
    )
    report = {
        "status": "PASS",
        "instance": args.instance,
        "source_state": args.state,
        "output_state": args.output_state,
        "source_energy": json.load(open(args.state, encoding="utf-8"))["energy"],
        "final_energy": energy,
        "final_histogram": {
            str(value): int(np.count_nonzero(loads == value))
            for value in np.unique(loads)
        },
        "iterations": len(trajectory),
        "trajectory": trajectory,
        "best_remaining_pair_swap": final_pair,
        "best_remaining_self_swap": final_self,
        "pair_options": len(pair_rows),
        "self_options": len(self_rows),
        "pair_comparisons_per_iteration": len(pair_rows) * 54,
        "elapsed_seconds": time.time() - started,
    }
    Path(args.report).write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="ascii"
    )
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
