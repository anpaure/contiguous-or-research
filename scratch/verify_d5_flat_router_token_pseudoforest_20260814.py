#!/usr/bin/env python3
"""Verify the router--token incidence pseudoforest of the flat D5 atlas.

Substantive execution belongs on H100.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter, defaultdict, deque
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate")
    args = parser.parse_args()
    raw = Path(args.certificate).read_bytes()
    certificate = json.loads(raw)
    assert certificate["status"] == "PASS"
    factors = certificate["factors"]

    adjacency = defaultdict(set)
    for index, factor in enumerate(factors):
        fnode = ("factor", index)
        assert len(factor) == len(set(factor)) == 3
        for token in factor:
            tnode = ("token", token)
            adjacency[fnode].add(tnode)
            adjacency[tnode].add(fnode)

    components = []
    unseen = set(adjacency)
    while unseen:
        root = min(unseen)
        queue = [root]
        vertices = set()
        while queue:
            vertex = queue.pop()
            if vertex in vertices:
                continue
            vertices.add(vertex)
            queue.extend(adjacency[vertex] - vertices)
        unseen -= vertices
        edges = sum(len(adjacency[v]) for v in vertices) // 2
        factors_here = sorted(v[1] for v in vertices if v[0] == "factor")
        tokens_here = sorted(v[1] for v in vertices if v[0] == "token")
        cycle_rank = edges - len(vertices) + 1

        # Peel leaves to identify the unique core of a unicyclic block.
        degree = {v: len(adjacency[v] & vertices) for v in vertices}
        leaves = deque(v for v, d in degree.items() if d <= 1)
        while leaves:
            vertex = leaves.popleft()
            if degree[vertex] == 0:
                continue
            degree[vertex] = 0
            for neighbor in adjacency[vertex] & vertices:
                if degree[neighbor] > 0:
                    degree[neighbor] -= 1
                    if degree[neighbor] == 1:
                        leaves.append(neighbor)
        core = {v for v, d in degree.items() if d > 0}
        components.append({
            "vertices": len(vertices),
            "edges": edges,
            "factors": factors_here,
            "tokens": tokens_here,
            "cycle_rank": cycle_rank,
            "two_core": sorted(core),
        })

    assert len(components) == 33
    assert Counter(component["cycle_rank"] for component in components) == {0: 25, 1: 8}
    assert all(
        not component["two_core"] if component["cycle_rank"] == 0
        else len(component["two_core"]) == 4
        for component in components
    )
    assert all(
        all(len(adjacency[vertex] & set(
            [(kind, value) for kind, value in component["two_core"]]
        )) == 2 for vertex in [tuple(value) for value in component["two_core"]])
        for component in components if component["cycle_rank"] == 1
    )

    # Each provenance block is exactly one graph component.
    factor_component = {}
    for component_index, component in enumerate(components):
        for factor_index in component["factors"]:
            assert factor_index not in factor_component
            factor_component[factor_index] = component_index
    provenance_kinds = Counter()
    for record in certificate["provenance"]:
        lo, hi = record["factor_range"]
        indices = list(range(lo, hi))
        component_ids = {factor_component[index] for index in indices}
        assert len(component_ids) == 1
        component = components[next(iter(component_ids))]
        assert component["factors"] == indices
        if record["kind"] == "odd_adjacent_chain":
            assert component["cycle_rank"] == 0
        elif record["kind"] == "paired_even_adjacent_chains":
            assert component["cycle_rank"] == 1
            core = [tuple(value) for value in component["two_core"]]
            assert Counter(kind for kind, _ in core) == {"factor": 2, "token": 2}
        else:
            raise AssertionError(record["kind"])
        provenance_kinds[record["kind"]] += 1

    token_degrees = Counter(
        len(neighbors) for vertex, neighbors in adjacency.items()
        if vertex[0] == "token"
    )
    factor_degrees = Counter(
        len(neighbors) for vertex, neighbors in adjacency.items()
        if vertex[0] == "factor"
    )
    assert token_degrees == {1: 292, 2: 169, 3: 16}
    assert factor_degrees == {3: 226}
    assert provenance_kinds == {
        "odd_adjacent_chain": 25,
        "paired_even_adjacent_chains": 8,
    }

    report = {
        "status": "PASS",
        "certificate_sha256": hashlib.sha256(raw).hexdigest(),
        "router_nodes": 226,
        "token_nodes": 477,
        "incidences": 678,
        "connected_components": len(components),
        "component_cycle_rank_histogram": {
            str(k): v for k, v in sorted(Counter(
                component["cycle_rank"] for component in components
            ).items())
        },
        "token_degree_histogram": {
            str(k): v for k, v in sorted(token_degrees.items())
        },
        "factor_degree_histogram": {
            str(k): v for k, v in sorted(factor_degrees.items())
        },
        "tree_blocks": provenance_kinds["odd_adjacent_chain"],
        "unicyclic_blocks": provenance_kinds["paired_even_adjacent_chains"],
        "unicyclic_two_core_shape": "K2,2=C4",
        "provenance_blocks_equal_components": True,
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
