#!/usr/bin/env python3
"""Try to fuse a certified A_occ=0 Johnson 2-factor into one cycle.

Run on H100 only.  Every accepted two-edge switch preserves degree two,
lower completeness, and the exact mixed-occurrence zero predicate.
"""

from __future__ import annotations

import argparse
import itertools
import json
import random
from collections import Counter, defaultdict


def mask_of(xs):
    return sum(1 << x for x in xs)


def points(x, n):
    return [i for i in range(n) if (x >> i) & 1]


def build(m):
    n = 2 * m + 1
    verts = [mask_of(c) for c in itertools.combinations(range(n), m)]
    lowers = [mask_of(c) for c in itertools.combinations(range(n), m - 1)]
    edges = []
    eid = {}
    color = []
    for i, x in enumerate(verts):
        for y in verts[i + 1:]:
            if (x ^ y).bit_count() == 2:
                eid[(x, y)] = eid[(y, x)] = len(edges)
                edges.append((x, y))
                color.append(x & y)
    mates = defaultdict(int)
    for B in lowers:
        inside = points(B, n)
        outside = [x for x in range(n) if not ((B >> x) & 1)]
        for b in inside:
            for p in outside:
                for a in outside:
                    if p == a:
                        continue
                    e1 = eid[(B | (1 << p), B | (1 << a))]
                    P = (B ^ (1 << b)) | (1 << p)
                    for c in outside:
                        if c in (p, a):
                            continue
                        e2 = eid[(P | (1 << a), P | (1 << c))]
                        mates[(B, e1)] |= 1 << e2
    return n, verts, lowers, edges, eid, color, mates


def components(edges, selected_ids):
    adj = defaultdict(list)
    for e in selected_ids:
        x, y = edges[e]
        adj[x].append(y)
        adj[y].append(x)
    comp = {}
    groups = []
    for x in adj:
        if x in comp:
            continue
        cid = len(groups)
        stack = [x]
        group = []
        while stack:
            u = stack.pop()
            if u in comp:
                continue
            comp[u] = cid
            group.append(u)
            stack.extend(adj[u])
        groups.append(group)
    return comp, groups


def valid_zero(mask, loads, selected_ids, color, mates):
    for e in selected_ids:
        B = color[e]
        if loads[B] >= 2 and mates[(B, e)] & mask:
            return False
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--output", required=True)
    ap.add_argument("--seed", type=int, default=20260814)
    ap.add_argument("--rounds", type=int, default=100)
    args = ap.parse_args()
    rng = random.Random(args.seed)
    data = json.load(open(args.input, encoding="utf-8"))
    m = data["m"]
    n, verts, lowers, edges, eid, color, mates = build(m)
    initial = {eid[(mask_of(x), mask_of(y))] for x, y in data["selected_edges"]}

    best = set(initial)
    best_groups = components(edges, best)[1]
    for round_no in range(args.rounds):
        state = set(best if round_no == 0 else initial)
        while True:
            comp, groups = components(edges, state)
            if len(groups) < len(best_groups):
                best = set(state)
                best_groups = groups
                print(f"BEST components={len(groups)} lengths={sorted(map(len, groups))}", flush=True)
            if len(groups) == 1:
                break
            loads = Counter(color[e] for e in state)
            mask = sum(1 << e for e in state)
            pairs = [(e, f) for e in state for f in state
                     if e < f and comp[edges[e][0]] != comp[edges[f][0]]]
            rng.shuffle(pairs)
            moved = False
            for e, f in pairs:
                u, v = edges[e]
                x, y = edges[f]
                options = [(u, x, v, y), (u, y, v, x)]
                rng.shuffle(options)
                for a, b, c, d in options:
                    if (a, b) not in eid or (c, d) not in eid:
                        continue
                    g, h = eid[(a, b)], eid[(c, d)]
                    if g == h or g in state or h in state:
                        continue
                    newloads = loads.copy()
                    newloads[color[e]] -= 1
                    newloads[color[f]] -= 1
                    newloads[color[g]] += 1
                    newloads[color[h]] += 1
                    if newloads[color[e]] < 1 or newloads[color[f]] < 1:
                        continue
                    newstate = (state - {e, f}) | {g, h}
                    newmask = mask ^ (1 << e) ^ (1 << f) ^ (1 << g) ^ (1 << h)
                    if not valid_zero(newmask, newloads, newstate, color, mates):
                        continue
                    state = newstate
                    moved = True
                    break
                if moved:
                    break
            if not moved:
                break
        if len(best_groups) == 1:
            break

    result = {
        "m": m,
        "n": n,
        "components": len(best_groups),
        "component_lengths": sorted(map(len, best_groups)),
        "selected_edges": [[points(edges[e][0], n), points(edges[e][1], n)] for e in sorted(best)],
    }
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, sort_keys=True)
        f.write("\n")
    print(json.dumps({k: v for k, v in result.items() if k != "selected_edges"}, sort_keys=True))


if __name__ == "__main__":
    main()
