#!/usr/bin/env python3
"""Jointly design an exact b=9 middle wreath factor and clean q=1 ribbons.

Intended execution environment: H100 only.  A selected row chooses one of
its nine lower windows as dirty.  The remaining eight lower windows and the
same-start middle windows must be target-disjoint.  Exact middle-factor
constraints make the latter automatic, including the deleted middle starts.
"""

from __future__ import annotations

import argparse
from collections import Counter
from itertools import combinations, permutations

from ortools.sat.python import cp_model


def canonical(order):
    order = tuple(order)
    rotations = [order[i:] + order[:i] for i in range(len(order))]
    reverse = tuple(reversed(order))
    rotations.extend(reverse[i:] + reverse[:i] for i in range(len(order)))
    return min(rotations)


def windows(order, k):
    b = len(order)
    return tuple(
        sum(1 << order[(i + j) % b] for j in range(k)) for i in range(b)
    )


def main(seconds, workers, requested):
    b, r = 9, 4
    rank_r = [sum(1 << q for q in c) for c in combinations(range(b), r)]
    rank_low = [sum(1 << q for q in c) for c in combinations(range(b), r - 1)]
    id_r = {target: i for i, target in enumerate(rank_r)}
    id_low = {target: i for i, target in enumerate(rank_low)}

    rows = []
    for tail in permutations(range(1, b)):
        order = (0,) + tail
        if order[1] > order[-1]:
            continue
        middle = tuple(id_r[x] for x in windows(order, r))
        lower = tuple(id_low[x] for x in windows(order, r - 1))
        assert len(set(middle)) == len(set(lower)) == b
        rows.append((order, middle, lower))
    assert len(rows) == 20160

    by_middle = [[] for _ in rank_r]
    by_lower = [[] for _ in rank_low]
    lower_position = {}
    for row_id, (_, middle, lower) in enumerate(rows):
        for target in middle:
            by_middle[target].append(row_id)
        for position, target in enumerate(lower):
            by_lower[target].append(row_id)
            lower_position[(row_id, target)] = position

    model = cp_model.CpModel()
    in_factor = [model.new_bool_var(f"factor_{i}") for i in range(len(rows))]
    selected = [model.new_bool_var(f"selected_{i}") for i in range(len(rows))]
    dirty = [
        [model.new_bool_var(f"dirty_{i}_{j}") for j in range(b)]
        for i in range(len(rows))
    ]
    for i in range(len(rows)):
        model.add(sum(dirty[i]) == selected[i])
        model.add(selected[i] <= in_factor[i])
    for support in by_middle:
        model.add(sum(in_factor[i] for i in support) == 1)
    for target, support in enumerate(by_lower):
        model.add(
            sum(selected[i] for i in support)
            - sum(dirty[i][lower_position[(i, target)]] for i in support)
            <= 1
        )
    upper_bound = len(rank_low) // (b - 1)
    assert upper_bound == 10
    if requested is not None:
        model.add(sum(selected) == requested)
    model.maximize(sum(selected))

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = seconds
    solver.parameters.num_search_workers = workers
    solver.parameters.log_search_progress = False
    status = solver.solve(model)
    feasible = status in (cp_model.FEASIBLE, cp_model.OPTIMAL)
    factor = [i for i, var in enumerate(in_factor) if feasible and solver.value(var)]
    packing = [i for i, var in enumerate(selected) if feasible and solver.value(var)]
    print(
        {
            "status": solver.status_name(status),
            "objective": int(round(solver.objective_value)) if feasible else None,
            "best_bound": solver.best_objective_bound,
            "factor_rows": len(factor),
            "selected_rows": len(packing),
            "wall": solver.wall_time,
        },
        flush=True,
    )
    if not feasible:
        return

    assert len(factor) == len(rank_r) // b == 14
    middle_count = Counter(t for i in factor for t in rows[i][1])
    assert middle_count == Counter({i: 1 for i in range(len(rank_r))})
    clean_lower = []
    clean_middle = []
    for i in packing:
        dirty_position = next(j for j in range(b) if solver.value(dirty[i][j]))
        clean_lower.extend(t for j, t in enumerate(rows[i][2]) if j != dirty_position)
        clean_middle.extend(t for j, t in enumerate(rows[i][1]) if j != dirty_position)
        print(
            "SELECT",
            " ".join(str(q + 1) for q in rows[i][0]),
            "DIRTY_START",
            dirty_position,
            "DIRTY_LOWER",
            sorted(q + 1 for q in range(b) if (rank_low[rows[i][2][dirty_position]] >> q) & 1),
        )
    assert len(clean_lower) == len(set(clean_lower)) == (b - 1) * len(packing)
    assert len(clean_middle) == len(set(clean_middle)) == (b - 1) * len(packing)
    for i in factor:
        if i not in packing:
            print("FILLER", " ".join(str(q + 1) for q in rows[i][0]))
    print("JOINT_FACTOR_PUNCTURED_WREATH_PACKING_PASS", flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--seconds", type=float, default=600.0)
    parser.add_argument("--workers", type=int, default=64)
    parser.add_argument("--requested", type=int)
    args = parser.parse_args()
    main(args.seconds, args.workers, args.requested)
