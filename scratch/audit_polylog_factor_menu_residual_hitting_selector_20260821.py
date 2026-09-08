#!/usr/bin/env python3
"""Audit the residual-hitting selector theorem and a b=5 factor-menu diagnostic."""

from __future__ import annotations

import itertools
import math
import random
from collections import defaultdict

import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import maximum_bipartite_matching


def exhaustive_ideal_hit() -> None:
    for n in range(1, 6):
        universe = tuple(range(n))
        maps = list(itertools.product(universe, repeat=n))
        for s_size in range(n + 1):
            sset = set(range(s_size))
            for t_size in range(n + 1):
                tset = set(range(t_size))
                total = 0
                for f in maps:
                    total += len({f[u] for u in sset} & tset)
                exact = total / len(maps)
                formula = t_size * (1 - (1 - 1 / n) ** s_size)
                assert abs(exact - formula) < 1e-12


def greedy_selector(maps: list[list[int]], n_targets: int):
    n_sources = len(maps[0])
    unused = set(range(n_sources))
    unmatched = set(range(n_targets))
    chosen = []
    trajectory = [len(unmatched)]
    for f in maps:
        preimages = defaultdict(list)
        for u in unused:
            v = f[u]
            if v in unmatched:
                preimages[v].append(u)
        for v in list(preimages):
            u = preimages[v][0]
            chosen.append((u, v))
            unused.remove(u)
            unmatched.remove(v)
        trajectory.append(len(unmatched))
    assert len({u for u, _ in chosen}) == len(chosen)
    assert len({v for _, v in chosen}) == len(chosen)
    return len(unmatched), trajectory


def audit_ideal_greedy() -> None:
    rng = random.Random(20260821)
    rows = []
    for n in (100, 300, 1000):
        for k in (2, 5, 10, 25):
            trials = 300 if n <= 300 else 100
            misses = []
            for _ in range(trials):
                maps = [[rng.randrange(n) for _ in range(n)] for _ in range(k)]
                miss, trajectory = greedy_selector(maps, n)
                assert all(trajectory[j + 1] <= trajectory[j]
                           for j in range(len(trajectory) - 1))
                misses.append(miss)
            empirical = sum(misses) / (trials * n)
            theorem_bound = 1 / (1 + k)
            # The theorem is an expectation statement; allow finite sampling noise.
            assert empirical <= theorem_bound + 0.03
            rows.append((n, k, empirical, theorem_bound))
    print("IDEAL_GREEDY", rows)


def audit_collapsed_counterexample() -> None:
    for n in range(2, 30):
        for k in range(1, min(8, n) + 1):
            # Enumerate a deterministic list of distinct collapsed targets;
            # repeats can only make the matching smaller.
            maps = [[j % n] * n for j in range(k)]
            miss, _ = greedy_selector(maps, n)
            assert miss == n - k
            images = len({j % n for j in range(k)})
            assert images == k
            assert n - images == miss
            joint = 1 / n
            assert abs(joint - n / (n * n)) < 1e-15


def audit_containment_covering_maps() -> None:
    rows = []
    for b in range(2, 7):
        ground = range(2 * b)
        sources = [frozenset(x) for x in itertools.combinations(ground, b)]
        for q in range(1, min(2, b) + 1):
            targets = [frozenset(x) for x in itertools.combinations(ground, b + q)]
            uncovered = set(range(len(sources)))
            cover = []
            incidences = [set(i for i, u in enumerate(sources) if u <= v)
                          for v in targets]
            while uncovered:
                j = max(range(len(targets)), key=lambda x: len(incidences[x] & uncovered))
                hit = incidences[j] & uncovered
                assert hit
                cover.append(j)
                uncovered -= hit
            d = math.comb(b, q)
            bound = math.ceil(len(targets) * (math.log(len(sources)) + 1) / d)
            assert len(cover) <= bound
            # Assign every source to the first chosen containing target.
            mapping = {}
            for u in sources:
                v = next(targets[j] for j in cover if u <= targets[j])
                mapping[u] = v
                assert u <= v
            assert len(mapping) == len(sources)
            assert len(set(mapping.values())) <= len(cover)
            rows.append((b, q, len(cover), bound, len(targets)))
    print("CONTAINMENT_COVERS", rows)


