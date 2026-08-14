#!/usr/bin/env python3
"""Audit the fixed-closure phase-clock lift of the typed-safe T0 C8+C6.

Substantive execution belongs on H100.  The mixed packet is the unique
typed-support-safe owner-disjoint target-directed C8+C6 found by the exact
atlas replay.  This script derives its actual lifted-closure orientation,
tests a common binary owner phase, exhausts all old component directions,
and checks the finite stratified all-h certificate and direct clocks.
"""

from __future__ import annotations

import itertools
import json
from collections import defaultdict

import audit_msw_t0_relay_phase_endpoint_refinement as phase
import audit_msw_t0_relay_linear_allwidth as linear


M = 6
N = 12

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


def packet_incidences():
    owners = list(map(linear.bits, C8_OWNERS))
    colours = list(map(linear.bits, C8_COLOURS))
    c8 = {
        (owners[0], colours[3]), (owners[0], colours[0]),
        (owners[1], colours[0]), (owners[1], colours[1]),
        (owners[2], colours[1]), (owners[2], colours[2]),
        (owners[3], colours[2]), (owners[3], colours[3]),
    }
    core = linear.bits(C6_CORE)
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


def endpoint_closure_orientations(paths, names):
    adjacency = defaultdict(list)
    for pid, (owners, _) in enumerate(paths):
        left, right = names[owners[0]], names[owners[-1]]
        adjacency[left].append((right, "path", pid))
        adjacency[right].append((left, "path", pid))
    roots = {name[0] for name in adjacency}
    for root in roots:
        left, right = (root, 0), (root, M)
        assert left in adjacency and right in adjacency
        adjacency[left].append((right, "closure", root))
        adjacency[right].append((left, "closure", root))
    assert all(len(edges) == 2 for edges in adjacency.values())

    seen_edges = set()
    components = []
    for start in adjacency:
        if all((kind, label) in seen_edges for _, kind, label in adjacency[start]):
            continue
        current = start
        previous_edge = None
        orientations = {}
        roots_in_component = set()
        while True:
            options = [
                edge for edge in adjacency[current]
                if (edge[1], edge[2]) != previous_edge
            ]
            if previous_edge is None:
                options.sort(key=lambda edge: edge[1] != "path")
            assert options
            nxt, kind, label = options[0]
            edge_id = (kind, label)
            seen_edges.add(edge_id)
            if kind == "path":
                pid = label
                orientations[pid] = int(names[paths[pid][0][0]] != current)
            else:
                roots_in_component.add(label)
            previous_edge = edge_id
            current = nxt
            if current == start:
                break
        components.append({
            "paths": sorted(orientations),
            "roots": sorted(roots_in_component),
            "mask": orientations,
        })
    return components


def orient(paths, pids, mask):
    answer = list(paths)
    for index, pid in enumerate(pids):
        if mask >> index & 1:
            answer[pid] = phase.reverse_path(answer[pid])
    return answer


def word(value):
    return format(value, f"0{N}b")[::-1]


