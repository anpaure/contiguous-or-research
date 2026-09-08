#!/usr/bin/env python3
"""Search the smallest noncanonical C8 joint recut on the first flat factor.

Run substantively on H100 only.  The old alternating matching has four
Johnson cuts in cyclic order

    context, auxiliary-left, router, auxiliary-right,

so the prescribed context and router cuts are opposite.  The new matching
uses the four cross edges.  This is the smallest alternating collar that
actually replaces both seam-to-router joins: each side contains one freely
chosen auxiliary Johnson cut.  The program enumerates all simple length-3
Johnson paths between the oriented prescribed endpoints, hash-joins the two
halves by exact lower/upper-q1 current, and audits owner/q1 simplicity and
every fixed-side q2/residence window in both router phases.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import solve_d5_tapped_c6_212_coinstantiation_20260814 as d5  # noqa:E402
from search_d5_first_flat_token0_c8_transition_collar_20260814 import (  # noqa:E402
    adjacency,
    context_collar_edges,
    counter_delta,
    cycle_edges,
    decode,
    decode_edge,
    edge,
    encode,
    exact_q1,
    fixed_path_reports,
    internal_q2,
    q1,
    router_edges,
    simple_q1,
)

GROUND = frozenset(range(23))


def neighbors(owner):
    return {
        frozenset((owner - {out}) | {inside})
        for out in owner
        for inside in GROUND - owner
    }


def length_three_paths(start, end, forbidden):
    """All oriented start--a--b--end paths with two fresh owners."""
    end_neighbors = neighbors(end)
    answer = []
    for a in neighbors(start):
        if a in forbidden or a == end:
            continue
        for b in neighbors(a) & end_neighbors:
            if b in forbidden or b in {start, a}:
                continue
            answer.append((start, a, b, end))
    return answer


def resource_int(resource):
    return sum(1 << x for x in resource)


def current_key(current):
    return tuple(
        tuple(sorted((resource_int(resource), coefficient) for resource, coefficient in shore.items() if coefficient))
        for shore in current
    )


def path_current(path):
    start, a, b, end = path
    old = edge(a, b)
    new = (edge(start, a), edge(b, end))
    result = []
    for shore in (0, 1):
        value = Counter(q1(e)[shore] for e in new)
        value.subtract([q1(old)[shore]])
        result.append(value)
    return tuple(result)


def subtract_current(target, value):
    result = []
    for shore in (0, 1):
        item = Counter(target[shore])
        item.subtract(value[shore])
        result.append(item)
    return tuple(result)


def fixed_target(context_cut, router_cut):
    return tuple(Counter(q1(e)[shore] for e in (context_cut, router_cut)) for shore in (0, 1))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("selection")
    parser.add_argument("certificate")
    parser.add_argument("q1_witnesses")
    parser.add_argument("--max-output", type=int, default=100)
    args = parser.parse_args()
    selection_raw = Path(args.selection).read_bytes()
    certificate_raw = Path(args.certificate).read_bytes()
    q1_raw = Path(args.q1_witnesses).read_bytes()
    selection = json.loads(selection_raw)
    certificate = json.loads(certificate_raw)
    source = json.loads(q1_raw)
    witnesses = source["witnesses"]
    assert len(witnesses) == 21

    all_context_cuts = {
        decode_edge(role["collar"]["old"][0])
        for role in witnesses[0]["roles"]
    }
    exterior_collar_edges = context_collar_edges(selection, certificate, all_context_cuts)
    counters = Counter()
    solutions = []
    failure_histogram = Counter()
    orientation_reports = []

    for witness_index, witness in enumerate(witnesses):
        cycles = tuple(tuple(decode(owner) for owner in cycle) for cycle in witness["router_cycles"])
        roles = witness["roles"]
        token_zero_port = witness["token_permutation"].index(0)
        role0 = roles[token_zero_port]
        context_cut = decode_edge(role0["collar"]["old"][0])
        router_cut = decode_edge(role0["router_edge"])
        router_cuts = {decode_edge(role["router_edge"]) for role in roles}
        other_roles = [role for i, role in enumerate(roles) if i != token_zero_port]
        other_old = [decode_edge(e) for role in other_roles for e in role["collar"]["old"]]
        other_new = [decode_edge(e) for role in other_roles for e in role["collar"]["new"]]
        other_aux = [decode_edge(role["auxiliary_edge"]) for role in other_roles]
        other_owners = set().union(*(
            set(map(decode, role["collar"]["a"])) | set(map(decode, role["collar"]["b"]))
            for role in other_roles
        ))
        router_owners = set().union(*map(set, cycles))
        router_phases = tuple(router_edges(cycles, switched) for switched in (False, True))
        prescribed_owners = set(context_cut) | set(router_cut)
        # Fresh auxiliary owners must avoid every already used owner except
        # the four prescribed endpoints, which remain literal occurrences.
        forbidden_aux = (other_owners | router_owners | set(context_cut)) - prescribed_owners
        target = fixed_target(context_cut, router_cut)

        for context_orientation in (tuple(context_cut), tuple(reversed(tuple(context_cut)))):
            for router_orientation in (tuple(router_cut), tuple(reversed(tuple(router_cut)))):
                a0, b0 = context_orientation
                a2, b2 = router_orientation
                # Enumerate the raw local C8 first.  Ambient owner exclusions
                # are imposed after the q1 hash join, so the report separates
                # algebraic q1 feasibility from owner-simple embedding.
                left_paths = length_three_paths(b0, a2, {a0, b2})
                right_paths = length_three_paths(b2, a0, {b0, a2})
                counters["oriented_pairs"] += 1
                counters["left_paths"] += len(left_paths)
                counters["right_paths"] += len(right_paths)
                right_index = defaultdict(list)
                for path in right_paths:
                    right_index[current_key(path_current(path))].append(path)
                q1_join_pairs = 0
                owner_simple_pairs = 0
                for left in left_paths:
                    left_current = path_current(left)
                    need = current_key(subtract_current(target, left_current))
                    for right in right_index.get(need, ()):
                        q1_join_pairs += 1
                        counters["q1_exact_path_pairs"] += 1
                        _, a1, b1, _ = left
                        _, a3, b3, _ = right
                        collar_owners = (a0, b0, a1, b1, a2, b2, a3, b3)
                        if len(set(collar_owners)) != 8:
                            continue
                        if {a1, b1, a3, b3} & forbidden_aux:
                            continue
                        owner_simple_pairs += 1
                        counters["owner_simple_path_pairs"] += 1
                        old = (context_cut, edge(a1, b1), router_cut, edge(a3, b3))
                        new = (edge(b0, a1), edge(b1, a2), edge(b2, a3), edge(b3, a0))
                        assert exact_q1(old, new)
                        if not simple_q1(old) or not simple_q1(new):
                            continue
                        counters["collar_q1_simple"] += 1

                        phase_before = []
                        phase_after = []
                        valid_q1 = True
                        for router_phase in router_phases:
                            before = set(router_phase) | set(other_old) | set(old)
                            after = (set(router_phase) - router_cuts) | set(other_new) | set(new)
                            if len(before) != 25 or len(after) != 25:
                                valid_q1 = False
                                break
                            if not exact_q1(before, after) or not simple_q1(before) or not simple_q1(after):
                                valid_q1 = False
                                break
                            phase_before.append(before)
                            phase_after.append(after)
                        if not valid_q1:
                            continue
                        counters["full_q1_exact_simple_both_phases"] += 1

                        auxiliary = (old[1], old[3]) + tuple(other_aux)
                        reports_by_phase = []
                        q2_by_phase = []
                        resident = True
                        for after in phase_after:
                            fixed = after | exterior_collar_edges
                            reports = fixed_path_reports(fixed, auxiliary)
                            reports_by_phase.append(reports)
                            bad = [item for item in reports if item.get("resolved") and not item["resident"]]
                            failure_histogram[len(bad)] += 1
                            if bad:
                                resident = False
                            q2_by_phase.append(internal_q2(fixed))
                        if not resident:
                            continue
                        counters["all_fixed_side_runs_at_least_three"] += 1

                        lower_delta = counter_delta(q2_by_phase[1], q2_by_phase[0], 0)
                        upper_delta = counter_delta(q2_by_phase[1], q2_by_phase[0], 1)
                        if not lower_delta and not upper_delta:
                            counters["internal_q2_zero_current"] += 1
                        solutions.append({
                            "witness_index": witness_index,
                            "token_permutation": witness["token_permutation"],
                            "token_zero_port": token_zero_port,
                            "context_orientation": context_orientation,
                            "router_orientation": router_orientation,
                            "router_cycles": cycles,
                            "router_cuts": router_cuts,
                            "c8_old": old,
                            "c8_new": new,
                            "c8_auxiliary_edges": (old[1], old[3]),
                            "other_roles": other_roles,
                            "all_auxiliary_edges": auxiliary,
                            "before_edges": phase_before,
                            "after_edges": phase_after,
                            "fixed_path_reports": reports_by_phase,
                            "internal_q2_count": tuple(map(len, q2_by_phase)),
                            "internal_q2_lower_delta": lower_delta,
                            "internal_q2_upper_delta": upper_delta,
                        })
                        if len(solutions) >= args.max_output:
                            break
                    if len(solutions) >= args.max_output:
                        break
                orientation_reports.append({
                    "witness_index": witness_index,
                    "context_orientation": context_orientation,
                    "router_orientation": router_orientation,
                    "left_paths": len(left_paths),
                    "right_paths": len(right_paths),
                    "q1_exact_path_pairs": q1_join_pairs,
                    "owner_simple_path_pairs": owner_simple_pairs,
                })
                if len(solutions) >= args.max_output:
                    break
            if len(solutions) >= args.max_output:
                break
        if len(solutions) >= args.max_output:
            break

    output = {
        "status": "PASS" if solutions else "NO_WITNESS",
        "class": "general owner-simple alternating C8 with prescribed opposite context/router cuts",
        "selection_sha256": hashlib.sha256(selection_raw).hexdigest(),
        "certificate_sha256": hashlib.sha256(certificate_raw).hexdigest(),
        "q1_witnesses_sha256": hashlib.sha256(q1_raw).hexdigest(),
        "source_witnesses": len(witnesses),
        "counters": dict(counters),
        "failure_histogram_per_phase": dict(failure_histogram),
        "orientation_reports": orientation_reports,
        "solutions": solutions,
    }
    print(json.dumps(encode(output), indent=2, sort_keys=True))
    if not solutions:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
