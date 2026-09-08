#!/usr/bin/env python3
"""Exact SAT audit of the first piece-preserving PBBS q-safe cut gate.

The complement-GK/PBBS owner factor has one Johnson edge for every
rank-m lower set on [2m+1].  A Boolean variable says that this old edge is
cut.  We impose

  * every positive coordinate-run collar of length < q contains a cut;
  * for every rank-(m+2) union colour, at least one old witness is uncut.

Thus SAT is exactly the capacitated collar transversal (4.5) in
MATH_SYNTHESIS_SECOND_SHADOW_SUPPORT_CLOSED_AND_LONG_RESIDENCE_RETHREAD_GATE_20260813.md.
It is only a necessary gate for a successful rethread: new seams and deeper
flags are not represented.

Run substantial instances on h100, not on the local Mac.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
import time
from collections import defaultdict

from pysat.solvers import Solver


def masks(n: int, rank: int):
    for cc in itertools.combinations(range(n), rank):
        z = 0
        for i in cc:
            z |= 1 << i
        yield z


def unmatched_linear(word: int, n: int):
    """The audited GK linear matching convention used by the factor."""
    stack = []
    free_ones = []
    for i in range(n):
        if (word >> i) & 1:
            if stack:
                stack.pop()
            else:
                free_ones.append(i)
        else:
            stack.append(i)
    return free_ones, stack


def gk_up(word: int, n: int) -> int:
    return word | (1 << unmatched_linear(word, n)[1][0])


def gk_down(word: int, n: int) -> int:
    return word ^ (1 << unmatched_linear(word, n)[0][-1])


def complement_up(word: int, n: int) -> int:
    full = (1 << n) - 1
    return full ^ gk_down(full ^ word, n)


def rank_slack(k: int) -> int:
    r = (k + 1) // 2
    w = math.comb(k, r)
    lower = sum(math.comb(k, s) for s in range(1, r))
    d = 0
    while lower > d * w + d * (d + 1) // 2:
        d += 1
    return d


def build_factor(m: int):
    n = 2 * m + 1
    edges = []
    adjacency = defaultdict(list)
    fibres = defaultdict(list)
    for lower in masks(n, m):
        a = gk_up(lower, n)
        b = complement_up(lower, n)
        if a == b or (a ^ b).bit_count() != 2:
            raise AssertionError((lower, a, b))
        eid = len(edges)
        upper = a | b
        edges.append((a, b, upper, lower))
        adjacency[a].append((b, eid))
        adjacency[b].append((a, eid))
        fibres[upper].append(eid)
    if any(len(v) != 2 for v in adjacency.values()):
        raise AssertionError("owner graph is not 2-regular")
    return n, edges, adjacency, fibres


def factor_cycles(edges, adjacency):
    used = [False] * len(edges)
    cycles = []
    for seed in range(len(edges)):
        if used[seed]:
            continue
        a, b, _, _ = edges[seed]
        vertices = [a]
        edge_ids = []
        cur = a
        eid = seed
        while True:
            if used[eid]:
                raise AssertionError("premature repeated edge")
            used[eid] = True
            edge_ids.append(eid)
            x, y, _, _ = edges[eid]
            nxt = y if cur == x else x
            if nxt == vertices[0]:
                break
            vertices.append(nxt)
            candidates = [e for _, e in adjacency[nxt] if e != eid]
            if len(candidates) != 1:
                raise AssertionError("bad degree")
            cur, eid = nxt, candidates[0]
        if len(vertices) != len(edge_ids):
            raise AssertionError("cycle indexing mismatch")
        cycles.append((vertices, edge_ids))
    if not all(used):
        raise AssertionError("unvisited factor edge")
    return cycles


def short_run_collars(cycles, n: int, q: int):
    collars = []
    run_hist = defaultdict(int)
    for vertices, edge_ids in cycles:
        length = len(vertices)
        for x in range(n):
            bits = [bool(v & (1 << x)) for v in vertices]
            if all(bits) or not any(bits):
                continue
            zero = next(i for i, bit in enumerate(bits) if not bit)
            i = (zero + 1) % length
            seen = 0
            while seen < length:
                while seen < length and not bits[i]:
                    i = (i + 1) % length
                    seen += 1
                if seen >= length:
                    break
                start = i
                run = 0
                while seen < length and bits[i]:
                    i = (i + 1) % length
                    seen += 1
                    run += 1
                run_hist[run] += 1
                if run < q:
                    # edge_ids[j] joins vertex j to vertex j+1.  The collar
                    # begins with the entering edge start-1 and ends with the
                    # leaving edge start+run-1.
                    collar = tuple(
                        edge_ids[(start - 1 + t) % length]
                        for t in range(run + 1)
                    )
                    collars.append(collar)
    return collars, dict(sorted(run_hist.items()))


def solve(m: int, q: int | None, solver_name: str):
    started = time.time()
    n, edges, adjacency, fibres = build_factor(m)
    cycles = factor_cycles(edges, adjacency)
    if q is None:
        q = rank_slack(n) + 1
    collars, run_hist = short_run_collars(cycles, n, q)
    repeat_count = {
        eid: len(fibres[edges[eid][2]])
        for eid in range(len(edges))
    }
    spare_counts = [
        sum(repeat_count[eid] > 1 for eid in collar)
        for collar in collars
    ]

    # Variable eid+1 is true iff the old edge is cut.
    with Solver(name=solver_name) as sat:
        for collar in collars:
            sat.add_clause([eid + 1 for eid in collar])
        for fibre in fibres.values():
            sat.add_clause([-(eid + 1) for eid in fibre])
        feasible = sat.solve()
        model = sat.get_model() if feasible else None

    cuts = []
    if model is not None:
        positive = {lit for lit in model if lit > 0}
        cuts = [eid for eid in range(len(edges)) if eid + 1 in positive]
        if any(not any(eid in cuts for eid in collar) for collar in collars):
            raise AssertionError("model misses collar")
        if any(all(eid in cuts for eid in fibre) for fibre in fibres.values()):
            raise AssertionError("model deletes an upper fibre")

    result = {
        "m": m,
        "n": n,
        "q": q,
        "owners": len(adjacency),
        "edges": len(edges),
        "components": len(cycles),
        "component_lengths": dict(sorted(
            (str(size), sum(1 for vs, _ in cycles if len(vs) == size))
            for size in sorted({len(vs) for vs, _ in cycles})
        )),
        "upper_colours": len(fibres),
        "upper_fibre_hist": dict(sorted(
            (str(size), sum(1 for f in fibres.values() if len(f) == size))
            for size in sorted({len(f) for f in fibres.values()})
        )),
        "short_collars": len(collars),
        "blocked_short_collars": sum(x == 0 for x in spare_counts),
        "one_spare_short_collars": sum(x == 1 for x in spare_counts),
        "minimum_spare_edges_in_short_collar": min(spare_counts, default=None),
        "blocked_gap9_formula": n * math.comb(m + 1, 5) if q >= 6 else 0,
        "positive_run_hist": {str(k): v for k, v in run_hist.items()},
        "sat": feasible,
        "model_cuts": len(cuts) if feasible else None,
        "upper_total_cut_capacity": len(edges) - len(fibres),
        "seconds": time.time() - started,
    }
    return result


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("m", type=int)
    ap.add_argument("--q", type=int)
    ap.add_argument("--solver", default="cadical195")
    ap.add_argument("--json")
    args = ap.parse_args()
    result = solve(args.m, args.q, args.solver)
    payload = json.dumps(result, indent=2, sort_keys=True)
    print(payload)
    if args.json:
        with open(args.json, "w", encoding="utf-8") as out:
            out.write(payload + "\n")


if __name__ == "__main__":
    main()
