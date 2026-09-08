#!/usr/bin/env python3
"""Exact minimum typed overlap for two affine-relabeled q4 reserve copies.

Run substantively on H100 only.  Only affine maps whose two owner banks are
disjoint in both recoupled states are retained.  For every pair of
minimum-excess whole-rail polarity assignments, compute the exact active
q1/q2 collision excess of their union.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import audit_q4_k17_recoupled_typed_rail_ledgers_20260814 as base  # noqa:E402
import audit_q4_k17_typed_polarity_unsat_core_20260814 as core  # noqa:E402

BANKS = ("lower_q1", "upper_q1", "lower_q2", "upper_q2")


def relabel(value, a, b):
    return frozenset((a * item + b) % 17 for item in value)


def relabel_rails(rails, a, b):
    return [(name, [relabel(owner, a, b) for owner in cycle]) for name, cycle in rails]


def owner_bank(rails):
    return {owner for _, cycle in rails for owner in cycle}


def assignment_records(rails):
    by_rail, _ = base.occurrences(rails)
    names = [name for name, _ in rails]
    records = []
    for bits in itertools.product((False, True), repeat=len(names)):
        if sum(core.active_collision_score(names, by_rail, bits).values()) != 1:
            continue
        active = {bank: [] for bank in BANKS}
        for name, upper in zip(names, bits):
            for suffix in ("q1", "q2"):
                bank = ("upper_" if upper else "lower_") + suffix
                active[bank].extend(by_rail[name][bank])
        assert sum(len(values) - len(set(values)) for values in active.values()) == 1
        records.append({"bits": bits, "sets": tuple(frozenset(active[bank]) for bank in BANKS)})
    return records


def bitword(bits):
    return "".join("1" if bit else "0" for bit in bits)


def search_state(left, a, b):
    right = [
        {
            "bits": item["bits"],
            "sets": tuple(
                frozenset(relabel(resource, a, b) for resource in bank)
                for bank in item["sets"]
            ),
        }
        for item in left
    ]
    best = None
    witness = None
    checked = 0
    attained_lower_bound = False
    for x in left:
        for y in right:
            checked += 1
            cross = tuple(len(s & t) for s, t in zip(x["sets"], y["sets"]))
            total = 2 + sum(cross)
            candidate = (total, cross, bitword(x["bits"]), bitword(y["bits"]))
            if best is None or candidate < best:
                best = candidate
                witness = {
                    "left_bits": candidate[2],
                    "right_bits": candidate[3],
                    "cross_resource_intersections": dict(zip(BANKS, cross)),
                }
            if total == 2:
                attained_lower_bound = True
                break
        if attained_lower_bound:
            break
    return {
        "assignment_pairs": len(left) * len(right),
        "assignment_pairs_checked": checked,
        "minimum_active_collision_excess": best[0],
        "minimum_is_proved": attained_lower_bound or checked == len(left) * len(right),
        "first_minimum_pair": witness,
    }


def main():
    source_raw = Path(sys.argv[1]).read_bytes()
    states = dict(base.rail_states())
    owner_simple_maps = []
    for a in range(1, 17):
        for b in range(17):
            if all(
                owner_bank(rails).isdisjoint(owner_bank(relabel_rails(rails, a, b)))
                for rails in states.values()
            ):
                owner_simple_maps.append((a, b))
    assignments = {name: assignment_records(rails) for name, rails in states.items()}
    reports = []
    for a, b in owner_simple_maps:
        state_reports = {
            name: search_state(assignments[name], a, b) for name in states
        }
        reports.append({"a": a, "b": b, "states": state_reports})
    print(json.dumps({
        "status": "PASS",
        "scope": "all common-owner-simple affine Z_17 second-copy relabelings",
        "source_sha256": hashlib.sha256(source_raw).hexdigest(),
        "owner_simple_maps": len(owner_simple_maps),
        "reports": reports,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
