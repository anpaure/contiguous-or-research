#!/usr/bin/env python3
"""Small exact MILP audit for the full token-orbit color-cap reduction."""

from itertools import combinations
from math import comb

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import coo_array


def phase_count(b, r, q, z):
    if z == 0:
        return b - r - q + 1
    if z == q:
        return r - q + 1
    return 2


def solve(b, q):
    universe = range(2 * b)
    payloads = range(q, b - q + 1)
    sources = []
    for values in combinations(universe, b):
        source = frozenset(values)
        r = sum(value < b for value in source)
        if r in payloads:
            sources.append((source, r))

    targets = [frozenset(values) for values in combinations(universe, b + q)]
    target_index = {target: index for index, target in enumerate(targets)}
    colors = [(r, z) for r in payloads for z in range(q + 1)]
    color_index = {color: index for index, color in enumerate(colors)}

    row_indices = []
    column_indices = []
    entries = []
    edge_count = 0
    for source_index, (source, r) in enumerate(sources):
        complement = [value for value in universe if value not in source]
        for added in combinations(complement, q):
            z = sum(value < b for value in added)
            target = source | set(added)
            rows = (
                source_index,
                len(sources) + target_index[target],
                len(sources) + len(targets) + color_index[(r, z)],
            )
            for row in rows:
                row_indices.append(row)
                column_indices.append(edge_count)
                entries.append(1.0)
            edge_count += 1

    row_count = len(sources) + len(targets) + len(colors)
    matrix = coo_array(
        (entries, (row_indices, column_indices)),
        shape=(row_count, edge_count),
    ).tocsc()
    capacities = np.ones(row_count)
    for (r, z), index in color_index.items():
        capacities[len(sources) + len(targets) + index] = (
            phase_count(b, r, q, z) * comb(b, r) ** 2 // b
        )

    result = milp(
        -np.ones(edge_count),
        integrality=np.ones(edge_count),
        bounds=Bounds(0, 1),
        constraints=LinearConstraint(matrix, np.zeros(row_count), capacities),
        options={"mip_rel_gap": 0},
    )
    assert result.success
    optimum = round(-result.fun)

    scalar_bound = 0
    for s in range(q, b + 1):
        demand = comb(b, s) * comb(b, s - q)
        capacity = sum(
            phase_count(b, r, q, s - r) * comb(b, r) ** 2 // b
            for r in payloads
            if 0 <= s - r <= q
        )
        scalar_bound += min(demand, capacity)

    assert optimum == scalar_bound
    print(f"PASS b={b} q={q} optimum={optimum} scalar={scalar_bound}")


def main():
    for b, q in ((5, 1), (5, 2), (7, 1), (7, 2)):
        solve(b, q)
    print("ALL FULL-ORBIT COLOR-CAP CHECKS PASS")


if __name__ == "__main__":
    main()
