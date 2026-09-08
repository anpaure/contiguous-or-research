#!/usr/bin/env python3
"""Search the smallest two-copy cross-C4 repair of the q4 typed reserve.

Run substantively on H100 only.  The second reserve copy is relabelled by
the same affine map x -> a*x+b in both recoupled states.  We retain only
maps whose owner banks are disjoint in both states.  Each copy uses a
minimum-excess whole-rail polarity assignment, their active typed resource
banks must have no cross-copy collision, and one old cut from each copy
must touch its sole collision.  The two cuts are recoupled by a legal mixed
C4.  Acceptance requires unit lower and upper q1 current, final active
q1/q2 simplicity, and three-support residence at least six.
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

BANKS = ("lower_q1", "upper_q1", "lower_q2", "upper_q2")


def relabel(value, a, b):
    return frozenset((a * item + b) % 17 for item in value)


def relabel_rails(rails, a, b):
    return [(name, [relabel(owner, a, b) for owner in cycle]) for name, cycle in rails]


def owner_bank(rails):
    return {owner for _, cycle in rails for owner in cycle}


def bitword(bits):
    return "".join("1" if bit else "0" for bit in bits)


def records(rails):
    by_rail, _ = base.occurrences(rails)
    names = [name for name, _ in rails]
    answer = []
    for bits in itertools.product((False, True), repeat=len(names)):
        if sum(core.active_collision_score(names, by_rail, bits).values()) != 1:
            continue
        active = {bank: [] for bank in BANKS}
        for name, upper in zip(names, bits):
            for suffix in ("q1", "q2"):
                bank = ("upper_" if upper else "lower_") + suffix
                active[bank].extend(by_rail[name][bank])
        collisions = all_c8.active_collisions(names, by_rail, bits)
        assert len(collisions) == 1 and len(collisions[0][2]) == 2
        answer.append({
            "bits": bits,
            "sets": tuple(frozenset(active[bank]) for bank in BANKS),
            "collision": collisions[0],
        })
    return answer


def translate_record(item, a, b):
    bank, resource, providers = item["collision"]
    return {
        "bits": item["bits"],
        "sets": tuple(
            frozenset(relabel(resource, a, b) for resource in values)
            for values in item["sets"]
        ),
        "collision": (bank, relabel(resource, a, b), providers),
    }


def collision_cuts(rail_map, collision):
    bank, _, providers = collision
    return set().union(*(set(all_c8.target_cuts(rail_map, bank, provider)) for provider in providers))


def encode_delta(delta):
    return {base.encode_set(resource): value for resource, value in delta.items()}


def collision_key(collision):
    return collision[0], collision[1], tuple(collision[2])


def cross_c4_candidates(left_map, right_map, left_collision, right_collision, counters):
    answer = []
    seen_global = set()
    for cut_left in collision_cuts(left_map, left_collision):
        for cut_right in collision_cuts(right_map, right_collision):
            assert set(cut_left).isdisjoint(cut_right)
            counters["collision_type_target_cut_pairs"] += 1
            for first in (tuple(cut_left), tuple(reversed(tuple(cut_left)))):
                for second in (tuple(cut_right), tuple(reversed(tuple(cut_right)))):
                    new = (c8.edge(first[1], second[0]), c8.edge(second[1], first[0]))
                    key = (frozenset((cut_left, cut_right)), frozenset(new))
                    if key in seen_global:
                        continue
                    seen_global.add(key)
                    if len(key[1]) != 2 or any(len(c8.edge_support(item)) != 2 for item in new):
                        continue
                    counters["collision_type_cross_johnson_c4"] += 1
                    lower_unit, lower_delta = mixed.unit_current(
                        (cut_left, cut_right), new, 0
                    )
                    upper_unit, upper_delta = mixed.unit_current(
                        (cut_left, cut_right), new, 1
                    )
                    if not lower_unit or not upper_unit:
                        continue
                    counters["collision_type_mixed_unit_c4"] += 1
                    answer.append((cut_left, cut_right, new, lower_delta, upper_delta))
    return answer


def search_state(state_name, rails, left_records, a, b, counters):
    shifted = relabel_rails(rails, a, b)
    left_map = dict(rails)
    right_map = dict(shifted)
    old_edges = set().union(*(set(c8.cycle_edges(cycle)) for _, cycle in rails + shifted))
    assert len(old_edges) == 292
    right_records = [translate_record(item, a, b) for item in left_records]
    names = [name for name, _ in rails]
    left_groups = defaultdict(list)
    right_groups = defaultdict(list)
    for item in left_records:
        left_groups[collision_key(item["collision"])].append(item)
    for item in right_records:
        right_groups[collision_key(item["collision"])].append(item)
    counters["assignment_pairs"] = len(left_records) * len(right_records)
    for left_key, left_group in left_groups.items():
        left_bank = left_key[0]
        for right_key, right_group in right_groups.items():
            pair_count = len(left_group) * len(right_group)
            right_bank = right_key[0]
            if left_bank.startswith("upper") != right_bank.startswith("upper"):
                counters["opposite_polarity_collision_pairs"] += pair_count
                continue
            candidates = cross_c4_candidates(
                left_map, right_map, left_group[0]["collision"],
                right_group[0]["collision"], counters
            )
            if not candidates:
                counters["collision_type_pairs_without_mixed_unit_c4"] += 1
                continue
            counters["collision_type_pairs_with_mixed_unit_c4"] += 1
            for left in left_group:
                for right in right_group:
                    if any(x & y for x, y in zip(left["sets"], right["sets"])):
                        counters["cross_resource_collision_pairs"] += 1
                        continue
                    counters["resource_disjoint_assignment_pairs"] += 1
                    for cut_left, cut_right, new, lower_delta, upper_delta in candidates:
                        counters["mixed_unit_c4_assignment_trials"] += 1
                        upper_owners = set()
                        for name, bit in zip(names, left["bits"]):
                            if bit:
                                upper_owners.update(left_map[name])
                        for name, bit in zip(names, right["bits"]):
                            if bit:
                                upper_owners.update(right_map[name])
                        before_cycles = c8.graph_cycles(old_edges)
                        before_banks, before_residence = c8.active_banks(
                            before_cycles, upper_owners
                        )
                        assert sum(
                            len(values) - len(set(values))
                            for values in before_banks.values()
                        ) == 2
                        after_edges = (old_edges - {cut_left, cut_right}) | set(new)
                        if len(after_edges) != 292:
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
                            "state": state_name,
                            "left_bits": bitword(left["bits"]),
                            "right_bits": bitword(right["bits"]),
                            "left_collision": left["collision"],
                            "right_collision": right["collision"],
                            "old_cuts": (cut_left, cut_right),
                            "new_edges": new,
                            "lower_q1_current": encode_delta(lower_delta),
                            "upper_q1_current": encode_delta(upper_delta),
                            "components_before": sorted(map(len, before_cycles)),
                            "components_after": sorted(map(len, cycles)),
                            "minimum_three_support_union_before": min(before_residence),
                            "minimum_three_support_union_after": min(residence),
                            "final_bank_sizes": {bank: len(values) for bank, values in banks.items()},
                        }
    return None


def encode(value):
    if isinstance(value, frozenset):
        if all(isinstance(item, int) for item in value):
            return base.encode_set(value)
        return sorted(encode(item) for item in value)
    if isinstance(value, (tuple, list, set)):
        return [encode(item) for item in value]
    if isinstance(value, dict):
        return {str(key): encode(item) for key, item in value.items()}
    return value


def main():
    source_raw = Path(sys.argv[1]).read_bytes()
    states = dict(base.rail_states())
    state_records = {name: records(rails) for name, rails in states.items()}
    maps = []
    for a in range(1, 17):
        for b in range(17):
            if all(
                owner_bank(rails).isdisjoint(owner_bank(relabel_rails(rails, a, b)))
                for rails in states.values()
            ):
                maps.append((a, b))
    map_reports = []
    solution = None
    for a, b in maps:
        state_solutions = {}
        state_counters = {}
        for state_name, rails in states.items():
            counters = Counter()
            state_solutions[state_name] = search_state(
                state_name, rails, state_records[state_name], a, b, counters
            )
            state_counters[state_name] = dict(counters)
        report = {"a": a, "b": b, "counters": state_counters, "solutions": state_solutions}
        map_reports.append(report)
        if all(state_solutions.values()):
            solution = report
            break
    print(json.dumps(encode({
        "status": "PASS" if solution else "NO_WITNESS",
        "scope": (
            "every common-owner-simple affine Z_17 relabelling until the first two-state "
            "witness; every pair of minimum-polarity assignments; no preexisting cross-copy "
            "typed collision; one collision-touching cut per copy; exact mixed unit C4"
        ),
        "source_sha256": hashlib.sha256(source_raw).hexdigest(),
        "common_owner_simple_maps": len(maps),
        "maps_tested": len(map_reports),
        "reports": map_reports,
        "solution": solution,
    }), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
