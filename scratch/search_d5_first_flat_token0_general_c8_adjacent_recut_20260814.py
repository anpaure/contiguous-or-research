#!/usr/bin/env python3
"""Exhaust general adjacent-placement alternating C8 repairs.

Run substantively on H100 only.  The prescribed context and router old cuts
are adjacent in the alternating C8.  One new edge joins one pair of their
endpoints directly; the other side is a five-edge path through two freely
chosen auxiliary old cuts.  A meet-in-the-middle current join enumerates
every such simple Johnson C8, then checks complete owner/q1 simplicity and
the fixed-side q2/residence collar in both router phases.
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
from search_d5_first_flat_token0_general_c8_joint_recut_20260814 import (  # noqa:E402
    current_key,
    fixed_target,
    neighbors,
    subtract_current,
)
from search_d5_first_flat_token0_c8_transition_collar_20260814 import (  # noqa:E402
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
import solve_d5_tapped_c6_212_coinstantiation_20260814 as d5  # noqa:E402


def is_johnson(a, b):
    return len(a ^ b) == 2


def length_two_paths(start, excluded):
    """All start--u--v paths; first edge is new and second edge old."""
    answer = []
    for u in neighbors(start):
        if u in excluded:
            continue
        for v in neighbors(u):
            if v in excluded or v in {start, u}:
                continue
            answer.append((start, u, v))
    return answer


def half_current(path):
    start, u, v = path
    result = []
    for shore in (0, 1):
        value = Counter([q1(edge(start, u))[shore]])
        value.subtract([q1(edge(u, v))[shore]])
        result.append(value)
    return tuple(result)


def add_resource(current, resource_edge):
    result = []
    for shore in (0, 1):
        item = Counter(current[shore])
        item[q1(resource_edge)[shore]] += 1
        result.append(item)
    return tuple(result)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("selection")
    parser.add_argument("certificate")
    parser.add_argument("q1_witnesses")
    parser.add_argument("--max-output", type=int, default=100)
    parser.add_argument("--witness-start", type=int, default=0)
    parser.add_argument("--witness-end", type=int, default=21)
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
    reports = []

    assert 0 <= args.witness_start <= args.witness_end <= len(witnesses)
    for witness_index in range(args.witness_start, args.witness_end):
        witness = witnesses[witness_index]
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
        prescribed = set(context_cut) | set(router_cut)
        forbidden_aux = (other_owners | router_owners | set(context_cut)) - prescribed

        for context_orientation in (tuple(context_cut), tuple(reversed(tuple(context_cut)))):
            for router_orientation in (tuple(router_cut), tuple(reversed(tuple(router_cut)))):
                a0, b0 = context_orientation
                a1, b1 = router_orientation
                direct = edge(b0, a1)
                if not is_johnson(b0, a1):
                    counters["non_johnson_direct_orientations"] += 1
                    reports.append({
                        "witness_index": witness_index,
                        "context_orientation": context_orientation,
                        "router_orientation": router_orientation,
                        "direct_johnson": False,
                    })
                    continue
                counters["johnson_direct_orientations"] += 1
                excluded = {a0, b0, a1, b1}
                left_paths = length_two_paths(b1, excluded)
                right_paths = length_two_paths(a0, excluded)
                target = fixed_target(context_cut, router_cut)
                # Exact equality is
                #   left_current + middle_new + right_current
                #       = old_fixed - direct_new.
                direct_current = tuple(Counter([q1(direct)[shore]]) for shore in (0, 1))
                target = subtract_current(target, direct_current)
                right_index = defaultdict(list)
                for path in right_paths:
                    right_index[(path[2], current_key(half_current(path)))].append(path)

                q1_pairs = owner_pairs = 0
                for left in left_paths:
                    _, u, v = left
                    left_current = half_current(left)
                    for w in neighbors(v):
                        if w in excluded or w in {u, v}:
                            continue
                        middle = edge(v, w)
                        need = subtract_current(target, add_resource(left_current, middle))
                        for right in right_index.get((w, current_key(need)), ()):
                            q1_pairs += 1
                            counters["q1_exact_path_pairs"] += 1
                            _, x, w_check = right
                            assert w_check == w
                            collar_owners = (a0, b0, a1, b1, u, v, w, x)
                            if len(set(collar_owners)) != 8:
                                continue
                            if {u, v, w, x} & forbidden_aux:
                                continue
                            owner_pairs += 1
                            counters["owner_simple_path_pairs"] += 1
                            old = (context_cut, router_cut, edge(u, v), edge(w, x))
                            new = (direct, edge(b1, u), middle, edge(x, a0))
                            assert exact_q1(old, new)
                            if not simple_q1(old) or not simple_q1(new):
                                continue
                            counters["collar_q1_simple"] += 1

                            phase_before = []
                            phase_after = []
                            valid = True
                            for router_phase in router_phases:
                                before = set(router_phase) | set(other_old) | set(old)
                                after = (set(router_phase) - router_cuts) | set(other_new) | set(new)
                                if len(before) != 25 or len(after) != 25:
                                    valid = False
                                    break
                                if not exact_q1(before, after) or not simple_q1(before) or not simple_q1(after):
                                    valid = False
                                    break
                                phase_before.append(before)
                                phase_after.append(after)
                            if not valid:
                                continue
                            counters["full_q1_exact_simple_both_phases"] += 1

                            auxiliary = (old[2], old[3]) + tuple(other_aux)
                            fixed_reports = []
                            q2_by_phase = []
                            resident = True
                            for after in phase_after:
                                fixed = after | exterior_collar_edges
                                phase_report = fixed_path_reports(fixed, auxiliary)
                                fixed_reports.append(phase_report)
                                if any(item.get("resolved") and not item["resident"] for item in phase_report):
                                    resident = False
                                q2_by_phase.append(internal_q2(fixed))
                            if not resident:
                                counters["fixed_side_residence_failure"] += 1
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
                                "c8_auxiliary_edges": (old[2], old[3]),
                                "other_roles": other_roles,
                                "all_auxiliary_edges": auxiliary,
                                "before_edges": phase_before,
                                "after_edges": phase_after,
                                "fixed_path_reports": fixed_reports,
                                "internal_q2_count": tuple(map(len, q2_by_phase)),
                                "internal_q2_lower_delta": lower_delta,
                                "internal_q2_upper_delta": upper_delta,
                            })
                            if len(solutions) >= args.max_output:
                                break
                        if len(solutions) >= args.max_output:
                            break
                    if len(solutions) >= args.max_output:
                        break
                reports.append({
                    "witness_index": witness_index,
                    "context_orientation": context_orientation,
                    "router_orientation": router_orientation,
                    "direct_johnson": True,
                    "left_paths": len(left_paths),
                    "right_paths": len(right_paths),
                    "q1_exact_path_pairs": q1_pairs,
                    "owner_simple_path_pairs": owner_pairs,
                })
                if len(solutions) >= args.max_output:
                    break
            if len(solutions) >= args.max_output:
                break
        if len(solutions) >= args.max_output:
            break

    output = {
        "status": "PASS" if solutions else "NO_WITNESS",
        "class": "general owner-simple alternating C8 with prescribed adjacent context/router cuts",
        "selection_sha256": hashlib.sha256(selection_raw).hexdigest(),
        "certificate_sha256": hashlib.sha256(certificate_raw).hexdigest(),
        "q1_witnesses_sha256": hashlib.sha256(q1_raw).hexdigest(),
        "source_witnesses": len(witnesses),
        "witness_range": [args.witness_start, args.witness_end],
        "counters": dict(counters),
        "orientation_reports": reports,
        "solutions": solutions,
    }
    print(json.dumps(encode(output), indent=2, sort_keys=True))
    if not solutions:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
