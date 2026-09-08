#!/usr/bin/env python3
"""Solve and verify a variable-successor-tag lift of the frozen D5 bank.

Substantive execution belongs on H100.  We orient every affected pre-switch
cycle and the unique post-switch cycle, then solve

    tag(s_minus(v)) = tag(s_plus(v)) != tag(v).

For the minimum feasible tag alphabet, the script expands the two states by
the h=2 variable-tag clock block and audits literal graph/palette simplicity,
component action, two-shore q=2 residence, and width-three target support.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

from pysat.solvers import Solver

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import search_t2_cross_suffix_alternating_cycles_20260813 as base  # noqa:E402
from audit_t2_cross_suffix_c16_full_ml_topology_20260813 import (  # noqa:E402
    lifted_edges,
)
from verify_t2_c16_suffix_component_residence_20260813 import (  # noqa:E402
    cyclic_run_minimum,
    projected_cycles,
    toggle,
)


def orient(owners, labels, reverse):
    if not reverse:
        return list(owners), list(labels)
    return [owners[0], *reversed(owners[1:])], list(reversed(labels))


def exactly_one(clauses, variables):
    clauses.append(list(variables))
    for i, left in enumerate(variables):
        for right in variables[i + 1:]:
            clauses.append([-left, -right])


def tag_solver(pre_cycles, post_cycle, colours):
    owners = sorted(post_cycle[0])
    owner_index = {owner: index for index, owner in enumerate(owners)}
    pre_component = {}
    pre_successors = {}
    for component, (cycle_owners, _) in enumerate(pre_cycles):
        length = len(cycle_owners)
        for index, owner in enumerate(cycle_owners):
            assert owner not in pre_component
            pre_component[owner] = component
            pre_successors[owner] = (
                cycle_owners[(index + 1) % length],
                cycle_owners[index - 1],
            )
    assert set(pre_component) == set(owners)
    post_successor = {
        owner: post_cycle[0][(index + 1) % len(post_cycle[0])]
        for index, owner in enumerate(post_cycle[0])
    }

    tag_variables = len(owners) * colours
    orientation_variables = {
        component: tag_variables + component + 1
        for component in range(len(pre_cycles))
    }

    def tv(owner, colour):
        return owner_index[owner] * colours + colour + 1

    clauses = []
    for owner in owners:
        exactly_one(clauses, [tv(owner, c) for c in range(colours)])
    for owner in owners:
        component = pre_component[owner]
        orientation = orientation_variables[component]
        post_head = post_successor[owner]
        for reverse, pre_head in enumerate(pre_successors[owner]):
            guard = orientation if reverse == 0 else -orientation
            for colour in range(colours):
                # If this orientation is active, the two heads have equal
                # tags and that tag differs from the tail tag.
                clauses.append([
                    guard, -tv(pre_head, colour), tv(post_head, colour)
                ])
                clauses.append([
                    guard, tv(pre_head, colour), -tv(post_head, colour)
                ])
                clauses.append([
                    guard, -tv(owner, colour), -tv(pre_head, colour)
                ])
    with Solver(name="cadical195", bootstrap_with=clauses) as solver:
        sat = solver.solve()
        if not sat:
            return None, {
                "status": "UNSAT",
                "variables": tag_variables + len(pre_cycles),
                "clauses": len(clauses),
            }
        model = set(literal for literal in solver.get_model() if literal > 0)
    tags = {
        owner: next(
            colour for colour in range(colours) if tv(owner, colour) in model
        )
        for owner in owners
    }
    orientations = {
        component: int(orientation_variables[component] in model)
        for component in range(len(pre_cycles))
    }
    for owner in owners:
        pre_head = pre_successors[owner][orientations[pre_component[owner]]]
        post_head = post_successor[owner]
        assert tags[pre_head] == tags[post_head] != tags[owner]
    return (tags, orientations), {
        "status": "SAT",
        "variables": tag_variables + len(pre_cycles),
        "clauses": len(clauses),
    }


def unrestricted_tag_solver(pre_cycles, post_cycle, bits=14):
    """Decide the no-loop quotient criterion with binary class names."""
    owners = sorted(post_cycle[0])
    owner_index = {owner: index for index, owner in enumerate(owners)}
    pre_component = {}
    pre_successors = {}
    for component, (cycle_owners, _) in enumerate(pre_cycles):
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
    tag_variable_count = len(owners) * bits
    orientation_variables = {
        component: tag_variable_count + component + 1
        for component in range(len(pre_cycles))
    }
    next_variable = tag_variable_count + len(pre_cycles) + 1

    def tv(owner, bit):
        return owner_index[owner] * bits + bit + 1

    clauses = []
    for owner in owners:
        orientation = orientation_variables[pre_component[owner]]
        post_head = post_successor[owner]
        for reverse, pre_head in enumerate(pre_successors[owner]):
            guard = orientation if reverse == 0 else -orientation
            differences = []
            for bit in range(bits):
                # Conditional equality of the two successor tags.
                clauses.append([
                    guard, -tv(pre_head, bit), tv(post_head, bit)
                ])
                clauses.append([
                    guard, tv(pre_head, bit), -tv(post_head, bit)
                ])
                # A one-way XOR witness is enough for the inequality OR.
                difference = next_variable
                next_variable += 1
                differences.append(difference)
                clauses.append([
                    -difference, tv(owner, bit), tv(pre_head, bit)
                ])
                clauses.append([
                    -difference, -tv(owner, bit), -tv(pre_head, bit)
                ])
            clauses.append([guard, *differences])
    with Solver(name="cadical195", bootstrap_with=clauses) as solver:
        sat = solver.solve()
        report = {
            "status": "SAT" if sat else "UNSAT",
            "tag_bits": bits,
            "variables": next_variable - 1,
            "clauses": len(clauses),
        }
        if not sat:
            return None, report
        model = set(literal for literal in solver.get_model() if literal > 0)
    orientations = {
        component: int(orientation_variables[component] in model)
        for component in range(len(pre_cycles))
    }
    codes = {
        owner: sum(
            (1 << bit) for bit in range(bits) if tv(owner, bit) in model
        )
        for owner in owners
    }
    for owner in owners:
        head = pre_successors[owner][orientations[pre_component[owner]]]
        assert codes[head] == codes[post_successor[owner]] != codes[owner]
    report["used_codes"] = len(set(codes.values()))
    return (codes, orientations), report


def expand_trace(owners, tags, tag_bits, clock_bits):
    h = 2
    d = [
        clock_bits[index] | clock_bits[(index + 1) % (2 * h)]
        for index in range(2 * h + 1)
    ]
    answer = []
    length = len(owners)
    for index, owner in enumerate(owners):
        head = owners[(index + 1) % length]
        a, b = tags[owner], tags[head]
        assert a != b
        answer.extend((
            owner | tag_bits[a] | d[0],
            owner | tag_bits[a] | d[1],
            owner | tag_bits[a] | d[2],
            owner | tag_bits[b] | d[2],
            owner | tag_bits[b] | d[3],
            owner | tag_bits[b] | d[4],
        ))
    return answer


def width_support(trace, width):
    length = len(trace)
    return Counter(
        __import__("functools").reduce(
            int.__or__,
            (trace[(index + step) % length] for step in range(width)),
        )
        for index in range(length)
    )


def audit_expansion(traces, tags, tag_bits, clock_bits, ground_size):
    owner_bank = set()
    lower_bank = set()
    upper_bank = set()
    width3 = Counter()
    minimum_lower = [ground_size + 1, ground_size + 1]
    minimum_upper = [ground_size + 1, ground_size + 1]
    lengths = []
    for trace in traces:
        expanded = expand_trace(trace, tags, tag_bits, clock_bits)
        length = len(expanded)
        lengths.append(length)
        assert len(set(expanded)) == length
        assert not owner_bank.intersection(expanded)
        owner_bank.update(expanded)
        lower = [
            expanded[index] & expanded[(index + 1) % length]
            for index in range(length)
        ]
        upper = [
            expanded[index] | expanded[(index + 1) % length]
            for index in range(length)
        ]
        assert len(set(lower)) == length
        assert len(set(upper)) == length
        assert not lower_bank.intersection(lower)
        assert not upper_bank.intersection(upper)
        lower_bank.update(lower)
        upper_bank.update(upper)
        supports = [
            expanded[index] ^ expanded[(index + 1) % length]
            for index in range(length)
        ]
        upper_supports = [
            upper[index] ^ upper[(index + 1) % length]
            for index in range(length)
        ]
        assert all(support.bit_count() == 2 for support in supports)
        assert all(support.bit_count() == 2 for support in upper_supports)
        assert all(not supports[index - 1] & supports[index]
                   for index in range(length))
        assert all(not upper_supports[index - 1] & upper_supports[index]
                   for index in range(length))
        width3.update(width_support(expanded, 3))
        lp, _ = cyclic_run_minimum(expanded, ground_size, 1)
        lz, _ = cyclic_run_minimum(expanded, ground_size, 0)
        up, _ = cyclic_run_minimum(upper, ground_size, 1)
        uz, _ = cyclic_run_minimum(upper, ground_size, 0)
        minimum_lower[0] = min(minimum_lower[0], lp)
        minimum_lower[1] = min(minimum_lower[1], lz)
        minimum_upper[0] = min(minimum_upper[0], up)
        minimum_upper[1] = min(minimum_upper[1], uz)
    return {
        "owners": owner_bank,
        "lower": lower_bank,
        "upper": upper_bank,
        "width3": width3,
        "component_lengths": lengths,
        "minimum_lower": minimum_lower,
        "minimum_upper": minimum_upper,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("selection")
    args = parser.parse_args()
    raw = Path(args.selection).read_bytes()
    data = json.loads(raw)
    assert data["status"] == "SAT" and len(data["selection"]) == 41

    m, n = 11, 22
    canonical = base.canonical_edges(m)
    post = set(canonical)
    base.apply_t2(post, list(base.dyck_words(5)))
    before_all = projected_cycles(lifted_edges(post, canonical, n), m)
    circuits = []
    touched = set()
    for item in data["selection"]:
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
    before_cycles = [
        (owners, labels) for owners, labels in before_all
        if touched.intersection(owners)
    ]
    assert len(before_cycles) == 372

    simultaneous = toggle(post, circuits)
    after_all = projected_cycles(
        lifted_edges(simultaneous, canonical, n), m
    )
    after_cycles = [
        (owners, labels) for owners, labels in after_all
        if touched.intersection(owners)
    ]
    assert len(after_cycles) == 1 and len(after_cycles[0][0]) == 12420
    post_cycle = after_cycles[0]

    solver_trials = []
    solution = None
    alphabet = None
    post_orientation = None
    tested_post_cycles = [
        post_cycle,
        orient(*post_cycle, True),
    ]
    for post_reverse, tested_post_cycle in enumerate(tested_post_cycles):
        for colours in range(1, 9):
            solution, report = tag_solver(
                before_cycles, tested_post_cycle, colours
            )
            report["tag_states"] = colours
            report["post_reverse"] = post_reverse
            solver_trials.append(report)
            if solution is not None:
                alphabet = colours
                post_orientation = post_reverse
                post_cycle = tested_post_cycle
                break
        if solution is not None:
            break
    unrestricted = None
    unrestricted_reports = []
    if solution is None:
        for post_reverse, tested_post_cycle in enumerate(tested_post_cycles):
            unrestricted, unrestricted_report = unrestricted_tag_solver(
                before_cycles, tested_post_cycle
            )
            unrestricted_report["post_reverse"] = post_reverse
            unrestricted_reports.append(unrestricted_report)
        print(json.dumps({
            "status": "BOUNDED_TAG_FAILURE",
            "selection_sha256": hashlib.sha256(raw).hexdigest(),
            "solver_trials": solver_trials,
            "unrestricted_quotient_tests": unrestricted_reports,
        }, indent=2, sort_keys=True))
        return
    tags, orientations = solution

    oriented_before = [
        orient(*cycle, orientations[component])[0]
        for component, cycle in enumerate(before_cycles)
    ]
    oriented_after = [post_cycle[0]]
    before_successor = {
        owner: trace[(index + 1) % len(trace)]
        for trace in oriented_before
        for index, owner in enumerate(trace)
    }
    after_successor = {
        owner: post_cycle[0][(index + 1) % len(post_cycle[0])]
        for index, owner in enumerate(post_cycle[0])
    }
    assert set(before_successor) == set(after_successor) == set(tags)
    assert all(
        tags[before_successor[owner]] == tags[after_successor[owner]]
        != tags[owner]
        for owner in tags
    )

    tag_bits = [1 << (n + 1 + index) for index in range(alphabet)]
    clock_bits = [
        1 << (n + 1 + alphabet + index) for index in range(4)
    ]
    ground_size = n + 1 + alphabet + 4
    before_audit = audit_expansion(
        oriented_before, tags, tag_bits, clock_bits, ground_size
    )
    after_audit = audit_expansion(
        oriented_after, tags, tag_bits, clock_bits, ground_size
    )
    assert before_audit["owners"] == after_audit["owners"]
    assert before_audit["lower"] == after_audit["lower"]
    assert before_audit["upper"] == after_audit["upper"]
    losses = {
        target: count
        for target, count in before_audit["width3"].items()
        if after_audit["width3"][target] == 0
    }
    load_decreases = {
        target: count - after_audit["width3"][target]
        for target, count in before_audit["width3"].items()
        if after_audit["width3"][target] < count
    }

    changed = sum(
        before_successor[owner] != after_successor[owner] for owner in tags
    )
    print(json.dumps({
        "status": "PASS",
        "selection_sha256": hashlib.sha256(raw).hexdigest(),
        "solver_trials": solver_trials,
        "minimum_tag_states": alphabet,
        "post_reverse": post_orientation,
        "tag_histogram": dict(sorted(Counter(tags.values()).items())),
        "pre_orientation_histogram": dict(sorted(
            Counter(orientations.values()).items()
        )),
        "common_successor_tag_equations": len(tags),
        "changed_successors": changed,
        "source_blocks_preserved_exactly": True,
        "fresh_tag_coordinates": alphabet,
        "fresh_clock_coordinates": 4,
        "clock_height": 2,
        "expanded_ground_size": ground_size,
        "expanded_owner_rank": m + 3,
        "expanded_owner_count": len(after_audit["owners"]),
        "expanded_pre_components": len(before_audit["component_lengths"]),
        "expanded_post_components": len(after_audit["component_lengths"]),
        "expanded_component_reduction": (
            len(before_audit["component_lengths"])
            - len(after_audit["component_lengths"])
        ),
        "expanded_owner_ledger_invariant": True,
        "expanded_immediate_lower_ledger_invariant": True,
        "expanded_immediate_upper_ledger_invariant": True,
        "pre_lower_minimum_positive_zero_runs": before_audit["minimum_lower"],
        "post_lower_minimum_positive_zero_runs": after_audit["minimum_lower"],
        "pre_upper_minimum_positive_zero_runs": before_audit["minimum_upper"],
        "post_upper_minimum_positive_zero_runs": after_audit["minimum_upper"],
        "two_shore_q2_resident": all(
            value >= 2
            for value in (
                *before_audit["minimum_lower"],
                *after_audit["minimum_lower"],
                *before_audit["minimum_upper"],
                *after_audit["minimum_upper"],
            )
        ),
        "expanded_width3_old_support": len(before_audit["width3"]),
        "expanded_width3_new_support": len(after_audit["width3"]),
        "expanded_width3_support_losses": len(losses),
        "expanded_width3_total_lost_occurrences": sum(losses.values()),
        "expanded_width3_load_decrease_targets": len(load_decreases),
        "expanded_width3_load_decrease_occurrences": sum(
            load_decreases.values()
        ),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
