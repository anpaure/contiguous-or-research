#!/usr/bin/env python3
"""Topology and residence audit for the two T2 cross-suffix C16s.

Substantive execution belongs on h100.  Builds the complete lifted ML(17)
two-factor: current z-free incidence forest, canonical complemented return
forest, and fixed endpoint verticals.
"""

from __future__ import annotations

import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from search_t2_cross_suffix_alternating_cycles_20260813 import (  # noqa:E402
    T2,
    apply_t2,
    bits,
    bitword,
    canonical_edges,
    dyck_words,
    factor_maps,
)
from verify_t2_cross_suffix_c16_q2_safe_20260813 import explicit_cycle  # noqa:E402


def graph_components(edges):
    adj = defaultdict(list)
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    assert all(len(ns) == 2 for ns in adj.values()), Counter(map(len, adj.values()))
    seen = set()
    comps = []
    which = {}
    for start in adj:
        if start in seen:
            continue
        stack = [start]
        seen.add(start)
        vs = []
        while stack:
            u = stack.pop()
            which[u] = len(comps)
            vs.append(u)
            for v in adj[u]:
                if v not in seen:
                    seen.add(v)
                    stack.append(v)
        comps.append(vs)
    return comps, which


def path_endpoint_matching(selected):
    by_owner, by_colour = factor_maps(selected)
    adj = defaultdict(list)
    for o, c in selected:
        adj[(0, o)].append((1, c))
        adj[(1, c)].append((0, o))
    endpoints = [(0, o) for o, cs in by_owner.items() if len(cs) == 1]
    out = {}
    owner_to_pair = {}
    seen = set()
    for a in endpoints:
        if a in seen:
            continue
        prev = None
        cur = a
        owners = []
        while True:
            if cur[0] == 0:
                owners.append(cur[1])
            ns = [v for v in adj[cur] if v != prev]
            if not ns:
                break
            prev, cur = cur, ns[0]
        b = cur
        assert b[0] == 0 and b != a
        seen.add(a)
        seen.add(b)
        pair = tuple(sorted((a[1], b[1])))
        out[a[1]] = b[1]
        out[b[1]] = a[1]
        for o in owners:
            owner_to_pair[o] = pair
    return out, owner_to_pair


def matching_difference_cycles(m0, m1):
    changed = {v for v in m0 if m0[v] != m1[v]}
    out = []
    seen = set()
    for v in changed:
        if v in seen:
            continue
        cyc = []
        cur = v
        parity = 0
        while cur not in seen:
            seen.add(cur)
            cyc.append(cur)
            cur = (m0 if parity == 0 else m1)[cur]
            parity ^= 1
        out.append(cyc)
    return out


def lifted_edges(current, canonical, n_even):
    z = 1 << n_even
    mask = z - 1
    edges = []
    # Current z-free half.
    edges.extend((o, c) for o, c in current)
    # Fixed canonical complemented return half.
    edges.extend((z | (mask ^ c), z | (mask ^ o)) for o, c in canonical)
    canonical_by_owner, _ = factor_maps(canonical)
    endpoints = [o for o, cs in canonical_by_owner.items() if len(cs) == 1]
    edges.extend((o, z | o) for o in endpoints)
    return edges


def component_run_minimum(edges, n_total):
    adj = defaultdict(list)
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    seen = set()
    minimum = n_total + 1
    witness = None
    for start in adj:
        if start in seen:
            continue
        cyc = [start]
        prev = None
        cur = start
        while True:
            seen.add(cur)
            nxt = adj[cur][0] if adj[cur][0] != prev else adj[cur][1]
            if nxt == start:
                break
            cyc.append(nxt)
            prev, cur = cur, nxt
        # Owner chronology takes every other vertex; either parity works.
        owners = cyc[::2]
        if owners and owners[0].bit_count() != (n_total - 1) // 2:
            owners = cyc[1::2]
        L = len(owners)
        for x in range(n_total):
            word = [bool(o >> x & 1) for o in owners]
            if all(word) or not any(word):
                continue
            doubled = word + word
            i = 0
            while i < L:
                val = word[i]
                j = i + 1
                while j < i + L and doubled[j] == val:
                    j += 1
                run = j - i
                if run < minimum:
                    minimum = run
                    witness = {
                        "coordinate": x,
                        "run_value": int(val),
                        "run_length": run,
                        "component_owner_length": L,
                    }
                i = j
    return minimum, witness


def main():
    m = 8
    n = 16
    canonical = canonical_edges(m)
    suffixes = list(dyck_words(2))
    post_t2 = set(canonical)
    apply_t2(post_t2, suffixes)

    cycle_specs = [
        (4, {2, 5, 7, 9, 11, 12}),
        (6, {2, 5, 8, 9, 11, 12}),
    ]
    cycles = [explicit_cycle(core, b) for b, core in cycle_specs]

    base_matching, base_owner_path = path_endpoint_matching(post_t2)
    base_full, base_which = graph_components(lifted_edges(post_t2, canonical, n))
    results = []
    for mask in range(4):
        selected = set(post_t2)
        for i, cyc in enumerate(cycles):
            if not (mask >> i & 1):
                continue
            for owner, removed, added in cyc:
                assert (owner, removed) in selected
                assert (owner, added) not in selected
                selected.remove((owner, removed))
                selected.add((owner, added))

        matching, owner_path = path_endpoint_matching(selected)
        diffs = matching_difference_cycles(base_matching, matching)
        full_edges = lifted_edges(selected, canonical, n)
        comps, which = graph_components(full_edges)
        run_min, run_witness = component_run_minimum(full_edges, 17)

        target_rows = []
        for prefix in ("101001010101", "101001001101"):
            a = bits(prefix) | (bits("1100") << 12)
            b = bits(prefix) | (bits("1010") << 12)
            target_rows.append({
                "prefix": prefix,
                "same_full_component": which[a] == which[b],
                "component_a": which[a],
                "component_b": which[b],
                "path_endpoints_a": [bitword(x, n) for x in owner_path[a]],
                "path_endpoints_b": [bitword(x, n) for x in owner_path[b]],
            })

        results.append({
            "switch_mask": mask,
            "component_count": len(comps),
            "component_delta_from_post_t2": len(comps) - len(base_full),
            "component_size_hist": dict(sorted(Counter(len(c) for c in comps).items())),
            "changed_endpoint_pairs": sum(
                base_matching[v] != matching[v] for v in matching
            ) // 2,
            "matching_difference_cycles": [
                [bitword(v, n) for v in cyc] for cyc in diffs
            ],
            "targets": target_rows,
            "minimum_positive_or_zero_owner_run": run_min,
            "run_witness": run_witness,
        })

    print(json.dumps({
        "m": m,
        "canonical_components_expected": 1430,
        "post_t2_components": len(base_full),
        "results": results,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
