#!/usr/bin/env python3
"""Audit all resource collisions of the 164 canonical D5 Johnson squares.

Substantive execution belongs on H100 only.  This rebuilds the frozen D5
factor and its simultaneous switch, extracts every nontrivial distance-two
terminal triple, constructs the unique commuting fourth corner, and counts
owner/lower/upper overlaps both within the square catalogue and against the
old/new factors.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import search_t2_cross_suffix_alternating_cycles_20260813 as base  # noqa:E402


def jdist(left, right):
    return (left ^ right).bit_count() // 2


def histogram(counter):
    return {str(key): value for key, value in sorted(counter.items())}


def factor_edges(selected):
    """Return suppressed owner edges labelled by their rank-(m+1) colour."""
    by_upper = {}
    for owner, upper in selected:
        by_upper.setdefault(upper, []).append(owner)
    assert all(len(owners) == 2 for owners in by_upper.values())
    edges = set()
    for upper, owners in by_upper.items():
        left, right = owners
        assert (left & right).bit_count() + 1 == left.bit_count()
        edges.add((
            min(left, right), max(left, right), left & right, upper
        ))
    return edges


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("selection")
    parser.add_argument("certificate")
    args = parser.parse_args()
    selection_raw = Path(args.selection).read_bytes()
    certificate_raw = Path(args.certificate).read_bytes()
    selection = json.loads(selection_raw)
    certificate = json.loads(certificate_raw)
    selection_sha = hashlib.sha256(selection_raw).hexdigest()
    assert selection_sha == (
        "94deb656dac1d8955b20d851e92600156d703842d6de169d4b6bea356fa3ec32"
    )
    assert certificate["selection_sha256"] == selection_sha

    m = 11
    old_factor = set(base.canonical_edges(m))
    base.apply_t2(old_factor, list(base.dyck_words(5)))
    by_owner, by_upper = base.factor_maps(old_factor)
    state = {
        base.bits(word): value
        for word, value in certificate["owner_union_graph"][
            "three_state_assignment"
        ]
    }

    selected_rows = []
    all_rows = []
    for item in selection["selection"]:
        owners = tuple(
            base.bits(word) for word in item["candidate"]["owners"]
        )
        uppers = tuple(
            base.bits(word) for word in item["candidate"]["new_colours"]
        )
        rows = [
            (owners[index], uppers[index - 1], uppers[index])
            for index in range(len(owners))
        ]
        selected_rows.append(rows)
        all_rows.extend(rows)
    removed = {(tail, old) for tail, old, _ in all_rows}
    added = {(tail, new) for tail, _, new in all_rows}
    new_factor = (old_factor - removed) | added

    old_edges = factor_edges(old_factor)
    new_edges = factor_edges(new_factor)
    old_owners = {owner for owner, _ in old_factor}
    new_owners = {owner for owner, _ in new_factor}
    old_lowers = {edge[2] for edge in old_edges}
    new_lowers = {edge[2] for edge in new_edges}
    old_uppers = {upper for _, upper in old_factor}
    new_uppers = {upper for _, upper in new_factor}
    assert old_owners == new_owners

    owner_load = Counter()
    lower_load = Counter()
    upper_load = Counter()
    edge_role_load = Counter()
    collateral_phase = Counter()
    direct_factor_overlap = Counter()
    records = []
    terminal_owners = set()
    touched_owners = set(state)

    for rows in selected_rows:
        removed_owner = {old: tail for tail, old, _ in rows}
        for tail, old_upper, new_upper in rows:
            old_head = next(owner for owner in by_upper[old_upper] if owner != tail)
            new_head = next(
                owner for owner in by_upper[new_upper]
                if owner != removed_owner[new_upper]
            )
            terminal_owners.update((tail, old_head, new_head))

    for rows in selected_rows:
        removed_owner = {old: tail for tail, old, _ in rows}
        for tail, old_upper, new_upper in rows:
            old_head = next(owner for owner in by_upper[old_upper] if owner != tail)
            new_head = next(
                owner for owner in by_upper[new_upper]
                if owner != removed_owner[new_upper]
            )
            if state[old_head] == state[new_head]:
                continue
            if jdist(old_head, new_head) != 2:
                continue

            core = tail & old_head & new_head
            assert core.bit_count() == m - 2
            D = core | (old_head & ~tail) | (new_head & ~tail)
            assert D.bit_count() == m
            assert len({tail, old_head, new_head, D}) == 4
            square = (tail, old_head, D, new_head)
            assert all(
                jdist(square[index], square[(index + 1) % 4]) == 1
                for index in range(4)
            )
            lowers = tuple(
                square[index] & square[(index + 1) % 4]
                for index in range(4)
            )
            uppers = tuple(
                square[index] | square[(index + 1) % 4]
                for index in range(4)
            )
            assert len(set(lowers)) == len(set(uppers)) == 4

            old_collateral = (
                min(D, new_head), max(D, new_head), lowers[2], uppers[2]
            )
            new_collateral = (
                min(old_head, D), max(old_head, D), lowers[1], uppers[1]
            )
            phase = (old_collateral in old_edges, new_collateral in new_edges)
            collateral_phase[phase] += 1

            owner_load[D] += 1
            for lower in lowers:
                lower_load[lower] += 1
            for upper in uppers:
                upper_load[upper] += 1
            for index, role in enumerate(("TB", "BD", "DC", "CT")):
                edge_role_load[(
                    min(square[index], square[(index + 1) % 4]),
                    max(square[index], square[(index + 1) % 4]),
                    lowers[index], uppers[index], role,
                )] += 1

            direct_factor_overlap[(
                "D_is_existing_owner", D in old_owners
            )] += 1
            direct_factor_overlap[(
                "D_is_touched_owner", D in touched_owners
            )] += 1
            direct_factor_overlap[(
                "D_is_prescribed_terminal", D in terminal_owners
            )] += 1
            direct_factor_overlap[(
                "lower_values_in_old_factor", sum(x in old_lowers for x in lowers)
            )] += 1
            direct_factor_overlap[(
                "lower_values_in_new_factor", sum(x in new_lowers for x in lowers)
            )] += 1
            direct_factor_overlap[(
                "upper_values_in_factor", sum(x in old_uppers for x in uppers)
            )] += 1
            direct_factor_overlap[(
                "square_edges_old", sum(
                    (
                        min(square[i], square[(i + 1) % 4]),
                        max(square[i], square[(i + 1) % 4]),
                        lowers[i], uppers[i],
                    ) in old_edges for i in range(4)
                )
            )] += 1
            direct_factor_overlap[(
                "square_edges_new", sum(
                    (
                        min(square[i], square[(i + 1) % 4]),
                        max(square[i], square[(i + 1) % 4]),
                        lowers[i], uppers[i],
                    ) in new_edges for i in range(4)
                )
            )] += 1
            records.append((tail, old_head, new_head, D, lowers, uppers))

    assert len(records) == 164
    assert collateral_phase == Counter({(False, False): 139,
                                        (False, True): 12,
                                        (True, False): 13})

    # Every square uses TB and CT, the prescribed old/new D5 transitions.
    assert direct_factor_overlap[("square_edges_old", 1)] == 137
    assert direct_factor_overlap[("square_edges_old", 2)] == 27
    assert direct_factor_overlap[("square_edges_new", 1)] == 145
    assert direct_factor_overlap[("square_edges_new", 2)] == 19

    print(json.dumps({
        "status": "PASS",
        "selection_sha256": selection_sha,
        "certificate_sha256": hashlib.sha256(certificate_raw).hexdigest(),
        "distance_two_rows": len(records),
        "collateral_phase_histogram": {
            str(key): value for key, value in sorted(collateral_phase.items())
        },
        "auxiliary_owner": {
            "occurrences": sum(owner_load.values()),
            "distinct": len(owner_load),
            "load_histogram": histogram(Counter(owner_load.values())),
            "all_are_existing_middle_level_owners": all(
                owner in old_owners for owner in owner_load
            ),
        },
        "four_edge_square_resource_occurrences": {
            "lower": sum(lower_load.values()),
            "upper": sum(upper_load.values()),
        },
        "four_edge_square_resource_distinct": {
            "lower": len(lower_load),
            "upper": len(upper_load),
        },
        "four_edge_square_resource_load_histogram": {
            "lower": histogram(Counter(lower_load.values())),
            "upper": histogram(Counter(upper_load.values())),
        },
        "distinct_square_resource_overlap_with_factor": {
            "lower_old": len(set(lower_load) & old_lowers),
            "lower_new": len(set(lower_load) & new_lowers),
            "upper_old": len(set(upper_load) & old_uppers),
            "upper_new": len(set(upper_load) & new_uppers),
        },
        "direct_factor_overlap_histogram": {
            str(key): value for key, value in sorted(
                direct_factor_overlap.items(), key=lambda item: str(item[0])
            )
        },
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
