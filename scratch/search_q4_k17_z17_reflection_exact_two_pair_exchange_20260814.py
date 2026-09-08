#!/usr/bin/env python3
"""Complete negative two-reflected-pair exchange oracle for a finite pool."""

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
    """Intersection size of two tiny sorted row arrays."""
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
    state = json.loads(Path(args.state).read_text())
    selected_pairs = np.asarray(state["pair_indices"], dtype=np.int32)
    selected_self = np.asarray(state["self_indices"], dtype=np.int32)
    if len(selected_pairs) != 54 or len(set(map(int, selected_pairs))) != 54:
        raise ValueError("expected 54 distinct selected pair configurations")

    loads = np.zeros(680, dtype=np.int16)
    for index in selected_self:
        loads[self_rows[index]] += 1
    for index in selected_pairs:
        loads[pair_rows[index]] += 1
    energy = int(((loads - 1) ** 2).sum())
    if energy != state["energy"]:
        raise ValueError(f"replayed energy {energy} != state energy {state['energy']}")

    selected_rows = pair_rows[selected_pairs]
    add_score = (2 * loads[pair_rows] - 1).sum(axis=1).astype(np.int16)
    remove_score = (3 - 2 * loads[selected_rows]).sum(axis=1).astype(np.int16)
    intersections = np.empty((len(pair_rows), 54), dtype=np.uint8)
    for position, rows in enumerate(selected_rows):
        intersections[:, position] = np.isin(pair_rows, rows).sum(axis=1)
    unselected = np.ones(len(pair_rows), dtype=bool)
    unselected[selected_pairs] = False

    surviving_faces = []
    best = None
    pair_tests = 0
    survivor_sum = 0
    for left in range(54):
        for right in range(left + 1, 54):
            constant = int(
                remove_score[left]
                + remove_score[right]
                + 2 * overlap(selected_rows[left], selected_rows[right])
            )
            directed = (
                add_score
                - 2 * intersections[:, left]
                - 2 * intersections[:, right]
            )
            minimum = int(directed[unselected].min())
            lower_bound = constant + 2 * minimum
            if lower_bound >= 0:
                continue
            threshold = -constant - minimum
            candidates = np.flatnonzero(unselected & (directed < threshold))
            survivor_sum += len(candidates)
            face_best = None
            for first_position, incoming_left in enumerate(candidates):
                for incoming_right in candidates[first_position + 1:]:
                    pair_tests += 1
                    delta = int(
                        constant
                        + directed[incoming_left]
                        + directed[incoming_right]
                        + 2 * overlap(pair_rows[incoming_left], pair_rows[incoming_right])
                    )
                    candidate = (
                        delta,
                        int(selected_pairs[left]),
                        int(selected_pairs[right]),
                        int(incoming_left),
                        int(incoming_right),
                    )
                    if face_best is None or candidate < face_best:
                        face_best = candidate
                    if best is None or candidate < best:
                        best = candidate
            surviving_faces.append({
                "candidate_count": int(len(candidates)),
                "constant": constant,
                "directed_minimum": minimum,
                "lower_bound": lower_bound,
                "outgoing_left": int(selected_pairs[left]),
                "outgoing_right": int(selected_pairs[right]),
                "tested_best_delta": None if face_best is None else face_best[0],
                "threshold": threshold,
            })

    solution = None
    final_histogram = None
    if best is not None and best[0] < 0:
        delta, old_left, old_right, new_left, new_right = best
        new_pairs = list(map(int, selected_pairs))
        new_pairs.remove(old_left)
        new_pairs.remove(old_right)
        new_pairs.extend((new_left, new_right))
        new_pairs.sort()
        replay = loads.copy()
        replay[pair_rows[old_left]] -= 1
        replay[pair_rows[old_right]] -= 1
        replay[pair_rows[new_left]] += 1
        replay[pair_rows[new_right]] += 1
        replay_energy = int(((replay - 1) ** 2).sum())
        if replay_energy != energy + delta:
            raise ValueError(f"two-exchange replay {replay_energy} != {energy + delta}")
        solution = dict(state)
        solution["energy"] = replay_energy
        solution["pair_indices"] = new_pairs
        solution["status"] = "EXACT_TWO_PAIR_EXCHANGE"
        Path(args.output_state).write_text(
            json.dumps(solution, indent=2, sort_keys=True) + "\n", encoding="ascii"
        )
        final_histogram = histogram(replay)

    report = {
        "status": "PASS" if solution is not None else "NO_NEGATIVE_TWO_PAIR_EXCHANGE",
        "scope": "complete over two distinct unselected reflected-pair options in the finite instance",
        "instance": args.instance,
        "source_state": args.state,
        "source_energy": energy,
        "source_histogram": histogram(loads),
        "pair_options": len(pair_rows),
        "outgoing_faces": 54 * 53 // 2,
        "surviving_faces": len(surviving_faces),
        "threshold_survivor_sum": survivor_sum,
        "exact_incoming_pair_tests": pair_tests,
        "best_exchange": None if best is None else {
            "delta": best[0],
            "remove": [best[1], best[2]],
            "add": [best[3], best[4]],
        },
        "output_state": args.output_state if solution is not None else None,
        "output_histogram": final_histogram,
        "face_audit": surviving_faces,
        "elapsed_seconds": time.time() - started,
    }
    Path(args.report).write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="ascii"
    )
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
