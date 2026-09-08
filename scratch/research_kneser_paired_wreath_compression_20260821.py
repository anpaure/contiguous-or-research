#!/usr/bin/env python3
"""Finite test of a Kneser-pair compression of the central wreath problem.

For b=2r+1, choose a maximum matching P in KG(b,r).  Retain a wreath when
all but one of its b cyclic r-windows form r edges of P.  Discarding the
one unpaired window costs only one source per selected wreath.  The retained
wreath is then an r-edge on the P-pair ground set.  We measure regularity,
codegrees, and greedy matching coverage of this compressed hypergraph.

Research diagnostic only.  Run on H100.
"""

from __future__ import annotations

from collections import Counter
from itertools import combinations, permutations
from math import comb
import argparse
import random

import networkx as nx

try:
    import numpy as np
    from scipy.optimize import Bounds, LinearConstraint, milp
    from scipy.sparse import csc_matrix
except ImportError:  # diagnostics can still run without exact MILP support
    np = None


def masks_of_rank(b: int, r: int) -> list[int]:
    return [sum(1 << x for x in s) for s in combinations(range(b), r)]


def random_kneser_matching(
    vertices: list[int], seed: int
) -> tuple[dict[int, int], int | None]:
    rng = random.Random(seed)
    graph = nx.Graph()
    graph.add_nodes_from(vertices)
    weighted = []
    for at, x in enumerate(vertices):
        for y in vertices[at + 1 :]:
            if not (x & y):
                weighted.append((x, y, rng.random()))
    graph.add_weighted_edges_from(weighted)
    matching = nx.algorithms.matching.max_weight_matching(
        graph, maxcardinality=True, weight="weight"
    )
    mate: dict[int, int] = {}
    for x, y in matching:
        mate[x] = y
        mate[y] = x
    unmatched = next((x for x in vertices if x not in mate), None)
    assert len(mate) // 2 == len(vertices) // 2
    return mate, unmatched


def wreath_windows(order: tuple[int, ...], r: int) -> tuple[int, ...]:
    b = len(order)
    doubled = order + order[: r - 1]
    return tuple(
        sum(1 << doubled[i + j] for j in range(r)) for i in range(b)
    )


def auxiliary_configuration_stats(b: int):
    """Degrees/codegrees before choosing the global Kneser matching P."""
    r = (b - 1) // 2
    targets = masks_of_rank(b, r)
    kneser_id = {}
    for at, x in enumerate(targets):
        for y in targets[at + 1 :]:
            if not (x & y):
                kneser_id[(min(x, y), max(x, y))] = len(kneser_id)
    degree = [0] * len(kneser_id)
    codegree = Counter()
    config_count = 0
    config_mult = Counter()
    for tail in permutations(range(1, b)):
        order = (0,) + tail
        if order[1] > order[-1]:
            continue
        windows = wreath_windows(order, r)
        cycle = tuple((t * r) % b for t in range(b))
        for dirty_at in range(b):
            # Delete one cycle vertex and pair consecutive remaining vertices.
            ids = []
            for j in range(1, b, 2):
                x = windows[cycle[(dirty_at + j) % b]]
                y = windows[cycle[(dirty_at + j + 1) % b]]
                key = (min(x, y), max(x, y))
                ids.append(kneser_id[key])
            edge = tuple(sorted(ids))
            config_count += 1
            config_mult[edge] += 1
            for x in edge:
                degree[x] += 1
            for x, y in combinations(edge, 2):
                codegree[(x, y)] += 1
    pair_sums = [
        sum(codegree[(x, y)] for x, y in combinations(edge, 2))
        for edge in config_mult
    ]
    print(
        "AUXILIARY",
        b,
        "TARGETS",
        len(targets),
        "KNESER_VERTICES",
        len(kneser_id),
        "CONFIGS",
        config_count,
        "SIMPLE_CONFIGS",
        len(config_mult),
        "MAX_MULT",
        max(config_mult.values(), default=0),
        "DEG_MIN_MAX",
        (min(degree, default=0), max(degree, default=0)),
        "CODEG_MAX",
        max(codegree.values(), default=0),
        "EDGE_PAIR_CODEG_SUM_MEAN_MAX",
        (
            round(sum(pair_sums) / len(pair_sums), 6) if pair_sums else 0.0,
            max(pair_sums, default=0),
        ),
        flush=True,
    )


def retained_edges(b: int, mate: dict[int, int]):
    r = (b - 1) // 2
    pair_id: dict[tuple[int, int], int] = {}
    for x, y in mate.items():
        key = (min(x, y), max(x, y))
        if key not in pair_id:
            pair_id[key] = len(pair_id)

    edges: list[tuple[int, ...]] = []
    dirty = Counter()
    all_wreaths = 0
    # Fix 0 in the first position and quotient reversal by order[1]<order[-1].
    for tail in permutations(range(1, b)):
        order = (0,) + tail
        if order[1] > order[-1]:
            continue
        all_wreaths += 1
        windows = wreath_windows(order, r)
        window_set = set(windows)
        internal = []
        paired_targets = set()
        for x in windows:
            y = mate.get(x)
            if y is not None and y in window_set and x < y:
                internal.append(pair_id[(x, y)])
                paired_targets.add(x)
                paired_targets.add(y)
        if len(internal) != r:
            continue
        singleton = next(x for x in windows if x not in paired_targets)
        dirty[singleton] += 1
        edges.append(tuple(sorted(internal)))
    # Different cyclic orders can in principle induce the same compressed edge.
    multiplicities = Counter(edges)
    simple_edges = list(multiplicities)
    return all_wreaths, simple_edges, multiplicities, dirty, len(pair_id)


