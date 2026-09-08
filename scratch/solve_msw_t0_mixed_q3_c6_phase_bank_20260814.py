#!/usr/bin/env python3
"""Solve the minimum added C6 phase bank around the mixed T0 packet.

Substantive execution belongs on H100.  The fixed mixed C8+C6 is installed
first.  An arbitrary owner-disjoint subset of initially alternating native
C6s is selected, shared q1 colours are modeled by literal final endpoints,
and all old typed support through q2 plus T0 is imposed.  At least one of
the seven individually q3-creating C6s is required.  Each optimum candidate
is then replayed on the complete q3 deck; failed candidates are excluded.
"""

from __future__ import annotations

import argparse
import itertools
import json
from collections import Counter, defaultdict

from ortools.sat.python import cp_model

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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--time-limit", type=float, default=600.0)
    parser.add_argument("--workers", type=int, default=32)
    parser.add_argument("--max-candidates", type=int, default=200)
    args = parser.parse_args()

    canonical = base.canonical_edges(6)
    old_decks = search.decks(canonical)
    old_q3 = q3_deck(canonical)
    fixed_c8, fixed_c6 = tensor.prefix_packet()
    fixed_support = fixed_c8 | fixed_c6
    fixed_owners = {owner for owner, _ in fixed_support}
    mixed = set(canonical)
    mixed.symmetric_difference_update(fixed_support)
    mixed_decks = search.decks(mixed)
    assert q3_deck(mixed)[W3] == 0

    hexes = search.enumerate_hexes(canonical)
    allowed = [
        not bool(fixed_owners & hexagon["owners"])
        for hexagon in hexes
    ]
    raw_creators = []
    for index, hexagon in enumerate(hexes):
        if not allowed[index]:
            continue
        selected = set(mixed)
        selected.symmetric_difference_update(hexagon["incidences"])
        deck = q3_deck(selected)
        if deck is not None and deck[W3] > 0:
            raw_creators.append(index)
    assert len(raw_creators) == 7

    per_hex = []
    owner_to_hexes = defaultdict(list)
    incidence_to_hexes = defaultdict(list)
    for index, hexagon in enumerate(hexes):
        if allowed[index]:
            for owner in hexagon["owners"]:
                owner_to_hexes[owner].append(index)
            for incidence in hexagon["incidences"]:
                incidence_to_hexes[incidence].append(index)
        after = search.decks(search.apply(canonical, hexagon))
        per_hex.append({
            "upper_q2": difference(old_decks["upper_q2"], after["upper_q2"]),
            "lower_q2": difference(old_decks["lower_q2"], after["lower_q2"]),
        })

    model = cp_model.CpModel()
    x = [model.new_bool_var(f"h{index}") for index in range(len(hexes))]
    for index, is_allowed in enumerate(allowed):
        if not is_allowed:
            model.add(x[index] == 0)
    for indices in owner_to_hexes.values():
        model.add(sum(x[index] for index in indices) <= 1)
    model.add(sum(x[index] for index in raw_creators) >= 1)

    all_colours = [
        value for value in range(1 << 12) if value.bit_count() == 7
    ]
    final_incidence = {}
    for colour in all_colours:
        for removed in range(12):
            if not (colour >> removed & 1):
                continue
            owner = colour & ~(1 << removed)
            incidence = (owner, colour)
            variable = model.new_bool_var(f"s_{owner}_{colour}")
            togglers = incidence_to_hexes.get(incidence, [])
            toggle_sum = sum(x[index] for index in togglers)
            model.add(toggle_sum <= 1)
            if incidence in mixed:
                model.add(variable == 1 - toggle_sum)
            else:
                model.add(variable == toggle_sum)
            final_incidence[incidence] = variable

    lower_providers = defaultdict(list)
    for colour in all_colours:
        owners = [
            colour & ~(1 << removed)
            for removed in range(12) if colour >> removed & 1
        ]
        endpoints = [final_incidence[(owner, colour)] for owner in owners]
        model.add(sum(endpoints) == 2)
        for first, second in itertools.combinations(range(len(owners)), 2):
            pair = model.new_bool_var(f"p_{colour}_{first}_{second}")
            model.add(pair <= endpoints[first])
            model.add(pair <= endpoints[second])
            model.add(pair >= endpoints[first] + endpoints[second] - 1)
            lower_providers[owners[first] & owners[second]].append(pair)
    for value in old_decks["lower_q1"]:
        model.add(sum(lower_providers[value]) >= 1)

    for deck_name in ("upper_q2", "lower_q2"):
        coefficients = defaultdict(list)
        for index, currents in enumerate(per_hex):
            for value, amount in currents[deck_name].items():
                coefficients[value].append((index, amount))
        for value in set(old_decks[deck_name]) | set(mixed_decks[deck_name]) | set(coefficients):
            expression = sum(
                amount * x[index] for index, amount in coefficients[value]
            )
            required = 1 if old_decks[deck_name][value] else 0
            model.add(mixed_decks[deck_name][value] + expression >= required)
    target_expression = sum(
        per_hex[index]["upper_q2"][search.TARGET] * x[index]
        for index in range(len(hexes))
    )
    model.add(mixed_decks["upper_q2"][search.TARGET] + target_expression >= 1)
    objective = sum(x)
    model.minimize(objective)

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = args.time_limit
    solver.parameters.num_search_workers = args.workers
    candidates = []
    solution = None
    final_status = None
    for attempt in range(args.max_candidates):
        status = solver.solve(model)
        final_status = solver.status_name(status)
        if status not in (cp_model.OPTIMAL, cp_model.FEASIBLE):
            break
        chosen = [index for index, variable in enumerate(x) if solver.value(variable)]
        selected = set(mixed)
        for index in chosen:
            selected.symmetric_difference_update(hexes[index]["incidences"])
        new_decks = search.decks(selected)
        q3 = q3_deck(selected)
        q3_current = None if q3 is None else difference(old_q3, q3)
        q3_casualties = None if q3 is None else [
            value for value, amount in q3_current.items()
            if amount < 0 and q3[value] == 0
        ]
        row = {
            "chosen": chosen,
            "count": len(chosen),
            "q3_path_factor": q3 is not None,
            "q3_target_load": None if q3 is None else q3[W3],
            "q3_casualties": None if q3_casualties is None else len(q3_casualties),
        }
        candidates.append(row)
        if q3 is not None and q3[W3] > 0 and not q3_casualties:
            typed_currents = {
                name: difference(old_decks[name], new_decks[name])
                for name in old_decks
            }
            solution = {
                "indices": chosen,
                "circuits": [
                    {
                        "index": index,
                        "core": base.bitword(hexes[index]["core"], 12),
                        "active_one_based": [bit + 1 for bit in hexes[index]["active"]],
                        "owners": sorted(base.bitword(value, 12) for value in hexes[index]["owners"]),
                        "colours": sorted(base.bitword(value, 12) for value in hexes[index]["colours"]),
                    }
                    for index in chosen
                ],
                "typed_currents": {
                    name: rows(delta, old_decks[name], new_decks[name])
                    for name, delta in typed_currents.items()
                },
                "q3_current": rows(q3_current, old_q3, q3),
                "topology_residence": search.topology_and_residence(selected, canonical),
            }
            break
        chosen_set = set(chosen)
        model.add(
            sum(x[index] for index in chosen)
            - sum(x[index] for index in range(len(hexes)) if index not in chosen_set)
            <= len(chosen) - 1
        )

    print(json.dumps({
        "status": "PASS",
        "solver_status": final_status,
        "raw_creator_indices": raw_creators,
        "candidates_tested": len(candidates),
        "candidates": candidates,
        "solution": solution,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
