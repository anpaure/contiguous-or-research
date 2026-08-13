#!/usr/bin/env python3
"""Verify topology and compatibility of frozen context anchor repairs.

Substantive execution belongs on H100.  The input is a frozen output of
``search_t2_suffix_context_anchor_repairs_20260814.py``.  Every available
cycle is reconstructed independently; the verifier checks factor legality,
q2 support, individual lifted component action, and exact owner/colour
resource conflicts within each context image bank.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import search_t2_cross_suffix_alternating_cycles_20260813 as base  # noqa:E402
from audit_t2_cross_suffix_c16_full_ml_topology_20260813 import (  # noqa:E402
    graph_components,
    lifted_edges,
)
from verify_t2_c16_suffix_component_residence_20260813 import (  # noqa:E402
    toggle,
)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("repair_output")
    args = parser.parse_args()
    data = json.loads(Path(args.repair_output).read_text(encoding="utf-8"))
    source_s = data["source_s"]
    target_s = data["target_s"]
    m = 6 + target_s
    n = 2 * m
    canonical = base.canonical_edges(m)
    post = set(canonical)
    base.apply_t2(post, list(base.dyck_words(target_s)))
    by_owner, _ = base.factor_maps(post)
    loads = Counter(
        colours[0] | colours[1]
        for colours in by_owner.values() if len(colours) == 2
    )
    before_components, before_which = graph_components(
        lifted_edges(post, canonical, n)
    )

    reports = []
    cycles_by_context = defaultdict(list)
    for index, item in enumerate(data["reports"]):
        solution = item["solution"]
        if solution is None:
            reports.append({
                "index": index,
                "context": item["context"],
                "source_suffix_edge": item["source_suffix_edge"],
                "status": "NO_FROZEN_SOLUTION",
            })
            continue
        owners = tuple(base.bits(word) for word in solution["owners"])
        new_colours = tuple(
            base.bits(word) for word in solution["new_colours"]
        )
        rows = [
            (owners[i], new_colours[i - 1], new_colours[i])
            for i in range(len(owners))
        ]
        assert all(
            (owner, old) in post
            and (owner, new) not in post
            and len(by_owner[owner]) == 2
            and owner & ~old == 0
            and owner & ~new == 0
            for owner, old, new in rows
        )
        assert len(set(owners)) == len(owners)
        assert len(set(new_colours)) == len(new_colours)
        _, losses, _ = base.q2_current(
            (owners, new_colours), by_owner, loads
        )
        assert not losses

        toggled = toggle(post, [rows])
        after_components, after_which = graph_components(
            lifted_edges(toggled, canonical, n)
        )
        old_components = {before_which[owner] for owner in owners}
        new_components = {after_which[owner] for owner in owners}
        cycles_by_context[item["context"]].append({
            "index": index,
            "rows": rows,
            "owners": set(owners),
            "colours": set(new_colours),
            "source_suffix_edge": item["source_suffix_edge"],
            "mapped_suffix_edge": item["mapped_suffix_edge"],
        })
        reports.append({
            "index": index,
            "context": item["context"],
            "source_suffix_edge": item["source_suffix_edge"],
            "mapped_suffix_edge": item["mapped_suffix_edge"],
            "status": "PASS",
            "incidence_length": 2 * len(owners),
            "old_components_met": len(old_components),
            "new_components_on_touched_owners": len(new_components),
            "component_reduction": (
                len(before_components) - len(after_components)
            ),
            "new_component_owner_lengths": sorted(
                len(after_components[component]) // 2
                for component in new_components
            ),
        })

    bank_reports = {}
    for context, cycles in cycles_by_context.items():
        owner_users = defaultdict(list)
        colour_users = defaultdict(list)
        for cycle in cycles:
            for owner in cycle["owners"]:
                owner_users[owner].append(cycle["index"])
            for colour in cycle["colours"]:
                colour_users[colour].append(cycle["index"])
        owner_conflicts = {
            resource: users for resource, users in owner_users.items()
            if len(users) > 1
        }
        colour_conflicts = {
            resource: users for resource, users in colour_users.items()
            if len(users) > 1
        }
        conflict_pairs = {
            tuple(sorted((left, right)))
            for users in list(owner_conflicts.values()) + list(colour_conflicts.values())
            for position, left in enumerate(users)
            for right in users[position + 1:]
        }
        pairwise_disjoint = not owner_conflicts and not colour_conflicts
        simultaneous = None
        if pairwise_disjoint:
            all_rows = [cycle["rows"] for cycle in cycles]
            q2_delta = Counter()
            for rows in all_rows:
                for owner, old, new in rows:
                    other = next(colour for colour in by_owner[owner] if colour != old)
                    q2_delta[other | old] -= 1
                    q2_delta[other | new] += 1
            q2_losses = [
                target for target, delta in q2_delta.items()
                if loads[target] and loads[target] + delta == 0
            ]
            after = toggle(post, all_rows)
            after_components, after_which = graph_components(
                lifted_edges(after, canonical, n)
            )
            touched_before = {
                before_which[owner]
                for cycle in cycles for owner in cycle["owners"]
            }
            touched_after = {
                after_which[owner]
                for cycle in cycles for owner in cycle["owners"]
            }
            simultaneous = {
                "q2_support_losses": len(q2_losses),
                "old_components_met": len(touched_before),
                "output_components_on_touched_owners": len(touched_after),
                "component_reduction": (
                    len(before_components) - len(after_components)
                ),
                "output_component_owner_lengths": sorted(
                    len(after_components[component]) // 2
                    for component in touched_after
                ),
            }
        bank_reports[context] = {
            "available_cycles": len(cycles),
            "pairwise_owner_colour_disjoint": pairwise_disjoint,
            "owner_conflict_resources": len(owner_conflicts),
            "colour_conflict_resources": len(colour_conflicts),
            "conflicting_cycle_pairs": [list(pair) for pair in sorted(conflict_pairs)],
            "simultaneous": simultaneous,
        }

    print(json.dumps({
        "status": "PASS",
        "source_s": source_s,
        "target_s": target_s,
        "individual_cycles": reports,
        "banks": bank_reports,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
