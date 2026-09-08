#!/usr/bin/env python3
"""Search for an exact b=9 wreath factor with complete q1 but a q2 hole.

The forced q2 hole is {0,1}; label transitivity makes this equivalent to
the existence of any q2 hole.  Intended execution environment: H100 only.
"""

from __future__ import annotations

import argparse
from itertools import combinations, permutations

from ortools.sat.python import cp_model


def windows(order, length):
    b = len(order)
    return tuple(
        sum(1 << order[(i + j) % b] for j in range(length))
        for i in range(b)
    )


def main(seconds: float, workers: int, maximize_holes: bool):
    b, r = 9, 4
    layers = {
        k: tuple(sum(1 << x for x in target) for target in combinations(range(b), k))
        for k in (r, r - 1, r - 2)
    }
    indices = {k: {target: i for i, target in enumerate(layer)} for k, layer in layers.items()}

    rows = []
    for tail in permutations(range(1, b)):
        order = (0,) + tail
        if order[1] > order[-1]:
            continue
        rows.append((
            order,
            tuple(indices[r][x] for x in windows(order, r)),
            tuple(indices[r - 1][x] for x in windows(order, r - 1)),
            tuple(indices[r - 2][x] for x in windows(order, r - 2)),
        ))
    assert len(rows) == 20160

    by_middle = [[] for _ in layers[r]]
    by_q1 = [[] for _ in layers[r - 1]]
    for row_id, (_, middle, q1, _) in enumerate(rows):
        for target in middle:
            by_middle[target].append(row_id)
        for target in q1:
            by_q1[target].append(row_id)

    by_q2 = [[] for _ in layers[r - 2]]
    for row_id, row in enumerate(rows):
        for target in row[3]:
            by_q2[target].append(row_id)
    forbidden = indices[r - 2][(1 << 0) | (1 << 1)]
    forbidden_rows = by_q2[forbidden]

    model = cp_model.CpModel()
    chosen = [model.new_bool_var(f"row_{i}") for i in range(len(rows))]
    for support in by_middle:
        model.add(sum(chosen[i] for i in support) == 1)
    for support in by_q1:
        model.add(sum(chosen[i] for i in support) >= 1)
    q2_used = []
    if maximize_holes:
        for target, support in enumerate(by_q2):
            used = model.new_bool_var(f"q2_used_{target}")
            q2_used.append(used)
            for row_id in support:
                model.add(used >= chosen[row_id])
            model.add(used <= sum(chosen[row_id] for row_id in support))
        model.minimize(sum(q2_used))
    else:
        for row_id in forbidden_rows:
            model.add(chosen[row_id] == 0)

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = seconds
    solver.parameters.num_search_workers = workers
    status = solver.solve(model)
    feasible = status in (cp_model.FEASIBLE, cp_model.OPTIMAL)
    selected = [i for i, variable in enumerate(chosen) if feasible and solver.value(variable)]
    print({
        "status": solver.status_name(status),
        "rows": len(selected),
        "wall": solver.wall_time,
        "q2_forbidden_rows": len(forbidden_rows),
        "q2_holes": 36 - sum(solver.value(x) for x in q2_used) if feasible and q2_used else None,
        "best_bound_holes": 36 - solver.best_objective_bound if q2_used else None,
    })
    if feasible:
        assert len(selected) == 14
        for row_id in selected:
            print("ROW", " ".join(str(x + 1) for x in rows[row_id][0]))
        print("B9_Q1_COMPLETE_Q2_HOLE_FACTOR_FOUND")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--seconds", type=float, default=600.0)
    parser.add_argument("--workers", type=int, default=64)
    parser.add_argument("--maximize-q2-holes", action="store_true")
    arguments = parser.parse_args()
    main(arguments.seconds, arguments.workers, arguments.maximize_q2_holes)
