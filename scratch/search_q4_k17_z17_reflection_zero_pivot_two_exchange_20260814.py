#!/usr/bin/env python3
"""Exhaust every second 1-exchange after catalogue zero-delta pair pivots."""

from __future__ import annotations

import argparse
import csv
import json
import sys
import time
from collections import Counter
from pathlib import Path

import numpy as np

sys.path.insert(0, "scratch")
from search_q4_k17_z17_reflection_fixed_face_kissat_20260814 import read_instance


def histogram(loads: np.ndarray) -> dict[str, int]:
    return {str(value): int(count) for value, count in sorted(Counter(loads).items())}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--instance", required=True)
    parser.add_argument("--state", required=True)
    parser.add_argument("--catalog", required=True)
    parser.add_argument("--output-state", required=True)
    parser.add_argument("--report", required=True)
    args = parser.parse_args()

    _, _, self_raw, pair_raw = read_instance(args.instance)
    pair_rows = np.asarray(pair_raw, dtype=np.int16)
    self_rows = np.asarray([record[1] for record in self_raw], dtype=np.int16)
    self_groups = np.asarray([record[0] for record in self_raw], dtype=np.int16)
    group_options = [np.flatnonzero(self_groups == group) for group in range(35)]
    pair_index = {tuple(map(int, rows)): index for index, rows in enumerate(pair_raw)}
    state = json.loads(Path(args.state).read_text())
    base_pairs = list(map(int, state["pair_indices"]))
    base_self = list(map(int, state["self_indices"]))
    loads = np.zeros(680, dtype=np.int16)
    for index in base_self:
        loads[self_rows[index]] += 1
    for index in base_pairs:
        loads[pair_rows[index]] += 1
    energy = int(((loads - 1) ** 2).sum())
    if energy != state["energy"]:
        raise ValueError(f"replayed energy {energy} != state energy {state['energy']}")

    pivots = []
    seen = set()
    with open(args.catalog, newline="", encoding="utf-8") as handle:
        for record in csv.DictReader(handle, delimiter="\t"):
            if int(record["delta"]) != 0:
                continue
            rows = tuple(map(int, record["rows"].split(",")))
            old = int(record["best_outgoing_pair_index"])
            new = pair_index.get(rows)
            key = old, new
            if new is None or key in seen:
                continue
            seen.add(key)
            pivots.append((old, new, rows))

    selected_by_group = {self_raw[index][0]: index for index in base_self}
    audited = []
    best_chain = None
    started = time.time()
    for old, new, rows in pivots:
        if old not in base_pairs or new in base_pairs:
            continue
        pivot_pairs = base_pairs.copy()
        pivot_pairs[pivot_pairs.index(old)] = new
        pivot_pairs.sort()
        pivot_loads = loads.copy()
        pivot_loads[pair_rows[old]] -= 1
        pivot_loads[pair_rows[new]] += 1
        pivot_energy = int(((pivot_loads - 1) ** 2).sum())
        if pivot_energy != energy:
            raise ValueError(f"catalogue zero pivot {old}->{new} replays at {pivot_energy}")

        selected_pairs = np.zeros(len(pair_rows), dtype=bool)
        selected_pairs[pivot_pairs] = True
        best_pair = None
        for position, second_old in enumerate(pivot_pairs):
            reduced = pivot_loads.copy()
            reduced[pair_rows[second_old]] -= 1
            removal_delta = int(((reduced - 1) ** 2).sum() - pivot_energy)
            deltas = removal_delta + (2 * reduced[pair_rows] - 1).sum(axis=1)
            deltas[selected_pairs] = 100_000
            second_new = int(deltas.argmin())
            candidate = (int(deltas[second_new]), second_old, second_new, position)
            if best_pair is None or candidate < best_pair:
                best_pair = candidate

        best_self = None
        for group in range(35):
            second_old = selected_by_group[group]
            reduced = pivot_loads.copy()
            reduced[self_rows[second_old]] -= 1
            removal_delta = int(((reduced - 1) ** 2).sum() - pivot_energy)
            options = group_options[group]
            deltas = removal_delta + (2 * reduced[self_rows[options]] - 1).sum(axis=1)
            deltas[options == second_old] = 100_000
            offset = int(deltas.argmin())
            second_new = int(options[offset])
            candidate = (int(deltas[offset]), second_old, second_new, group)
            if best_self is None or candidate < best_self:
                best_self = candidate

        if best_pair[0] <= best_self[0]:
            kind, second = "pair", best_pair
        else:
            kind, second = "self", best_self
        result = {
            "pivot_add": new,
            "pivot_remove": old,
            "pivot_rows": list(rows),
            "second_add": second[2],
            "second_delta": second[0],
            "second_kind": kind,
            "second_remove": second[1],
        }
        audited.append(result)
        key = (second[0], old, new, kind, second[1], second[2])
        if best_chain is None or key < best_chain[0]:
            best_chain = key, result, pivot_pairs

    solution = None
    if best_chain is not None and best_chain[1]["second_delta"] < 0:
        result = best_chain[1]
        solution = dict(state)
        solution["pair_indices"] = best_chain[2]
        if result["second_kind"] == "pair":
            values = solution["pair_indices"]
            values[values.index(result["second_remove"])] = result["second_add"]
            values.sort()
        else:
            values = solution["self_indices"]
            values[values.index(result["second_remove"])] = result["second_add"]
            values.sort()
        solution["energy"] = energy + result["second_delta"]
        solution["status"] = "ZERO_PIVOT_TWO_EXCHANGE"
        Path(args.output_state).write_text(
            json.dumps(solution, indent=2, sort_keys=True) + "\n", encoding="ascii"
        )

    report = {
        "status": "PASS" if solution is not None else "NO_NEGATIVE_TWO_STEP_CHAIN",
        "base_energy": energy,
        "base_histogram": histogram(loads),
        "catalogue_zero_pivots": len(pivots),
        "legal_zero_pivots_audited": len(audited),
        "best_chain": None if best_chain is None else best_chain[1],
        "output_state": args.output_state if solution is not None else None,
        "pair_options": len(pair_rows),
        "self_options": len(self_rows),
        "second_pair_comparisons": len(audited) * len(pair_rows) * len(base_pairs),
        "elapsed_seconds": time.time() - started,
        "pivots": audited,
    }
    Path(args.report).write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="ascii"
    )
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
