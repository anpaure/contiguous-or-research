#!/usr/bin/env python3
"""Solve the exact separated-port, edgewise-upper-safe MSW tree at m=8.

Heavy runs belong on h100.  Candidate edges are transposition-adjacent tight
MSW roots with a concrete compatible pair of oriented/shifted d-histories.
Candidates are retained only when the corresponding two-cycle splice loses
no globally supported proper-upper target.  CP-SAT then imposes one global
orientation per root, separated length-d ports, and a spanning tree.
"""

from __future__ import annotations

import argparse
import collections
import itertools
import json
import math
import time

from ortools.sat.python import cp_model

import audit_msw_common_history_upper_deck_20260813 as up
import audit_msw_inverse_trade_portal_shadow_20260813 as base


def proper_upper_support(owners, R, ground):
    n = len(owners)
    ans = set()
    for i in range(n):
        u = 0
        for length in range(1, n):
            u |= owners[(i + length - 1) % n]
            if u == ground:
                break
            if u.bit_count() > R:
                ans.add(u)
    return ans


def build(m):
    R = m + 1
    n = 2 * m + 1
    W = math.comb(n, R)
    half = 1 << (n - 1)
    d = 0
    while d * W + d * (d + 1) // 2 < half:
        d += 1
    roots = list(base.dyck_words(m))
    rows = [list(base.msw_row(root)) for root in roots]
    root_index = {root: i for i, root in enumerate(roots)}
    ground = (1 << n) - 1

    owner_cycles = []
    row_support = []
    global_load = collections.Counter()
    states = []
    for row in rows:
        oriented_cycles = []
        ss = []
        for oi, order in enumerate((row, list(reversed(row)))):
            oriented_cycles.append([up.owner_cycle(order, shift, R)
                                    for shift in range(n)])
            for shift in range(n):
                ss.append((oi, shift, up.state(order, shift, d, R)))
        owner_cycles.append(oriented_cycles)
        support = proper_upper_support(oriented_cycles[0][0], R, ground)
        row_support.append(support)
        global_load.update(support)
        states.append(ss)

    root_pairs = []
    candidates = []
    pair_candidates = collections.defaultdict(list)
    for a, root in enumerate(roots):
        ones = [i for i, x in enumerate(root) if x == "1"]
        zeros = [i for i, x in enumerate(root) if x == "0"]
        for p in ones:
            for q in zeros:
                z = list(root)
                z[p], z[q] = "0", "1"
                b = root_index.get("".join(z))
                if b is None or b <= a:
                    continue
                at_risk = {u for u in row_support[a] | row_support[b]
                           if global_load[u] == ((u in row_support[a]) +
                                                (u in row_support[b]))}
                local = []
                for oa, sa, xa in states[a]:
                    for ob, sb, xb in states[b]:
                        if not up.compatible(xa, xb):
                            continue
                        owners = owner_cycles[a][oa][sa] + owner_cycles[b][ob][sb]
                        if not at_risk <= proper_upper_support(owners, R, ground):
                            continue
                        key = (a, b, oa, sa, ob, sb)
                        local.append(len(candidates))
                        candidates.append(key)
                if local:
                    pi = len(root_pairs)
                    root_pairs.append((a, b))
                    pair_candidates[pi] = local
    return {
        "m": m, "R": R, "n": n, "d": d, "roots": roots,
        "rows": rows, "states": states, "owner_cycles": owner_cycles,
        "global_load": global_load, "ground": ground,
        "root_pairs": root_pairs, "candidates": candidates,
        "pair_candidates": pair_candidates,
    }


def solve(data, seconds):
    N = len(data["roots"])
    n, d = data["n"], data["d"]
    pairs, candidates = data["root_pairs"], data["candidates"]
    model = cp_model.CpModel()
    x = [model.NewBoolVar(f"x_{i}") for i in range(len(candidates))]
    y = [model.NewBoolVar(f"e_{i}") for i in range(len(pairs))]
    orient = [model.NewBoolVar(f"o_{v}") for v in range(N)]
    incident = [[[] for _ in range(2 * n)] for _ in range(N)]

    for pi, ids in data["pair_candidates"].items():
        model.Add(sum(x[i] for i in ids) == y[pi])
    for i, (a, b, oa, sa, ob, sb) in enumerate(candidates):
        incident[a][oa * n + sa].append(x[i])
        incident[b][ob * n + sb].append(x[i])
        if oa:
            model.Add(x[i] <= orient[a])
        else:
            model.Add(x[i] + orient[a] <= 1)
        if ob:
            model.Add(x[i] <= orient[b])
        else:
            model.Add(x[i] + orient[b] <= 1)

    # One edge per physical port and cyclic separation of length-d blocks.
    for v in range(N):
        for oi in range(2):
            loads = []
            for s in range(n):
                z = model.NewBoolVar(f"p_{v}_{oi}_{s}")
                ids = incident[v][oi * n + s]
                model.Add(sum(ids) == z) if ids else model.Add(z == 0)
                loads.append(z)
            for s in range(n):
                for delta in range(1, d + 1):
                    t = (s + delta) % n
                    if s < t or (s + delta >= n):
                        model.Add(loads[s] + loads[t] <= 1)

    model.Add(sum(y) == N - 1)

    # Single-commodity flow on root-pair edges proves connectivity.
    incoming = [[] for _ in range(N)]
    outgoing = [[] for _ in range(N)]
    for pi, (a, b) in enumerate(pairs):
        fab = model.NewIntVar(0, N - 1, f"f_{a}_{b}")
        fba = model.NewIntVar(0, N - 1, f"f_{b}_{a}")
        model.Add(fab <= (N - 1) * y[pi])
        model.Add(fba <= (N - 1) * y[pi])
        outgoing[a].append(fab); incoming[b].append(fab)
        outgoing[b].append(fba); incoming[a].append(fba)
    model.Add(sum(outgoing[0]) - sum(incoming[0]) == N - 1)
    for v in range(1, N):
        model.Add(sum(incoming[v]) - sum(outgoing[v]) == 1)

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = seconds
    solver.parameters.num_search_workers = 32
    solver.parameters.log_search_progress = True
    status = solver.Solve(model)
    selected = [candidates[i] for i in range(len(candidates))
                if solver.Value(x[i])] if status in (
                    cp_model.OPTIMAL, cp_model.FEASIBLE) else []
    return solver.StatusName(status), selected, {
        "wall_time": solver.WallTime(),
        "branches": solver.NumBranches(),
        "conflicts": solver.NumConflicts(),
    }


