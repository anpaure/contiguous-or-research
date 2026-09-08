#!/usr/bin/env python3
"""Audit the stabilized all-m endpoint-rotation seam/repair formula (H100).

The candidate is defined by explicit moving-owner sequences.  For every step
the factor itself must supply the displayed old coloured edge; no search is
used once the formulas are instantiated.
"""

from __future__ import annotations

import argparse
import collections
import json

import audit_pbbs_portal_compound_coexistence_20260813 as co
import cpsat_relative_incidence_trade_compound_seam_20260813 as cp
import search_uniform_endpoint_rotation_paths_20260813 as ep
import audit_msw_inverse_trade_portal_shadow_20260813 as base


def fs(*parts):
    out = set()
    for part in parts:
        out.update(part)
    return frozenset(out)


def candidate(m):
    n = 2 * m + 1
    c = co.c_owner(m, 4)
    u = co.height_owner(m, 5)
    f0 = c & u
    old_a = f0 | {2 * m - 3}
    old_b = f0 | {2 * m - 5}

    # The stabilized shortest paths are most safely defined directly from
    # their elementary exchanges; this keeps every rank exactly m+1.
    def exchange(v, delete, insert):
        assert delete in v and insert not in v
        return (v - {delete}) | {insert}
    p = [c]
    for delete, insert in ((2*m-4, 3), (5, 2), (2*m, 2*m-4),
                           (3, 2*m-3), (2, 2*m)):
        p.append(exchange(p[-1], delete, insert))
    assert p[-1] == old_a
    q = [u]
    parity = m & 1
    base_odd = 11 + 2 * parity
    t = (m - 4) // 2
    q.append(exchange(q[-1], 2*m-2, base_odd))
    q.append(exchange(q[-1], 10, base_odd + 4))
    for j in range(3, t):
        q.append(exchange(q[-1], base_odd + 4*(j-3),
                          base_odd + 4*(j-1)))
    q.append(exchange(q[-1], base_odd + 4*(t-3), 2*m-2))
    assert q[-1] == old_b

    # Repair circuit: lift m=9 labels 15..18 to the last four labels and
    # insert intermediate evens in every owner.
    tail = {15: 2*m-3, 16: 2*m-2, 17: 2*m-1, 18: 2*m}
    fixed = set(range(16, 2*m-2, 2))
    def lift(xs):
        return fs((tail.get(x, x) for x in xs), fixed)
    r = [lift(x) for x in (
        {2,6,8,9,10,12,14,15,16,17},
        {2,6,7,8,9,10,12,14,15,16},
        {0,2,6,7,8,9,12,14,15,16},
        {0,1,2,6,7,9,12,14,15,16},
        {0,1,2,6,9,10,12,14,15,16},
        {0,2,6,9,10,12,14,15,16,17},
        {2,6,8,9,10,12,14,15,16,17},
    )]
    return f0, frozenset((c, u)), (p, q, r)


def audit(m, d):
    _, old, loads, _ = cp.old_factor_data(m)
    frozen = ep.protected_facets(m, d)
    f0, seam_pair, circuits = candidate(m)
    neg = {f0: old[f0]}
    pos = {f0: seam_pair}
    failures = []
    steps = []
    for ci, vertices in enumerate(circuits):
        for a, b in zip(vertices, vertices[1:]):
            facet = a & b
            matches = facet in old and a in old[facet]
            stationary = None
            if matches:
                stationary = next(iter(old[facet] - {a}))
                neg[facet] = old[facet]
                pos[facet] = frozenset((stationary, b))
            steps.append({"circuit": ci, "from": sorted(a), "to": sorted(b),
                          "facet": sorted(facet), "matches": matches,
                          "frozen": facet in frozen,
                          "stationary": sorted(stationary) if stationary else None})
            if not matches:
                failures.append(steps[-1])
    old_deg = collections.Counter(v for e in neg.values() for v in e)
    new_deg = collections.Counter(v for e in pos.values() for v in e)
    old_part = collections.Counter(frozenset().union(*e) for e in neg.values())
    new_part = collections.Counter(frozenset().union(*e) for e in pos.values())
    holes = [sorted(u) for u, count in (old_part - new_part).items()
             if loads[u] - count < 1]
    # Whole selected portal rows are frozen iff none of their row facets is
    # changed.  The cheap owner-marker argument should ultimately replace this
    # finite check in the proof.
    portal_row_hits = []
    _, canonical = base.build_factor(m)
    tasks = [(a, q0) for q0 in range(2, d)
             for a in range(q0 + 1, d + 1) if a <= m - q0]
    if d + 1 <= m - d:
        tasks.append((d + 1, d))
    for a, q0 in tasks:
        z = co.z_word(m, a, q0)
        neg_rows = (canonical["1100" + z], canonical["1010" + z])
        for row in base.recover_inverse_trade(*neg_rows, m):
            owners = [co.cyc_window(row, i, m + 1)
                      for i in range(2 * m + 1)]
            facets = {owners[i] & owners[(i + 1) % (2 * m + 1)]
                      for i in range(2 * m + 1)}
            hit = facets & set(neg)
            if hit:
                portal_row_hits.append({"task": [a, q0],
                                        "hits": [sorted(x) for x in hit]})
    return {"m": m, "d": d, "steps": len(steps),
            "changed_facets": len(neg), "failures": failures,
            "any_frozen": any(x["frozen"] for x in steps),
            "owner_exact": old_deg == new_deg,
            "upper_holes": holes, "support_monotone": not holes,
            "portal_row_hits": portal_row_hits,
            "detail": steps}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pairs", nargs="+", help="m:d")
    ap.add_argument("--json")
    args = ap.parse_args()
    ans = [audit(*map(int, p.split(":"))) for p in args.pairs]
    payload = json.dumps(ans, indent=2, sort_keys=True)
    print(payload)
    if args.json:
        with open(args.json, "w", encoding="utf-8") as f:
            f.write(payload + "\n")


if __name__ == "__main__":
    main()
