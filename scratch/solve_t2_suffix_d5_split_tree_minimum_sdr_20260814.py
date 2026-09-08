#!/usr/bin/env python3
"""Solve the exact minimum-class resource SDR on the D5 split suffix tree.

Substantive execution belongs on H100.  Inputs are the 41 exhaustive
per-edge candidate files.  The CNF chooses exactly one candidate per suffix
tree edge and uses every owner/q1 colour at most once.  If UNSAT, deletion
shrinking returns an inclusion-minimal edge core and split/role statistics.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import tempfile
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import search_t2_cross_suffix_alternating_cycles_20260813 as base  # noqa:E402
from pysat.card import CardEnc, EncType  # noqa:E402


def bits(word):
    return sum((character == "1") << index for index, character in enumerate(word))


def at_most_one(variables, clauses, next_variable):
    variables = sorted(set(variables))
    if len(variables) <= 1:
        return next_variable
    auxiliaries = list(range(next_variable, next_variable + len(variables) - 1))
    clauses.append([-variables[0], auxiliaries[0]])
    for index in range(1, len(variables) - 1):
        clauses.append([-variables[index], auxiliaries[index]])
        clauses.append([-auxiliaries[index - 1], auxiliaries[index]])
        clauses.append([-variables[index], -auxiliaries[index - 1]])
    clauses.append([-variables[-1], -auxiliaries[-1]])
    return next_variable + len(auxiliaries)


def at_most_k(variables, bound, clauses, next_variable):
    """Forward sequential counter: at most ``bound`` true literals."""
    variables = list(variables)
    if bound >= len(variables):
        return next_variable
    if bound == 0:
        clauses.extend([[-variable] for variable in variables])
        return next_variable
    # state[(i,j)] means at least j of the first i literals are true.
    state = {}
    for i in range(1, len(variables) + 1):
        for j in range(1, min(i, bound + 1) + 1):
            state[(i, j)] = next_variable
            next_variable += 1
            if j == 1:
                clauses.append([-variables[i - 1], state[(i, j)]])
            else:
                clauses.append([
                    -variables[i - 1],
                    -state[(i - 1, j - 1)],
                    state[(i, j)],
                ])
            if j <= i - 1:
                clauses.append([-state[(i - 1, j)], state[(i, j)]])
    clauses.append([-state[(len(variables), bound + 1)]])
    return next_variable


def build_instance(
    data,
    active_edges,
    maximum_extension_uses=None,
    maximum_extension_overhead=None,
    q2_loads=None,
):
    variable = 1
    variable_to_choice = {}
    edge_variables = defaultdict(list)
    resources = defaultdict(list)
    extension_candidate_variables = defaultdict(list)
    extension_overhead_variables = []
    q2_terms = defaultdict(list)
    q2_gain_constant = Counter()
    for edge_index in active_edges:
        for candidate_index, candidate in enumerate(data[edge_index]["candidates"]):
            variable_to_choice[variable] = (edge_index, candidate_index)
            edge_variables[edge_index].append(variable)
            if candidate.get("is_extension", False):
                extension_candidate_variables[edge_index].append(variable)
                overhead = (
                    candidate["incidence_length"]
                    - data[edge_index]["minimum_incidence_length"]
                ) // 2
                assert overhead >= 0
                extension_overhead_variables.extend([variable] * overhead)
            for owner in candidate["owners"]:
                resources[("owner", bits(owner))].append(variable)
            for colour in candidate["new_colours"]:
                resources[("colour", bits(colour))].append(variable)
            if q2_loads is not None:
                for target, delta in candidate["_q2_delta"].items():
                    if target not in q2_loads:
                        assert delta > 0
                        continue
                    if delta < 0:
                        q2_terms[target].extend([variable] * -delta)
                    elif delta > 0:
                        # -variable is true exactly when this possible gain
                        # is absent.  Adding every absent-gain literal to the
                        # left and the total possible gain to the right turns
                        # the signed support inequality into cardinality.
                        q2_terms[target].extend([-variable] * delta)
                        q2_gain_constant[target] += delta
            variable += 1

    clauses = []
    next_variable = variable
    for edge_index in active_edges:
        variables = edge_variables[edge_index]
        assert variables
        clauses.append(variables)
        next_variable = at_most_one(variables, clauses, next_variable)
    for variables in resources.values():
        next_variable = at_most_one(variables, clauses, next_variable)
    for target, literals in q2_terms.items():
        bound = q2_loads[target] - 1 + q2_gain_constant[target]
        if bound < len(literals):
            encoded = CardEnc.atmost(
                lits=literals,
                bound=bound,
                top_id=next_variable - 1,
                encoding=EncType.kmtotalizer,
            )
            clauses.extend(encoded.clauses)
            next_variable = max(next_variable, encoded.nv + 1)
    extension_indicators = {}
    for edge_index, variables in sorted(extension_candidate_variables.items()):
        indicator = next_variable
        next_variable += 1
        extension_indicators[edge_index] = indicator
        for variable in variables:
            clauses.append([-variable, indicator])
        clauses.append([-indicator] + variables)
    if maximum_extension_uses is not None:
        next_variable = at_most_k(
            extension_indicators.values(),
            maximum_extension_uses,
            clauses,
            next_variable,
        )
    if maximum_extension_overhead is not None:
        next_variable = at_most_k(
            extension_overhead_variables,
            maximum_extension_overhead,
            clauses,
            next_variable,
        )
    return (
        clauses,
        next_variable - 1,
        variable_to_choice,
        extension_indicators,
        len(q2_terms),
    )


def solve(
    data,
    active_edges,
    kissat,
    maximum_extension_uses=None,
    maximum_extension_overhead=None,
    q2_loads=None,
):
    (
        clauses,
        variables,
        variable_to_choice,
        extension_indicators,
        q2_targets,
    ) = build_instance(
        data,
        active_edges,
        maximum_extension_uses,
        maximum_extension_overhead,
        q2_loads,
    )
    with tempfile.TemporaryDirectory(prefix="t2_d5_sdr_") as directory:
        cnf = Path(directory) / "instance.cnf"
        with cnf.open("w", encoding="utf-8") as handle:
            handle.write(f"p cnf {variables} {len(clauses)}\n")
            for clause in clauses:
                handle.write(" ".join(map(str, clause)) + " 0\n")
        result = subprocess.run(
            [kissat, "--quiet", str(cnf)],
            check=False,
            capture_output=True,
            text=True,
        )
    if result.returncode == 20:
        return None, {
            "variables": variables,
            "clauses": len(clauses),
            "extension_edges": len(extension_indicators),
            "q2_targets": q2_targets,
        }
    assert result.returncode == 10, result.stdout + result.stderr
    model = {
        int(value)
        for line in result.stdout.splitlines() if line.startswith("v ")
        for value in line.split()[1:] if int(value) > 0
    }
    choices = [
        variable_to_choice[variable]
        for variable in sorted(model & set(variable_to_choice))
    ]
    assert len(choices) == len(active_edges)
    return choices, {
        "variables": variables,
        "clauses": len(clauses),
        "extension_edges": len(extension_indicators),
        "q2_targets": q2_targets,
    }


def annotate_q2_currents(data):
    m = 11
    selected = base.canonical_edges(m)
    base.apply_t2(selected, list(base.dyck_words(5)))
    by_owner, _ = base.factor_maps(selected)
    loads = Counter(
        colours[0] | colours[1]
        for colours in by_owner.values() if len(colours) == 2
    )
    for item in data.values():
        for candidate in item["candidates"]:
            owners = [bits(word) for word in candidate["owners"]]
            colours = [bits(word) for word in candidate["new_colours"]]
            assert len(owners) == len(colours)
            delta = Counter()
            for index, owner in enumerate(owners):
                old = colours[index - 1]
                new = colours[index]
                assert old in by_owner[owner] and new not in by_owner[owner]
                other = next(
                    colour for colour in by_owner[owner] if colour != old
                )
                delta[other | old] -= 1
                delta[other | new] += 1
            candidate["_q2_delta"] = dict(delta)
            assert all(
                loads[target] + change >= 1
                for target, change in delta.items()
                if change < 0
            )
    return loads


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("candidate_files", nargs="+")
    parser.add_argument("--kissat", default=os.environ.get("KISSAT", "kissat"))
    parser.add_argument("--core-extension", action="append", default=[])
    parser.add_argument("--minimize-extensions", action="store_true")
    parser.add_argument("--skip-core-shrink", action="store_true")
    parser.add_argument("--enforce-q2", action="store_true")
    args = parser.parse_args()
    parts = [
        json.loads(Path(path).read_text(encoding="utf-8"))
        for path in args.candidate_files
    ]
    data = {part["edge_index"]: part for part in parts}
    assert set(data) == set(range(41))
    for item in data.values():
        for candidate in item["candidates"]:
            candidate.setdefault(
                "incidence_length", item["minimum_incidence_length"]
            )
    for path in args.core_extension:
        extension = json.loads(Path(path).read_text(encoding="utf-8"))
        edge_index = extension["edge_index"]
        assert edge_index in data
        candidates = {
            (tuple(candidate["owners"]), tuple(candidate["new_colours"])): candidate
            for candidate in data[edge_index]["candidates"]
        }
        for prefix_row in extension["prefixes"]:
            length = prefix_row["shortest_q2_safe_incidence_length"]
            if length is None:
                continue
            for candidate in prefix_row["candidates"]:
                candidate = dict(
                    candidate,
                    incidence_length=length,
                    is_extension=True,
                )
                signature = (
                    tuple(candidate["owners"]),
                    tuple(candidate["new_colours"]),
                )
                # A resource-identical minimum candidate is never an
                # extension use.  Preserve it instead of letting a later
                # phase relabel it and artificially raise the optimum.
                candidates.setdefault(signature, candidate)
        data[edge_index]["candidates"] = list(candidates.values())
    q2_loads = annotate_q2_currents(data) if args.enforce_q2 else None
    active = list(range(41))
    minimum_extension_uses = None
    minimum_extension_overhead = None
    if args.minimize_extensions:
        for bound in range(42):
            choices, dimensions = solve(
                data,
                active,
                args.kissat,
                maximum_extension_uses=bound,
                q2_loads=q2_loads,
            )
            if choices is not None:
                minimum_extension_uses = bound
                break
        if choices is not None:
            maximum_overhead = sum(
                max(
                    [0] + [
                        (candidate["incidence_length"] - item[
                            "minimum_incidence_length"
                        ]) // 2
                        for candidate in item["candidates"]
                        if candidate.get("is_extension", False)
                    ]
                )
                for item in data.values()
            )
            for overhead_bound in range(maximum_overhead + 1):
                trial_choices, trial_dimensions = solve(
                    data,
                    active,
                    args.kissat,
                    maximum_extension_uses=minimum_extension_uses,
                    maximum_extension_overhead=overhead_bound,
                    q2_loads=q2_loads,
                )
                if trial_choices is not None:
                    choices = trial_choices
                    dimensions = trial_dimensions
                    minimum_extension_overhead = overhead_bound
                    break
    else:
        choices, dimensions = solve(
            data, active, args.kissat, q2_loads=q2_loads
        )

    core = None
    if choices is None:
        core = active[:]
        if not args.skip_core_shrink:
            position = 0
            while position < len(core):
                trial = core[:position] + core[position + 1:]
                trial_choices, _ = solve(
                    data, trial, args.kissat, q2_loads=q2_loads
                )
                if trial_choices is None:
                    core = trial
                else:
                    position += 1
            assert solve(
                data, core, args.kissat, q2_loads=q2_loads
            )[0] is None
            for position in range(len(core)):
                assert solve(
                    data,
                    core[:position] + core[position + 1:],
                    args.kissat,
                    q2_loads=q2_loads,
                )[0] is not None

    selection = None
    if choices is not None:
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
                "minimum_incidence_length": item["minimum_incidence_length"],
                "selected_incidence_length": candidate["incidence_length"],
                "candidate": candidate,
            })

    core_rows = []
    if core is not None:
        for edge_index in core:
            item = data[edge_index]
            core_rows.append({
                "edge_index": edge_index,
                "edge": item["edge"],
                "minimum_incidence_length": item["minimum_incidence_length"],
                "candidate_count": len(item["candidates"]),
                "candidate_prefix_histogram": dict(sorted(Counter(
                    candidate["prefix"] for candidate in item["candidates"]
                ).items())),
            })

    print(json.dumps({
        "status": "SAT" if choices is not None else "UNSAT",
        "edges": 41,
        "candidate_count_histogram": dict(sorted(Counter(
            len(item["candidates"]) for item in data.values()
        ).items())),
        "total_candidates": sum(
            len(item["candidates"]) for item in data.values()
        ),
        "cnf": dimensions,
        "minimum_extension_uses": minimum_extension_uses,
        "minimum_extension_overhead_owner_steps": minimum_extension_overhead,
        "aggregate_q2_support_encoded": args.enforce_q2,
        "selection": selection,
        "minimal_unsat_core": core_rows,
        "unsat_core_inclusion_minimal": (
            None if core is None else not args.skip_core_shrink
        ),
        "core_role_histogram": (
            None if core is None else dict(sorted(Counter(
                data[index]["edge"]["role"] for index in core
            ).items()))
        ),
        "core_split_histogram": (
            None if core is None else dict(sorted(Counter(
                str(data[index]["edge"]["split_pair"]) for index in core
            ).items()))
        ),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
