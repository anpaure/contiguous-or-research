#!/usr/bin/env python3
"""Compact hostile replay of the mixed T0V q3 relay and suffix gate.

Substantive execution belongs on H100.  This script reconstructs the
canonical factor, the literal four-circuit packet, every typed deck through
linear upper q3, the complete body/S1/S2 current identity, finite provider
loads, the phase triangle/three-colouring, and projected component counts.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict

import networkx as nx

import audit_msw_t0v_tensor_residence_20260814 as base
import audit_msw_t0v_tensor_typed_currents_20260814 as typed
import audit_msw_t0v_mixed_c8_c6_tensor_20260814 as mixed_tensor
import audit_msw_t0v_mixed_q3_closed_tensor_20260814 as closed
import audit_msw_t0v_mixed_q3_loss_providers_20260814 as q3trace


W3 = base.bits("110111001111")
H3 = base.bits("110101101111")
S1_ROWS = [
    ("111010010111", -1),
    ("101011010111", +1),
    ("000011110111", +1),
    ("100011011111", -1),
    ("000011111111", -1),
]
S2_ROWS = [
    ("000011110111", +1),
    ("100011010111", -1),
]


def nonzero_difference(old, new):
    result = Counter(new)
    result.subtract(old)
    return Counter({value: amount for value, amount in result.items() if amount})


def all_decks(selected):
    result = typed.typed_decks(selected)
    result["upper_q3"] = closed.q3_deck(selected)
    return result


def support_casualties(old, new):
    delta = nonzero_difference(old, new)
    return sorted(
        value for value, amount in delta.items()
        if amount < 0 and new[value] == 0
    )


def tensor_delta(m, deck_name):
    old_selected = base.canonical_edges(m)
    new_selected = set(old_selected)
    closed.apply_tensor(new_selected, m)
    old = all_decks(old_selected)[deck_name]
    new = all_decks(new_selected)[deck_name]
    return nonzero_difference(old, new), old, new


def expected_delta(m, deck_name, base_delta):
    s = m - 6
    result = Counter()
    for suffix_word in base.dyck_words(s):
        suffix_owner = base.bits(suffix_word)
        owner_mark = suffix_owner << 12
        for value, amount in base_delta.items():
            result[value | owner_mark] += amount
        if s >= 1 and deck_name == "upper_q2":
            c0 = base.g(suffix_owner, s)
            result[base.bits("000011110111") | (c0 << 12)] += 1
            result[base.bits("100011010111") | (c0 << 12)] -= 1
        if s >= 1 and deck_name == "upper_q3":
            c0 = base.g(suffix_owner, s)
            for prefix, amount in S1_ROWS:
                result[base.bits(prefix) | (c0 << 12)] += amount
            if s >= 2:
                c1 = base.g(base.hmap(c0, s), s)
                g2 = c0 | c1
                for prefix, amount in S2_ROWS:
                    result[base.bits(prefix) | (g2 << 12)] += amount
    return Counter({value: amount for value, amount in result.items() if amount})


def owner_graph(selected):
    by_colour = defaultdict(list)
    for owner, colour in selected:
        by_colour[colour].append(owner)
    edges = []
    for colour, owners in by_colour.items():
        assert len(owners) == 2
        edges.append((min(owners), max(owners), colour))
    return edges


def phase_certificate():
    old = base.canonical_edges(6)
    new = set(old)
    closed.apply_tensor(new, 6)
    old_edges = owner_graph(old)
    new_edges = owner_graph(new)
    graph = nx.Graph()
    for left, right, _ in sorted(old_edges + new_edges):
        graph.add_edge(left, right)
    colouring = nx.coloring.greedy_color(
        graph, strategy="saturation_largest_first"
    )
    assert all(colouring[left] != colouring[right] for left, right in graph.edges())
    colours_used = 1 + max(colouring.values())
    assert colours_used == 3

    triangle = list(map(base.bits, [
        "110100000111", "110100001101", "110100100101",
    ]))
    expected = [
        (triangle[0], triangle[1], "new", base.bits("110100001111")),
        (triangle[1], triangle[2], "old", base.bits("110100101101")),
        (triangle[2], triangle[0], "new", base.bits("110100100111")),
    ]
    banks = {"old": old_edges, "new": new_edges}
    for left, right, label, colour in expected:
        assert any(
            {a, b} == {left, right} and edge_colour == colour
            for a, b, edge_colour in banks[label]
        )
    old_lifted = base.lifted_edges(old, old, 12)
    new_lifted = base.lifted_edges(new, old, 12)
    old_cycles = base.projected_cycles(old_lifted, 6)
    new_cycles = base.projected_cycles(new_lifted, 6)
    old_histogram = dict(sorted(Counter(map(len, old_cycles)).items()))
    new_histogram = dict(sorted(Counter(map(len, new_cycles)).items()))
    assert old_histogram == {13: 132}
    assert new_histogram == {13: 124, 104: 1}

    owner_to_root = {}
    for cycle in old_cycles:
        roots = [
            owner for owner in cycle
            if owner < (1 << 12) and base.dyck(owner, 6)
        ]
        assert len(roots) == 1
        for owner in cycle:
            owner_to_root[owner] = roots[0]
    merged = next(cycle for cycle in new_cycles if len(cycle) == 104)
    affected_roots = sorted({owner_to_root[owner] for owner in merged})
    expected_roots = sorted(map(base.bits, [
        "110101101000", "111100100010", "111100001010",
        "111100101000", "110111010000", "110101110000",
        "110101011000", "110110011000",
    ]))
    assert affected_roots == expected_roots

    # A directed unit Z3 potential sums to L=0 mod 3 around every oriented
    # component of length L.  Reversing a component changes no length.
    old_unit_z3 = all(len(cycle) % 3 == 0 for cycle in old_cycles)
    new_unit_z3 = all(len(cycle) % 3 == 0 for cycle in new_cycles)
    assert not old_unit_z3 and not new_unit_z3

    return {
        "triangle": [base.bitword(value, 12) for value in triangle],
        "z_free_three_colouring_verified": True,
        "colour_class_sizes": dict(sorted(Counter(colouring.values()).items())),
        "closure_cycle_histograms": {
            "old": old_histogram,
            "new": new_histogram,
        },
        "affected_old_roots": [base.bitword(root, 12) for root in affected_roots],
        "common_directed_unit_Z3_potential": False,
        "voltage_obstruction": "13 mod 3 = 1 already in the old closure; 104 mod 3 = 2 in the new merged closure",
        "minimum_nonunit_Z3_edges": {
            "old_full_closure": 264,
            "new_full_closure": 249,
            "old_affected_eight_cycles": 16,
            "new_affected_cycle": 1,
        },
    }


def base_packet_audit():
    canonical = base.canonical_edges(6)
    old = all_decks(canonical)
    frozen_c8, frozen_c6 = mixed_tensor.prefix_packet()
    frozen = set(canonical)
    frozen.symmetric_difference_update(frozen_c8 | frozen_c6)

    c12 = closed.cycle_support(closed.C12_OWNERS, closed.C12_COLOURS)
    relay = set(frozen)
    relay.symmetric_difference_update(c12)

    final = set(canonical)
    packets, owners, colours, incidences = closed.apply_tensor(final, 6)
    assert packets == 1
    assert (len(owners), len(colours), len(incidences)) == (17, 16, 34)
    final_decks = all_decks(final)
    frozen_q3 = closed.q3_deck(frozen)
    relay_q3 = closed.q3_deck(relay)

    assert old["upper_q3"][W3] == 1
    assert frozen_q3[W3] == 0
    assert relay_q3[W3] == 2 and relay_q3[H3] == 0
    assert final_decks["upper_q3"][W3] == 2
    assert final_decks["upper_q3"][H3] == old["upper_q3"][H3] == 1

    current_profile = {}
    for name in old:
        delta = nonzero_difference(old[name], final_decks[name])
        casualties = support_casualties(old[name], final_decks[name])
        assert not casualties
        current_profile[name] = {
            "positive_values": sum(amount > 0 for amount in delta.values()),
            "negative_values": sum(amount < 0 for amount in delta.values()),
            "support_casualties": 0,
        }
    return {
        "resources": {
            "owners": len(owners),
            "colours": len(colours),
            "incidences": len(incidences),
        },
        "loads": {
            "old_W3": old["upper_q3"][W3],
            "frozen_W3": frozen_q3[W3],
            "relay_W3": relay_q3[W3],
            "relay_H3": relay_q3[H3],
            "final_W3": final_decks["upper_q3"][W3],
            "final_H3": final_decks["upper_q3"][H3],
        },
        "current_profile": current_profile,
        "base_delta": {
            name: nonzero_difference(old[name], final_decks[name])
            for name in old
        },
    }


def projected_component_data(canonical, selected, m):
    lifted = base.lifted_edges(selected, canonical, 2 * m)
    counts = []
    histograms = []
    for rank in (m, m + 1):
        cycles = base.projected_cycles(lifted, rank)
        counts.append(len(cycles))
        histograms.append(dict(sorted(Counter(map(len, cycles)).items())))
    assert counts[0] == counts[1]
    assert histograms[0] == histograms[1]
    return counts[0], histograms[0]


def audit_width(m, base_delta):
    canonical = base.canonical_edges(m)
    final = set(canonical)
    packets, owners, colours, incidences = closed.apply_tensor(final, m)
    old = all_decks(canonical)
    new = all_decks(final)

    identity = {}
    casualties = {}
    for name in old:
        actual = nonzero_difference(old[name], new[name])
        expected = expected_delta(m, name, base_delta[name])
        assert actual == expected, (m, name, actual - expected, expected - actual)
        identity[name] = len(actual)
        rows = support_casualties(old[name], new[name])
        casualties[name] = [base.bitword(value, 2 * m) for value in rows]
        if name != "upper_q3":
            assert not rows

    expected_q3_casualties = {
        6: [],
        7: [],
        8: [],
        9: ["100011010111110111"],
        10: [
            "10001101011111011110",
            "10001101011111010111",
        ],
    }
    if m in expected_q3_casualties:
        assert casualties["upper_q3"] == expected_q3_casualties[m]

    # The destroyed W3[V] occurrence remains singleton through this finite
    # replay range.  This is deliberately not elevated to an all-width claim.
    frozen = set(canonical)
    mixed_tensor.apply_tensor(frozen, m)
    frozen_q3 = closed.q3_deck(frozen)
    singleton_rows = []
    for suffix_word in base.dyck_words(m - 6):
        target = W3 | (base.bits(suffix_word) << 12)
        assert old["upper_q3"][target] == 1
        assert frozen_q3[target] == 0
        singleton_rows.append(suffix_word)

    component_count, cycle_histogram = projected_component_data(canonical, final, m)
    catalan_m = sum(1 for _ in base.dyck_words(m))
    catalan_suffix = sum(1 for _ in base.dyck_words(m - 6))
    expected_components = catalan_m - 7 * catalan_suffix
    expected_histogram = {
        2 * m + 1: catalan_m - 8 * catalan_suffix,
        8 * (2 * m + 1): catalan_suffix,
    }
    assert component_count == expected_components
    assert cycle_histogram == expected_histogram

    return {
        "m": m,
        "packets": packets,
        "resources": [len(owners), len(colours), len(incidences)],
        "current_identity_nonzero_rows": identity,
        "support_casualties": casualties,
        "singleton_W3_suffixes_checked": len(singleton_rows),
        "projected_components": component_count,
        "component_formula": expected_components,
        "projected_cycle_histogram": cycle_histogram,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("m", nargs="*", type=int, default=[6, 7, 8, 9, 10])
    args = parser.parse_args()
    assert all(6 <= m <= 10 for m in args.m)

    base_audit = base_packet_audit()
    base_delta = base_audit.pop("base_delta")
    result = {
        "status": "PASS",
        "base": base_audit,
        "phase": phase_certificate(),
        "widths": [audit_width(m, base_delta) for m in args.m],
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
