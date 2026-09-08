#!/usr/bin/env python3
"""Verify the m=4 lower-complete A_occ=0 two-factor certificate.

Run on H100 only.  The certificate is deliberately compact: vertices are
9-bit masks and each inner list is one cyclic component.
"""

from __future__ import annotations

import itertools
from collections import Counter, defaultdict


M = 4
N = 9
CYCLES = [
    [45, 297, 300], [46, 78, 142], [57, 89, 153],
    [85, 337, 340], [101, 353, 356], [102, 106, 108],
    [105, 113, 120], [114, 354, 368], [149, 401, 404],
    [154, 394, 408], [166, 170, 172], [169, 177, 184],
    [198, 202, 204], [201, 209, 216], [210, 450, 464],
    [99, 225, 195, 163, 226], [116, 228, 212, 180, 240],
    [232, 360, 456, 424, 480],
    [60, 156, 396, 452, 332, 92, 344, 312],
    [15, 23, 29, 27, 281, 275, 306, 338, 402, 282, 278, 284, 270, 30],
    [39, 291, 305, 51, 43, 58, 90, 86, 150, 147, 83, 71, 326, 330,
     75, 139, 393, 329, 77, 197, 141, 269, 293, 325, 277, 389, 263,
     390, 135, 387, 418, 298, 267, 323, 449, 417, 420, 165, 53, 54,
     178, 432, 308, 294],
]


def pts(x):
    return tuple(i for i in range(N) if (x >> i) & 1)


def edge_set(cycles):
    return {
        tuple(sorted((cyc[i], cyc[(i + 1) % len(cyc)])))
        for cyc in cycles for i in range(len(cyc))
    }


def data(edges):
    loads = Counter()
    hs = defaultdict(set)
    for x, y in edges:
        assert (x ^ y).bit_count() == 2
        b = x & y
        loads[b] += 1
        px = (x ^ b).bit_length() - 1
        py = (y ^ b).bit_length() - 1
        hs[b].add(tuple(sorted((px, py))))
    return loads, hs


def occurrence_count(edges):
    loads, hs = data(edges)
    total = 0
    for bset, load in loads.items():
        if load < 2:
            continue
        for b in pts(bset):
            for u, v in hs[bset]:
                for p, a in ((u, v), (v, u)):
                    pset = (bset ^ (1 << b)) | (1 << p)
                    for x, y in hs[pset]:
                        if a not in (x, y):
                            continue
                        c = y if x == a else x
                        if c != b:
                            total += 1
    return total


def main():
    vertices = [sum(1 << x for x in c) for c in itertools.combinations(range(N), M)]
    flat = [x for cyc in CYCLES for x in cyc]
    assert sorted(flat) == sorted(vertices)
    assert all(len(cyc) >= 3 for cyc in CYCLES)
    edges = edge_set(CYCLES)
    assert len(edges) == len(vertices) == 126
    loads, hs = data(edges)
    lowers = [sum(1 << x for x in c) for c in itertools.combinations(range(N), M - 1)]
    assert set(loads) == set(lowers)
    assert sum(loads.values()) == 126
    assert occurrence_count(edges) == 0
    colour_cycles = []
    for r, redges in hs.items():
        adj = defaultdict(list)
        for x, y in redges:
            adj[x].append(y)
            adj[y].append(x)
        seen = set()
        for x in adj:
            if x in seen:
                continue
            stack = [x]
            vv = []
            degree_sum = 0
            while stack:
                u = stack.pop()
                if u in seen:
                    continue
                seen.add(u)
                vv.append(u)
                degree_sum += len(adj[u])
                stack.extend(adj[u])
            if degree_sum // 2 == len(vv):
                colour_cycles.append((r, tuple(sorted(vv))))
    assert sorted((pts(r), v) for r, v in colour_cycles) == [
        ((0, 3, 4), (5, 6, 7)),
        ((1, 2, 3), (5, 6, 7)),
    ]
    d = {r: loads[r] - 1 for r in lowers}
    assert sum(d.values()) == 42
    point = [sum(v for r, v in d.items() if (r >> z) & 1) for z in range(N)]
    assert point == [13, 14, 13, 13, 14, 18, 16, 14, 11]

    component = {x: i for i, cyc in enumerate(CYCLES) for x in cyc}
    all_johnson = {
        (x, y) for x in vertices for y in vertices
        if x < y and (x ^ y).bit_count() == 2
    }
    johnson_reconnections = 0
    lower_complete_reconnections = 0
    zero_occ_reconnections = 0
    edge_list = sorted(edges)
    for i, (u, v) in enumerate(edge_list):
        for x, y in edge_list[i + 1:]:
            if component[u] == component[x]:
                continue
            for a, b, c, e in ((u, x, v, y), (u, y, v, x)):
                g = tuple(sorted((a, b)))
                h = tuple(sorted((c, e)))
                if g not in all_johnson or h not in all_johnson:
                    continue
                if g == h or g in edges or h in edges:
                    continue
                johnson_reconnections += 1
                switched = (edges - {(u, v), (x, y)}) | {g, h}
                newloads, _ = data(switched)
                if set(newloads) != set(lowers):
                    continue
                lower_complete_reconnections += 1
                if occurrence_count(switched) == 0:
                    zero_occ_reconnections += 1
    assert johnson_reconnections == 335
    assert lower_complete_reconnections == 165
    assert zero_occ_reconnections == 0
    print(
        "PASS m=4 vertices=126 components=21 "
        f"lengths={','.join(map(str, sorted(map(len, CYCLES))))} "
        "lower_colours=84 surplus_mass=42 A_occ=0 "
        "colour_cycle_defects=2 "
        f"point_surplus={','.join(map(str, point))} "
        f"cross_component_johnson_reconnections={johnson_reconnections} "
        f"lower_complete_reconnections={lower_complete_reconnections} "
        "zero_occ_reconnections=0"
    )


if __name__ == "__main__":
    main()