def verify_source(data, selected):
    m, R, n, d = data["m"], data["R"], data["n"], data["d"]
    N = len(data["roots"])
    chosen_orientation = [-1] * N
    ports = [[] for _ in range(N)]
    for ei, (a, b, oa, sa, ob, sb) in enumerate(selected):
        for v, oi, s, other in ((a, oa, sa, b), (b, ob, sb, a)):
            if chosen_orientation[v] < 0:
                chosen_orientation[v] = oi
            assert chosen_orientation[v] == oi
            ports[v].append((s, ei, other))
    assert all(x >= 0 for x in chosen_orientation)

    orders = [data["rows"][v] if chosen_orientation[v] == 0
              else list(reversed(data["rows"][v])) for v in range(N)]
    s_rank = R - d
    source = []
    forced = []
    for order in orders:
        source.append([sum(1 << order[(j + z) % n] for z in range(s_rank))
                       for j in range(n)])
        forced.append([(1 << order[j]) | (1 << order[(j + s_rank - 1) % n])
                       for j in range(n)])

    cuts = []
    for ei, (a, b, oa, sa, ob, sb) in enumerate(selected):
        history = []
        for j in range(d):
            ha = forced[a][(sa + j) % n]
            hb = forced[b][(sb + j) % n]
            h = ha | hb
            assert h & ~(source[a][(sa + j) % n] & source[b][(sb + j) % n]) == 0
            history.append(h)
            source[a][(sa + j) % n] = h
            source[b][(sb + j) % n] = h
        cuts.append(((a, (sa + d - 1) % n),
                     (b, (sb + d - 1) % n)))

    # All declared source blocks are disjoint and separated at every root.
    for v in range(N):
        starts = [x[0] for x in ports[v]]
        assert len(starts) == len(set(starts))
        for a, b in itertools.combinations(starts, 2):
            assert min((a - b) % n, (b - a) % n) >= d + 1

    # Swap successor occurrences at every tree port.
    successor = {(v, j): (v, (j + 1) % n)
                 for v in range(N) for j in range(n)}
    for ca, cb in cuts:
        successor[ca], successor[cb] = successor[cb], successor[ca]
    start = (0, 0)
    chronology = []
    cur = start
    while True:
        chronology.append(cur)
        cur = successor[cur]
        if cur == start:
            break
        assert len(chronology) <= N * n
    assert len(chronology) == N * n
    word = [source[v][j] for v, j in chronology]

    # Owner ledger induced by the final source word.
    owner_load = collections.Counter()
    for i in range(len(word)):
        u = 0
        for j in range(d + 1):
            u |= word[(i + j) % len(word)]
        owner_load[u] += 1
    assert len(owner_load) == math.comb(2 * m + 1, R)
    assert set(owner_load.values()) == {1}

    # Full proper upper support.  Stop a start once the full ground is met.
    upper = set()
    max_width = 0
    for i in range(len(word)):
        u = 0
        for ell in range(1, len(word) + 1):
            u |= word[(i + ell - 1) % len(word)]
            if u == data["ground"]:
                max_width = max(max_width, ell)
                break
            if u.bit_count() > R:
                upper.add(u)
    all_upper = {sum(1 << z for z in comb)
                 for r in range(R + 1, 2 * m + 1)
                 for comb in itertools.combinations(range(2 * m + 1), r)}
    missing = all_upper - upper
    return {
        "selected_edges": len(selected),
        "source_length": len(word),
        "degree_histogram": dict(collections.Counter(len(x) for x in ports)),
        "owner_exact": True,
        "proper_upper_covered": len(upper),
        "proper_upper_total": len(all_upper),
        "proper_upper_missing": len(missing),
        "proper_upper_missing_rank_histogram": dict(collections.Counter(
            x.bit_count() for x in missing)),
        "maximum_width_until_full_ground": max_width,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("m", type=int)
    ap.add_argument("--seconds", type=float, default=600)
    ap.add_argument("--json")
    args = ap.parse_args()
    started = time.time()
    data = build(args.m)
    build_seconds = time.time() - started
    print(json.dumps({"phase": "build", "roots": len(data["roots"]),
                      "safe_root_pairs": len(data["root_pairs"]),
                      "safe_state_candidates": len(data["candidates"]),
                      "seconds": build_seconds}), flush=True)
    status, selected, stats = solve(data, args.seconds)
    result = {
        "m": args.m, "d": data["d"], "roots": len(data["roots"]),
        "safe_root_pairs": len(data["root_pairs"]),
        "safe_state_candidates": len(data["candidates"]),
        "build_seconds": build_seconds, "status": status,
        "solver": stats,
    }
    if selected:
        result["verification"] = verify_source(data, selected)
        result["selected"] = selected
    payload = json.dumps(result, indent=2, sort_keys=True)
    print(payload)
    if args.json:
        with open(args.json, "w", encoding="utf-8") as f:
            f.write(payload + "\n")


if __name__ == "__main__":
    main()
