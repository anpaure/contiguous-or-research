#!/usr/bin/env python3
"""MILP probe for one constant-side length-2 chain per middle source."""

import argparse
from itertools import combinations

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import coo_array


def masks(n, k):
    out = []
    for xs in combinations(range(n), k):
        value = 0
        for x in xs:
            value |= 1 << x
        out.append(value)
    return out


def solve(b, time_limit):
    n = 2 * b
    middle = masks(n, b)
    q1 = masks(n, b + 1)
    q2 = masks(n, b + 2)
    q1_index = {x: i for i, x in enumerate(q1)}
    q2_index = {x: i for i, x in enumerate(q2)}

    options = []
    source_offsets = [0]
    for u in middle:
        missing_a = [x for x in range(b) if not (u >> x) & 1]
        missing_b = [x for x in range(b, n) if not (u >> x) & 1]
        for missing in (missing_a, missing_b):
            for first in missing:
                for second in missing:
                    if first != second:
                        options.append(
                            (q1_index[u | (1 << first)],
                             q2_index[u | (1 << first) | (1 << second)])
                        )
        source_offsets.append(len(options))

    nx = len(options)
    ny = len(q1)
    nvars = nx + ny
    source_base = 0
    q2_base = len(middle)
    q1_base = q2_base + len(q2)
    nrows = q1_base + len(q1)

    rows = []
    cols = []
    data = []
    for source in range(len(middle)):
        for j in range(source_offsets[source], source_offsets[source + 1]):
            one, two = options[j]
            rows.extend((source_base + source, q2_base + two, q1_base + one))
            cols.extend((j, j, j))
            data.extend((1.0, -1.0, -1.0))
    for one in range(ny):
        rows.append(q1_base + one)
        cols.append(nx + one)
        data.append(1.0)

    matrix = coo_array((data, (rows, cols)), shape=(nrows, nvars)).tocsr()
    lower = np.full(nrows, -np.inf)
    upper = np.zeros(nrows)
    lower[: len(middle)] = 1.0
    upper[: len(middle)] = 1.0
    upper[q2_base:q1_base] = -1.0

    objective = np.zeros(nvars)
    objective[nx:] = -1.0
    result = milp(
        objective,
        integrality=np.ones(nvars),
        bounds=Bounds(np.zeros(nvars), np.ones(nvars)),
        constraints=LinearConstraint(matrix, lower, upper),
        options={"time_limit": time_limit, "mip_rel_gap": 0.0},
    )
    covered_q1 = None if result.fun is None else round(-result.fun)
    print({
        "b": b,
        "sources": len(middle),
        "q1_targets": len(q1),
        "q2_targets": len(q2),
        "chain_variables": nx,
        "status": result.status,
        "message": result.message,
        "covered_q1": covered_q1,
        "miss_q1": None if covered_q1 is None else len(q1) - covered_q1,
        "mip_gap": getattr(result, "mip_gap", None),
        "mip_node_count": getattr(result, "mip_node_count", None),
    })


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--b", type=int, default=7)
    parser.add_argument("--time-limit", type=float, default=300.0)
    args = parser.parse_args()
    solve(args.b, args.time_limit)
