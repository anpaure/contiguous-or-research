#!/usr/bin/env python3
"""Replay finite-pool E60/E58 mixed two-exchange reports on H100."""

from __future__ import annotations

import argparse
import itertools
import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, "scratch")
from audit_q4_k17_z17_finite_pool_two_pair_exchange_e62_e60_20260814 import (
    replay as replay_pair,
)
from search_q4_k17_z17_reflection_fixed_face_kissat_20260814 import read_instance


def intersection(left, right):
    return len(set(map(int, left)) & set(map(int, right)))


def replay_mixed(report_path):
    report = json.loads(Path(report_path).read_text())
    _, _, self_raw, pair_raw = read_instance(report["instance"])
    pair_rows = np.asarray(pair_raw, dtype=np.int16)
    self_rows = np.asarray([record[1] for record in self_raw], dtype=np.int16)
    self_groups = np.asarray([record[0] for record in self_raw], dtype=np.int16)
    group_options = [np.flatnonzero(self_groups == group) for group in range(35)]
    state = json.loads(Path(report["source_state"]).read_text())
    selected_pairs = np.asarray(state["pair_indices"], dtype=np.int32)
    selected_self = np.asarray(
        sorted(state["self_indices"], key=lambda index: self_raw[index][0]),
        dtype=np.int32,
    )
    assert len(selected_pairs) == 54 and len(selected_self) == 35
    assert [self_raw[index][0] for index in selected_self] == list(range(35))

    loads = np.zeros(680, dtype=np.int16)
    for index in selected_pairs:
        loads[pair_rows[index]] += 1
    for index in selected_self:
        loads[self_rows[index]] += 1
    energy = int(((loads - 1) ** 2).sum())
    assert energy == state["energy"] == report["source_energy"]

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

    mixed_audit = {
        (face["outgoing_pair"], face["outgoing_self"]): face
        for face in report["mixed_face_audit"]
    }
    self_audit = {
        (face["left_group"], face["right_group"]): face
        for face in report["self_face_audit"]
    }
    best = None
    mixed_faces = self_faces = mixed_tests = self_tests = 0

    for pair_position in range(54):
        for group in range(35):
            constant = int(
                pair_remove[pair_position]
                + self_remove[group]
                + 2 * intersection(
                    selected_pair_rows[pair_position], selected_self_rows[group]
                )
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
            key = (int(selected_pairs[pair_position]), int(selected_self[group]))
            if lower_bound >= 0:
                assert key not in mixed_audit
                continue
            mixed_faces += 1
            pair_candidates = np.flatnonzero(
                unselected_pairs
                & (pair_directed < -constant - self_minimum)
            )
            self_candidates = alternatives[
                self_directed[alternatives] < -constant - pair_minimum
            ]
            face_best = None
            for incoming_pair in map(int, pair_candidates):
                for incoming_self in map(int, self_candidates):
                    mixed_tests += 1
                    delta = int(
                        constant
                        + pair_directed[incoming_pair]
                        + self_directed[incoming_self]
                        + 2 * intersection(
                            pair_rows[incoming_pair], self_rows[incoming_self]
                        )
                    )
                    candidate = (
                        delta,
                        "pair+self",
                        key[0], key[1],
                        incoming_pair, incoming_self,
                    )
                    if face_best is None or candidate < face_best:
                        face_best = candidate
                    if best is None or candidate < best:
                        best = candidate
            face = mixed_audit[key]
            assert (
                face["constant"],
                face["pair_minimum"],
                face["self_minimum"],
                face["lower_bound"],
                face["incoming_pair_candidates"],
                face["incoming_self_candidates"],
                face["tested_best_delta"],
            ) == (
                constant,
                pair_minimum,
                self_minimum,
                lower_bound,
                len(pair_candidates),
                len(self_candidates),
                None if face_best is None else face_best[0],
            )

    for left_group in range(35):
        for right_group in range(left_group + 1, 35):
            constant = int(
                self_remove[left_group]
                + self_remove[right_group]
                + 2 * intersection(
                    selected_self_rows[left_group],
                    selected_self_rows[right_group],
                )
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
            key = (left_group, right_group)
            if lower_bound >= 0:
                assert key not in self_audit
                continue
            self_faces += 1
            left_candidates = left_options[
                directed[left_options] < -constant - right_minimum
            ]
            right_candidates = right_options[
                directed[right_options] < -constant - left_minimum
            ]
            face_best = None
            for incoming_left in map(int, left_candidates):
                for incoming_right in map(int, right_candidates):
                    self_tests += 1
                    delta = int(
                        constant
                        + directed[incoming_left]
                        + directed[incoming_right]
                        + 2 * intersection(
                            self_rows[incoming_left], self_rows[incoming_right]
                        )
                    )
                    candidate = (
                        delta,
                        "self+self",
                        int(selected_self[left_group]),
                        int(selected_self[right_group]),
                        incoming_left,
                        incoming_right,
                    )
                    if face_best is None or candidate < face_best:
                        face_best = candidate
                    if best is None or candidate < best:
                        best = candidate
            face = self_audit[key]
            assert (
                face["constant"],
                face["left_minimum"],
                face["right_minimum"],
                face["lower_bound"],
                face["incoming_left_candidates"],
                face["incoming_right_candidates"],
                face["tested_best_delta"],
            ) == (
                constant,
                left_minimum,
                right_minimum,
                lower_bound,
                len(left_candidates),
                len(right_candidates),
                None if face_best is None else face_best[0],
            )

    assert len(mixed_audit) == mixed_faces
    assert len(self_audit) == self_faces
    assert report["mixed_exact_tests"] == mixed_tests
    assert report["self_exact_tests"] == self_tests
    expected_best = None if best is None else {
        "delta": best[0],
        "kind": best[1],
        "remove": [best[2], best[3]],
        "add": [best[4], best[5]],
    }
    assert report["best_exchange"] == expected_best
    if best is not None and best[0] < 0:
        output = json.loads(Path(report["output_state"]).read_text())
        assert output["energy"] == energy + best[0]
        assert report["status"] == "PASS"
    else:
        assert report["status"] == "NO_NEGATIVE_MIXED_TWO_EXCHANGE"
        assert report["output_state"] is None
    return {
        "report": str(report_path),
        "status": report["status"],
        "source_energy": energy,
        "mixed_surviving_faces": mixed_faces,
        "self_surviving_faces": self_faces,
        "mixed_exact_tests": mixed_tests,
        "self_exact_tests": self_tests,
        "best_exchange": expected_best,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("e60_mixed")
    parser.add_argument("e58_pair")
    parser.add_argument("e58_mixed")
    args = parser.parse_args()
    e60 = replay_mixed(args.e60_mixed)
    e58_pair = replay_pair(args.e58_pair)
    e58_mixed = replay_mixed(args.e58_mixed)
    assert e60["source_energy"] == 60 and e60["status"] == "PASS"
    assert e58_pair["source_energy"] == 58
    assert e58_pair["status"] == "NO_NEGATIVE_TWO_PAIR_EXCHANGE"
    assert e58_mixed["source_energy"] == 58
    assert e58_mixed["status"] == "NO_NEGATIVE_MIXED_TWO_EXCHANGE"
    print(json.dumps({
        "status": "PASS",
        "method": (
            "independent replay of all pair+self, self+self, and pair+pair "
            "face minima, thresholds, surviving tests, and E58 state"
        ),
        "e60_mixed": e60,
        "e58_pair": e58_pair,
        "e58_mixed": e58_mixed,
        "scope": "finite 174462-pair/3749-self face only",
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
