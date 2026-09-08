#!/usr/bin/env python3
"""Enumerate shortest cross-suffix alternating cycles allowing owner endpoints.

Substantive execution belongs on h100.
"""

from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import search_t2_cross_suffix_alternating_cycles_20260813 as base  # noqa:E402
from audit_t2_cross_suffix_c16_full_ml_topology_20260813 import (  # noqa:E402
    graph_components,
    lifted_edges,
    matching_difference_cycles,
    path_endpoint_matching,
)
from search_t2_cross_suffix_safe_cycle_topology_residence_20260813 import (  # noqa:E402
    target_run_score,
)


def endpoint_q2_current(cycle, by_owner, loads):
    owners, new_colours = cycle
    changes = Counter()
    rows = []
    for i, owner in enumerate(owners):
        removed = new_colours[i - 1]
        added = new_colours[i]
        selected = by_owner[owner]
        assert removed in selected and added not in selected
        old_q2 = new_q2 = None
        if len(selected) == 2:
            other = selected[0] if selected[1] == removed else selected[1]
            old_q2 = other | removed
            new_q2 = other | added
            changes[old_q2] -= 1
            changes[new_q2] += 1
        else:
            assert len(selected) == 1
        rows.append((owner, removed, added, old_q2, new_q2))
    losses = [t for t, d in changes.items() if loads[t] + d == 0]
    return changes, losses, rows


def main():
    m, n = 8, 16
    suffixes = list(base.dyck_words(2))
    canonical = base.canonical_edges(m)
    post = set(canonical)
    base.apply_t2(post, suffixes)
    by_owner, by_colour = base.factor_maps(post)
    base.INTERNAL_OWNERS = set(by_owner)
    loads = Counter(cs[0] | cs[1] for cs in by_owner.values() if len(cs) == 2)
    base_matching, _ = path_endpoint_matching(post)
    base_components, _ = graph_components(lifted_edges(post, canonical, n))

    reports = []
    for prefix, _, _ in base.T2:
        a = base.bits(prefix) | (base.bits("1100") << 12)
        b = base.bits(prefix) | (base.bits("1010") << 12)
        # Unrestricted distances are at most 4 and 5; cap exactly there.
        pab = base.paths_to_target(a, b, 5, n, post, by_colour, 1000000)
        pba = base.paths_to_target(b, a, 5, n, post, by_colour, 1000000)
        raw_cycles = []
        for p in pab:
            for q in pba:
                cycle = base.combine_cycle(p, q)
                if cycle is not None:
                    raw_cycles.append(cycle)
        min_len = min(len(cycle[0]) for cycle in raw_cycles)
        candidates = []
        seen = set()
        for cycle in raw_cycles:
            if len(cycle[0]) != min_len:
                continue
            if tuple(cycle[0]) in seen:
                continue
            seen.add(tuple(cycle[0]))
            changes, losses, rows = endpoint_q2_current(cycle, by_owner, loads)
            if losses:
                continue
            selected = set(post)
            for owner, removed, added, _, _ in rows:
                selected.remove((owner, removed))
                selected.add((owner, added))
            full = lifted_edges(selected, canonical, n)
            comps, which = graph_components(full)
            matching, _ = path_endpoint_matching(selected)
            diff = matching_difference_cycles(base_matching, matching)
            score, witness = target_run_score(full, (a, b), m, range(12))
            candidates.append({
                "target_run_score": score,
                "run_witness": {
                    "target": base.bitword(witness[0], n),
                    "coordinate": witness[1],
                    "value": witness[2],
                    "run": witness[3],
                    "component_owner_length": witness[4],
                },
                "component_delta": len(comps) - len(base_components),
                "targets_same_component": which[a] == which[b],
                "endpoint_difference_cycle_lengths": [len(x) for x in diff],
                "endpoint_owner_count": sum(len(by_owner[o]) == 1 for o in cycle[0]),
                "owners": [base.bitword(o, n) for o in cycle[0]],
                "colours": [base.bitword(c, n) for c in cycle[1]],
            })
        candidates.sort(
            key=lambda x: (
                x["targets_same_component"], x["target_run_score"],
                -abs(x["component_delta"])
            ), reverse=True
        )
        reports.append({
            "prefix": prefix,
            "minimum_owner_cycle_length": min_len,
            "minimum_incidence_cycle_length": 2 * min_len,
            "q2_safe_minimum_cycle_count": len(candidates),
            "best": candidates[:30],
        })

    print(json.dumps({"m": m, "reports": reports}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
