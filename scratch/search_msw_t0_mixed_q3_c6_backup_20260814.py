#!/usr/bin/env python3
"""Search one owner-disjoint native C6 backing the mixed packet's q3 loss.

Substantive execution belongs on H100.  Every initially alternating
semilength-six C6 disjoint from the seven-owner C8+C6 packet is toggled with
that packet.  The complete typed decks through q2 and the complete linear
upper-q3 deck are recomputed; solutions must retain every old support value
and retain the created T0.
"""

from __future__ import annotations

import json
from collections import Counter

import audit_msw_t0v_tensor_residence_20260814 as base
import audit_msw_t0v_mixed_c8_c6_tensor_20260814 as tensor
import audit_msw_t0v_mixed_q3_loss_providers_20260814 as q3trace
import search_msw_t0_twohex_typed_safe_20260814 as search


W3 = base.bits("110111001111")


def q3_deck(selected):
    result = Counter()
    for _, colours in q3trace.paths(selected):
        for start in range(len(colours) - 2):
            result[colours[start] | colours[start + 1] | colours[start + 2]] += 1
    return result


def current(old, new):
    result = Counter(new)
    result.subtract(old)
    return Counter({value: amount for value, amount in result.items() if amount})


def rows(delta, old, new):
    return [
        {
            "value": base.bitword(value, 12),
            "delta": amount,
            "old_load": old[value],
            "new_load": new[value],
        }
        for value, amount in sorted(delta.items())
    ]


def main():
    canonical = base.canonical_edges(6)
    old_typed = search.decks(canonical)
    old_q3 = q3_deck(canonical)
    c8, c6 = tensor.prefix_packet()
    mixed_support = c8 | c6
    mixed_owners = {owner for owner, _ in mixed_support}
    mixed = set(canonical)
    mixed.symmetric_difference_update(mixed_support)
    assert q3_deck(mixed)[W3] == 0

    hexes = search.enumerate_hexes(canonical)
    counts = {
        "alternating_c6": len(hexes),
        "owner_disjoint_tested": 0,
        "raw_creates_q3_target": 0,
        "typed_q2_safe": 0,
        "creates_q3_target": 0,
        "all_q3_support_safe": 0,
    }
    solutions = []
    raw_creator_indices = []
    for index, hexagon in enumerate(hexes):
        if mixed_owners & hexagon["owners"]:
            continue
        counts["owner_disjoint_tested"] += 1
        selected = set(mixed)
        selected.symmetric_difference_update(hexagon["incidences"])
        new_q3 = q3_deck(selected)
        if new_q3[W3] > 0:
            counts["raw_creates_q3_target"] += 1
            raw_creator_indices.append(index)
        new_typed = search.decks(selected)
        typed_currents = {}
        typed_casualty = False
        for name in old_typed:
            delta = current(old_typed[name], new_typed[name])
            typed_currents[name] = delta
            if any(
                amount < 0 and new_typed[name][value] == 0
                for value, amount in delta.items()
            ):
                typed_casualty = True
        if typed_casualty or new_typed["upper_q2"][search.TARGET] == 0:
            continue
        counts["typed_q2_safe"] += 1
        if new_q3[W3] == 0:
            continue
        counts["creates_q3_target"] += 1
        q3_current = current(old_q3, new_q3)
        q3_casualties = [
            value for value, amount in q3_current.items()
            if amount < 0 and new_q3[value] == 0
        ]
        if q3_casualties:
            continue
        counts["all_q3_support_safe"] += 1
        solutions.append({
            "index": index,
            "core": base.bitword(hexagon["core"], 12),
            "active_one_based": [bit + 1 for bit in hexagon["active"]],
            "owners": sorted(base.bitword(value, 12) for value in hexagon["owners"]),
            "colours": sorted(base.bitword(value, 12) for value in hexagon["colours"]),
            "typed_currents": {
                name: rows(delta, old_typed[name], new_typed[name])
                for name, delta in typed_currents.items()
            },
            "q3_current": rows(q3_current, old_q3, new_q3),
            "topology_residence": search.topology_and_residence(selected, canonical),
        })

    pair_counts = {
        "owner_disjoint_tested": 0,
        "typed_q2_safe": 0,
        "creates_q3_target": 0,
        "all_q3_support_safe": 0,
    }
    pair_solutions = []
    seen_pairs = set()
    for creator_index in raw_creator_indices:
        creator = hexes[creator_index]
        for helper_index, helper in enumerate(hexes):
            pair = tuple(sorted((creator_index, helper_index)))
            if helper_index == creator_index or pair in seen_pairs:
                continue
            seen_pairs.add(pair)
            if mixed_owners & helper["owners"] or creator["owners"] & helper["owners"]:
                continue
            pair_counts["owner_disjoint_tested"] += 1
            selected = set(mixed)
            selected.symmetric_difference_update(creator["incidences"])
            selected.symmetric_difference_update(helper["incidences"])
            new_typed = search.decks(selected)
            typed_currents = {}
            typed_casualty = False
            for name in old_typed:
                delta = current(old_typed[name], new_typed[name])
                typed_currents[name] = delta
                if any(
                    amount < 0 and new_typed[name][value] == 0
                    for value, amount in delta.items()
                ):
                    typed_casualty = True
            if typed_casualty or new_typed["upper_q2"][search.TARGET] == 0:
                continue
            pair_counts["typed_q2_safe"] += 1
            new_q3 = q3_deck(selected)
            if new_q3[W3] == 0:
                continue
            pair_counts["creates_q3_target"] += 1
            q3_current = current(old_q3, new_q3)
            if any(
                amount < 0 and new_q3[value] == 0
                for value, amount in q3_current.items()
            ):
                continue
            pair_counts["all_q3_support_safe"] += 1
            if len(pair_solutions) < 20:
                pair_solutions.append({
                    "indices": list(pair),
                    "circuits": [
                        {
                            "index": index,
                            "core": base.bitword(hexes[index]["core"], 12),
                            "active_one_based": [bit + 1 for bit in hexes[index]["active"]],
                            "owners": sorted(base.bitword(value, 12) for value in hexes[index]["owners"]),
                            "colours": sorted(base.bitword(value, 12) for value in hexes[index]["colours"]),
                        }
                        for index in pair
                    ],
                    "typed_currents": {
                        name: rows(delta, old_typed[name], new_typed[name])
                        for name, delta in typed_currents.items()
                    },
                    "q3_current": rows(q3_current, old_q3, new_q3),
                    "topology_residence": search.topology_and_residence(selected, canonical),
                })
    print(json.dumps({
        "status": "PASS",
        "counts": counts,
        "solutions": solutions,
        "two_c6_counts": pair_counts,
        "two_c6_solutions": pair_solutions,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
