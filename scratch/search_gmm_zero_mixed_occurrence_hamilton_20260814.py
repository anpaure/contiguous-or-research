#!/usr/bin/env python3
"""Search for a lower-complete Johnson Hamilton cycle with A_occ=0.

Run on H100 only.  This uses an exact directed AddCircuit model; the
mixed-C4 exclusion is imposed on undirected selected edge pairs.
"""

from __future__ import annotations

import argparse
import itertools
import json

from ortools.sat.python import cp_model


def masks(n, k):
    return [sum(1 << i for i in c) for c in itertools.combinations(range(n), k)]


def points(x, n):
    return [i for i in range(n) if (x >> i) & 1]


def solve(m, time_limit, workers, require_nonregular, two_factor,
          color_forest, fix_first, output):
    n = 2 * m + 1
    verts = masks(n, m)
    lowers = masks(n, m - 1)
    vid = {x: i for i, x in enumerate(verts)}
    edges = []
    eid = {}
    by_lower = {r: [] for r in lowers}
    for i, x in enumerate(verts):
        for j in range(i + 1, len(verts)):
            y = verts[j]
            if (x ^ y).bit_count() != 2:
                continue
            e = len(edges)
            edges.append((x, y))
            eid[(x, y)] = e
            by_lower[x & y].append(e)

    model = cp_model.CpModel()
    arcs = []
    directed = {}
    for e, (x, y) in enumerate(edges):
        xy = model.NewBoolVar(f"a_{vid[x]}_{vid[y]}")
        yx = model.NewBoolVar(f"a_{vid[y]}_{vid[x]}")
        directed[(x, y)] = xy
        directed[(y, x)] = yx
        arcs.append((vid[x], vid[y], xy))
        arcs.append((vid[y], vid[x], yx))
    if not two_factor:
        model.AddCircuit(arcs)
        if fix_first:
            first = sum(1 << i for i in range(m))
            second = (first ^ (1 << (m - 1))) | (1 << m)
            model.Add(directed[(first, second)] == 1)

    selected = []
    for e, (x, y) in enumerate(edges):
        z = model.NewBoolVar(f"e_{e}")
        model.Add(z == directed[(x, y)] + directed[(y, x)])
        selected.append(z)
    if two_factor:
        for x in verts:
            model.Add(sum(selected[e] for e, (u, v) in enumerate(edges)
                          if u == x or v == x) == 2)

    repeated = {}
    loads = {}
    max_load = m + 1
    for r in lowers:
        load = model.NewIntVar(1, max_load, f"load_{r}")
        model.Add(load == sum(selected[e] for e in by_lower[r]))
        loads[r] = load
        rep = model.NewBoolVar(f"rep_{r}")
        model.Add(load == 1).OnlyEnforceIf(rep.Not())
        model.Add(load >= 2).OnlyEnforceIf(rep)
        repeated[r] = rep
        if color_forest:
            outside = [z for z in range(n) if not ((r >> z) & 1)]
            root = outside[0]
            # Enumerate each undirected simple cycle once by fixing its
            # least vertex first and quotienting reversal.
            for k in range(3, len(outside) + 1):
                for support in itertools.combinations(outside, k):
                    least = min(support)
                    rest = tuple(x for x in support if x != least)
                    for tail in itertools.permutations(rest):
                        if tail[0] > tail[-1]:
                            continue
                        cyc = (least,) + tail
                        cycle_edges = []
                        for i in range(k):
                            x = r | (1 << cyc[i])
                            y = r | (1 << cyc[(i + 1) % k])
                            cycle_edges.append(eid[tuple(sorted((x, y)))])
                        model.Add(sum(selected[e] for e in cycle_edges) <= k - 1)

    atoms = set()
    for bset in lowers:
        inside = points(bset, n)
        outside = [z for z in range(n) if not ((bset >> z) & 1)]
        for b in inside:
            for p in outside:
                for a in outside:
                    if a == p:
                        continue
                    e1x = bset | (1 << p)
                    e1y = bset | (1 << a)
                    e1 = eid[tuple(sorted((e1x, e1y)))]
                    pset = (bset ^ (1 << b)) | (1 << p)
                    for c in outside:
                        if c in (p, a):
                            continue
                        e2x = pset | (1 << a)
                        e2y = pset | (1 << c)
                        e2 = eid[tuple(sorted((e2x, e2y)))]
                        atoms.add((bset, min(e1, e2), max(e1, e2)))
    for bset, e1, e2 in atoms:
        model.Add(repeated[bset] + selected[e1] + selected[e2] <= 2)

    eta = (2 * len(verts) // (m + 2)) * (m - 1) // n
    point_surplus = []
    for z in range(n):
        deg = model.NewIntVar(0, 2 * len(verts), f"point_{z}")
        model.Add(deg == sum(loads[r] - 1 for r in lowers if (r >> z) & 1))
        point_surplus.append(deg)
    if require_nonregular:
        neq = []
        for z, deg in enumerate(point_surplus):
            low = model.NewBoolVar(f"point_low_{z}")
            high = model.NewBoolVar(f"point_high_{z}")
            model.Add(deg <= eta - 1).OnlyEnforceIf(low)
            model.Add(deg >= eta).OnlyEnforceIf(low.Not())
            model.Add(deg >= eta + 1).OnlyEnforceIf(high)
            model.Add(deg <= eta).OnlyEnforceIf(high.Not())
            neq.extend((low, high))
        model.AddBoolOr(neq)

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = time_limit
    solver.parameters.num_search_workers = workers
    solver.parameters.log_search_progress = True
    status = solver.Solve(model)
    status_name = solver.StatusName(status)
    result = {
        "m": m,
        "n": n,
        "status": status_name,
        "require_nonregular": require_nonregular,
        "two_factor": two_factor,
        "color_forest": color_forest,
        "fix_first": fix_first,
        "vertices": len(verts),
        "edges": len(edges),
        "mixed_pair_constraints": len(atoms),
        "wall_time": solver.WallTime(),
        "branches": solver.NumBranches(),
        "conflicts": solver.NumConflicts(),
    }
    if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        if not two_factor:
            succ = {}
            for (x, y), var in directed.items():
                if solver.Value(var):
                    succ[x] = y
            cycle = [verts[0]]
            while len(cycle) < len(verts):
                cycle.append(succ[cycle[-1]])
            result["cycle"] = [points(x, n) for x in cycle]
        else:
            result["selected_edges"] = [
                [points(x, n), points(y, n)]
                for e, (x, y) in enumerate(edges) if solver.Value(selected[e])
            ]
        result["loads"] = {str(points(r, n)): solver.Value(loads[r]) for r in lowers}
        result["point_surplus"] = [solver.Value(x) for x in point_surplus]
    with open(output, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, sort_keys=True)
        f.write("\n")
    print(json.dumps({k: v for k, v in result.items() if k not in ("cycle", "loads")}, sort_keys=True))
    return 0 if status in (cp_model.OPTIMAL, cp_model.FEASIBLE, cp_model.INFEASIBLE) else 2


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--m", type=int, required=True)
    ap.add_argument("--time-limit", type=float, default=600)
    ap.add_argument("--workers", type=int, default=32)
    ap.add_argument("--require-nonregular", action="store_true")
    ap.add_argument("--two-factor", action="store_true")
    ap.add_argument("--color-forest", action="store_true")
    ap.add_argument("--fix-first", action="store_true")
    ap.add_argument("--output", required=True)
    args = ap.parse_args()
    raise SystemExit(solve(args.m, args.time_limit, args.workers,
                           args.require_nonregular, args.two_factor,
                           args.color_forest,
                           args.fix_first,
                           args.output))


if __name__ == "__main__":
    main()
