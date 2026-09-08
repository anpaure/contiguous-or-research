#!/usr/bin/env python3
"""Exact recurrent core for length-b GK macros with two reset sources.

Write a start queue as (P,R,S), |P|=b-2.  Follow b-2 strong GK
transitions, obtaining endpoint (R,S,F), |F|=b-2.  Two arbitrary FIFO
steps then produce the next start (F,R',S').  The two reset-source chains
may be discarded, costing at most 2H incidences per b-source macro.

This finite graph asks whether allowing two rather than one reset destroys
the polynomial recurrent-core obstruction.  Research-only; run on H100.
"""

from __future__ import annotations

from collections import Counter, defaultdict, deque
from itertools import permutations
from math import comb
import argparse


def additions(n: int, source: frozenset[int]) -> tuple[int, ...]:
    bits = [i in source for i in range(n)]
    stack: list[int] = []
    matched = [False] * n
    for i, bit in enumerate(bits):
        if bit:
            stack.append(i)
        elif stack:
            j = stack.pop()
            matched[i] = matched[j] = True
    return tuple(
        reversed([i for i in range(n) if not bits[i] and not matched[i]])
    )


def build(b: int, allow_duplicate_reset: bool):
    n = 2 * b
    add_cache = {}

    def aa(q):
        source = frozenset(q)
        if source not in add_cache:
            add_cache[source] = additions(n, source)
        return add_cache[source]

    def strong_step(q):
        add = aa(q)
        if not add:
            return None
        nxt = q[1:] + (add[0],)
        nxt_add = aa(nxt)
        common = min(len(nxt_add), max(0, len(add) - 1))
        if len(add) == 1 or (
            common > 0 and nxt_add[:common] == add[1 : 1 + common]
        ):
            return nxt
        return None

    starts = {}
    paths = []
    forced_blocks = []
    endpoints = []
    by_prefix = defaultdict(list)
    for q0 in permutations(range(n), b):
        q = q0
        path = [frozenset(q)]
        forced = []
        for _ in range(b - 2):
            add = aa(q)
            if not add:
                q = None
                break
            forced.append(add[0])
            q = strong_step(q)
            if q is None:
                break
            path.append(frozenset(q))
        if q is None:
            continue
        idx = len(paths)
        starts[q0] = idx
        paths.append(tuple(path))
        forced_blocks.append(tuple(forced))
        endpoints.append(q)
        by_prefix[q0[: b - 2]].append(idx)

    inverse = [None] * len(starts)
    for q, i in starts.items():
        inverse[i] = q

    adjacency = [[] for _ in paths]
    reverse = [[] for _ in paths]
    for i in range(len(paths)):
        endpoint = endpoints[i]
        old_r, old_s = endpoint[:2]
        forced = forced_blocks[i]
        mid_source = frozenset((old_s,) + forced)
        for j in by_prefix.get(forced, ()):
            qn = inverse[j]
            new_r, new_s = qn[-2:]
            # First reset appends new_r after dropping old_r.
            if new_r in mid_source:
                continue
            if not allow_duplicate_reset and new_r == old_r:
                continue
            second_source = frozenset(forced + (new_r,))
            # Second reset appends new_s after dropping old_s.
            if new_s in second_source:
                continue
            if not allow_duplicate_reset and new_s == old_s:
                continue
            adjacency[i].append(j)
            reverse[j].append(i)

    # Exact SCCs via iterative Kosaraju.
    seen = bytearray(len(paths))
    finish = []
    for root in range(len(paths)):
        if seen[root]:
            continue
        seen[root] = 1
        stack = [(root, 0)]
        while stack:
            v, at = stack[-1]
            if at < len(adjacency[v]):
                w = adjacency[v][at]
                stack[-1] = (v, at + 1)
                if not seen[w]:
                    seen[w] = 1
                    stack.append((w, 0))
            else:
                finish.append(v)
                stack.pop()
    comp = [-1] * len(paths)
    comp_sizes = []
    for root in reversed(finish):
        if comp[root] >= 0:
            continue
        cid = len(comp_sizes)
        size = 0
        comp[root] = cid
        stack = [root]
        while stack:
            v = stack.pop()
            size += 1
            for w in reverse[v]:
                if comp[w] < 0:
                    comp[w] = cid
                    stack.append(w)
        comp_sizes.append(size)
    cyclic_components = {
        cid for cid, size in enumerate(comp_sizes) if size > 1
    }
    for i, row in enumerate(adjacency):
        if i in row:
            cyclic_components.add(comp[i])
    core = [i for i in range(len(paths)) if comp[i] in cyclic_components]
    core_sources = set().union(*(set(paths[i]) for i in core)) if core else set()
    return {
        "b": b,
        "starts": len(starts),
        "arcs": sum(map(len, adjacency)),
        "core": len(core),
        "components": Counter(comp[i] for i in core),
        "core_sources": len(core_sources),
        "W": comb(2 * b, b),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-b", type=int, default=6)
    args = parser.parse_args()
    for allow in (True, False):
        print("ALLOW_DUPLICATE_RESET", allow)
        for b in range(2, args.max_b + 1):
            data = build(b, allow)
            print(
                "CASE",
                b,
                "STARTS",
                data["starts"],
                "ARCS",
                data["arcs"],
                "CORE",
                data["core"],
                "CYCLIC_COMPONENTS",
                len(data["components"]),
                "MAX_COMPONENT",
                max(data["components"].values(), default=0),
                "SOURCE_UNION",
                data["core_sources"],
                "W",
                data["W"],
                flush=True,
            )


if __name__ == "__main__":
    main()
