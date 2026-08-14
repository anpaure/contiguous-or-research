#!/usr/bin/env python3
"""Independent tenfold and literal-witness replay of the complete F208 atlas."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path

from search_q4_k17_z17_quotient_exact_cover_20260814 import (
    canonical_orbit_mask,
    deck_masks,
    owner_orbits,
)
from search_q4_k17_z17_reflection_fixed_face_kissat_20260814 import read_instance
from search_q4_k17_z17_reflection_invariant_owner_cover_20260814 import (
    reflection_action,
)


FIELDS = ["rows", "core", "order", "owner_ids", "status"]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def integers(value: str) -> tuple[int, ...]:
    return tuple(map(int, value.split(","))) if value else ()


def read_catalog(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="ascii") as stream:
        reader = csv.DictReader(stream, delimiter="\t")
        assert reader.fieldnames == FIELDS
        return list(reader)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    manifest_path = Path(args.manifest).resolve()
    output_path = Path(args.output).resolve()
    with manifest_path.open(encoding="ascii") as stream:
        manifest = json.load(stream)
    assert manifest["status"] == "PASS"

    instance = Path(manifest["instance"])
    binary = Path(manifest["binary"])
    allowed_path = Path(manifest["allowed_rows"])
    all_catalog_path = Path(manifest["all_catalog"])
    new_catalog_path = Path(manifest["new_catalog"])
    assert sha256(instance) == manifest["instance_sha256"]
    assert sha256(binary) == manifest["binary_sha256"]
    assert sha256(allowed_path) == manifest["allowed_rows_sha256"]
    assert sha256(all_catalog_path) == manifest["all_catalog_sha256"]
    assert sha256(new_catalog_path) == manifest["new_catalog_sha256"]

    with allowed_path.open(encoding="ascii") as stream:
        allowed = tuple(sorted(map(int, stream.read().split())))
    assert len(allowed) == len(set(allowed)) == 208
    assert manifest["target_rows"] == list(allowed)
    assert manifest["allowed_row_count"] == 208

    _, _, _, pair_options = read_instance(str(instance))
    existing = {tuple(sorted(map(int, rows))) for rows in pair_options}
    assert len(existing) == len(pair_options)

    representatives, orbit_index = owner_orbits()
    reflection = reflection_action(representatives, orbit_index)
    nonfixed = [owner for owner in range(1430) if owner < reflection[owner]]
    assert len(nonfixed) == 680
    reduced: dict[int, int] = {}
    for row, owner in enumerate(nonfixed):
        reduced[owner] = reduced[reflection[owner]] = row

    replayed = 0

    def replay(record: dict[str, str], *, expected_target: int | None = None) -> tuple[int, ...]:
        nonlocal replayed
        rows = integers(record["rows"])
        core = integers(record["core"])
        order = integers(record["order"])
        owner_ids = integers(record["owner_ids"])
        assert len(rows) == len(set(rows)) == 10
        assert rows == tuple(sorted(rows)) and set(rows) <= set(allowed)
        if expected_target is not None:
            assert expected_target in rows
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
        expected_status = "frozen" if rows in existing else "new"
        assert record["status"] == expected_status
        replayed += 1
        return rows

    target_occurrences: defaultdict[tuple[int, ...], set[int]] = defaultdict(set)
    per_target_record_sum = 0
    entries = manifest["per_target"]
    assert len(entries) == 208
    assert sorted(entry["target_row"] for entry in entries) == list(allowed)
    for entry in entries:
        target = int(entry["target_row"])
        report_path = Path(entry["report"])
        catalog_path = Path(entry["catalog"])
        assert sha256(report_path) == entry["report_sha256"]
        assert sha256(catalog_path) == entry["catalog_sha256"]
        with report_path.open(encoding="ascii") as stream:
            report = json.load(stream)
        assert report["status"] == "PASS" and report["target_row"] == target
        assert Path(report["allowed_filter"]).resolve() == allowed_path.resolve()
        assert Path(report["catalogue"]).resolve() == catalog_path.resolve()
        records = read_catalog(catalog_path)
        assert len(records) == entry["unique_pair_masks"] == report["unique_pair_masks"]
        local: set[tuple[int, ...]] = set()
        local_status = Counter()
        for record in records:
            rows = replay(record, expected_target=target)
            assert rows not in local
            local.add(rows)
            assert target not in target_occurrences[rows]
            target_occurrences[rows].add(target)
            per_target_record_sum += 1
            local_status[record["status"]] += 1
        assert entry["allowed_raw"] == report["allowed_raw"]
        assert entry["frozen_pair_masks"] == report[
            "regenerated_frozen_target_masks"
        ] == local_status["frozen"]
        assert entry["new_pair_masks"] == report[
            "genuinely_new_pair_masks"
        ] == local_status["new"]

    assert per_target_record_sum == manifest["per_target_record_sum"]
    assert all(target_occurrences[rows] == set(rows) for rows in target_occurrences)
    multiplicities = Counter(len(targets) for targets in target_occurrences.values())
    assert multiplicities == {10: len(target_occurrences)}
    assert manifest["tenfold_membership_histogram"] == {
        "10": len(target_occurrences)
    }

    all_records = read_catalog(all_catalog_path)
    all_masks: set[tuple[int, ...]] = set()
    for record in all_records:
        rows = replay(record)
        assert rows not in all_masks
        all_masks.add(rows)
    assert all_masks == set(target_occurrences)
    assert len(all_masks) == manifest["unique_pair_masks"]

    new_records = read_catalog(new_catalog_path)
    new_masks: set[tuple[int, ...]] = set()
    for record in new_records:
        rows = replay(record)
        assert record["status"] == "new" and rows not in existing
        assert rows not in new_masks
        new_masks.add(rows)
    expected_new = all_masks - existing
    expected_frozen = all_masks & existing
    assert new_masks == expected_new
    assert len(expected_new) == manifest["genuinely_new_pair_masks"]
    assert len(expected_frozen) == manifest["frozen_pair_masks"]

    result = {
        "status": "PASS",
        "scope": "independent literal and tenfold replay of complete owner-only F208 atlas",
        "allowed_row_count": len(allowed),
        "target_catalogues": len(entries),
        "per_target_record_sum": per_target_record_sum,
        "tenfold_membership_histogram": {"10": len(all_masks)},
        "unique_pair_masks": len(all_masks),
        "frozen_pair_masks": len(expected_frozen),
        "genuinely_new_pair_masks": len(expected_new),
        "literal_witness_replays": replayed,
        "new_union_literal_witnesses_replayed": len(new_records),
        "instance_pair_masks": len(existing),
        "all_masks_contained_in_F": True,
        "every_mask_seen_at_exactly_its_ten_target_rows": True,
        "new_union_exactly_subtracts_frozen_instance": True,
    }
    with output_path.open("w", encoding="ascii") as stream:
        json.dump(result, stream, indent=2, sort_keys=True)
        stream.write("\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
