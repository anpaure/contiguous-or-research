#!/usr/bin/env python3
"""Search semilength-six T0 two-C6 relays with typed support safety.

Substantive execution belongs on H100.  We enumerate every canonical
alternating incidence C6, then every owner-disjoint simultaneous pair.
The exact owner, upper/lower q1, and upper/lower q2 occurrence decks are
checked after the pair.  Positive pairs are replayed in the fixed odd lift
to obtain their exact component action and undilated residence minima.
"""

from __future__ import annotations

import argparse
import itertools
import json
from collections import Counter, defaultdict

import audit_msw_t0v_tensor_residence_20260814 as base


M = 6
N = 12
TARGET = base.bits("110011001111")


def deck_maps(selected):
    by_owner = defaultdict(set)
    by_colour = defaultdict(set)
    for owner, colour in selected:
        by_owner[owner].add(colour)
        by_colour[colour].add(owner)
    assert all(len(values) in (1, 2) for values in by_owner.values())
    assert all(len(values) == 2 for values in by_colour.values())
    return by_owner, by_colour


def decks(selected):
    by_owner, by_colour = deck_maps(selected)
    return {
        "owner": Counter(by_owner.keys()),
        "upper_q1": Counter(by_colour.keys()),
        "lower_q1": Counter(a & b for a, b in map(tuple, by_colour.values())),
        "upper_q2": Counter(
            a | b for values in by_owner.values() if len(values) == 2
            for a, b in (tuple(values),)
        ),
        "lower_q2": Counter(
            a & b for values in by_owner.values() if len(values) == 2
            for a, b in (tuple(values),)
        ),
    }


def enumerate_hexes(selected):
    answer = []
    for active_owner_bits in itertools.combinations(range(N), M - 1):
        core = sum(1 << bit for bit in active_owner_bits)
        outside = [bit for bit in range(N) if not core >> bit & 1]
        for a, b, c in itertools.combinations(outside, 3):
            oa, ob, oc = (core | 1 << bit for bit in (a, b, c))
            qab = core | 1 << a | 1 << b
            qbc = core | 1 << b | 1 << c
            qca = core | 1 << c | 1 << a
            incidences = (
                (oa, qab), (ob, qab),
                (ob, qbc), (oc, qbc),
                (oc, qca), (oa, qca),
            )
            statuses = [incidence in selected for incidence in incidences]
            if all(statuses[index] != statuses[(index + 1) % 6] for index in range(6)):
                answer.append(
                    {
                        "core": core,
                        "active": (a, b, c),
                        "owners": frozenset((oa, ob, oc)),
                        "colours": frozenset((qab, qbc, qca)),
                        "incidences": frozenset(incidences),
                    }
                )
    return answer


def apply(selected, *hexes):
    answer = set(selected)
    for hexagon in hexes:
        answer.symmetric_difference_update(hexagon["incidences"])
    return answer


def current(old, new):
    delta = Counter(new)
    delta.subtract(old)
    delta = Counter({value: amount for value, amount in delta.items() if amount})
    casualties = sorted(
        value for value, amount in delta.items()
        if amount < 0 and old[value] > 0 and new[value] == 0
    )
    return delta, casualties


