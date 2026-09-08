#!/usr/bin/env python3
"""CP-SAT search for a maximum Kneser matching with few retained wreaths."""

from __future__ import annotations

import argparse
from itertools import combinations, permutations

from ortools.sat.python import cp_model


def masks(b: int, r: int) -> list[int]:
    return [sum(1 << q for q in c) for c in combinations(range(b), r)]


def windows(order: tuple[int, ...], r: int) -> tuple[int, ...]:
    b = len(order)
    return tuple(
        sum(1 << order[(i + j) % b] for j in range(r)) for i in range(b)
    )


def build(b: int):
    r = (b - 1) // 2
    targets = masks(b, r)
    kg_edges = [
        tuple(sorted((x, y)))
        for at, x in enumerate(targets)
        for y in targets[at + 1 :]
        if not (x & y)
    ]
    edge_id = {e: i for i, e in enumerate(kg_edges)}
    configs = set()
    for tail in permutations(range(1, b)):
        order = (0,) + tail
        if order[1] > order[-1]:
            continue
        ww = windows(order, r)
        for dirty in range(b):
            config = []
            for k in range(1, r + 1):
                i = (dirty + k) % b
                e = tuple(sorted((ww[i], ww[(i + r) % b])))
                config.append(edge_id[e])
            configs.add(tuple(sorted(config)))
    return targets, kg_edges, sorted(configs)


def solve(b: int, seconds: float, workers: int, forbid_all: bool) -> None:
    r = (b - 1) // 2
    targets, kg_edges, configs = build(b)
    model = cp_model.CpModel()
    chosen = [model.new_bool_var(f"p_{i}") for i in range(len(kg_edges))]
    incident = {x: [] for x in targets}
    for i, (x, y) in enumerate(kg_edges):
        incident[x].append(chosen[i])
        incident[y].append(chosen[i])
    for x in targets:
        model.add(sum(incident[x]) <= 1)
    model.add(sum(chosen) == len(targets) // 2)

    retained = []
    for j, config in enumerate(configs):
        if forbid_all:
            model.add(sum(chosen[i] for i in config) <= r - 1)
        else:
            z = model.new_bool_var(f"z_{j}")
            model.add(z <= chosen[config[0]])
            model.add(sum(chosen[i] for i in config) - (r - 1) <= z)
            retained.append(z)
    if not forbid_all:
        model.minimize(sum(retained))

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = seconds
    solver.parameters.num_search_workers = workers
    status = solver.solve(model)
    selected = [kg_edges[i] for i, z in enumerate(chosen) if solver.value(z)] if status in (cp_model.OPTIMAL, cp_model.FEASIBLE) else []
    print(
        {
            "b": b,
            "targets": len(targets),
            "kg_edges": len(kg_edges),
            "configs": len(configs),
            "forbid_all": forbid_all,
            "status": solver.status_name(status),
            "objective": solver.objective_value if not forbid_all and selected else None,
            "selected": selected,
            "wall": solver.wall_time,
        },
        flush=True,
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--b", type=int, default=7)
    parser.add_argument("--seconds", type=float, default=300)
    parser.add_argument("--workers", type=int, default=64)
    parser.add_argument("--forbid-all", action="store_true")
    args = parser.parse_args()
    solve(args.b, args.seconds, args.workers, args.forbid_all)
