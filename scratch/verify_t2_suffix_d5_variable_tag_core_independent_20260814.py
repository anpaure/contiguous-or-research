#!/usr/bin/env python3
"""Solver-free hostile audit of the D5 variable-tag no-go cores.

Substantive execution belongs on H100.  The input cores are replayed as
equality quotients.  Every orientation of the listed old components must
identify the endpoints of some required tag-change edge.  Deleting any one
owner equation must admit an orientation with no such quotient loop.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import Counter, defaultdict, deque
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


class DSU:
    def __init__(self):
        self.parent = {}

    def find(self, value):
        if value not in self.parent:
            self.parent[value] = value
        if self.parent[value] != value:
            self.parent[value] = self.find(self.parent[value])
        return self.parent[value]

    def union(self, left, right):
        left, right = self.find(left), self.find(right)
        if left != right:
            self.parent[right] = left


def orient(owners, labels, reverse):
    if not reverse:
        return list(owners), list(labels)
    return [owners[0], *reversed(owners[1:])], list(reversed(labels))


def quotient_loops(rows, components, mask, omitted=None):
    orientation = {
        component: (mask >> index) & 1
        for index, component in enumerate(components)
    }
    dsu = DSU()
    adjacency = defaultdict(list)
    active = []
    for index, row in enumerate(rows):
        if index == omitted:
            continue
        head = row["pre_heads"][orientation[row["component"]]]
        post_head = row["post_head"]
        dsu.union(head, post_head)
        adjacency[head].append((post_head, index))
        adjacency[post_head].append((head, index))
        active.append((index, row, head))
    loops = [
        (index, row, head) for index, row, head in active
        if dsu.find(row["owner"]) == dsu.find(head)
    ]
    return orientation, adjacency, loops


def shortest_path(adjacency, start, target):
    queue = deque([start])
    parent = {start: None}
    edge = {}
    while queue and target not in parent:
        node = queue.popleft()
        for other, row in adjacency[node]:
            if other in parent:
                continue
            parent[other] = node
            edge[other] = row
            queue.append(other)
    assert target in parent
    path = []
    node = target
    while node != start:
        path.append(edge[node])
        node = parent[node]
    return list(reversed(path))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("selection")
    parser.add_argument("core")
    args = parser.parse_args()
    selection_raw = Path(args.selection).read_bytes()
    core_raw = Path(args.core).read_bytes()
    selection = json.loads(selection_raw)
    core = json.loads(core_raw)
    assert core["selection_sha256"] == hashlib.sha256(selection_raw).hexdigest()

    m, n = 11, 22
    canonical = base.canonical_edges(m)
    post = set(canonical)
    base.apply_t2(post, list(base.dyck_words(5)))
    before_cycles = projected_cycles(lifted_edges(post, canonical, n), m)
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
        cycle for cycle in before_cycles if touched.intersection(cycle[0])
    ]
    simultaneous = toggle(post, circuits)
    after_cycles = [
        cycle for cycle in projected_cycles(
            lifted_edges(simultaneous, canonical, n), m
        )
        if touched.intersection(cycle[0])
    ]
    assert len(before_cycles) == 372 and len(after_cycles) == 1

    reports = []
    for result in core["orientations"]:
        post_reverse = result["post_reverse"]
        post_owners, _ = orient(*after_cycles[0], post_reverse)
        post_successor = {
            owner: post_owners[(index + 1) % len(post_owners)]
            for index, owner in enumerate(post_owners)
        }
        owner_component = {}
        pre_heads = {}
        for component, (owners, _) in enumerate(before_cycles):
            for index, owner in enumerate(owners):
                owner_component[owner] = component
                pre_heads[owner] = (
                    owners[(index + 1) % len(owners)], owners[index - 1]
                )
        rows = []
        for saved in result["rows"]:
            owner = base.bits(saved["owner"])
            assert owner_component[owner] == saved["pre_component"]
            heads = pre_heads[owner]
            assert [base.bitword(head, n + 1) for head in heads] == [
                saved["pre_forward_head"], saved["pre_reverse_head"]
            ]
            assert base.bitword(post_successor[owner], n + 1) == saved["post_head"]
            rows.append({
                "owner": owner,
                "component": saved["pre_component"],
                "pre_heads": heads,
                "post_head": post_successor[owner],
            })
        components = result["touched_pre_components"]
        assert {row["component"] for row in rows} == set(components)
        assignment_count = 1 << len(components)
        loop_histogram = Counter()
        path_histogram = Counter()
        witnesses = []
        for mask in range(assignment_count):
            orientation, adjacency, loops = quotient_loops(
                rows, components, mask
            )
            assert loops
            loop_histogram[len(loops)] += 1
            row_index, row, head = loops[0]
            path = shortest_path(adjacency, row["owner"], head)
            path_histogram[len(path)] += 1
            witnesses.append({
                "orientation": orientation,
                "violated_row": row_index,
                "equality_path_rows": path,
            })
        deletion_witnesses = []
        for omitted in range(len(rows)):
            witness = None
            for mask in range(assignment_count):
                orientation, _, loops = quotient_loops(
                    rows, components, mask, omitted=omitted
                )
                if not loops:
                    witness = orientation
                    break
            assert witness is not None
            deletion_witnesses.append(witness)
        reports.append({
            "post_reverse": post_reverse,
            "owner_equations": len(rows),
            "pre_components": len(components),
            "orientations_tested": assignment_count,
            "all_orientations_have_quotient_loop": True,
            "loop_count_histogram": dict(sorted(loop_histogram.items())),
            "shortest_equality_path_histogram": dict(sorted(
                path_histogram.items()
            )),
            "inclusion_minimal": True,
            "single_deletions_with_loop_free_orientation": len(
                deletion_witnesses
            ),
            "orientation_witnesses": witnesses,
        })
    print(json.dumps({
        "status": "PASS",
        "selection_sha256": hashlib.sha256(selection_raw).hexdigest(),
        "core_sha256": hashlib.sha256(core_raw).hexdigest(),
        "solver_free_quotient_replay": reports,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
