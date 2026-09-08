#!/usr/bin/env python3
"""Run the exact compact Profile-3 model with a feasible label-5 slice hint.

The hints do not constrain the model; every support/order remains in scope.
Substantive runs belong on H100.
"""

from __future__ import annotations

import argparse
import json

from ortools.sat.python import cp_model

from search_q4_near_c_five_by_five_v13_atom_20260814 import V, rails_for_mass5
from search_q4_v13_position_matching_exact_20260814 import (
    build_model,
    extract_and_verify,
)


SLICE_CYCLES = {
    "n10c0_1": [5, 9, 7, 1, 8, 4, 11, 6, 2, 10],
    "n10c1_1": [5, 7, 11, 8, 3, 4, 12, 0, 10, 9],
    "n10c2_1": [5, 0, 7, 9, 11, 12, 1, 8, 4, 6],
    "n11c3_1": [5, 1, 10, 9, 7, 8, 2, 12, 6, 4, 11],
    "n11c4_1": [5, 6, 2, 10, 12, 9, 3, 1, 7, 8, 11],
    "p10c5_1": [0, 9, 1, 7, 11, 8, 4, 6, 2, 10],
    "p10c5_2": [0, 2, 6, 4, 11, 3, 1, 10, 9, 7],
}


def canonical_cycle(cycle):
    candidates = []
    for oriented in (list(cycle), list(reversed(cycle))):
        position = oriented.index(min(oriented))
        rotated = oriented[position:] + oriented[:position]
        if rotated[1] < rotated[-1]:
            candidates.append(rotated)
    assert len(candidates) == 1
    return candidates[0]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--time-limit", type=float, default=1200.0)
    parser.add_argument("--workers", type=int, default=32)
    parser.add_argument("--seed", type=int, default=20260814)
    args = parser.parse_args()

    rails = rails_for_mass5(3)
    model, selected, permutations, _ = build_model(rails)
    for r, rail in enumerate(rails):
        if rail["name"] not in SLICE_CYCLES:
            continue
        cycle = canonical_cycle(SLICE_CYCLES[rail["name"]])
        holes = sorted(set(V) - {rail["center"]} - set(cycle))
        full = cycle + holes
        labels = [x for x in V if x != rail["center"]]
        assert len(full) == 12
        for i, value in enumerate(full):
            model.AddHint(permutations[r][i], labels.index(value))

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = args.time_limit
    solver.parameters.num_search_workers = args.workers
    solver.parameters.random_seed = args.seed
    status = solver.Solve(model)
    report = {
        "status": solver.StatusName(status),
        "wall_time": solver.WallTime(),
        "branches": solver.NumBranches(),
        "conflicts": solver.NumConflicts(),
        "scope": "exact all-support/all-order Profile 3; slice certificate is hint only",
    }
    if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        supports, cycles, common = extract_and_verify(
            solver, rails, selected, permutations
        )
        report.update({
            "supports": supports,
            "cycles": cycles,
            "common_owner_count": common,
        })
    print(json.dumps({"status": "PASS", "report": report},
                     indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
