#!/usr/bin/env python3
"""Materialize and audit the genuine four-filter two-endpoint reroot.

This script accepts only the authenticated K15 four-filter parent.  It first
reconstructs the canonical natural K16 chronology of SHA 0f6d64e9..., then
reverses target positions [0,6388] and [12826,12869].  The two reversals are
disjoint endpoint reroots; hence all internal interval unions are retained.
"""

from __future__ import annotations

from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
PARENT = ROOT / "scratch/K15_FOURFILTER_SEED_20260731.word"
TARGET = ROOT / "scratch/k16_true_fourfilter_endpoint_reroot_targets_20260731.word"
AUDIT = ROOT / "scratch/k16_true_fourfilter_endpoint_reroot_20260731.audit.json"
PARENT_SHA = "51f57125ea3e145e08ed9d5f8816d22313a010907588457260c824c6f40217f4"
NATURAL_SHA = "0f6d64e9311ef634169964350baa8f817b17b9d1619970c881f87e7346550a5c"
TARGET_SHA = "c7beccc38489ad0ce4f203fa11e348a9fb04a18418cdc8ac9dce038ddde06906"
K = 16
RANK = 8
FULL = (1 << K) - 1

sys.path.insert(0, str(ROOT / "scratch"))
from audit_three_hole_middle_schedule_dp_20260731 import maximize_area  # noqa: E402


def stable(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return sha256(raw).hexdigest()


def canonical(values: list[int]) -> bytes:
    return (" ".join(map(str, values)) + "\n").encode()


def interval_coverage(values: list[int]) -> set[int]:
    """All interval ORs, adding a value only when a new bit first appears."""
    n = len(values)
    next_position = [[n] * K for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        next_position[i] = next_position[i + 1].copy()
        for bit in range(K):
            if values[i] & (1 << bit):
                next_position[i][bit] = i
    covered: set[int] = set()
    for i, first in enumerate(values):
        union = first
        covered.add(union)
        events = sorted(
            (next_position[i + 1][bit], bit)
            for bit in range(K)
            if not (first & (1 << bit)) and next_position[i + 1][bit] < n
        )
        cursor = 0
        while cursor < len(events):
            position = events[cursor][0]
            while cursor < len(events) and events[cursor][0] == position:
                union |= 1 << events[cursor][1]
                cursor += 1
            covered.add(union)
    return covered


def first_witness(values: list[int], target: int) -> list[int]:
    for left in range(len(values)):
        union = 0
        for right in range(left, min(len(values), left + K + 1)):
            union |= values[right]
            if union == target:
                return [left, right]
            if union & ~target:
                break
    raise AssertionError(f"no witness for {target:#06x}")


def main() -> None:
    assert sha256(PARENT.read_bytes()).hexdigest() == PARENT_SHA
    parent = [int(token) for token in PARENT.read_text().split()]
    d2 = [parent[i] | parent[i + 1] | parent[i + 2]
          for i in range(len(parent) - 2)]
    d3 = [parent[i] | parent[i + 1] | parent[i + 2] | parent[i + 3]
          for i in range(len(parent) - 3)]
    assert [(i, value.bit_count()) for i, value in enumerate(d2)
            if value.bit_count() != 7] == [(6390, 6)]
    natural = (
        list(reversed([0x8000 | value for value in d2[:6390]]))
        + d3
        + list(reversed([0x8000 | value for value in d2[6391:]]))
    )
    assert sha256(canonical(natural)).hexdigest() == NATURAL_SHA

    target = (
        list(reversed(natural[:6389]))
        + natural[6389:12826]
        + list(reversed(natural[12826:]))
    )
    assert sha256(canonical(target)).hexdigest() == TARGET_SHA
    assert len(target) == len(set(target)) == 12870
    assert all(value.bit_count() == RANK for value in target)

    natural_q1 = Counter(a | b for a, b in zip(natural, natural[1:]))
    target_q1 = Counter(a | b for a, b in zip(target, target[1:]))
    q1_universe = {value for value in range(1, FULL + 1)
                   if value.bit_count() == RANK + 1}
    assert q1_universe - set(natural_q1) == {0xB3CC, 0xD3CC}
    assert q1_universe <= set(target_q1)
    assert natural_q1[0xC3CE] == 2
    assert natural_q1[0xF38C] == 2

    natural_coverage = interval_coverage(natural)
    target_coverage = interval_coverage(target)
    added = sorted(target_coverage - natural_coverage)
    expected_added = [0xB3CC, 0xD3CC, 0xD3CE, 0xDBCE, 0xF3CC, 0xFBCE]
    assert not (natural_coverage - target_coverage)
    assert added == sorted(expected_added)
    assert not [value for value in range(1, FULL + 1)
                if value.bit_count() > RANK and value not in target_coverage]

    dp = maximize_area(target, K, holes=3)
    assert dp["maximum_lower_area"] == 32226
    assert dp["lower_capacity_upper_bound"] == 32235
    assert dp["maximizing_start_holes"] == [12870, 12871, 12872]
    assert dp["maximizing_deadline_holes"] == [0, 1, 6386]

    TARGET.write_bytes(canonical(target))
    payload = {
        "schema": "r.k16.true_fourfilter.endpoint_reroot.v1",
        "status": "PASS_EXACT_CARRIER_AND_SCALAR_CAPACITY",
        "parent": str(PARENT.relative_to(ROOT)),
        "parent_sha256": PARENT_SHA,
        "natural_target_sha256": NATURAL_SHA,
        "target": str(TARGET.relative_to(ROOT)),
        "target_sha256": TARGET_SHA,
        "reversals_inclusive": [[0, 6388], [12826, 12869]],
        "removed_boundary_colours": [0xC3CE, 0xF38C],
        "removed_boundary_colour_multiplicities": [2, 2],
        "added_boundary_colours": [0xD3CC, 0xB3CC],
        "middle_count": len(target),
        "middle_distinct": len(set(target)),
        "q1_missing": [],
        "natural_coverage_size": len(natural_coverage),
        "target_coverage_size": len(target_coverage),
        "lost_interval_or_masks": [],
        "added_interval_or_masks": expected_added,
        "added_interval_or_witnesses": {
            f"0x{value:04x}": first_witness(target, value)
            for value in expected_added
        },
        "all_upper_missing": [],
        "max_pq": dp,
        "scope": [
            "Exact for the authenticated four-filter parent and displayed two endpoint reroots.",
            "The carrier and scalar capacity pass do not imply lower Hall or common capped-envelope realizability.",
        ],
    }
    payload["payload_sha256"] = stable(payload)
    AUDIT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "status": payload["status"],
        "target": str(TARGET.relative_to(ROOT)),
        "target_sha256": TARGET_SHA,
        "payload_sha256": payload["payload_sha256"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
