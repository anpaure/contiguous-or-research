#!/usr/bin/env python3
"""Build a complete owner-only reflected-pair atlas for a fixed free set."""

from __future__ import annotations

import argparse
import concurrent.futures
import csv
import hashlib
import json
import subprocess
import time
from collections import Counter, defaultdict
from pathlib import Path


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


def write_catalog(path: Path, records: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="ascii") as stream:
        writer = csv.DictWriter(stream, fieldnames=FIELDS, delimiter="\t")
        writer.writeheader()
        writer.writerows(records)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--binary", required=True)
    parser.add_argument("--instance", required=True)
    parser.add_argument("--allowed-rows", required=True)
    parser.add_argument("--expected-allowed-count", required=True, type=int)
    parser.add_argument("--work-dir", required=True)
    parser.add_argument("--all-catalog", required=True)
    parser.add_argument("--new-catalog", required=True)
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--jobs", type=int, default=2)
    parser.add_argument("--threads-per-job", type=int, default=40)
    args = parser.parse_args()

    binary = Path(args.binary).resolve()
    instance = Path(args.instance).resolve()
    allowed_path = Path(args.allowed_rows).resolve()
    work_dir = Path(args.work_dir).resolve()
    all_catalog = Path(args.all_catalog).resolve()
    new_catalog = Path(args.new_catalog).resolve()
    manifest_path = Path(args.manifest).resolve()
    work_dir.mkdir(parents=True, exist_ok=True)

    with allowed_path.open(encoding="ascii") as stream:
        allowed = tuple(sorted(map(int, stream.read().split())))
    assert len(allowed) == len(set(allowed)) == args.expected_allowed_count
    assert all(0 <= row < 680 for row in allowed)
    assert args.jobs > 0 and args.threads_per_job > 0
    started = time.time()

    def generate(target: int) -> dict[str, object]:
        report_path = work_dir / f"row{target}.h100.json"
        catalog_path = work_dir / f"row{target}.h100.tsv"
        command = [
            str(binary),
            "--target-row", str(target),
            "--instance", str(instance),
            "--allowed-rows", str(allowed_path),
            "--catalog", str(catalog_path),
            "--threads", str(args.threads_per_job),
        ]
        row_started = time.time()
        with report_path.open("w", encoding="ascii") as output:
            subprocess.run(command, check=True, stdout=output)
        with report_path.open(encoding="ascii") as stream:
            report = json.load(stream)
        assert report["status"] == "PASS" and report["target_row"] == target
        assert Path(report["allowed_filter"]).resolve() == allowed_path
        assert Path(report["catalogue"]).resolve() == catalog_path
        records = read_catalog(catalog_path)
        assert len(records) == report["unique_pair_masks"]
        masks = [integers(record["rows"]) for record in records]
        assert len(masks) == len(set(masks))
        assert all(target in mask and set(mask) <= set(allowed) for mask in masks)
        return {
            "target_row": target,
            "report": str(report_path),
            "report_sha256": sha256(report_path),
            "catalog": str(catalog_path),
            "catalog_sha256": sha256(catalog_path),
            "unique_pair_masks": report["unique_pair_masks"],
            "frozen_pair_masks": report["regenerated_frozen_target_masks"],
            "new_pair_masks": report["genuinely_new_pair_masks"],
            "allowed_raw": report["allowed_raw"],
            "wall_seconds": round(time.time() - row_started, 6),
        }

    entries: list[dict[str, object]] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.jobs) as executor:
        futures = {executor.submit(generate, target): target for target in allowed}
        for completed, future in enumerate(
            concurrent.futures.as_completed(futures), start=1
        ):
            entry = future.result()
            entries.append(entry)
            if completed % 16 == 0 or completed == len(allowed):
                print(json.dumps({
                    "progress": completed,
                    "targets": len(allowed),
                    "last_target": entry["target_row"],
                    "elapsed_seconds": round(time.time() - started, 3),
                }), flush=True)
    entries.sort(key=lambda entry: int(entry["target_row"]))
    assert [entry["target_row"] for entry in entries] == list(allowed)

    retained: dict[tuple[int, ...], dict[str, str]] = {}
    target_occurrences: defaultdict[tuple[int, ...], set[int]] = defaultdict(set)
    status_by_mask: dict[tuple[int, ...], str] = {}
    total_records = 0
    for entry in entries:
        target = int(entry["target_row"])
        for record in read_catalog(Path(str(entry["catalog"]))):
            rows = integers(record["rows"])
            assert len(rows) == len(set(rows)) == 10
            assert rows == tuple(sorted(rows))
            assert target in rows and set(rows) <= set(allowed)
            assert target not in target_occurrences[rows]
            target_occurrences[rows].add(target)
            total_records += 1
            assert status_by_mask.setdefault(rows, record["status"]) == record["status"]
            retained.setdefault(rows, record)
    assert retained
    assert all(target_occurrences[rows] == set(rows) for rows in retained)
    multiplicities = Counter(len(targets) for targets in target_occurrences.values())
    assert multiplicities == {10: len(retained)}
    assert total_records == 10 * len(retained)

    ordered = [retained[rows] for rows in sorted(retained)]
    new_records = [record for record in ordered if record["status"] == "new"]
    frozen_records = [record for record in ordered if record["status"] == "frozen"]
    assert len(ordered) == len(new_records) + len(frozen_records)
    write_catalog(all_catalog, ordered)
    write_catalog(new_catalog, new_records)

    manifest: dict[str, object] = {
        "status": "PASS",
        "scope": (
            "complete owner-only reflection-pair masks contained in fixed "
            f"F{len(allowed)}"
        ),
        "instance": str(instance),
        "instance_sha256": sha256(instance),
        "binary": str(binary),
        "binary_sha256": sha256(binary),
        "allowed_rows": str(allowed_path),
        "allowed_rows_sha256": sha256(allowed_path),
        "allowed_row_count": len(allowed),
        "target_rows": list(allowed),
        "jobs": args.jobs,
        "threads_per_job": args.threads_per_job,
        "per_target": entries,
        "per_target_record_sum": total_records,
        "tenfold_membership_histogram": {"10": len(retained)},
        "unique_pair_masks": len(ordered),
        "frozen_pair_masks": len(frozen_records),
        "genuinely_new_pair_masks": len(new_records),
        "all_catalog": str(all_catalog),
        "all_catalog_sha256": sha256(all_catalog),
        "new_catalog": str(new_catalog),
        "new_catalog_sha256": sha256(new_catalog),
        "elapsed_seconds": round(time.time() - started, 6),
        "completeness": (
            f"all {len(allowed)} allowed rows were anchored; every retained "
            "10-row mask occurred at exactly its ten constituent targets"
        ),
    }
    with manifest_path.open("w", encoding="ascii") as stream:
        json.dump(manifest, stream, indent=2, sort_keys=True)
        stream.write("\n")
    print(json.dumps({key: manifest[key] for key in (
        "status", "allowed_row_count", "per_target_record_sum",
        "tenfold_membership_histogram", "unique_pair_masks",
        "frozen_pair_masks", "genuinely_new_pair_masks", "elapsed_seconds",
    )}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
