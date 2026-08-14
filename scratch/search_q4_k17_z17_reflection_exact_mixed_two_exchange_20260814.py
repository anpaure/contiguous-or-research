#!/usr/bin/env python3
"""Complete pair+self and self+self two-exchange oracle for a finite face."""

from __future__ import annotations

import argparse
import json
import sys
import time
from collections import Counter
from pathlib import Path

import numpy as np

sys.path.insert(0, "scratch")
from search_q4_k17_z17_reflection_fixed_face_kissat_20260814 import read_instance


def overlap(left: np.ndarray, right: np.ndarray) -> int:
    i = j = result = 0
    while i < len(left) and j < len(right):
        if left[i] == right[j]:
            result += 1
            i += 1
            j += 1
        elif left[i] < right[j]:
            i += 1
        else:
            j += 1
    return result


def histogram(loads: np.ndarray) -> dict[str, int]:
    return {str(value): int(count) for value, count in sorted(Counter(loads).items())}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--instance", required=True)
    parser.add_argument("--state", required=True)
    parser.add_argument("--output-state", required=True)
    parser.add_argument("--report", required=True)
    args = parser.parse_args()
    started = time.time()

    _, _, self_raw, pair_raw = read_instance(args.instance)
    pair_rows = np.asarray(pair_raw, dtype=np.int16)
    self_rows = np.asarray([record[1] for record in self_raw], dtype=np.int16)
    self_groups = np.asarray([record[0] for record in self_raw], dtype=np.int16)
    group_options = [np.flatnonzero(self_groups == group) for group in range(35)]
    state = json.loads(Path(args.state).read_text())
    selected_pairs = np.asarray(state["pair_indices"], dtype=np.int32)
    selected_self = np.asarray(sorted(state["self_indices"], key=lambda i: self_raw[i][0]), dtype=np.int32)
    if len(selected_pairs) != 54 or len(selected_self) != 35:
        raise ValueError("expected 54 selected pairs and 35 selected self lifts")
    if [self_raw[index][0] for index in selected_self] != list(range(35)):
        raise ValueError("expected one selected self lift per group")

    loads = np.zeros(680, dtype=np.int16)
    for index in selected_self:
        loads[self_rows[index]] += 1
    for index in selected_pairs:
        loads[pair_rows[index]] += 1
    energy = int(((loads - 1) ** 2).sum())
    if energy != state["energy"]:
        raise ValueError(f"replayed energy {energy} != state energy {state['energy']}")

    selected_pair_rows = pair_rows[selected_pairs]
    selected_self_rows = self_rows[selected_self]
    pair_add = (2 * loads[pair_rows] - 1).sum(axis=1).astype(np.int16)
    self_add = (2 * loads[self_rows] - 1).sum(axis=1).astype(np.int16)
    pair_remove = (3 - 2 * loads[selected_pair_rows]).sum(axis=1).astype(np.int16)
    self_remove = (3 - 2 * loads[selected_self_rows]).sum(axis=1).astype(np.int16)

    pair_vs_pair = np.empty((len(pair_rows), 54), dtype=np.uint8)
    self_vs_pair = np.empty((len(self_rows), 54), dtype=np.uint8)
    for position, rows in enumerate(selected_pair_rows):
        pair_vs_pair[:, position] = np.isin(pair_rows, rows).sum(axis=1)
        self_vs_pair[:, position] = np.isin(self_rows, rows).sum(axis=1)
    pair_vs_self = np.empty((len(pair_rows), 35), dtype=np.uint8)
    self_vs_self = np.empty((len(self_rows), 35), dtype=np.uint8)
    for group, rows in enumerate(selected_self_rows):
        pair_vs_self[:, group] = np.isin(pair_rows, rows).sum(axis=1)
        self_vs_self[:, group] = np.isin(self_rows, rows).sum(axis=1)
    unselected_pairs = np.ones(len(pair_rows), dtype=bool)
    unselected_pairs[selected_pairs] = False

    best = None
    mixed_faces = []
    self_faces = []
    mixed_tests = self_tests = 0
    for pair_position in range(54):
        for group in range(35):
            constant = int(
                pair_remove[pair_position]
                + self_remove[group]
                + 2 * overlap(selected_pair_rows[pair_position], selected_self_rows[group])
            )
            pair_directed = (
                pair_add
                - 2 * pair_vs_pair[:, pair_position]
                - 2 * pair_vs_self[:, group]
            )
            self_directed = (
                self_add
                - 2 * self_vs_pair[:, pair_position]
                - 2 * self_vs_self[:, group]
            )
            alternatives = group_options[group]
            alternatives = alternatives[alternatives != selected_self[group]]
            pair_minimum = int(pair_directed[unselected_pairs].min())
            self_minimum = int(self_directed[alternatives].min())
            lower_bound = constant + pair_minimum + self_minimum
            if lower_bound >= 0:
                continue
            pair_candidates = np.flatnonzero(
                unselected_pairs & (pair_directed < -constant - self_minimum)
            )
            self_candidates = alternatives[
                self_directed[alternatives] < -constant - pair_minimum
            ]
            face_best = None
            for incoming_pair in pair_candidates:
                for incoming_self in self_candidates:
                    mixed_tests += 1
                    delta = int(
                        constant
                        + pair_directed[incoming_pair]
                        + self_directed[incoming_self]
                        + 2 * overlap(pair_rows[incoming_pair], self_rows[incoming_self])
                    )
                    candidate = (
                        delta,
                        "pair+self",
                        int(selected_pairs[pair_position]),
                        int(selected_self[group]),
                        int(incoming_pair),
                        int(incoming_self),
                    )
                    if face_best is None or candidate < face_best:
                        face_best = candidate
                    if best is None or candidate < best:
                        best = candidate
            mixed_faces.append({
                "constant": constant,
                "incoming_pair_candidates": int(len(pair_candidates)),
                "incoming_self_candidates": int(len(self_candidates)),
                "lower_bound": lower_bound,
                "outgoing_pair": int(selected_pairs[pair_position]),
                "outgoing_self": int(selected_self[group]),
                "pair_minimum": pair_minimum,
                "self_minimum": self_minimum,
                "tested_best_delta": None if face_best is None else face_best[0],
            })

    for left_group in range(35):
        for right_group in range(left_group + 1, 35):
            constant = int(
                self_remove[left_group]
                + self_remove[right_group]
                + 2 * overlap(selected_self_rows[left_group], selected_self_rows[right_group])
            )
            directed = (
                self_add
                - 2 * self_vs_self[:, left_group]
                - 2 * self_vs_self[:, right_group]
            )
            left_options = group_options[left_group]
            left_options = left_options[left_options != selected_self[left_group]]
            right_options = group_options[right_group]
            right_options = right_options[right_options != selected_self[right_group]]
            left_minimum = int(directed[left_options].min())
            right_minimum = int(directed[right_options].min())
            lower_bound = constant + left_minimum + right_minimum
            if lower_bound >= 0:
                continue
            left_candidates = left_options[
                directed[left_options] < -constant - right_minimum
            ]
            right_candidates = right_options[
                directed[right_options] < -constant - left_minimum
            ]
            face_best = None
            for incoming_left in left_candidates:
                for incoming_right in right_candidates:
                    self_tests += 1
                    delta = int(
                        constant
                        + directed[incoming_left]
                        + directed[incoming_right]
                        + 2 * overlap(self_rows[incoming_left], self_rows[incoming_right])
                    )
                    candidate = (
                        delta,
                        "self+self",
                        int(selected_self[left_group]),
                        int(selected_self[right_group]),
                        int(incoming_left),
                        int(incoming_right),
                    )
                    if face_best is None or candidate < face_best:
                        face_best = candidate
                    if best is None or candidate < best:
                        best = candidate
            self_faces.append({
                "constant": constant,
                "incoming_left_candidates": int(len(left_candidates)),
                "incoming_right_candidates": int(len(right_candidates)),
                "left_group": left_group,
                "left_minimum": left_minimum,
                "lower_bound": lower_bound,
                "right_group": right_group,
                "right_minimum": right_minimum,
                "tested_best_delta": None if face_best is None else face_best[0],
            })

    solution = None
    output_histogram = None
    if best is not None and best[0] < 0:
        delta, kind, old_left, old_right, new_left, new_right = best
        solution = dict(state)
        replay = loads.copy()
        if kind == "pair+self":
            pairs = list(map(int, selected_pairs))
            pairs[pairs.index(old_left)] = new_left
            pairs.sort()
            selfs = list(map(int, selected_self))
            selfs[selfs.index(old_right)] = new_right
            selfs.sort()
            replay[pair_rows[old_left]] -= 1
            replay[self_rows[old_right]] -= 1
            replay[pair_rows[new_left]] += 1
            replay[self_rows[new_right]] += 1
        else:
            pairs = list(map(int, selected_pairs))
            selfs = list(map(int, selected_self))
            selfs[selfs.index(old_left)] = new_left
            selfs[selfs.index(old_right)] = new_right
            selfs.sort()
            replay[self_rows[old_left]] -= 1
            replay[self_rows[old_right]] -= 1
            replay[self_rows[new_left]] += 1
            replay[self_rows[new_right]] += 1
        replay_energy = int(((replay - 1) ** 2).sum())
        if replay_energy != energy + delta:
            raise ValueError(f"two-exchange replay {replay_energy} != {energy + delta}")
        solution.update({
            "energy": replay_energy,
            "pair_indices": pairs,
            "self_indices": selfs,
            "status": "EXACT_MIXED_TWO_EXCHANGE",
        })
        Path(args.output_state).write_text(
            json.dumps(solution, indent=2, sort_keys=True) + "\n", encoding="ascii"
        )
        output_histogram = histogram(replay)

    report = {
        "status": "PASS" if solution is not None else "NO_NEGATIVE_MIXED_TWO_EXCHANGE",
        "scope": "complete pair+self and self+self two-exchange oracle in the finite face",
        "instance": args.instance,
        "source_state": args.state,
        "source_energy": energy,
        "source_histogram": histogram(loads),
        "pair_options": len(pair_rows),
        "self_options": len(self_rows),
        "mixed_outgoing_faces": 54 * 35,
        "self_outgoing_faces": 35 * 34 // 2,
        "mixed_surviving_faces": len(mixed_faces),
        "self_surviving_faces": len(self_faces),
        "mixed_exact_tests": mixed_tests,
        "self_exact_tests": self_tests,
        "best_exchange": None if best is None else {
            "delta": best[0],
            "kind": best[1],
            "remove": [best[2], best[3]],
            "add": [best[4], best[5]],
        },
        "output_state": args.output_state if solution is not None else None,
        "output_histogram": output_histogram,
        "mixed_face_audit": mixed_faces,
        "self_face_audit": self_faces,
        "elapsed_seconds": time.time() - started,
    }
    Path(args.report).write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="ascii"
    )
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