def main():
    selected, names = phase.canonical_named(M)
    canonical = set(selected)
    old_paths = phase.named_paths(canonical, names)
    c8, c6 = packet_incidences()
    assert len(c8) == 8 and len(c6) == 6
    assert len(c8 & c6) == 0
    assert sum(incidence in canonical for incidence in c8) == 4
    assert sum(incidence in canonical for incidence in c6) == 3
    selected.symmetric_difference_update(c8)
    selected.symmetric_difference_update(c6)
    new_paths = phase.named_paths(selected, names)

    old_edges = phase.owner_edges(old_paths)
    new_edges = phase.owner_edges(new_paths)
    affected_old = [
        pid for pid, path in enumerate(old_paths)
        if phase.owner_edges([path]) - new_edges
    ]
    affected_new = [
        pid for pid, path in enumerate(new_paths)
        if phase.owner_edges([path]) - old_edges
    ]
    common_phase, conflict = phase.common_phase(old_paths, new_paths)
    closure_components = endpoint_closure_orientations(new_paths, names)
    affected_set = set(affected_new)
    affected_components = [
        component for component in closure_components
        if affected_set & set(component["paths"])
    ]

    report = {
        "status": "PASS",
        "common_binary_phase": common_phase is not None,
        "phase_conflict": conflict,
        "old_path_count": len(old_paths),
        "new_path_count": len(new_paths),
        "affected_old_paths": affected_old,
        "affected_new_paths": affected_new,
        "affected_old_detail": [],
        "affected_new_detail": [],
        "affected_closure_components": [],
        "orientation_search": [],
    }
    for key, paths, pids in (
        ("affected_old_detail", old_paths, affected_old),
        ("affected_new_detail", new_paths, affected_new),
    ):
        report[key] = [
            {
                "pid": pid,
                "owners": [word(owner) for owner in paths[pid][0]],
                "owner_names": [names[owner] for owner in paths[pid][0]],
            }
            for pid in pids
        ]
    report["affected_closure_components"] = [
        {
            "paths": component["paths"],
            "roots": component["roots"],
            "stored_orientation_mask": {
                str(pid): direction for pid, direction in component["mask"].items()
            },
        }
        for component in affected_components
    ]
    if common_phase is None:
        print(json.dumps(report, indent=2, sort_keys=True))
        return
    assert len(affected_components) == 1
    component = affected_components[0]
    assert set(component["paths"]) == affected_set
    new_physical_masks = []
    for reverse_all in (0, 1):
        mask = 0
        for index, pid in enumerate(affected_new):
            if component["mask"][pid] ^ reverse_all:
                mask |= 1 << index
        new_physical_masks.append(mask)

    best = None
    for old_mask in range(1 << len(affected_old)):
        oriented_old = orient(old_paths, affected_old, old_mask)
        old_stratified, old_witness = phase.stratified_base_signatures(
            oriented_old, common_phase
        )
        for new_mask in new_physical_masks:
            oriented_new = orient(new_paths, affected_new, new_mask)
            new_stratified, new_witness = phase.stratified_base_signatures(
                oriented_new, common_phase
            )
            short_old = {
                (owners[index] | owners[index + 1], common_phase[owners[index]])
                for owners, _ in oriented_old
                for index in range(len(owners) - 1)
            }
            short_new = {
                (owners[index] | owners[index + 1], common_phase[owners[index]])
                for owners, _ in oriented_new
                for index in range(len(owners) - 1)
            }
            row = {
                "old_mask": old_mask,
                "new_mask": new_mask,
                "stratified_loss": len(old_stratified - new_stratified),
                "stratified_birth": len(new_stratified - old_stratified),
                "two_block_loss": len(short_old - short_new),
                "two_block_birth": len(short_new - short_old),
            }
            key = (row["stratified_loss"], row["two_block_loss"], old_mask, new_mask)
            if best is None or key < best[0]:
                best = (
                    key, row, oriented_old, oriented_new,
                    old_stratified, new_stratified,
                    old_witness, new_witness,
                )
    (
        _, best_row, oriented_old, oriented_new,
        old_stratified, new_stratified,
        old_witness, new_witness,
    ) = best
    best_row["new_physical_masks"] = new_physical_masks
    best_row["stratified_loss_rows"] = []
    for value in sorted(old_stratified - new_stratified, key=str)[:40]:
        pid, first, last = old_witness[value]
        target = value[1]
        alternatives = [
            {
                "signature": str(signature),
                "witness": new_witness[signature],
            }
            for signature in sorted(new_stratified, key=str)
            if signature[1] == target
        ]
        best_row["stratified_loss_rows"].append({
            "signature": str(value),
            "value_word": word(target),
            "old_witness": [pid, first, last],
            "old_owner_interval": [
                word(owner) for owner in oriented_old[pid][0][first:last + 1]
            ],
            "new_same_value_alternatives": alternatives,
        })
    for h in range(2, 9):
        old_support, _ = phase.lifted_clock_support(oriented_old, common_phase, h)
        new_support, _ = phase.lifted_clock_support(oriented_new, common_phase, h)
        best_row.setdefault("clock_replay", []).append({
            "h": h,
            "old": len(old_support),
            "new": len(new_support),
            "loss": len(old_support - new_support),
            "birth": len(new_support - old_support),
        })
    report["orientation_search"] = best_row
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
