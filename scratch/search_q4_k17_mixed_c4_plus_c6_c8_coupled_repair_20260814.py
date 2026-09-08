#!/usr/bin/env python3
"""Exhaust an owner-disjoint mixed-C4 plus C6/C8 q4 repair.

Run substantively on H100 only.  For every minimum pure-rail polarity
assignment, enumerate every exact mixed-C4 unit move touching its sole
collision.  Independently enumerate all alternating C6 and C8 switches on
one polarity.  Join a pair only when their complete lower+upper q1 currents
cancel exactly and their owner sets are disjoint.  The final factor must
have simple active q1/q2 decks and three-support residence at least six.
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
import search_q4_k17_all_minimum_polarity_adjacent_c8_repair_20260814 as all_c8  # noqa:E402
import search_q4_k17_all_minimum_polarity_mixed_c4_repair_20260814 as mixed  # noqa:E402
import search_q4_k17_first_minimum_polarity_adjacent_c8_repair_20260814 as c8  # noqa:E402


def resource_int(value):
    return sum(1 << x for x in value)


def q1_current(old, new):
    answer = []
    for shore in (0, 1):
        delta = Counter(c8.q1(item)[shore] for item in new)
        delta.subtract(c8.q1(item)[shore] for item in old)
        answer.append({resource: coefficient for resource, coefficient in delta.items() if coefficient})
    return tuple(answer)


def current_key(current):
    return tuple(
        tuple(sorted((resource_int(resource), coefficient) for resource, coefficient in shore.items()))
        for shore in current
    )


def inverse_key(current):
    return tuple(
        tuple(sorted((resource_int(resource), -coefficient) for resource, coefficient in shore.items()))
        for shore in current
    )


def johnson(a, b):
    return len(a ^ b) == 2


def alternating_switches(edges, length, counters):
    """All unoriented length-`length` alternating matching switches."""
    oriented = all_c8.oriented_edges(edges)
    successors = defaultdict(list)
    for previous in oriented:
        b = previous[1][1]
        for following in oriented:
            if previous[0] != following[0] and johnson(b, following[1][0]):
                successors[previous].append(following)
    seen = set()
    result = []
    for start in oriented:
        a0 = start[1][0]

        def dfs(path):
            if len(path) == length:
                if not johnson(path[-1][1][1], a0):
                    return
                cuts = tuple(item[0] for item in path)
                new = tuple(
                    c8.edge(path[i][1][1], path[(i + 1) % length][1][0])
                    for i in range(length)
                )
                key = (frozenset(cuts), frozenset(new))
                if key in seen or len(set(cuts)) != length or len(set(new)) != length:
                    return
                seen.add(key)
                counters[f"raw_c{2*length}_switches"] += 1
                current = q1_current(cuts, new)
                # Only unit-by-unit currents can cancel the mixed C4.
                if any(
                    sum(value for value in shore.values() if value > 0) != 1
                    or -sum(value for value in shore.values() if value < 0) != 1
                    or max(map(abs, shore.values()), default=0) != 1
                    for shore in current
                ):
                    return
                counters[f"unit_c{2*length}_switches"] += 1
                result.append({
                    "cuts": cuts,
                    "new": new,
                    "owners": set().union(*(set(item) for item in cuts)),
                    "current": current,
                })
                return
            used_edges = {item[0] for item in path}
            used_owners = {owner for item in path for owner in item[0]}
            for following in successors[path[-1]]:
                if following[0] in used_edges or set(following[0]) & used_owners:
                    continue
                dfs(path + [following])

        dfs([start])
    return result


def mixed_c4_switches(rails, names, bits, collision, counters):
    bank, _, providers = collision
    upper = bank.startswith("upper")
    rail_map = dict(rails)
    active_names = {name for name, bit in zip(names, bits) if bit == upper}
    active_edges = set().union(*(set(c8.cycle_edges(rail_map[name])) for name in active_names))
    seen = set()
    result = []
    for target in mixed.target_edges(rail_map, bank, providers):
        for other in active_edges - {target}:
            if set(target) & set(other):
                continue
            for first in (tuple(target), tuple(reversed(tuple(target)))):
                for second in (tuple(other), tuple(reversed(tuple(other)))):
                    a0, b0 = first
                    a1, b1 = second
                    new = (c8.edge(b0, a1), c8.edge(b1, a0))
                    if any(len(item) != 2 or len(c8.edge_support(item)) != 2 for item in new):
                        continue
                    lower_unit, _ = mixed.unit_current((target, other), new, 0)
                    upper_unit, _ = mixed.unit_current((target, other), new, 1)
                    if not lower_unit or not upper_unit:
                        continue
                    key = (frozenset((target, other)), frozenset(new))
                    if key in seen:
                        continue
                    seen.add(key)
                    current = q1_current((target, other), new)
                    counters["mixed_c4_switches"] += 1
                    result.append({
                        "cuts": (target, other),
                        "new": new,
                        "owners": set(target) | set(other),
                        "current": current,
                    })
    return result


def encode_set(value):
    return "".join("1" if i in value else "0" for i in range(17))


def encode(value):
    if isinstance(value, frozenset):
        if all(isinstance(item, int) for item in value):
            return encode_set(value)
        return sorted(encode(item) for item in value)
    if isinstance(value, set):
        return sorted(encode(item) for item in value)
    if isinstance(value, (tuple, list)):
        return [encode(item) for item in value]
    if isinstance(value, dict):
        return {
            encode_set(key) if isinstance(key, frozenset) else str(key): encode(item)
            for key, item in value.items()
        }
    return value


def try_pair(rails, names, bits, collision, first, second, second_length):
    if first["owners"] & second["owners"]:
        return None
    rail_map = dict(rails)
    upper_names = {name for name, bit in zip(names, bits) if bit}
    upper_owners = set().union(*(set(rail_map[name]) for name in upper_names)) if upper_names else set()
    old_edges = set().union(*(set(c8.cycle_edges(owners)) for _, owners in rails))
    before_cycles = c8.graph_cycles(old_edges)
    before_banks, before_residence = c8.active_banks(before_cycles, upper_owners)
    after_edges = (
        old_edges - set(first["cuts"]) - set(second["cuts"])
    ) | set(first["new"]) | set(second["new"])
    if len(after_edges) != 146:
        return None
    cycles = c8.graph_cycles(after_edges)
    banks, residence = c8.active_banks(cycles, upper_owners)
    if not c8.simple(banks) or min(residence) < 6:
        return None
    return {
        "source_collision_bank": collision[0],
        "source_collision_resource": collision[1],
        "source_collision_providers": collision[2],
        "lower_rails": sorted(name for name, bit in zip(names, bits) if not bit),
        "upper_rails": sorted(name for name, bit in zip(names, bits) if bit),
        "second_switch": f"C{2*second_length}",
        "c4_old_cuts": first["cuts"],
        "c4_new_edges": first["new"],
        "second_old_cuts": second["cuts"],
        "second_new_edges": second["new"],
        "aggregate_lower_q1_current": {},
        "aggregate_upper_q1_current": {},
        "component_lengths_before": sorted(map(len, before_cycles)),
        "component_lengths_after": sorted(map(len, cycles)),
        "minimum_three_support_union_before": min(before_residence),
        "minimum_three_support_union_after": min(residence),
        "active_lower_q1_delta": c8.counter_delta(banks["lower_q1"], before_banks["lower_q1"]),
        "active_upper_q1_delta": c8.counter_delta(banks["upper_q1"], before_banks["upper_q1"]),
        "active_lower_q2_delta": c8.counter_delta(banks["lower_q2"], before_banks["lower_q2"]),
        "active_upper_q2_delta": c8.counter_delta(banks["upper_q2"], before_banks["upper_q2"]),
    }


def search_state(state_name, rails):
    by_rail, _ = base.occurrences(rails)
    names = [name for name, _ in rails]
    rail_map = dict(rails)
    counters = Counter()
    solution = None
    for bits in itertools.product((False, True), repeat=len(names)):
        scores = core.active_collision_score(names, by_rail, bits)
        if sum(scores.values()) != 1:
            continue
        counters["minimum_assignments"] += 1
        collisions = all_c8.active_collisions(names, by_rail, bits)
        assert len(collisions) == 1 and len(collisions[0][2]) == 2
        first_switches = mixed_c4_switches(rails, names, bits, collisions[0], counters)
        if not first_switches:
            continue
        lower_names = {name for name, bit in zip(names, bits) if not bit}
        upper_names = set(names) - lower_names
        second_switches = []
        for polarity_names in (lower_names, upper_names):
            polarity_edges = set().union(*(set(c8.cycle_edges(rail_map[name])) for name in polarity_names))
            for length in (3, 4):
                for item in alternating_switches(polarity_edges, length, counters):
                    item["length"] = length
                    second_switches.append(item)
        by_current = defaultdict(list)
        for item in second_switches:
            by_current[current_key(item["current"])].append(item)
        counters["second_switches"] += len(second_switches)
        for first in first_switches:
            matches = by_current.get(inverse_key(first["current"]), ())
            counters["q1_canceling_pairs"] += len(matches)
            for second in matches:
                if first["owners"] & second["owners"]:
                    counters["owner_overlap_pairs"] += 1
                    continue
                counters["owner_disjoint_q1_canceling_pairs"] += 1
                solution = try_pair(
                    rails, names, bits, collisions[0], first, second, second["length"]
                )
                if solution:
                    counters["typed_simple_resident_pairs"] += 1
                    break
            if solution:
                break
        if solution:
            break
    return {
        "state": state_name,
        "status": "PASS" if solution else "NO_WITNESS",
        "class": (
            "every minimum pure-rail polarity; every collision-touching mixed C4; "
            "one owner-disjoint same-polarity alternating C6 or C8 with inverse "
            "lower+upper q1 current"
        ),
        "counters": dict(counters),
        "solution": solution,
    }


def main():
    source_raw = Path(sys.argv[1]).read_bytes()
    reports = [search_state(name, rails) for name, rails in base.rail_states()]
    print(json.dumps(encode({
        "status": "PASS" if all(report["status"] == "PASS" for report in reports) else "NO_WITNESS",
        "source_sha256": hashlib.sha256(source_raw).hexdigest(),
        "reports": reports,
    }), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
