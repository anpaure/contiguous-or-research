#!/usr/bin/env python3
"""Exhaust five-cut alternating C10 repairs of minimum q4 q2 defects.

Run substantively on H100 only.  Each C10 uses five old same-polarity rail
edges and the cyclic cross matching.  The two prescribed bad-window cuts
are tried at both inequivalent distances in the five-cycle.  A sparse DFS
over oriented old cuts exhausts the other three positions.  Exact lower and
upper q1 equality, active q1/q2 simplicity, and residence are mandatory.
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
import audit_q4_k17_typed_polarity_unsat_core_20260814 as core  # noqa:E402
import search_q4_k17_all_minimum_polarity_adjacent_c8_repair_20260814 as adjacent  # noqa:E402
import search_q4_k17_first_minimum_polarity_adjacent_c8_repair_20260814 as c8  # noqa:E402


def johnson(a, b):
    return len(a ^ b) == 2


def try_assignment(rails, names, bits, collision, counters):
    bank, collision_resource, providers = collision
    if bank.endswith("q1"):
        counters["q1_collision_assignments_interface_impossible"] += 1
        return None
    upper = bank.startswith("upper")
    rail_map = dict(rails)
    active_names = {name for name, bit in zip(names, bits) if bit == upper}
    upper_names = {name for name, bit in zip(names, bits) if bit}
    old_edges = set().union(*(set(c8.cycle_edges(owners)) for _, owners in rails))
    active_edges = set().union(*(set(c8.cycle_edges(rail_map[name])) for name in active_names))
    upper_owners = set().union(*(set(rail_map[name]) for name in upper_names)) if upper_names else set()
    before_cycles = c8.graph_cycles(old_edges)
    before_banks, before_residence = c8.active_banks(before_cycles, upper_owners)
    assert sum(len(values) - len(set(values)) for values in before_banks.values()) == 1

    oriented = adjacent.oriented_edges(active_edges)
    successors = defaultdict(list)
    for item in oriented:
        _, (a, _) = item
        for previous in oriented:
            _, (_, bprev) = previous
            if johnson(bprev, a):
                successors[previous].append(item)

    target_left_states = [
        item for item in oriented
        if item[0] in adjacent.target_cuts(rail_map, bank, providers[0])
    ]
    target_right_states = [
        item for item in oriented
        if item[0] in adjacent.target_cuts(rail_map, bank, providers[1])
    ]
    target_right_set = set((edge_item, endpoints) for edge_item, endpoints in target_right_states)

    for distance in (1, 2):
        for start in target_left_states:
            start_edge, (a0, _) = start

            def dfs(path):
                position = len(path)
                if position == 5:
                    last = path[-1]
                    if not johnson(last[1][1], a0):
                        return None
                    counters["cross_johnson_c10"] += 1
                    cuts = tuple(item[0] for item in path)
                    new = tuple(
                        c8.edge(path[i][1][1], path[(i + 1) % 5][1][0])
                        for i in range(5)
                    )
                    if not c8.exact_q1(cuts, new, (0,)):
                        return None
                    counters["lower_q1_exact"] += 1
                    if not c8.exact_q1(cuts, new, (1,)):
                        return None
                    counters["both_q1_exact"] += 1
                    after_edges = (old_edges - set(cuts)) | set(new)
                    if len(after_edges) != 146:
                        return None
                    cycles = c8.graph_cycles(after_edges)
                    banks, residence = c8.active_banks(cycles, upper_owners)
                    if not c8.simple(banks):
                        counters["active_bank_collision"] += 1
                        return None
                    counters["active_banks_simple"] += 1
                    if min(residence) < 6:
                        counters["residence_failure"] += 1
                        return None
                    counters["resident"] += 1
                    return {
                        "bank": bank,
                        "collision_resource": collision_resource,
                        "collision_providers": providers,
                        "target_distance": distance,
                        "lower_rails": sorted(name for name, bit in zip(names, bits) if not bit),
                        "upper_rails": sorted(name for name, bit in zip(names, bits) if bit),
                        "old_cuts": cuts,
                        "new_edges": new,
                        "component_lengths_before": sorted(map(len, before_cycles)),
                        "component_lengths_after": sorted(map(len, cycles)),
                        "minimum_three_support_union_before": min(before_residence),
                        "minimum_three_support_union_after": min(residence),
                        "q1_lower_delta": c8.counter_delta(banks["lower_q1"], before_banks["lower_q1"]),
                        "q1_upper_delta": c8.counter_delta(banks["upper_q1"], before_banks["upper_q1"]),
                        "q2_lower_delta": c8.counter_delta(banks["lower_q2"], before_banks["lower_q2"]),
                        "q2_upper_delta": c8.counter_delta(banks["upper_q2"], before_banks["upper_q2"]),
                    }

                # Position `distance` is the second prescribed cut.  No
                # other position may use either prescribed family.
                if position == distance:
                    candidates = target_right_states
                else:
                    candidates = successors[path[-1]]
                used_edges = {item[0] for item in path}
                used_owners = {owner for item in path for owner in item[0]}
                for candidate in candidates:
                    if candidate not in successors[path[-1]]:
                        continue
                    edge_item, endpoints = candidate
                    if edge_item in used_edges:
                        continue
                    if set(edge_item) & used_owners:
                        continue
                    if position != distance and candidate in target_right_set:
                        continue
                    answer = dfs(path + [candidate])
                    if answer is not None:
                        return answer
                return None

            answer = dfs([start])
            if answer is not None:
                return answer
    return None


def search_state(state_name, rails):
    by_rail, _ = base.occurrences(rails)
    names = [name for name, _ in rails]
    counters = Counter()
    solution = None
    for bits in itertools.product((False, True), repeat=len(names)):
        scores = core.active_collision_score(names, by_rail, bits)
        if sum(scores.values()) != 1:
            continue
        counters["minimum_assignments"] += 1
        collisions = adjacent.active_collisions(names, by_rail, bits)
        assert len(collisions) == 1 and len(collisions[0][2]) == 2
        solution = try_assignment(rails, names, bits, collisions[0], counters)
        if solution:
            break
    return {
        "state": state_name,
        "status": "PASS" if solution else "NO_WITNESS",
        "class": (
            "all minimum-excess pure-rail polarities; two prescribed bad-window cuts "
            "at C10 distance one or two; three same-polarity cuts; exact lower+upper q1"
        ),
        "counters": dict(counters),
        "solution": solution,
    }


def main():
    source_raw = Path(sys.argv[1]).read_bytes()
    reports = [search_state(name, rails) for name, rails in base.rail_states()]
    print(json.dumps(c8.encode({
        "status": "PASS" if all(report["status"] == "PASS" for report in reports) else "NO_WITNESS",
        "source_sha256": hashlib.sha256(source_raw).hexdigest(),
        "reports": reports,
    }), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
