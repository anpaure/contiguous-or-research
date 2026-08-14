#!/usr/bin/env python3
"""Independent hostile replay of the affine two-copy cross-C4 obstruction.

Run substantively on H100 only.  This file does not import the search being
replayed.  It reconstructs the rails, minimum polarity collision types,
common owner-simple affine maps, bad-window cut menus, and both C4 cross
matchings directly.  Since no cross matching is Johnson, assignment-level
q1/q2 and residence checks cannot be reached.
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

BANKS = ("lower_q1", "upper_q1", "lower_q2", "upper_q2")


def affine(value, a, b):
    return frozenset((a * x + b) % 17 for x in value)


def move_rails(rails, a, b):
    return [(name, [affine(owner, a, b) for owner in cycle]) for name, cycle in rails]


def owners(rails):
    return {owner for _, cycle in rails for owner in cycle}


def edge(x, y):
    return frozenset((x, y))


def minimum_collision_types(rails):
    names = [name for name, _ in rails]
    decks = {name: base.typed_decks(cycle) for name, cycle in rails}
    types = Counter()
    assignments = 0
    for bits in itertools.product((False, True), repeat=len(names)):
        collisions = []
        for bank in BANKS:
            wants_upper = bank.startswith("upper")
            providers = defaultdict(list)
            for name, upper in zip(names, bits):
                if upper != wants_upper:
                    continue
                for index, resource in enumerate(decks[name][bank]):
                    providers[resource].append((name, index))
            collisions.extend(
                (bank, resource, tuple(where))
                for resource, where in providers.items() for _ in range(len(where) - 1)
                if len(where) > 1
            )
        if len(collisions) != 1:
            continue
        assignments += 1
        types[collisions[0]] += 1
    return assignments, types


def bad_window_cuts(rail_map, collision):
    bank, _, providers = collision
    cuts = set()
    for name, index in providers:
        cycle = rail_map[name]
        n = len(cycle)
        cuts.add(edge(cycle[index], cycle[(index + 1) % n]))
        if bank.endswith("q2"):
            cuts.add(edge(cycle[(index + 1) % n], cycle[(index + 2) % n]))
    return cuts


def cross_matchings(left, right):
    results = set()
    for x0, x1 in (tuple(left), tuple(reversed(tuple(left)))):
        for y0, y1 in (tuple(right), tuple(reversed(tuple(right)))):
            results.add(frozenset((edge(x1, y0), edge(y1, x0))))
    return results


def johnson(item):
    if len(item) != 2:
        return False
    x, y = tuple(item)
    return len(x ^ y) == 2


def encode_collision(collision, multiplicity):
    return {
        "bank": collision[0],
        "resource": base.encode_set(collision[1]),
        "providers": collision[2],
        "assignments": multiplicity,
    }


def main():
    source_raw = Path(sys.argv[1]).read_bytes()
    states = dict(base.rail_states())
    type_data = {}
    for name, rails in states.items():
        assert len(owners(rails)) == sum(len(cycle) for _, cycle in rails) == 146
        count, types = minimum_collision_types(rails)
        type_data[name] = (count, types)
    maps = []
    for a in range(1, 17):
        for b in range(17):
            if all(owners(rails).isdisjoint(owners(move_rails(rails, a, b))) for rails in states.values()):
                maps.append((a, b))
    totals = {name: Counter() for name in states}
    for a, b in maps:
        for state_name, rails in states.items():
            rail_map = dict(rails)
            moved_map = dict(move_rails(rails, a, b))
            types = type_data[state_name][1]
            for left_collision in types:
                for source_right in types:
                    right_collision = (
                        source_right[0], affine(source_right[1], a, b), source_right[2]
                    )
                    if left_collision[0].startswith("upper") != right_collision[0].startswith("upper"):
                        totals[state_name]["opposite_polarity_type_pairs"] += 1
                        continue
                    totals[state_name]["same_polarity_type_pairs"] += 1
                    for left_cut in bad_window_cuts(rail_map, left_collision):
                        for right_cut in bad_window_cuts(moved_map, right_collision):
                            assert set(left_cut).isdisjoint(right_cut)
                            totals[state_name]["target_cut_pairs"] += 1
                            for matching in cross_matchings(left_cut, right_cut):
                                totals[state_name]["distinct_cross_matchings"] += 1
                                if len(matching) == 2 and all(johnson(item) for item in matching):
                                    totals[state_name]["legal_johnson_c4"] += 1
    assert len(maps) == 103
    assert type_data["state_one"][0] == 160
    assert type_data["state_two"][0] == 320
    assert totals["state_one"]["target_cut_pairs"] == 8240
    assert totals["state_two"]["target_cut_pairs"] == 10712
    assert totals["state_one"]["legal_johnson_c4"] == 0
    assert totals["state_two"]["legal_johnson_c4"] == 0
    totals["state_one"]["legal_johnson_c4"] = 0
    totals["state_two"]["legal_johnson_c4"] = 0
    print(json.dumps({
        "status": "PASS",
        "conclusion": "NO_WITNESS",
        "scope": (
            "all 103 affine Z_17 relabelings owner-disjoint in both states; all minimum "
            "whole-rail polarity collision types; one bad-window cut per copy; both C4 "
            "cross matchings"
        ),
        "source_sha256": hashlib.sha256(source_raw).hexdigest(),
        "common_owner_simple_affine_maps": len(maps),
        "states": {
            name: {
                "minimum_assignments": type_data[name][0],
                "collision_types": [
                    encode_collision(key, value)
                    for key, value in sorted(
                        type_data[name][1].items(),
                        key=lambda item: (item[0][0], base.encode_set(item[0][1]), item[0][2]),
                    )
                ],
                "census": dict(totals[name]),
            }
            for name in states
        },
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
