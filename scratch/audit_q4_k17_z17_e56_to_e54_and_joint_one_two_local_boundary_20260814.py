#!/usr/bin/env python3
"""Replay E56->E54 and the final one/two-local finite-face boundary (H100)."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, "scratch")
from audit_q4_k17_z17_finite_pool_mixed_two_exchange_e60_e58_20260814 import (
    replay_mixed,
)
from audit_q4_k17_z17_finite_pool_two_pair_exchange_e62_e60_20260814 import (
    replay as replay_pair,
)
from search_q4_k17_z17_reflection_fixed_face_kissat_20260814 import read_instance


def replay_one(report_path):
    report = json.loads(Path(report_path).read_text())
    _, _, self_raw, pair_raw = read_instance(report["instance"])
    pair_rows = np.asarray(pair_raw, dtype=np.int16)
    self_rows = np.asarray([record[1] for record in self_raw], dtype=np.int16)
    self_groups = np.asarray([record[0] for record in self_raw], dtype=np.int16)
    group_options = [np.flatnonzero(self_groups == group) for group in range(35)]
    state = json.loads(Path(report["source_state"]).read_text())

    loads = np.zeros(680, dtype=np.int16)
    for index in state["pair_indices"]:
        loads[pair_rows[index]] += 1
    for index in state["self_indices"]:
        loads[self_rows[index]] += 1
    energy = int(((loads - 1) ** 2).sum())
    assert energy == state["energy"] == report["source_energy"]

    selected_mask = np.zeros(len(pair_rows), dtype=bool)
    selected_mask[state["pair_indices"]] = True
    best_pair = None
    for position, old in enumerate(state["pair_indices"]):
        reduced = loads.copy()
        reduced[pair_rows[old]] -= 1
        removal_delta = int(((reduced - 1) ** 2).sum() - energy)
        deltas = removal_delta + (2 * reduced[pair_rows] - 1).sum(axis=1)
        deltas[selected_mask] = 100_000
        new = int(deltas.argmin())
        candidate = (int(deltas[new]), old, new, position)
        if best_pair is None or candidate < best_pair:
            best_pair = candidate

    selected_by_group = {
        self_raw[index][0]: index for index in state["self_indices"]
    }
    best_self = None
    for group in range(35):
        old = selected_by_group[group]
        reduced = loads.copy()
        reduced[self_rows[old]] -= 1
        removal_delta = int(((reduced - 1) ** 2).sum() - energy)
        options = group_options[group]
        deltas = removal_delta + (2 * reduced[self_rows[options]] - 1).sum(axis=1)
        deltas[options == old] = 100_000
        offset = int(deltas.argmin())
        new = int(options[offset])
        candidate = (int(deltas[offset]), old, new, group)
        if best_self is None or candidate < best_self:
            best_self = candidate

    expected_pair = {
        "delta": best_pair[0], "old": best_pair[1], "new": best_pair[2]
    }
    expected_self = {
        "delta": best_self[0], "old": best_self[1], "new": best_self[2]
    }
    assert report["best_remaining_pair_swap"] == expected_pair
    assert report["best_remaining_self_swap"] == expected_self
    assert best_pair[0] >= 0 and best_self[0] >= 0
    assert report["iterations"] == 0 and report["trajectory"] == []
    assert report["final_energy"] == energy
    output = json.loads(Path(report["output_state"]).read_text())
    assert output["pair_indices"] == state["pair_indices"]
    assert output["self_indices"] == state["self_indices"]
    assert output["energy"] == energy
    return {
        "report": str(report_path),
        "status": "NO_NEGATIVE_ONE_EXCHANGE",
        "source_energy": energy,
        "best_remaining_pair_swap": expected_pair,
        "best_remaining_self_swap": expected_self,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("e56_pair")
    parser.add_argument("e54_one")
    parser.add_argument("e54_pair")
    parser.add_argument("e54_mixed")
    args = parser.parse_args()

    descent = replay_pair(args.e56_pair)
    one = replay_one(args.e54_one)
    pair = replay_pair(args.e54_pair)
    mixed = replay_mixed(args.e54_mixed)
    assert descent["source_energy"] == 56 and descent["status"] == "PASS"
    assert descent["best_exchange"]["delta"] == -2
    assert one["source_energy"] == 54
    assert pair["source_energy"] == 54
    assert pair["status"] == "NO_NEGATIVE_TWO_PAIR_EXCHANGE"
    assert mixed["source_energy"] == 54
    assert mixed["status"] == "NO_NEGATIVE_MIXED_TWO_EXCHANGE"

    print(json.dumps({
        "status": "PASS",
        "method": (
            "independent E56 pair2 descent replay and complete E54 one- and "
            "two-exchange replay over pair, pair+self, and self+self menus"
        ),
        "e56_pair_descent": descent,
        "e54_one_boundary": one,
        "e54_pair_two_boundary": pair,
        "e54_mixed_two_boundary": mixed,
        "scope": (
            "finite 189462-pair/3749-self face; three-local mixed menus "
            "not included"
        ),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
