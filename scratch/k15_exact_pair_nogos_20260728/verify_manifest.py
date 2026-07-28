#!/usr/bin/env python3
"""Fail closed if the certified k=15 pair bundle has drifted."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def digest(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            value.update(block)
    return value.hexdigest()


def main() -> None:
    manifest = json.loads((ROOT / "MANIFEST.json").read_text())
    errors: list[str] = []
    expected_payload: set[str] = set()

    for entry in manifest["entries"]:
        summary = ROOT / entry["summary"]
        log = ROOT / entry["log"]
        expected_payload.update((summary.name, log.name))
        for path, expected_hash, expected_size in (
            (summary, entry["summary_sha256_expected"], entry["summary_bytes"]),
            (log, entry["log_sha256"], entry["log_bytes"]),
        ):
            if not path.is_file():
                errors.append(f"missing {path.name}")
                continue
            if path.stat().st_size != expected_size:
                errors.append(f"size mismatch {path.name}")
            if digest(path) != expected_hash:
                errors.append(f"SHA-256 mismatch {path.name}")

        if summary.is_file():
            result = json.loads(summary.read_text())
            if result.get("status") != "DONE":
                errors.append(f"run status is not DONE: {summary.name}")
            if result.get("census") != [{"round": 0, "status": "INFEASIBLE"}]:
                errors.append(f"solver census is not the frozen UNSAT: {summary.name}")
            if result.get("parent_count") != 2:
                errors.append(f"parent count is not two: {summary.name}")
            if len(result.get("exact_fixed_models", [])) != 2:
                errors.append(f"fixed-shore model count is not two: {summary.name}")
            if result.get("residence_forbidden_motifs", 0) <= 0:
                errors.append(f"residence was not visibly enforced: {summary.name}")

    actual_payload = {
        path.name
        for path in ROOT.iterdir()
        if path.name.startswith("exactdm_pair")
    }
    if actual_payload != expected_payload:
        errors.append(
            "payload inventory mismatch: "
            f"missing={sorted(expected_payload - actual_payload)} "
            f"extra={sorted(actual_payload - expected_payload)}"
        )
    forbidden = sorted(path.name for path in ROOT.iterdir() if "allow6" in path.name)
    if forbidden:
        errors.append(f"retracted allow6 artifacts present: {forbidden}")

    report = {
        "status": "PASS" if not errors else "FAIL",
        "summaries_verified": len(manifest["entries"]),
        "payload_files_verified": len(expected_payload),
        "allow6_artifacts": forbidden,
        "errors": errors,
    }
    print(json.dumps(report, indent=2, sort_keys=True))
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
