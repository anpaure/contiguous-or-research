#!/usr/bin/env python3
"""Verify a two-history residence lift of the frozen D5 actuator bank.

Substantive execution belongs on H100.  The program asks whether the 477
removed lower-projection edges of the frozen 41-circuit bank can be oriented
and two-coloured so that every alternating circuit uses one clock phase and
one splice orientation.  If so, it builds the literal depth-two source lift

    T, p_c, q_c

on every affected pre-switch component, rethreads the resulting chunks, and
checks the expanded post-switch factor.  In particular, it verifies exact
q2-target multiset invariance and two-shore q=2 residence.
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
    cyclic_run_minimum,
    projected_cycles,
    toggle,
)


def solve_bipartite_xor(constraints):
    """Solve value[left] xor value[right] = bit by graph propagation."""
    adjacency = defaultdict(list)
    for left, right, bit, witness in constraints:
        adjacency[left].append((right, bit, witness))
        adjacency[right].append((left, bit, witness))
    value = {}
    parent = {}
    parent_witness = {}
    for root in adjacency:
        if root in value:
            continue
        value[root] = 0
        queue = deque([root])
        while queue:
            node = queue.popleft()
            for other, bit, witness in adjacency[node]:
                wanted = value[node] ^ bit
                if other not in value:
                    value[other] = wanted
                    parent[other] = node
                    parent_witness[other] = witness
                    queue.append(other)
                elif value[other] != wanted:
                    return None, {
                        "node": repr(node),
                        "other": repr(other),
                        "required_xor": bit,
                        "actual_xor": value[node] ^ value[other],
                        "witness": witness,
                    }
    return value, None


def oriented_cycle(owners, labels, reverse):
    if not reverse:
        return list(owners), list(labels)
    return [owners[0], *reversed(owners[1:])], list(reversed(labels))


def traces_from_successor(successor, universe):
    seen = set()
    traces = []
    for start in universe:
        if start in seen:
            continue
        owners = []
        labels = []
        owner = start
        while owner not in seen:
            seen.add(owner)
            owners.append(owner)
            next_owner, label = successor[owner]
            labels.append(label)
            owner = next_owner
        assert owner == start
        traces.append((owners, labels))
    assert seen == set(universe)
    return traces


def expanded_trace(owners, labels, phase, p, q):
    length = len(owners)
    answer = []
    for index, owner in enumerate(owners):
        label = labels[index]
        colour = phase[label]
        next_owner = owners[(index + 1) % length]
        next_colour = phase[labels[(index + 1) % length]]
        assert next_colour == 1 - colour
        answer.extend((
            owner | p[colour] | q[colour],
            next_owner | p[colour] | q[colour],
            next_owner | p[next_colour] | q[colour],
        ))
    return answer


def audit_expanded(traces, phase, p, q, ground_size):
    all_owners = set()
    all_upper = set()
    q1_screens = Counter()
    q2_targets = Counter()
    lower_minima = [ground_size + 1, ground_size + 1]
    upper_minima = [ground_size + 1, ground_size + 1]
    total = 0
    for owners, labels in traces:
        length = len(owners)
        assert length % 2 == 0
        assert all(
            phase[labels[(i + 1) % length]] == 1 - phase[labels[i]]
            for i in range(length)
        )
        expanded = expanded_trace(owners, labels, phase, p, q)
        size = len(expanded)
        total += size
        assert len(set(expanded)) == size
        assert not all_owners.intersection(expanded)
        all_owners.update(expanded)
        supports = [
            expanded[i] ^ expanded[(i + 1) % size] for i in range(size)
        ]
        assert all(support.bit_count() == 2 for support in supports)
        assert all(not supports[i - 1] & supports[i] for i in range(size))
        upper = [
            expanded[i] | expanded[(i + 1) % size] for i in range(size)
        ]
        assert len(set(upper)) == size
        assert not all_upper.intersection(upper)
        all_upper.update(upper)
        upper_supports = [
            upper[i] ^ upper[(i + 1) % size] for i in range(size)
        ]
        assert all(support.bit_count() == 2 for support in upper_supports)
        assert all(
            not upper_supports[i - 1] & upper_supports[i]
            for i in range(size)
        )
        for i, label in enumerate(labels):
            c = phase[label]
            q1_screens[label | p[c] | q[c]] += 1
        for i in range(size):
            q2_targets[
                expanded[i - 1] | expanded[i] | expanded[(i + 1) % size]
            ] += 1
        lp, _ = cyclic_run_minimum(expanded, ground_size, 1)
        lz, _ = cyclic_run_minimum(expanded, ground_size, 0)
        up, _ = cyclic_run_minimum(upper, ground_size, 1)
        uz, _ = cyclic_run_minimum(upper, ground_size, 0)
        lower_minima[0] = min(lower_minima[0], lp)
        lower_minima[1] = min(lower_minima[1], lz)
        upper_minima[0] = min(upper_minima[0], up)
        upper_minima[1] = min(upper_minima[1], uz)
        assert lp >= 2 and lz >= 2 and up >= 2 and uz >= 2
    return {
        "owners": all_owners,
        "upper": all_upper,
        "q1_screens": q1_screens,
        "q2_targets": q2_targets,
        "total": total,
        "lower_minima": lower_minima,
        "upper_minima": upper_minima,
    }


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
    before_full = lifted_edges(post, canonical, n)
    before_cycles = projected_cycles(before_full, m)

    label_info = {}
    owner_cycle = {}
    for component, (owners, labels) in enumerate(before_cycles):
        assert len(owners) == len(labels) and len(owners) % 2 == 0
        for index, (owner, label) in enumerate(zip(owners, labels)):
            assert owner not in owner_cycle and label not in label_info
            owner_cycle[owner] = component
            label_info[label] = {
                "component": component,
                "index": index,
                "tail": owner,
                "head": owners[(index + 1) % len(owners)],
                "parity": index & 1,
            }

    circuits = []
    removed_endpoint = {}
    touched_components = set()
    phase_constraints = []
    orientation_constraints = []
    incidence_count = 0
    for circuit_index, item in enumerate(data["selection"]):
        candidate = item["candidate"]
        owners = tuple(base.bits(word) for word in candidate["owners"])
        colours = tuple(base.bits(word) for word in candidate["new_colours"])
        rows = [
            (owners[index], colours[index - 1], colours[index])
            for index in range(len(owners))
        ]
        circuits.append(rows)
        incidence_count += len(rows)
        trade_node_phase = ("trade_phase", circuit_index)
        trade_node_orientation = ("trade_orientation", circuit_index)
        for row_index, (owner, old, _) in enumerate(rows):
            assert old not in removed_endpoint
            removed_endpoint[old] = owner
            info = label_info[old]
            assert owner in (info["tail"], info["head"])
            component = info["component"]
            touched_components.add(component)
            direction_bit = 0 if info["tail"] == owner else 1
            witness = {
                "circuit": circuit_index,
                "edge_index": item["edge_index"],
                "row": row_index,
                "label": base.bitword(old, n + 1),
                "component": component,
            }
            phase_constraints.append((
                ("component_phase", component),
                trade_node_phase,
                info["parity"],
                witness,
            ))
            orientation_constraints.append((
                ("component_orientation", component),
                trade_node_orientation,
                direction_bit,
                witness,
            ))

    phase_solution, phase_obstruction = solve_bipartite_xor(
        phase_constraints
    )
    orientation_solution, orientation_obstruction = solve_bipartite_xor(
        orientation_constraints
    )
    if phase_solution is None or orientation_solution is None:
        print(json.dumps({
            "status": "OBSTRUCTION",
            "selection_sha256": hashlib.sha256(raw).hexdigest(),
            "phase_system_sat": phase_solution is not None,
            "orientation_system_sat": orientation_solution is not None,
            "phase_obstruction": phase_obstruction,
            "orientation_obstruction": orientation_obstruction,
        }, indent=2, sort_keys=True))
        return

    phase = {}
    for label, info in label_info.items():
        offset = phase_solution.get(
            ("component_phase", info["component"]), 0
        )
        phase[label] = info["parity"] ^ offset

    directed_before = {}
    before_traces = []
    touched_owners = set()
    for component in sorted(touched_components):
        owners, labels = oriented_cycle(
            *before_cycles[component],
            orientation_solution.get(
                ("component_orientation", component), 0
            ),
        )
        before_traces.append((owners, labels))
        touched_owners.update(owners)
        for index, (owner, label) in enumerate(zip(owners, labels)):
            directed_before[label] = (
                owner, owners[(index + 1) % len(owners)]
            )

    simultaneous = toggle(post, circuits)
    after_full = lifted_edges(simultaneous, canonical, n)
    after_projected = projected_cycles(after_full, m)
    after_endpoints = {}
    for owners, labels in after_projected:
        for index, label in enumerate(labels):
            after_endpoints[label] = frozenset((
                owners[index], owners[(index + 1) % len(owners)]
            ))

    successor_before = {}
    successor_after = {}
    incoming_after = Counter()
    for label, (tail, head) in directed_before.items():
        successor_before[tail] = (head, label)
        endpoints = after_endpoints[label]
        assert tail in touched_owners and head in touched_owners
        if label in removed_endpoint:
            old_selected = removed_endpoint[label]
            external = head if tail == old_selected else tail
            assert external in endpoints
            new_selected = next(owner for owner in endpoints if owner != external)
            if tail == external:
                new_tail, new_head = external, new_selected
            else:
                new_tail, new_head = new_selected, external
        else:
            assert endpoints == frozenset((tail, head))
            new_tail, new_head = tail, head
        assert new_tail not in successor_after
        successor_after[new_tail] = (new_head, label)
        incoming_after[new_head] += 1
    assert set(successor_before) == touched_owners
    assert set(successor_after) == touched_owners
    assert all(incoming_after[owner] == 1 for owner in touched_owners)

    after_traces = traces_from_successor(successor_after, touched_owners)
    assert len(before_traces) == len(touched_components) == 372
    assert len(after_traces) == 1
    assert len(after_traces[0][0]) == 12420

    # The retained label phase alternates at every old and new owner.
    for traces in (before_traces, after_traces):
        for owners, labels in traces:
            assert len(owners) % 2 == 0
            assert all(
                phase[labels[(i + 1) % len(labels)]]
                == 1 - phase[labels[i]]
                for i in range(len(labels))
            )

    pre_chunks = Counter()
    post_chunks = Counter()
    for owners, labels in before_traces:
        pre_chunks.update(
            (owner, phase[label]) for owner, label in zip(owners, labels)
        )
    for owners, labels in after_traces:
        post_chunks.update(
            (owner, phase[label]) for owner, label in zip(owners, labels)
        )
    assert pre_chunks == post_chunks

    changed_tails = {
        owner for owner in touched_owners
        if successor_before[owner] != successor_after[owner]
    }
    assert len(changed_tails) == incidence_count == 477
    history_histogram = Counter(
        phase[successor_before[owner][1]] for owner in changed_tails
    )

    p = [1 << (n + 1), 1 << (n + 2)]
    q = [1 << (n + 3), 1 << (n + 4)]
    ground_size = n + 5
    pre_audit = audit_expanded(
        before_traces, phase, p, q, ground_size
    )
    post_audit = audit_expanded(
        after_traces, phase, p, q, ground_size
    )
    assert pre_audit["total"] == post_audit["total"] == 37260
    assert pre_audit["q1_screens"] == post_audit["q1_screens"]
    assert pre_audit["q2_targets"] == post_audit["q2_targets"]

    print(json.dumps({
        "status": "PASS",
        "selection_sha256": hashlib.sha256(raw).hexdigest(),
        "affected_pre_components": len(before_traces),
        "affected_post_components": len(after_traces),
        "component_reduction": len(before_traces) - len(after_traces),
        "original_owners": len(touched_owners),
        "expanded_owners": pre_audit["total"],
        "selected_circuits": len(circuits),
        "selected_removed_edges": incidence_count,
        "phase_system": {
            "status": "SAT",
            "constraints": len(phase_constraints),
            "component_variables": len(touched_components),
            "trade_variables": len(circuits),
        },
        "orientation_system": {
            "status": "SAT",
            "constraints": len(orientation_constraints),
            "component_variables": len(touched_components),
            "trade_variables": len(circuits),
        },
        "common_history_words": ["p0,q0", "p1,q1"],
        "changed_chunk_successors": len(changed_tails),
        "changed_history_phase_histogram": dict(sorted(history_histogram.items())),
        "source_chunks_preserved_exactly": True,
        "cut_occurrences_disjoint": True,
        "fresh_clock_coordinates": 4,
        "source_depth": 2,
        "expanded_ground_size": ground_size,
        "expanded_owner_rank": m + 2,
        "expanded_q1_screen_multiset_invariant": True,
        "expanded_q2_target_multiset_invariant": True,
        "q2_support_losses": 0,
        "pre_lower_minimum_positive_zero_runs": pre_audit["lower_minima"],
        "post_lower_minimum_positive_zero_runs": post_audit["lower_minima"],
        "pre_upper_minimum_positive_zero_runs": pre_audit["upper_minima"],
        "post_upper_minimum_positive_zero_runs": post_audit["upper_minima"],
        "two_shore_q2_resident": True,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
