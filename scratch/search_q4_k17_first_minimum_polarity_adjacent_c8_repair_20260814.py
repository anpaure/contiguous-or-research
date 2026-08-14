#!/usr/bin/env python3
"""Search an adjacent-C8 repair of the first minimum-collision q4 lifts.

Run substantively on H100 only.  For each recoupled state, freeze the first
whole-rail polarity assignment with exactly one active collision.  That
collision is a duplicated lower-q2 window.  Select one of the two edges in
each bad window as the prescribed adjacent C8 cuts, select two further cuts
from lower-polarity rails, and exhaust both cut orientations and auxiliary
orders.  The strong class requires exact lower *and* upper q1 equality, as
in the proved adjacent-C8 compiler, before checking the rethreaded active
q1/q2 banks and residence.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import audit_q4_k17_recoupled_typed_rail_ledgers_20260814 as base  # noqa:E402


def edge(a, b):
    return frozenset((a, b))


def q1(item):
    a, b = tuple(item)
    return a & b, a | b


def edge_support(item):
    a, b = tuple(item)
    return a ^ b


def cycle_edges(owners):
    return [edge(owners[i], owners[(i + 1) % len(owners)]) for i in range(len(owners))]


def exact_q1(old, new, shores=(0, 1)):
    return all(Counter(q1(item)[s] for item in old) == Counter(q1(item)[s] for item in new) for s in shores)


def graph_cycles(edges):
    adjacency = defaultdict(set)
    for item in edges:
        a, b = tuple(item)
        adjacency[a].add(b)
        adjacency[b].add(a)
    assert all(len(neighbors) == 2 for neighbors in adjacency.values())
    unseen = set(adjacency)
    cycles = []
    while unseen:
        start = next(iter(unseen))
        cycle = [start]
        previous = None
        current = start
        while True:
            following = next(value for value in adjacency[current] if value != previous)
            if following == start:
                break
            assert following not in cycle
            cycle.append(following)
            previous, current = current, following
        unseen -= set(cycle)
        cycles.append(cycle)
    return cycles


def active_banks(cycles, upper_owners):
    banks = {name: [] for name in ("lower_q1", "upper_q1", "lower_q2", "upper_q2")}
    residence = []
    for cycle in cycles:
        upper = cycle[0] in upper_owners
        assert all((owner in upper_owners) == upper for owner in cycle)
        n = len(cycle)
        supports = [cycle[i] ^ cycle[(i + 1) % n] for i in range(n)]
        residence.extend(len(supports[i] | supports[(i + 1) % n] | supports[(i + 2) % n]) for i in range(n))
        if upper:
            banks["upper_q1"].extend(cycle[i] | cycle[(i + 1) % n] for i in range(n))
            banks["upper_q2"].extend(
                cycle[i] | cycle[(i + 1) % n] | cycle[(i + 2) % n] for i in range(n)
            )
        else:
            banks["lower_q1"].extend(cycle[i] & cycle[(i + 1) % n] for i in range(n))
            banks["lower_q2"].extend(
                cycle[i] & cycle[(i + 1) % n] & cycle[(i + 2) % n] for i in range(n)
            )
    return banks, residence


def simple(banks):
    return all(len(values) == len(set(values)) for values in banks.values())


def counter_delta(after, before):
    value = Counter(after)
    value.subtract(before)
    return {resource: coefficient for resource, coefficient in value.items() if coefficient}


def encode_set(value):
    return "".join("1" if i in value else "0" for i in range(17))


def encode(value):
    if isinstance(value, frozenset):
        if all(isinstance(item, int) for item in value):
            return encode_set(value)
        return sorted(encode(item) for item in value)
    if isinstance(value, (tuple, list, set)):
        return [encode(item) for item in value]
    if isinstance(value, dict):
        return {str(key): encode(item) for key, item in value.items()}
    return value


def first_minimum_assignment(core_report):
    row = core_report["first_minimum_assignment"]
    assert row["collision_excess"] == {
        "lower_q1": 0, "lower_q2": 1, "upper_q1": 0, "upper_q2": 0
    }
    return set(row["lower_rails"]), set(row["upper_rails"])


def sole_collision(rails, lower_names):
    by_rail, _ = base.occurrences(rails)
    providers = defaultdict(list)
    for name in lower_names:
        for index, value in enumerate(by_rail[name]["lower_q2"]):
            providers[value].append((name, index))
    collisions = [(resource, where) for resource, where in providers.items() if len(where) > 1]
    assert len(collisions) == 1 and len(collisions[0][1]) == 2
    return collisions[0]


def search_state(state_name, rails, core_report):
    lower_names, upper_names = first_minimum_assignment(core_report)
    rail_map = dict(rails)
    old_edges = set().union(*(set(cycle_edges(owners)) for _, owners in rails))
    assert len(old_edges) == 146
    lower_edges = set().union(*(set(cycle_edges(rail_map[name])) for name in lower_names))
    upper_owners = set().union(*(set(rail_map[name]) for name in upper_names))
    before_cycles = graph_cycles(old_edges)
    before_banks, before_residence = active_banks(before_cycles, upper_owners)
    assert sum(len(values) - len(set(values)) for values in before_banks.values()) == 1
    collision_resource, providers = sole_collision(rails, lower_names)
    target_menus = []
    for name, index in providers:
        owners = rail_map[name]
        target_menus.append((
            edge(owners[index], owners[(index + 1) % len(owners)]),
            edge(owners[(index + 1) % len(owners)], owners[(index + 2) % len(owners)]),
        ))

    counters = Counter()
    solution = None
    for target_left in target_menus[0]:
        for target_right in target_menus[1]:
            if set(target_left) & set(target_right):
                continue
            for aux_left, aux_right in itertools.permutations(lower_edges - {target_left, target_right}, 2):
                cuts = (target_left, target_right, aux_left, aux_right)
                owner_list = [owner for item in cuts for owner in item]
                if len(owner_list) != len(set(owner_list)):
                    continue
                counters["owner_disjoint_cut_quadruples"] += 1
                endpoint_orders = [tuple(item) for item in cuts]
                for flips in itertools.product((0, 1), repeat=4):
                    counters["oriented_cut_quadruples"] += 1
                    oriented = [
                        endpoints if not flip else tuple(reversed(endpoints))
                        for endpoints, flip in zip(endpoint_orders, flips)
                    ]
                    a = [item[0] for item in oriented]
                    b = [item[1] for item in oriented]
                    new = tuple(edge(b[i], a[(i + 1) % 4]) for i in range(4))
                    if any(len(item) != 2 or len(edge_support(item)) != 2 for item in new):
                        continue
                    counters["cross_johnson"] += 1
                    if not exact_q1(cuts, new, (0,)):
                        continue
                    counters["lower_q1_exact"] += 1
                    if not exact_q1(cuts, new, (1,)):
                        continue
                    counters["both_q1_exact"] += 1
                    after_edges = (old_edges - set(cuts)) | set(new)
                    if len(after_edges) != 146:
                        continue
                    cycles = graph_cycles(after_edges)
                    banks, residence = active_banks(cycles, upper_owners)
                    if not simple(banks):
                        counters["active_bank_collision"] += 1
                        continue
                    counters["active_banks_simple"] += 1
                    if min(residence) < 6:
                        counters["residence_failure"] += 1
                        continue
                    counters["resident"] += 1
                    solution = {
                        "lower_rails": sorted(lower_names),
                        "upper_rails": sorted(upper_names),
                        "collision_resource": collision_resource,
                        "collision_providers": providers,
                        "old_cuts": cuts,
                        "new_edges": new,
                        "component_lengths_before": sorted(map(len, before_cycles)),
                        "component_lengths_after": sorted(map(len, cycles)),
                        "minimum_three_support_union_before": min(before_residence),
                        "minimum_three_support_union_after": min(residence),
                        "q1_lower_delta": counter_delta(banks["lower_q1"], before_banks["lower_q1"]),
                        "q1_upper_delta": counter_delta(banks["upper_q1"], before_banks["upper_q1"]),
                        "q2_lower_delta": counter_delta(banks["lower_q2"], before_banks["lower_q2"]),
                        "q2_upper_delta": counter_delta(banks["upper_q2"], before_banks["upper_q2"]),
                    }
                    break
                if solution:
                    break
            if solution:
                break
        if solution:
            break
    return {
        "state": state_name,
        "status": "PASS" if solution else "NO_WITNESS",
        "class": (
            "four owner-disjoint cuts from lower-polarity components, one cut in each "
            "bad q2 window, adjacent alternating C8, exact lower+upper q1"
        ),
        "counters": dict(counters),
        "solution": solution,
    }


def main():
    source_raw = Path(sys.argv[1]).read_bytes()
    core_raw = Path(sys.argv[2]).read_bytes()
    core = json.loads(core_raw)
    states = base.rail_states()
    assert [report["state"] for report in core["reports"]] == [name for name, _ in states]
    reports = [
        search_state(name, rails, report)
        for (name, rails), report in zip(states, core["reports"])
    ]
    print(json.dumps(encode({
        "status": "PASS" if all(report["status"] == "PASS" for report in reports) else "PARTIAL",
        "source_sha256": hashlib.sha256(source_raw).hexdigest(),
        "core_sha256": hashlib.sha256(core_raw).hexdigest(),
        "reports": reports,
    }), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
