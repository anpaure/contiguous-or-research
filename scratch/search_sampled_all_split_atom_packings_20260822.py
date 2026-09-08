#!/usr/bin/env python3
"""Sampled set-packing diagnostics for the all-split atom hypergraph.

Evidence only.  For b=5 the full atom family is enumerable elsewhere.  This
script samples labelled atoms for b>=7, deduplicates their vertex masks, and
solves the resulting restricted set-packing MILP.  Any solution is a valid
packing in the full hypergraph; failure or an upper bound for the sampled
instance says nothing about the full problem.
"""

from __future__ import annotations

from argparse import ArgumentParser
from itertools import combinations
from math import comb
from random import Random


def cyclic_intervals(cycle: list[int], length: int) -> list[frozenset[int]]:
    b = len(cycle)
    return [
        frozenset(cycle[(i + j) % b] for j in range(length))
        for i in range(b)
    ]


def sampled_atoms(b: int, count: int, seed: int) -> tuple[list[tuple[int, ...]], list[int]]:
    rng = Random(seed)
    omega = tuple(range(2 * b))
    vertices = list(combinations(omega, b))
    vid = {s: i for i, s in enumerate(vertices)}
    h = (b - 1) // 2

    def make_atom(a_list: list[int], b_list: list[int]) -> int:
        aa = cyclic_intervals(a_list, h)
        bb = cyclic_intervals(b_list, h + 1)
        mask = 0
        for x in aa:
            for y in bb:
                mask |= 1 << vid[tuple(sorted(x | y))]
        assert mask.bit_count() == b * b
        return mask

    # Include one canonical atom, allowing transitivity-based comparisons.
    left = list(range(b))
    right = list(range(b, 2 * b))
    masks = {make_atom(left, right)}
    while len(masks) < count:
        shuffled = list(omega)
        rng.shuffle(shuffled)
        left = shuffled[:b]
        right = shuffled[b:]
        rng.shuffle(left)
        rng.shuffle(right)
        masks.add(make_atom(left, right))
    return vertices, list(masks)


def solve(vertices: list[tuple[int, ...]], atoms: list[int], seconds: float) -> list[int]:
    import numpy as np
    from scipy.optimize import Bounds, LinearConstraint, milp
    from scipy.sparse import csc_matrix

    rows: list[int] = []
    cols: list[int] = []
    for j, edge in enumerate(atoms):
        bits = edge
        while bits:
            low = bits & -bits
            rows.append(low.bit_length() - 1)
            cols.append(j)
            bits ^= low
    matrix = csc_matrix(
        (np.ones(len(rows), dtype=np.uint8), (rows, cols)),
        shape=(len(vertices), len(atoms)),
    )
    result = milp(
        c=-np.ones(len(atoms)),
        integrality=np.ones(len(atoms)),
        bounds=Bounds(np.zeros(len(atoms)), np.ones(len(atoms))),
        constraints=LinearConstraint(matrix, -np.inf, 1.0),
        options={"time_limit": seconds, "mip_rel_gap": 0.0},
    )
    print(
        "status", result.status,
        "success", result.success,
        "objective", None if result.fun is None else -result.fun,
        "bound", getattr(result, "mip_dual_bound", None),
        "gap", getattr(result, "mip_gap", None),
    )
    if result.x is None:
        return []
    return [atoms[i] for i, value in enumerate(result.x) if value > 0.5]


def main() -> None:
    parser = ArgumentParser()
    parser.add_argument("--b", type=int, default=7)
    parser.add_argument("--samples", type=int, default=50_000)
    parser.add_argument("--seconds", type=float, default=120.0)
    parser.add_argument("--seed", type=int, default=20260822)
    args = parser.parse_args()
    assert args.b >= 5 and args.b % 2 == 1
    vertices, atoms = sampled_atoms(args.b, args.samples, args.seed)
    print(
        "b", args.b,
        "vertices", len(vertices),
        "edge_size", args.b * args.b,
        "sampled_distinct_atoms", len(atoms),
        "fractional_target", len(vertices) / (args.b * args.b),
    )
    packing = solve(vertices, atoms, args.seconds)
    used = 0
    for edge in packing:
        assert used & edge == 0
        used |= edge
    print(
        "SAMPLED_ALL_SPLIT_PACKING",
        "edges", len(packing),
        "covered", used.bit_count(),
        "holes", len(vertices) - used.bit_count(),
        "density", used.bit_count() / len(vertices),
    )


if __name__ == "__main__":
    main()
