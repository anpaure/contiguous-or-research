#!/usr/bin/env python3
"""Independently replay the E46 finite-pool PPS/PSS/SSS report (H100)."""

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
    value = 0
    for row in rows:
        value |= 1 << int(row)
    return value


def direct_delta(loads, pair_rows, self_rows, kinds, old, new):
    changed = loads.copy()
    for kind, index in zip(kinds, old):
        changed[(pair_rows if kind == "P" else self_rows)[index]] -= 1
    for kind, index in zip(kinds, new):
        changed[(pair_rows if kind == "P" else self_rows)[index]] += 1
    return int(((changed - 1) ** 2).sum() - ((loads - 1) ** 2).sum())


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("report")
    args = parser.parse_args()
    report = json.loads(Path(args.report).read_text())
    _, _, self_raw, pair_raw = read_instance(report["instance"])
    pair_rows = np.asarray(pair_raw, dtype=np.int16)
    self_rows = np.asarray([record[1] for record in self_raw], dtype=np.int16)
    self_groups = np.asarray([record[0] for record in self_raw], dtype=np.int16)
    pair_masks = [row_mask(rows) for rows in pair_raw]
    self_masks = [row_mask(record[1]) for record in self_raw]
    group_options = [np.flatnonzero(self_groups == group) for group in range(35)]
    state = json.loads(Path(report["source_state"]).read_text())
    selected_pairs = np.asarray(state["pair_indices"], dtype=np.int32)
    selected_self = np.asarray(
        sorted(state["self_indices"], key=lambda index: self_raw[index][0]),
        dtype=np.int32,
    )
    assert len(selected_pairs) == len(set(map(int, selected_pairs))) == 54
    assert [self_raw[index][0] for index in selected_self] == list(range(35))

    loads = np.zeros(680, dtype=np.int16)
    for index in selected_pairs:
        loads[pair_rows[index]] += 1
    for index in selected_self:
        loads[self_rows[index]] += 1
    energy = int(((loads - 1) ** 2).sum())
    assert energy == state["energy"] == report["source_energy"] == 46

    selected_pair_rows = pair_rows[selected_pairs]
    selected_self_rows = self_rows[selected_self]
    pair_add = (2 * loads[pair_rows] - 1).sum(axis=1).astype(np.int32)
    self_add = (2 * loads[self_rows] - 1).sum(axis=1).astype(np.int32)
    pair_remove = (3 - 2 * loads[selected_pair_rows]).sum(axis=1).astype(np.int32)
    self_remove = (3 - 2 * loads[selected_self_rows]).sum(axis=1).astype(np.int32)

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

    audited = {
        (face["kind"], tuple(face["out"])): face for face in report["face_audit"]
    }
    counts = {
        "pps_faces": 0, "pss_faces": 0, "sss_faces": 0,
        "pps_survivors": 0, "pss_survivors": 0, "sss_survivors": 0,
        "pps_tests": 0, "pss_tests": 0, "sss_tests": 0,
    }
    best = None

    for left, right in itertools.combinations(range(54), 2):
        for group in range(35):
            counts["pps_faces"] += 1
            old = (
                int(selected_pairs[left]), int(selected_pairs[right]),
                int(selected_self[group]),
            )
            constant = int(
                pair_remove[left] + pair_remove[right] + self_remove[group]
                + 2 * (
                    (pair_masks[old[0]] & pair_masks[old[1]]).bit_count()
                    + (pair_masks[old[0]] & self_masks[old[2]]).bit_count()
                    + (pair_masks[old[1]] & self_masks[old[2]]).bit_count()
                )
            )
            pair_score = (
                pair_add - 2 * pair_vs_pair[:, left]
                - 2 * pair_vs_pair[:, right] - 2 * pair_vs_self[:, group]
            )
            pair_score[selected_pairs] = 30_000
            self_score = (
                self_add - 2 * self_vs_pair[:, left]
                - 2 * self_vs_pair[:, right] - 2 * self_vs_self[:, group]
            )
            alternatives = group_options[group]
            alternatives = alternatives[alternatives != selected_self[group]]
            first_two = np.argpartition(pair_score, 1)[:2]
            first_two = sorted(
                map(int, first_two),
                key=lambda index: (int(pair_score[index]), index),
            )
            first_value, second_value = (
                int(pair_score[index]) for index in first_two
            )
            self_minimum = int(self_score[alternatives].min())
            key = ("PPS", old)
            if constant + first_value + second_value + self_minimum >= 0:
                assert key not in audited
                continue

            counts["pps_survivors"] += 1
            keep = unselected_pairs & (
                constant + pair_score + first_value + self_minimum < 0
            )
            keep[first_two[0]] = (
                constant + first_value + second_value + self_minimum < 0
            )
            pair_candidates = list(map(int, np.flatnonzero(keep)))
            self_candidates = list(map(int, alternatives[
                constant + self_score[alternatives]
                + first_value + second_value < 0
            ]))
            face_best = None
            for first_position, incoming_left in enumerate(pair_candidates):
                for incoming_right in pair_candidates[first_position + 1:]:
                    prefix = int(
                        pair_score[incoming_left] + pair_score[incoming_right]
                        + 2 * (
                            pair_masks[incoming_left] & pair_masks[incoming_right]
                        ).bit_count()
                    )
                    if constant + prefix + self_minimum >= 0:
                        continue
                    for incoming_self in self_candidates:
                        if self_score[incoming_self] >= -constant - prefix:
                            continue
                        counts["pps_tests"] += 1
                        delta = int(
                            constant + prefix + self_score[incoming_self]
                            + 2 * (
                                (pair_masks[incoming_left] & self_masks[incoming_self]).bit_count()
                                + (pair_masks[incoming_right] & self_masks[incoming_self]).bit_count()
                            )
                        )
                        new = (incoming_left, incoming_right, incoming_self)
                        assert delta == direct_delta(
                            loads, pair_rows, self_rows, ("P", "P", "S"), old, new
                        )
                        candidate = (delta, "PPS", *old, *new)
                        if face_best is None or candidate < face_best:
                            face_best = candidate
                        if best is None or candidate < best:
                            best = candidate
            face = audited[key]
            assert (face["pc"], face["sc"], face["best"]) == (
                len(pair_candidates), len(self_candidates),
                None if face_best is None else face_best[0],
            )

    for pair_position in range(54):
        for left_group, right_group in itertools.combinations(range(35), 2):
            counts["pss_faces"] += 1
            old = (
                int(selected_pairs[pair_position]),
                int(selected_self[left_group]), int(selected_self[right_group]),
            )
            constant = int(
                pair_remove[pair_position] + self_remove[left_group]
                + self_remove[right_group]
                + 2 * (
                    (pair_masks[old[0]] & self_masks[old[1]]).bit_count()
                    + (pair_masks[old[0]] & self_masks[old[2]]).bit_count()
                    + (self_masks[old[1]] & self_masks[old[2]]).bit_count()
                )
            )
            pair_score = (
                pair_add - 2 * pair_vs_pair[:, pair_position]
                - 2 * pair_vs_self[:, left_group]
                - 2 * pair_vs_self[:, right_group]
            )
            pair_score[selected_pairs] = 30_000
            self_score = (
                self_add - 2 * self_vs_pair[:, pair_position]
                - 2 * self_vs_self[:, left_group]
                - 2 * self_vs_self[:, right_group]
            )
            left_options = group_options[left_group]
            left_options = left_options[left_options != selected_self[left_group]]
            right_options = group_options[right_group]
            right_options = right_options[right_options != selected_self[right_group]]
            pair_minimum = int(pair_score.min())
            left_minimum = int(self_score[left_options].min())
            right_minimum = int(self_score[right_options].min())
            key = ("PSS", old)
            if constant + pair_minimum + left_minimum + right_minimum >= 0:
                assert key not in audited
                continue

            counts["pss_survivors"] += 1
            pair_candidates = list(map(int, np.flatnonzero(
                unselected_pairs
                & (constant + pair_score + left_minimum + right_minimum < 0)
            )))
            left_candidates = list(map(int, left_options[
                constant + self_score[left_options]
                + pair_minimum + right_minimum < 0
            ]))
            right_candidates = list(map(int, right_options[
                constant + self_score[right_options]
                + pair_minimum + left_minimum < 0
            ]))
            face_best = None
            for incoming_pair in pair_candidates:
                for incoming_left in left_candidates:
                    prefix = int(
                        pair_score[incoming_pair] + self_score[incoming_left]
                        + 2 * (
                            pair_masks[incoming_pair] & self_masks[incoming_left]
                        ).bit_count()
                    )
                    if constant + prefix + right_minimum >= 0:
                        continue
                    for incoming_right in right_candidates:
                        if self_score[incoming_right] >= -constant - prefix:
                            continue
                        counts["pss_tests"] += 1
                        delta = int(
                            constant + prefix + self_score[incoming_right]
                            + 2 * (
                                (pair_masks[incoming_pair] & self_masks[incoming_right]).bit_count()
                                + (self_masks[incoming_left] & self_masks[incoming_right]).bit_count()
                            )
                        )
                        new = (incoming_pair, incoming_left, incoming_right)
                        assert delta == direct_delta(
                            loads, pair_rows, self_rows, ("P", "S", "S"), old, new
                        )
                        candidate = (delta, "PSS", *old, *new)
                        if face_best is None or candidate < face_best:
                            face_best = candidate
                        if best is None or candidate < best:
                            best = candidate
            face = audited[key]
            assert (face["pc"], face["gc"], face["hc"], face["best"]) == (
                len(pair_candidates), len(left_candidates), len(right_candidates),
                None if face_best is None else face_best[0],
            )

    for left_group, middle_group, right_group in itertools.combinations(range(35), 3):
        counts["sss_faces"] += 1
        old = (
            int(selected_self[left_group]), int(selected_self[middle_group]),
            int(selected_self[right_group]),
        )
        constant = int(
            self_remove[left_group] + self_remove[middle_group]
            + self_remove[right_group]
            + 2 * (
                (self_masks[old[0]] & self_masks[old[1]]).bit_count()
                + (self_masks[old[0]] & self_masks[old[2]]).bit_count()
                + (self_masks[old[1]] & self_masks[old[2]]).bit_count()
            )
        )
        self_score = (
            self_add - 2 * self_vs_self[:, left_group]
            - 2 * self_vs_self[:, middle_group]
            - 2 * self_vs_self[:, right_group]
        )
        left_options = group_options[left_group]
        left_options = left_options[left_options != selected_self[left_group]]
        middle_options = group_options[middle_group]
        middle_options = middle_options[middle_options != selected_self[middle_group]]
        right_options = group_options[right_group]
        right_options = right_options[right_options != selected_self[right_group]]
        left_minimum = int(self_score[left_options].min())
        middle_minimum = int(self_score[middle_options].min())
        right_minimum = int(self_score[right_options].min())
        key = ("SSS", old)
        if constant + left_minimum + middle_minimum + right_minimum >= 0:
            assert key not in audited
            continue

        counts["sss_survivors"] += 1
        left_candidates = list(map(int, left_options[
            constant + self_score[left_options]
            + middle_minimum + right_minimum < 0
        ]))
        middle_candidates = list(map(int, middle_options[
            constant + self_score[middle_options]
            + left_minimum + right_minimum < 0
        ]))
        right_candidates = list(map(int, right_options[
            constant + self_score[right_options]
            + left_minimum + middle_minimum < 0
        ]))
        face_best = None
        for incoming_left in left_candidates:
            for incoming_middle in middle_candidates:
                prefix = int(
                    self_score[incoming_left] + self_score[incoming_middle]
                    + 2 * (
                        self_masks[incoming_left] & self_masks[incoming_middle]
                    ).bit_count()
                )
                if constant + prefix + right_minimum >= 0:
                    continue
                for incoming_right in right_candidates:
                    if self_score[incoming_right] >= -constant - prefix:
                        continue
                    counts["sss_tests"] += 1
                    delta = int(
                        constant + prefix + self_score[incoming_right]
                        + 2 * (
                            (self_masks[incoming_left] & self_masks[incoming_right]).bit_count()
                            + (self_masks[incoming_middle] & self_masks[incoming_right]).bit_count()
                        )
                    )
                    new = (incoming_left, incoming_middle, incoming_right)
                    assert delta == direct_delta(
                        loads, pair_rows, self_rows, ("S", "S", "S"), old, new
                    )
                    candidate = (delta, "SSS", *old, *new)
                    if face_best is None or candidate < face_best:
                        face_best = candidate
                    if best is None or candidate < best:
                        best = candidate
        face = audited[key]
        assert (face["gc"], face["hc"], face["kc"], face["best"]) == (
            len(left_candidates), len(middle_candidates), len(right_candidates),
            None if face_best is None else face_best[0],
        )

    assert len(audited) == (
        counts["pps_survivors"] + counts["pss_survivors"]
        + counts["sss_survivors"]
    )
    for key, value in counts.items():
        assert report[key] == value
    assert report["outgoing_faces"] == sum(
        counts[key] for key in ("pps_faces", "pss_faces", "sss_faces")
    ) == 88_760
    expected_best = None if best is None else {
        "delta": best[0], "kind": best[1],
        "remove": list(best[2:5]), "add": list(best[5:8]),
    }
    assert report["best_exchange"] == expected_best
    assert best is not None and best[0] == 2
    assert report["status"] == "NO_NEGATIVE_MIXED_THREE_EXCHANGE"
    assert report["output_state"] is None

    print(json.dumps({
        "status": "PASS",
        "method": (
            "independent replay of all 88760 PPS/PSS/SSS face cuts, "
            "typed group menus, retained leaves, and direct load deltas"
        ),
        "source_energy": energy,
        "pair_options": len(pair_rows),
        "self_options": len(self_rows),
        **counts,
        "outgoing_faces": 88_760,
        "least_tested_leaf": expected_best,
        "scope": "finite 223564-pair/3749-self snapshot only",
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
