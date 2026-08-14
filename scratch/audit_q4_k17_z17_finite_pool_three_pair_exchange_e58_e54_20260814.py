#!/usr/bin/env python3
"""Independently replay the finite-pool E58/E54 three-pair reports (H100)."""

from __future__ import annotations

import argparse
import itertools
import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, "scratch")
from search_q4_k17_z17_reflection_fixed_face_kissat_20260814 import read_instance


def row_mask(rows):
    mask = 0
    for row in rows:
        mask |= 1 << int(row)
    return mask


def replay(report_path):
    report = json.loads(Path(report_path).read_text())
    _, _, self_raw, pair_raw = read_instance(report["instance"])
    pair_rows = np.asarray(pair_raw, dtype=np.int16)
    self_rows = np.asarray([record[1] for record in self_raw], dtype=np.int16)
    pair_masks = [row_mask(rows) for rows in pair_raw]
    state = json.loads(Path(report["source_state"]).read_text())
    selected = np.asarray(state["pair_indices"], dtype=np.int32)
    assert len(selected) == len(set(map(int, selected))) == 54

    loads = np.zeros(680, dtype=np.int16)
    for index in state["self_indices"]:
        loads[self_rows[index]] += 1
    for index in selected:
        loads[pair_rows[index]] += 1
    energy = int(((loads - 1) ** 2).sum())
    assert energy == state["energy"] == report["source_energy"]

    selected_rows = pair_rows[selected]
    add_score = (2 * loads[pair_rows] - 1).sum(axis=1).astype(np.int32)
    remove_score = (3 - 2 * loads[selected_rows]).sum(axis=1).astype(np.int32)
    selected_overlap = np.empty((len(pair_rows), 54), dtype=np.uint8)
    for position, rows in enumerate(selected_rows):
        selected_overlap[:, position] = np.isin(pair_rows, rows).sum(axis=1)
    unselected = np.ones(len(pair_rows), dtype=bool)
    unselected[selected] = False
    unselected_indices = np.flatnonzero(unselected)

    audited_faces = {
        tuple(face["outgoing"]): face for face in report["face_audit"]
    }
    survivors = candidate_sum = pair_tests = triple_tests = 0
    best = None

    for positions in itertools.combinations(range(54), 3):
        left, middle, right = positions
        constant = int(
            remove_score[left] + remove_score[middle] + remove_score[right]
            + 2 * (
                selected_overlap[selected[left], middle]
                + selected_overlap[selected[left], right]
                + selected_overlap[selected[middle], right]
            )
        )
        scores = (
            add_score
            - 2 * selected_overlap[:, left]
            - 2 * selected_overlap[:, middle]
            - 2 * selected_overlap[:, right]
        )
        candidate_scores = scores[unselected_indices]
        local_minima = np.argpartition(candidate_scores, 2)[:3]
        first_three = sorted(
            map(int, unselected_indices[local_minima]),
            key=lambda index: (int(scores[index]), index),
        )
        minima = [int(scores[index]) for index in first_three]
        lower_bound = constant + sum(minima)
        outgoing = tuple(map(int, selected[list(positions)]))
        if lower_bound >= 0:
            assert outgoing not in audited_faces
            continue

        survivors += 1
        keep_mask = unselected & (
            constant + scores + minima[0] + minima[1] < 0
        )
        keep_mask[first_three[0]] = (
            constant + minima[0] + minima[1] + minima[2] < 0
        )
        keep_mask[first_three[1]] = (
            constant + minima[1] + minima[0] + minima[2] < 0
        )
        keep = list(map(int, np.flatnonzero(keep_mask)))
        candidate_sum += len(keep)

        face_best = None
        face_pair_tests = 0
        face_triple_tests = 0
        for first_position, incoming_left in enumerate(keep):
            for second_position in range(first_position + 1, len(keep)):
                incoming_middle = keep[second_position]
                face_pair_tests += 1
                pair_tests += 1
                pair_score = int(
                    scores[incoming_left] + scores[incoming_middle]
                    + 2 * (
                        pair_masks[incoming_left] & pair_masks[incoming_middle]
                    ).bit_count()
                )
                exclusion = next(
                    int(scores[index]) for index in first_three
                    if index not in (incoming_left, incoming_middle)
                )
                if constant + pair_score + exclusion >= 0:
                    continue
                threshold = -constant - pair_score
                for incoming_right in keep[second_position + 1:]:
                    if int(scores[incoming_right]) >= threshold:
                        continue
                    face_triple_tests += 1
                    triple_tests += 1
                    delta = int(
                        constant + pair_score + scores[incoming_right]
                        + 2 * (
                            (
                                pair_masks[incoming_left]
                                & pair_masks[incoming_right]
                            ).bit_count()
                            + (
                                pair_masks[incoming_middle]
                                & pair_masks[incoming_right]
                            ).bit_count()
                        )
                    )
                    candidate = (
                        delta,
                        *outgoing,
                        incoming_left,
                        incoming_middle,
                        incoming_right,
                    )
                    if face_best is None or candidate < face_best:
                        face_best = candidate
                    if best is None or candidate < best:
                        best = candidate

        face = audited_faces[outgoing]
        assert (
            face["candidate_count"],
            face["constant"],
            face["exact_triple_tests"],
            face["lower_bound"],
            face["minima"],
            face["retained_pair_tests"],
            face["tested_best_delta"],
        ) == (
            len(keep),
            constant,
            face_triple_tests,
            lower_bound,
            minima,
            face_pair_tests,
            None if face_best is None else face_best[0],
        )

    assert len(audited_faces) == survivors
    assert report["outgoing_faces"] == 24_804
    assert report["surviving_faces"] == survivors
    assert report["retained_candidate_sum"] == candidate_sum
    assert report["retained_pair_tests"] == pair_tests
    assert report["exact_triple_tests"] == triple_tests
    expected_best = None if best is None else {
        "delta": best[0],
        "remove": list(best[1:4]),
        "add": list(best[4:7]),
    }
    assert report["best_exchange"] == expected_best

    if best is not None and best[0] < 0:
        output = json.loads(Path(report["output_state"]).read_text())
        new_pairs = list(map(int, selected))
        for index in best[1:4]:
            new_pairs.remove(index)
        new_pairs.extend(best[4:7])
        new_pairs.sort()
        assert output["pair_indices"] == new_pairs
        assert output["energy"] == energy + best[0]
        assert report["status"] == "PASS"
    else:
        assert report["status"] == "NO_NEGATIVE_THREE_PAIR_EXCHANGE"
        assert report["output_state"] is None

    return {
        "report": str(report_path),
        "status": report["status"],
        "source_energy": energy,
        "pair_options": len(pair_rows),
        "surviving_faces": survivors,
        "retained_candidate_sum": candidate_sum,
        "retained_pair_tests": pair_tests,
        "exact_triple_tests": triple_tests,
        "best_exchange": expected_best,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("reports", nargs=2, help="E58 descent and E54 no-go JSON")
    args = parser.parse_args()
    summaries = [replay(path) for path in args.reports]
    assert [summary["source_energy"] for summary in summaries] == [58, 54]
    assert [summary["status"] for summary in summaries] == [
        "PASS", "NO_NEGATIVE_THREE_PAIR_EXCHANGE"
    ]
    print(json.dumps({
        "status": "PASS",
        "method": (
            "independent replay of all 24804 outgoing face minima, exact "
            "distinct exclusions, retained pairs/triples, and output state"
        ),
        "cases": summaries,
        "scope": "finite reflected-pair pool only; self lifts fixed",
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
