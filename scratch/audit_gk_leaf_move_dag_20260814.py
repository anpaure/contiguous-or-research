#!/usr/bin/env python3
"""Audit the full directed graph of fixed-GK leaf moves.

Owners have weight m+1 on [2m+1].  The tails are precisely owners with
at least one unmatched zero in the linear 10 matching.  If p is the last
unmatched zero, an allowed move replaces a leaf one q (a free one or the
one in an adjacent 10 pair) by p.  We test whether the graph of *all* such
moves is acyclic and record exact SCC/cycle witnesses and useful rankings.
"""

from __future__ import annotations

import argparse
import collections
import itertools


def masks(n: int, r: int):
    for c in itertools.combinations(range(n), r):
        x = 0
        for i in c:
            x |= 1 << i
        yield x


def matching(x: int, n: int):
    stack: list[int] = []
    mate: dict[int, int] = {}
    for i in range(n):
        if (x >> i) & 1:
            stack.append(i)
        elif stack:
            j = stack.pop()
            mate[i] = j
            mate[j] = i
    free_zero = [i for i in range(n) if not ((x >> i) & 1) and i not in mate]
    free_one = [i for i in range(n) if ((x >> i) & 1) and i not in mate]
    return mate, free_zero, free_one


def rooted_word(x: int, n: int) -> tuple[int, ...]:
    """Rotate immediately after the last free zero; sinks use their word."""
    _, fz, _ = matching(x, n)
    if not fz:
        return tuple((x >> i) & 1 for i in range(n))
    p = fz[-1]
    return tuple((x >> ((p + 1 + j) % n)) & 1 for j in range(n))


def rankings(x: int, n: int):
    mate, fz, fo = matching(x, n)
    w = rooted_word(x, n)
    bal = 0
    area = 0
    sqarea = 0
    for bit in w:
        bal += 1 if bit else -1
        area += bal
        sqarea += bal * bal
    positions = tuple(i for i in range(n) if (x >> i) & 1)
    return {
        "free_zero_count": len(fz),
        "rooted_word": w,
        "rooted_area": area,
        "rooted_sqarea": sqarea,
        "positions": positions,
        "linear_sum": sum(positions),
        "free_one_count": len(fo),
    }


def audit(m: int) -> None:
    n = 2 * m + 1
    verts = list(masks(n, m + 1))
    idx = {x: i for i, x in enumerate(verts)}
    adj: list[list[int]] = [[] for _ in verts]
    edge_data: list[tuple[int, int, int, int, str]] = []
    for a in verts:
        mate, fz, fo = matching(a, n)
        if not fz:
            continue
        p = fz[-1]
        for q in range(n):
            if not ((a >> q) & 1):
                continue
            if q not in mate:
                kind = "free"
            elif mate[q] == q + 1:
                kind = "peak"
            else:
                continue
            b = a ^ (1 << p) ^ (1 << q)
            adj[idx[a]].append(idx[b])
            edge_data.append((a, b, p, q, kind))

    # Tarjan SCC.
    timer = 0
    st: list[int] = []
    on = [False] * len(verts)
    tin = [-1] * len(verts)
    low = [-1] * len(verts)
    comps: list[list[int]] = []

    def dfs(v: int) -> None:
        nonlocal timer
        tin[v] = low[v] = timer
        timer += 1
        st.append(v)
        on[v] = True
        for w in adj[v]:
            if tin[w] < 0:
                dfs(w)
                low[v] = min(low[v], low[w])
            elif on[w]:
                low[v] = min(low[v], tin[w])
        if low[v] == tin[v]:
            c: list[int] = []
            while True:
                w = st.pop()
                on[w] = False
                c.append(w)
                if w == v:
                    break
            comps.append(c)

    for v in range(len(verts)):
        if tin[v] < 0:
            dfs(v)
    nontrivial = [c for c in comps if len(c) > 1]

    keys = ["free_zero_count", "rooted_word", "rooted_area", "rooted_sqarea",
            "positions", "linear_sum", "free_one_count"]
    signs = {k: collections.Counter() for k in keys}
    examples: dict[tuple[str, int], tuple] = {}
    for a, b, p, q, kind in edge_data:
        ra, rb = rankings(a, n), rankings(b, n)
        for k in keys:
            d = (rb[k] > ra[k]) - (rb[k] < ra[k])
            signs[k][d] += 1
            examples.setdefault((k, d), (a, b, p, q, kind, ra[k], rb[k]))

    print({
        "m": m,
        "vertices": len(verts),
        "edges": len(edge_data),
        "sccs": len(comps),
        "nontrivial_sccs": len(nontrivial),
        "max_scc": max(map(len, comps)),
        "signs": {k: dict(v) for k, v in signs.items()},
    })
    if nontrivial:
        c = nontrivial[0]
        cset = set(c)
        print("scc_witness", [format(verts[v], f"0{n}b")[::-1] for v in c[:20]])
        for v in c:
            for w in adj[v]:
                if w in cset:
                    print("scc_edge", format(verts[v], f"0{n}b")[::-1],
                          format(verts[w], f"0{n}b")[::-1])
                    return
    for k in keys:
        if len(signs[k]) > 1:
            for d in sorted(signs[k]):
                print("ranking_example", k, d, examples[(k, d)])


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("m", type=int, nargs="+")
    args = ap.parse_args()
    for m in args.m:
        audit(m)
