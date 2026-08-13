#!/usr/bin/env python3
"""Classify finite-state common-history obstructions for the D5 bank.

Run only on H100.  This diagnostic separates three questions:

* whether the old edge cuts admit a direction-compatible rethreading;
* the minimum number of fixed owner-history states properly colouring the
  union of the pre/post suppressed factors;
* whether the sharper edge-history scheme (which preserves two-phase q2
  screens) survives equality contractions forced by direction-changing
  selected endpoints.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import Counter, defaultdict, deque
from pathlib import Path

from pysat.solvers import Solver

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
        self.size = {}

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.size[x] = 1
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b:
            return
        if self.size[a] < self.size[b]:
            a, b = b, a
        self.parent[b] = a
        self.size[a] += self.size[b]


def xor_components(constraints):
    adjacency = defaultdict(list)
    for left, right, bit, witness in constraints:
        adjacency[left].append((right, bit, witness))
        adjacency[right].append((left, bit, witness))
    value = {}
    root_of = {}
    contradiction = None
    roots = []
    for root in adjacency:
        if root in value:
            continue
        roots.append(root)
        value[root] = 0
        root_of[root] = root
        queue = deque([root])
        while queue:
            node = queue.popleft()
            for other, bit, witness in adjacency[node]:
                wanted = value[node] ^ bit
                if other not in value:
                    value[other] = wanted
                    root_of[other] = root
                    queue.append(other)
                elif value[other] != wanted and contradiction is None:
                    contradiction = witness
    return value, root_of, roots, contradiction


def shortest_xor_obstruction(constraints):
    adjacency = defaultdict(list)
    for index, (left, right, bit, witness) in enumerate(constraints):
        adjacency[left].append((right, bit, index))
        adjacency[right].append((left, bit, index))
    best = None
    for excluded, (left, right, bit, witness) in enumerate(constraints):
        start = (left, 0)
        target = (right, 1 - bit)
        queue = deque([start])
        parent = {start: None}
        parent_edge = {}
        while queue and target not in parent:
            node, parity = queue.popleft()
            for other, edge_bit, edge_index in adjacency[node]:
                if edge_index == excluded:
                    continue
                state = (other, parity ^ edge_bit)
                if state in parent:
                    continue
                parent[state] = (node, parity)
                parent_edge[state] = edge_index
                queue.append(state)
        if target not in parent:
            continue
        path = []
        state = target
        while state != start:
            path.append(parent_edge[state])
            state = parent[state]
        core = list(reversed(path)) + [excluded]
        if best is None or len(core) < len(best):
            best = core
    assert best is not None
    return [
        {
            "required_xor": constraints[index][2],
            **constraints[index][3],
        }
        for index in best
    ]


def colour_graph(vertices, edges, colours):
    vertices = sorted(vertices)
    index = {vertex: i for i, vertex in enumerate(vertices)}
    clauses = []
    for vertex in vertices:
        row = [index[vertex] * colours + c + 1 for c in range(colours)]
        clauses.append(row)
        for a in range(colours):
            for b in range(a + 1, colours):
                clauses.append([-row[a], -row[b]])
    for a, b in edges:
        assert a != b
        for colour in range(colours):
            clauses.append([
                -(index[a] * colours + colour + 1),
                -(index[b] * colours + colour + 1),
            ])
    with Solver(name="cadical195", bootstrap_with=clauses) as solver:
        if not solver.solve():
            return None, len(clauses)
        model = set(x for x in solver.get_model() if x > 0)
    assignment = {
        vertex: next(
            colour for colour in range(colours)
            if index[vertex] * colours + colour + 1 in model
        )
        for vertex in vertices
    }
    assert all(assignment[a] != assignment[b] for a, b in edges)
    return assignment, len(clauses)


def canonical_edge(a, b):
    return (a, b) if a < b else (b, a)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("selection")
    args = parser.parse_args()
    raw = Path(args.selection).read_bytes()
    data = json.loads(raw)
    assert data["status"] == "SAT" and len(data["selection"]) == 41

    m, n = 11, 22
    canonical = base.canonical_edges(m)
    post = set(canonical)
    base.apply_t2(post, list(base.dyck_words(5)))
    before_cycles = projected_cycles(lifted_edges(post, canonical, n), m)

    label_info = {}
    owner_info = {}
    length_histogram = Counter()
    for component, (owners, labels) in enumerate(before_cycles):
        length_histogram[len(owners)] += 1
        for index, (owner, label) in enumerate(zip(owners, labels)):
            assert label not in label_info and owner not in owner_info
            label_info[label] = (
                component,
                index,
                owner,
                owners[(index + 1) % len(owners)],
            )
            owner_info[owner] = component

    circuits = []
    removed_endpoint = {}
    orientation_constraints = []
    touched_components = set()
    for circuit_index, item in enumerate(data["selection"]):
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
        for row_index, (owner, old, _) in enumerate(rows):
            assert old not in removed_endpoint
            removed_endpoint[old] = owner
            component, _, tail, head = label_info[old]
            touched_components.add(component)
            assert owner in (tail, head)
            direction = 0 if owner == tail else 1
            orientation_constraints.append((
                ("component", component),
                ("trade", circuit_index),
                direction,
                {
                    "trade": circuit_index,
                    "edge_index": item["edge_index"],
                    "row": row_index,
                    "component": component,
                    "label": base.bitword(old, n + 1),
                },
            ))

    orientation, root_of, roots, orientation_obstruction = xor_components(
        orientation_constraints
    )
    orientation_core = None
    if orientation_obstruction is not None:
        orientation_core = shortest_xor_obstruction(
            orientation_constraints
        )
    touched_lengths = Counter(
        len(before_cycles[component][0]) for component in touched_components
    )
    odd_touched = sum(
        count for length, count in touched_lengths.items() if length & 1
    )

    simultaneous = toggle(post, circuits)
    after_cycles = projected_cycles(
        lifted_edges(simultaneous, canonical, n), m
    )
    after_endpoints = {}
    after_owner_labels = {}
    for owners, labels in after_cycles:
        for index, (owner, label) in enumerate(zip(owners, labels)):
            after_endpoints[label] = frozenset((
                owner, owners[(index + 1) % len(owners)]
            ))
        for index, owner in enumerate(owners):
            after_owner_labels[owner] = frozenset((
                labels[index - 1], labels[index]
            ))

    touched_owners = {
        owner
        for component in touched_components
        for owner in before_cycles[component][0]
    }
    before_edges = set()
    before_owner_labels = {}
    touched_labels = set()
    for component in touched_components:
        owners, labels = before_cycles[component]
        for index, (owner, label) in enumerate(zip(owners, labels)):
            next_owner = owners[(index + 1) % len(owners)]
            before_edges.add(canonical_edge(owner, next_owner))
            touched_labels.add(label)
        for index, owner in enumerate(owners):
            before_owner_labels[owner] = frozenset((
                labels[index - 1], labels[index]
            ))
    after_edges = {
        canonical_edge(*after_endpoints[label]) for label in touched_labels
    }
    union_edges = before_edges | after_edges
    union_degree = Counter()
    for a, b in union_edges:
        union_degree[a] += 1
        union_degree[b] += 1
    assert set(union_degree) == touched_owners
    owner_colouring = None
    owner_colour_trials = []
    for colours in range(1, 6):
        assignment, clauses = colour_graph(
            touched_owners, union_edges, colours
        )
        owner_colour_trials.append({
            "states": colours,
            "status": "SAT" if assignment is not None else "UNSAT",
            "clauses": clauses,
        })
        if assignment is not None:
            owner_colouring = assignment
            break
    assert owner_colouring is not None

    by_owner, by_colour = base.factor_maps(post)
    reset_histogram = Counter()
    reset_rows = 0
    pass_rows = 0
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
                owner_colouring[owner],
                owner_colouring[old_external],
                owner_colouring[new_external],
            )
            assert triple[0] != triple[1] and triple[0] != triple[2]
            reset_histogram["".join(map(str, triple))] += 1
            if triple[1] == triple[2]:
                pass_rows += 1
            else:
                reset_rows += 1

    # Each XOR connected component has two global orientations.  Enumerate
    # all choices when the finite orientation system is small (it is one for
    # this bank), and test the edge-history equality quotient.
    assert len(roots) <= 12
    orientation_variants = []
    for mask in range(
        (1 << len(roots)) if orientation_obstruction is None else 0
    ):
        flip = {
            root: (mask >> index) & 1 for index, root in enumerate(roots)
        }
        trade_sign = {
            trade: orientation[("trade", trade)]
            ^ flip[root_of[("trade", trade)]]
            for trade in range(len(circuits))
        }
        dsu = DSU()
        for label in touched_labels:
            dsu.find(label)
        for trade, rows in enumerate(circuits):
            if trade_sign[trade] != 0:
                continue
            old_labels = [old for _, old, _ in rows]
            for label in old_labels[1:]:
                dsu.union(old_labels[0], label)
        quotient_edges = set()
        self_loops = []
        for owner in touched_owners:
            for pair, shore in (
                (before_owner_labels[owner], "before"),
                (after_owner_labels[owner], "after"),
            ):
                a, b = map(dsu.find, pair)
                if a == b:
                    self_loops.append({
                        "owner": base.bitword(owner, n + 1),
                        "shore": shore,
                        "labels": [
                            base.bitword(label, n + 1) for label in pair
                        ],
                    })
                else:
                    quotient_edges.add(canonical_edge(a, b))
        trial = {
            "orientation_mask": mask,
            "trade_sign_histogram": dict(sorted(Counter(
                trade_sign.values()
            ).items())),
            "equality_classes": len({
                dsu.find(label) for label in touched_labels
            }),
            "self_loop_count": len(self_loops),
            "first_self_loops": self_loops[:8],
        }
        if not self_loops:
            vertices = {dsu.find(label) for label in touched_labels}
            colour_trials = []
            for colours in range(1, 7):
                assignment, clauses = colour_graph(
                    vertices, quotient_edges, colours
                )
                colour_trials.append({
                    "states": colours,
                    "status": "SAT" if assignment is not None else "UNSAT",
                    "clauses": clauses,
                })
                if assignment is not None:
                    break
            trial["edge_history_colour_trials"] = colour_trials
        orientation_variants.append(trial)

    print(json.dumps({
        "status": "PASS",
        "selection_sha256": hashlib.sha256(raw).hexdigest(),
        "selected_circuits": len(circuits),
        "selected_removed_edges": len(removed_endpoint),
        "touched_components": len(touched_components),
        "touched_component_length_histogram": dict(sorted(
            touched_lengths.items()
        )),
        "odd_touched_components": odd_touched,
        "two_phase_cycle_alternation_possible": odd_touched == 0,
        "orientation_xor": {
            "status": (
                "SAT" if orientation_obstruction is None else "UNSAT"
            ),
            "constraints": len(orientation_constraints),
            "connected_systems": len(roots),
            "minimum_inconsistent_cycle_size": (
                None if orientation_core is None else len(orientation_core)
            ),
            "minimum_inconsistent_cycle": orientation_core,
        },
        "owner_union_graph": {
            "vertices": len(touched_owners),
            "before_edges": len(before_edges),
            "after_edges": len(after_edges),
            "union_edges": len(union_edges),
            "degree_histogram": dict(sorted(Counter(
                union_degree.values()
            ).items())),
            "minimum_history_states": len(set(owner_colouring.values())),
            "colour_trials": owner_colour_trials,
            "three_state_assignment": [
                [base.bitword(owner, n + 1), owner_colouring[owner]]
                for owner in sorted(owner_colouring)
            ],
            "selected_tail_old_new_state_histogram": dict(sorted(
                reset_histogram.items()
            )),
            "selected_pass_rows": pass_rows,
            "selected_nontrivial_reset_rows": reset_rows,
            "unoriented_nontrivial_reset_template_types": 3,
        },
        "edge_history_orientation_variants": orientation_variants,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
