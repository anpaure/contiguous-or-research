#!/usr/bin/env python3
"""Compact hostile audit of candidate 5's singleton two-target rail.

Substantive execution belongs on H100.  This binds the literal ranks, the
complete adjacent-window five-owner census, the exhaustive target-relevant
native C6/C8 single-cycle banks, and the inverse-current obstruction for
commuting owner-and-colour-disjoint pairs from those banks.
"""

from __future__ import annotations

import json

import audit_msw_t0v_tensor_typed_currents_20260814 as typed
import audit_msw_t0v_mixed_q3_closed_tensor_20260814 as q3closed
import search_c16_two_target_rail_candidate5_20260814 as search


def target_edges(selected, target):
    return {
        incidence for incidence in selected
        if incidence[1] & ~target == 0
    }


def single_counts(selected, supports):
    base_edges = {
        target: target_edges(selected, target)
        for target in (search.A, search.B)
    }
    counts = {
        "creates_A": 0,
        "creates_B": 0,
        "creates_both": 0,
    }
    for support in supports:
        loads = {}
        for target in (search.A, search.B):
            edges = set(base_edges[target])
            edges.symmetric_difference_update(
                incidence for incidence in support
                if incidence[1] & ~target == 0
            )
            loads[target] = search.target_provider_count(edges, target)
        counts["creates_A"] += bool(loads[search.A])
        counts["creates_B"] += bool(loads[search.B])
        counts["creates_both"] += bool(loads[search.A] and loads[search.B])
    return counts


def main():
    canonical, selected = search.current_factor()
    old_typed = typed.typed_decks(selected)
    old_q3 = q3closed.q3_deck(selected)

    assert search.A.bit_count() == search.B.bit_count() == 12
    assert (search.A & search.B).bit_count() == 11
    assert (search.A ^ search.B).bit_count() == 2
    assert old_q3[search.A] == old_q3[search.B] == 0
    assert search.pairsearch.common_binary_phase(canonical, selected)

    rails, missing_histogram = search.rail_rows(selected)
    assert sum(missing_histogram.values()) == 721710
    assert missing_histogram == {
        3: 404,
        4: 8406,
        5: 61536,
        6: 202132,
        7: 296940,
        8: 152292,
    }
    assert len(rails) == 8810
    c6_closures = set()
    c8_closures = set()
    for rail in rails:
        absent = rail["absent"]
        if len(absent) == 3:
            c6_closures.update(search.one_cycle(absent, selected))
        c8_closures.update(search.complete_c8(absent, selected))
    assert not c6_closures and not c8_closures

    banks = {}
    starts_count = None
    single = {}
    for kind, owner_count in (("C6", 3), ("C8", 4)):
        starts, supports = search.target_relevant_cycles(selected, owner_count)
        if starts_count is None:
            starts_count = len(starts)
        assert len(starts) == starts_count == 1936
        banks[kind] = supports
        single[kind] = {
            "target_start_arcs": len(starts),
            "distinct_target_relevant_cycles": len(supports),
            **single_counts(selected, supports),
        }
    assert len(banks["C6"]) == 382
    assert len(banks["C8"]) == 1495
    assert single["C6"]["creates_both"] == 0
    assert single["C8"]["creates_both"] == 0

    pair_counts, solutions = search.pair_atlas(
        selected, canonical, old_typed, old_q3, banks, 20
    )
    expected_zero = {
        "inverse_typed_signature_pairs": 0,
        "owner_colour_disjoint_inverse_pairs": 0,
        "zero_typed_create_both_targets": 0,
        "nonpath_factor": 0,
        "zero_typed_binary": 0,
    }
    assert pair_counts == {
        "C6+C6": expected_zero,
        "C6+C8": expected_zero,
        "C8+C8": expected_zero,
    }
    assert not solutions

    report = {
        "status": "PASS",
        "literal_ranks": {
            "factor_owner_rank": 9,
            "target_A_rank": search.A.bit_count(),
            "target_B_rank": search.B.bit_count(),
            "intersection_rank": (search.A & search.B).bit_count(),
            "target_exchange_distance": (search.A ^ search.B).bit_count() // 2,
        },
        "targets": {
            "A": search.base.bitword(search.A, search.WIDTH),
            "B": search.base.bitword(search.B, search.WIDTH),
            "intersection": search.base.bitword(search.A & search.B, search.WIDTH),
            "current_load_A": old_q3[search.A],
            "current_load_B": old_q3[search.B],
        },
        "corrected_middle_owner_form": (
            "O_i=(A intersection B) minus a two-element set; consecutive "
            "two-element omissions share one element"
        ),
        "five_owner_adjacent_window_census": {
            "total": sum(missing_histogram.values()),
            "internal_upper_q1_colours_equal": 0,
            "internal_upper_q1_colours_distinct": sum(missing_histogram.values()),
            "missing_incidence_histogram": dict(sorted(missing_histogram.items())),
            "rails_missing_at_most_four": len(rails),
            "native_C6_closures": len(c6_closures),
            "native_C8_closures": len(c8_closures),
        },
        "single_cycle_banks": single,
        "commuting_pair_counts": pair_counts,
        "solutions": solutions,
        "completeness_scope": (
            "Every native alternating C6/C8 in the current candidate-5 m=9 "
            "factor containing an absent A/B-provider incidence; every "
            "commuting owner-and-colour-disjoint pair from those banks. "
            "Overlapping sequential cycles and open noncycle rails are excluded."
        ),
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
