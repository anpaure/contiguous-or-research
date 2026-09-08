#!/usr/bin/env python3
"""Search the reflection-invariant Z17 q4 owner-cover face.

Run only on H100.  The frozen group-closed period-10 pool supplies paired
columns.  A complete, explicit strong self-reflecting family supplies the
columns needed on the 70 fixed owner bracelets.
"""

from __future__ import annotations

import argparse
import itertools
import json
import sys

from ortools.sat.python import cp_model

sys.path.insert(0, "scratch")
from search_q4_k17_z17_quotient_exact_cover_20260814 import (
    K,
    canonical_orbit_mask,
    deck_masks,
    owner_orbits,
    verify_development,
)


def reflect_mask(mask: int) -> int:
    reflected = 0
    for value in range(K):
        if mask >> value & 1:
            reflected |= 1 << ((-value) % K)
    return canonical_orbit_mask(reflected)


def reflection_action(representatives, orbit_index):
    action = tuple(
        orbit_index[reflect_mask(mask)] for mask in representatives
    )
    assert all(action[action[v]] == v for v in range(len(action)))
    return action


def enumerate_strong_self_columns(orbit_index, reflection):
    """Enumerate invariant-core, reflection-palindromic period-10 rails.

    Translation lets the affine reflection be normalized to x -> -x.
    The invariant five-core is {0,+-a,+-b}.  The ten-label support is five
    further reflection pairs.  If the first half of the cyclic order is
    x1,...,x5, the second half is -x5,...,-x1; reflection reverses the
    order and hence preserves its cyclic four-window deck.
    """
    unique = {}
    raw = 0
    quotient_simple = 0
    pair_labels = tuple(range(1, 9))
    for core_pairs in itertools.combinations(pair_labels, 2):
        core = tuple(sorted(
            (0,) + tuple(
                value
                for pair in core_pairs
                for value in (pair, (-pair) % K)
            )
        ))
        remaining = tuple(x for x in pair_labels if x not in core_pairs)
        for support_pairs in itertools.combinations(remaining, 5):
            for permutation in itertools.permutations(support_pairs):
                for signs in itertools.product((-1, 1), repeat=5):
                    raw += 1
                    first = tuple(
                        (sign * pair) % K
                        for sign, pair in zip(signs, permutation)
                    )
                    order = first + tuple((-x) % K for x in reversed(first))
                    owners = deck_masks(core, order)
                    edge = tuple(sorted(
                        orbit_index[canonical_orbit_mask(owner)]
                        for owner in owners
                    ))
                    if len(set(edge)) != 10:
                        continue
                    quotient_simple += 1
                    reflected_edge = tuple(sorted(reflection[v] for v in edge))
                    assert reflected_edge == edge
                    unique.setdefault(edge, {
                        "core": core,
                        "order": order,
                        "edge": edge,
                    })
    return list(unique.values()), raw, quotient_simple


def paired_columns(pool, reflection):
    edge_index = {
        tuple(candidate["edge"]): index
        for index, candidate in enumerate(pool)
    }
    assert len(edge_index) == len(pool)
    pairs = []
    self_columns = []
    for index, candidate in enumerate(pool):
        edge = tuple(candidate["edge"])
        reflected_edge = tuple(sorted(reflection[v] for v in edge))
        mate = edge_index[reflected_edge]
        if mate == index:
            self_columns.append(index)
        elif index < mate and not (set(edge) & set(pool[mate]["edge"])):
            pairs.append((index, mate))
    return pairs, self_columns


def solve(map_path, time_limit, workers, seed):
    data = json.load(open(map_path, encoding="utf-8"))
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
    pairs, pool_self = paired_columns(data["candidates"], reflection)
    assert not pool_self

    configurations = []
    for candidate in self_candidates:
        # For s_i with -s_i=s_(9-i), reflection sends window start i to
        # 6-i mod 10.  Quotient simplicity therefore leaves exactly the
        # fixed starts i=3,8 and no accidental fixed quotient vertex.
        assert len(set(candidate["edge"]) & fixed) == 2
        reduced_edge = tuple(sorted({
            reduced_index[min(v, reflection[v])]
            for v in candidate["edge"]
        }))
        configurations.append({
            "kind": "self",
            "columns": [candidate],
            "edge": reduced_edge,
        })
    for left, right in pairs:
        columns = [data["candidates"][left], data["candidates"][right]]
        union = set(columns[0]["edge"]) | set(columns[1]["edge"])
        assert len(union) == 20
        reduced_edge = tuple(sorted({
            reduced_index[min(v, reflection[v])] for v in union
        }))
        assert len(reduced_edge) == 10
        configurations.append({
            "kind": "pair",
            "columns": columns,
            "edge": reduced_edge,
        })

    incidence = [[] for _ in orbit_representatives]
    for i, configuration in enumerate(configurations):
        for row in configuration["edge"]:
            incidence[row].append(i)
    fixed_rows = [reduced_index[v] for v in fixed]
    report = {
        "map": map_path,
        "owner_reflection_orbits": len(orbit_representatives),
        "fixed_owner_orbits": len(fixed),
        "raw_self_orders": raw,
        "quotient_simple_self_orders": quotient_simple,
        "unique_strong_self_columns": len(self_candidates),
        "usable_paired_configurations": len(pairs),
        "configurations": len(configurations),
        "min_row_degree": min(map(len, incidence)),
        "max_row_degree": max(map(len, incidence)),
        "min_fixed_row_degree": min(len(incidence[row]) for row in fixed_rows),
        "max_fixed_row_degree": max(len(incidence[row]) for row in fixed_rows),
    }
    if any(not row for row in incidence):
        report["status"] = "UNCOVERED_ROW"
        print(json.dumps(report, indent=2, sort_keys=True))
        return

    model = cp_model.CpModel()
    selected = [model.NewBoolVar(f"configuration_{i}")
                for i in range(len(configurations))]
    for row in incidence:
        model.AddExactlyOne(selected[i] for i in row)
    # The 70 fixed owner bracelets can only be covered by self columns,
    # and every strong self column covers exactly two.  Thus the invariant
    # face has exactly 35 self columns and (143-35)/2=54 paired orbits.
    model.Add(sum(selected[:len(self_candidates)]) == 35)
    model.Add(sum(selected[len(self_candidates):]) == 54)
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = time_limit
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
            configuration for i, configuration in enumerate(configurations)
            if solver.Value(selected[i])
        ]
        chosen = [
            column
            for configuration in chosen_configurations
            for column in configuration["columns"]
        ]
        loads = [0] * 1430
        for column in chosen:
            for vertex in column["edge"]:
                loads[vertex] += 1
        assert set(loads) == {1}
        assert len(chosen) == 143
        normalized = [
            {"core": tuple(column["core"]),
             "order": tuple(column["order"]),
             "edge": tuple(column["edge"])}
            for column in chosen
        ]
        rails, owners, point = verify_development(normalized)
        report.update({
            "selected_configurations": len(chosen_configurations),
            "selected_self_columns": sum(
                configuration["kind"] == "self"
                for configuration in chosen_configurations
            ),
            "selected_paired_configurations": sum(
                configuration["kind"] == "pair"
                for configuration in chosen_configurations
            ),
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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--map", required=True)
    parser.add_argument("--time-limit", type=float, default=600)
    parser.add_argument("--workers", type=int, default=32)
    parser.add_argument("--seed", type=int, default=20260814)
    args = parser.parse_args()
    solve(args.map, args.time_limit, args.workers, args.seed)


if __name__ == "__main__":
    main()
