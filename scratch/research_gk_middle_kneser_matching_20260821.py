#!/usr/bin/env python3
"""Explore the middle GK inclusion permutation and its Kneser matching."""

from __future__ import annotations

import argparse
from collections import Counter
from itertools import combinations, permutations
import random

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import csc_matrix
from ortools.sat.python import cp_model


def rank_masks(b: int, r: int) -> list[int]:
    return [sum(1 << q for q in c) for c in combinations(range(b), r)]


def successor_10(x: int, b: int) -> int:
    """BTK successor: recursively pair 1...0 and flip first unpaired 0."""
    stack = []
    paired = set()
    for q in range(b):
        if (x >> q) & 1:
            stack.append(q)
        elif stack:
            p = stack.pop()
            paired.add(p)
            paired.add(q)
    free_zero = [q for q in range(b) if not (x >> q) & 1 and q not in paired]
    assert free_zero
    return x | (1 << free_zero[-1])


def successor_01(x: int, b: int) -> int:
    """Reflected BTK successor: pair 0...1 and flip last unpaired 0."""
    stack = []
    paired = set()
    for q in range(b):
        if not ((x >> q) & 1):
            stack.append(q)
        elif stack:
            p = stack.pop()
            paired.add(p)
            paired.add(q)
    free_zero = [q for q in range(b) if not (x >> q) & 1 and q not in paired]
    assert free_zero
    return x | (1 << free_zero[0])


def cycles_of(mapping: dict[int, int]) -> list[list[int]]:
    unseen = set(mapping)
    cycles = []
    while unseen:
        start = next(iter(unseen))
        cycle = []
        x = start
        while x not in cycle:
            cycle.append(x)
            unseen.discard(x)
            x = mapping[x]
        assert x == start
        cycles.append(cycle)
    return cycles


def matching_from_cycles(cycles: list[list[int]]) -> tuple[dict[int, int], list[int]]:
    mate = {}
    unmatched = []
    for cycle in cycles:
        stop = len(cycle) - (len(cycle) & 1)
        for i in range(0, stop, 2):
            x, y = cycle[i], cycle[i + 1]
            mate[x] = y
            mate[y] = x
        if stop != len(cycle):
            unmatched.append(cycle[-1])
    return mate, unmatched


def wreath_windows(order: tuple[int, ...], r: int) -> tuple[int, ...]:
    b = len(order)
    return tuple(
        sum(1 << order[(i + j) % b] for j in range(r)) for i in range(b)
    )


def canonical_order_scores(b: int, mate: dict[int, int]) -> Counter:
    r = (b - 1) // 2
    full = (1 << b) - 1
    scores = Counter()
    for x, y in mate.items():
        if x > y:
            continue
        hole_mask = full ^ x ^ y
        assert hole_mask.bit_count() == 1
        hole = hole_mask.bit_length() - 1
        xx = [q for q in range(b) if x >> q & 1]
        yy = [q for q in range(b) if y >> q & 1]
        best = 0
        for ax in (xx, list(reversed(xx))):
            for ay in (yy, list(reversed(yy))):
                for order in (tuple(ax + [hole] + ay), tuple(ay + [hole] + ax)):
                    ww = wreath_windows(order, r)
                    count = 0
                    used = set()
                    for u in ww:
                        v = mate.get(u)
                        if v in ww and u < v:
                            count += 1
                            used.update((u, v))
                    if len(used) == 2 * count:
                        best = max(best, count)
        scores[best] += 1
    return scores


