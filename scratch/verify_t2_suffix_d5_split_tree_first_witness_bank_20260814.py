#!/usr/bin/env python3
"""Verify the 41 first q2-safe witnesses on the split-aware D5 suffix tree.

Substantive execution belongs on H100.  Twenty-six circuits come from the
frozen extreme-block reset output and fifteen from the middle/bridge output.
The verifier reconstructs every circuit in the exact post-T2 factor, checks
suffix-edge coverage and q2 support, and reports resource conflicts by
first-return role and split class.
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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("tree")
    parser.add_argument("extreme_minima")
    parser.add_argument("missing_minima")
    args = parser.parse_args()
    tree = json.loads(Path(args.tree).read_text(encoding="utf-8"))
    extreme = json.loads(Path(args.extreme_minima).read_text(encoding="utf-8"))
    missing = json.loads(Path(args.missing_minima).read_text(encoding="utf-8"))

    tree_by_edge = {
        tuple(sorted(item["suffix_edge"])): item
        for item in tree["tree_edges"]
    }
    source_rows = []
    for item in extreme["reports"]:
        key = tuple(sorted(item["image_suffix_edge"]))
        source_rows.append((key, item["solution"]))
    for item in missing["reports"]:
        key = tuple(sorted(item["suffix_edge"]))
        source_rows.append((key, item["solution"]))
    assert len(source_rows) == len(tree_by_edge) == 41
    assert {key for key, _ in source_rows} == set(tree_by_edge)

    m, n = 11, 22
    post = base.canonical_edges(m)
    base.apply_t2(post, list(base.dyck_words(5)))
    by_owner, _ = base.factor_maps(post)
    loads = Counter(
        colours[0] | colours[1]
        for colours in by_owner.values() if len(colours) == 2
    )

    cycles = []
    for index, (key, solution) in enumerate(source_rows):
        edge = tree_by_edge[key]
        owners = tuple(base.bits(word) for word in solution["owners"])
        new_colours = tuple(base.bits(word) for word in solution["new_colours"])
        rows = [
            (owners[i], new_colours[i - 1], new_colours[i])
            for i in range(len(owners))
        ]
        assert len(set(owners)) == len(owners)
        assert len(set(new_colours)) == len(new_colours)
        assert all(
            (owner, old) in post
            and (owner, new) not in post
            and len(by_owner[owner]) == 2
            for owner, old, new in rows
        )
        _, losses, _ = base.q2_current(
            (owners, new_colours), by_owner, loads
        )
        assert not losses
        prefix = solution["prefix"]
        endpoints = {
            base.bits(prefix) | (base.bits(word) << 12)
            for word in edge["suffix_edge"]
        }
        assert endpoints <= set(owners)
        cycles.append({
            "index": index,
            "edge": edge,
            "prefix": prefix,
            "incidence_length": 2 * len(owners),
            "owners": set(owners),
            "colours": set(new_colours),
        })

    owner_users = defaultdict(list)
    colour_users = defaultdict(list)
    for cycle in cycles:
        for owner in cycle["owners"]:
            owner_users[owner].append(cycle["index"])
        for colour in cycle["colours"]:
            colour_users[colour].append(cycle["index"])
    owner_conflicts = {
        owner: users for owner, users in owner_users.items() if len(users) > 1
    }
    colour_conflicts = {
        colour: users for colour, users in colour_users.items() if len(users) > 1
    }
    conflict_pairs = {
        tuple(sorted((left, right)))
        for users in list(owner_conflicts.values()) + list(colour_conflicts.values())
        for position, left in enumerate(users)
        for right in users[position + 1:]
    }

    pair_reports = []
    role_pair_histogram = Counter()
    split_pair_histogram = Counter()
    for left, right in sorted(conflict_pairs):
        a, b = cycles[left], cycles[right]
        role_pair = tuple(sorted((a["edge"]["role"], b["edge"]["role"])))
        split_a = tuple(tuple(x) for x in a["edge"]["split_pair"])
        split_b = tuple(tuple(x) for x in b["edge"]["split_pair"])
        split_pair = tuple(sorted((split_a, split_b)))
        role_pair_histogram[str(role_pair)] += 1
        split_pair_histogram[str(split_pair)] += 1
        pair_reports.append({
            "cycles": [left, right],
            "roles": [a["edge"]["role"], b["edge"]["role"]],
            "suffix_edges": [
                a["edge"]["suffix_edge"], b["edge"]["suffix_edge"]
            ],
            "shared_owners": len(a["owners"] & b["owners"]),
            "shared_colours": len(a["colours"] & b["colours"]),
        })

    print(json.dumps({
        "status": "PASS",
        "suffix_semilength": 5,
        "tree_edges": 41,
        "all_individually_q2_safe": True,
        "length_histogram": dict(sorted(Counter(
            cycle["incidence_length"] for cycle in cycles
        ).items())),
        "prefix_histogram": dict(sorted(Counter(
            cycle["prefix"] for cycle in cycles
        ).items())),
        "resource_conflicts": {
            "owner_resources": len(owner_conflicts),
            "colour_resources": len(colour_conflicts),
            "cycle_pairs": len(conflict_pairs),
            "role_pair_histogram": dict(sorted(role_pair_histogram.items())),
            "split_pair_histogram": dict(sorted(split_pair_histogram.items())),
            "pairs": pair_reports,
        },
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
