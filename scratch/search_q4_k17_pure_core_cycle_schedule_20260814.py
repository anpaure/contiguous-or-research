#!/usr/bin/env python3
"""Solve the factor-independent q4/k17 labelled-core cycle schedule.

Run substantively on H100 only.  For face t there are 143-11t cycles of
length ten and 10t cycles of length eleven.  Each position is one of the 72
labelled five-core states.  Consecutive states, including each cyclic wrap,
must obey the exact refresh relation, and the aggregate nine type counts
must equal the frozen 1,430-position census.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from collections import Counter
from pathlib import Path

from ortools.sat.python import cp_model


CORE = frozenset(range(5))
TYPES = (
    (1, 5, 2, 1),
    (1, 6, 1, 1),
    (2, 5, 1, 1),
    (3, 3, 2, 1),
    (3, 4, 1, 1),
    (4, 3, 1, 1),
    (5, 1, 2, 1),
    (5, 2, 1, 1),
    (6, 1, 1, 1),
)
TYPE_COUNTS = (139, 297, 8, 20, 20, 140, 127, 237, 442)


def partitions(sizes):
    values = tuple(CORE)
    for middle in itertools.combinations(values, sizes[1]):
        middle = frozenset(middle)
        remaining = tuple(x for x in values if x not in middle)
        for old in itertools.combinations(remaining, sizes[2]):
            old = frozenset(old)
            fresh = CORE - middle - old
            assert len(fresh) == sizes[0]
            yield fresh, middle, old


def state_catalogue():
    states = []
    for type_id, kind in enumerate(TYPES):
        sizes = tuple(value - 1 for value in kind[:3])
        for parts in partitions(sizes):
            states.append({"type": type_id, "parts": parts})
    assert len(states) == 72
    arcs = []
    for i, old in enumerate(states):
        for j, new in enumerate(states):
            if new["parts"][1] <= old["parts"][0] and new["parts"][2] <= old["parts"][1]:
                arcs.append((i, j))
    return states, arcs


def solve_face(t, states, arcs, time_limit, workers, seed):
    number10 = 143 - 11 * t
    number11 = 10 * t
    assert number10 >= 0 and 10 * number10 + 11 * number11 == 1430
    model = cp_model.CpModel()
    cycles = []
    type_variables = []
    for length, number in ((10, number10), (11, number11)):
        family = []
        for cycle_id in range(number):
            row = [
                model.new_int_var(0, len(states) - 1, f"s_{length}_{cycle_id}_{position}")
                for position in range(length)
            ]
            types = [
                model.new_int_var(0, len(TYPES) - 1, f"q_{length}_{cycle_id}_{position}")
                for position in range(length)
            ]
            for position in range(length):
                model.add_allowed_assignments(
                    [row[position], row[(position + 1) % length]], arcs
                )
                model.add_allowed_assignments(
                    [row[position], types[position]],
                    [(state_id, state["type"]) for state_id, state in enumerate(states)],
                )
                model.add(row[0] <= row[position])
            family.append(row)
            cycles.append((length, row, types))
            type_variables.extend(types)
        for left, right in zip(family, family[1:]):
            model.add(left[0] <= right[0])

    indicators = [[] for _ in TYPES]
    for position, variable in enumerate(type_variables):
        for type_id in range(len(TYPES)):
            flag = model.new_bool_var(f"is_{position}_{type_id}")
            model.add(variable == type_id).only_enforce_if(flag)
            model.add(variable != type_id).only_enforce_if(flag.Not())
            indicators[type_id].append(flag)
    for type_id, count in enumerate(TYPE_COUNTS):
        model.add(sum(indicators[type_id]) == count)

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = time_limit
    solver.parameters.num_search_workers = workers
    solver.parameters.random_seed = seed
    solver.parameters.cp_model_presolve = True
    solver.parameters.symmetry_level = 3
    status = solver.solve(model)
    status_name = solver.status_name(status)
    if status not in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        return {
            "t": t,
            "number_period_10": number10,
            "number_period_11": number11,
            "status": status_name,
            "wall_time": solver.wall_time,
            "conflicts": solver.num_conflicts,
            "branches": solver.num_branches,
            "cycle_multiset": None,
        }

    multiplicities = Counter()
    for length, row, _ in cycles:
        word = tuple(solver.value(variable) for variable in row)
        assert word[0] == min(word)
        multiplicities[(length, word)] += 1
    return {
        "t": t,
        "number_period_10": number10,
        "number_period_11": number11,
        "status": status_name,
        "wall_time": solver.wall_time,
        "conflicts": solver.num_conflicts,
        "branches": solver.num_branches,
        "cycle_multiset": [
            {"period": key[0], "state_ids": key[1], "multiplicity": value}
            for key, value in sorted(multiplicities.items())
        ],
    }


def encode_state(state_id, state):
    return {
        "state_id": state_id,
        "type_id": state["type"],
        "type": TYPES[state["type"]],
        "core_classes": [sorted(part) for part in state["parts"]],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("source")
    parser.add_argument("--faces", default="0-13")
    parser.add_argument("--time-limit", type=float, default=600.0)
    parser.add_argument("--workers", type=int, default=64)
    parser.add_argument("--seed", type=int, default=20260814)
    args = parser.parse_args()
    if "-" in args.faces:
        lo, hi = map(int, args.faces.split("-"))
        faces = list(range(lo, hi + 1))
    else:
        faces = [int(value) for value in args.faces.split(",")]
    source_raw = Path(args.source).read_bytes()
    states, arcs = state_catalogue()
    reports = [
        solve_face(t, states, arcs, args.time_limit, args.workers, args.seed + t)
        for t in faces
    ]
    print(json.dumps({
        "status": (
            "PASS" if all(report["status"] in ("OPTIMAL", "FEASIBLE") for report in reports)
            else "INCOMPLETE"
        ),
        "scope": (
            "labelled five-core state cycles and aggregate frozen type counts only; "
            "no owner-column, lower-q2 representative, or rank-seven-pin coupling"
        ),
        "source_sha256": hashlib.sha256(source_raw).hexdigest(),
        "types": [
            {"type_id": i, "type": kind, "count": TYPE_COUNTS[i]}
            for i, kind in enumerate(TYPES)
        ],
        "states": [encode_state(i, state) for i, state in enumerate(states)],
        "transition_arcs": len(arcs),
        "reports": reports,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
