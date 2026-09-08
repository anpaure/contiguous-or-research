#!/usr/bin/env python3
"""Solver-free audit of the D5 three-state conditional reset gate.

Substantive execution belongs on H100.  The supplied state assignment is
checked directly on the union of the old and new suppressed owner factors.
Odd old components prove that two states are impossible.  The selected
tail/old-head/new-head state histogram is independently reconstructed.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import search_t2_cross_suffix_alternating_cycles_20260813 as base  # noqa:E402
from audit_t2_cross_suffix_c16_full_ml_topology_20260813 import (  # noqa:E402
    lifted_edges,
)
from verify_t2_c16_suffix_component_residence_20260813 import (  # noqa:E402
    projected_cycles,
    toggle,
)


def edge(left, right):
    return (left, right) if left < right else (right, left)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("selection")
    parser.add_argument("certificate")
    args = parser.parse_args()
    selection_raw = Path(args.selection).read_bytes()
    certificate_raw = Path(args.certificate).read_bytes()
    selection = json.loads(selection_raw)
    certificate = json.loads(certificate_raw)
    selection_sha = hashlib.sha256(selection_raw).hexdigest()
    assert certificate["selection_sha256"] == selection_sha

    m, n = 11, 22
    canonical = base.canonical_edges(m)
    post = set(canonical)
    base.apply_t2(post, list(base.dyck_words(5)))
    by_owner, by_colour = base.factor_maps(post)
    before_all = projected_cycles(lifted_edges(post, canonical, n), m)
    circuits = []
    touched = set()
    for item in selection["selection"]:
        owners = tuple(
            base.bits(word) for word in item["candidate"]["owners"]
        )
        colours = tuple(
            base.bits(word) for word in item["candidate"]["new_colours"]
        )
        rows = [
            (owners[index], colours[index - 1], colours[index])
            for index in range(len(owners))
        ]
        circuits.append(rows)
        touched.update(owners)
    before_cycles = [
        cycle for cycle in before_all if touched.intersection(cycle[0])
    ]
    assert len(before_cycles) == 372
    touched_owners = {owner for owners, _ in before_cycles for owner in owners}
    assert len(touched_owners) == 12420
    before_edges = {
        edge(owner, owners[(index + 1) % len(owners)])
        for owners, _ in before_cycles
        for index, owner in enumerate(owners)
    }
    simultaneous = toggle(post, circuits)
    after_cycles = [
        cycle for cycle in projected_cycles(
            lifted_edges(simultaneous, canonical, n), m
        )
        if touched.intersection(cycle[0])
    ]
    assert len(after_cycles) == 1
    after_owners = after_cycles[0][0]
    assert set(after_owners) == touched_owners
    after_edges = {
        edge(owner, after_owners[(index + 1) % len(after_owners)])
        for index, owner in enumerate(after_owners)
    }
    union_edges = before_edges | after_edges

    saved = certificate["owner_union_graph"]
    assignment_rows = saved["three_state_assignment"]
    assignment = {
        base.bits(word): state for word, state in assignment_rows
    }
    assert len(assignment) == len(assignment_rows) == len(touched_owners)
    assert set(assignment) == touched_owners
    assert set(assignment.values()) == {0, 1, 2}
    assert all(assignment[left] != assignment[right]
               for left, right in union_edges)

    old_length_histogram = Counter(len(owners) for owners, _ in before_cycles)
    assert all(length & 1 for length in old_length_histogram)
    # An old odd cycle is already a certificate that the union graph is not
    # bipartite, while the literal assignment is a three-colouring.
    chromatic_number = 3

    reset_histogram = Counter()
    pass_rows = 0
    reset_rows = 0
    for rows in circuits:
        removed_owner = {old: owner for owner, old, _ in rows}
        for owner, old, new in rows:
            old_external = next(
                other for other in by_colour[old] if other != owner
            )
            new_external = next(
                other for other in by_colour[new]
                if other != removed_owner[new]
            )
            triple = (
                assignment[owner], assignment[old_external],
                assignment[new_external]
            )
            assert triple[0] != triple[1] and triple[0] != triple[2]
            reset_histogram["".join(map(str, triple))] += 1
            if triple[1] == triple[2]:
                pass_rows += 1
            else:
                assert set(triple) == {0, 1, 2}
                reset_rows += 1
    assert dict(sorted(reset_histogram.items())) == (
        saved["selected_tail_old_new_state_histogram"]
    )
    assert pass_rows == saved["selected_pass_rows"]
    assert reset_rows == saved["selected_nontrivial_reset_rows"]

    degree = Counter()
    for left, right in union_edges:
        degree[left] += 1
        degree[right] += 1
    print(json.dumps({
        "status": "PASS",
        "selection_sha256": selection_sha,
        "certificate_sha256": hashlib.sha256(certificate_raw).hexdigest(),
        "vertices": len(touched_owners),
        "before_edges": len(before_edges),
        "after_edges": len(after_edges),
        "union_edges": len(union_edges),
        "degree_histogram": dict(sorted(Counter(degree.values()).items())),
        "old_component_length_histogram": dict(sorted(
            old_length_histogram.items()
        )),
        "odd_cycle_lower_bound": 3,
        "literal_three_colouring_upper_bound": 3,
        "union_graph_chromatic_number": chromatic_number,
        "selected_rows": pass_rows + reset_rows,
        "selected_pass_rows": pass_rows,
        "selected_nontrivial_reset_rows": reset_rows,
        "tail_old_new_state_histogram": dict(sorted(
            reset_histogram.items()
        )),
        "unoriented_nontrivial_reset_types": [
            "0:{1,2}", "1:{0,2}", "2:{0,1}"
        ],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
