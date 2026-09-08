#!/usr/bin/env python3
"""Hostile replay of the positive first-flat C8 transition relation.

Run on H100 only.  This verifier is deliberately downstream of the seven
exhaustive search partitions: it rechecks every literal C8/q1/q2/residence
witness, extracts the q2-simple five-state transport relation, reconstructs the flat
router--token pseudoforest, and audits the eight abstract C4 holonomies.

The holonomy conclusion is support-quotient-level: it proves that a
transported copy of the extracted complete-irreflexive five-state support
relation never blocks one of the eight K2,2 cores.  It does not identify
the literal auxiliary owner edges across different typed factors, nor claim
that 226 packages have been coinstantiated with globally disjoint banks.
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
import solve_d5_tapped_c6_212_coinstantiation_20260814 as d5  # noqa:E402


def decode(word):
    return frozenset(i for i, c in enumerate(word) if c == "1")


def decode_edge(words):
    return frozenset(decode(word) for word in words)


def q1(edge):
    a, b = tuple(edge)
    return a & b, a | b


def support(edge):
    a, b = tuple(edge)
    return a ^ b


def exact_q1(before, after):
    return all(
        Counter(q1(edge)[shore] for edge in before)
        == Counter(q1(edge)[shore] for edge in after)
        for shore in (0, 1)
    )


def simple_q1(edges):
    return all(len(edges) == len({q1(edge)[shore] for edge in edges}) for shore in (0, 1))


def edge(a, b):
    return frozenset((a, b))


def adjacency(edges):
    result = defaultdict(set)
    for item in edges:
        a, b = tuple(item)
        result[a].add(b)
        result[b].add(a)
    return result


def internal_q2(edges):
    adj = adjacency(edges)
    rows = []
    for center, neighbors in adj.items():
        if len(neighbors) != 2:
            continue
        left, right = tuple(neighbors)
        rows.append((left & center & right, left | center | right))
    return rows


def context_collar_edges(selection, certificate, context_edges):
    _, raw_old, _ = d5.extract_rows(selection, certificate)
    canonical = set(d5.base.canonical_edges(11))
    integer_adj, _ = d5.factor_adjacency(d5.lifted_edges(raw_old, canonical))

    def integer(owner):
        return sum(1 << x for x in owner)

    result = set()
    for cut in context_edges:
        x, y = tuple(cut)
        for endpoint, other in ((x, y), (y, x)):
            endpoint_i, other_i = integer(endpoint), integer(other)
            one_i = next(value for value in integer_adj[endpoint_i] if value != other_i)
            two_i = next(value for value in integer_adj[one_i] if value != endpoint_i)
            one = frozenset(d5.bits_of(one_i))
            two = frozenset(d5.bits_of(two_i))
            result.add(edge(endpoint, one))
            result.add(edge(one, two))
    return result


def graph_components(factors):
    graph = defaultdict(set)
    for router, factor in enumerate(factors):
        rnode = ("r", router)
        for token in factor:
            tnode = ("t", token)
            graph[rnode].add(tnode)
            graph[tnode].add(rnode)
    unseen = set(graph)
    components = []
    while unseen:
        start = next(iter(unseen))
        stack = [start]
        vertices = set()
        while stack:
            vertex = stack.pop()
            if vertex in vertices:
                continue
            vertices.add(vertex)
            stack.extend(graph[vertex] - vertices)
        unseen -= vertices
        edge_count = sum(len(graph[v]) for v in vertices) // 2
        degree = {v: len(graph[v] & vertices) for v in vertices}
        queue = deque(v for v, d in degree.items() if d < 2)
        core = set(vertices)
        while queue:
            v = queue.popleft()
            if v not in core:
                continue
            core.remove(v)
            for w in graph[v] & core:
                degree[w] -= 1
                if degree[w] == 1:
                    queue.append(w)
        components.append({
            "vertices": vertices,
            "edges": edge_count,
            "cycle_rank": edge_count - len(vertices) + 1,
            "core": core,
        })
    return graph, components


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("selection")
    parser.add_argument("certificate")
    parser.add_argument("q1_witnesses")
    parser.add_argument("flat")
    parser.add_argument("partitions", nargs="+")
    args = parser.parse_args()
    assert len(args.partitions) == 7
    selection_raw = Path(args.selection).read_bytes()
    certificate_raw = Path(args.certificate).read_bytes()
    q1_raw = Path(args.q1_witnesses).read_bytes()
    flat_raw = Path(args.flat).read_bytes()
    selection = json.loads(selection_raw)
    certificate = json.loads(certificate_raw)
    source = json.loads(q1_raw)
    flat = json.loads(flat_raw)
    assert len(source["witnesses"]) == 21

    partition_hashes = {}
    partition_ranges = []
    aggregate_counters = Counter()
    solutions = []
    for path_text in args.partitions:
        path = Path(path_text)
        raw = path.read_bytes()
        report = json.loads(raw)
        assert report["status"] == "PASS"
        partition_hashes[path.name] = hashlib.sha256(raw).hexdigest()
        partition_ranges.append(tuple(report["witness_range"]))
        aggregate_counters.update(report["counters"])
        solutions.extend(report["solutions"])
    assert sorted(partition_ranges) == [
        (0, 3), (3, 6), (6, 9), (9, 12), (12, 15), (15, 18), (18, 21)
    ]
    assert len(solutions) == 147
    assert Counter(solution["witness_index"] for solution in solutions) == Counter({i: 7 for i in range(21)})

    context_cuts = {
        decode_edge(role["collar"]["old"][0])
        for role in source["witnesses"][0]["roles"]
    }
    exterior_collar_edges = context_collar_edges(selection, certificate, context_cuts)
    q2_simple_solutions = []
    q2_rejected_by_witness = Counter()
    for solution in solutions:
        phase_simple = []
        for phase in solution["after_edges"]:
            fixed = {decode_edge(words) for words in phase} | exterior_collar_edges
            decks = internal_q2(fixed)
            phase_simple.append(
                len(decks) == 30
                and len({lower for lower, _ in decks}) == 30
                and len({upper for _, upper in decks}) == 30
            )
        if all(phase_simple):
            q2_simple_solutions.append(solution)
        else:
            q2_rejected_by_witness[solution["witness_index"]] += 1
    assert len(q2_simple_solutions) == 126
    assert q2_rejected_by_witness == Counter({2: 7, 9: 7, 16: 7})

    relation_by_permutation = defaultdict(set)
    literal_checks = Counter()
    representative = None
    for solution in q2_simple_solutions:
        witness = source["witnesses"][solution["witness_index"]]
        old = tuple(decode_edge(edge_words) for edge_words in solution["c8_old"])
        new = tuple(decode_edge(edge_words) for edge_words in solution["c8_new"])
        assert len(set().union(*(set(edge) for edge in old))) == 8
        assert all(len(edge) == 2 and len(support(edge)) == 2 for edge in old + new)
        assert exact_q1(old, new) and simple_q1(old) and simple_q1(new)
        literal_checks["c8_owner_q1"] += 1

        before_phases = [tuple(decode_edge(words) for words in phase) for phase in solution["before_edges"]]
        after_phases = [tuple(decode_edge(words) for words in phase) for phase in solution["after_edges"]]
        assert len(before_phases) == len(after_phases) == 2
        for before, after in zip(before_phases, after_phases):
            assert len(before) == len(after) == 25
            assert exact_q1(before, after) and simple_q1(before) and simple_q1(after)
            literal_checks["full_phase_q1"] += 1
        assert solution["internal_q2_lower_delta"] == {}
        assert solution["internal_q2_upper_delta"] == {}
        literal_checks["internal_q2_zero"] += 1
        literal_checks["internal_q2_simple_phases"] += 2

        for phase_reports in solution["fixed_path_reports"]:
            for item in phase_reports:
                if item.get("resolved"):
                    assert item["resident"] and item["union_size"] == 6
                    assert not item["lower_q2_equal"] and not item["upper_q2_equal"]
                    literal_checks["resolved_resident_window"] += 1

        supports_old = tuple(support(edge) for edge in old)
        pivot = set.intersection(*(set(item) for item in supports_old))
        assert len(pivot) == 1
        pivot = next(iter(pivot))
        labels = tuple(next(iter(item - {pivot})) for item in supports_old)
        assert len(set(labels)) == 4
        # old order is context, current router, existing auxiliary, added auxiliary
        context_label, router_label, incoming_state, outgoing_state = labels
        assert Counter(support(edge) for edge in old) == Counter(support(edge) for edge in new)
        port = witness["token_permutation"].index(0)
        role = witness["roles"][port]
        assert old[0] == decode_edge(role["collar"]["old"][0])
        assert old[1] == decode_edge(role["router_edge"])
        # The general C8 replaces the old auxiliary occurrence.  Its first
        # auxiliary edge carries the same exchange-support state, but need
        # not have the same q1 flag or endpoints.
        assert support(old[2]) == support(decode_edge(role["auxiliary_edge"]))
        assert solution["token_zero_port"] == port
        relation_by_permutation[tuple(witness["token_permutation"])].add((incoming_state, outgoing_state))
        literal_checks["boundary_relation"] += 1
        if representative is None:
            representative = {
                "witness_index": solution["witness_index"],
                "token_permutation": witness["token_permutation"],
                "pivot": pivot,
                "context_label": context_label,
                "router_label": router_label,
                "incoming_state": incoming_state,
                "outgoing_state": outgoing_state,
                "old": solution["c8_old"],
                "new": solution["c8_new"],
            }

    assert len(relation_by_permutation) == 3
    relation_reports = []
    common_domain = None
    for permutation, relation in sorted(relation_by_permutation.items()):
        inputs = {left for left, _ in relation}
        outputs = {right for _, right in relation}
        domain = inputs & outputs
        assert len(inputs) == 6 and len(outputs) == 8 and len(domain) == 5
        restricted = {(left, right) for left, right in relation if left in domain and right in domain}
        expected = {(left, right) for left in domain for right in domain if left != right}
        assert restricted == expected
        assert len(relation) == 42 and len(restricted) == 20
        if common_domain is None:
            common_domain = domain
        else:
            assert domain == common_domain
        relation_reports.append({
            "token_permutation": permutation,
            "input_states": sorted(inputs),
            "output_states": sorted(outputs),
            "transport_domain": sorted(domain),
            "full_relation_size": len(relation),
            "restricted_relation_size": len(restricted),
            "restricted_relation": sorted(restricted),
        })
    assert common_domain is not None

    graph, components = graph_components(flat["factors"])
    assert len(components) == 33
    assert Counter(component["cycle_rank"] for component in components) == Counter({0: 25, 1: 8})
    cyclic = [component for component in components if component["cycle_rank"] == 1]
    assert all(len(component["core"]) == 4 for component in cyclic)
    assert all(
        len([v for v in component["core"] if v[0] == "r"]) == 2
        and len([v for v in component["core"] if v[0] == "t"]) == 2
        and all(len(graph[v] & component["core"]) == 2 for v in component["core"])
        for component in cyclic
    )

    q = len(common_domain)
    assert q == 5
    # A transported edge forbids at most one successor of each state.  On a
    # four-cycle: q choices, then q-1, q-1, and at least q-2 choices.
    twisted_c4_lower_bound = q * (q - 1) * (q - 1) * (q - 2)
    aligned_c4_assignments = (q - 1) ** 4 + (q - 1)
    assert twisted_c4_lower_bound == 240
    assert aligned_c4_assignments == 260
    holonomies = []
    for component in sorted(cyclic, key=lambda item: min(v[1] for v in item["core"] if v[0] == "r")):
        holonomies.append({
            "router_nodes": sorted(v[1] for v in component["core"] if v[0] == "r"),
            "token_nodes": sorted(v[1] for v in component["core"] if v[0] == "t"),
            "transport_robust_assignment_lower_bound": twisted_c4_lower_bound,
            "aligned_assignment_count": aligned_c4_assignments,
        })

    print(json.dumps({
        "status": "PASS",
        "scope": (
            "literal first-flat C8 extension relation plus transported support-quotient "
            "pseudoforest holonomy; not literal all-factor boundary identification or "
            "a 226-package resource coinstantiation"
        ),
        "selection_sha256": hashlib.sha256(selection_raw).hexdigest(),
        "certificate_sha256": hashlib.sha256(certificate_raw).hexdigest(),
        "q1_witnesses_sha256": hashlib.sha256(q1_raw).hexdigest(),
        "flat_sha256": hashlib.sha256(flat_raw).hexdigest(),
        "partition_sha256": partition_hashes,
        "aggregate_search_counters": dict(sorted(aggregate_counters.items())),
        "raw_resident_zero_current_solutions": len(solutions),
        "q2_simple_solutions": len(q2_simple_solutions),
        "q2_rejected_by_witness": dict(sorted(q2_rejected_by_witness.items())),
        "literal_checks": dict(sorted(literal_checks.items())),
        "representative": representative,
        "relation_reports": relation_reports,
        "common_transport_domain": sorted(common_domain),
        "tree_successors_per_state": q - 1,
        "pseudoforest": {
            "components": len(components),
            "tree_components": 25,
            "unicyclic_components": 8,
            "holonomies": holonomies,
        },
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
