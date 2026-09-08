#!/usr/bin/env python3
"""Verify a resource-disjoint D5 split-tree actuator selection.

Substantive execution belongs on H100.  The verifier rebuilds the exact
post-T2 factor, checks all 41 frozen circuits and the suffix-label tree,
recomputes aggregate q2 support, traverses the simultaneous lifted
middle-level factor, and audits both projected q=2 residence collars.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import Counter, defaultdict, deque
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import search_t2_cross_suffix_alternating_cycles_20260813 as base  # noqa:E402
from audit_t2_cross_suffix_c16_full_ml_topology_20260813 import (  # noqa:E402
    graph_components,
    lifted_edges,
)
from verify_t2_c16_suffix_component_residence_20260813 import (  # noqa:E402
    seam_collar_report,
    toggle,
)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("selection")
    parser.add_argument("--require-spanning", action="store_true")
    args = parser.parse_args()
    raw = Path(args.selection).read_bytes()
    data = json.loads(raw)
    assert data["status"] == "SAT"
    assert len(data["selection"]) == 41

    m, n = 11, 22
    suffixes = list(base.dyck_words(5))
    canonical = base.canonical_edges(m)
    post = set(canonical)
    base.apply_t2(post, suffixes)
    by_owner, by_colour = base.factor_maps(post)
    loads = Counter(
        colours[0] | colours[1]
        for colours in by_owner.values() if len(colours) == 2
    )
    before_components, before_which = graph_components(
        lifted_edges(post, canonical, n)
    )

    suffix_adjacency = defaultdict(list)
    edge_keys = set()
    all_owners = set()
    all_colours = set()
    cycles = []
    q2_delta = Counter()
    individual_reports = []
    component_supports = []
    for item in data["selection"]:
        left, right = item["edge"]["suffix_edge"]
        key = tuple(sorted((left, right)))
        assert key not in edge_keys
        edge_keys.add(key)
        assert left in suffixes and right in suffixes
        assert (base.bits(left) ^ base.bits(right)).bit_count() == 2
        suffix_adjacency[left].append(right)
        suffix_adjacency[right].append(left)

        candidate = item["candidate"]
        owners = tuple(base.bits(word) for word in candidate["owners"])
        new_colours = tuple(
            base.bits(word) for word in candidate["new_colours"]
        )
        assert 2 * len(owners) == item["selected_incidence_length"]
        assert len(set(owners)) == len(owners)
        assert len(set(new_colours)) == len(new_colours)
        assert not all_owners & set(owners)
        assert not all_colours & set(new_colours)
        all_owners.update(owners)
        all_colours.update(new_colours)
        prefix = candidate["prefix"]
        endpoints = {
            base.bits(prefix) | (base.bits(word) << 12)
            for word in (left, right)
        }
        assert endpoints <= set(owners)

        rows = [
            (owners[index], new_colours[index - 1], new_colours[index])
            for index in range(len(owners))
        ]
        component_ids = set()
        upper_core = (1 << n) - 1
        lower_core = (1 << n) - 1
        lower_palette = Counter()
        removed_owner = {old: owner for owner, old, _ in rows}
        assert len(removed_owner) == len(rows)
        for owner, old, new in rows:
            assert (owner, old) in post
            assert (owner, new) not in post
            assert owner & ~old == 0 and owner & ~new == 0
            assert len(by_owner[owner]) == 2
            other = next(colour for colour in by_owner[owner] if colour != old)
            q2_delta[other | old] -= 1
            q2_delta[other | new] += 1
            component_ids.add(before_which[owner])
            upper_core &= other & old & new
            old_external = next(x for x in by_colour[old] if x != owner)
            assert owner not in by_colour[new]
            new_external = next(
                x for x in by_colour[new] if x != removed_owner[new]
            )
            lower_core &= owner & old_external & new_external
            lower_palette[owner & old_external] -= 1
            lower_palette[owner & new_external] += 1
        cycles.append(rows)
        component_supports.append(component_ids)
        individual_reports.append({
            "edge_index": item["edge_index"],
            "role": item["edge"]["role"],
            "split_pair": item["edge"]["split_pair"],
            "suffix_edge": [left, right],
            "prefix": prefix,
            "incidence_length": 2 * len(owners),
            "base_component_arity": len(component_ids),
            "upper_common_intersection_rank": upper_core.bit_count(),
            "lower_common_intersection_rank": lower_core.bit_count(),
            "lower_palette_losses": sum(
                -delta for delta in lower_palette.values() if delta < 0
            ),
            "lower_palette_births": sum(
                delta for delta in lower_palette.values() if delta > 0
            ),
        })

    assert len(edge_keys) == len(suffixes) - 1
    seen = {suffixes[0]}
    queue = deque(seen)
    while queue:
        word = queue.popleft()
        for other in suffix_adjacency[word]:
            if other not in seen:
                seen.add(other)
                queue.append(other)
    assert seen == set(suffixes)

    incidence_adjacency = defaultdict(set)
    for trade_index, support in enumerate(component_supports):
        trade = ("trade", trade_index)
        for component in support:
            vertex = ("component", component)
            incidence_adjacency[trade].add(vertex)
            incidence_adjacency[vertex].add(trade)
    incidence_seen = set()
    incidence_components = 0
    for start in incidence_adjacency:
        if start in incidence_seen:
            continue
        incidence_components += 1
        queue = deque([start])
        incidence_seen.add(start)
        while queue:
            vertex = queue.popleft()
            for other in incidence_adjacency[vertex]:
                if other not in incidence_seen:
                    incidence_seen.add(other)
                    queue.append(other)
    incidence_edges = sum(map(len, component_supports))
    incidence_vertices = len(incidence_adjacency)
    incidence_cycle_rank = (
        incidence_edges - incidence_vertices + incidence_components
    )

    q2_losses = [
        target for target, delta in q2_delta.items()
        if loads[target] and loads[target] + delta <= 0
    ]
    simultaneous = toggle(post, cycles)
    after_components, after_which = graph_components(
        lifted_edges(simultaneous, canonical, n)
    )
    touched_before = {
        before_which[owner] for rows in cycles for owner, _, _ in rows
    }
    touched_after = {
        after_which[owner] for rows in cycles for owner, _, _ in rows
    }
    suffix_outputs = {
        after_which[
            base.bits(item["candidate"]["prefix"])
            | (base.bits(word) << 12)
        ]
        for item in data["selection"]
        for word in item["edge"]["suffix_edge"]
    }

    changed_lower = {owner for rows in cycles for owner, _, _ in rows}
    added = {(owner, new) for rows in cycles for owner, _, new in rows}
    full_edges = lifted_edges(simultaneous, canonical, n)
    upper = seam_collar_report(
        full_edges,
        m + 1,
        lambda label, pair: label in changed_lower,
        n + 1,
    )
    lower = seam_collar_report(
        full_edges,
        m,
        lambda label, pair: any(
            colour == label and owner in pair for owner, colour in added
        ),
        n + 1,
    )
    upper_bad = [seam for seam in upper["seams"] if seam["collisions"]]
    lower_bad = [seam for seam in lower["seams"] if seam["collisions"]]
    spanning_gate = (
        not q2_losses
        and len(touched_after) == 1
        and len(suffix_outputs) == 1
        and len(before_components) - len(after_components)
        == len(touched_before) - 1
    )
    residence_gate = not upper_bad and not lower_bad

    report = {
        "status": "PASS" if spanning_gate else "DIAGNOSTIC_FAIL",
        "selection": str(args.selection),
        "selection_sha256": hashlib.sha256(raw).hexdigest(),
        "suffix_vertices": len(suffixes),
        "suffix_tree_edges": len(edge_keys),
        "owner_disjoint": True,
        "colour_disjoint": True,
        "selected_length_histogram": dict(sorted(Counter(
            item["selected_incidence_length"] for item in data["selection"]
        ).items())),
        "selected_prefix_histogram": dict(sorted(Counter(
            item["candidate"]["prefix"] for item in data["selection"]
        ).items())),
        "individual_actuators": individual_reports,
        "simultaneous": {
            "q2_support_losses": len(q2_losses),
            "minimum_q2_load_after": min(
                loads[target] + q2_delta[target] for target in loads
            ),
            "q2_negative_occurrences": sum(
                -delta for delta in q2_delta.values() if delta < 0
            ),
            "base_components_met": len(touched_before),
            "output_components_on_touched_owners": len(touched_after),
            "suffix_representative_output_components": len(suffix_outputs),
            "component_reduction": (
                len(before_components) - len(after_components)
            ),
            "component_trade_incidence_components": incidence_components,
            "component_trade_incidence_cycle_rank": incidence_cycle_rank,
            "component_trade_hypertree": (
                incidence_components == 1 and incidence_cycle_rank == 0
            ),
            "output_component_owner_lengths": sorted(
                len(after_components[component]) // 2
                for component in touched_after
            ),
            "upper_bad_2_collars": len(upper_bad),
            "lower_bad_2_collars": len(lower_bad),
            "minimum_upper_seam_gap": min(upper["seam_gaps"]),
            "minimum_lower_seam_gap": min(lower["seam_gaps"]),
            "spanning_gate": spanning_gate,
            "undilated_two_shore_residence_gate": residence_gate,
        },
    }
    print(json.dumps(report, indent=2, sort_keys=True))
    if args.require_spanning:
        assert spanning_gate


if __name__ == "__main__":
    main()
