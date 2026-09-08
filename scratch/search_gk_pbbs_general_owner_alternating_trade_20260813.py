#!/usr/bin/env python3
"""Enumerate short owner-alternating surgeries through the rigid GK edge.

An order-t surgery replaces old factor edges (A_i,B_i) by the alternating
matching (A_i,B_(i+1)).  All owner degrees are therefore preserved.  We
require the multiset of rank-m intersections to be unchanged and require
global rank-(m+2) support after the surgery, but do not require the upper
multiset itself to be unchanged.  This strictly contains matching-cycle
switches and clean common-core packets.
"""

import argparse
from collections import Counter, defaultdict

from search_gk_pbbs_general_owner_c6_20260813 import components, johnson_neighbors
from search_gk_pbbs_palette_neutral_short_trade_20260813 import (
    complement_up, gk_up, masks, word,
)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('m', type=int)
    ap.add_argument('--half', type=int, default=4)
    ap.add_argument('--limit', type=int, default=20)
    args = ap.parse_args()
    m, n, half = args.m, 2 * args.m + 1, args.half
    assert half >= 2

    old_edges = []
    incident = defaultdict(list)
    upper_fibre = Counter()
    for lower in masks(n, m):
        a, b = gk_up(lower, n), complement_up(lower, n)
        edge = tuple(sorted((a, b)))
        i = len(old_edges)
        old_edges.append(edge)
        incident[a].append((i, b))
        incident[b].append((i, a))
        upper_fibre[a | b] += 1
    assert all(len(x) == 2 for x in incident.values())
    old_parts, old_part_of = components(old_edges)

    forced_upper = ((1 << (m + 2)) - 1) << (m - 1)
    roots = [i for i, e in enumerate(old_edges) if e[0] | e[1] == forced_upper]
    assert len(roots) == 1
    root = roots[0]
    root_edge = old_edges[root]

    neighbor_cache = {}
    def neighbors(x):
        if x not in neighbor_cache:
            neighbor_cache[x] = tuple(johnson_neighbors(x, n))
        return neighbor_cache[x]

    seen = set()
    accepted = []

    # path stores oriented old edges (left endpoint, right endpoint, index).
    def close_and_test(path, start_left):
        last_right = path[-1][1]
        if (last_right ^ start_left).bit_count() != 2:
            return
        old = tuple(sorted(tuple(sorted((a, b))) for a, b, _ in path))
        new_oriented = [(path[pos][1], path[(pos + 1) % half][0])
                        for pos in range(half)]
        new = tuple(sorted(tuple(sorted(e)) for e in new_oriented))
        key = (old, new)
        if key in seen:
            return
        seen.add(key)
        if Counter(a & b for a, b in old) != Counter(a & b for a, b in new):
            return
        old_upper = Counter(a | b for a, b in old)
        new_upper = Counter(a | b for a, b in new)
        for upper, count in old_upper.items():
            if upper_fibre[upper] == count and new_upper[upper] < count:
                return
        removed = {i for _, _, i in path}
        changed = [e for i, e in enumerate(old_edges) if i not in removed]
        changed.extend(new)
        new_parts, _ = components(changed)
        touched = sorted({old_part_of[x] for e in old for x in e})
        accepted.append((len(new_parts)-len(old_parts), touched, old, new,
                         old_upper == new_upper))

    def extend(path, used_edges, used_vertices, start_left):
        if len(path) == half:
            close_and_test(path, start_left)
            return
        current = path[-1][1]
        for left in neighbors(current):
            if left in used_vertices:
                continue
            for idx, right in incident[left]:
                if idx in used_edges or right in used_vertices:
                    continue
                used_edges.add(idx)
                used_vertices.add(left)
                used_vertices.add(right)
                path.append((left, right, idx))
                extend(path, used_edges, used_vertices, start_left)
                path.pop()
                used_vertices.remove(right)
                used_vertices.remove(left)
                used_edges.remove(idx)

    a0, b0 = root_edge
    for left0, right0 in ((a0, b0), (b0, a0)):
        path = [(left0, right0, root)]
        extend(path, {root}, {left0, right0}, left0)

    accepted.sort(key=lambda z: (z[0], -len(z[1]), not z[4], z[2], z[3]))
    print('SUMMARY', 'm', m, 'half', half, 'accepted', len(accepted),
          'component_delta_hist', dict(sorted(Counter(x[0] for x in accepted).items())),
          'old_component_count_hist', dict(sorted(Counter(len(x[1]) for x in accepted).items())),
          'upper_multiset_equal', sum(x[4] for x in accepted))
    for delta, touched, old, new, upper_equal in accepted[:args.limit]:
        print('TRADE', 'delta', delta,
              'old_components', [len(old_parts[i]) for i in touched],
              'upper_multiset_equal', upper_equal)
        for tag, edges in (('OLD', old), ('NEW', new)):
            for x, y in edges:
                extra = ''
                if tag == 'OLD':
                    pid = old_part_of[x]
                    extra = f' component={pid}:{len(old_parts[pid])}'
                print(' ', tag, word(x, n), word(y, n),
                      'L', word(x & y, n), 'U', word(x | y, n),
                      'mu', upper_fibre[x | y] if tag == 'OLD' else '-', extra)


if __name__ == '__main__':
    main()
