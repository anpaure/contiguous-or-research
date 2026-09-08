#!/usr/bin/env python3
"""Finite MILP audit of the exact cross-core q-star assignment system.

For each R=c+q owner A choose exactly one c-core C subset A.  The choice
(A,C) contributes one unit to each incidence edge
    C -- C+u,  u in A\\C.
A necessary condition for decomposing every assigned core fibre into pure
q-window rails is that every such edge load be divisible by q.

This script tests feasibility of that exact 0/1 assignment system.  Heavy
runs belong on h100 only.
"""

from itertools import combinations
from collections import Counter
import argparse
import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import coo_matrix


def bits(comb):
    return sum(1 << x for x in comb)


def audit(k, c, q, time_limit):
    R = c + q
    owners = [bits(x) for x in combinations(range(k), R)]
    cores = [bits(x) for x in combinations(range(k), c)]
    core_index = {x: i for i, x in enumerate(cores)}
    edges = []
    edge_index = {}
    for ci, C in enumerate(cores):
        for u in range(k):
            if C >> u & 1:
                continue
            edge_index[(C, u)] = len(edges)
            edges.append((C, u))

    y = []
    y_by_owner = [[] for _ in owners]
    y_by_edge = [[] for _ in edges]
    for ai, A in enumerate(owners):
        elems = [x for x in range(k) if A >> x & 1]
        for cc in combinations(elems, c):
            C = bits(cc)
            yi = len(y)
            y.append((ai, C))
            y_by_owner[ai].append(yi)
            for u in elems:
                if not (C >> u & 1):
                    y_by_edge[edge_index[(C, u)]].append(yi)

    ny = len(y)
    nz = len(edges)
    nvar = ny + nz
    row = []
    col = []
    data = []
    lb = []
    ub = []
    rid = 0
    for inds in y_by_owner:
        for j in inds:
            row.append(rid); col.append(j); data.append(1)
        lb.append(1); ub.append(1); rid += 1
    for ei, inds in enumerate(y_by_edge):
        for j in inds:
            row.append(rid); col.append(j); data.append(1)
        row.append(rid); col.append(ny + ei); data.append(-q)
        lb.append(0); ub.append(0); rid += 1
    Acon = coo_matrix((data, (row, col)), shape=(rid, nvar)).tocsr()
    integrality = np.ones(nvar, dtype=np.uint8)
    lower = np.zeros(nvar)
    upper = np.r_[np.ones(ny), np.full(nz, np.inf)]
    result = milp(
        np.zeros(nvar), integrality=integrality,
        bounds=Bounds(lower, upper),
        constraints=LinearConstraint(Acon, np.array(lb), np.array(ub)),
        options={"time_limit": time_limit, "presolve": True},
    )
    print("QSTAR", "k", k, "R", R, "c", c, "q", q,
          "M", k-c, "owners", len(owners), "cores", len(cores),
          "edges", len(edges), "yvars", ny,
          "status", result.status, "success", int(result.success),
          "message", result.message)
    if not result.success:
        return False
    sol = result.x
    chosen = [y[j] for j in range(ny) if sol[j] > .5]
    assert len(chosen) == len(owners)
    core_load = Counter(C for _, C in chosen)
    edge_load = Counter()
    for ai, C in chosen:
        A = owners[ai]
        for u in range(k):
            if (A >> u & 1) and not (C >> u & 1):
                edge_load[(C, u)] += 1
    assert all(v % q == 0 for v in edge_load.values())
    print(" core_load_hist", dict(sorted(Counter(core_load.values()).items())),
          "zero_cores", len(cores)-len(core_load),
          "edge_load_hist", dict(sorted(Counter(edge_load.values()).items())),
          "zero_edges", len(edges)-len(edge_load))
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("params", nargs="+", help="k,c,q triples")
    ap.add_argument("--time-limit", type=float, default=300)
    args = ap.parse_args()
    assert len(args.params) % 3 == 0
    ok = []
    for i in range(0, len(args.params), 3):
        ok.append(audit(*(int(x) for x in args.params[i:i+3]),
                        args.time_limit))
    print("OVERALL", int(all(ok)))


if __name__ == "__main__":
    main()