def exact_local_currents(by_owner, by_colour, old_decks, hexagons):
    toggled = set()
    for hexagon in hexagons:
        toggled.symmetric_difference_update(hexagon["incidences"])
    affected_owners = {owner for owner, _ in toggled}
    affected_colours = {colour for _, colour in toggled}
    currents = {
        "owner": Counter(),
        "upper_q1": Counter(),
        "lower_q1": Counter(),
        "upper_q2": Counter(),
        "lower_q2": Counter(),
    }
    for owner in affected_owners:
        old_values = set(by_owner[owner])
        new_values = old_values ^ {
            colour for changed_owner, colour in toggled if changed_owner == owner
        }
        if len(new_values) != len(old_values):
            return None, None
        if len(old_values) == 2:
            old_a, old_b = old_values
            new_a, new_b = new_values
            currents["upper_q2"][new_a | new_b] += 1
            currents["upper_q2"][old_a | old_b] -= 1
            currents["lower_q2"][new_a & new_b] += 1
            currents["lower_q2"][old_a & old_b] -= 1
    for colour in affected_colours:
        old_values = set(by_colour[colour])
        new_values = old_values ^ {
            owner for owner, changed_colour in toggled if changed_colour == colour
        }
        if len(new_values) != len(old_values):
            return None, None
        old_a, old_b = old_values
        new_a, new_b = new_values
        currents["lower_q1"][new_a & new_b] += 1
        currents["lower_q1"][old_a & old_b] -= 1
    casualties = {
        name: sorted(
            value for value, amount in delta.items()
            if amount < 0 and old_decks[name][value] + amount <= 0
        )
        for name, delta in currents.items()
    }
    return currents, casualties


def encoded_current(delta):
    return [
        {"value": base.bitword(value, N), "delta": amount}
        for value, amount in sorted(delta.items())
    ]


