#!/usr/bin/env python3
"""Audit the Catalan tensor of the typed-safe mixed T0 C8+C6 packet.

Substantive execution belongs on H100.  For each semilength, every literal
prefix incidence is tensored by every Dyck suffix.  The verifier checks
packet/resource disjointness, all five typed occurrence currents, support,
the fixed odd-lift component count, and undilated residence diagnostics.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict

import audit_msw_t0v_tensor_residence_20260814 as base
import audit_msw_t0v_tensor_typed_currents_20260814 as typed


C8_OWNERS = [
    "110011000101",
    "110010000111",
    "100010010111",
    "100011010101",
]
C8_COLOURS = [
    "110011000111",
    "110010010111",
    "100011010111",
    "110011010101",
]
C6_CORE = "000011010110"
C6_ACTIVE = (0, 6, 11)


def prefix_packet():
    owners = list(map(base.bits, C8_OWNERS))
    colours = list(map(base.bits, C8_COLOURS))
    c8 = {
        (owners[0], colours[3]), (owners[0], colours[0]),
        (owners[1], colours[0]), (owners[1], colours[1]),
        (owners[2], colours[1]), (owners[2], colours[2]),
        (owners[3], colours[2]), (owners[3], colours[3]),
    }
    core = base.bits(C6_CORE)
    a, b, c = C6_ACTIVE
    oa, ob, oc = (core | 1 << bit for bit in (a, b, c))
    qab = core | 1 << a | 1 << b
    qbc = core | 1 << b | 1 << c
    qca = core | 1 << c | 1 << a
    c6 = {
        (oa, qab), (ob, qab),
        (ob, qbc), (oc, qbc),
        (oc, qca), (oa, qca),
    }
    return c8, c6


def apply_tensor(selected, m):
    c8, c6 = prefix_packet()
    used_owners = set()
    used_colours = set()
    used_incidences = set()
    packets = 0
    for suffix_word in base.dyck_words(m - 6):
        suffix = base.bits(suffix_word) << 12
        incidences = {
            (owner | suffix, colour | suffix)
            for owner, colour in c8 | c6
        }
        owners = {owner for owner, _ in incidences}
        colours = {colour for _, colour in incidences}
        assert not used_owners & owners
        assert not used_colours & colours
        assert not used_incidences & incidences
        used_owners |= owners
        used_colours |= colours
        used_incidences |= incidences
        assert sum(incidence in selected for incidence in incidences) == 7
        selected.symmetric_difference_update(incidences)
        packets += 1
    return packets, used_owners, used_colours, used_incidences


def current(old, new, width):
    result = Counter(new)
    result.subtract(old)
    rows = [
        {
            "value": base.bitword(value, width),
            "delta": amount,
            "old_load": old[value],
            "new_load": new[value],
        }
        for value, amount in sorted(result.items()) if amount
    ]
    casualties = [row for row in rows if row["delta"] < 0 and row["new_load"] == 0]
    return {
        "nonzero_values": len(rows),
        "negative_values": sum(row["delta"] < 0 for row in rows),
        "positive_values": sum(row["delta"] > 0 for row in rows),
        "support_casualties": casualties,
        "rows": rows,
    }


def owner_edges(selected):
    by_colour = defaultdict(list)
    for owner, colour in selected:
        by_colour[colour].append(owner)
    assert all(len(owners) == 2 for owners in by_colour.values())
    return {
        tuple(sorted(owners)) for owners in by_colour.values()
    }


def common_phase_exists(old_selected, new_selected):
    adjacency = defaultdict(set)
    for left, right in owner_edges(old_selected) | owner_edges(new_selected):
        adjacency[left].add(right)
        adjacency[right].add(left)
    phase = {}
    for start in adjacency:
        if start in phase:
            continue
        phase[start] = 0
        stack = [start]
        while stack:
            owner = stack.pop()
            for neighbour in adjacency[owner]:
                if neighbour not in phase:
                    phase[neighbour] = phase[owner] ^ 1
                    stack.append(neighbour)
                elif phase[neighbour] == phase[owner]:
                    return False
    return True


def audit(m):
    canonical = base.canonical_edges(m)
    old = typed.typed_decks(canonical)
    selected = set(canonical)
    packets, owners, colours, incidences = apply_tensor(selected, m)
    new = typed.typed_decks(selected)
    assert common_phase_exists(canonical, selected)
    currents = {
        name: current(old[name], new[name], 2 * m)
        for name in old
    }
    assert not any(report["support_casualties"] for report in currents.values())
    assert currents["owner"]["nonzero_values"] == 0
    assert currents["upper_q1"]["nonzero_values"] == 0
    assert currents["lower_q2"]["nonzero_values"] == 0
    assert currents["lower_q1"]["negative_values"] == 4 * packets
    assert currents["lower_q1"]["positive_values"] == 4 * packets
    upper_rows_per_packet = 3 if m == 6 else 4
    assert currents["upper_q2"]["negative_values"] == upper_rows_per_packet * packets
    assert currents["upper_q2"]["positive_values"] == upper_rows_per_packet * packets

    lifted = base.lifted_edges(selected, canonical, 2 * m)
    shores = {}
    expected = len(list(base.dyck_words(m))) - 5 * packets
    for rank in (m, m + 1):
        cycles = base.projected_cycles(lifted, rank)
        assert len(cycles) == expected
        shores[str(rank)] = {
            "components": len(cycles),
            "owner_runs": base.run_minimum(cycles, 2 * m + 1, False)["minimum"],
            "immediate_upper_runs": base.run_minimum(cycles, 2 * m + 1, True)["minimum"],
        }
    return {
        "m": m,
        "packets": packets,
        "changed_owners": len(owners),
        "touched_colours": len(colours),
        "toggled_incidences": len(incidences),
        "expected_components": expected,
        "common_binary_phase": True,
        "typed_currents": currents,
        "shores": shores,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("m", nargs="+", type=int)
    args = parser.parse_args()
    print(json.dumps({"status": "PASS", "runs": [audit(m) for m in args.m]}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
