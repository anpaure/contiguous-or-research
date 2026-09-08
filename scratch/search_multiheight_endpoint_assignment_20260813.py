#!/usr/bin/env python3
"""Multi-terminal endpoint-flow diagnostic for all low compound seams.

Heavy runs belong on h100.  Instead of cancelling seam defects height by
height, it permits an arbitrary assignment of C_h sources to the old
non-U seam endpoints B_j and searches shortest moving-owner paths.
"""

from __future__ import annotations

import argparse
import itertools
import json

import audit_pbbs_portal_compound_coexistence_20260813 as co
import cpsat_relative_incidence_trade_compound_seam_20260813 as cp
import search_uniform_endpoint_rotation_paths_20260813 as one


def audit(m: int, d: int, heights: list[int]):
    _, old, _, _ = cp.old_factor_data(m)
    frozen = one.protected_facets(m, d)
    seams = []
    cs = []
    bs = []
    for h in heights:
        c = co.c_owner(m, h)
        u = co.height_owner(m, h + 1)
        f = c & u
        endpoints = old[f]
        assert u in endpoints, (m, h, "U is not an old seam endpoint")
        b = next(iter(endpoints - {u}))
        cs.append(c)
        bs.append(b)
        seams.append(f)
    blocked = set(seams) | frozen
    matrix = []
    paths = {}
    for i, c in enumerate(cs):
        line = []
        for j, b in enumerate(bs):
            p = one.shortest_path(m, old, blocked, c, b, None)
            paths[(i, j)] = p
            line.append(None if p is None else len(p))
        matrix.append(line)
    best = None
    for perm in itertools.permutations(range(len(heights))):
        if any(matrix[i][j] is None for i, j in enumerate(perm)):
            continue
        cost = sum(matrix[i][j] for i, j in enumerate(perm))
        # Distinct facet colours are mandatory across all paths.
        used = set()
        okay = True
        for i, j in enumerate(perm):
            fp = {x[1] for x in paths[(i, j)]}
            if used & fp:
                okay = False
                break
            used |= fp
        if okay and (best is None or cost < best[0]):
            best = (cost, perm, used)
    return {
        "m": m,
        "d": d,
        "heights": heights,
        "distance_matrix": matrix,
        "best": None if best is None else {
            "total_path_colours": best[0],
            "assignment": [[heights[i], heights[j]]
                           for i, j in enumerate(best[1])],
            "individual_lengths": [matrix[i][j]
                                   for i, j in enumerate(best[1])],
            "total_with_seams": best[0] + len(heights),
        },
    }


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
