#!/usr/bin/env python3
"""Exhaust adjacent-C8 repairs over all minimum q4 polarity assignments.

Run substantively on H100 only.  The search visits every whole-rail polarity
assignment with the minimum active collision excess one.  A q1 collision is
an immediate interface obstruction because the C8 compiler preserves the
q1 occurrence Counter.  For a q2 collision, each incident edge of its two
three-owner windows is tried as a prescribed cut; two further same-polarity
cuts are enumerated with all orientations.  Only the strong adjacent-C8
class with exact lower and upper q1 equality is accepted.
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
import search_q4_k17_first_minimum_polarity_adjacent_c8_repair_20260814 as c8  # noqa:E402


def johnson(a, b):
    return len(a ^ b) == 2


def active_collisions(names, by_rail, bits):
    answer = []
    for bank, wants_upper in (
        ("lower_q1", False), ("lower_q2", False),
        ("upper_q1", True), ("upper_q2", True),
    ):
        providers = defaultdict(list)
        for name, upper in zip(names, bits):
            if upper != wants_upper:
                continue
            for index, resource in enumerate(by_rail[name][bank]):
                providers[resource].append((name, index))
        answer.extend(
            (bank, resource, where)
            for resource, where in providers.items() if len(where) > 1
        )
    return answer


def target_cuts(rail_map, bank, provider):
    name, index = provider
    owners = rail_map[name]
    n = len(owners)
    if bank.endswith("q1"):
        return (c8.edge(owners[index], owners[(index + 1) % n]),)
    return (
        c8.edge(owners[index], owners[(index + 1) % n]),
        c8.edge(owners[(index + 1) % n], owners[(index + 2) % n]),
    )


def oriented_edges(edges):
    return [
        (item, endpoints)
        for item in edges
        for endpoints in (tuple(item), tuple(reversed(tuple(item))))
    ]


def try_assignment(rails, names, bits, collision, counters):
    bank, collision_resource, providers = collision
    if bank.endswith("q1"):
        counters["q1_collision_assignments_interface_impossible"] += 1
        return None
    assert len(providers) == 2
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

    target_left_menu = target_cuts(rail_map, bank, providers[0])
    target_right_menu = target_cuts(rail_map, bank, providers[1])
    for target_left in target_left_menu:
        for target_right in target_right_menu:
            if set(target_left) & set(target_right):
                continue
            target_orientations = []
            for left in (tuple(target_left), tuple(reversed(tuple(target_left)))):
                for right in (tuple(target_right), tuple(reversed(tuple(target_right)))):
                    if johnson(left[1], right[0]):
                        target_orientations.append((left, right))
            if not target_orientations:
                counters["target_cut_pairs_without_direct_johnson"] += 1
                continue
            counters["target_cut_pairs_with_direct_johnson"] += 1
            auxiliary = active_edges - {target_left, target_right}
            oriented_auxiliary = oriented_edges(auxiliary)
            for left, right in target_orientations:
                a0, b0 = left
                a1, b1 = right
                for aux2_edge, aux2 in oriented_auxiliary:
                    a2, b2 = aux2
                    if not johnson(b1, a2):
                        continue
                    used = {a0, b0, a1, b1, a2, b2}
                    if len(used) != 6:
                        continue
                    for aux3_edge, aux3 in oriented_auxiliary:
                        if aux3_edge == aux2_edge:
                            continue
                        a3, b3 = aux3
                        if a3 in used or b3 in used or a3 == b3:
                            continue
                        if not johnson(b2, a3) or not johnson(b3, a0):
                            continue
                        counters["cross_johnson_c8"] += 1
                        cuts = (target_left, target_right, aux2_edge, aux3_edge)
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
    collision_types = Counter()
    solution = None
    for bits in itertools.product((False, True), repeat=len(names)):
        scores = core.active_collision_score(names, by_rail, bits)
        if sum(scores.values()) != 1:
            continue
        counters["minimum_assignments"] += 1
        collisions = active_collisions(names, by_rail, bits)
        assert len(collisions) == 1 and len(collisions[0][2]) == 2
        bank, resource, providers = collisions[0]
        collision_types[(bank, base.encode_set(resource), tuple(providers))] += 1
        candidate = try_assignment(rails, names, bits, collisions[0], counters)
        if candidate is not None:
            solution = candidate
            break
    return {
        "state": state_name,
        "status": "PASS" if solution else "NO_WITNESS",
        "class": (
            "all minimum-excess whole-rail polarities; prescribed bad-window cuts; "
            "two further same-polarity cuts; adjacent C8; exact lower+upper q1"
        ),
        "collision_type_histogram": [
            {"bank": key[0], "resource": key[1], "providers": key[2], "assignments": value}
            for key, value in sorted(collision_types.items())
        ],
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