def greedy_matching(
    edges: list[tuple[int, ...]], vertex_count: int, seed: int, trials: int
):
    rng = random.Random(seed)
    best: list[tuple[int, ...]] = []
    indices = list(range(len(edges)))
    for _ in range(trials):
        rng.shuffle(indices)
        used = 0
        chosen = []
        for idx in indices:
            edge = edges[idx]
            mask = sum(1 << x for x in edge)
            if not (used & mask):
                used |= mask
                chosen.append(edge)
        if len(chosen) > len(best):
            best = chosen
    covered = len(set().union(*(set(e) for e in best))) if best else 0
    return len(best), covered, vertex_count - covered


def exact_matching(edges: list[tuple[int, ...]], vertex_count: int, time_limit: float):
    if np is None or not edges:
        return None
    rows = []
    cols = []
    for j, edge in enumerate(edges):
        for x in edge:
            rows.append(x)
            cols.append(j)
    data = np.ones(len(rows), dtype=float)
    incidence = csc_matrix((data, (rows, cols)), shape=(vertex_count, len(edges)))
    result = milp(
        c=-np.ones(len(edges)),
        integrality=np.ones(len(edges)),
        bounds=Bounds(np.zeros(len(edges)), np.ones(len(edges))),
        constraints=LinearConstraint(
            incidence, np.zeros(vertex_count), np.ones(vertex_count)
        ),
        options={"time_limit": time_limit, "mip_rel_gap": 0.0},
    )
    if result.x is None:
        return {"status": result.status, "value": None, "gap": None}
    value = int(round(-result.fun))
    return {
        "status": result.status,
        "value": value,
        "gap": getattr(result, "mip_gap", None),
    }


def one_case(b: int, seed: int, trials: int, exact_seconds: float):
    r = (b - 1) // 2
    vertices = masks_of_rank(b, r)
    mate, unmatched = random_kneser_matching(vertices, seed)
    all_wreaths, edges, mult, dirty, pair_count = retained_edges(b, mate)
    degree = [0] * pair_count
    codegree = Counter()
    for edge in edges:
        for x in edge:
            degree[x] += 1
        for x, y in combinations(edge, 2):
            codegree[(x, y)] += 1
    overlap_sums = [
        sum(codegree[(x, y)] for x, y in combinations(edge, 2))
        for edge in edges
    ]
    mean_degree = (sum(degree) / pair_count) if pair_count else 0.0
    match_edges, covered, leave = greedy_matching(
        edges, pair_count, seed + 9173, trials
    )
    exact = exact_matching(edges, pair_count, exact_seconds) if exact_seconds else None
    print(
        "CASE",
        b,
        "SEED",
        seed,
        "TARGETS",
        len(vertices),
        "PAIRS",
        pair_count,
        "UNMATCHED_TARGET",
        unmatched,
        "ALL_WREATHS",
        all_wreaths,
        "RETAINED_SIMPLE",
        len(edges),
        "RETAINED_WITH_MULT",
        sum(mult.values()),
        "MAX_MULT",
        max(mult.values(), default=0),
        "DEG_MIN_MAX",
        (min(degree, default=0), max(degree, default=0)),
        "DEG_MEAN",
        round(mean_degree, 6),
        "CODEG_MAX",
        max(codegree.values(), default=0),
        "EDGE_PAIR_CODEG_SUM_MEAN_MAX",
        (
            round(sum(overlap_sums) / len(overlap_sums), 6)
            if overlap_sums
            else 0.0,
            max(overlap_sums, default=0),
        ),
        "GREEDY_EDGES",
        match_edges,
        "EXACT",
        exact,
        "PAIR_COVER",
        covered,
        "PAIR_LEAVE",
        leave,
        "ORIGINAL_CLEAN_COVER",
        2 * covered,
        "ORIGINAL_TOTAL",
        comb(b, r),
        "DIRTY_SUPPORT",
        len(dirty),
        flush=True,
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--b", type=int, default=9)
    parser.add_argument("--seeds", type=int, default=10)
    parser.add_argument("--trials", type=int, default=200)
    parser.add_argument("--exact-seconds", type=float, default=0.0)
    parser.add_argument("--auxiliary", action="store_true")
    args = parser.parse_args()
    assert args.b % 2 == 1
    if args.auxiliary:
        auxiliary_configuration_stats(args.b)
        return
    for seed in range(args.seeds):
        one_case(args.b, seed, args.trials, args.exact_seconds)


if __name__ == "__main__":
    main()