def topology_and_residence(selected, canonical):
    lifted = base.lifted_edges(selected, canonical, N)
    answer = {}
    for rank in (M, M + 1):
        cycles = base.projected_cycles(lifted, rank)
        answer[str(rank)] = {
            "components": len(cycles),
            "owner_runs": base.run_minimum(cycles, N + 1, False)["minimum"],
            "upper_runs": base.run_minimum(cycles, N + 1, True)["minimum"],
        }
    return answer


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=20)
    parser.add_argument("--skip-triples", action="store_true")
    args = parser.parse_args()
    canonical = base.canonical_edges(M)
    old_decks = decks(canonical)
    by_owner, by_colour = deck_maps(canonical)
    hexes = enumerate_hexes(canonical)

    # Precompute the upper-q2 current, which is owner-local and therefore
    # additive for the owner-disjoint pairs searched below.
    creators = []
    creator_rows = []
    for index, hexagon in enumerate(hexes):
        after = apply(canonical, hexagon)
        after_decks = decks(after)
        delta, _ = current(old_decks["upper_q2"], after_decks["upper_q2"])
        hexagon["upper_q2_delta"] = delta
        if delta[TARGET] > 0:
            creators.append(index)
            typed_currents = {
                name: current(old_decks[name], after_decks[name])[0]
                for name in old_decks
            }
            creator_rows.append({
                "index": index,
                "core": base.bitword(hexagon["core"], N),
                "active_one_based": [bit + 1 for bit in hexagon["active"]],
                "owners": sorted(base.bitword(value, N) for value in hexagon["owners"]),
                "colours": sorted(base.bitword(value, N) for value in hexagon["colours"]),
                "currents": {
                    name: encoded_current(typed_delta)
                    for name, typed_delta in typed_currents.items()
                },
            })

    tested = 0
    q2_safe = 0
    lower_q1_safe = 0
    all_typed_safe = 0
    solutions = []
    for first_index in creators:
        first = hexes[first_index]
        for second_index, second in enumerate(hexes):
            if first["owners"] & second["owners"]:
                continue
            tested += 1
            upper_delta = first["upper_q2_delta"] + second["upper_q2_delta"]
            # Counter addition drops negative entries, so form it manually.
            upper_delta = Counter(first["upper_q2_delta"])
            upper_delta.update(second["upper_q2_delta"])
            if old_decks["upper_q2"][TARGET] + upper_delta[TARGET] <= 0:
                continue
            if any(
                amount < 0 and old_decks["upper_q2"][value] + amount <= 0
                for value, amount in upper_delta.items()
            ):
                continue
            q2_safe += 1
            selected = apply(canonical, first, second)
            new_decks = decks(selected)
            currents = {}
            casualties = {}
            for name in old_decks:
                currents[name], casualties[name] = current(old_decks[name], new_decks[name])
            if casualties["lower_q1"]:
                continue
            lower_q1_safe += 1
            if any(casualties.values()):
                continue
            all_typed_safe += 1
            if len(solutions) < args.limit:
                solutions.append(
                    {
                        "hexes": [
                            {
                                "index": index,
                                "core": base.bitword(hexagon["core"], N),
                                "active_one_based": [bit + 1 for bit in hexagon["active"]],
                                "owners": sorted(base.bitword(value, N) for value in hexagon["owners"]),
                                "colours": sorted(base.bitword(value, N) for value in hexagon["colours"]),
                            }
                            for index, hexagon in ((first_index, first), (second_index, second))
                        ],
                        "currents": {
                            name: encoded_current(delta)
                            for name, delta in currents.items()
                        },
                        "topology_residence": topology_and_residence(selected, canonical),
                    }
                )

    triple_tested = 0
    triple_q2_safe = 0
    triple_lower_q1_safe = 0
    triple_all_typed_safe = 0
    triple_solutions = []
    for first_index in ([] if args.skip_triples else creators):
        first = hexes[first_index]
        for second_index, second in enumerate(hexes):
            used_owners = first["owners"] | second["owners"]
            if len(used_owners) != 6:
                continue
            for third_index in range(second_index + 1, len(hexes)):
                third = hexes[third_index]
                if used_owners & third["owners"]:
                    continue
                triple_tested += 1
                upper_delta = Counter(first["upper_q2_delta"])
                upper_delta.update(second["upper_q2_delta"])
                upper_delta.update(third["upper_q2_delta"])
                if old_decks["upper_q2"][TARGET] + upper_delta[TARGET] <= 0:
                    continue
                if any(
                    amount < 0 and old_decks["upper_q2"][value] + amount <= 0
                    for value, amount in upper_delta.items()
                ):
                    continue
                triple_q2_safe += 1
                currents, casualties = exact_local_currents(
                    by_owner, by_colour, old_decks, (first, second, third)
                )
                if currents is None:
                    continue
                assert not casualties["upper_q2"]
                if casualties["lower_q1"]:
                    continue
                triple_lower_q1_safe += 1
                if any(casualties.values()):
                    continue
                triple_all_typed_safe += 1
                if len(triple_solutions) < args.limit:
                    selected = apply(canonical, first, second, third)
                    triple_solutions.append(
                        {
                            "hexes": [
                                {
                                    "index": index,
                                    "core": base.bitword(hexagon["core"], N),
                                    "active_one_based": [bit + 1 for bit in hexagon["active"]],
                                    "owners": sorted(base.bitword(value, N) for value in hexagon["owners"]),
                                    "colours": sorted(base.bitword(value, N) for value in hexagon["colours"]),
                                }
                                for index, hexagon in (
                                    (first_index, first),
                                    (second_index, second),
                                    (third_index, third),
                                )
                            ],
                            "currents": {
                                name: encoded_current(delta)
                                for name, delta in currents.items()
                            },
                            "topology_residence": topology_and_residence(selected, canonical),
                        }
                    )

    print(json.dumps(
        {
            "status": "PASS",
            "alternating_hexes": len(hexes),
            "target_creators": len(creators),
            "creator_rows": creator_rows,
            "owner_disjoint_pairs_tested": tested,
            "q2_support_safe_pairs": q2_safe,
            "also_lower_q1_support_safe_pairs": lower_q1_safe,
            "all_typed_support_safe_pairs": all_typed_safe,
            "solutions": solutions,
            "owner_disjoint_triples_tested": triple_tested,
            "triple_q2_support_safe": triple_q2_safe,
            "triple_also_lower_q1_support_safe": triple_lower_q1_safe,
            "triple_all_typed_support_safe": triple_all_typed_safe,
            "triple_solutions": triple_solutions,
        },
        indent=2,
        sort_keys=True,
    ))


if __name__ == "__main__":
    main()
