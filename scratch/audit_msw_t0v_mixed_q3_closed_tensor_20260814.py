#!/usr/bin/env python3
"""Audit the suffix tensor of the q3-closed mixed+C12+C8 packet.

Substantive execution belongs on H100.  The 17-owner base packet is tensored
over every Dyck suffix.  Complete typed currents through linear upper q3,
support, topology, phase bipartiteness, and undilated residence are rebuilt.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict, deque

import audit_msw_t0v_tensor_residence_20260814 as base
import audit_msw_t0v_tensor_typed_currents_20260814 as typed
import audit_msw_t0v_mixed_c8_c6_tensor_20260814 as tensor
import audit_msw_t0v_mixed_q3_loss_providers_20260814 as q3trace


C12_OWNERS = [
    "110100000111", "110000001111", "110000101101",
    "110100100101", "110000100111", "110001000111",
]
C12_COLOURS = [
    "110100001111", "110000101111", "110100101101",
    "110100100111", "110001100111", "110101000111",
]
C8B_OWNERS = [
    "110101000011", "110100100011",
    "110100001011", "110100010011",
]
C8B_COLOURS = [
    "110101100011", "110100101011",
    "110100011011", "110101010011",
]
Q3_SEAM_NEGATIVE_PREFIX = "100011010111"


def cycle_support(owner_words, colour_words):
    owners = list(map(base.bits, owner_words))
    colours = list(map(base.bits, colour_words))
    support = set()
    for index, colour in enumerate(colours):
        support.add((owners[index], colour))
        support.add((owners[(index + 1) % len(owners)], colour))
    return support


def prefix_packet():
    c8, c6 = tensor.prefix_packet()
    return c8 | c6 | cycle_support(C12_OWNERS, C12_COLOURS) | cycle_support(C8B_OWNERS, C8B_COLOURS)


def apply_tensor(selected, m):
    prefix = prefix_packet()
    used_owners = set()
    used_colours = set()
    used_incidences = set()
    packets = 0
    for suffix_word in base.dyck_words(m - 6):
        suffix = base.bits(suffix_word) << 12
        incidences = {
            (owner | suffix, colour | suffix)
            for owner, colour in prefix
        }
        owners = {owner for owner, _ in incidences}
        colours = {colour for _, colour in incidences}
        assert not used_owners & owners
        assert not used_colours & colours
        assert not used_incidences & incidences
        used_owners |= owners
        used_colours |= colours
        used_incidences |= incidences
        assert sum(incidence in selected for incidence in incidences) == 17
        selected.symmetric_difference_update(incidences)
        packets += 1
    return packets, used_owners, used_colours, used_incidences


def q3_deck(selected):
    result = Counter()
    for _, colours in q3trace.paths(selected):
        for start in range(len(colours) - 2):
            result[colours[start] | colours[start + 1] | colours[start + 2]] += 1
    return result


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
    return {
        "negative_values": sum(row["delta"] < 0 for row in rows),
        "positive_values": sum(row["delta"] > 0 for row in rows),
        "support_casualties": [
            row for row in rows if row["delta"] < 0 and row["new_load"] == 0
        ],
        "rows": rows,
    }


def shortest_odd_phase_cycle(old_selected, new_selected, width):
    adjacency = defaultdict(set)
    edge_kind = defaultdict(set)
    for label, selected in (("old", old_selected), ("new", new_selected)):
        by_colour = defaultdict(list)
        for owner, colour in selected:
            by_colour[colour].append(owner)
        for colour, owners in by_colour.items():
            assert len(owners) == 2
            left, right = owners
            adjacency[left].add(right)
            adjacency[right].add(left)
            edge_kind[tuple(sorted((left, right)))].add(label)
    best = None
    for root in adjacency:
        distance = {root: 0}
        parent = {root: None}
        queue = deque([root])
        while queue:
            left = queue.popleft()
            for right in adjacency[left]:
                if right not in distance:
                    distance[right] = distance[left] + 1
                    parent[right] = left
                    queue.append(right)
                    continue
                if parent[left] == right or (distance[left] - distance[right]) % 2:
                    continue
                path_left = []
                path_right = []
                a, b = left, right
                seen_left = set()
                while a is not None:
                    seen_left.add(a)
                    path_left.append(a)
                    a = parent[a]
                while b not in seen_left:
                    path_right.append(b)
                    b = parent[b]
                common = b
                path_left = path_left[:path_left.index(common) + 1]
                cycle = path_left + list(reversed(path_right))
                if best is None or len(cycle) < len(best):
                    best = cycle
        if best is not None and len(best) == 3:
            break
    if best is None:
        return None
    edges = []
    for index, left in enumerate(best):
        right = best[(index + 1) % len(best)]
        edges.append({
            "left": base.bitword(left, width),
            "right": base.bitword(right, width),
            "present_in": sorted(edge_kind[tuple(sorted((left, right)))]),
        })
    return {
        "length": len(best),
        "owners": [base.bitword(owner, width) for owner in best],
        "edges": edges,
    }


def audit(m):
    canonical = base.canonical_edges(m)
    old = typed.typed_decks(canonical)
    old["upper_q3"] = q3_deck(canonical)
    selected = set(canonical)
    packets, owners, colours, incidences = apply_tensor(selected, m)
    new = typed.typed_decks(selected)
    new["upper_q3"] = q3_deck(selected)
    currents = {
        name: current(old[name], new[name], 2 * m)
        for name in old
    }
    phase_cycle = shortest_odd_phase_cycle(canonical, selected, 2 * m)
    suffix_m = m - 6
    boundary_q3 = []
    suffix_q2_deck = None
    if suffix_m >= 2:
        suffix_q2_deck = typed.typed_decks(base.canonical_edges(suffix_m))["upper_q2"]
        for suffix_word in base.dyck_words(suffix_m):
            suffix_owner = base.bits(suffix_word)
            first_colour = base.g(suffix_owner, suffix_m)
            next_owner = base.hmap(first_colour, suffix_m)
            second_colour = base.g(next_owner, suffix_m)
            suffix_turn = first_colour | second_colour
            target = base.bits(Q3_SEAM_NEGATIVE_PREFIX) | suffix_turn << 12
            boundary_q3.append({
                "suffix": suffix_word,
                "suffix_two_colour_union": base.bitword(suffix_turn, 2 * suffix_m),
                "suffix_q2_load": suffix_q2_deck[suffix_turn],
                "target": base.bitword(target, 2 * m),
                "old_load": old["upper_q3"][target],
                "new_load": new["upper_q3"][target],
            })
    lifted = base.lifted_edges(selected, canonical, 2 * m)
    shores = {}
    for rank in (m, m + 1):
        cycles = base.projected_cycles(lifted, rank)
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
        "typed_currents": currents,
        "shores": shores,
        "common_binary_phase": phase_cycle is None,
        "shortest_odd_phase_cycle": phase_cycle,
        "boundary_q3_seam_rows": boundary_q3,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("m", nargs="+", type=int)
    args = parser.parse_args()
    print(json.dumps({"status": "PASS", "runs": [audit(m) for m in args.m]}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
