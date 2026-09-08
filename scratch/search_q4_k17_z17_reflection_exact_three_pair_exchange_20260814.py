#!/usr/bin/env python3
"""Complete three-reflected-pair exchange oracle for a finite pool."""

from __future__ import annotations

import argparse
import itertools
import json
import sys
import time
from collections import Counter
from pathlib import Path

import numpy as np

sys.path.insert(0, "scratch")
from search_q4_k17_z17_reflection_fixed_face_kissat_20260814 import read_instance


def row_mask(rows) -> int:
    mask = 0
    for row in rows:
        mask |= 1 << int(row)
    return mask


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
    pair_masks = [row_mask(rows) for rows in pair_raw]
    self_rows = np.asarray([record[1] for record in self_raw], dtype=np.int16)
    state = json.loads(Path(args.state).read_text())
    selected_pairs = np.asarray(state["pair_indices"], dtype=np.int32)
    selected_self = np.asarray(state["self_indices"], dtype=np.int32)
    if len(selected_pairs) != 54 or len(set(map(int, selected_pairs))) != 54:
        raise ValueError("expected 54 distinct selected reflected pairs")

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

    best = None
    surviving_faces = []
    retained_candidate_sum = 0
    retained_pair_tests = 0
    exact_triple_tests = 0
    face_number = 0
    for left, middle, right in itertools.combinations(range(54), 3):
        face_number += 1
        constant = int(
            remove_score[left]
            + remove_score[middle]
            + remove_score[right]
            + 2 * (
                intersections[selected_pairs[left], middle]
                + intersections[selected_pairs[left], right]
                + intersections[selected_pairs[middle], right]
            )
        )
        directed = (
            add_score
            - 2 * intersections[:, left]
            - 2 * intersections[:, middle]
            - 2 * intersections[:, right]
        )
        directed[selected_pairs] = 30_000
        minima_indices = np.argpartition(directed, 2)[:3]
        minima_indices = sorted(
            map(int, minima_indices), key=lambda index: (int(directed[index]), index)
        )
        minima = [int(directed[index]) for index in minima_indices]
        lower_bound = constant + sum(minima)
        if lower_bound >= 0:
            continue

        default_mu2 = minima[0] + minima[1]
        keep = unselected & (constant + directed + default_mu2 < 0)
        first, second, third = minima_indices
        keep[first] = constant + int(directed[first]) + minima[1] + minima[2] < 0
        keep[second] = constant + int(directed[second]) + minima[0] + minima[2] < 0
        candidates = np.flatnonzero(keep)
        retained_candidate_sum += len(candidates)
        face_best = None
        face_pair_tests = 0
        face_triple_tests = 0
        for first_position, incoming_left in enumerate(candidates):
            left_mask = pair_masks[incoming_left]
            for second_position in range(first_position + 1, len(candidates)):
                incoming_middle = int(candidates[second_position])
                face_pair_tests += 1
                retained_pair_tests += 1
                pair_score = int(
                    directed[incoming_left]
                    + directed[incoming_middle]
                    + 2 * (left_mask & pair_masks[incoming_middle]).bit_count()
                )
                exclusion_minimum = None
                for minimum_index in minima_indices:
                    if minimum_index not in (incoming_left, incoming_middle):
                        exclusion_minimum = int(directed[minimum_index])
                        break
                assert exclusion_minimum is not None
                if constant + pair_score + exclusion_minimum >= 0:
                    continue
                threshold = -constant - pair_score
                for incoming_right in candidates[second_position + 1:]:
                    incoming_right = int(incoming_right)
                    if directed[incoming_right] >= threshold:
                        continue
                    face_triple_tests += 1
                    exact_triple_tests += 1
                    delta = int(
                        constant
                        + pair_score
                        + directed[incoming_right]
                        + 2 * (
                            (left_mask & pair_masks[incoming_right]).bit_count()
                            + (pair_masks[incoming_middle] & pair_masks[incoming_right]).bit_count()
                        )
                    )
                    candidate = (
                        delta,
                        int(selected_pairs[left]),
                        int(selected_pairs[middle]),
                        int(selected_pairs[right]),
                        int(incoming_left),
                        incoming_middle,
                        incoming_right,
                    )
                    if face_best is None or candidate < face_best:
                        face_best = candidate
                    if best is None or candidate < best:
                        best = candidate
        surviving_faces.append({
            "candidate_count": int(len(candidates)),
            "constant": constant,
            "exact_triple_tests": face_triple_tests,
            "lower_bound": lower_bound,
            "minima": minima,
            "outgoing": [
                int(selected_pairs[left]),
                int(selected_pairs[middle]),
                int(selected_pairs[right]),
            ],
            "retained_pair_tests": face_pair_tests,
            "tested_best_delta": None if face_best is None else face_best[0],
        })
        if face_number % 2_000 == 0:
            print(json.dumps({
                "elapsed_seconds": time.time() - started,
                "exact_triple_tests": exact_triple_tests,
                "faces_scanned": face_number,
                "surviving_faces": len(surviving_faces),
            }, sort_keys=True), file=sys.stderr, flush=True)

    solution = None
    output_histogram = None
    if best is not None and best[0] < 0:
        delta = best[0]
        removed = list(best[1:4])
        added = list(best[4:7])
        new_pairs = list(map(int, selected_pairs))
        replay = loads.copy()
        for index in removed:
            new_pairs.remove(index)
            replay[pair_rows[index]] -= 1
        for index in added:
            new_pairs.append(index)
            replay[pair_rows[index]] += 1
        new_pairs.sort()
        replay_energy = int(((replay - 1) ** 2).sum())
        if replay_energy != energy + delta:
            raise ValueError(f"three-exchange replay {replay_energy} != {energy + delta}")
        solution = dict(state)
        solution["energy"] = replay_energy
        solution["pair_indices"] = new_pairs
        solution["status"] = "EXACT_THREE_PAIR_EXCHANGE"
        Path(args.output_state).write_text(
            json.dumps(solution, indent=2, sort_keys=True) + "\n", encoding="ascii"
        )
        output_histogram = histogram(replay)

    report = {
        "status": "PASS" if solution is not None else "NO_NEGATIVE_THREE_PAIR_EXCHANGE",
        "scope": "complete over three distinct unselected reflected-pair options in the finite instance",
        "instance": args.instance,
        "source_state": args.state,
        "source_energy": energy,
        "source_histogram": histogram(loads),
        "pair_options": len(pair_rows),
        "outgoing_faces": 54 * 53 * 52 // 6,
        "surviving_faces": len(surviving_faces),
        "retained_candidate_sum": retained_candidate_sum,
        "retained_pair_tests": retained_pair_tests,
        "exact_triple_tests": exact_triple_tests,
        "best_exchange": None if best is None else {
            "delta": best[0],
            "remove": list(best[1:4]),
            "add": list(best[4:7]),
        },
        "output_state": args.output_state if solution is not None else None,
        "output_histogram": output_histogram,
        "face_audit": surviving_faces,
        "elapsed_seconds": time.time() - started,
    }
    Path(args.report).write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="ascii"
    )
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
