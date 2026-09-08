#!/usr/bin/env python3
"""Combine independently partitioned full-signature conjugation outputs."""

from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path


def main():
    paths = [Path(name) for name in sys.argv[1:]]
    assert paths
    parts = [json.loads(path.read_text(encoding="utf-8")) for path in paths]
    source_s = parts[0]["source_s"]
    target_s = parts[0]["target_s"]
    assert all(
        part["status"] == "PASS"
        and part["source_s"] == source_s
        and part["target_s"] == target_s
        for part in parts
    )
    reports = [row for part in parts for row in part["reports"]]
    key_counts = Counter(
        (
            tuple(row["source_suffix_edge"]),
            row["context"],
            row["target_prefix"],
        )
        for row in reports
    )
    assert set(key_counts.values()) == {1}
    print(json.dumps({
        "status": "PASS",
        "source_s": source_s,
        "target_s": target_s,
        "partition_files": [str(path) for path in paths],
        "reports": reports,
        "summary": {
            context: {
                "phase_pairs_tested": sum(
                    row["context"] == context for row in reports
                ),
                "distinct_coordinate_images_tested": sum(
                    row["distinct_coordinate_images_tested"]
                    for row in reports if row["context"] == context
                ),
                "phase_pairs_with_selection_conjugation": sum(
                    row["context"] == context
                    and row["selection_valid_images"] > 0
                    for row in reports
                ),
                "phase_pairs_with_q2_safe_conjugation": sum(
                    row["context"] == context
                    and row["q2_safe_images"] > 0
                    for row in reports
                ),
                "actuators_with_q2_safe_conjugation": len({
                    tuple(row["source_suffix_edge"])
                    for row in reports
                    if row["context"] == context
                    and row["q2_safe_images"] > 0
                }),
            }
            for context in ("10", "wrap")
        },
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
