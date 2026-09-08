#!/usr/bin/env python3
"""Extract small owner-equation cores for the D5 successor-tag no-go.

Substantive execution belongs on H100.  Every owner equation is guarded by
an assumption literal.  CaDiCaL first extracts an assumption core; greedy
deletion then makes it inclusion-minimal.  The tag has 14 bits, enough to
name all 12,420 owners privately, so UNSAT is exactly a quotient-loop
obstruction rather than an alphabet bound.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import defaultdict
from pathlib import Path

from pysat.solvers import Solver

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import search_t2_cross_suffix_alternating_cycles_20260813 as base  # noqa:E402
from audit_t2_cross_suffix_c16_full_ml_topology_20260813 import (  # noqa:E402
    lifted_edges,
)
from verify_t2_c16_suffix_component_residence_20260813 import (  # noqa:E402
    projected_cycles,
    toggle,
)


def orient(owners, labels, reverse):
    if not reverse:
        return list(owners), list(labels)
    return [owners[0], *reversed(owners[1:])], list(reversed(labels))


def build_data(selection):
    m, n = 11, 22
    canonical = base.canonical_edges(m)
    post = set(canonical)
    base.apply_t2(post, list(base.dyck_words(5)))
    before_all = projected_cycles(lifted_edges(post, canonical, n), m)
    circuits = []
    touched = set()
    changed_owner = {}
    for circuit, item in enumerate(selection["selection"]):
        owners = tuple(
            base.bits(word) for word in item["candidate"]["owners"]
        )
        colours = tuple(
            base.bits(word) for word in item["candidate"]["new_colours"]
        )
        rows = [
            (owners[index], colours[index - 1], colours[index])
            for index in range(len(owners))
        ]
        circuits.append(rows)
        touched.update(owners)
        for row, owner in enumerate(owners):
            changed_owner[owner] = {
                "circuit": circuit,
                "edge_index": item["edge_index"],
                "row": row,
            }
    before_cycles = [
        cycle for cycle in before_all if touched.intersection(cycle[0])
    ]
    simultaneous = toggle(post, circuits)
    after_cycles = [
        cycle for cycle in projected_cycles(
            lifted_edges(simultaneous, canonical, n), m
        )
        if touched.intersection(cycle[0])
    ]
    assert len(before_cycles) == 372 and len(after_cycles) == 1
    return n, before_cycles, after_cycles[0], changed_owner


def solve_core(before_cycles, post_cycle, post_reverse, bits=14):
    post_cycle = orient(*post_cycle, post_reverse)
    owners = sorted(post_cycle[0])
    owner_index = {owner: index for index, owner in enumerate(owners)}
    pre_component = {}
    pre_successors = {}
    for component, (cycle_owners, _) in enumerate(before_cycles):
        length = len(cycle_owners)
        for index, owner in enumerate(cycle_owners):
            pre_component[owner] = component
            pre_successors[owner] = (
                cycle_owners[(index + 1) % length],
                cycle_owners[index - 1],
            )
    post_successor = {
        owner: post_cycle[0][(index + 1) % len(post_cycle[0])]
        for index, owner in enumerate(post_cycle[0])
    }
    tag_variables = len(owners) * bits
    orientation_variables = {
        component: tag_variables + component + 1
        for component in range(len(before_cycles))
    }
    next_variable = tag_variables + len(before_cycles) + 1
    activation_variables = {}

    def tv(owner, bit):
        return owner_index[owner] * bits + bit + 1

    clauses = []
    owner_clauses = defaultdict(list)
    for owner in owners:
        orientation = orientation_variables[pre_component[owner]]
        post_head = post_successor[owner]
        for reverse, pre_head in enumerate(pre_successors[owner]):
            guard = orientation if reverse == 0 else -orientation
            differences = []
            for bit in range(bits):
                owner_clauses[owner].append([
                    guard, -tv(pre_head, bit), tv(post_head, bit)
                ])
                owner_clauses[owner].append([
                    guard, tv(pre_head, bit), -tv(post_head, bit)
                ])
                difference = next_variable
                next_variable += 1
                differences.append(difference)
                owner_clauses[owner].append([
                    -difference, tv(owner, bit), tv(pre_head, bit)
                ])
                owner_clauses[owner].append([
                    -difference, -tv(owner, bit), -tv(pre_head, bit)
                ])
            owner_clauses[owner].append([guard, *differences])
    for owner in owners:
        activation_variables[owner] = next_variable
        next_variable += 1
        activation = activation_variables[owner]
        clauses.extend([[-activation, *clause] for clause in owner_clauses[owner]])
    assumptions = list(activation_variables.values())
    activation_to_owner = {
        activation: owner for owner, activation in activation_variables.items()
    }
    with Solver(name="cadical195", bootstrap_with=clauses) as solver:
        assert not solver.solve(assumptions=assumptions)
        raw_core = list(solver.get_core())
        assert raw_core and all(literal > 0 for literal in raw_core)
        core = raw_core[:]
        index = 0
        while index < len(core):
            trial = core[:index] + core[index + 1:]
            if not solver.solve(assumptions=trial):
                core = list(solver.get_core())
                index = 0
            else:
                index += 1
        assert not solver.solve(assumptions=core)
        assert all(
            solver.solve(assumptions=core[:index] + core[index + 1:])
            for index in range(len(core))
        )
    core_owners = [activation_to_owner[literal] for literal in core]
    touched_components = sorted({pre_component[owner] for owner in core_owners})
    rows = []
    for owner in core_owners:
        rows.append({
            "owner": owner,
            "pre_component": pre_component[owner],
            "pre_forward_head": pre_successors[owner][0],
            "pre_reverse_head": pre_successors[owner][1],
            "post_head": post_successor[owner],
        })
    return {
        "post_reverse": post_reverse,
        "tag_bits": bits,
        "variables": next_variable - 1,
        "clauses": len(clauses),
        "raw_assumption_core_size": len(raw_core),
        "minimal_owner_core_size": len(core),
        "touched_pre_components": touched_components,
        "rows": rows,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("selection")
    args = parser.parse_args()
    raw = Path(args.selection).read_bytes()
    selection = json.loads(raw)
    n, before_cycles, post_cycle, changed_owner = build_data(selection)
    results = [
        solve_core(before_cycles, post_cycle, post_reverse)
        for post_reverse in (0, 1)
    ]
    for result in results:
        for row in result["rows"]:
            owner = row["owner"]
            row["owner"] = base.bitword(owner, n + 1)
            for key in (
                "pre_forward_head", "pre_reverse_head", "post_head"
            ):
                row[key] = base.bitword(row[key], n + 1)
            row["selected_role"] = changed_owner.get(owner)
    print(json.dumps({
        "status": "PASS",
        "selection_sha256": hashlib.sha256(raw).hexdigest(),
        "interpretation": (
            "14 bits permit private tags for all 12420 owners; each core "
            "is an alphabet-independent quotient-loop obstruction"
        ),
        "orientations": results,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
