#!/usr/bin/env python3
"""Enumerate short q2-safe cross-suffix cycles and score topology/runs.

H100-only for substantive execution.
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
    combine_cycle,
    dyck_words,
    factor_maps,
    paths_to_target,
    q2_current,
)
from audit_t2_cross_suffix_c16_full_ml_topology_20260813 import (  # noqa:E402
    graph_components,
    lifted_edges,
    matching_difference_cycles,
    path_endpoint_matching,
)


def owner_cycles(edges, rank):
    adj = defaultdict(list)
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    seen = set()
    out = []
    for start in adj:
        if start in seen or start.bit_count() != rank:
            continue
        owners = []
        prev = None
        cur = start
        while True:
            seen.add(cur)
            owners.append(cur)
            colour = adj[cur][0] if adj[cur][0] != prev else adj[cur][1]
            seen.add(colour)
            nxt = adj[colour][0] if adj[colour][0] != cur else adj[colour][1]
            prev, cur = colour, nxt
            if cur == start:
                break
        out.append(owners)
    return out


def target_run_score(edges, targets, rank, prefix_coords):
    cycles = owner_cycles(edges, rank)
    where = {o: (cyc, i) for cyc in cycles for i, o in enumerate(cyc)}
    minimum = 10**9
    witness = None
    for target in targets:
        cyc, idx = where[target]
        n = len(cyc)
        for x in prefix_coords:
            val = bool(target >> x & 1)
            run = 1
            j = (idx - 1) % n
            while j != idx and bool(cyc[j] >> x & 1) == val:
                run += 1
                j = (j - 1) % n
            j = (idx + 1) % n
            while j != idx and bool(cyc[j] >> x & 1) == val:
                run += 1
                j = (j + 1) % n
            if run < minimum:
                minimum = run
                witness = (target, x, int(val), run, n)
    return minimum, witness


def main():
    m, n = 8, 16
    suffixes = list(dyck_words(2))
    canonical = canonical_edges(m)
    post = set(canonical)
    apply_t2(post, suffixes)
    by_owner, by_colour = factor_maps(post)
    internal = {o for o, cs in by_owner.items() if len(cs) == 2}
    globals_source = sys.modules[
        "search_t2_cross_suffix_alternating_cycles_20260813"
    ]
    globals_source.INTERNAL_OWNERS = internal
    loads = Counter(cs[0] | cs[1] for cs in by_owner.values() if len(cs) == 2)
    base_matching, _ = path_endpoint_matching(post)
    base_components, _ = graph_components(lifted_edges(post, canonical, n))

    reports = []
    for prefix in ("101001010101", "101001001101"):
        a = bits(prefix) | (bits("1100") << 12)
        b = bits(prefix) | (bits("1010") << 12)
        pab = paths_to_target(a, b, 5, n, post, by_colour, 1000000)
        pba = paths_to_target(b, a, 5, n, post, by_colour, 1000000)
        candidates = []
        seen = set()
        for p in pab:
            for q in pba:
                cycle = combine_cycle(p, q)
                if cycle is None:
                    continue
                owners, colours = cycle
                if len(owners) != 8:
                    continue
                key = tuple(owners)
                if key in seen:
                    continue
                seen.add(key)
                changes, losses, rows = q2_current(cycle, by_owner, loads)
                if losses:
                    continue
                selected = set(post)
                for o, removed, added, _, _ in rows:
                    selected.remove((o, removed))
                    selected.add((o, added))
                full_edges = lifted_edges(selected, canonical, n)
                comps, which = graph_components(full_edges)
                matching, _ = path_endpoint_matching(selected)
                diff = matching_difference_cycles(base_matching, matching)
                score, witness = target_run_score(
                    full_edges, (a, b), m, range(12)
                )
                candidates.append({
                    "target_run_score": score,
                    "run_witness": {
                        "target": bitword(witness[0], n),
                        "coordinate": witness[1],
                        "value": witness[2],
                        "run": witness[3],
                        "component_owner_length": witness[4],
                    },
                    "component_delta": len(comps) - len(base_components),
                    "targets_same_component": which[a] == which[b],
                    "endpoint_difference_cycle_lengths": [len(x) for x in diff],
                    "owners": [bitword(x, n) for x in owners],
                    "colours": [bitword(x, n) for x in colours],
                })
        candidates.sort(
            key=lambda x: (
                x["targets_same_component"],
                x["target_run_score"],
                -abs(x["component_delta"]),
            ),
            reverse=True,
        )
        reports.append({
            "prefix": prefix,
            "safe_c16_count": len(candidates),
            "score_hist": {
                str(k): v for k, v in sorted(Counter(
                    (x["targets_same_component"], x["target_run_score"], x["component_delta"])
                    for x in candidates
                ).items(), key=lambda kv: str(kv[0]))
            },
            "best": candidates[:20],
        })

    print(json.dumps({"m": m, "reports": reports}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
