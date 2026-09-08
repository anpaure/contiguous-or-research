#!/usr/bin/env python3
"""Inspect local U--L reassignment freedom inside each BTK forest component."""

import collections
import itertools
import sys

sys.setrecursionlimit(1000000)

from scratch_scd_double_turn import btk_chains, popcount


def components(r):
    n = 2 * r - 1
    edges = []
    for chain in btk_chains(n):
        at = {popcount(x): x for x in chain}
        if r + 1 not in at:
            continue
        hi, lo, mid = at[r + 1], at[r - 1], at[r]
        other = lo | ((hi ^ lo) ^ (mid ^ lo))
        edges.append((mid, other, lo, hi))
    graph = collections.defaultdict(list)
    for i, (a, b, _, _) in enumerate(edges):
        graph[a].append((b, i))
        graph[b].append((a, i))
    seen = set()
    ans = []
    for start in graph:
        if start in seen:
            continue
        stack = [start]
        seen.add(start)
        vertices, ids = [], set()
        while stack:
            a = stack.pop()
            vertices.append(a)
            for b, i in graph[a]:
                ids.add(i)
                if b not in seen:
                    seen.add(b)
                    stack.append(b)
        ans.append((vertices, [edges[i] for i in ids]))
    for owner in range(1 << n):
        if popcount(owner) == r and owner not in seen:
            ans.append(([owner], []))
    return ans


def owner_chain_data(r):
    n = 2 * r - 1
    result = {}
    for chain_id, chain in enumerate(btk_chains(n)):
        at = {popcount(x): x for x in chain}
        result[at[r]] = (chain_id, popcount(chain[0]), at[r - 1])
    return result


def permanent_count(matrix):
    n = len(matrix)
    dp = {0: 1}
    for row in matrix:
        ndp = collections.defaultdict(int)
        for used, count in dp.items():
            for j, ok in enumerate(row):
                if ok and not (used >> j) & 1:
                    ndp[used | (1 << j)] += count
        dp = ndp
    return dp.get((1 << n) - 1, 0)


def analyze(r):
    chain_data = owner_chain_data(r)
    stats = collections.Counter()
    examples = {}
    for vertices, edges in components(r):
        lowers = [e[2] for e in edges]
        uppers = [e[3] for e in edges]
        matrix = [[(l & u) == l for l in lowers] for u in uppers]
        matchings = permanent_count(matrix)
        matrix_internal = []
        vset = set(vertices)
        for u in uppers:
            row = []
            for l in lowers:
                diff = u ^ l
                mids = [u & ~(1 << x) for x in range(2 * r - 1) if (diff >> x) & 1]
                row.append((l & u) == l and set(mids) <= vset)
            matrix_internal.append(row)
        internal = permanent_count(matrix_internal)
        degree_shape = tuple(sorted((sum(a == x or b == x for a, b, _, _ in edges) for x in vertices), reverse=True))
        key = (len(edges), degree_shape, matchings, internal)
        stats[key] += 1
        examples.setdefault(key, (vertices, edges, matrix, matrix_internal))
    print(f"r={r} component types={len(stats)}")
    for key, count in stats.most_common():
        print(count, key)
    root_profiles = collections.Counter()
    bridge_profile = collections.Counter()
    comps = components(r)
    owner_to_component = {}
    for ci, (vertices, _) in enumerate(comps):
        for a in vertices:
            owner_to_component[a] = ci
    short = []
    for ci, (vertices, edges) in enumerate(comps):
        roots = [a for a in vertices if chain_data[a][1] == r - 1]
        assert len(roots) == 1
        root = roots[0]
        root_profiles[(len(edges), sum(root in (a, b) for a, b, _, _ in edges))] += 1
        lower = chain_data[root][2]
        touched = collections.Counter()
        for x in range(2 * r - 1):
            if not ((lower >> x) & 1):
                owner = lower | (1 << x)
                touched[owner_to_component.get(owner, -1)] += 1
        bridge_profile[(len(touched), tuple(sorted(touched.values(), reverse=True)))] += 1
        short.append((ci, root, lower, touched))
    print(" root degree by component edges", root_profiles)
    print(" unused lower component incidence", bridge_profile)
    # Component transition multigraph: a short-chain lower colour sends one
    # arc through each of its non-chain parents to that parent's sink.
    arcs = collections.Counter()
    undirected = collections.defaultdict(set)
    for ci, root, lower, touched in short:
        for x in range(2 * r - 1):
            if (lower >> x) & 1:
                continue
            owner = lower | (1 << x)
            cj = owner_to_component[owner]
            if cj != ci:
                arcs[(ci, cj)] += 1
                undirected[ci].add(cj)
                undirected[cj].add(ci)
    seen = set()
    cc_sizes = []
    for ci in range(len(comps)):
        if ci in seen:
            continue
        stack = [ci]
        seen.add(ci)
        size = 0
        while stack:
            x = stack.pop()
            size += 1
            for y in undirected[x]:
                if y not in seen:
                    seen.add(y)
                    stack.append(y)
        cc_sizes.append(size)
    print(
        " transition graph",
        "arcs", sum(arcs.values()),
        "distinct", len(arcs),
        "loops removed", len(short) * (r - 1) - sum(arcs.values()),
        "undirected cc", sorted(cc_sizes, reverse=True)[:10],
        "out distinct", collections.Counter(len({b for a, b in arcs if a == ci}) for ci in range(len(comps))),
        "symmetric", all(arcs[(b, a)] == multiplicity for (a, b), multiplicity in arcs.items()),
        "indeg", collections.Counter(sum(mult for (a, b), mult in arcs.items() if b == ci) for ci in range(len(comps))),
    )
    # Kosaraju SCC census.
    directed = collections.defaultdict(list)
    reverse = collections.defaultdict(list)
    for a, b in arcs:
        directed[a].append(b)
        reverse[b].append(a)
    visited = set()
    order = []
    def dfs(x):
        visited.add(x)
        for y in directed[x]:
            if y not in visited:
                dfs(y)
        order.append(x)
    for x in range(len(comps)):
        if x not in visited:
            dfs(x)
    visited.clear()
    scc = []
    def rdfs(x, bucket):
        visited.add(x)
        bucket.append(x)
        for y in reverse[x]:
            if y not in visited:
                rdfs(y, bucket)
    for x in reversed(order):
        if x not in visited:
            bucket = []
            rdfs(x, bucket)
            scc.append(bucket)
    print(" transition SCC", sorted(map(len, scc), reverse=True)[:20])


def main():
    hi = int(sys.argv[1]) if len(sys.argv) > 1 else 7
    for r in range(3, hi + 1):
        analyze(r)


if __name__ == "__main__":
    main()
