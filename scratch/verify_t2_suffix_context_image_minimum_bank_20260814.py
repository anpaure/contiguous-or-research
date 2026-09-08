#!/usr/bin/env python3
"""Verify frozen fresh minimum circuits on D4-to-D5 context-image banks.

Substantive execution belongs on H100.  This verifier rebuilds the exact
post-T2 factor, checks each frozen circuit and its q2 current, then reports
owner/colour resource conflicts among the thirteen ``10`` images and among
the thirteen primitive-wrap images.
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
    parser.add_argument("minimum_output")
    args = parser.parse_args()
    data = json.loads(Path(args.minimum_output).read_text(encoding="utf-8"))
    assert data["source_s"] == 4 and data["target_s"] == 5
    m, n = 11, 22
    post = base.canonical_edges(m)
    base.apply_t2(post, list(base.dyck_words(5)))
    by_owner, _ = base.factor_maps(post)
    loads = Counter(
        colours[0] | colours[1]
        for colours in by_owner.values() if len(colours) == 2
    )

    banks = defaultdict(list)
    individual = []
    for index, item in enumerate(data["reports"]):
        solution = item["solution"]
        assert solution is not None, item["image_suffix_edge"]
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
            and owner & ~old == 0
            and owner & ~new == 0
            and len(by_owner[owner]) == 2
            for owner, old, new in rows
        )
        _, losses, _ = base.q2_current(
            (owners, new_colours), by_owner, loads
        )
        assert not losses
        prefix = solution["prefix"]
        endpoint_a = base.bits(prefix) | (
            base.bits(item["image_suffix_edge"][0]) << 12
        )
        endpoint_b = base.bits(prefix) | (
            base.bits(item["image_suffix_edge"][1]) << 12
        )
        assert endpoint_a in owners and endpoint_b in owners
        banks[item["context"]].append({
            "index": index,
            "owners": set(owners),
            "colours": set(new_colours),
            "rows": rows,
        })
        individual.append({
            "index": index,
            "context": item["context"],
            "source_suffix_edge": item["source_suffix_edge"],
            "image_suffix_edge": item["image_suffix_edge"],
            "prefix": prefix,
            "incidence_length": 2 * len(owners),
            "q2_support_losses": 0,
        })

    bank_reports = {}
    for context, cycles in banks.items():
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
            colour: users for colour, users in colour_users.items()
            if len(users) > 1
        }
        conflict_pairs = {
            tuple(sorted((left, right)))
            for users in list(owner_conflicts.values()) + list(colour_conflicts.values())
            for position, left in enumerate(users)
            for right in users[position + 1:]
        }
        bank_reports[context] = {
            "cycles": len(cycles),
            "pairwise_owner_colour_disjoint": (
                not owner_conflicts and not colour_conflicts
            ),
            "owner_conflict_resources": len(owner_conflicts),
            "colour_conflict_resources": len(colour_conflicts),
            "conflicting_cycle_pairs": [list(pair) for pair in sorted(conflict_pairs)],
            "owner_conflict_witnesses": [
                {"resource": base.bitword(owner, n), "cycles": users}
                for owner, users in sorted(owner_conflicts.items())
            ],
            "colour_conflict_witnesses": [
                {"resource": base.bitword(colour, n), "cycles": users}
                for colour, users in sorted(colour_conflicts.items())
            ],
        }

    print(json.dumps({
        "status": "PASS",
        "individual": individual,
        "banks": bank_reports,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