def retained(b: int, mate: dict[int, int], exact_seconds: float):
    r = (b - 1) // 2
    pair_id = {}
    for x, y in mate.items():
        e = tuple(sorted((x, y)))
        if e not in pair_id:
            pair_id[e] = len(pair_id)
    edges = set()
    if b > 11:
        return None
    for tail in permutations(range(1, b)):
        order = (0,) + tail
        if order[1] > order[-1]:
            continue
        ww = wreath_windows(order, r)
        have = []
        used = set()
        for x in ww:
            y = mate.get(x)
            if y in ww and x < y:
                have.append(pair_id[tuple(sorted((x, y)))])
                used.update((x, y))
        if len(have) == r and len(used) == 2 * r:
            edges.add(tuple(sorted(have)))
    degree = Counter(x for edge in edges for x in edge)
    edge_list = sorted(edges)
    codegree = Counter(
        pair for edge in edge_list for pair in combinations(edge, 2)
    )
    overlap = [
        sum(codegree[pair] for pair in combinations(edge, 2))
        for edge in edge_list
    ]
    best = []
    indices = list(range(len(edge_list)))
    rng = random.Random(1701 + b)
    for _ in range(500):
        rng.shuffle(indices)
        used = set()
        chosen = []
        for j in indices:
            edge = edge_list[j]
            if used.isdisjoint(edge):
                used.update(edge)
                chosen.append(j)
        if len(chosen) > len(best):
            best = chosen
    exact = None
    if exact_seconds < 0:
        rows = []
        cols = []
        for j, edge in enumerate(edge_list):
            for x in edge:
                rows.append(x)
                cols.append(j)
        incidence = csc_matrix(
            (np.ones(len(rows)), (rows, cols)),
            shape=(len(pair_id), len(edge_list)),
        )
        result = milp(
            c=-np.ones(len(edge_list)),
            integrality=np.ones(len(edge_list)),
            bounds=Bounds(np.zeros(len(edge_list)), np.ones(len(edge_list))),
            constraints=LinearConstraint(
                incidence, np.zeros(len(pair_id)), np.ones(len(pair_id))
            ),
            options={"time_limit": -exact_seconds, "mip_rel_gap": 0.0},
        )
        exact = (
            result.status,
            int(round(-result.fun)) if result.fun is not None else None,
            getattr(result, "mip_gap", None),
        )
    exact_cover = None
    if exact_seconds > 0 and len(pair_id) % r == 0:
        model = cp_model.CpModel()
        take = [model.new_bool_var(f"take_{j}") for j in range(len(edge_list))]
        incident = [[] for _ in range(len(pair_id))]
        for j, edge in enumerate(edge_list):
            for x in edge:
                incident[x].append(take[j])
        for row in incident:
            model.add(sum(row) == 1)
        solver = cp_model.CpSolver()
        solver.parameters.max_time_in_seconds = exact_seconds
        solver.parameters.num_search_workers = 64
        status = solver.solve(model)
        exact_cover = (solver.status_name(status), solver.wall_time)
    return (
        len(edges),
        (min(degree.values()), max(degree.values())),
        sum(degree.values()) / len(pair_id),
        (max(codegree.values()), sum(overlap) / len(overlap), max(overlap)),
        (len(best), len(pair_id) - r * len(best)),
        exact,
        exact_cover,
    )


def one(b: int, convention: str, exact_seconds: float) -> None:
    r = (b - 1) // 2
    vv = rank_masks(b, r)
    successor = successor_10 if convention == "10" else successor_01
    full = (1 << b) - 1
    mapping = {x: full ^ successor(x, b) for x in vv}
    assert set(mapping.values()) == set(vv)
    assert all(not (x & y) for x, y in mapping.items())
    cycles = cycles_of(mapping)
    mate, unmatched = matching_from_cycles(cycles)
    print(
        {
            "b": b,
            "convention": convention,
            "targets": len(vv),
            "cycle_hist": dict(sorted(Counter(map(len, cycles)).items())),
            "cycles": len(cycles),
            "matched_pairs": len(mate) // 2,
            "unmatched": len(unmatched),
            "canonical_score_hist": dict(sorted(canonical_order_scores(b, mate).items())),
            "retained": retained(b, mate, exact_seconds),
        },
        flush=True,
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--b", type=int, nargs="+", default=[5, 7, 9, 11])
    parser.add_argument("--exact-seconds", type=float, default=0.0)
    parser.add_argument("--convention", nargs="+", choices=("10", "01"), default=("10", "01"))
    args = parser.parse_args()
    for bb in args.b:
        for cc in args.convention:
            one(bb, cc, args.exact_seconds)
