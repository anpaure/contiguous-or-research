#!/usr/bin/env python3
"""Search the exact mixed-C4 unit-current repair of q4 typed collisions.

Run substantively on H100 only.  Every minimum whole-rail polarity
assignment is considered.  One old cut must touch a provider window of the
sole q1/q2 collision; the second may be any same-polarity rail edge.  Both
cross matchings are exhausted.  A candidate must be a legal owner C4 whose
lower and upper q1 currents are both elementary units, then make all active
q1/q2 banks simple and preserve the three-support residence collar.
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
import search_q4_k17_all_minimum_polarity_adjacent_c8_repair_20260814 as all_c8  # noqa:E402
import search_q4_k17_first_minimum_polarity_adjacent_c8_repair_20260814 as c8  # noqa:E402


def unit_current(old, new, shore):
    delta = Counter(c8.q1(item)[shore] for item in new)
    delta.subtract(c8.q1(item)[shore] for item in old)
    nonzero = {resource: value for resource, value in delta.items() if value}
    return (
        sum(value for value in nonzero.values() if value > 0) == 1
        and -sum(value for value in nonzero.values() if value < 0) == 1
        and max(map(abs, nonzero.values()), default=0) == 1
    ), nonzero


def target_edges(rail_map, bank, providers):
    result = set()
    for provider in providers:
        result.update(all_c8.target_cuts(rail_map, bank, provider))
    return result


def collision_summary(banks):
    result = []
    for bank, values in banks.items():
        providers = Counter(values)
        for resource, multiplicity in providers.items():
            if multiplicity > 1:
                result.append((bank, resource, multiplicity))
    return result


def try_assignment(rails, names, bits, collision, counters, best_near):
    bank, collision_resource, providers = collision
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

    for target in target_edges(rail_map, bank, providers):
        for other in active_edges - {target}:
            if set(target) & set(other):
                continue
            counters["owner_disjoint_edge_pairs"] += 1
            for first in (tuple(target), tuple(reversed(tuple(target)))):
                for second in (tuple(other), tuple(reversed(tuple(other)))):
                    a0, b0 = first
                    a1, b1 = second
                    new = (c8.edge(b0, a1), c8.edge(b1, a0))
                    if any(len(item) != 2 or len(c8.edge_support(item)) != 2 for item in new):
                        continue
                    counters["cross_johnson_c4"] += 1
                    lower_unit, lower_delta = unit_current((target, other), new, 0)
                    upper_unit, upper_delta = unit_current((target, other), new, 1)
                    if not lower_unit or not upper_unit:
                        continue
                    counters["mixed_unit_c4"] += 1
                    after_edges = (old_edges - {target, other}) | set(new)
                    if len(after_edges) != 146:
                        continue
                    cycles = c8.graph_cycles(after_edges)
                    banks, residence = c8.active_banks(cycles, upper_owners)
                    if not c8.simple(banks):
                        counters["active_bank_collision"] += 1
                        collisions = collision_summary(banks)
                        excess = sum(multiplicity - 1 for _, _, multiplicity in collisions)
                        counters[f"post_active_excess_{excess}"] += 1
                        if best_near[0] is None or excess < best_near[0]:
                            best_near[:] = [excess, {
                                "source_bank": bank,
                                "source_collision_resource": collision_resource,
                                "source_collision_providers": providers,
                                "lower_rails": sorted(name for name, bit in zip(names, bits) if not bit),
                                "upper_rails": sorted(name for name, bit in zip(names, bits) if bit),
                                "old_cuts": (target, other),
                                "new_edges": new,
                                "c4_lower_q1_delta": lower_delta,
                                "c4_upper_q1_delta": upper_delta,
                                "remaining_collisions": collisions,
                                "minimum_three_support_union": min(residence),
                            }]
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
                        "old_cuts": (target, other),
                        "new_edges": new,
                        "c4_lower_q1_delta": lower_delta,
                        "c4_upper_q1_delta": upper_delta,
                        "component_lengths_before": sorted(map(len, before_cycles)),
                        "component_lengths_after": sorted(map(len, cycles)),
                        "minimum_three_support_union_before": min(before_residence),
                        "minimum_three_support_union_after": min(residence),
                        "active_lower_q1_delta": c8.counter_delta(banks["lower_q1"], before_banks["lower_q1"]),
                        "active_upper_q1_delta": c8.counter_delta(banks["upper_q1"], before_banks["upper_q1"]),
                        "active_lower_q2_delta": c8.counter_delta(banks["lower_q2"], before_banks["lower_q2"]),
                        "active_upper_q2_delta": c8.counter_delta(banks["upper_q2"], before_banks["upper_q2"]),
                    }
    return None


def search_state(state_name, rails):
    by_rail, _ = base.occurrences(rails)
    names = [name for name, _ in rails]
    counters = Counter()
    solution = None
    best_near = [None, None]
    for bits in itertools.product((False, True), repeat=len(names)):
        scores = core.active_collision_score(names, by_rail, bits)
        if sum(scores.values()) != 1:
            continue
        counters["minimum_assignments"] += 1
        collisions = all_c8.active_collisions(names, by_rail, bits)
        assert len(collisions) == 1 and len(collisions[0][2]) == 2
        candidate = try_assignment(rails, names, bits, collisions[0], counters, best_near)
        if candidate is not None:
            solution = candidate
            break
    return {
        "state": state_name,
        "status": "PASS" if solution else "NO_WITNESS",
        "class": (
            "all minimum-excess pure-rail polarities; one target-window cut plus one "
            "same-polarity cut; legal mixed C4 with unit lower and upper q1 current"
        ),
        "counters": dict(counters),
        "solution": solution,
        "minimum_post_c4_collision_excess": best_near[0],
        "first_minimum_near_miss": best_near[1],
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
