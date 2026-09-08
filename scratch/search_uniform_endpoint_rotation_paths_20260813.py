#!/usr/bin/env python3
"""Search shortest endpoint-rotation paths for the seam C4--U5.

Heavy runs belong on h100.  The script reconstructs the complete
first-aligned packet factor, freezes selected portal rows, searches the
directed endpoint-rotation graph, and records shortest paths together with
their exact immediate-upper support loss.  It is diagnostic for a uniform
symbolic pattern, not itself a theorem.
"""

from __future__ import annotations

import argparse
import collections
import json

import audit_pbbs_portal_compound_coexistence_20260813 as co
import cpsat_relative_incidence_trade_compound_seam_20260813 as cp
import search_relative_inverse_trade_for_compound_seam_20260813 as rel


def protected_facets(m, d):
    ans = set()
    for row in rel.selected_portal_rows(m, d):
        O = [co.cyc_window(row, t, m + 1) for t in range(2 * m + 1)]
        ans.update(
            O[t] & O[(t + 1) % (2 * m + 1)]
            for t in range(2 * m + 1)
        )
    return ans


def shortest_path(m, old, frozen, src, dst, F0):
    ground = set(range(2 * m + 1))
    inc = collections.defaultdict(list)
    for F, edge in old.items():
        upper = frozenset().union(*edge)
        for V in edge:
            inc[V].append((F, next(iter(edge - {V})), upper))
    queue = collections.deque([src])
    pred = {src: None}
    step = {}
    while queue:
        V = queue.popleft()
        if V == dst:
            break
        for F, stationary, old_upper in inc[V]:
            if F == F0 or F in frozen:
                continue
            for x in ground - F:
                W = F | {x}
                if W in (V, stationary) or W in pred:
                    continue
                pred[W] = V
                step[W] = (F, stationary, old_upper)
                queue.append(W)
    if dst not in pred:
        return None
    out = []
    W = dst
    while pred[W] is not None:
        V = pred[W]
        F, stationary, old_upper = step[W]
        out.append((V, F, stationary, W, old_upper, stationary | W))
        W = V
    return out[::-1]


def audit(m, d):
    _, old, loads, _ = cp.old_factor_data(m)
    frozen = protected_facets(m, d)
    C, U = co.c_owner(m, 4), co.height_owner(m, 5)
    F0 = C & U
    old_endpoints = sorted(old[F0], key=lambda V: tuple(sorted(V)))
    choices = []
    for A, B in (old_endpoints, old_endpoints[::-1]):
        p = shortest_path(m, old, frozen, C, A, F0)
        q = shortest_path(m, old, frozen, U, B, F0)
        if p is None or q is None:
            continue
        labels_p = {x[1] for x in p}
        labels_q = {x[1] for x in q}
        if labels_p & labels_q:
            continue
        neg = {F0: old[F0]}
        pos = {F0: frozenset((C, U))}
        for V, F, stationary, W, *_ in p + q:
            neg[F] = old[F]
            pos[F] = frozenset((stationary, W))
        old_deg = collections.Counter(v for e in neg.values() for v in e)
        new_deg = collections.Counter(v for e in pos.values() for v in e)
        assert old_deg == new_deg
        old_u = collections.Counter(frozenset().union(*e) for e in neg.values())
        new_u = collections.Counter(frozenset().union(*e) for e in pos.values())
        removed = old_u - new_u
        choices.append(
            {
                "assignment": [sorted(A - F0), sorted(B - F0)],
                "changed_facets": len(neg),
                "path_lengths": [len(p), len(q)],
                "upper_holes": [
                    {"target": sorted(T), "old_load": loads[T], "removed": c}
                    for T, c in removed.items() if loads[T] - c < 1
                ],
                "paths": [
                    [
                        {
                            "from": sorted(V),
                            "facet": sorted(F),
                            "stationary": sorted(stationary),
                            "to": sorted(W),
                            "old_upper": sorted(old_upper),
                            "new_upper": sorted(new_upper),
                        }
                        for V, F, stationary, W, old_upper, new_upper in path
                    ]
                    for path in (p, q)
                ],
            }
        )
    return {
        "m": m,
        "d": d,
        "frozen_facets": len(frozen),
        "old_seam_endpoint_extras": [sorted(V - F0) for V in old_endpoints],
        "choices": choices,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pairs", nargs="+", help="m:d")
    ap.add_argument("--json")
    args = ap.parse_args()
    out = [audit(*map(int, x.split(":"))) for x in args.pairs]
    payload = json.dumps(out, indent=2, sort_keys=True)
    print(payload)
    if args.json:
        with open(args.json, "w", encoding="utf-8") as f:
            f.write(payload + "\n")


if __name__ == "__main__":
    main()
