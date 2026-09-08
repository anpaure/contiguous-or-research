#!/usr/bin/env python3
"""Small exact MILP: largest point-regular wreath-free rank family (H100)."""

import argparse
from itertools import permutations
from math import comb

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import coo_matrix, vstack


def masks_of_rank(b: int, r: int) -> list[int]:
    return [mask for mask in range(1 << b) if mask.bit_count() == r]


def wreaths(b: int, r: int, index: dict[int, int]) -> list[tuple[int, ...]]:
    out: set[tuple[int, ...]] = set()
    for tail in permutations(range(1, b)):
        order = (0,) + tail
        deck = []
        for i in range(b):
            mask = 0
            for j in range(r):
                mask |= 1 << order[(i + j) % b]
            deck.append(index[mask])
        out.add(tuple(sorted(deck)))
    return sorted(out)


def solve(b: int, r: int, time_limit: float) -> None:
    masks = masks_of_rank(b, r)
    index = {mask: i for i, mask in enumerate(masks)}
    edges = wreaths(b, r, index)
    rows: list[int] = []
    cols: list[int] = []
    data: list[float] = []
    lower: list[float] = []
    upper: list[float] = []
    row = 0
    for edge in edges:
        for vertex in edge:
            rows.append(row)
            cols.append(vertex)
            data.append(1.0)
        lower.append(-np.inf)
        upper.append(float(b - 1))
        row += 1
    # Point degree(x) - point degree(0) = 0.
    for point in range(1, b):
        for vertex, mask in enumerate(masks):
            coefficient = ((mask >> point) & 1) - (mask & 1)
            if coefficient:
                rows.append(row)
                cols.append(vertex)
                data.append(float(coefficient))
        lower.append(0.0)
        upper.append(0.0)
        row += 1
    matrix = coo_matrix((data, (rows, cols)), shape=(row, len(masks))).tocsr()
    result = milp(
        c=-np.ones(len(masks)),
        integrality=np.ones(len(masks)),
        bounds=Bounds(np.zeros(len(masks)), np.ones(len(masks))),
        constraints=LinearConstraint(matrix, np.array(lower), np.array(upper)),
        options={"time_limit": time_limit, "mip_rel_gap": 0.0},
    )
    print(
        "REGULAR_FREE",
        {"b": b, "r": r, "vertices": len(masks), "wreaths": len(edges)},
        {"success": result.success, "status": result.status, "message": result.message},
        {"maximum": None if result.fun is None else round(-result.fun), "density": None if result.fun is None else -result.fun / len(masks)},
    )
    if result.x is not None:
        chosen = [masks[i] for i, value in enumerate(result.x) if value > 0.5]
        degrees = [sum((mask >> point) & 1 for mask in chosen) for point in range(b)]
        print("DEGREES", degrees, "LEAVE", len(masks) - len(chosen))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("b", type=int)
    parser.add_argument("r", type=int)
    parser.add_argument("--time-limit", type=float, default=120.0)
    args = parser.parse_args()
    solve(args.b, args.r, args.time_limit)


if __name__ == "__main__":
    main()
