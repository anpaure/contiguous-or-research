#!/usr/bin/env python3
"""MILP audit of unchanged-cycle Z13 origin shifts for T2 tag losses.

Heavy runs belong on h100 only.
"""

from collections import defaultdict

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import lil_matrix

import audit_msw_t0_relay_linear_allwidth as base
import audit_msw_t2_complete_ml13_cyclic as full


def main():
    canonical = base.canonical_edges(full.M)
    endpoints = full.endpoint_set(canonical)
    old_cycles = full.cycles(*full.full_graph(canonical, canonical, endpoints))
    new_cycles = full.cycles(
        *full.full_graph(full.toggle_t2(canonical), canonical, endpoints)
    )
    merged = next(c for c in new_cycles if len(c[0]) == 65)
    merged_set = set(merged[0])
    affected_old = [c for c in old_cycles if set(c[0]) <= merged_set]
    answer = full.search_common_z13(affected_old, merged)[0]
    old_orders, new_orders, labels = full.build_global_tag_orders(
        old_cycles, new_cycles, affected_old, merged, answer
    )
    so, _ = full.tagged_base_signatures(old_orders, labels)
    sn, _ = full.tagged_base_signatures(new_orders, labels)
    losses = sorted(so - sn, key=lambda z: (z[1], z[0], z[2]))
    assert len(losses) == 42

    candidates = defaultdict(set)
    for lid, (value, span, tag) in enumerate(losses):
        for cid, order in enumerate(old_orders[5:]):
            for i in range(13):
                got = 0
                for j in range(span):
                    got |= order[(i + j) % 13]
                if got == value:
                    candidates[lid].add((cid, (tag - i) % 13))

    zero = [lid for lid in range(len(losses)) if not candidates[lid]]
    print("losses", len(losses), "zero_candidate", len(zero))
    for lid in zero:
        value, span, tag = losses[lid]
        print(" ZERO", lid, full.word(value), span, tag)

    # One origin per unchanged cycle.  First demand every nonzero-candidate
    # loss, then maximize total coverage to obtain a sharp certificate if
    # those constraints conflict.
    ncycles = 127
    nshifts = 13
    nx = ncycles * nshifts
    live = [lid for lid in range(len(losses)) if candidates[lid]]
    rows = ncycles + len(live)
    A = lil_matrix((rows, nx), dtype=float)
    lb = np.empty(rows)
    ub = np.empty(rows)
    for cid in range(ncycles):
        for shift in range(nshifts):
            A[cid, cid * nshifts + shift] = 1
        lb[cid] = ub[cid] = 1
    for r, lid in enumerate(live, start=ncycles):
        for cid, shift in candidates[lid]:
            A[r, cid * nshifts + shift] = 1
        lb[r] = 1
        ub[r] = np.inf
    res = milp(
        c=np.zeros(nx),
        integrality=np.ones(nx),
        bounds=Bounds(np.zeros(nx), np.ones(nx)),
        constraints=LinearConstraint(A.tocsr(), lb, ub),
        options={"time_limit": 60},
    )
    print("cover_all_nonzero_status", res.status, res.message)
    if res.success:
        chosen = {
            cid: max(range(nshifts), key=lambda s: res.x[cid * nshifts + s])
            for cid in range(ncycles)
        }
        covered = [
            lid for lid in range(len(losses))
            if any(chosen[cid] == shift for cid, shift in candidates[lid])
        ]
        print("covered", len(covered), "uncovered", len(losses) - len(covered))
        for lid in sorted(set(range(len(losses))) - set(covered)):
            value, span, tag = losses[lid]
            print(" UNCOVERED", lid, full.word(value), span, tag)
        print("nonzero_origin_assignments")
        for cid, shift in sorted(chosen.items()):
            if shift:
                print(cid, shift)
        return

    # Exact maximum coverage MILP with y_l variables.
    ny = len(losses)
    nvar = nx + ny
    rows = ncycles + len(losses)
    A = lil_matrix((rows, nvar), dtype=float)
    lb = np.empty(rows)
    ub = np.empty(rows)
    for cid in range(ncycles):
        for shift in range(nshifts):
            A[cid, cid * nshifts + shift] = 1
        lb[cid] = ub[cid] = 1
    for lid in range(len(losses)):
        for cid, shift in candidates[lid]:
            A[ncycles + lid, cid * nshifts + shift] = 1
        A[ncycles + lid, nx + lid] = -1
        lb[ncycles + lid] = 0
        ub[ncycles + lid] = np.inf
    c = np.zeros(nvar)
    c[nx:] = -1
    res = milp(
        c=c,
        integrality=np.ones(nvar),
        bounds=Bounds(np.zeros(nvar), np.ones(nvar)),
        constraints=LinearConstraint(A.tocsr(), lb, ub),
        options={"time_limit": 120},
    )
    assert res.success
    covered = [lid for lid in range(ny) if res.x[nx + lid] > .5]
    print("maximum_covered", len(covered), "uncovered", ny - len(covered))
    for lid in sorted(set(range(ny)) - set(covered)):
        value, span, tag = losses[lid]
        print(" UNCOVERED", lid, full.word(value), span, tag,
              "candidate_pairs", len(candidates[lid]))


if __name__ == "__main__":
    main()
