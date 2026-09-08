#!/usr/bin/env python3
"""Audit owner and typed-resource overlap of two translated q4 reserve copies.

Run substantively on H100 only.  The first copy is fixed and the second is
translated by every nonzero element of Z_17.  For each recoupled state and
each pair of minimum-excess whole-rail polarity assignments, count whether
the two owner banks are disjoint and record the minimum active q1/q2
cross-collision excess before any cross-copy recut.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import audit_q4_k17_recoupled_typed_rail_ledgers_20260814 as base  # noqa:E402
import audit_q4_k17_typed_polarity_unsat_core_20260814 as core  # noqa:E402
import search_q4_k17_first_minimum_polarity_adjacent_c8_repair_20260814 as c8  # noqa:E402


def translate(value, delta):
    return frozenset((item + delta) % 17 for item in value)


def translate_rails(rails, delta):
    return [(name, [translate(owner, delta) for owner in owners]) for name, owners in rails]


def minimum_assignments(rails):
    by_rail, _ = base.occurrences(rails)
    names = [name for name, _ in rails]
    return [
        bits for bits in itertools.product((False, True), repeat=len(names))
        if sum(core.active_collision_score(names, by_rail, bits).values()) == 1
    ]


def active_banks(rails, bits):
    by_rail, _ = base.occurrences(rails)
    names = [name for name, _ in rails]
    result = {bank: [] for bank in ("lower_q1", "upper_q1", "lower_q2", "upper_q2")}
    for name, upper in zip(names, bits):
        for suffix in ("q1", "q2"):
            bank = ("upper_" if upper else "lower_") + suffix
            result[bank].extend(by_rail[name][bank])
    return result


def excess(values):
    return len(values) - len(set(values))


def search_state(state_name, rails):
    owners = {owner for _, cycle in rails for owner in cycle}
    assignments = minimum_assignments(rails)
    banks = [active_banks(rails, bits) for bits in assignments]
    reports = []
    for delta in range(1, 17):
        shifted = translate_rails(rails, delta)
        shifted_owners = {owner for _, cycle in shifted for owner in cycle}
        owner_overlap = len(owners & shifted_owners)
        minimum = None
        histogram = Counter()
        if owner_overlap == 0:
            shifted_assignments = minimum_assignments(shifted)
            assert shifted_assignments == assignments
            shifted_banks = [active_banks(shifted, bits) for bits in assignments]
            for left in banks:
                for right in shifted_banks:
                    score = tuple(excess(left[bank] + right[bank]) for bank in left)
                    total = sum(score)
                    histogram[total] += 1
                    if minimum is None or (total, score) < minimum:
                        minimum = (total, score)
        reports.append({
            "translation": delta,
            "owner_overlap": owner_overlap,
            "assignment_pairs": len(assignments) ** 2 if owner_overlap == 0 else 0,
            "minimum_active_collision_excess": None if minimum is None else minimum[0],
            "minimum_bank_excess": None if minimum is None else dict(zip(
                ("lower_q1", "upper_q1", "lower_q2", "upper_q2"), minimum[1]
            )),
            "active_collision_excess_histogram": dict(histogram),
        })
    return {
        "state": state_name,
        "minimum_assignments_per_copy": len(assignments),
        "translation_reports": reports,
    }


def main():
    source_raw = Path(sys.argv[1]).read_bytes()
    reports = [search_state(name, rails) for name, rails in base.rail_states()]
    print(json.dumps({
        "status": "PASS",
        "scope": "two copies related by a nonzero Z_17 translation; no recut",
        "source_sha256": hashlib.sha256(source_raw).hexdigest(),
        "reports": reports,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
