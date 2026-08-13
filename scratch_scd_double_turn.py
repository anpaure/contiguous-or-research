#!/usr/bin/env python3
"""Test the BTK symmetric-chain two-step map as a double-colour forest."""

import collections
import sys


def btk_chains(n):
    chains = [[0]]
    for x in range(n):
        bit = 1 << x
        nxt = []
        for chain in chains:
            nxt.append(chain + [chain[-1] | bit])
            if len(chain) >= 2:
                nxt.append([a | bit for a in chain[:-1]])
        chains = nxt
    return chains


def popcount(x):
    return x.bit_count()


def analyze(r):
    n = 2 * r - 1
    edges = []
    seen_lo = set()
    seen_hi = set()
    for chain in btk_chains(n):
        at = {popcount(x): x for x in chain}
        if r + 1 not in at:
            continue
        hi = at[r + 1]
        lo = at[r - 1]
        mid = at[r]
        diff = hi ^ lo
        assert popcount(diff) == 2
        other = lo | (diff ^ (mid ^ lo))
        assert popcount(other) == r
        assert (mid & other) == lo and (mid | other) == hi
        assert lo not in seen_lo and hi not in seen_hi
        seen_lo.add(lo)
        seen_hi.add(hi)
        edges.append((mid, other, lo, hi))

    graph = collections.defaultdict(list)
    for i, (a, b, _, _) in enumerate(edges):
        graph[a].append((b, i))
        graph[b].append((a, i))
    degree_hist = collections.Counter(map(len, graph.values()))
    used = set()
    components = 0
    cycles = 0
    sizes = []
    shapes = collections.Counter()
    for start in graph:
        if start in used:
            continue
        components += 1
        stack = [start]
        used.add(start)
        vertices = 0
        edge_twice = 0
        while stack:
            v = stack.pop()
            vertices += 1
            edge_twice += len(graph[v])
            for w, _ in graph[v]:
                if w not in used:
                    used.add(w)
                    stack.append(w)
        ecount = edge_twice // 2
        cycles += ecount - vertices + 1
        sizes.append((vertices, ecount))
        component_vertices = [v for v in used if False]  # shape is collected below in a second pass
    total_owners = sum(1 for x in range(1 << n) if popcount(x) == r)
    isolates = total_owners - len(graph)
    seen2 = set()
    for start in graph:
        if start in seen2:
            continue
        stack = [start]
        seen2.add(start)
        degrees = []
        while stack:
            v = stack.pop()
            degrees.append(len(graph[v]))
            for w, _ in graph[v]:
                if w not in seen2:
                    seen2.add(w)
                    stack.append(w)
        shapes[tuple(sorted(degrees, reverse=True))] += 1
    print(
        f"r={r} n={n} edges={len(edges)} used={len(graph)} isolates={isolates} "
        f"components_noniso={components} cycle_rank={cycles} maxdeg={max(degree_hist, default=0)} "
        f"degrees={dict(sorted(degree_hist.items()))} sizes={sorted(sizes, reverse=True)[:8]} "
        f"shapes={shapes.most_common(12)}"
    )


def main():
    hi = int(sys.argv[1]) if len(sys.argv) > 1 else 8
    for r in range(2, hi + 1):
        analyze(r)


if __name__ == "__main__":
    main()
