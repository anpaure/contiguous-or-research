#!/usr/bin/env python3
"""Rank/SNF diagnostics for q1 currents in canonical universal-C8 orbits."""

from __future__ import annotations

import argparse
from collections import Counter, deque
from itertools import combinations

from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form

from search_b9_c8_switch_path_20260821 import canonical, dyck_words, msw_row, switches


def windows(order, k):
    b = len(order)
    return tuple(
        frozenset(order[(i + j) % b] for j in range(k)) for i in range(b)
    )


def normal_current(old_pair, new_pair, target_id, k):
    old = Counter(x for row in old_pair for x in windows(row, k))
    new = Counter(x for row in new_pair for x in windows(row, k))
    delta = new.copy()
    delta.subtract(old)
    sparse = {target_id[x]: v for x, v in delta.items() if v}
    if not sparse:
        return ()
    first = min(sparse)
    if sparse[first] < 0:
        sparse = {i: -v for i, v in sparse.items()}
    return tuple(sorted(sparse.items()))


def mod_rank(vectors, n, p):
    basis = {}
    for sparse_tuple in vectors:
        row = {i: v % p for i, v in sparse_tuple if v % p}
        while row:
            pivot = min(row)
            if pivot not in basis:
                inv = pow(row[pivot], -1, p)
                row = {i: (v * inv) % p for i, v in row.items() if (v * inv) % p}
                basis[pivot] = row
                break
            coefficient = row[pivot]
            base = basis[pivot]
            for i, v in base.items():
                value = (row.get(i, 0) - coefficient * v) % p
                if value:
                    row[i] = value
                elif i in row:
                    del row[i]
    return len(basis)


def run(r, do_snf):
    b = 2 * r + 1
    k = r - 1
    targets = [frozenset(x) for x in combinations(range(1, b + 1), k)]
    target_id = {x: i for i, x in enumerate(targets)}
    start = tuple(sorted(msw_row(w) for w in dyck_words(r)))
    queue = deque([start])
    seen = {start}
    currents = set()
    directed_edges = 0
    while queue:
        state = queue.popleft()
        for i, j in combinations(range(len(state)), 2):
            old_pair = (state[i], state[j])
            for new_pair in switches(state[i], state[j], r):
                directed_edges += 1
                current = normal_current(old_pair, new_pair, target_id, k)
                if current:
                    currents.add(current)
                nxt = tuple(
                    sorted(
                        new_pair
                        + tuple(state[t] for t in range(len(state)) if t not in (i, j))
                    )
                )
                if nxt not in seen:
                    seen.add(nxt)
                    queue.append(nxt)
    expected_rank = len(targets) - b if k else 0
    ranks = {p: mod_rank(currents, len(targets), p) for p in (2, 3, 5, 7, 101, 1_000_003)}
    result = {
        "r": r,
        "b": b,
        "states": len(seen),
        "directed_edges": directed_edges,
        "distinct_unsigned_currents": len(currents),
        "targets": len(targets),
        "point_kernel_rank": expected_rank,
        "mod_ranks": ranks,
    }
    if currents and k >= 2:
        touched = {i for current in currents for i, _ in current}
        parent = {i: i for i in touched}

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            x, y = find(x), find(y)
            if x != y:
                parent[y] = x

        for current in currents:
            support_ids = [i for i, _ in current]
            for x in support_ids[1:]:
                union(support_ids[0], x)
        components = {}
        for i in touched:
            components.setdefault(find(i), set()).add(i)
        core_hist = Counter()
        pivot_hist = Counter()
        for current in currents:
            support = [targets[i] for i, _ in current]
            core = frozenset.intersection(*support)
            union = frozenset.union(*support)
            core_hist[tuple(sorted(core))] += 1
            pivot_hist[(tuple(sorted(core)), tuple(sorted(union - core)))] += 1
        result["core_hist"] = sorted(core_hist.items())
        result["distinct_core_pivot_blocks"] = len(pivot_hist)
        result["touched_targets"] = len(touched)
        result["untouched_target_coordinates"] = len(targets) - len(touched)
        start_load = Counter(x for row in start for x in windows(row, k))
        fixed_load_hist = Counter(start_load[targets[i]] for i in range(len(targets)) if i not in touched)
        fixed_gap = sum(
            (load - 1) * (load - 2) // 2 * count
            for load, count in fixed_load_hist.items()
        )
        result["untouched_load_hist"] = sorted(fixed_load_hist.items())
        result["untouched_energy_gap_contribution"] = fixed_gap
        component_profile = []
        for vertex_set in components.values():
            local_currents = [
                tuple((i, v) for i, v in current if i in vertex_set)
                for current in currents
                if any(i in vertex_set for i, _ in current)
            ]
            component_profile.append(
                (len(vertex_set), len(local_currents), mod_rank(local_currents, len(targets), 1_000_003))
            )
        result["current_support_components"] = sorted(component_profile)
    print(result, flush=True)
    if do_snf and currents:
        columns = list(currents)
        matrix = Matrix(
            len(targets),
            len(columns),
            lambda i, j: dict(columns[j]).get(i, 0),
        )
        diagonal = smith_normal_form(matrix, domain=ZZ)
        invariants = []
        for i in range(min(diagonal.rows, diagonal.cols)):
            value = abs(int(diagonal[i, i]))
            if value:
                invariants.append(value)
        print(
            {
                "r": r,
                "snf_nonzero": len(invariants),
                "snf_hist": sorted(Counter(invariants).items()),
                "lattice_index_if_full_rank": 0 if len(invariants) != expected_rank else __import__("math").prod(invariants),
            },
            flush=True,
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--r", type=int, nargs="+", default=[2, 3, 4])
    parser.add_argument("--snf", action="store_true")
    args = parser.parse_args()
    for r in args.r:
        run(r, args.snf)
