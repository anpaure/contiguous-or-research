#!/usr/bin/env python3
"""Fixed common-history-state connectivity census for tight MSW rows.

Heavy runs belong on h100.  Vertices are oriented/shifted row states; edges
join transposition-adjacent Dyck roots having compatible d-history at those
fixed states.  We ask whether one can select one state per root and retain a
connected root graph, beginning with the sufficient star/one-coordinate
tests supplied here.
"""

from __future__ import annotations

import argparse
import collections
import json
import math

import audit_msw_common_history_upper_deck_20260813 as up
import audit_msw_inverse_trade_portal_shadow_20260813 as base


def audit(m):
    R = m + 1
    n = 2 * m + 1
    W = math.comb(n, R)
    half = 1 << (n - 1)
    d = 0
    while d * W + d * (d + 1) // 2 < half:
        d += 1
    roots = list(base.dyck_words(m))
    rows = [list(base.msw_row(root)) for root in roots]
    idx = {root: i for i, root in enumerate(roots)}
    trans = []
    for a, root in enumerate(roots):
        for p, x in enumerate(root):
            if x != "1":
                continue
            for q, y in enumerate(root):
                if y != "0":
                    continue
                z = list(root)
                z[p], z[q] = "0", "1"
                b = idx.get("".join(z))
                if b is not None and b > a:
                    trans.append((a, b))

    states = []
    for row in rows:
        ss = []
        for orient in (row, list(reversed(row))):
            for shift in range(n):
                ss.append(up.state(orient, shift, d, R))
        states.append(ss)

    state_graph = collections.defaultdict(set)
    root_state_degree = [collections.Counter() for _ in roots]
    for a, b in trans:
        for ia, sa in enumerate(states[a]):
            for ib, sb in enumerate(states[b]):
                if up.compatible(sa, sb):
                    va, vb = (a, ia), (b, ib)
                    state_graph[va].add(vb)
                    state_graph[vb].add(va)
                    root_state_degree[a][ia] += 1
                    root_state_degree[b][ib] += 1

    # Component/root coverage in the expanded fixed-state graph.
    seen = set()
    components = []
    for v in state_graph:
        if v in seen:
            continue
        seen.add(v)
        stack = [v]
        roots_seen = set()
        vertices = 0
        while stack:
            x = stack.pop()
            vertices += 1
            roots_seen.add(x[0])
            for y in state_graph[x]:
                if y not in seen:
                    seen.add(y)
                    stack.append(y)
        components.append((len(roots_seen), vertices))
    components.sort(reverse=True)

    return {
        "m": m,
        "d": d,
        "roots": len(roots),
        "states_per_root": 2 * n,
        "transposition_edges": len(trans),
        "active_fixed_states": len(state_graph),
        "expanded_components": len(components),
        "largest_component_root_coverage": components[0][0],
        "largest_component_state_vertices": components[0][1],
        "component_summary": components[:20],
        "roots_with_some_fixed_state_degree": sum(bool(x) for x in root_state_degree),
        "minimum_best_fixed_state_degree": min(max(x.values(), default=0)
                                               for x in root_state_degree),
        "maximum_best_fixed_state_degree": max(max(x.values(), default=0)
                                               for x in root_state_degree),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("m", type=int)
    ap.add_argument("--json")
    args = ap.parse_args()
    ans = audit(args.m)
    payload = json.dumps(ans, indent=2, sort_keys=True)
    print(payload)
    if args.json:
        with open(args.json, "w", encoding="utf-8") as f:
            f.write(payload + "\n")


if __name__ == "__main__":
    main()
