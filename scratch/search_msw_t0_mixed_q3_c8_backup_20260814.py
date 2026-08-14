#!/usr/bin/env python3
"""Search one owner-disjoint native C8 backing the mixed packet's q3 loss.

Substantive execution belongs on H100.  All simple directed four-owner
cycles in the canonical alternating owner-arc digraph are enumerated.  Each
is toggled with the frozen mixed T0 packet and checked on the complete typed
decks through q3.
"""

from __future__ import annotations

import json
from collections import Counter, defaultdict

import audit_msw_t0v_tensor_residence_20260814 as base
import audit_msw_t0v_mixed_c8_c6_tensor_20260814 as tensor
import audit_msw_t0v_mixed_q3_loss_providers_20260814 as q3trace
import search_msw_t0_twohex_typed_safe_20260814 as search


W3 = base.bits("110111001111")


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


def alternating_c8s(canonical):
    by_colour = defaultdict(list)
    owners = set()
    for owner, colour in canonical:
        by_colour[colour].append(owner)
        owners.add(owner)
    outgoing = defaultdict(list)
    full = (1 << 12) - 1
    for owner in owners:
        absent = full ^ owner
        while absent:
            bit = absent & -absent
            absent -= bit
            colour = owner | bit
            if (owner, colour) in canonical:
                continue
            for next_owner in by_colour[colour]:
                outgoing[owner].append((next_owner, colour))

    cycles = {}
    for start in sorted(owners):
        path_owners = [start]
        path_colours = []

        def dfs():
            owner = path_owners[-1]
            if len(path_colours) == 3:
                for next_owner, colour in outgoing[owner]:
                    if next_owner != start or colour in path_colours:
                        continue
                    incidences = set()
                    all_colours = path_colours + [colour]
                    all_owners = path_owners
                    for index, qvalue in enumerate(all_colours):
                        left = all_owners[index]
                        right = all_owners[(index + 1) % 4]
                        incidences.add((left, qvalue))
                        incidences.add((right, qvalue))
                    support = frozenset(incidences)
                    cycles[support] = {
                        "owners": tuple(all_owners),
                        "colours": tuple(all_colours),
                    }
                return
            for next_owner, colour in outgoing[owner]:
                if next_owner <= start or next_owner in path_owners or colour in path_colours:
                    continue
                path_owners.append(next_owner)
                path_colours.append(colour)
                dfs()
                path_colours.pop()
                path_owners.pop()

        dfs()
    return cycles


def main():
    canonical = base.canonical_edges(6)
    old_typed = search.decks(canonical)
    old_q3 = q3_deck(canonical)
    c8, c6 = tensor.prefix_packet()
    mixed_support = c8 | c6
    mixed_owners = {owner for owner, _ in mixed_support}
    mixed = set(canonical)
    mixed.symmetric_difference_update(mixed_support)
    cycles = alternating_c8s(canonical)
    counts = {
        "alternating_c8": len(cycles),
        "owner_disjoint_tested": 0,
        "nonpath_factors": 0,
        "raw_creates_q3_target": 0,
        "typed_q2_safe": 0,
        "creates_q3_target": 0,
        "all_q3_support_safe": 0,
    }
    solutions = []
    raw_creators = []
    for support, cycle in cycles.items():
        if mixed_owners & set(cycle["owners"]):
            continue
        counts["owner_disjoint_tested"] += 1
        selected = set(mixed)
        selected.symmetric_difference_update(support)
        new_q3 = q3_deck(selected)
        if new_q3 is None:
            counts["nonpath_factors"] += 1
            continue
        if new_q3[W3] > 0:
            counts["raw_creates_q3_target"] += 1
            raw_creators.append((support, cycle))
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
        if any(
            amount < 0 and new_q3[value] == 0
            for value, amount in q3_current.items()
        ):
            continue
        counts["all_q3_support_safe"] += 1
        if len(solutions) < 20:
            solutions.append({
                "owners": [base.bitword(value, 12) for value in cycle["owners"]],
                "colours": [base.bitword(value, 12) for value in cycle["colours"]],
                "typed_currents": {
                    name: rows(delta, old_typed[name], new_typed[name])
                    for name, delta in typed_currents.items()
                },
                "q3_current": rows(q3_current, old_q3, new_q3),
                "topology_residence": search.topology_and_residence(selected, canonical),
            })

    hexes = search.enumerate_hexes(canonical)
    pair_counts = {
        "owner_disjoint_tested": 0,
        "nonpath_factors": 0,
        "typed_q2_safe": 0,
        "creates_q3_target": 0,
        "all_q3_support_safe": 0,
    }
    pair_solutions = []
    for c8_support, c8_cycle in raw_creators:
        c8_owners = set(c8_cycle["owners"])
        for hex_index, hexagon in enumerate(hexes):
            if mixed_owners & hexagon["owners"] or c8_owners & hexagon["owners"]:
                continue
            pair_counts["owner_disjoint_tested"] += 1
            selected = set(mixed)
            selected.symmetric_difference_update(c8_support)
            selected.symmetric_difference_update(hexagon["incidences"])
            new_q3 = q3_deck(selected)
            if new_q3 is None:
                pair_counts["nonpath_factors"] += 1
                continue
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
                    "c8_owners": [base.bitword(value, 12) for value in c8_cycle["owners"]],
                    "c8_colours": [base.bitword(value, 12) for value in c8_cycle["colours"]],
                    "c6_index": hex_index,
                    "c6_core": base.bitword(hexagon["core"], 12),
                    "c6_active_one_based": [bit + 1 for bit in hexagon["active"]],
                    "c6_owners": sorted(base.bitword(value, 12) for value in hexagon["owners"]),
                    "c6_colours": sorted(base.bitword(value, 12) for value in hexagon["colours"]),
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
        "c8_c6_counts": pair_counts,
        "c8_c6_solutions": pair_solutions,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