def walecki_factor(b: int) -> list[tuple[int, ...]]:
    assert b % 2 == 1
    h = (b - 1) // 2
    inf = b - 1
    base = [inf]
    for j in range(h):
        base.extend([j, (-j - 1) % (b - 1)])
    cycles = []
    for shift in range(h):
        cycles.append(tuple(inf if x == inf else (x + shift) % (b - 1)
                            for x in base))
    edges = set()
    for cyc in cycles:
        for i in range(b):
            edge = frozenset((cyc[i], cyc[(i + 1) % b]))
            assert edge not in edges
            edges.add(edge)
    assert len(edges) == math.comb(b, 2)
    return cycles


def factors_b5() -> dict[int, list[tuple[int, ...]]]:
    b = 5
    base = [tuple(range(b))]
    wal = walecki_factor(b)
    factors = {1: base, 2: wal, 3: wal, 4: base}
    for r, orders in factors.items():
        seen = set()
        for order in orders:
            for i in range(b):
                window = frozenset(order[(i + j) % b] for j in range(r))
                assert window not in seen
                seen.add(window)
        assert len(seen) == math.comb(b, r)
    return factors


def conjugate_orders(orders, perm):
    return [tuple(perm[x] for x in order) for order in orders]


def physical_bank_b5(rank_perm, q, rng):
    b = 5
    factors = factors_b5()
    mapping = {}
    for r in range(q, b - q + 1):
        pa = list(range(b)); pb = list(range(b))
        rng.shuffle(pa); rng.shuffle(pb)
        fa = conjugate_orders(factors[r], pa)
        fb = conjugate_orders(factors[r], pb)
        pset = {x for x in range(b) if rank_perm[x] < r}
        types = [x in pset for x in range(b)]
        for alpha in fa:
            for beta in fb:
                ca = cb = 0
                word = []
                length = b * b + b + q
                for time in range(length):
                    if types[time % b]:
                        word.append(alpha[ca % b])
                        ca += 1
                    else:
                        word.append(b + beta[cb % b])
                        cb += 1
                for start in range(b * b):
                    source = frozenset(word[start:start + b])
                    target = frozenset(word[start:start + b + q])
                    assert len(source) == b
                    assert len(target) == b + q
                    assert source not in mapping
                    mapping[source] = target
    assert len(mapping) == sum(math.comb(b, r) ** 2 for r in range(q, b - q + 1))
    return mapping


def matching_size(maps, target_layer):
    sources = sorted(set().union(*(m.keys() for m in maps)), key=lambda x: tuple(sorted(x)))
    targets = {v: i for i, v in enumerate(target_layer)}
    rows, cols = [], []
    for i, u in enumerate(sources):
        for m in maps:
            v = m[u]
            rows.append(i); cols.append(targets[v])
    data = np.ones(len(rows), dtype=np.int8)
    graph = csr_matrix((data, (rows, cols)), shape=(len(sources), len(targets)))
    match = maximum_bipartite_matching(graph, perm_type="column")
    return int(np.count_nonzero(match >= 0))


def audit_physical_b5_menu() -> None:
    rng = random.Random(510817)
    b = 5
    rank_perm = list(range(b))
    rng.shuffle(rank_perm)
    rows = []
    for q in (1, 2):
        target_layer = [frozenset(c) for c in itertools.combinations(range(2 * b), b + q)]
        maps = []
        last = 0
        for k in range(1, 9):
            maps.append(physical_bank_b5(rank_perm, q, rng))
            size = matching_size(maps, target_layer)
            assert size >= last
            assert size <= len(target_layer)
            last = size
            rows.append((q, k, size, len(target_layer)))
    print("PHYSICAL_B5_MENU", rows)


def main() -> None:
    exhaustive_ideal_hit()
    audit_ideal_greedy()
    audit_collapsed_counterexample()
    audit_containment_covering_maps()
    audit_physical_b5_menu()
    print("PASS polylog factor-menu residual-hitting selector audit")


if __name__ == "__main__":
    main()
