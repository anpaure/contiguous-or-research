#!/usr/bin/env python3
"""Select an aggregate-q2-safe one-output D5 suffix actuator bank.

Substantive execution belongs on H100.  The base CNF enforces one candidate
per frozen suffix-tree edge, pairwise owner/q1-colour disjointness, and exact
aggregate q2 support.  After each model, the complete lifted middle-level
factor is traversed.  If its touched set has several output components, each
proper output shore gives a necessary connectivity cut: either a currently
removed old incidence crossing that shore must be restored, or some candidate
adding a crossing incidence must be selected.  These exact cuts are added to
an incremental CaDiCaL instance until a one-output model is found or the menu
is proved topologically UNSAT.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

import pysat
from pysat.solvers import Solver

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import search_t2_cross_suffix_alternating_cycles_20260813 as base  # noqa:E402
from audit_t2_cross_suffix_c16_full_ml_topology_20260813 import (  # noqa:E402
    graph_components,
    lifted_edges,
)
from solve_t2_suffix_d5_split_tree_minimum_sdr_20260814 import (  # noqa:E402
    annotate_q2_currents,
    bits,
    build_instance,
)
from verify_t2_c16_suffix_component_residence_20260813 import (  # noqa:E402
    toggle,
)


def load_data(candidate_files, extensions):
    parts = [
        json.loads(Path(path).read_text(encoding="utf-8"))
        for path in candidate_files
    ]
    data = {part["edge_index"]: part for part in parts}
    assert set(data) == set(range(41))
    for item in data.values():
        for candidate in item["candidates"]:
            candidate.setdefault(
                "incidence_length", item["minimum_incidence_length"]
            )
    for path in extensions:
        extension = json.loads(Path(path).read_text(encoding="utf-8"))
        edge_index = extension["edge_index"]
        candidates = {
            (tuple(candidate["owners"]), tuple(candidate["new_colours"])):
            candidate
            for candidate in data[edge_index]["candidates"]
        }
        for prefix_row in extension["prefixes"]:
            length = prefix_row["shortest_q2_safe_incidence_length"]
            if length is None:
                continue
            for row in prefix_row["candidates"]:
                candidate = dict(
                    row,
                    incidence_length=length,
                    is_extension=True,
                )
                signature = (
                    tuple(candidate["owners"]),
                    tuple(candidate["new_colours"]),
                )
                candidates.setdefault(signature, candidate)
        data[edge_index]["candidates"] = list(candidates.values())
    return data


def candidate_cycle(candidate):
    owners = tuple(bits(word) for word in candidate["owners"])
    colours = tuple(bits(word) for word in candidate["new_colours"])
    return [
        (owners[index], colours[index - 1], colours[index])
        for index in range(len(owners))
    ]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("candidate_files", nargs="+")
    parser.add_argument("--core-extension", action="append", default=[])
    parser.add_argument("--maximum-models", type=int, default=1000)
    args = parser.parse_args()

    data = load_data(args.candidate_files, args.core_extension)
    q2_loads = annotate_q2_currents(data)
    (
        clauses,
        variables,
        variable_to_choice,
        _,
        q2_targets,
    ) = build_instance(data, list(range(41)), q2_loads=q2_loads)
    choice_to_variable = {
        choice: variable for variable, choice in variable_to_choice.items()
    }

    m, n = 11, 22
    suffixes = list(base.dyck_words(5))
    canonical = base.canonical_edges(m)
    post = set(canonical)
    base.apply_t2(post, suffixes)
    by_owner, _ = base.factor_maps(post)
    before_components, before_which = graph_components(
        lifted_edges(post, canonical, n)
    )

    # Decode every possible changed lower incidence once.  The lists also
    # let the cut separator scan the finite candidate menu directly.
    removed_and_added = {}
    for variable, (edge_index, candidate_index) in variable_to_choice.items():
        cycle = candidate_cycle(data[edge_index]["candidates"][candidate_index])
        removed_and_added[variable] = (
            tuple((owner, old) for owner, old, _ in cycle),
            tuple((owner, new) for owner, _, new in cycle),
        )

    dimensions = {
        "variables": variables,
        "clauses_before_topology_cuts": len(clauses),
        "q2_targets": q2_targets,
    }
    rejected = []
    selection = None
    final_summary = None
    with Solver(name="cadical195", bootstrap_with=clauses) as sat:
        del clauses
        for model_index in range(args.maximum_models):
            if not sat.solve():
                final_summary = {
                    "status": "TOPOLOGY_UNSAT",
                    "reason": "exact connectivity cuts exhaust the menu",
                }
                break
            model = {literal for literal in sat.get_model() if literal > 0}
            chosen_variables = sorted(model & set(variable_to_choice))
            assert len(chosen_variables) == 41
            choices = [variable_to_choice[variable] for variable in chosen_variables]
            cycles = [
                candidate_cycle(data[edge]["candidates"][candidate])
                for edge, candidate in choices
            ]

            # Independent aggregate-q2 replay despite its presence in CNF.
            q2_delta = Counter()
            for cycle in cycles:
                for owner, old, new in cycle:
                    other = next(colour for colour in by_owner[owner] if colour != old)
                    q2_delta[other | old] -= 1
                    q2_delta[other | new] += 1
            q2_losses = [
                target for target in q2_loads
                if q2_loads[target] + q2_delta[target] <= 0
            ]
            assert not q2_losses

            simultaneous = toggle(post, cycles)
            after_components, after_which = graph_components(
                lifted_edges(simultaneous, canonical, n)
            )
            touched_before = {
                before_which[owner]
                for cycle in cycles for owner, _, _ in cycle
            }
            touched_after = {
                after_which[owner]
                for cycle in cycles for owner, _, _ in cycle
            }
            suffix_outputs = {
                after_which[
                    bits(item["candidates"][candidate_index]["prefix"])
                    | (bits(word) << 12)
                ]
                for edge_index, candidate_index in choices
                for item in [data[edge_index]]
                for word in item["edge"]["suffix_edge"]
            }
            component_reduction = len(before_components) - len(after_components)
            spanning = (
                len(touched_after) == 1
                and len(suffix_outputs) == 1
                and component_reduction == len(touched_before) - 1
            )
            print(
                f"c model={model_index} touched_before={len(touched_before)} "
                f"outputs={len(touched_after)} suffix_outputs={len(suffix_outputs)} "
                f"reduction={component_reduction}",
                file=sys.stderr,
                flush=True,
            )
            if spanning:
                selection = []
                for edge_index, candidate_index in sorted(choices):
                    item = data[edge_index]
                    candidate = {
                        key: value
                        for key, value in item["candidates"][candidate_index].items()
                        if not key.startswith("_")
                    }
                    selection.append({
                        "edge_index": edge_index,
                        "candidate_index": candidate_index,
                        "edge": item["edge"],
                        "minimum_incidence_length": item[
                            "minimum_incidence_length"
                        ],
                        "selected_incidence_length": candidate[
                            "incidence_length"
                        ],
                        "candidate": candidate,
                    })
                output = next(iter(touched_after))
                final_summary = {
                    "status": "SAT",
                    "q2_support_losses": 0,
                    "minimum_q2_load_after": min(
                        q2_loads[target] + q2_delta[target]
                        for target in q2_loads
                    ),
                    "base_components_met": len(touched_before),
                    "output_components_on_touched_owners": 1,
                    "suffix_representative_output_components": 1,
                    "component_reduction": component_reduction,
                    "output_component_owner_length": (
                        len(after_components[output]) // 2
                    ),
                }
                break

            cut_sizes = []
            cut_keys = set()
            for component in sorted(touched_after):
                current_removers = {
                    variable
                    for variable in chosen_variables
                    if any(
                        (after_which[owner] == component)
                        != (after_which[colour] == component)
                        for owner, colour in removed_and_added[variable][0]
                    )
                }
                possible_adders = {
                    variable
                    for variable in variable_to_choice
                    if any(
                        (after_which[owner] == component)
                        != (after_which[colour] == component)
                        for owner, colour in removed_and_added[variable][1]
                    )
                }
                cut = tuple(sorted(
                    {-variable for variable in current_removers}
                    | possible_adders,
                    key=lambda literal: (abs(literal), literal),
                ))
                # Every literal is false in the rejected model.  Thus this
                # clause rejects it and is a genuine necessary cut, not a
                # heuristic block.
                assert cut
                assert all(
                    (literal > 0 and literal not in model)
                    or (literal < 0 and -literal in model)
                    for literal in cut
                )
                if cut not in cut_keys:
                    sat.add_clause(list(cut))
                    cut_keys.add(cut)
                    cut_sizes.append(len(cut))
            rejected.append({
                "model_index": model_index,
                "base_components_met": len(touched_before),
                "output_components": len(touched_after),
                "suffix_output_components": len(suffix_outputs),
                "component_reduction": component_reduction,
                "connectivity_cuts_added": len(cut_sizes),
                "cut_size_minimum": min(cut_sizes),
                "cut_size_maximum": max(cut_sizes),
            })
        else:
            final_summary = {
                "status": "MODEL_LIMIT",
                "reason": f"reached {args.maximum_models} models",
            }

    assert final_summary is not None
    print(json.dumps({
        "status": final_summary["status"],
        "edges": 41,
        "total_candidates": sum(
            len(item["candidates"]) for item in data.values()
        ),
        "aggregate_q2_support_encoded": True,
        "topology_connectivity_cegar": True,
        "incremental_solver": "cadical195",
        "python_sat_version": pysat.__version__,
        "cnf": dimensions,
        "rejected_model_count": len(rejected),
        "rejected_models": rejected,
        "selection": selection,
        "simultaneous": final_summary,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
