#!/usr/bin/env python3
"""Complete four-reflected-pair exchange oracle for a finite pool."""

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


def exclusion_sum(directed: np.ndarray, minima_indices: list[int], excluded, count: int) -> int:
    result = 0
    found = 0
    for index in minima_indices:
        if index in excluded:
            continue
        result += int(directed[index])
        found += 1
        if found == count:
            return result
    raise AssertionError("insufficient distinct exclusion minima")


def histogram(loads: np.ndarray) -> dict[str, int]:
    return {str(value): int(count) for value, count in sorted(Counter(loads).items())}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--instance", required=True)
    parser.add_argument("--state", required=True)
    parser.add_argument("--output-state", required=True)
    parser.add_argument("--report", required=True)
    parser.add_argument("--progress-every", type=int, default=10_000)
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
    retained_triple_tests = 0
    exact_quadruple_tests = 0
    face_number = 0
    for first, second, third, fourth in itertools.combinations(range(54), 4):
        face_number += 1
        if args.progress_every and face_number % args.progress_every == 0:
            print(json.dumps({
                "elapsed_seconds": time.time() - started,
                "exact_quadruple_tests": exact_quadruple_tests,
                "faces_scanned": face_number,
                "surviving_faces": len(surviving_faces),
            }, sort_keys=True), file=sys.stderr, flush=True)
        outgoing_positions = (first, second, third, fourth)
        constant = int(sum(remove_score[position] for position in outgoing_positions))
        for left_position, right_position in itertools.combinations(outgoing_positions, 2):
            constant += 2 * int(intersections[selected_pairs[left_position], right_position])
        directed = add_score.copy()
        for position in outgoing_positions:
            directed -= 2 * intersections[:, position]
        directed[selected_pairs] = 30_000
        minima_indices = np.argpartition(directed, 3)[:4]
        minima_indices = sorted(
            map(int, minima_indices), key=lambda index: (int(directed[index]), index)
        )
        minima = [int(directed[index]) for index in minima_indices]
        lower_bound = constant + sum(minima)
        if lower_bound >= 0:
            continue

        default_mu3 = sum(minima[:3])
        keep = unselected & (constant + directed + default_mu3 < 0)
        for minimum_index in minima_indices[:3]:
            keep[minimum_index] = (
                constant
                + int(directed[minimum_index])
                + exclusion_sum(directed, minima_indices, {minimum_index}, 3)
                < 0
            )
        candidates = np.flatnonzero(keep)
        retained_candidate_sum += len(candidates)
        face_best = None
        face_pair_tests = 0
        face_triple_tests = 0
        face_quadruple_tests = 0
        for first_position, incoming_first in enumerate(candidates):
            incoming_first = int(incoming_first)
            first_mask = pair_masks[incoming_first]
            for second_position in range(first_position + 1, len(candidates)):
                incoming_second = int(candidates[second_position])
                face_pair_tests += 1
                retained_pair_tests += 1
                pair_score = int(
                    directed[incoming_first]
                    + directed[incoming_second]
                    + 2 * (first_mask & pair_masks[incoming_second]).bit_count()
                )
                pair_excluded = {incoming_first, incoming_second}
                if constant + pair_score + exclusion_sum(
                    directed, minima_indices, pair_excluded, 2
                ) >= 0:
                    continue
                second_mask = pair_masks[incoming_second]
                for third_position in range(second_position + 1, len(candidates)):
                    incoming_third = int(candidates[third_position])
                    third_score = int(
                        pair_score
                        + directed[incoming_third]
                        + 2 * (
                            (first_mask & pair_masks[incoming_third]).bit_count()
                            + (second_mask & pair_masks[incoming_third]).bit_count()
                        )
                    )
                    face_triple_tests += 1
                    retained_triple_tests += 1
                    triple_excluded = {
                        incoming_first, incoming_second, incoming_third
                    }
                    if constant + third_score + exclusion_sum(
                        directed, minima_indices, triple_excluded, 1
                    ) >= 0:
                        continue
                    threshold = -constant - third_score
                    third_mask = pair_masks[incoming_third]
                    for incoming_fourth in candidates[third_position + 1:]:
                        incoming_fourth = int(incoming_fourth)
                        if directed[incoming_fourth] >= threshold:
                            continue
                        face_quadruple_tests += 1
                        exact_quadruple_tests += 1
                        fourth_mask = pair_masks[incoming_fourth]
                        delta = int(
                            constant
                            + third_score
                            + directed[incoming_fourth]
                            + 2 * (
                                (first_mask & fourth_mask).bit_count()
                                + (second_mask & fourth_mask).bit_count()
                                + (third_mask & fourth_mask).bit_count()
                            )
                        )
                        candidate = (
                            delta,
                            *(int(selected_pairs[position]) for position in outgoing_positions),
                            incoming_first,
                            incoming_second,
                            incoming_third,
                            incoming_fourth,
                        )
                        if face_best is None or candidate < face_best:
                            face_best = candidate
                        if best is None or candidate < best:
                            best = candidate
        surviving_faces.append({
            "candidate_count": int(len(candidates)),
            "constant": constant,
            "exact_quadruple_tests": face_quadruple_tests,
            "lower_bound": lower_bound,
            "minima": minima,
            "outgoing": [int(selected_pairs[position]) for position in outgoing_positions],
            "retained_pair_tests": face_pair_tests,
            "retained_triple_tests": face_triple_tests,
            "tested_best_delta": None if face_best is None else face_best[0],
        })

    solution = None
    output_histogram = None
    if best is not None and best[0] < 0:
        delta = best[0]
        removed = list(best[1:5])
        added = list(best[5:9])
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
            raise ValueError(f"four-exchange replay {replay_energy} != {energy + delta}")
        solution = dict(state)
        solution["energy"] = replay_energy
        solution["pair_indices"] = new_pairs
        solution["status"] = "EXACT_FOUR_PAIR_EXCHANGE"
        Path(args.output_state).write_text(
            json.dumps(solution, indent=2, sort_keys=True) + "\n", encoding="ascii"
        )
        output_histogram = histogram(replay)

    report = {
        "status": "PASS" if solution is not None else "NO_NEGATIVE_FOUR_PAIR_EXCHANGE",
        "scope": "complete over four distinct unselected reflected-pair options in the finite instance",
        "instance": args.instance,
        "source_state": args.state,
        "source_energy": energy,
        "source_histogram": histogram(loads),
        "pair_options": len(pair_rows),
        "outgoing_faces": 54 * 53 * 52 * 51 // 24,
        "surviving_faces": len(surviving_faces),
        "retained_candidate_sum": retained_candidate_sum,
        "retained_pair_tests": retained_pair_tests,
        "retained_triple_tests": retained_triple_tests,
        "exact_quadruple_tests": exact_quadruple_tests,
        "best_exchange": None if best is None else {
            "delta": best[0],
            "remove": list(best[1:5]),
            "add": list(best[5:9]),
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
