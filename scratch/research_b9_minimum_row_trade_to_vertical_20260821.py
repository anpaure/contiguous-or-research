#!/usr/bin/env python3
"""Certify the minimum canonical-row replacement for b=9 completeness.

The model maximizes the number of canonical MSW rows retained in an exact
middle wreath factor, subject to complete q1 coverage and, optionally,
complete q2 coverage.  Intended execution environment: H100 only.
"""

from __future__ import annotations

import argparse
from itertools import combinations, permutations

from ortools.sat.python import cp_model

from audit_b9_five_wreath_shadow_switch_20260821 import (
    canonical,
    dyck_words,
    msw_row,
)


def bit_windows(order, length):
    b = len(order)
    return tuple(
        sum(1 << (order[(i + j) % b] - 1) for j in range(length))
        for i in range(b)
    )


def main(seconds: float, workers: int, require_q2: bool):
    b, r = 9, 4
    targets = {
        k: tuple(sum(1 << x for x in target) for target in combinations(range(b), k))
        for k in (r, r - 1, r - 2)
    }
    target_id = {k: {target: i for i, target in enumerate(layer)} for k, layer in targets.items()}
    rows = []
    row_id = {}
    for tail in permutations(range(2, b + 1)):
        order = (1,) + tail
        if order[1] > order[-1]:
            continue
        row_id[canonical(order)] = len(rows)
        rows.append((
            order,
            tuple(target_id[r][x] for x in bit_windows(order, r)),
            tuple(target_id[r - 1][x] for x in bit_windows(order, r - 1)),
            tuple(target_id[r - 2][x] for x in bit_windows(order, r - 2)),
        ))
    assert len(rows) == len(row_id) == 20160
    canonical_ids = {row_id[msw_row(word)] for word in dyck_words(r)}
    assert len(canonical_ids) == 14

    supports = {k: [[] for _ in targets[k]] for k in targets}
    for index, row in enumerate(rows):
        for layer, k in enumerate((r, r - 1, r - 2), start=1):
            for target in row[layer]:
                supports[k][target].append(index)

    model = cp_model.CpModel()
    chosen = [model.new_bool_var(f"row_{i}") for i in range(len(rows))]
    for support in supports[r]:
        model.add(sum(chosen[i] for i in support) == 1)
    for support in supports[r - 1]:
        model.add(sum(chosen[i] for i in support) >= 1)
    if require_q2:
        for support in supports[r - 2]:
            model.add(sum(chosen[i] for i in support) >= 1)
    model.maximize(sum(chosen[i] for i in canonical_ids))

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = seconds
    solver.parameters.num_search_workers = workers
    status = solver.solve(model)
    feasible = status in (cp_model.FEASIBLE, cp_model.OPTIMAL)
    selected = {i for i, variable in enumerate(chosen) if feasible and solver.value(variable)}
    overlap = len(selected & canonical_ids)
    print({
        "status": solver.status_name(status),
        "require_q2": require_q2,
        "factor_rows": len(selected),
        "canonical_overlap": overlap,
        "row_replacements": 14 - overlap if feasible else None,
        "best_bound_overlap": solver.best_objective_bound,
        "wall": solver.wall_time,
    })
    if feasible:
        for index in sorted(selected - canonical_ids):
            print("ADDED", " ".join(map(str, rows[index][0])))
        print("B9_MINIMUM_ROW_TRADE_VERTICAL_SEARCH_PASS")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--seconds", type=float, default=600.0)
    parser.add_argument("--workers", type=int, default=64)
    parser.add_argument("--require-q2", action="store_true")
    arguments = parser.parse_args()
    main(arguments.seconds, arguments.workers, arguments.require_q2)
