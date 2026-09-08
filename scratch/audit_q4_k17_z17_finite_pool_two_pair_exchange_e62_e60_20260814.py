#!/usr/bin/env python3
"""Independently replay the E62/E60 finite-pool two-pair reports (H100)."""

from __future__ import annotations

import argparse
import itertools
import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, "scratch")
from search_q4_k17_z17_reflection_fixed_face_kissat_20260814 import read_instance


def intersection(left, right):
    return len(set(map(int, left)) & set(map(int, right)))


def replay(report_path):
    report = json.loads(Path(report_path).read_text())
    _, _, self_raw, pair_raw = read_instance(report["instance"])
    pair_rows = np.asarray(pair_raw, dtype=np.int16)
    self_rows = np.asarray([record[1] for record in self_raw], dtype=np.int16)
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
    intersections = np.empty((len(pair_rows), 54), dtype=np.uint8)
    for position, rows in enumerate(selected_rows):
        intersections[:, position] = np.isin(pair_rows, rows).sum(axis=1)
    unselected = np.ones(len(pair_rows), dtype=bool)
    unselected[selected] = False
    audited_faces = {
        (face["outgoing_left"], face["outgoing_right"]): face
        for face in report["face_audit"]
    }

    surviving_faces = 0
    survivor_sum = 0
    pair_tests = 0
    best = None
    for left in range(54):
        for right in range(left + 1, 54):
            constant = int(
                remove_score[left]
                + remove_score[right]
                + 2 * intersection(selected_rows[left], selected_rows[right])
            )
            directed = (
                add_score
                - 2 * intersections[:, left]
                - 2 * intersections[:, right]
            )
            minimum = int(directed[unselected].min())
            lower_bound = constant + 2 * minimum
            key = (int(selected[left]), int(selected[right]))
            if lower_bound >= 0:
                assert key not in audited_faces
                continue

            surviving_faces += 1
            threshold = -constant - minimum
            candidates = np.flatnonzero(unselected & (directed < threshold))
            survivor_sum += len(candidates)
            face_best = None
            for incoming_left, incoming_right in itertools.combinations(
                map(int, candidates), 2
            ):
                pair_tests += 1
                delta = int(
                    constant
                    + directed[incoming_left]
                    + directed[incoming_right]
                    + 2 * intersection(
                        pair_rows[incoming_left], pair_rows[incoming_right]
                    )
                )
                candidate = (
                    delta,
                    key[0], key[1],
                    incoming_left, incoming_right,
                )
                if face_best is None or candidate < face_best:
                    face_best = candidate
                if best is None or candidate < best:
                    best = candidate

            face = audited_faces[key]
            assert (
                face["constant"],
                face["directed_minimum"],
                face["lower_bound"],
                face["threshold"],
                face["candidate_count"],
                face["tested_best_delta"],
            ) == (
                constant,
                minimum,
                lower_bound,
                threshold,
                len(candidates),
                None if face_best is None else face_best[0],
            )

    assert len(audited_faces) == surviving_faces
    assert report["outgoing_faces"] == 1431
    assert report["surviving_faces"] == surviving_faces
    assert report["threshold_survivor_sum"] == survivor_sum
    assert report["exact_incoming_pair_tests"] == pair_tests
    expected_best = None if best is None else {
        "delta": best[0],
        "remove": [best[1], best[2]],
        "add": [best[3], best[4]],
    }
    assert report["best_exchange"] == expected_best

    if best is not None and best[0] < 0:
        output = json.loads(Path(report["output_state"]).read_text())
        new_pairs = list(map(int, selected))
        new_pairs.remove(best[1])
        new_pairs.remove(best[2])
        new_pairs.extend((best[3], best[4]))
        new_pairs.sort()
        assert output["pair_indices"] == new_pairs
        assert output["energy"] == energy + best[0]
        assert report["status"] == "PASS"
    else:
        assert report["status"] == "NO_NEGATIVE_TWO_PAIR_EXCHANGE"
        assert report["output_state"] is None

    return {
        "report": str(report_path),
        "status": report["status"],
        "source_energy": energy,
        "pair_options": len(pair_rows),
        "surviving_faces": surviving_faces,
        "threshold_survivor_sum": survivor_sum,
        "exact_incoming_pair_tests": pair_tests,
        "best_exchange": expected_best,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("reports", nargs="+", help="two-pair JSON reports")
    args = parser.parse_args()
    summaries = [replay(path) for path in args.reports]
    assert [summary["source_energy"] for summary in summaries] == [62, 60]
    assert [summary["status"] for summary in summaries] == [
        "PASS", "NO_NEGATIVE_TWO_PAIR_EXCHANGE"
    ]
    print(json.dumps({
        "status": "PASS",
        "method": (
            "independent full replay of all 1431 face minima, exact strict "
            "thresholds, every surviving incoming pair, and output state"
        ),
        "cases": summaries,
        "scope": "finite pair pools only; self lifts held fixed",
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
