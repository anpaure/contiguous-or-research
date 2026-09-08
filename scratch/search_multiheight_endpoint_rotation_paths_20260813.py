#!/usr/bin/env python3
"""Finite multi-height endpoint-rotation diagnostic.

Heavy runs belong on h100.  It builds the complete first-aligned factor once
and searches the two moving-owner paths for each requested compound seam.
"""

from __future__ import annotations

import argparse
import json

import audit_pbbs_portal_compound_coexistence_20260813 as co
import cpsat_relative_incidence_trade_compound_seam_20260813 as cp
import search_uniform_endpoint_rotation_paths_20260813 as one


def audit(m: int, d: int, heights: list[int]):
    _, old, loads, _ = cp.old_factor_data(m)
    frozen = one.protected_facets(m, d)
    records = []
    for h in heights:
        c = co.c_owner(m, h)
        u = co.height_owner(m, h + 1)
        f0 = c & u
        endpoints = sorted(old[f0], key=lambda x: tuple(sorted(x)))
        choices = []
        for a, b in (endpoints, endpoints[::-1]):
            p = one.shortest_path(m, old, frozen, c, a, f0)
            q = one.shortest_path(m, old, frozen, u, b, f0)
            if p is None or q is None:
                continue
            fp = {x[1] for x in p}
            fq = {x[1] for x in q}
            if fp & fq:
                continue
            choices.append({
                "assignment": [sorted(a - f0), sorted(b - f0)],
                "path_lengths": [len(p), len(q)],
                "facets_p": [sorted(x[1]) for x in p],
                "facets_q": [sorted(x[1]) for x in q],
                "moving_p": [sorted(c)] + [sorted(x[3]) for x in p],
                "moving_q": [sorted(u)] + [sorted(x[3]) for x in q],
            })
        records.append({
            "h": h,
            "c": sorted(c),
            "u": sorted(u),
            "seam": sorted(f0),
            "old_endpoint_extras": [sorted(x - f0) for x in endpoints],
            "choices": choices,
        })
    # Exact overlap census for the first shortest choice at each height.
    overlaps = []
    for i, x in enumerate(records):
        if not x["choices"]:
            continue
        fx = {tuple(a) for key in ("facets_p", "facets_q")
              for a in x["choices"][0][key]} | {tuple(x["seam"])}
        for y in records[i + 1:]:
            if not y["choices"]:
                continue
            fy = {tuple(a) for key in ("facets_p", "facets_q")
                  for a in y["choices"][0][key]} | {tuple(y["seam"])}
            overlaps.append({"heights": [x["h"], y["h"]],
                             "facet_overlap": len(fx & fy)})
    return {"m": m, "d": d, "records": records, "overlaps": overlaps}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("m", type=int)
    ap.add_argument("d", type=int)
    ap.add_argument("heights", nargs="+", type=int)
    ap.add_argument("--json")
    args = ap.parse_args()
    ans = audit(args.m, args.d, args.heights)
    payload = json.dumps(ans, indent=2, sort_keys=True)
    print(payload)
    if args.json:
        with open(args.json, "w", encoding="utf-8") as handle:
            handle.write(payload + "\n")


if __name__ == "__main__":
    main()
