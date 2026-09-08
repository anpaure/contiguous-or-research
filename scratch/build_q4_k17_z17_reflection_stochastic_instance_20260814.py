#!/usr/bin/env python3
"""Build/decode one fixed-matching stochastic bracelet instance (H100)."""

from __future__ import annotations

import argparse
import json
import random
import sys
from collections import defaultdict

import networkx as nx

sys.path.insert(0, "scratch")
from search_q4_k17_z17_quotient_exact_cover_20260814 import (
    owner_orbits,
    verify_development,
)
from search_q4_k17_z17_reflection_invariant_owner_cover_20260814 import (
    enumerate_strong_self_columns,
    paired_columns,
    reflection_action,
)


def make_instance(map_path: str, sample: int, seed: int):
    data = json.load(open(map_path, encoding="utf-8"))
    representatives, orbit_index = owner_orbits()
    reflection = reflection_action(representatives, orbit_index)
    fixed = {v for v in range(1430) if reflection[v] == v}
    nonfixed_representatives = sorted(
        v for v in range(1430) if v < reflection[v]
    )
    nonfixed_index = {}
    for i, v in enumerate(nonfixed_representatives):
        nonfixed_index[v] = i
        nonfixed_index[reflection[v]] = i
    assert len(nonfixed_representatives) == 680

    self_candidates, _, _ = enumerate_strong_self_columns(
        orbit_index, reflection
    )
    lifts = defaultdict(list)
    for candidate in self_candidates:
        signature = tuple(sorted(set(candidate["edge"]) & fixed))
        assert len(signature) == 2
        lifts[signature].append(candidate)
    graph = nx.Graph()
    graph.add_nodes_from(fixed)
    graph.add_edges_from(lifts)
    matching = None
    for current in range(sample + 1):
        rng = random.Random(seed + current)
        for left, right in graph.edges:
            graph[left][right]["weight"] = rng.random()
        raw = nx.max_weight_matching(graph, maxcardinality=True, weight="weight")
        matching = tuple(sorted(tuple(sorted(edge)) for edge in raw))
    assert matching is not None and len(matching) == 35

    self_options = []
    for group, signature in enumerate(matching):
        for candidate in lifts[signature]:
            rows = tuple(sorted({
                nonfixed_index[v] for v in candidate["edge"] if v not in fixed
            }))
            assert len(rows) == 4
            self_options.append((group, candidate, rows))

    pairs = []
    pair_indices, pool_self = paired_columns(data["candidates"], reflection)
    assert not pool_self
    for left, right in pair_indices:
        columns = [data["candidates"][left], data["candidates"][right]]
        union = set(columns[0]["edge"]) | set(columns[1]["edge"])
        assert not (union & fixed) and len(union) == 20
        rows = tuple(sorted({nonfixed_index[v] for v in union}))
        assert len(rows) == 10
        pairs.append((columns, rows))
    return matching, self_options, pairs


def build(args):
    matching, self_options, pairs = make_instance(args.map, args.sample, args.seed)
    with open(args.instance, "w", encoding="ascii") as stream:
        stream.write(f"680 35 {len(self_options)} {len(pairs)}\n")
        for group, _, rows in self_options:
            stream.write(" ".join(map(str, (group,) + rows)) + "\n")
        for _, rows in pairs:
            stream.write(" ".join(map(str, rows)) + "\n")
    print(json.dumps({
        "status": "BUILT",
        "sample": args.sample,
        "matching": [list(edge) for edge in matching],
        "self_options": len(self_options),
        "pair_options": len(pairs),
        "instance": args.instance,
    }, indent=2, sort_keys=True))


def decode(args):
    matching, self_options, pairs = make_instance(args.map, args.sample, args.seed)
    result = json.load(open(args.solution, encoding="utf-8"))
    assert result["status"] == "PASS" and result["energy"] == 0
    self_indices = result["self_indices"]
    pair_indices = result["pair_indices"]
    assert len(self_indices) == 35 and len(pair_indices) == 54
    assert len(set(self_indices)) == 35 and len(set(pair_indices)) == 54
    assert {self_options[i][0] for i in self_indices} == set(range(35))
    chosen = [self_options[i][1] for i in self_indices]
    for i in pair_indices:
        chosen.extend(pairs[i][0])
    assert len(chosen) == 143
    loads = [0] * 1430
    for column in chosen:
        for vertex in column["edge"]:
            loads[vertex] += 1
    assert set(loads) == {1}
    normalized = [
        {"core": tuple(column["core"]),
         "order": tuple(column["order"]),
         "edge": tuple(column["edge"])}
        for column in chosen
    ]
    rails, owners, point = verify_development(normalized)
    print(json.dumps({
        "status": "PASS",
        "sample": args.sample,
        "selected_rail_orbits": len(chosen),
        "selected_self_columns": 35,
        "selected_paired_configurations": 54,
        "developed_rails": rails,
        "covered_owners": owners,
        "point_degree": sorted(set(point.values())),
        "certificate": [
            {"core": list(column["core"]),
             "order": list(column["order"]),
             "quotient_edge": list(column["edge"])}
            for column in normalized
        ],
    }, indent=2, sort_keys=True))


def main():
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    builder = sub.add_parser("build")
    decoder = sub.add_parser("decode")
    for command in (builder, decoder):
        command.add_argument("--map", required=True)
        command.add_argument("--sample", type=int, default=0)
        command.add_argument("--seed", type=int, default=20260814)
    builder.add_argument("--instance", required=True)
    decoder.add_argument("--solution", required=True)
    args = parser.parse_args()
    (build if args.command == "build" else decode)(args)


if __name__ == "__main__":
    main()
