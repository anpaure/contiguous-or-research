#!/usr/bin/env python3
"""Search a short endpoint-rotation circuit repairing the uniform seam-path hole.

Heavy runs belong on h100.  This is a diagnostic: it reconstructs the complete
first-aligned factor, uses the preferred shortest C4/U5 seam paths, enumerates
arcs whose new upper union is the unique lost target, and searches a short
return path closing a facet-distinct endpoint-rotation circuit.
"""

from __future__ import annotations

import argparse
import collections
import json

import audit_pbbs_portal_compound_coexistence_20260813 as co
import cpsat_relative_incidence_trade_compound_seam_20260813 as cp
import search_uniform_endpoint_rotation_paths_20260813 as ep


def arc_index(old):
    inc = collections.defaultdict(list)
    for facet, edge in old.items():
        upper = frozenset().union(*edge)
        for moving in edge:
            stationary = next(iter(edge - {moving}))
            inc[moving].append((facet, stationary, upper))
    return inc


def shortest_paths(inc, ground, src, dst, forbidden, max_depth, limit):
    """Enumerate up to limit simple labelled directed paths by breadth first."""
    out = []
    queue = collections.deque([(src, (), frozenset((src,)), frozenset())])
    while queue and len(out) < limit:
        vertex, path, seen_vertices, seen_facets = queue.popleft()
        if len(path) >= max_depth:
            continue
        for facet, stationary, old_upper in inc[vertex]:
            if facet in forbidden or facet in seen_facets:
                continue
            for x in ground - facet:
                nxt = facet | {x}
                if nxt in (vertex, stationary) or nxt in seen_vertices:
                    continue
                step = (vertex, facet, stationary, nxt, old_upper,
                        stationary | nxt)
                new_path = path + (step,)
                if nxt == dst:
                    out.append(new_path)
                    if len(out) >= limit:
                        break
                else:
                    queue.append((nxt, new_path, seen_vertices | {nxt},
                                  seen_facets | {facet}))
    return out


def changes_from_paths(old, seam_facet, seam_pair, paths):
    neg = {seam_facet: old[seam_facet]}
    pos = {seam_facet: seam_pair}
    for path in paths:
        for _v, facet, stationary, nxt, _ou, _nu in path:
            if facet in neg:
                raise ValueError("repeated facet")
            neg[facet] = old[facet]
            pos[facet] = frozenset((stationary, nxt))
    return neg, pos


def support_holes(loads, neg, pos):
    old_part = collections.Counter(frozenset().union(*e) for e in neg.values())
    new_part = collections.Counter(frozenset().union(*e) for e in pos.values())
    return {
        u: c for u, c in (old_part - new_part).items()
        if loads[u] - c < 1
    }


def serialize_step(step):
    v, f, p, w, ou, nu = step
    return {
        "from": sorted(v), "facet": sorted(f), "stationary": sorted(p),
        "to": sorted(w), "old_upper": sorted(ou), "new_upper": sorted(nu),
    }


def audit(m, d, max_depth, path_limit):
    _, old, loads, _ = cp.old_factor_data(m)
    ground = frozenset(range(2 * m + 1))
    frozen = ep.protected_facets(m, d)
    c4, u5 = co.c_owner(m, 4), co.height_owner(m, 5)
    seam_facet = c4 & u5
    seam_pair = frozenset((c4, u5))
    endpoints = sorted(old[seam_facet], key=lambda x: tuple(sorted(x)))

    # Prefer the assignment with the larger old extra on the C4 path; this is
    # the stable m>=9 shortest-path family in the diagnostic census.
    a, b = endpoints[::-1]
    p = ep.shortest_path(m, old, frozen, c4, a, seam_facet)
    q = ep.shortest_path(m, old, frozen, u5, b, seam_facet)
    main_neg, main_pos = changes_from_paths(
        old, seam_facet, seam_pair, (p, q)
    )
    main_holes = support_holes(loads, main_neg, main_pos)
    inc = arc_index(old)

    candidates = []
    main_facets = frozenset(main_neg)
    for hole in main_holes:
        # Any new edge with upper union ``hole`` has endpoints hole-{x},
        # hole-{y}; enumerate all old oriented arcs that can create it.
        for facet, edge in old.items():
            if facet in frozen or facet in main_facets:
                continue
            for moving in edge:
                stationary = next(iter(edge - {moving}))
                if not stationary <= hole:
                    continue
                for x in hole:
                    nxt = hole - {x}
                    if facet <= nxt and nxt not in (moving, stationary):
                        first = (moving, facet, stationary, nxt,
                                 stationary | moving, stationary | nxt)
                        assert first[-1] == hole
                        forbidden = frozen | main_facets | {facet}
                        returns = shortest_paths(
                            inc, ground, nxt, moving, forbidden,
                            max_depth, path_limit,
                        )
                        for ret in returns:
                            try:
                                neg, pos = changes_from_paths(
                                    old, seam_facet, seam_pair,
                                    (p, q, (first,) + ret),
                                )
                            except ValueError:
                                continue
                            holes = support_holes(loads, neg, pos)
                            candidates.append({
                                "repaired_target": sorted(hole),
                                "repair_length": 1 + len(ret),
                                "remaining_holes": [sorted(x) for x in holes],
                                "repair": [serialize_step(first)]
                                          + [serialize_step(x) for x in ret],
                            })
                            if not holes:
                                return {
                                    "m": m, "d": d,
                                    "main_changed": len(main_neg),
                                    "main_holes": [sorted(x) for x in main_holes],
                                    "support_monotone": candidates[-1],
                                    "tested_candidates": len(candidates),
                                }
    candidates.sort(key=lambda x: (len(x["remaining_holes"]),
                                   x["repair_length"]))
    return {
        "m": m, "d": d,
        "main_changed": len(main_neg),
        "main_holes": [sorted(x) for x in main_holes],
        "support_monotone": None,
        "tested_candidates": len(candidates),
        "best": candidates[:20],
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pairs", nargs="+", help="m:d")
    ap.add_argument("--max-depth", type=int, default=5)
    ap.add_argument("--path-limit", type=int, default=100)
    ap.add_argument("--json")
    args = ap.parse_args()
    result = [audit(*map(int, x.split(":")), args.max_depth,
                    args.path_limit) for x in args.pairs]
    payload = json.dumps(result, indent=2, sort_keys=True)
    print(payload)
    if args.json:
        with open(args.json, "w", encoding="utf-8") as f:
            f.write(payload + "\n")


if __name__ == "__main__":
    main()
