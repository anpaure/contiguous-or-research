#!/usr/bin/env python3
"""Parallel exact target-relevant C14/C16/C18/C20 q3 cycle atlas.

Substantive execution belongs on H100.  Each alternating cycle is assigned
to the lexicographically first target-relevant directed arc in its support,
so independently enumerated worker chunks remain duplicate-free.  C14 is
used as a regression against the frozen sequential count.
"""

from __future__ import annotations

import argparse
import json
import multiprocessing as mp
from collections import Counter

import audit_msw_t0v_tensor_residence_20260814 as base
import audit_msw_t0v_mixed_c8_c6_tensor_20260814 as tensor
import audit_msw_t0v_mixed_q3_loss_providers_20260814 as q3trace
import search_msw_t0_twohex_typed_safe_20260814 as search
import search_msw_t0_mixed_q3_long_cycle_backup_20260814 as serial


W3 = base.bits("110111001111")
_STATE = {}


def q3_deck(selected):
    try:
        paths = q3trace.paths(selected)
    except AssertionError:
        return None
    result = Counter()
    for _, colours in paths:
        for start in range(len(colours) - 2):
            result[colours[start] | colours[start + 1] | colours[start + 2]] += 1
    return result


def difference(old, new):
    result = Counter(new)
    result.subtract(old)
    return Counter({value: amount for value, amount in result.items() if amount})


def inspect(owners, colours, assigned_arc, counts, solutions, near_misses):
    state = _STATE
    arcs = {
        (owners[index], owners[(index + 1) % len(owners)], colours[index])
        for index in range(len(owners))
    }
    relevant = arcs & state["start_set"]
    assert relevant
    if assigned_arc != min(relevant):
        return

    support = serial.cycle_support(owners, colours)
    counts["distinct_cycles"] += 1
    if state["fixed_owners"] & set(owners):
        return
    counts["owner_disjoint_cycles"] += 1
    selected = set(state["mixed"])
    selected.symmetric_difference_update(support)
    q3 = q3_deck(selected)
    if q3 is None:
        counts["nonpath_factors"] += 1
        return
    if q3[W3] == 0:
        return
    counts["raw_creates_q3_target"] += 1
    new_typed = search.decks(selected)
    typed_currents = {
        name: difference(state["old_typed"][name], new_typed[name])
        for name in state["old_typed"]
    }
    if any(
        amount < 0 and new_typed[name][value] == 0
        for name, delta in typed_currents.items()
        for value, amount in delta.items()
    ) or new_typed["upper_q2"][search.TARGET] == 0:
        return
    counts["typed_q2_safe"] += 1
    q3_current = difference(state["old_q3"], q3)
    casualties = [
        value for value, amount in q3_current.items()
        if amount < 0 and q3[value] == 0
    ]
    row = {
        "owners": [base.bitword(value, 12) for value in owners],
        "colours": [base.bitword(value, 12) for value in colours],
        "q3_casualties": [base.bitword(value, 12) for value in casualties],
        "topology_residence": search.topology_and_residence(selected, state["canonical"]),
    }
    if casualties:
        if len(near_misses) < state["limit"]:
            near_misses.append(row)
        return
    counts["all_q3_support_safe"] += 1
    if len(solutions) < state["limit"]:
        solutions.append(row)


def worker(arcs):
    state = _STATE
    counts = Counter()
    solutions = []
    near_misses = []
    k = state["k"]
    for assigned_arc in arcs:
        start, second, first_colour = assigned_arc
        owners = [start, second]
        colours = [first_colour]

        def dfs():
            current = owners[-1]
            if len(colours) == k - 1:
                for next_owner, colour in state["outgoing"][current]:
                    if next_owner != start or colour in colours:
                        continue
                    inspect(
                        tuple(owners), tuple(colours + [colour]), assigned_arc,
                        counts, solutions, near_misses,
                    )
                return
            for next_owner, colour in state["outgoing"][current]:
                if next_owner == start or next_owner in owners or colour in colours:
                    continue
                owners.append(next_owner)
                colours.append(colour)
                dfs()
                colours.pop()
                owners.pop()

        dfs()
    return counts, solutions, near_misses


def chunks(values, workers):
    result = [[] for _ in range(workers)]
    for index, value in enumerate(values):
        result[index % workers].append(value)
    return [row for row in result if row]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("cycle_owners", type=int, choices=(7, 8, 9, 10))
    parser.add_argument("--workers", type=int, default=32)
    parser.add_argument("--limit", type=int, default=5)
    args = parser.parse_args()

    canonical = base.canonical_edges(6)
    old_typed = search.decks(canonical)
    old_q3 = q3_deck(canonical)
    fixed_c8, fixed_c6 = tensor.prefix_packet()
    fixed_support = fixed_c8 | fixed_c6
    fixed_owners = {owner for owner, _ in fixed_support}
    mixed = set(canonical)
    mixed.symmetric_difference_update(fixed_support)
    by_colour, outgoing = serial.owner_arc_graph(canonical)
    starts = sorted(serial.target_arcs(by_colour))

    global _STATE
    _STATE = {
        "canonical": canonical,
        "old_typed": old_typed,
        "old_q3": old_q3,
        "fixed_owners": fixed_owners,
        "mixed": mixed,
        "outgoing": outgoing,
        "start_set": set(starts),
        "k": args.cycle_owners,
        "limit": args.limit,
    }

    context = mp.get_context("fork")
    work = chunks(starts, args.workers)
    with context.Pool(processes=len(work)) as pool:
        rows = pool.map(worker, work)
    counts = Counter({"target_relevant_start_arcs": len(starts)})
    solutions = []
    near_misses = []
    for partial, found, near in rows:
        counts.update(partial)
        solutions.extend(found)
        near_misses.extend(near)
    print(json.dumps({
        "status": "PASS",
        "cycle_length": 2 * args.cycle_owners,
        "counts": dict(sorted(counts.items())),
        "solutions": solutions[:args.limit],
        "near_misses": near_misses[:args.limit],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
