#!/usr/bin/env python3
"""Independently replay the finite-pool E46 four-pair report (H100)."""

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


def exclusion_sum(scores, first_four, excluded, count):
    values = []
    for index in first_four:
        if index not in excluded:
            values.append(int(scores[index]))
            if len(values) == count:
                return sum(values)
    raise AssertionError("insufficient exclusion entries")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("report")
    args = parser.parse_args()
    report = json.loads(Path(args.report).read_text())
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
    assert energy == state["energy"] == report["source_energy"] == 46

    selected_rows = pair_rows[selected]
    add_score = (2 * loads[pair_rows] - 1).sum(axis=1).astype(np.int32)
    remove_score = (3 - 2 * loads[selected_rows]).sum(axis=1).astype(np.int32)
    selected_overlap = np.empty((len(pair_rows), 54), dtype=np.uint8)
    for position, rows in enumerate(selected_rows):
        selected_overlap[:, position] = np.isin(pair_rows, rows).sum(axis=1)
    unselected = np.ones(len(pair_rows), dtype=bool)
    unselected[selected] = False

    audited_faces = {
        tuple(face["outgoing"]): face for face in report["face_audit"]
    }
    survivors = candidate_sum = pair_tests = triple_tests = quad_tests = 0
    best = None

    for positions in itertools.combinations(range(54), 4):
        constant = int(sum(remove_score[position] for position in positions))
        for left, right in itertools.combinations(positions, 2):
            constant += 2 * int(selected_overlap[selected[left], right])
        scores = add_score.copy()
        for position in positions:
            scores -= 2 * selected_overlap[:, position]
        scores[selected] = 30_000

        first_four = np.argpartition(scores, 3)[:4]
        first_four = sorted(
            map(int, first_four), key=lambda index: (int(scores[index]), index)
        )
        minima = [int(scores[index]) for index in first_four]
        lower_bound = constant + sum(minima)
        outgoing = tuple(map(int, selected[list(positions)]))
        if lower_bound >= 0:
            assert outgoing not in audited_faces
            continue

        survivors += 1
        keep_mask = unselected & (
            constant + scores + minima[0] + minima[1] + minima[2] < 0
        )
        for index in first_four[:3]:
            keep_mask[index] = (
                constant + int(scores[index])
                + exclusion_sum(scores, first_four, {index}, 3) < 0
            )
        candidates = list(map(int, np.flatnonzero(keep_mask)))
        candidate_sum += len(candidates)

        face_best = None
        face_pairs = face_triples = face_quads = 0
        for first_position, incoming_first in enumerate(candidates):
            first_mask = pair_masks[incoming_first]
            for second_position in range(first_position + 1, len(candidates)):
                incoming_second = candidates[second_position]
                second_mask = pair_masks[incoming_second]
                face_pairs += 1
                pair_tests += 1
                pair_score = int(
                    scores[incoming_first] + scores[incoming_second]
                    + 2 * (first_mask & second_mask).bit_count()
                )
                if constant + pair_score + exclusion_sum(
                    scores, first_four,
                    {incoming_first, incoming_second}, 2,
                ) >= 0:
                    continue
                for third_position in range(second_position + 1, len(candidates)):
                    incoming_third = candidates[third_position]
                    third_mask = pair_masks[incoming_third]
                    face_triples += 1
                    triple_tests += 1
                    triple_score = int(
                        pair_score + scores[incoming_third]
                        + 2 * (
                            (first_mask & third_mask).bit_count()
                            + (second_mask & third_mask).bit_count()
                        )
                    )
                    if constant + triple_score + exclusion_sum(
                        scores, first_four,
                        {incoming_first, incoming_second, incoming_third}, 1,
                    ) >= 0:
                        continue
                    threshold = -constant - triple_score
                    for incoming_fourth in candidates[third_position + 1:]:
                        if int(scores[incoming_fourth]) >= threshold:
                            continue
                        fourth_mask = pair_masks[incoming_fourth]
                        face_quads += 1
                        quad_tests += 1
                        delta = int(
                            constant + triple_score + scores[incoming_fourth]
                            + 2 * (
                                (first_mask & fourth_mask).bit_count()
                                + (second_mask & fourth_mask).bit_count()
                                + (third_mask & fourth_mask).bit_count()
                            )
                        )
                        candidate = (
                            delta,
                            *outgoing,
                            incoming_first,
                            incoming_second,
                            incoming_third,
                            incoming_fourth,
                        )
                        if face_best is None or candidate < face_best:
                            face_best = candidate
                        if best is None or candidate < best:
                            best = candidate

        face = audited_faces[outgoing]
        assert (
            face["candidate_count"],
            face["constant"],
            face["exact_quadruple_tests"],
            face["lower_bound"],
            face["minima"],
            face["retained_pair_tests"],
            face["retained_triple_tests"],
            face["tested_best_delta"],
        ) == (
            len(candidates),
            constant,
            face_quads,
            lower_bound,
            minima,
            face_pairs,
            face_triples,
            None if face_best is None else face_best[0],
        )

    assert len(audited_faces) == survivors
    assert report["outgoing_faces"] == 316_251
    assert report["surviving_faces"] == survivors
    assert report["retained_candidate_sum"] == candidate_sum
    assert report["retained_pair_tests"] == pair_tests
    assert report["retained_triple_tests"] == triple_tests
    assert report["exact_quadruple_tests"] == quad_tests
    expected_best = None if best is None else {
        "delta": best[0],
        "remove": list(best[1:5]),
        "add": list(best[5:9]),
    }
    assert report["best_exchange"] == expected_best
    assert best is not None and best[0] == 8
    assert report["status"] == "NO_NEGATIVE_FOUR_PAIR_EXCHANGE"
    assert report["output_state"] is None

    print(json.dumps({
        "status": "PASS",
        "method": (
            "independent replay of all 316251 face cuts, exact distinct "
            "exclusions, retained prefixes, and literal quadruples"
        ),
        "source_energy": energy,
        "pair_options": len(pair_rows),
        "outgoing_faces": 316_251,
        "surviving_faces": survivors,
        "retained_candidate_sum": candidate_sum,
        "retained_pair_tests": pair_tests,
        "retained_triple_tests": triple_tests,
        "exact_quadruple_tests": quad_tests,
        "best_exchange": expected_best,
        "scope": "finite reflected-pair pool only; self lifts fixed",
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
