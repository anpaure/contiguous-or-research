#!/usr/bin/env python3
"""Replay an allowed-row emit-all catalogue from the targeted q4 generator."""

from __future__ import annotations

import argparse
import csv
import json

from search_q4_k17_z17_quotient_exact_cover_20260814 import (
    canonical_orbit_mask,
    deck_masks,
    owner_orbits,
)
from search_q4_k17_z17_reflection_fixed_face_kissat_20260814 import (
    read_instance,
)
from search_q4_k17_z17_reflection_invariant_owner_cover_20260814 import (
    reflection_action,
)


FIELDS = ["rows", "core", "order", "owner_ids", "status"]


def integers(value):
    return tuple(map(int, value.split(","))) if value else ()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--instance", required=True)
    parser.add_argument("--allowed-rows", required=True)
    parser.add_argument("--target-row", required=True, type=int)
    parser.add_argument("--report", required=True)
    parser.add_argument("--catalog", required=True)
    args = parser.parse_args()

    with open(args.allowed_rows, encoding="ascii") as stream:
        allowed = {int(value) for value in stream.read().split()}
    assert args.target_row in allowed
    assert all(0 <= row < 680 for row in allowed)

    with open(args.report, encoding="ascii") as stream:
        report = json.load(stream)
    assert report["status"] == "PASS"
    assert report["target_row"] == args.target_row
    assert report["allowed_filter"] == args.allowed_rows
    assert report["catalogue"] == args.catalog

    _, _, _, pair_options = read_instance(args.instance)
    existing = {tuple(sorted(map(int, rows))) for rows in pair_options}
    assert len(existing) == len(pair_options)

    representatives, orbit_index = owner_orbits()
    reflection = reflection_action(representatives, orbit_index)
    nonfixed = [owner for owner in range(1430) if owner < reflection[owner]]
    assert len(nonfixed) == 680
    reduced = {}
    for row, owner in enumerate(nonfixed):
        reduced[owner] = reduced[reflection[owner]] = row

    with open(args.catalog, newline="", encoding="ascii") as stream:
        reader = csv.DictReader(stream, delimiter="\t")
        assert reader.fieldnames == FIELDS
        records = list(reader)

    masks = set()
    status_counts = {"new": 0, "existing": 0}
    for record in records:
        rows = integers(record["rows"])
        core = integers(record["core"])
        order = integers(record["order"])
        owner_ids = integers(record["owner_ids"])
        assert len(rows) == len(set(rows)) == 10
        assert rows == tuple(sorted(rows))
        assert args.target_row in rows and set(rows) <= allowed
        assert rows not in masks
        masks.add(rows)

        assert len(core) == len(set(core)) == 5
        assert len(order) == len(set(order)) == 10
        assert not (set(core) & set(order))
        owners = deck_masks(core, order)
        replay_ids = tuple(
            orbit_index[canonical_orbit_mask(owner)] for owner in owners
        )
        assert replay_ids == owner_ids
        assert len(owner_ids) == len(set(owner_ids)) == 10
        assert not (set(owner_ids) & {reflection[owner] for owner in owner_ids})
        assert rows == tuple(sorted(reduced[owner] for owner in owner_ids))

        expected_status = "existing" if rows in existing else "new"
        assert record["status"] == expected_status
        status_counts[expected_status] += 1

    assert len(records) == report["unique_pair_masks"]
    assert status_counts["existing"] == report["regenerated_frozen_target_masks"]
    assert status_counts["new"] == report["genuinely_new_pair_masks"]
    assert report["allowed_raw"] >= len(records)

    print(json.dumps({
        "status": "PASS",
        "target_row": args.target_row,
        "allowed_row_count": len(allowed),
        "catalogue_records": len(records),
        "new_records": status_counts["new"],
        "existing_records": status_counts["existing"],
        "literal_witnesses_replayed": len(records),
        "all_masks_contained_in_allowed_rows": True,
        "all_masks_contain_target": True,
        "all_reflection_pairs_owner_disjoint": True,
        "scope": (
            "literal replay of every emitted mask/witness; enumeration "
            "completeness follows from the anchored symbolic theorem"
        ),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
