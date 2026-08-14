#!/usr/bin/env python3
"""Independent full-record audit of targeted top-K artifacts (H100)."""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter

from search_q4_k17_z17_quotient_exact_cover_20260814 import (
    K,
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


FIELDS = [
    "rows", "core", "order", "reflected_core", "reflected_order",
    "owner_ids", "reflected_owner_ids", "best_outgoing_pair_index",
    "delta", "new_energy", "hole_change", "holes_filled", "add_base",
    "covered_incumbent_holes", "target_row", "tier",
]


def integers(value):
    return tuple(map(int, value.split(","))) if value else ()


def load_energy(loads):
    return sum((load - 1) ** 2 for load in loads)


def read_records(path):
    with open(path, newline="", encoding="ascii") as stream:
        reader = csv.DictReader(stream, delimiter="\t")
        assert reader.fieldnames == FIELDS
        return list(reader)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--instance", required=True)
    parser.add_argument("--incumbent", required=True)
    parser.add_argument("--report", required=True)
    parser.add_argument("--top", required=True)
    parser.add_argument("--reservoir", required=True)
    args = parser.parse_args()

    _, _, self_options, pair_options = read_instance(args.instance)
    with open(args.incumbent, encoding="ascii") as stream:
        state = json.load(stream)
    with open(args.report, encoding="ascii") as stream:
        report = json.load(stream)
    assert state["energy"] == report["incumbent_energy"]
    energy = state["energy"]
    assert energy > 0 and energy % 2 == 0
    assert report["status"] == "PASS"
    target_row = report["target_row"]

    loads = [0] * 680
    for index in state["self_indices"]:
        for row in self_options[index][1]:
            loads[row] += 1
    for index in state["pair_indices"]:
        for row in pair_options[index]:
            loads[row] += 1
    defect = energy // 2
    assert Counter(loads) == Counter({1: 680 - 2 * defect, 0: defect, 2: defect})
    assert load_energy(loads) == energy
    holes = {row for row, load in enumerate(loads) if load == 0}
    selected_pairs = {
        index: frozenset(pair_options[index]) for index in state["pair_indices"]
    }

    frozen = {tuple(sorted(rows)) for rows in pair_options}
    assert len(frozen) == len(pair_options)
    representatives, orbit_index = owner_orbits()
    reflection = reflection_action(representatives, orbit_index)
    nonfixed = [owner for owner in range(1430) if owner < reflection[owner]]
    reduced = {}
    for row, owner in enumerate(nonfixed):
        reduced[owner] = reduced[reflection[owner]] = row

    top = read_records(args.top)
    reservoir = read_records(args.reservoir)
    assert len(top) == report["top_k_retained"]
    assert len(reservoir) == report["reservoir_union_masks"]

    literal_replays = 0
    best_literal_checked = False
    for expected_tier, records in (("top", top), ("reservoir", reservoir)):
        keys = []
        ranks = []
        for record in records:
            assert record["tier"] == expected_tier
            rows = integers(record["rows"])
            core = integers(record["core"])
            order = integers(record["order"])
            reflected_core = integers(record["reflected_core"])
            reflected_order = integers(record["reflected_order"])
            owner_ids = integers(record["owner_ids"])
            reflected_ids = integers(record["reflected_owner_ids"])
            covered_holes = integers(record["covered_incumbent_holes"])
            key = tuple(rows)
            assert len(rows) == len(set(rows)) == 10 and rows == tuple(sorted(rows))
            assert target_row in rows and key not in frozen
            assert len(core) == len(set(core)) == 5
            assert len(order) == len(set(order)) == 10
            assert not (set(core) & set(order))
            assert reflected_core == tuple(sorted((-value) % K for value in core))
            assert reflected_order == tuple((-value) % K for value in order)

            owners = deck_masks(core, order)
            replay_ids = tuple(
                orbit_index[canonical_orbit_mask(owner)] for owner in owners
            )
            assert replay_ids == owner_ids and len(set(owner_ids)) == 10
            assert reflected_ids == tuple(reflection[owner] for owner in owner_ids)
            assert not (set(owner_ids) & set(reflected_ids))
            assert rows == tuple(sorted(reduced[owner] for owner in owner_ids))
            assert covered_holes == tuple(row for row in rows if row in holes)
            literal_replays += 1

            row_set = frozenset(rows)
            add_base = sum(-1 if loads[row] == 0 else 1 if loads[row] == 1 else 3
                           for row in rows)
            holes_filled = len(row_set & holes)
            choices = []
            for outgoing_index, outgoing in selected_pairs.items():
                remove_base = sum(
                    -1 if loads[row] == 2 else 1 if loads[row] == 1 else 3
                    for row in outgoing
                )
                intersection = len(row_set & outgoing)
                delta = add_base + remove_base - 2 * intersection
                single_intersection = sum(
                    loads[row] == 1 for row in row_set & outgoing
                )
                hole_change = (
                    -holes_filled
                    + sum(loads[row] == 1 for row in outgoing)
                    - single_intersection
                )
                choices.append((delta, hole_change, outgoing_index))
            best = min(choices)
            assert int(record["best_outgoing_pair_index"]) == best[2]
            assert int(record["delta"]) == best[0]
            assert int(record["new_energy"]) == energy + best[0]
            assert int(record["hole_change"]) == best[1]
            assert int(record["holes_filled"]) == holes_filled
            assert int(record["add_base"]) == add_base

            if not best_literal_checked and key == tuple(report["best_rows"]):
                changed = loads[:]
                for row in selected_pairs[best[2]]:
                    changed[row] -= 1
                for row in row_set:
                    changed[row] += 1
                assert load_energy(changed) == energy + best[0]
                assert changed.count(0) - loads.count(0) == best[1]
                best_literal_checked = True

            keys.append(key)
            ranks.append((best[0], best[1], key))
        assert len(keys) == len(set(keys))
        assert ranks == sorted(ranks)

    assert best_literal_checked
    top_delta = Counter(int(record["delta"]) for record in top)
    top_hole_change = Counter(int(record["hole_change"]) for record in top)
    assert {str(key): value for key, value in sorted(top_delta.items())} == report[
        "top_delta_histogram"
    ]
    assert {str(key): value for key, value in sorted(top_hole_change.items())} == report[
        "top_hole_change_histogram"
    ]
    reservoir_coverage = Counter()
    for record in reservoir:
        reservoir_coverage.update(integers(record["covered_incumbent_holes"]))
    assert set(reservoir_coverage) == holes
    assert min(reservoir_coverage.values()) >= report["reservoir_per_hole"]
    assert {str(key): value for key, value in sorted(reservoir_coverage.items())} == report[
        "reservoir_hole_coverage"
    ]

    best = top[0]
    assert int(best["delta"]) == report["best_delta"]
    assert int(best["new_energy"]) == report["best_new_energy"]
    assert int(best["hole_change"]) == report["best_hole_change"]
    assert int(best["best_outgoing_pair_index"]) == report[
        "best_outgoing_pair_index"
    ]
    assert list(integers(best["rows"])) == report["best_rows"]

    print(json.dumps({
        "status": "PASS",
        "incumbent_energy": energy,
        "target_row": target_row,
        "top_records_replayed": len(top),
        "reservoir_records_replayed": len(reservoir),
        "physical_witnesses_replayed": literal_replays,
        "top_unique_masks": len({integers(record["rows"]) for record in top}),
        "reservoir_unique_masks": len({
            integers(record["rows"]) for record in reservoir
        }),
        "top_reservoir_overlap": len(
            {integers(record["rows"]) for record in top}
            & {integers(record["rows"]) for record in reservoir}
        ),
        "reservoir_holes_covered": len(reservoir_coverage),
        "minimum_reservoir_hole_degree": min(reservoir_coverage.values()),
        "best_delta": int(best["delta"]),
        "best_new_energy": int(best["new_energy"]),
        "best_hole_change": int(best["hole_change"]),
        "best_outgoing_pair_index": int(best["best_outgoing_pair_index"]),
        "best_rows": list(integers(best["rows"])),
        "scope": (
            "full independent replay of every emitted physical witness and "
            "all 54 outgoing swaps; global top-K completeness follows from "
            "the separately audited bounded-shard theorem"
        ),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
