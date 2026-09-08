#!/usr/bin/env python3
"""Audit the frozen 164/48 tapped-C6 collar census without rebuilding menus.

Run only on H100.  The symbolic forced-cell theorem is proved in the note;
this script independently checks that every row in the frozen finite output
has exactly the asserted kind/capacity diagnosis.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output")
    args = parser.parse_args()
    report = json.loads(Path(args.output).read_text())

    assert report["status"] == "UNSAT_COLLAR"
    assert report["collar_mode"] == "full"
    assert report["row_kind_histogram"] == {
        "adjacent": 48,
        "distance_two": 164,
    }
    diagnostics = report["diagnostics"]
    assert len(diagnostics) == 212

    kinds = Counter()
    hard_cells = Counter()
    hard_coordinates = []
    for expected_row, item in enumerate(diagnostics):
        assert item["row"] == expected_row
        kind = item["kind"]
        kinds[kind] += 1
        deficits = item["collar_deficits"]
        if kind == "adjacent":
            # This is only the exact clock-cell capacity precheck.  The
            # larger protected-halo menu may still be empty.
            assert deficits == []
            continue

        assert kind == "distance_two"
        assert item["attempts"] == item["accepted"] == 0
        assert item["rejections"] == {"exact_collar_capacity": 1}
        assert len(deficits) == 2
        by_cell = {entry["cell"]: entry for entry in deficits}
        assert set(by_cell) == {"010", "001"}
        for cell in ("010", "001"):
            entry = by_cell[cell]
            assert entry["required_clock_roles"] == 1
            assert entry["available_coordinates"] == []
            assert len(entry["all_cell_coordinates"]) == 1
            assert entry["guarded_coordinates"] == entry["all_cell_coordinates"]
            hard_cells[cell] += 1
            hard_coordinates.append(entry["all_cell_coordinates"][0])

    assert kinds == Counter({"distance_two": 164, "adjacent": 48})
    assert hard_cells == Counter({"010": 164, "001": 164})
    assert report["collar_infeasible_rows"] == 164
    core = report["smallest_exact_unsat_core"]
    assert core["rows"] == 1
    assert core["row"] == 0 and core["source_row"] == 1
    assert core["kind"] == "distance_two"
    assert {item["cell"] for item in core["deficits"]} == {"010", "001"}

    print(json.dumps({
        "status": "PASS",
        "rows": len(diagnostics),
        "row_kind_histogram": dict(sorted(kinds.items())),
        "hard_rows_with_exact_010_and_001_deficits": 164,
        "adjacent_rows_without_capacity_deficit": 48,
        "hard_deficient_cell_histogram": dict(sorted(hard_cells.items())),
        "smallest_hard_core": {
            "rows": 1,
            "row": 0,
            "source_row": 1,
        },
        "adjacent_scope": "capacity precheck only; not menu feasibility",
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
