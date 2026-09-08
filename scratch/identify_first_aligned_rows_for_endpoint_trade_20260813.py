#!/usr/bin/env python3
"""Identify root/row witnesses for endpoint-rotation trade edges (H100)."""

from __future__ import annotations

import argparse
import json

import audit_msw_inverse_trade_portal_shadow_20260813 as base
import audit_pbbs_portal_compound_coexistence_20260813 as co
import cpsat_relative_incidence_trade_compound_seam_20260813 as cp


def described_factor(m):
    roots, original = base.build_factor(m)
    paired = set()
    removed = set()
    result = {}
    for w in roots:
        if w in paired:
            continue
        mate = None
        gap = None
        for j in range(0, 2 * m - 3, 4):
            block = w[j:j + 4]
            if block == "1100":
                mate = w[:j] + "1010" + w[j + 4:]
                gap = j
                break
            if block == "1010":
                mate = w[:j] + "1100" + w[j + 4:]
                gap = j
                break
        if mate is None:
            continue
        paired.update((w, mate))
        neg = (original[w], original[mate])
        pos = base.recover_inverse_trade(*neg, m)
        removed.update(neg)
        for idx, row in enumerate(pos):
            result[row] = {"kind": "positive", "root": w,
                           "mate": mate, "gap": gap, "positive_index": idx}
    for w, row in original.items():
        if row not in removed:
            result[row] = {"kind": "original", "root": w}
    return result


def edge_map(desc, m):
    ans = {}
    for row, info in desc.items():
        owners = [co.cyc_window(row, i, m + 1) for i in range(2 * m + 1)]
        for i in range(2 * m + 1):
            edge = frozenset((owners[i], owners[(i + 1) % (2 * m + 1)]))
            facet = frozenset.intersection(*edge)
            ans[facet] = (edge, row, i, info)
    return ans


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("m", type=int)
    ap.add_argument("changes_json")
    ap.add_argument("--lift-m9", action="store_true")
    ap.add_argument("--main-paths", action="store_true")
    args = ap.parse_args()
    with open(args.changes_json, encoding="utf-8") as f:
        payload = json.load(f)
    if args.main_paths:
        record = next(x for x in payload if x["m"] == args.m)
        choice = record["choices"][1]
        facets = [frozenset(x["facet"])
                  for path in choice["paths"] for x in path]
    elif args.lift_m9:
        steps = payload[0]["support_monotone"]["repair"]
        tail_map = {15: 2 * args.m - 3, 16: 2 * args.m - 2,
                    17: 2 * args.m - 1, 18: 2 * args.m}
        extras = set(range(16, 2 * args.m - 2, 2))
        lift = lambda xs: frozenset(tail_map.get(x, x) for x in xs) | extras
        facets = [lift(x["facet"]) for x in steps]
    else:
        facets = [frozenset(x["facet"]) for x in payload]
    desc = described_factor(args.m)
    emap = edge_map(desc, args.m)
    out = []
    for facet in facets:
        edge, row, i, info = emap[facet]
        out.append({
            "facet": sorted(facet),
            "owners": [sorted(x) for x in edge],
            "row": list(row),
            "index": i,
            **info,
        })
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
