#!/usr/bin/env python3
"""Replay the exact F208 atlas append into the immutable full instance."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path

from search_q4_k17_z17_reflection_fixed_face_kissat_20260814 import read_instance


FIELDS = ["rows", "core", "order", "owner_ids", "status"]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-instance", required=True)
    parser.add_argument("--full-instance", required=True)
    parser.add_argument("--allowed-rows", required=True)
    parser.add_argument("--new-catalog", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    base_path = Path(args.base_instance).resolve()
    full_path = Path(args.full_instance).resolve()
    allowed_path = Path(args.allowed_rows).resolve()
    catalog_path = Path(args.new_catalog).resolve()
    output_path = Path(args.output).resolve()

    with allowed_path.open(encoding="ascii") as stream:
        allowed = set(map(int, stream.read().split()))
    assert len(allowed) == 208

    base_rows, base_groups, base_self, base_pairs = read_instance(str(base_path))
    full_rows, full_groups, full_self, full_pairs = read_instance(str(full_path))
    assert (base_rows, base_groups) == (full_rows, full_groups) == (680, 35)
    assert base_self == full_self and len(base_self) == 3749
    assert base_pairs == full_pairs[:len(base_pairs)]
    assert len(base_pairs) == len(set(base_pairs)) == 277960
    assert len(full_pairs) == len(set(full_pairs)) == 280047

    with catalog_path.open(newline="", encoding="ascii") as stream:
        reader = csv.DictReader(stream, delimiter="\t")
        assert reader.fieldnames == FIELDS
        records = list(reader)
    catalog_rows = []
    for record in records:
        rows = tuple(map(int, record["rows"].split(",")))
        assert len(rows) == len(set(rows)) == 10
        assert rows == tuple(sorted(rows)) and set(rows) <= allowed
        assert record["status"] == "new"
        catalog_rows.append(rows)
    assert len(catalog_rows) == len(set(catalog_rows)) == 2087
    assert not (set(catalog_rows) & set(base_pairs))
    assert catalog_rows == full_pairs[len(base_pairs):]

    result = {
        "status": "PASS",
        "scope": "exact ordered replay of the complete F208 new-mask append",
        "base_instance": str(base_path),
        "base_instance_sha256": sha256(base_path),
        "full_instance": str(full_path),
        "full_instance_sha256": sha256(full_path),
        "allowed_rows": str(allowed_path),
        "allowed_rows_sha256": sha256(allowed_path),
        "new_catalog": str(catalog_path),
        "new_catalog_sha256": sha256(catalog_path),
        "base_pair_masks": len(base_pairs),
        "appended_pair_masks": len(catalog_rows),
        "full_pair_masks": len(full_pairs),
        "self_options": len(full_self),
        "base_prefix_identical": True,
        "all_appended_masks_unique": True,
        "all_appended_masks_contained_in_F208": True,
        "ordered_appended_suffix_equals_new_catalog": True,
    }
    with output_path.open("w", encoding="ascii") as stream:
        json.dump(result, stream, indent=2, sort_keys=True)
        stream.write("\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
