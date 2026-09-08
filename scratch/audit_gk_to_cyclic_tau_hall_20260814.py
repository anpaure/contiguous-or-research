#!/usr/bin/env python3
"""Hall audit for fixed GK first endpoints against cyclic tau pairs."""

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


def first_free_one(x: int, n: int) -> int:
    stack = []
    paired = set()
    for i in range(n):
        if (x >> i) & 1:
            stack.append(i)
        elif stack:
            paired.add(i)
            paired.add(stack.pop())
    return next(i for i in range(n) if ((x >> i) & 1) and i not in paired)


def cyclic_unmatched_zero(x: int, n: int) -> int:
    # Literal cyclic 01 cancellation on a linked circular list.
    nxt = [(i + 1) % n for i in range(n)]
    prv = [(i - 1) % n for i in range(n)]
    alive = [True] * n
    remaining = n
    changed = True
    while changed and remaining > 1:
        changed = False
        i = next(j for j in range(n) if alive[j])
        seen = 0
        while seen < remaining:
            j = nxt[i]
            if ((x >> i) & 1) == 0 and ((x >> j) & 1) == 1:
                a, b = prv[i], nxt[j]
                nxt[a] = b
                prv[b] = a
                alive[i] = alive[j] = False
                remaining -= 2
                changed = True
                break
            i = j
            seen += 1
    survivors = [i for i in range(n) if alive[i]]
    assert len(survivors) == 1 and ((x >> survivors[0]) & 1) == 0, (x, survivors)
    return survivors[0]


def hopcroft_karp(adj: list[list[int]], nr: int):
    nl = len(adj)
    ml = [-1] * nl
    mr = [-1] * nr
    inf = nl + nr + 1
    while True:
        dist = [inf] * nl
        q = collections.deque()
        for u in range(nl):
            if ml[u] < 0:
                dist[u] = 0
                q.append(u)
        found = False
        while q:
            u = q.popleft()
            for v in adj[u]:
                w = mr[v]
                if w < 0:
                    found = True
                elif dist[w] == inf:
                    dist[w] = dist[u] + 1
                    q.append(w)
        if not found:
            break
        def dfs(u: int) -> bool:
            for v in adj[u]:
                w = mr[v]
                if w < 0 or (dist[w] == dist[u] + 1 and dfs(w)):
                    ml[u] = v
                    mr[v] = u
                    return True
            dist[u] = inf
            return False
        for u in range(nl):
            if ml[u] < 0:
                dfs(u)
    return ml, mr


def linear_unmatched(mask: int, order: list[int]) -> list[int]:
    stack = []
    paired = set()
    for i in order:
        if (mask >> i) & 1:
            stack.append(i)
        elif stack:
            paired.add(i)
            paired.add(stack.pop())
    return [i for i in order if i not in paired]


def audit(m: int, mode: str) -> None:
    n = 2 * m + 1
    lower_list = list(masks(n, m))
    lower_id = {x: i for i, x in enumerate(lower_list)}
    if mode == "cyclic":
        tau_adders = [{x: cyclic_unmatched_zero(x, n) for x in lower_list}]
        labels = ["cyclic"]
    else:
        tau_adders = []
        labels = []
        for direction in (1, -1):
            for delta in range(n):
                order = [(delta + direction * j) % n for j in range(n)]
                for endpoint in (0, -1):
                    add = {}
                    for x in lower_list:
                        zeros = [i for i in linear_unmatched(x, order) if not ((x >> i) & 1)]
                        add[x] = zeros[endpoint]
                    # Retain only actual bijections lower -> owner.
                    if len({x | (1 << add[x]) for x in lower_list}) == len(lower_list):
                        tau_adders.append(add)
                        labels.append(f"lin_dir{direction}_delta{delta}_end{endpoint}")
    left = []
    a_seen = set()
    for upper in masks(n, m + 2):
        p = first_free_one(upper, n)
        a = upper ^ (1 << p)
        assert a not in a_seen
        a_seen.add(a)
        left.append((upper, a, p))
    for label, z in zip(labels, tau_adders):
        adj = []
        for upper, a, p in left:
            ns = []
            for q in range(n):
                if (a >> q) & 1:
                    lower = a ^ (1 << q)
                    if z[lower] == p:
                        ns.append(lower_id[lower])
            adj.append(ns)
        ml, mr = hopcroft_karp(adj, len(lower_list))
        hist = sorted(collections.Counter(map(len, adj)).items())
        print("m", m, "tau", label, "left", len(left), "right", len(lower_list),
              "matched", sum(v >= 0 for v in ml), "degree_hist", hist,
              "zero_first", next((left[i] for i, ns in enumerate(adj) if not ns), None))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("m", nargs="+", type=int)
    ap.add_argument("--mode", choices=("cyclic", "linear"), default="cyclic")
    args = ap.parse_args()
    for m in args.m:
        audit(m, args.mode)
