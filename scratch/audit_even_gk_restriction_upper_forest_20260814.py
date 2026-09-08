#!/usr/bin/env python3
"""Restrict the even-dimensional GK two-sided rainbow forest to uppers avoiding z."""

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


def last_free_zero(x: int, n: int) -> int:
    st: list[int] = []
    paired: set[int] = set()
    for i in range(n):
        if (x >> i) & 1:
            st.append(i)
        elif st:
            paired.add(i)
            paired.add(st.pop())
    for i in range(n - 1, -1, -1):
        if not ((x >> i) & 1) and i not in paired:
            return i
    raise AssertionError("no free zero")


def audit(m: int, zpos: int) -> None:
    # Desired odd ground has 2m+1 points; embed it in even ground 2(m+1).
    n = 2 * m + 2
    M = m + 1
    z = zpos % n
    edges = []
    for s in masks(n, M - 1):
        p = last_free_zero(s, n)
        t = s | (1 << p)
        q = last_free_zero(t, n)
        u = t | (1 << q)
        tp = s | (1 << q)
        if not ((u >> z) & 1):
            edges.append((t, tp, s, u, p, q))

    upper = collections.Counter(u for _, _, _, u, _, _ in edges)
    lower = collections.Counter(s for _, _, s, _, _, _ in edges)
    deg = collections.Counter()
    adj: dict[int, list[int]] = collections.defaultdict(list)
    for i, (a, b, *_rest) in enumerate(edges):
        deg[a] += 1
        deg[b] += 1
        adj[a].append(i)
        adj[b].append(i)

    # Component/cycle census.
    seen: set[int] = set()
    comps = cycles = 0
    for v in deg:
        if v in seen:
            continue
        comps += 1
        stack = [v]
        nv = ne2 = 0
        while stack:
            w = stack.pop()
            if w in seen:
                continue
            seen.add(w)
            nv += 1
            ne2 += len(adj[w])
            for ei in adj[w]:
                a, b, *_ = edges[ei]
                stack.append(b if a == w else a)
        if ne2 // 2 >= nv:
            cycles += 1
    expected = sum(1 for u in masks(n, M + 1) if not ((u >> z) & 1))
    print({
        "m": m,
        "z": z,
        "edges": len(edges),
        "expected_uppers": expected,
        "upper_hist": sorted(collections.Counter(upper.values()).items()),
        "lower_max": max(lower.values(), default=0),
        "degree_hist": sorted(collections.Counter(deg.values()).items()),
        "max_degree": max(deg.values(), default=0),
        "components_on_used": comps,
        "cycles": cycles,
    })
    bad = [(a, deg[a]) for a in deg if deg[a] > 2]
    if bad:
        for a, d in bad[:5]:
            print("bad", format(a, f"0{n}b")[::-1], d,
                  [(format(edges[i][2], f"0{n}b")[::-1],
                    format(edges[i][3], f"0{n}b")[::-1], edges[i][4], edges[i][5])
                   for i in adj[a]])


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("m", type=int, nargs="+")
    ap.add_argument("--z", type=int, default=-1)
    args = ap.parse_args()
    for m in args.m:
        audit(m, args.z)
