#!/usr/bin/env python3
"""Exact typed-safe T0 C6-bank model allowing within-bank q1 relays.

Substantive execution belongs on H100.  Owner-disjoint initially
alternating C6s are selected simultaneously.  Shared q1 colours are
allowed; their final two endpoints are modeled literally, so lower-q1
support is not approximated by additive single-circuit currents.
"""

from __future__ import annotations

import argparse
import itertools
import json
from collections import Counter, defaultdict

from ortools.sat.python import cp_model

import audit_msw_t0v_tensor_residence_20260814 as base
import search_msw_t0_twohex_typed_safe_20260814 as search


def delta(old, new):
    answer = Counter(new)
    answer.subtract(old)
    return Counter({value: amount for value, amount in answer.items() if amount})


def encoded(delta_counter):
    return [
        {"value": base.bitword(value, search.N), "delta": amount}
        for value, amount in sorted(delta_counter.items())
    ]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--time-limit", type=float, default=600.0)
    parser.add_argument("--workers", type=int, default=32)
    args = parser.parse_args()

    canonical = base.canonical_edges(search.M)
    old_decks = search.decks(canonical)
    by_owner, by_colour = search.deck_maps(canonical)
    hexes = search.enumerate_hexes(canonical)

    model = cp_model.CpModel()
    x = [model.new_bool_var(f"h{index}") for index in range(len(hexes))]
    owner_to_hexes = defaultdict(list)
    incidence_to_hexes = defaultdict(list)
    per_hex_upper = []
    per_hex_lower_q2 = []
    for index, hexagon in enumerate(hexes):
        for owner in hexagon["owners"]:
            owner_to_hexes[owner].append(index)
        for incidence in hexagon["incidences"]:
            incidence_to_hexes[incidence].append(index)
        after_decks = search.decks(search.apply(canonical, hexagon))
        per_hex_upper.append(delta(old_decks["upper_q2"], after_decks["upper_q2"]))
        per_hex_lower_q2.append(delta(old_decks["lower_q2"], after_decks["lower_q2"]))
    for indices in owner_to_hexes.values():
        model.add(sum(x[index] for index in indices) <= 1)

    # Every possible incidence of a rank-(m+1) colour with a rank-m owner.
    final_incidence = {}
    all_colours = [
        value for value in range(1 << search.N)
        if value.bit_count() == search.M + 1
    ]
    for colour in all_colours:
        bits = [bit for bit in range(search.N) if colour >> bit & 1]
        for removed in bits:
            owner = colour & ~(1 << removed)
            incidence = (owner, colour)
            variable = model.new_bool_var(f"s_{owner}_{colour}")
            togglers = incidence_to_hexes.get(incidence, [])
            toggle_sum = sum(x[index] for index in togglers)
            model.add(toggle_sum <= 1)
            if incidence in canonical:
                model.add(variable == 1 - toggle_sum)
            else:
                model.add(variable == toggle_sum)
            final_incidence[incidence] = variable

    lower_providers = defaultdict(list)
    for colour in all_colours:
        owners = [
            colour & ~(1 << removed)
            for removed in range(search.N) if colour >> removed & 1
        ]
        endpoint_variables = [final_incidence[(owner, colour)] for owner in owners]
        model.add(sum(endpoint_variables) == 2)
        for first, second in itertools.combinations(range(len(owners)), 2):
            pair = model.new_bool_var(f"p_{colour}_{first}_{second}")
            left = endpoint_variables[first]
            right = endpoint_variables[second]
            model.add(pair <= left)
            model.add(pair <= right)
            model.add(pair >= left + right - 1)
            lower_providers[owners[first] & owners[second]].append(pair)
    for value in old_decks["lower_q1"]:
        model.add(sum(lower_providers[value]) >= 1)

    for deck_name, currents in (
        ("upper_q2", per_hex_upper),
        ("lower_q2", per_hex_lower_q2),
    ):
        coefficients = defaultdict(list)
        for index, current in enumerate(currents):
            for value, amount in current.items():
                coefficients[value].append((index, amount))
        for value in set(old_decks[deck_name]) | set(coefficients):
            expression = sum(
                amount * x[index] for index, amount in coefficients[value]
            )
            required = 1 if old_decks[deck_name][value] else 0
            model.add(old_decks[deck_name][value] + expression >= required)

    model.add(sum(
        current[search.TARGET] * x[index]
        for index, current in enumerate(per_hex_upper)
    ) >= 1)
    model.minimize(sum(x))

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = args.time_limit
    solver.parameters.num_search_workers = args.workers
    status = solver.solve(model)
    chosen = [
        index for index, variable in enumerate(x)
        if status in (cp_model.OPTIMAL, cp_model.FEASIBLE) and solver.value(variable)
    ]
    report = {
        "status": solver.status_name(status),
        "alternating_hexes": len(hexes),
        "chosen_count": len(chosen),
        "objective_bound": solver.best_objective_bound,
        "wall_time_seconds": solver.wall_time,
        "chosen": [],
    }
    if chosen:
        selected = search.apply(canonical, *(hexes[index] for index in chosen))
        new_decks = search.decks(selected)
        currents = {}
        casualties = {}
        for name in old_decks:
            currents[name], casualties[name] = search.current(
                old_decks[name], new_decks[name]
            )
        assert new_decks["upper_q2"][search.TARGET] >= 1
        assert not any(casualties.values())
        report["chosen"] = [
            {
                "index": index,
                "core": base.bitword(hexes[index]["core"], search.N),
                "active_one_based": [bit + 1 for bit in hexes[index]["active"]],
                "owners": sorted(base.bitword(value, search.N) for value in hexes[index]["owners"]),
                "colours": sorted(base.bitword(value, search.N) for value in hexes[index]["colours"]),
            }
            for index in chosen
        ]
        report["currents"] = {
            name: encoded(current) for name, current in currents.items()
        }
        report["topology_residence"] = search.topology_and_residence(
            selected, canonical
        )
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
