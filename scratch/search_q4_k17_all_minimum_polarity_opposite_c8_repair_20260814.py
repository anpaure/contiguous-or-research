#!/usr/bin/env python3
"""Exhaust opposite-placement C8 repairs of minimum q4 collisions.

Run substantively on H100 only.  The two prescribed bad-window cuts occupy
opposite positions in the old four-edge matching; two arbitrary
same-polarity rail cuts fill the other positions.  Every orientation is
tested, with exact lower+upper q1 equality, active q1/q2 simplicity, and
three-support residence required.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import sys
from collections import Counter
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

    for target_left in adjacent.target_cuts(rail_map, bank, providers[0]):
        for target_right in adjacent.target_cuts(rail_map, bank, providers[1]):
            if set(target_left) & set(target_right):
                continue
            auxiliary = active_edges - {target_left, target_right}
            oriented_auxiliary = adjacent.oriented_edges(auxiliary)
            for left in (tuple(target_left), tuple(reversed(tuple(target_left)))):
                a0, b0 = left
                for right in (tuple(target_right), tuple(reversed(tuple(target_right)))):
                    a2, b2 = right
                    used_target = {a0, b0, a2, b2}
                    if len(used_target) != 4:
                        continue
                    for aux1_edge, aux1 in oriented_auxiliary:
                        a1, b1 = aux1
                        if a1 in used_target or b1 in used_target or a1 == b1:
                            continue
                        if not johnson(b0, a1) or not johnson(b1, a2):
                            continue
                        used = used_target | {a1, b1}
                        for aux3_edge, aux3 in oriented_auxiliary:
                            if aux3_edge == aux1_edge:
                                continue
                            a3, b3 = aux3
                            if a3 in used or b3 in used or a3 == b3:
                                continue
                            if not johnson(b2, a3) or not johnson(b3, a0):
                                continue
                            counters["cross_johnson_c8"] += 1
                            cuts = (target_left, aux1_edge, target_right, aux3_edge)
                            new = (
                                c8.edge(b0, a1), c8.edge(b1, a2),
                                c8.edge(b2, a3), c8.edge(b3, a0),
                            )
                            if not c8.exact_q1(cuts, new, (0,)):
                                continue
                            counters["lower_q1_exact"] += 1
                            if not c8.exact_q1(cuts, new, (1,)):
                                continue
                            counters["both_q1_exact"] += 1
                            after_edges = (old_edges - set(cuts)) | set(new)
                            if len(after_edges) != 146:
                                continue
                            cycles = c8.graph_cycles(after_edges)
                            banks, residence = c8.active_banks(cycles, upper_owners)
                            if not c8.simple(banks):
                                counters["active_bank_collision"] += 1
                                continue
                            counters["active_banks_simple"] += 1
                            if min(residence) < 6:
                                counters["residence_failure"] += 1
                                continue
                            counters["resident"] += 1
                            return {
                                "bank": bank,
                                "collision_resource": collision_resource,
                                "collision_providers": providers,
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
            "opposite in a C8; two same-polarity auxiliary cuts; exact lower+upper q1"
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
