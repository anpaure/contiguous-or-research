#!/usr/bin/env python3
"""Search one target-relevant native C10/C12 backing the mixed q3 loss.

Substantive execution belongs on H100.  A cycle is generated only if it
contains a directed endpoint replacement that can occur on a four-owner
Johnson path whose union is W3.  Complete typed decks through q3 are then
replayed after the cycle and the fixed mixed T0 packet.
"""

from __future__ import annotations

import argparse
import itertools
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


def owner_arc_graph(canonical):
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
    return by_colour, outgoing


def target_arcs(by_colour):
    owners = [
        value for value in range(1 << 12)
        if value.bit_count() == 6 and value & ~W3 == 0
    ]
    arcs = set()
    for left, right in itertools.combinations(owners, 2):
        if (left ^ right).bit_count() != 2:
            continue
        colour = left | right
        old = set(by_colour[colour])
        desired = {left, right}
        if desired == old or len(desired & old) != 1:
            continue
        new_owner = next(iter(desired - old))
        removed_owner = next(iter(old - desired))
        arcs.add((new_owner, removed_owner, colour))
    return arcs


def cycle_support(owners, colours):
    incidences = set()
    for index, colour in enumerate(colours):
        incidences.add((owners[index], colour))
        incidences.add((owners[(index + 1) % len(owners)], colour))
    return frozenset(incidences)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("cycle_owners", type=int, choices=(5, 6, 7, 8, 9, 10))
    parser.add_argument("--limit", type=int, default=20)
    args = parser.parse_args()
    k = args.cycle_owners

    canonical = base.canonical_edges(6)
    old_typed = search.decks(canonical)
    old_q3 = q3_deck(canonical)
    fixed_c8, fixed_c6 = tensor.prefix_packet()
    fixed_support = fixed_c8 | fixed_c6
    fixed_owners = {owner for owner, _ in fixed_support}
    mixed = set(canonical)
    mixed.symmetric_difference_update(fixed_support)
    by_colour, outgoing = owner_arc_graph(canonical)
    starts = target_arcs(by_colour)

    seen = set()
    counts = {
        "target_relevant_start_arcs": len(starts),
        "distinct_cycles": 0,
        "owner_disjoint_cycles": 0,
        "nonpath_factors": 0,
        "raw_creates_q3_target": 0,
        "typed_q2_safe": 0,
        "all_q3_support_safe": 0,
    }
    solutions = []
    near_misses = []

    def inspect(owners, colours):
        support = cycle_support(owners, colours)
        if support in seen:
            return
        seen.add(support)
        counts["distinct_cycles"] += 1
        if fixed_owners & set(owners):
            return
        counts["owner_disjoint_cycles"] += 1
        selected = set(mixed)
        selected.symmetric_difference_update(support)
        q3 = q3_deck(selected)
        if q3 is None:
            counts["nonpath_factors"] += 1
            return
        if q3[W3] == 0:
            return
        counts["raw_creates_q3_target"] += 1
        new_typed = search.decks(selected)
        typed_currents = {}
        for name in old_typed:
            typed_currents[name] = difference(old_typed[name], new_typed[name])
        if any(
            amount < 0 and new_typed[name][value] == 0
            for name, delta in typed_currents.items()
            for value, amount in delta.items()
        ) or new_typed["upper_q2"][search.TARGET] == 0:
            return
        counts["typed_q2_safe"] += 1
        q3_current = difference(old_q3, q3)
        q3_casualties = [
            value for value, amount in q3_current.items()
            if amount < 0 and q3[value] == 0
        ]
        if q3_casualties:
            if len(near_misses) < args.limit:
                near_misses.append({
                    "owners": [base.bitword(value, 12) for value in owners],
                    "colours": [base.bitword(value, 12) for value in colours],
                    "q3_target_load": q3[W3],
                    "q3_casualties": [base.bitword(value, 12) for value in q3_casualties],
                    "typed_currents": {
                        name: rows(delta, old_typed[name], new_typed[name])
                        for name, delta in typed_currents.items()
                    },
                    "q3_current": rows(q3_current, old_q3, q3),
                    "topology_residence": search.topology_and_residence(selected, canonical),
                })
            return
        counts["all_q3_support_safe"] += 1
        if len(solutions) < args.limit:
            solutions.append({
                "owners": [base.bitword(value, 12) for value in owners],
                "colours": [base.bitword(value, 12) for value in colours],
                "typed_currents": {
                    name: rows(delta, old_typed[name], new_typed[name])
                    for name, delta in typed_currents.items()
                },
                "q3_current": rows(q3_current, old_q3, q3),
                "topology_residence": search.topology_and_residence(selected, canonical),
            })

    for start, second, first_colour in sorted(starts):
        if start in fixed_owners or second in fixed_owners:
            continue
        owners = [start, second]
        colours = [first_colour]

        def dfs():
            current = owners[-1]
            if len(colours) == k - 1:
                for next_owner, colour in outgoing[current]:
                    if next_owner != start or colour in colours:
                        continue
                    inspect(tuple(owners), tuple(colours + [colour]))
                return
            for next_owner, colour in outgoing[current]:
                if next_owner == start or next_owner in owners or colour in colours:
                    continue
                owners.append(next_owner)
                colours.append(colour)
                dfs()
                colours.pop()
                owners.pop()

        dfs()

    print(json.dumps({
        "status": "PASS",
        "cycle_length": 2 * k,
        "counts": counts,
        "solutions": solutions,
        "near_misses": near_misses,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
