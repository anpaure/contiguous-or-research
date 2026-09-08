#!/usr/bin/env python3
"""Exact finite min-cost deletion d-factors in split GK orientation graphs."""

from __future__ import annotations

import argparse
import itertools
import math

from ortools.graph.python import min_cost_flow


def top_excess(x: frozenset[int], y: frozenset[int], b: int) -> int:
    stack = 0
    unmatched = 0
    for i in range(b):
        for bit in (i in x, i in y):
            if bit:
                stack += 1
            elif stack:
                stack -= 1
            else:
                unmatched += 1
    assert stack == unmatched
    return unmatched


def solve_orientation(
    kval: list[list[int]], parity: int, deletion_degree: int, h: int
) -> int:
    n = len(kval)
    if deletion_degree == 0:
        return 0
    source = 2 * n
    sink = source + 1
    flow = min_cost_flow.SimpleMinCostFlow()
    for i in range(n):
        flow.add_arc_with_capacity_and_unit_cost(source, i, deletion_degree, 0)
        flow.add_arc_with_capacity_and_unit_cost(n + i, sink, deletion_degree, 0)
    for i, row in enumerate(kval):
        for j, k in enumerate(row):
            if (k & 1) == parity:
                flow.add_arc_with_capacity_and_unit_cost(i, n + j, 1, min(k, h))
    flow.set_node_supply(source, n * deletion_degree)
    flow.set_node_supply(sink, -n * deletion_degree)
    status = flow.solve()
    assert status == flow.OPTIMAL, status
    return flow.optimal_cost()


def audit(b: int, r: int, h: int) -> dict[str, int | float]:
    ground = range(b)
    xs = [frozenset(c) for c in itertools.combinations(ground, r)]
    ys = [frozenset(c) for c in itertools.combinations(ground, b - r)]
    nvert = len(xs)
    kval = [[top_excess(x, y, b) for y in ys] for x in xs]
    dsplit = abs(2 * r - b)
    nphase = max(0, (b - dsplit - h + 2) // 2)
    selected_degree = nphase * nvert // b
    assert selected_degree * b == nphase * nvert

    full = sum(min(k, h) for row in kval for k in row)
    ideal_deleted = 0
    factor_deleted = 0
    details = []
    for parity, label in ((1, "A"), (0, "B")):
        degree = math.comb(b - 1, r if parity else r - 1) if 0 <= (r if parity else r - 1) < b else 0
        deletion_degree = degree - selected_degree
        vals = sorted(
            min(k, h) for row in kval for k in row if (k & 1) == parity
        )
        ideal = sum(vals[: deletion_degree * nvert])
        optimum = solve_orientation(kval, parity, deletion_degree, h)
        assert optimum >= ideal
        ideal_deleted += ideal
        factor_deleted += optimum
        details.append((label, degree, deletion_degree, ideal, optimum))
    lsplit = nvert * nvert
    return {
        "b": b,
        "r": r,
        "h": h,
        "N": nvert,
        "nphase": nphase,
        "full": full,
        "ideal_deleted": ideal_deleted,
        "factor_deleted": factor_deleted,
        "extra": factor_deleted - ideal_deleted,
        "factor_over_Lr": factor_deleted / lsplit,
        "extra_over_Lr": (factor_deleted - ideal_deleted) / lsplit,
        "details": details,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--b", type=int, nargs="+", default=[5, 7, 11])
    parser.add_argument("--h", type=int, default=0)
    args = parser.parse_args()
    for b in args.b:
        h = args.h or max(1, math.isqrt(b))
        print(audit(b, (b - 1) // 2, h), flush=True)


if __name__ == "__main__":
    main()
