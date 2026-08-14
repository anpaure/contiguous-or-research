#!/usr/bin/env python3
"""Search one native C6 closing the typed-safe q3 C12 relay.

Substantive execution belongs on H100.  The fixed state is the mixed T0
C8+C6 plus the unique typed-q2-safe target-relevant C12.  Every initially
alternating C6 disjoint from all thirteen changed owners is tested on the
complete typed decks through q3.
"""

from __future__ import annotations

import json
from collections import Counter

import audit_msw_t0v_tensor_residence_20260814 as base
import audit_msw_t0v_mixed_c8_c6_tensor_20260814 as tensor
import audit_msw_t0v_mixed_q3_loss_providers_20260814 as q3trace
import search_msw_t0_twohex_typed_safe_20260814 as search
import search_msw_t0_mixed_q3_c8_backup_20260814 as c8search


W3 = base.bits("110111001111")
H3 = base.bits("110101101111")
C12_OWNERS = [
    "110100000111",
    "110000001111",
    "110000101101",
    "110100100101",
    "110000100111",
    "110001000111",
]
C12_COLOURS = [
    "110100001111",
    "110000101111",
    "110100101101",
    "110100100111",
    "110001100111",
    "110101000111",
]


def cycle_support(owner_words, colour_words):
    owners = list(map(base.bits, owner_words))
    colours = list(map(base.bits, colour_words))
    support = set()
    for index, colour in enumerate(colours):
        support.add((owners[index], colour))
        support.add((owners[(index + 1) % len(owners)], colour))
    return support


def q3_deck(selected):
    result = Counter()
    try:
        path_bank = q3trace.paths(selected)
    except AssertionError:
        return None
    for _, colours in path_bank:
        for start in range(len(colours) - 2):
            result[colours[start] | colours[start + 1] | colours[start + 2]] += 1
    return result


def difference(old, new):
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
    mixed_c8, mixed_c6 = tensor.prefix_packet()
    c12 = cycle_support(C12_OWNERS, C12_COLOURS)
    fixed_support = mixed_c8 | mixed_c6 | c12
    fixed_owners = {owner for owner, _ in fixed_support}
    fixed = set(canonical)
    fixed.symmetric_difference_update(fixed_support)
    fixed_typed = search.decks(fixed)
    fixed_q3 = q3_deck(fixed)
    assert fixed_q3[W3] == 2 and fixed_q3[H3] == 0
    assert not any(
        amount < 0 and fixed_typed[name][value] == 0
        for name in old_typed
        for value, amount in difference(old_typed[name], fixed_typed[name]).items()
    )

    hexes = search.enumerate_hexes(canonical)
    counts = {
        "alternating_c6": len(hexes),
        "owner_disjoint_tested": 0,
        "raw_creates_h3": 0,
        "typed_q2_safe": 0,
        "all_q3_support_safe": 0,
    }
    solutions = []
    for index, hexagon in enumerate(hexes):
        if fixed_owners & hexagon["owners"]:
            continue
        counts["owner_disjoint_tested"] += 1
        selected = set(fixed)
        selected.symmetric_difference_update(hexagon["incidences"])
        q3 = q3_deck(selected)
        if q3 is None:
            continue
        if q3[H3] > 0:
            counts["raw_creates_h3"] += 1
        new_typed = search.decks(selected)
        typed_currents = {
            name: difference(old_typed[name], new_typed[name])
            for name in old_typed
        }
        if any(
            amount < 0 and new_typed[name][value] == 0
            for name, delta in typed_currents.items()
            for value, amount in delta.items()
        ) or new_typed["upper_q2"][search.TARGET] == 0:
            continue
        counts["typed_q2_safe"] += 1
        q3_current = difference(old_q3, q3)
        if q3[W3] == 0 or q3[H3] == 0 or any(
            amount < 0 and q3[value] == 0
            for value, amount in q3_current.items()
        ):
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
            "q3_current": rows(q3_current, old_q3, q3),
            "topology_residence": search.topology_and_residence(selected, canonical),
        })
    c8_cycles = c8search.alternating_c8s(canonical)
    c8_counts = {
        "alternating_c8": len(c8_cycles),
        "owner_disjoint_tested": 0,
        "raw_creates_h3": 0,
        "typed_q2_safe": 0,
        "all_q3_support_safe": 0,
    }
    c8_solutions = []
    for support, cycle in c8_cycles.items():
        if fixed_owners & set(cycle["owners"]):
            continue
        c8_counts["owner_disjoint_tested"] += 1
        selected = set(fixed)
        selected.symmetric_difference_update(support)
        q3 = q3_deck(selected)
        if q3 is None:
            continue
        if q3[H3] > 0:
            c8_counts["raw_creates_h3"] += 1
        new_typed = search.decks(selected)
        typed_currents = {
            name: difference(old_typed[name], new_typed[name])
            for name in old_typed
        }
        if any(
            amount < 0 and new_typed[name][value] == 0
            for name, delta in typed_currents.items()
            for value, amount in delta.items()
        ) or new_typed["upper_q2"][search.TARGET] == 0:
            continue
        c8_counts["typed_q2_safe"] += 1
        q3_current = difference(old_q3, q3)
        if q3[W3] == 0 or q3[H3] == 0 or any(
            amount < 0 and q3[value] == 0
            for value, amount in q3_current.items()
        ):
            continue
        c8_counts["all_q3_support_safe"] += 1
        c8_solutions.append({
            "owners": [base.bitword(value, 12) for value in cycle["owners"]],
            "colours": [base.bitword(value, 12) for value in cycle["colours"]],
            "typed_currents": {
                name: rows(delta, old_typed[name], new_typed[name])
                for name, delta in typed_currents.items()
            },
            "q3_current": rows(q3_current, old_q3, q3),
            "topology_residence": search.topology_and_residence(selected, canonical),
        })
    print(json.dumps({
        "status": "PASS",
        "c6_counts": counts,
        "c6_solutions": solutions,
        "c8_counts": c8_counts,
        "c8_solutions": c8_solutions,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
