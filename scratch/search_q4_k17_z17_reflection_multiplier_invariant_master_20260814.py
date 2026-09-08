#!/usr/bin/env python3
"""Solve multiplier-invariant faces of the q4 Z17 bracelet master.

Run only on H100.  Reflection has already reduced the owner universe to
750 bracelet rows.  A nonzero multiplier commutes with reflection and acts
on those rows and on both configuration catalogues.  This program selects
whole configuration orbits under the generated multiplier subgroup.  An
orbit is retained only when its member configurations are row-disjoint;
it then becomes one exact-cover column on the quotient row orbits.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter

from ortools.sat.python import cp_model

sys.path.insert(0, "scratch")
from search_q4_k17_z17_quotient_exact_cover_20260814 import (
    K,
    canonical_orbit_mask,
    owner_orbits,
    verify_development,
)
from search_q4_k17_z17_reflection_invariant_owner_cover_20260814 import (
    enumerate_strong_self_columns,
    paired_columns,
    reflection_action,
)


def multiply_mask(mask: int, multiplier: int) -> int:
    moved = 0
    for value in range(K):
        if mask >> value & 1:
            moved |= 1 << ((multiplier * value) % K)
    return canonical_orbit_mask(moved)


def permutation_orbits(permutation):
    seen = set()
    result = []
    for start in range(len(permutation)):
        if start in seen:
            continue
        orbit = []
        current = start
        while current not in seen:
            seen.add(current)
            orbit.append(current)
            current = permutation[current]
        assert current == start
        result.append(tuple(orbit))
    return result


def solve(map_path: str, multiplier: int, seconds: float,
          workers: int, seed: int) -> None:
    data = json.load(open(map_path, encoding="utf-8"))
    representatives, orbit_index = owner_orbits()
    reflection = reflection_action(representatives, orbit_index)
    bracelet_representatives = sorted(
        vertex for vertex in range(1430) if vertex <= reflection[vertex]
    )
    bracelet_index = {
        vertex: index for index, vertex in enumerate(bracelet_representatives)
    }

    owner_action = tuple(
        orbit_index[multiply_mask(mask, multiplier)]
        for mask in representatives
    )
    bracelet_action = tuple(
        bracelet_index[min(owner_action[vertex],
                           reflection[owner_action[vertex]])]
        for vertex in bracelet_representatives
    )
    row_orbits = permutation_orbits(bracelet_action)
    row_orbit_index = {
        row: index for index, orbit in enumerate(row_orbits) for row in orbit
    }

    self_candidates, raw, quotient_simple = enumerate_strong_self_columns(
        orbit_index, reflection
    )
    configurations = []
    for candidate in self_candidates:
        edge = tuple(sorted({
            bracelet_index[min(vertex, reflection[vertex])]
            for vertex in candidate["edge"]
        }))
        assert len(edge) == 6
        configurations.append({
            "kind": "self", "columns": [candidate], "edge": edge,
        })

    pair_indices, pool_self = paired_columns(data["candidates"], reflection)
    assert not pool_self
    for left, right in pair_indices:
        columns = [data["candidates"][left], data["candidates"][right]]
        union = set(columns[0]["edge"]) | set(columns[1]["edge"])
        assert len(union) == 20
        edge = tuple(sorted({
            bracelet_index[min(vertex, reflection[vertex])]
            for vertex in union
        }))
        assert len(edge) == 10
        configurations.append({
            "kind": "pair", "columns": columns, "edge": edge,
        })

    # Owner-equivalent duplicate configurations are interchangeable for
    # this owner-only master.  Keep one concrete rail representative so a
    # selected quotient column still decodes to literal core/order data.
    unique = {}
    for configuration in configurations:
        unique.setdefault((configuration["kind"], configuration["edge"]),
                          configuration)
    configurations = list(unique.values())
    configuration_index = {
        (configuration["kind"], configuration["edge"]): index
        for index, configuration in enumerate(configurations)
    }
    configuration_action = []
    for configuration in configurations:
        moved_edge = tuple(sorted(bracelet_action[row]
                                  for row in configuration["edge"]))
        configuration_action.append(configuration_index[
            (configuration["kind"], moved_edge)
        ])
    configuration_orbits = permutation_orbits(configuration_action)

    orbit_columns = []
    rejected_overlap = Counter()
    for orbit in configuration_orbits:
        kind = configurations[orbit[0]]["kind"]
        assert all(configurations[index]["kind"] == kind for index in orbit)
        rows = [row for index in orbit
                for row in configurations[index]["edge"]]
        if len(set(rows)) != len(rows):
            rejected_overlap[kind] += 1
            continue
        quotient_edge = tuple(sorted({row_orbit_index[row] for row in rows}))
        assert sum(len(row_orbits[index]) for index in quotient_edge) == len(rows)
        orbit_columns.append({
            "kind": kind,
            "members": orbit,
            "edge": quotient_edge,
        })

    incidence = [[] for _ in row_orbits]
    for index, column in enumerate(orbit_columns):
        for row in column["edge"]:
            incidence[row].append(index)
    report = {
        "map": map_path,
        "multiplier": multiplier,
        "multiplier_row_orbit_histogram": dict(sorted(Counter(
            map(len, row_orbits)
        ).items())),
        "bracelet_rows": 750,
        "quotient_rows": len(row_orbits),
        "raw_self_orders": raw,
        "quotient_simple_self_orders": quotient_simple,
        "unique_self_configurations": sum(
            configuration["kind"] == "self"
            for configuration in configurations
        ),
        "unique_pair_configurations": sum(
            configuration["kind"] == "pair"
            for configuration in configurations
        ),
        "configuration_orbits": len(configuration_orbits),
        "usable_orbit_columns": len(orbit_columns),
        "rejected_overlapping_orbits": dict(rejected_overlap),
        "minimum_row_degree": min(map(len, incidence)),
        "maximum_row_degree": max(map(len, incidence)),
    }
    if any(not row for row in incidence):
        report["status"] = "UNCOVERED_QUOTIENT_ROW"
        print(json.dumps(report, indent=2, sort_keys=True))
        return

    model = cp_model.CpModel()
    selected = [model.NewBoolVar(f"orbit_{index}")
                for index in range(len(orbit_columns))]
    for row in incidence:
        model.AddExactlyOne(selected[index] for index in row)
    # Redundant physical configuration counts sharpen propagation.
    model.Add(sum(len(column["members"]) * selected[index]
                  for index, column in enumerate(orbit_columns)
                  if column["kind"] == "self") == 35)
    model.Add(sum(len(column["members"]) * selected[index]
                  for index, column in enumerate(orbit_columns)
                  if column["kind"] == "pair") == 54)
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = seconds
    solver.parameters.num_search_workers = workers
    solver.parameters.random_seed = seed
    status = solver.Solve(model)
    report.update({
        "status": solver.StatusName(status),
        "wall_time": solver.WallTime(),
        "branches": solver.NumBranches(),
        "conflicts": solver.NumConflicts(),
    })
    if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        chosen_configurations = [
            configurations[member]
            for index, orbit_column in enumerate(orbit_columns)
            if solver.Value(selected[index])
            for member in orbit_column["members"]
        ]
        assert sum(configuration["kind"] == "self"
                   for configuration in chosen_configurations) == 35
        assert sum(configuration["kind"] == "pair"
                   for configuration in chosen_configurations) == 54
        chosen = [column for configuration in chosen_configurations
                  for column in configuration["columns"]]
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
            "selected_configuration_orbits": sum(
                solver.Value(variable) for variable in selected
            ),
            "selected_self_columns": 35,
            "selected_paired_configurations": 54,
            "selected_rail_orbits": len(chosen),
            "developed_rails": rails,
            "covered_owners": owners,
            "point_degree": sorted(set(point.values())),
            "certificate": [
                {"core": list(column["core"]),
                 "order": list(column["order"]),
                 "quotient_edge": list(column["edge"])}
                for column in normalized
            ],
        })
    print(json.dumps(report, indent=2, sort_keys=True))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--map", required=True)
    parser.add_argument("--multiplier", type=int, default=4)
    parser.add_argument("--time-limit", type=float, default=600)
    parser.add_argument("--workers", type=int, default=32)
    parser.add_argument("--seed", type=int, default=20260814)
    args = parser.parse_args()
    solve(args.map, args.multiplier, args.time_limit, args.workers, args.seed)


if __name__ == "__main__":
    main()
