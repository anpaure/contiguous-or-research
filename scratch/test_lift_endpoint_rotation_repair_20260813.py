#!/usr/bin/env python3
"""Test fixed-even-coordinate lifts of the m=9 upper-repair circuit (H100)."""

from __future__ import annotations

import argparse
import collections
import json

import cpsat_relative_incidence_trade_compound_seam_20260813 as cp
import search_uniform_endpoint_rotation_paths_20260813 as ep
import audit_pbbs_portal_compound_coexistence_20260813 as co


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("m", type=int)
    ap.add_argument("repair_json")
    args = ap.parse_args()
    with open(args.repair_json, encoding="utf-8") as f:
        base = json.load(f)[0]["support_monotone"]["repair"]
    _, old, loads, _ = cp.old_factor_data(args.m)
    frozen = ep.protected_facets(args.m, 4)
    # The m=9 terminal block {15,16,17,18} is the moving tail
    # {2m-3,2m-2,2m-1,2m}; intervening even labels are fixed.
    tail_map = {15: 2 * args.m - 3, 16: 2 * args.m - 2,
                17: 2 * args.m - 1, 18: 2 * args.m}
    extras = set(range(16, 2 * args.m - 2, 2))
    def lift(xs):
        return frozenset(tail_map.get(x, x) for x in xs) | extras
    rows = []
    repair_neg = {}
    repair_pos = {}
    for r in base:
        facet = lift(r["facet"])
        old_pair = frozenset((lift(r["from"]), lift(r["stationary"])))
        new_pair = frozenset((lift(r["to"]), lift(r["stationary"])))
        rows.append({
            "facet": sorted(facet),
            "rank": len(facet),
            "old_pair_matches": old.get(facet) == old_pair,
            "frozen": facet in frozen,
            "old_pair": [sorted(x) for x in old_pair],
            "actual_old": [sorted(x) for x in old.get(facet, ())],
            "new_pair": [sorted(x) for x in new_pair],
        })
        repair_neg[facet] = old_pair
        repair_pos[facet] = new_pair

    c4, u5 = co.c_owner(args.m, 4), co.height_owner(args.m, 5)
    seam_facet = c4 & u5
    endpoints = sorted(old[seam_facet], key=lambda x: tuple(sorted(x)))
    a, b = endpoints[::-1]
    p = ep.shortest_path(args.m, old, frozen, c4, a, seam_facet)
    q = ep.shortest_path(args.m, old, frozen, u5, b, seam_facet)
    main_neg = {seam_facet: old[seam_facet]}
    main_pos = {seam_facet: frozenset((c4, u5))}
    for path in (p, q):
        for _v, facet, stationary, nxt, *_ in path:
            main_neg[facet] = old[facet]
            main_pos[facet] = frozenset((stationary, nxt))
    assert not (set(main_neg) & set(repair_neg))
    neg = main_neg | repair_neg
    pos = main_pos | repair_pos
    old_part = collections.Counter(frozenset().union(*e) for e in neg.values())
    new_part = collections.Counter(frozenset().union(*e) for e in pos.values())
    holes = [sorted(u) for u, c in (old_part - new_part).items()
             if loads[u] - c < 1]
    old_deg = collections.Counter(v for e in neg.values() for v in e)
    new_deg = collections.Counter(v for e in pos.values() for v in e)
    print(json.dumps({"m": args.m, "extras": sorted(extras), "rows": rows,
                      "all_match": all(x["old_pair_matches"] for x in rows),
                      "any_frozen": any(x["frozen"] for x in rows),
                      "main_lengths": [len(p), len(q)],
                      "owner_exact": old_deg == new_deg,
                      "upper_holes": holes,
                      "support_monotone": not holes}, indent=2))


if __name__ == "__main__":
    main()
