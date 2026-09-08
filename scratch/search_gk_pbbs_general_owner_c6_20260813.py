#!/usr/bin/env python3
"""Search owner-degree-neutral C6 surgeries through the rigid GK edge.

Unlike the matching-cycle search, this enumerates every alternating owner
C6 AB-CD-EF -> AC-DE-FB whose three old edges belong to the odd
GK/complement factor.  It requires only exact preservation of the three
lower intersection colours.  Upper colours need not be preserved as a
multiset; the global upper-support condition merely says that any removed
singleton upper colour is recreated by the three new edges.
"""

import argparse
import itertools
from collections import Counter, defaultdict

from search_gk_pbbs_palette_neutral_short_trade_20260813 import (
    complement_up, gk_up, masks, word,
)


def johnson_neighbors(x, n):
    ones = [i for i in range(n) if x & (1 << i)]
    zeros = [i for i in range(n) if not x & (1 << i)]
    for a in ones:
        for b in zeros:
            yield x ^ (1 << a) ^ (1 << b)


def colour(edge):
    a, b = edge
    return a & b, a | b


def components(edge_list):
    graph = defaultdict(list)
    for a, b in edge_list:
        graph[a].append(b)
        graph[b].append(a)
    parts = []
    part_of = {}
    for start in graph:
        if start in part_of:
            continue
        todo = [start]
        part = []
        part_id = len(parts)
        part_of[start] = part_id
        while todo:
            x = todo.pop()
            part.append(x)
            for y in graph[x]:
                if y not in part_of:
                    part_of[y] = part_id
                    todo.append(y)
        parts.append(part)
    return parts, part_of


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('m', type=int)
    ap.add_argument('--limit', type=int, default=20)
    args = ap.parse_args()
    m, n = args.m, 2 * args.m + 1

    old_edges = []
    edge_index = {}
    incident = defaultdict(list)
    upper_fibre = Counter()
    for lower in masks(n, m):
        a, b = gk_up(lower, n), complement_up(lower, n)
        edge = tuple(sorted((a, b)))
        i = len(old_edges)
        old_edges.append(edge)
        edge_index[edge] = i
        incident[a].append((i, b))
        incident[b].append((i, a))
        upper_fibre[a | b] += 1
    assert all(len(x) == 2 for x in incident.values())
    old_parts, old_part_of = components(old_edges)

    forced_upper = ((1 << (m + 2)) - 1) << (m - 1)
    roots = [i for i, e in enumerate(old_edges) if e[0] | e[1] == forced_upper]
    assert len(roots) == 1
    root = roots[0]
    A, B = old_edges[root]
    # Test both endpoint orientations; quotient by reversing the whole C6
    # only at output time via its unordered old/new edge sets.
    seen = set()
    found = []
    for A, B in ((A, B), (B, A)):
        for C in johnson_neighbors(A, n):
            for i1, D in incident[C]:
                if i1 == root or D in (A, B, C):
                    continue
                for E in johnson_neighbors(D, n):
                    for i2, F in incident[E]:
                        if i2 in (root, i1) or F in (A, B, C, D, E):
                            continue
                        if (F ^ B).bit_count() != 2:
                            continue
                        old = tuple(sorted((old_edges[root], old_edges[i1], old_edges[i2])))
                        new = tuple(sorted((tuple(sorted((A, C))),
                                            tuple(sorted((D, E))),
                                            tuple(sorted((F, B))))))
                        key = (old, new)
                        if key in seen:
                            continue
                        seen.add(key)
                        old_lower = Counter(x & y for x, y in old)
                        new_lower = Counter(x & y for x, y in new)
                        if old_lower != new_lower:
                            continue
                        old_upper = Counter(x | y for x, y in old)
                        new_upper = Counter(x | y for x, y in new)
                        lost = [u for u, count in old_upper.items()
                                if upper_fibre[u] == count and new_upper[u] < count]
                        if lost:
                            continue
                        # Component effect of the exact two-factor surgery.
                        removed = {root, i1, i2}
                        changed = [e for i, e in enumerate(old_edges) if i not in removed]
                        changed.extend(new)
                        new_parts, _ = components(changed)
                        touched = sorted({old_part_of[x] for e in old for x in e})
                        found.append((len(new_parts)-len(old_parts), touched, old, new,
                                      old_upper, new_upper))

    found.sort(key=lambda z: (z[0], -len(z[1]), z[2], z[3]))
    print('SUMMARY', 'm', m, 'candidates', len(found),
          'component_delta_hist', dict(sorted(Counter(x[0] for x in found).items())),
          'old_component_count_hist', dict(sorted(Counter(len(x[1]) for x in found).items())))
    for delta, touched, old, new, old_upper, new_upper in found[:args.limit]:
        print('C6', 'delta', delta,
              'old_components', [len(old_parts[i]) for i in touched],
              'upper_multiset_equal', old_upper == new_upper)
        for tag, edges in (('OLD', old), ('NEW', new)):
            for x, y in edges:
                print(' ', tag, word(x, n), word(y, n),
                      'L', word(x & y, n), 'U', word(x | y, n),
                      'mu', upper_fibre[x | y] if tag == 'OLD' else '-')


if __name__ == '__main__':
    main()
