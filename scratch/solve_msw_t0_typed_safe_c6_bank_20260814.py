#!/usr/bin/env python3
"""Solve the full resource-disjoint typed-safe native C6 bank for T0.

Substantive execution belongs on H100.  Every variable is one initially
alternating canonical semilength-six incidence C6.  Owner and q1-colour
packing make all selected switches simultaneous and make both the upper-q2
and lower-q1 currents additive.  CP-SAT minimizes the number of circuits
subject to creating T0 and retaining every old upper-q2 and lower-q1 value.
The returned bank is independently replayed as a literal incidence toggle.
"""

from __future__ import annotations

import argparse
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
    parser.add_argument("--time-limit", type=float, default=300.0)
    parser.add_argument("--workers", type=int, default=32)
    parser.add_argument("--core", action="store_true")
    args = parser.parse_args()

    canonical = base.canonical_edges(search.M)
    old_decks = search.decks(canonical)
    hexes = search.enumerate_hexes(canonical)
    per_hex = []
    owner_to_hexes = defaultdict(list)
    colour_to_hexes = defaultdict(list)
    for index, hexagon in enumerate(hexes):
        after_decks = search.decks(search.apply(canonical, hexagon))
        currents = {
            name: delta(old_decks[name], after_decks[name])
            for name in ("upper_q2", "lower_q1", "lower_q2")
        }
        per_hex.append(currents)
        for owner in hexagon["owners"]:
            owner_to_hexes[owner].append(index)
        for colour in hexagon["colours"]:
            colour_to_hexes[colour].append(index)

    model = cp_model.CpModel()
    variables = [model.new_bool_var(f"h{index}") for index in range(len(hexes))]
    for indices in owner_to_hexes.values():
        model.add(sum(variables[index] for index in indices) <= 1)
    for indices in colour_to_hexes.values():
        model.add(sum(variables[index] for index in indices) <= 1)

    assumption_names = {}
    for deck_name in ("upper_q2", "lower_q1", "lower_q2"):
        coefficients = defaultdict(list)
        for index, currents in enumerate(per_hex):
            for value, amount in currents[deck_name].items():
                coefficients[value].append((index, amount))
        values = set(old_decks[deck_name]) | set(coefficients)
        for value in values:
            expression = sum(
                amount * variables[index]
                for index, amount in coefficients[value]
            )
            required = 1 if old_decks[deck_name][value] else 0
            constraint = model.add(
                old_decks[deck_name][value] + expression >= required
            )
            if args.core:
                literal = model.new_bool_var(
                    f"keep_{deck_name}_{base.bitword(value, search.N)}"
                )
                constraint.only_enforce_if(literal)
                model.add_assumption(literal)
                assumption_names[literal.Index()] = (
                    f"{deck_name}:{base.bitword(value, search.N)}"
                )

    target_expression = sum(
        currents["upper_q2"][search.TARGET] * variables[index]
        for index, currents in enumerate(per_hex)
    )
    target_constraint = model.add(target_expression >= 1)
    if args.core:
        target_literal = model.new_bool_var("create_T0")
        target_constraint.only_enforce_if(target_literal)
        model.add_assumption(target_literal)
        assumption_names[target_literal.Index()] = "create_T0"
    else:
        model.minimize(sum(variables))

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = args.time_limit
    solver.parameters.num_search_workers = args.workers
    if args.core:
        solver.parameters.core_minimization_level = 2
    status = solver.solve(model)
    status_name = solver.status_name(status)
    chosen = [
        index for index, variable in enumerate(variables)
        if status in (cp_model.OPTIMAL, cp_model.FEASIBLE) and solver.value(variable)
    ]

    report = {
        "status": status_name,
        "alternating_hexes": len(hexes),
        "chosen_count": len(chosen),
        "objective_bound": solver.best_objective_bound,
        "wall_time_seconds": solver.wall_time,
        "chosen": [],
    }
    if args.core and status == cp_model.INFEASIBLE:
        report["sufficient_assumption_core"] = [
            assumption_names.get(literal, f"literal:{literal}")
            for literal in solver.sufficient_assumptions_for_infeasibility()
        ]
    if chosen:
        chosen_hexes = [hexes[index] for index in chosen]
        selected = search.apply(canonical, *chosen_hexes)
        new_decks = search.decks(selected)
        exact_currents = {}
        casualties = {}
        for name in old_decks:
            exact_currents[name], casualties[name] = search.current(
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
            name: encoded(current) for name, current in exact_currents.items()
        }
        report["topology_residence"] = search.topology_and_residence(
            selected, canonical
        )
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
