#!/usr/bin/env python3
"""Enumerate target-directed native C8 creators of T0 and typed currents.

Substantive execution belongs on H100.  Every returned cycle is a literal
alternating incidence C8 in the canonical semilength-six factor.  Exact
owner, upper/lower q1, upper/lower q2 support and lifted topology/residence
are replayed after the toggle.
"""

from __future__ import annotations

import json

import audit_msw_t0v_tensor_residence_20260814 as base
import search_msw_t0_twohex_typed_safe_20260814 as search


def encoded_with_loads(current, old, new):
    return [
        {
            "value": base.bitword(value, search.N),
            "delta": amount,
            "old_load": old[value],
            "new_load": new[value],
        }
        for value, amount in sorted(current.items())
    ]


def main():
    canonical = base.canonical_edges(search.M)
    old_decks = search.decks(canonical)
    by_owner, by_colour = search.deck_maps(canonical)

    cycles = {}
    for owner0, selected0 in by_owner.items():
        if len(selected0) != 2:
            continue
        selected0 = tuple(selected0)
        for keep_index in range(2):
            other0 = selected0[keep_index]
            incoming3 = selected0[1 - keep_index]
            for added0 in range(search.N):
                if owner0 >> added0 & 1:
                    continue
                outgoing0 = owner0 | 1 << added0
                if (owner0, outgoing0) in canonical:
                    continue
                if other0 | outgoing0 != search.TARGET:
                    continue
                for owner1 in by_colour[outgoing0]:
                    if owner1 == owner0 or len(by_owner[owner1]) != 2:
                        continue
                    other1 = next(value for value in by_owner[owner1] if value != outgoing0)
                    for added1 in range(search.N):
                        if owner1 >> added1 & 1:
                            continue
                        outgoing1 = owner1 | 1 << added1
                        if (owner1, outgoing1) in canonical or outgoing1 in (outgoing0, incoming3):
                            continue
                        for owner2 in by_colour[outgoing1]:
                            if owner2 in (owner0, owner1) or len(by_owner[owner2]) != 2:
                                continue
                            other2 = next(value for value in by_owner[owner2] if value != outgoing1)
                            for added2 in range(search.N):
                                if owner2 >> added2 & 1:
                                    continue
                                outgoing2 = owner2 | 1 << added2
                                if (
                                    (owner2, outgoing2) in canonical
                                    or outgoing2 in (outgoing0, outgoing1, incoming3)
                                ):
                                    continue
                                for owner3 in by_colour[outgoing2]:
                                    if owner3 in (owner0, owner1, owner2):
                                        continue
                                    if len(by_owner[owner3]) != 2:
                                        continue
                                    if owner3 & incoming3 != owner3:
                                        continue
                                    if (owner3, incoming3) in canonical:
                                        continue
                                    other3 = next(
                                        (value for value in by_owner[owner3] if value != outgoing2),
                                        None,
                                    )
                                    if other3 is None:
                                        continue
                                    incidences = frozenset((
                                        (owner0, incoming3), (owner0, outgoing0),
                                        (owner1, outgoing0), (owner1, outgoing1),
                                        (owner2, outgoing1), (owner2, outgoing2),
                                        (owner3, outgoing2), (owner3, incoming3),
                                    ))
                                    if len(incidences) != 8:
                                        continue
                                    statuses = [incidence in canonical for incidence in incidences]
                                    if sum(statuses) != 4:
                                        continue
                                    cycles[incidences] = {
                                        "owners": (owner0, owner1, owner2, owner3),
                                        "colours": (outgoing0, outgoing1, outgoing2, incoming3),
                                    }

    rows = []
    counts = {"creators": 0, "q2_safe": 0, "lower_q1_safe": 0, "all_typed_safe": 0}
    for incidences, cycle in cycles.items():
        selected = set(canonical)
        selected.symmetric_difference_update(incidences)
        new_decks = search.decks(selected)
        currents = {}
        casualties = {}
        for name in old_decks:
            currents[name], casualties[name] = search.current(old_decks[name], new_decks[name])
        if currents["upper_q2"][search.TARGET] <= 0:
            continue
        counts["creators"] += 1
        if not casualties["upper_q2"]:
            counts["q2_safe"] += 1
        if not casualties["lower_q1"]:
            counts["lower_q1_safe"] += 1
        if not any(casualties.values()):
            counts["all_typed_safe"] += 1
        rows.append({
            "owners": [base.bitword(value, search.N) for value in cycle["owners"]],
            "colours": [base.bitword(value, search.N) for value in cycle["colours"]],
            "q2_safe": not casualties["upper_q2"],
            "lower_q1_safe": not casualties["lower_q1"],
            "all_typed_safe": not any(casualties.values()),
            "casualties": {
                name: [base.bitword(value, search.N) for value in values]
                for name, values in casualties.items() if values
            },
            "currents": {
                name: search.encoded_current(current)
                for name, current in currents.items()
            },
            "topology_residence": search.topology_and_residence(selected, canonical),
        })
    hexes = search.enumerate_hexes(canonical)
    mixed_counts = {
        "owner_disjoint_tested": 0,
        "q2_safe": 0,
        "lower_q1_safe": 0,
        "all_typed_safe": 0,
    }
    mixed_rows = []
    for incidences, cycle in cycles.items():
        c8_owners = set(cycle["owners"])
        for hex_index, hexagon in enumerate(hexes):
            if c8_owners & hexagon["owners"]:
                continue
            mixed_counts["owner_disjoint_tested"] += 1
            selected = set(canonical)
            selected.symmetric_difference_update(incidences)
            selected.symmetric_difference_update(hexagon["incidences"])
            new_decks = search.decks(selected)
            currents = {}
            casualties = {}
            for name in old_decks:
                currents[name], casualties[name] = search.current(old_decks[name], new_decks[name])
            if new_decks["upper_q2"][search.TARGET] == 0:
                continue
            if not casualties["upper_q2"]:
                mixed_counts["q2_safe"] += 1
            if not casualties["lower_q1"]:
                mixed_counts["lower_q1_safe"] += 1
            if any(casualties.values()):
                continue
            mixed_counts["all_typed_safe"] += 1
            if len(mixed_rows) < 20:
                mixed_rows.append({
                    "c8_owners": [base.bitword(value, search.N) for value in cycle["owners"]],
                    "c8_colours": [base.bitword(value, search.N) for value in cycle["colours"]],
                    "c6_index": hex_index,
                    "c6_core": base.bitword(hexagon["core"], search.N),
                    "c6_active_one_based": [bit + 1 for bit in hexagon["active"]],
                    "c6_owners": sorted(base.bitword(value, search.N) for value in hexagon["owners"]),
                    "c6_colours": sorted(base.bitword(value, search.N) for value in hexagon["colours"]),
                    "currents": {
                        name: encoded_with_loads(
                            current, old_decks[name], new_decks[name]
                        )
                        for name, current in currents.items()
                    },
                    "topology_residence": search.topology_and_residence(selected, canonical),
                })
    print(json.dumps({
        "status": "PASS",
        "target_directed_cycle_supports": len(cycles),
        "counts": counts,
        "rows": rows,
        "mixed_c8_c6_counts": mixed_counts,
        "mixed_c8_c6_rows": mixed_rows,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
