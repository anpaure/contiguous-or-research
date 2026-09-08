#!/usr/bin/env python3
"""Search fixed-perfect-matching faces of the q4 Z17 bracelet master.

Run only on H100.  Each sampled perfect matching of the 70 fixed owner
bracelets retains only the strong self-column lifts above its 35 edges,
then solves those lift choices jointly with the 54 reflected column pairs.
"""

from __future__ import annotations

import argparse
import gc
import json
import random
import sys
from collections import Counter, defaultdict

import networkx as nx
from ortools.sat.python import cp_model

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


def reduced_edge(vertices, reflection, reduced_index):
    return tuple(sorted({
        reduced_index[min(v, reflection[v])] for v in vertices
    }))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--map", required=True)
    parser.add_argument("--samples", type=int, default=5)
    parser.add_argument("--seconds-per-sample", type=float, default=120)
    parser.add_argument("--workers", type=int, default=32)
    parser.add_argument("--seed", type=int, default=20260814)
    args = parser.parse_args()

    data = json.load(open(args.map, encoding="utf-8"))
    representatives, orbit_index = owner_orbits()
    reflection = reflection_action(representatives, orbit_index)
    fixed = {v for v in range(1430) if reflection[v] == v}
    orbit_representatives = sorted(
        v for v in range(1430) if v <= reflection[v]
    )
    reduced_index = {v: i for i, v in enumerate(orbit_representatives)}

    self_candidates, raw, quotient_simple = enumerate_strong_self_columns(
        orbit_index, reflection
    )
    lifts = defaultdict(list)
    for candidate in self_candidates:
        signature = tuple(sorted(set(candidate["edge"]) & fixed))
        assert len(signature) == 2
        lifts[signature].append(candidate)
    assert len(lifts) == 1260
    fixed_graph = nx.Graph()
    fixed_graph.add_nodes_from(fixed)
    fixed_graph.add_edges_from(lifts)
    assert set(dict(fixed_graph.degree()).values()) == {36}

    pair_indices, pool_self = paired_columns(data["candidates"], reflection)
    assert not pool_self and len(pair_indices) == 27008
    pair_configurations = []
    for left, right in pair_indices:
        columns = [data["candidates"][left], data["candidates"][right]]
        union = set(columns[0]["edge"]) | set(columns[1]["edge"])
        assert len(union) == 20 and not (union & fixed)
        edge = reduced_edge(union, reflection, reduced_index)
        assert len(edge) == 10
        pair_configurations.append((columns, edge))

    lift_degrees = [len(values) for values in lifts.values()]
    report = {
        "map": args.map,
        "raw_self_orders": raw,
        "quotient_simple_self_orders": quotient_simple,
        "unique_strong_self_columns": len(self_candidates),
        "fixed_distance2_vertices": len(fixed),
        "fixed_distance2_edges": len(lifts),
        "fixed_distance2_degree": 36,
        "min_lifts_per_fixed_edge": min(lift_degrees),
        "max_lifts_per_fixed_edge": max(lift_degrees),
        "lift_degree_histogram": dict(sorted(Counter(lift_degrees).items())),
        "usable_paired_configurations": len(pair_configurations),
        "samples": [],
    }

    seen_matchings = set()
    for sample in range(args.samples):
        rng = random.Random(args.seed + sample)
        for left, right in fixed_graph.edges:
            fixed_graph[left][right]["weight"] = rng.random()
        matching_raw = nx.max_weight_matching(
            fixed_graph, maxcardinality=True, weight="weight"
        )
        matching = tuple(sorted(tuple(sorted(edge)) for edge in matching_raw))
        assert len(matching) == 35
        if matching in seen_matchings:
            continue
        seen_matchings.add(matching)

        configurations = []
        for signature in matching:
            for candidate in lifts[signature]:
                edge = reduced_edge(candidate["edge"], reflection, reduced_index)
                assert len(edge) == 6
                configurations.append(("self", [candidate], edge))
        self_count = len(configurations)
        for columns, edge in pair_configurations:
            configurations.append(("pair", columns, edge))

        incidence = [[] for _ in orbit_representatives]
        for i, (_, _, edge) in enumerate(configurations):
            for row in edge:
                incidence[row].append(i)
        assert all(incidence)
        model = cp_model.CpModel()
        selected = [model.NewBoolVar(f"configuration_{i}")
                    for i in range(len(configurations))]
        for row in incidence:
            model.AddExactlyOne(selected[i] for i in row)
        model.Add(sum(selected[:self_count]) == 35)
        model.Add(sum(selected[self_count:]) == 54)
        solver = cp_model.CpSolver()
        solver.parameters.max_time_in_seconds = args.seconds_per_sample
        solver.parameters.num_search_workers = args.workers
        solver.parameters.random_seed = args.seed + sample
        status = solver.Solve(model)
        outcome = {
            "sample": sample,
            "status": solver.StatusName(status),
            "matching": [list(edge) for edge in matching],
            "self_lift_variables": self_count,
            "paired_variables": len(pair_configurations),
            "wall_time": solver.WallTime(),
            "branches": solver.NumBranches(),
            "conflicts": solver.NumConflicts(),
        }
        report["samples"].append(outcome)
        if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
            chosen_configurations = [
                configuration for i, configuration in enumerate(configurations)
                if solver.Value(selected[i])
            ]
            chosen = [
                column
                for _, columns, _ in chosen_configurations
                for column in columns
            ]
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
            report.update({
                "status": "PASS",
                "winning_sample": sample,
                "selected_rail_orbits": len(chosen),
                "selected_self_columns": 35,
                "selected_paired_configurations": 54,
                "developed_rails": rails,
                "covered_owners": owners,
                "point_degree": sorted(set(point.values())),
                # Core/order data deliberately preserve every L^(3)
                # position for the subsequent marked/unmarked assignment.
                "certificate": [
                    {"core": list(column["core"]),
                     "order": list(column["order"]),
                     "quotient_edge": list(column["edge"])}
                    for column in normalized
                ],
            })
            break
        del model, selected, solver, configurations, incidence
        gc.collect()
    else:
        report["status"] = "NO_CERTIFICATE_IN_CAPPED_SAMPLES"

    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
