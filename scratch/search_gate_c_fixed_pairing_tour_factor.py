#!/usr/bin/env python3
"""Exact-cover search for coherent tours in one fixed pairing stratum."""

from collections import defaultdict
from itertools import permutations
import sys


def tour_support(b, order, x):
    out = []
    state = x
    for s in range(b):
        j = order[s]
        for t in range(1, b):
            i = order[(s + t) % b]
            # Encode a defect-one target by (empty, double, split-bit mask).
            split = 0
            for q in range(1, b):
                k = order[(s + q) % b]
                if k == i:
                    continue
                bit = ((state >> k) & 1) ^ (q < t)
                split |= bit << k
            out.append((j, i, split))
        state ^= ((1 << b) - 1) ^ (1 << j)
    assert len(out) == len(set(out)) == b * (b - 1)
    return frozenset(out)


def all_tours(b):
    tours = {}
    for tail in permutations(range(1, b)):
        order = (0,) + tail
        for x in range(1 << b):
            support = tour_support(b, order, x)
            tours.setdefault(support, (order, x))
    return list(tours), [tours[s] for s in tours]


def exact_factor(b):
    edges, witnesses = all_tours(b)
    universe = set().union(*edges)
    expected = b * (b - 1) * (1 << (b - 2))
    assert len(universe) == expected
    incidence = defaultdict(list)
    for e, support in enumerate(edges):
        for v in support:
            incidence[v].append(e)
    print(f"b={b}: {len(edges)} simple tours, {len(universe)} targets, "
          f"degree range {min(map(len, incidence.values()))}.."
          f"{max(map(len, incidence.values()))}", flush=True)
    invariant_hist = defaultdict(int)
    for support in edges:
        total_sign = sum(-1 if split.bit_count() & 1 else 1
                         for _, _, split in support)
        by_empty = tuple(sum(-1 if split.bit_count() & 1 else 1
                             for jj, _, split in support if jj == j)
                         for j in range(b))
        invariant_hist[(total_sign, tuple(sorted(by_empty)))] += 1
    print("parity-sign profiles", dict(invariant_hist), flush=True)

    # Fixed-pairing automorphisms are transitive on tours, so an exact factor,
    # if one exists, may be moved to contain the natural tour.
    natural = edges.index(tour_support(b, tuple(range(b)), 0))
    chosen = [natural]
    covered = set(edges[natural])
    compatible = {e for e, support in enumerate(edges)
                  if support.isdisjoint(covered)}
    print("compatible with natural", len(compatible), flush=True)
    nodes = 0
    best_chosen = list(chosen)

    def search(covered, compatible):
        nonlocal nodes, best_chosen
        nodes += 1
        if len(chosen) > len(best_chosen):
            best_chosen = list(chosen)
            print("new depth", len(chosen), "covered", len(covered), flush=True)
        if len(covered) == len(universe):
            return list(chosen)
        if nodes % 100000 == 0:
            print("nodes", nodes, "depth", len(chosen), "compatible", len(compatible), flush=True)
        # Minimum remaining value, with an inexpensive impossibility check.
        best = None
        candidates = None
        for v in universe - covered:
            cand = [e for e in incidence[v] if e in compatible]
            if not cand:
                return None
            if candidates is None or len(cand) < len(candidates):
                best, candidates = v, cand
                if len(candidates) == 1:
                    break
        # Prefer edges which eliminate the most currently sparse constraints.
        scarcity = {v: sum(e in compatible for e in incidence[v])
                    for v in universe - covered}
        candidates.sort(key=lambda e: sum(1 / scarcity[v] for v in edges[e]), reverse=True)
        for e in candidates:
            support = edges[e]
            chosen.append(e)
            new_covered = covered | support
            new_compatible = {f for f in compatible if edges[f].isdisjoint(support)}
            ans = search(new_covered, new_compatible)
            if ans is not None:
                return ans
            chosen.pop()
        return None

    answer = search(covered, compatible)
    print("nodes", nodes, "answer", answer, "best depth", len(best_chosen), flush=True)
    if answer is not None:
        for e in answer:
            order, x = witnesses[e]
            print(" ", order, format(x, f"0{b}b"), flush=True)
    return answer


if __name__ == "__main__":
    exact_factor(int(sys.argv[1]) if len(sys.argv) > 1 else 5)
