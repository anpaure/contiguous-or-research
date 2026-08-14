#!/usr/bin/env python3
"""Audit occurrence-level typed lifts of the two q4/k17 recoupled states.

Run substantively on H100 only.  A closed owner rail has two distinct pure
incidence lifts: its lower lift alternates owners with consecutive-owner
intersections, while its upper lift alternates owners with unions.  Taking
both on every Johnson edge is *not* one degree-two occurrence lift: it gives
degree four at every owner.  The script records both possible shadow decks,
their q2 windows, collisions, signed state current, and all rail-polarity
assignments that are internally typed-simple.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import Counter, defaultdict
from itertools import product
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import verify_q4_k17_positive_common_reserve_20260814 as q4  # noqa:E402


def rail_states():
    atom_plus = q4.atom_shore(1)
    atom_minus = q4.atom_shore(-1)
    macro_plus, macro_minus = q4.macro_shores()
    return (
        ("state_one", macro_minus + atom_plus),
        ("state_two", macro_plus + atom_minus),
    )


def typed_decks(owners):
    n = len(owners)
    lower_q1 = [owners[i] & owners[(i + 1) % n] for i in range(n)]
    upper_q1 = [owners[i] | owners[(i + 1) % n] for i in range(n)]
    lower_q2 = [owners[i] & owners[(i + 1) % n] & owners[(i + 2) % n] for i in range(n)]
    upper_q2 = [owners[i] | owners[(i + 1) % n] | owners[(i + 2) % n] for i in range(n)]
    supports = [owners[i] ^ owners[(i + 1) % n] for i in range(n)]
    return {
        "lower_q1": lower_q1,
        "upper_q1": upper_q1,
        "lower_q2": lower_q2,
        "upper_q2": upper_q2,
        "supports": supports,
    }


def encode_set(value):
    return "".join("1" if i in value else "0" for i in range(17))


def occurrences(rails):
    banks = defaultdict(list)
    by_rail = {}
    for rail_name, owners in rails:
        decks = typed_decks(owners)
        by_rail[rail_name] = decks
        for bank in ("lower_q1", "upper_q1", "lower_q2", "upper_q2"):
            for index, resource in enumerate(decks[bank]):
                banks[bank].append((resource, rail_name, index))
    return by_rail, banks


def collision_ledger(entries):
    providers = defaultdict(list)
    for resource, rail, index in entries:
        providers[resource].append((rail, index))
    collisions = {
        resource: where for resource, where in providers.items() if len(where) > 1
    }
    return {
        "occurrences": len(entries),
        "distinct": len(providers),
        "collision_resources": len(collisions),
        "excess_occurrences": sum(len(where) - 1 for where in collisions.values()),
        "maximum_multiplicity": max(map(len, providers.values()), default=0),
        "collisions": [
            {
                "resource": encode_set(resource),
                "providers": [[rail, index] for rail, index in where],
            }
            for resource, where in sorted(collisions.items(), key=lambda item: encode_set(item[0]))
        ],
    }


def current(entries_one, entries_two):
    before = Counter(resource for resource, _, _ in entries_one)
    after = Counter(resource for resource, _, _ in entries_two)
    delta = after.copy()
    delta.subtract(before)
    nonzero = {resource: value for resource, value in delta.items() if value}
    return {
        "positive_total": sum(value for value in nonzero.values() if value > 0),
        "negative_total": -sum(value for value in nonzero.values() if value < 0),
        "support": len(nonzero),
        "maximum_absolute_coefficient": max(map(abs, nonzero.values()), default=0),
        "positive": [
            [encode_set(resource), value]
            for resource, value in sorted(nonzero.items(), key=lambda item: encode_set(item[0]))
            if value > 0
        ],
        "negative": [
            [encode_set(resource), -value]
            for resource, value in sorted(nonzero.items(), key=lambda item: encode_set(item[0]))
            if value < 0
        ],
    }


def support_residence(decks):
    supports = decks["supports"]
    n = len(supports)
    unions = [len(supports[i] | supports[(i + 1) % n] | supports[(i + 2) % n]) for i in range(n)]
    return {
        "three_support_minimum": min(unions),
        "three_support_histogram": dict(Counter(unions)),
        "owner_positive_run": 4,
        "owner_zero_run": n - 4,
        "upper_positive_run": 5,
        "upper_zero_run": n - 5,
    }


def polarity_menus(rails, by_rail):
    """Enumerate whole-rail lower/upper choices with simple active banks."""
    names = [name for name, _ in rails]
    answer = []
    rejection = Counter()
    for bits in product((0, 1), repeat=len(names)):
        active = {bank: [] for bank in ("lower_q1", "upper_q1", "lower_q2", "upper_q2")}
        for name, upper in zip(names, bits):
            if upper:
                active["upper_q1"].extend(by_rail[name]["upper_q1"])
                active["upper_q2"].extend(by_rail[name]["upper_q2"])
            else:
                active["lower_q1"].extend(by_rail[name]["lower_q1"])
                active["lower_q2"].extend(by_rail[name]["lower_q2"])
        bad = tuple(bank for bank, values in active.items() if len(values) != len(set(values)))
        if bad:
            rejection[bad] += 1
            continue
        answer.append({
            "upper_rails": tuple(name for name, upper in zip(names, bits) if upper),
            "lower_rails": tuple(name for name, upper in zip(names, bits) if not upper),
            "sizes": {bank: len(values) for bank, values in active.items()},
            "signature": tuple(
                tuple(sorted(encode_set(value) for value in active[bank]))
                for bank in ("lower_q1", "upper_q1", "lower_q2", "upper_q2")
            ),
        })
    return answer, rejection


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("source")
    args = parser.parse_args()
    source_raw = Path(args.source).read_bytes()
    states = rail_states()
    state_reports = []
    material = {}

    for state_name, rails in states:
        assert len(rails) == 14
        assert sum(len(owners) for _, owners in rails) == 146
        assert len({owner for _, owners in rails for owner in owners}) == 146
        by_rail, banks = occurrences(rails)
        menus, rejection = polarity_menus(rails, by_rail)
        material[state_name] = (rails, by_rail, banks, menus)
        state_reports.append({
            "state": state_name,
            "rails": [[name, len(owners)] for name, owners in rails],
            "physical_lift_rule": (
                "one whole rail is lower or upper; lower alternates O_i with "
                "O_i intersect O_(i+1), upper alternates O_i with O_i union O_(i+1)"
            ),
            "degree_if_both_shadows_selected": 4,
            "banks": {
                bank: collision_ledger(entries)
                for bank, entries in banks.items()
            },
            "rail_residence": {
                name: support_residence(by_rail[name]) for name, _ in rails
            },
            "simple_whole_rail_polarity_assignments": len(menus),
            "polarity_rejection_histogram": {
                ",".join(key): value for key, value in sorted(rejection.items())
            },
            "first_simple_polarity": None if not menus else {
                "lower_rails": menus[0]["lower_rails"],
                "upper_rails": menus[0]["upper_rails"],
                "sizes": menus[0]["sizes"],
            },
        })

    _, _, banks_one, menus_one = material["state_one"]
    _, _, banks_two, menus_two = material["state_two"]
    currents = {
        bank: current(banks_one[bank], banks_two[bank])
        for bank in ("lower_q1", "upper_q1", "lower_q2", "upper_q2")
    }

    signatures_one = defaultdict(list)
    for item in menus_one:
        signatures_one[item["signature"]].append(item)
    common_signatures = []
    for item in menus_two:
        if item["signature"] in signatures_one:
            common_signatures.append((signatures_one[item["signature"]][0], item))

    output = {
        "status": "PASS",
        "scope": (
            "occurrence-level pure lower/upper lifts and projected q1/q2 ledgers; "
            "not a connected two-sided factor"
        ),
        "source_sha256": hashlib.sha256(source_raw).hexdigest(),
        "state_reports": state_reports,
        "state_two_minus_state_one_currents": currents,
        "typed_simple_polarity_signature_matches": len(common_signatures),
        "first_matching_polarities": None if not common_signatures else {
            "state_one_lower": common_signatures[0][0]["lower_rails"],
            "state_one_upper": common_signatures[0][0]["upper_rails"],
            "state_two_lower": common_signatures[0][1]["lower_rails"],
            "state_two_upper": common_signatures[0][1]["upper_rails"],
            "sizes": common_signatures[0][0]["sizes"],
        },
    }
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
