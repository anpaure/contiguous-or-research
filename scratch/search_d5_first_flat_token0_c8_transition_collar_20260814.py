#!/usr/bin/env python3
"""Search the first flat factor for the minimal one-extra-cut C8 repair.

Run substantively on H100 only.  Starting from every canonical C6-strand
q1 witness, replace only the failing logical-token-0 C6 collar by the
canonical four-versus-four alternating C8 seam

    A_i = C + x_i + x_(i-1),   B_i = C + x_i + y,
    old A_i--B_i,               new A_i--B_(i-1).

The context cut and the already selected router cut are prescribed; the
other two old edges are boundary/dummy cuts.  The search requires complete
owner and lower/upper-q1 simplicity and exact q1 refill in both router
phases.  It then audits every three-support window determined wholly on the
fixed context/router side and records the internal crossing-q2 current.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import Counter, defaultdict
from itertools import permutations
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import solve_d5_tapped_c6_212_coinstantiation_20260814 as d5  # noqa:E402

GROUND = frozenset(range(23))


def decode(word):
    return frozenset(i for i, c in enumerate(word) if c == "1")


def decode_edge(value):
    return frozenset(decode(word) for word in value)


def edge(a, b):
    return frozenset((a, b))


def cycle_edges(cycle):
    return {edge(owner, cycle[(i + 1) % len(cycle)]) for i, owner in enumerate(cycle)}


def router_edges(cycles, switched):
    result = set().union(*(cycle_edges(cycle) for cycle in cycles))
    if switched:
        for i, cycle in enumerate(cycles):
            result.remove(edge(cycle[0], cycle[1]))
            result.add(edge(cycle[0], cycles[(i - 1) % 3][1]))
    return result


def q1(e):
    a, b = tuple(e)
    return a & b, a | b


def q2_at(left, center, right):
    return left & center & right, left | center | right


def exact_q1(before, after):
    return all(
        Counter(q1(e)[shore] for e in before) == Counter(q1(e)[shore] for e in after)
        for shore in (0, 1)
    )


def simple_q1(edges):
    return all(len(edges) == len({q1(e)[shore] for e in edges}) for shore in (0, 1))


def adjacency(edges):
    result = defaultdict(set)
    for e in edges:
        a, b = tuple(e)
        assert len(a ^ b) == 2
        result[a].add(b)
        result[b].add(a)
    return result


def context_collar_edges(selection, certificate, context_edges):
    _, raw_old, _ = d5.extract_rows(selection, certificate)
    canonical = set(d5.base.canonical_edges(11))
    integer_adj, _ = d5.factor_adjacency(d5.lifted_edges(raw_old, canonical))

    def integer(owner):
        return sum(1 << x for x in owner)

    result = set()
    for cut in context_edges:
        x, y = tuple(cut)
        for endpoint, other in ((x, y), (y, x)):
            endpoint_i, other_i = integer(endpoint), integer(other)
            one_i = next(value for value in integer_adj[endpoint_i] if value != other_i)
            two_i = next(value for value in integer_adj[one_i] if value != endpoint_i)
            one = frozenset(d5.bits_of(one_i))
            two = frozenset(d5.bits_of(two_i))
            result.add(edge(endpoint, one))
            result.add(edge(one, two))
    return result


def canonical_c8(context_edge):
    """Enumerate both cyclic orientations with prescribed old edge 0."""
    left, right = tuple(context_edge)
    lower = left & right
    left_extra = next(iter(left - lower))
    right_extra = next(iter(right - lower))
    seen = set()
    for x0 in sorted(lower):
        core = lower - {x0}
        for direction in (-1, 1):
            neighbor = direction % 4
            for neighbor_x, y in ((left_extra, right_extra), (right_extra, left_extra)):
                pool = sorted(GROUND - core - {x0, neighbor_x, y})
                free_indices = sorted({1, 2, 3} - {neighbor})
                for free_values in permutations(pool, 2):
                    xs_list = [None] * 4
                    xs_list[0] = x0
                    xs_list[neighbor] = neighbor_x
                    for index, value in zip(free_indices, free_values):
                        xs_list[index] = value
                    xs = tuple(xs_list)
                    aa = tuple(
                        frozenset(core | {xs[i], xs[(i + direction) % 4]})
                        for i in range(4)
                    )
                    bb = tuple(frozenset(core | {xs[i], y}) for i in range(4))
                    old = tuple(edge(aa[i], bb[i]) for i in range(4))
                    new = tuple(edge(aa[i], bb[(i + direction) % 4]) for i in range(4))
                    if old[0] != context_edge:
                        continue
                    key = (frozenset(old), frozenset(new))
                    if key in seen:
                        continue
                    seen.add(key)
                    assert len(set(aa) | set(bb)) == 8
                    assert exact_q1(old, new)
                    assert simple_q1(old) and simple_q1(new)
                    yield {
                        "core": core, "x": xs, "y": y,
                        "direction": direction,
                        "a": aa, "b": bb, "old": old, "new": new,
                    }


def fixed_path_reports(edges, auxiliary_cuts):
    """Report boundary-inward paths; unresolved means next cut is auxiliary."""
    adj = adjacency(edges)
    reports = []
    for cut_index, cut in enumerate(auxiliary_cuts):
        for endpoint in tuple(cut):
            assert len(adj[endpoint]) == 1
            other = next(iter(adj[endpoint]))
            item = {
                "cut_index": cut_index,
                "endpoint": endpoint,
                "join_neighbor": other,
                "join_support": endpoint ^ other,
            }
            if len(adj[other]) == 1:
                item["resolved"] = False
                reports.append(item)
                continue
            assert len(adj[other]) == 2
            one = next(owner for owner in adj[other] if owner != endpoint)
            if len(adj[one]) != 2:
                item["resolved"] = False
                item["one"] = one
                reports.append(item)
                continue
            two = next(owner for owner in adj[one] if owner != other)
            supports = (endpoint ^ other, other ^ one, one ^ two)
            repeated = (
                (supports[0] & supports[1])
                | (supports[0] & supports[2])
                | (supports[1] & supports[2])
            )
            q2_pair = (
                q2_at(endpoint, other, one),
                q2_at(other, one, two),
            )
            item.update({
                "resolved": True,
                "one": one,
                "two": two,
                "supports": supports,
                "union_size": len(set().union(*supports)),
                "resident": len(set().union(*supports)) == 6,
                "repeated": repeated,
                "q2": q2_pair,
                "lower_q2_equal": q2_pair[0][0] == q2_pair[1][0],
                "upper_q2_equal": q2_pair[0][1] == q2_pair[1][1],
            })
            reports.append(item)
    return reports


def internal_q2(edges):
    adj = adjacency(edges)
    rows = []
    for center, neighbors in adj.items():
        if len(neighbors) != 2:
            continue
        left, right = tuple(neighbors)
        rows.append((center, q2_at(left, center, right)))
    return rows


def counter_delta(after, before, shore):
    value = Counter(deck[shore] for _, deck in after)
    value.subtract(deck[shore] for _, deck in before)
    return {resource: coefficient for resource, coefficient in value.items() if coefficient}


def encode_set(value):
    return d5.base.bitword(sum(1 << x for x in value), 23)


def encode(value):
    if isinstance(value, frozenset):
        if all(isinstance(x, int) for x in value):
            return encode_set(value)
        return sorted(encode(x) for x in value)
    if isinstance(value, (tuple, list, set)):
        return [encode(x) for x in value]
    if isinstance(value, dict):
        return {str(k): encode(v) for k, v in value.items()}
    return value


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

    all_context_edges = {
        decode_edge(role["collar"]["old"][0])
        for role in witnesses[0]["roles"]
    }
    context_edges = context_collar_edges(selection, certificate, all_context_edges)
    counters = Counter()
    solutions = []
    failure_examples = []
    failure_union_histogram = Counter()
    repeated_coordinate_histogram = Counter()
    q2_duplicate_shore_histogram = Counter()

    for witness_index, witness in enumerate(witnesses):
        cycles = tuple(tuple(decode(owner) for owner in cycle) for cycle in witness["router_cycles"])
        roles = witness["roles"]
        token_zero_port = witness["token_permutation"].index(0)
        failing_role = roles[token_zero_port]
        prescribed_context = decode_edge(failing_role["collar"]["old"][0])
        prescribed_router = decode_edge(failing_role["router_edge"])
        router_cuts = {decode_edge(role["router_edge"]) for role in roles}
        other_roles = [role for i, role in enumerate(roles) if i != token_zero_port]
        other_old = [decode_edge(e) for role in other_roles for e in role["collar"]["old"]]
        other_new = [decode_edge(e) for role in other_roles for e in role["collar"]["new"]]
        other_aux = [decode_edge(role["auxiliary_edge"]) for role in other_roles]
        router_phases = tuple(router_edges(cycles, switched) for switched in (False, True))
        router_owners = set().union(*map(set, cycles))

        for candidate in canonical_c8(prescribed_context):
            counters["canonical_c8"] += 1
            if prescribed_router not in candidate["old"][1:]:
                continue
            counters["contains_router_cut"] += 1
            candidate_aux = tuple(e for e in candidate["old"] if e not in {prescribed_context, prescribed_router})
            assert len(candidate_aux) == 2
            collar_owner_sets = [set(candidate["a"]) | set(candidate["b"])]
            collar_owner_sets.extend(
                set(map(decode, role["collar"]["a"])) | set(map(decode, role["collar"]["b"]))
                for role in other_roles
            )
            collar_flat = [owner for owners in collar_owner_sets for owner in owners]
            if len(collar_flat) != len(set(collar_flat)):
                continue
            intended = set().union(*(set(cut) for cut in router_cuts))
            if set(collar_flat) & router_owners != intended:
                continue
            counters["owner_simple"] += 1

            candidate_old = list(candidate["old"])
            candidate_new = list(candidate["new"])
            phase_before = []
            phase_after = []
            valid_q1 = True
            for router_phase in router_phases:
                before = set(router_phase) | set(other_old) | set(candidate_old)
                after = (set(router_phase) - router_cuts) | set(other_new) | set(candidate_new)
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
            counters["q1_exact_simple_both_phases"] += 1

            auxiliary = tuple(candidate_aux) + tuple(other_aux)
            reports_by_phase = []
            q2_by_phase = []
            resident = True
            for after in phase_after:
                fixed = after | context_edges
                reports = fixed_path_reports(fixed, auxiliary)
                reports_by_phase.append(reports)
                if any(item.get("resolved") and not item["resident"] for item in reports):
                    resident = False
                q2_by_phase.append(internal_q2(fixed))
            if not resident:
                bad = [
                    (phase, item)
                    for phase, reports in enumerate(reports_by_phase)
                    for item in reports
                    if item.get("resolved") and not item["resident"]
                ]
                counters["fixed_side_failure_candidates"] += 1
                counters[f"fixed_side_bad_windows_{len(bad)}"] += 1
                for _, item in bad:
                    failure_union_histogram[item["union_size"]] += 1
                    repeated_coordinate_histogram.update(item["repeated"])
                    shore = (
                        "both" if item["lower_q2_equal"] and item["upper_q2_equal"]
                        else "lower" if item["lower_q2_equal"]
                        else "upper" if item["upper_q2_equal"]
                        else "neither"
                    )
                    q2_duplicate_shore_histogram[shore] += 1
                if len(failure_examples) < 20:
                    failure_examples.append({
                        "witness_index": witness_index,
                        "token_permutation": witness["token_permutation"],
                        "token_zero_port": token_zero_port,
                        "c8": candidate,
                        "c8_context_edge": prescribed_context,
                        "c8_router_edge": prescribed_router,
                        "c8_auxiliary_edges": candidate_aux,
                        "bad_fixed_paths": bad,
                    })
                continue
            counters["all_fixed_side_runs_at_least_three"] += 1

            lower_delta = counter_delta(q2_by_phase[1], q2_by_phase[0], 0)
            upper_delta = counter_delta(q2_by_phase[1], q2_by_phase[0], 1)
            if not lower_delta and not upper_delta:
                counters["internal_q2_zero_current"] += 1
            solution = {
                "witness_index": witness_index,
                "token_permutation": witness["token_permutation"],
                "token_zero_port": token_zero_port,
                "router_cycles": cycles,
                "router_cuts": router_cuts,
                "c8": candidate,
                "c8_context_edge": prescribed_context,
                "c8_router_edge": prescribed_router,
                "c8_auxiliary_edges": candidate_aux,
                "other_roles": other_roles,
                "all_auxiliary_edges": auxiliary,
                "before_edges": phase_before,
                "after_edges": phase_after,
                "fixed_path_reports": reports_by_phase,
                "internal_q2_count": tuple(map(len, q2_by_phase)),
                "internal_q2_lower_delta": lower_delta,
                "internal_q2_upper_delta": upper_delta,
            }
            solutions.append(solution)
            if len(solutions) >= args.max_output:
                break
        if len(solutions) >= args.max_output:
            break

    output = {
        "status": "PASS" if solutions else "NO_WITNESS",
        "class": "one canonical C8 on logical token 0; two canonical C6 collars unchanged",
        "selection_sha256": hashlib.sha256(selection_raw).hexdigest(),
        "certificate_sha256": hashlib.sha256(certificate_raw).hexdigest(),
        "q1_witnesses_sha256": hashlib.sha256(q1_raw).hexdigest(),
        "source_witnesses": len(witnesses),
        "counters": dict(counters),
        "failure_union_histogram": dict(failure_union_histogram),
        "repeated_coordinate_histogram": dict(repeated_coordinate_histogram),
        "q2_duplicate_shore_histogram": dict(q2_duplicate_shore_histogram),
        "failure_examples": failure_examples,
        "solutions": solutions,
    }
    print(json.dumps(encode(output), indent=2, sort_keys=True))
    if not solutions:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
