#!/usr/bin/env python3
"""All-height multi-terminal endpoint-flow diagnostic.

Heavy runs belong on h100.  Every compound seam contributes the two desired
owners C_h,U_{h+1} as sources and its two old factor endpoints as targets.
The owner-current equation permits arbitrary source-target pairing.  This
script searches shortest moving-owner paths and the exact minimum assignment;
it then reports colour overlaps in that assignment.
"""

from __future__ import annotations

import argparse
import collections
import functools
import json

import audit_pbbs_portal_compound_coexistence_20260813 as co
import cpsat_relative_incidence_trade_compound_seam_20260813 as cp
import search_uniform_endpoint_rotation_paths_20260813 as one


def build_incidence(old):
    inc = collections.defaultdict(list)
    for facet, edge in old.items():
        a, b = tuple(edge)
        inc[a].append((facet, b))
        inc[b].append((facet, a))
    return inc


def shortest_path(ground, inc, blocked, src, dst):
    queue = collections.deque([src])
    pred = {src: None}
    step = {}
    while queue:
        v = queue.popleft()
        if v == dst:
            break
        for facet, stationary in inc[v]:
            if facet in blocked:
                continue
            for x in ground - facet:
                w = facet | {x}
                if w in (v, stationary) or w in pred:
                    continue
                pred[w] = v
                step[w] = (facet, stationary)
                queue.append(w)
    if dst not in pred:
        return None
    ans = []
    w = dst
    while pred[w] is not None:
        v = pred[w]
        facet, stationary = step[w]
        ans.append((v, facet, stationary, w))
        w = v
    return ans[::-1]


def audit(m: int, d: int, heights: list[int]):
    _, old, _, _ = cp.old_factor_data(m)
    ground = frozenset(range(2 * m + 1))
    inc = build_incidence(old)
    frozen = one.protected_facets(m, d)
    seams = []
    sources = []
    targets = []
    source_labels = []
    target_labels = []
    for h in heights:
        c = co.c_owner(m, h)
        u = co.height_owner(m, h + 1)
        f = c & u
        seams.append(f)
        sources.extend((c, u))
        source_labels.extend(((h, "C"), (h, "U")))
        es = sorted(old[f], key=lambda x: tuple(sorted(x)))
        targets.extend(es)
        target_labels.extend(((h, "A"), (h, "B")))
    blocked = set(seams) | frozen
    paths = {}
    matrix = []
    for i, src in enumerate(sources):
        line = []
        for j, dst in enumerate(targets):
            p = shortest_path(ground, inc, blocked, src, dst)
            paths[(i, j)] = p
            line.append(None if p is None else len(p))
        matrix.append(line)

    n = len(sources)
    inf = 10**9

    @functools.lru_cache(None)
    def dp(i, mask):
        if i == n:
            return (0, ())
        best = (inf, ())
        for j in range(n):
            if mask >> j & 1 or matrix[i][j] is None:
                continue
            tail, perm = dp(i + 1, mask | (1 << j))
            cand = matrix[i][j] + tail
            if cand < best[0]:
                best = (cand, (j,) + perm)
        return best

    cost, perm = dp(0, 0)
    assert cost < inf
    used = {}
    conflicts = []
    for i, j in enumerate(perm):
        for step in paths[(i, j)]:
            f = step[1]
            if f in used:
                conflicts.append({"facet": sorted(f),
                                  "first": used[f], "second": i})
            else:
                used[f] = i
    return {
        "m": m,
        "d": d,
        "heights": heights,
        "terminal_count": n,
        "minimum_path_colours_relaxed": cost,
        "total_with_seams_relaxed": cost + len(heights),
        "assignment": [
            {"source": source_labels[i], "target": target_labels[j],
             "length": matrix[i][j]}
            for i, j in enumerate(perm)
        ],
        "chosen_path_colour_conflicts": conflicts,
        "distance_matrix": matrix,
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
