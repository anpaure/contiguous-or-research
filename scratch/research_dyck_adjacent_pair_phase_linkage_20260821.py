#!/usr/bin/env python3
"""CP-SAT diagnostic for adjacent-Dyck paired Chung--Feller linkage.

For even ``r`` we first find a perfect matching ``tau`` of the Dyck roots
using adjacent bit transpositions.  We then ask for vertex-disjoint Johnson
paths through the canonical flaw layers D^0,...,D^(r/2) such that paired
roots finish at complementary middle vertices.  Equivalently, if ``G`` is
the induced first-half bijection, the endpoint constraint is

    G(tau(P)) = complement(G(P)).

This is a finite research diagnostic, not a proof.  Substantive runs belong
on H100.
"""

from __future__ import annotations

import argparse
from collections import Counter
from itertools import combinations
from math import comb

import networkx as nx
from ortools.sat.python import cp_model

from research_c8_orbit_phase_normal_form_20260821 import canonical_layers
from research_mirrored_double_cycle_recut_20260821 import canonical_root_paths


def ordered_sets(values):
    return tuple(sorted(values, key=lambda x: tuple(sorted(x))))


def dyck_adjacent_matching(roots):
    graph = nx.Graph()
    graph.add_nodes_from(roots)
    for left in roots:
        for i in left:
            if i + 1 not in left:
                right = frozenset((left - {i}) | {i + 1})
                if right in graph:
                    graph.add_edge(left, right)
        for i in left:
            if i - 1 not in left:
                right = frozenset((left - {i}) | {i - 1})
                if right in graph:
                    graph.add_edge(left, right)
    matching = nx.algorithms.matching.max_weight_matching(graph, maxcardinality=True)
    assert 2 * len(matching) == len(roots), (len(roots), len(matching))
    tau = {}
    for left, right in matching:
        assert len(left ^ right) == 2
        removed = tuple(left - right)
        added = tuple(right - left)
        assert abs(removed[0] - added[0]) == 1
        tau[left] = right
        tau[right] = left
    return tau, graph.number_of_edges()


def solve(r, seconds, workers, fix_prefix, exact_palette, maximize_palette):
    assert r % 2 == 0
    ground = frozenset(range(1, 2 * r + 1))
    layer, _, counts = canonical_layers(r)
    h = r // 2
    by_layer = {
        phase: ordered_sets(x for x, value in layer.items() if value == phase)
        for phase in range(h + 1)
    }
    assert set(counts.values()) == {comb(2 * r, r) // (r + 1)}
    roots = by_layer[0]
    m = len(roots)
    assert m % 2 == 0
    tau, root_edges = dyck_adjacent_matching(roots)

    indices = {
        phase: {target: index for index, target in enumerate(by_layer[phase])}
        for phase in range(h + 1)
    }
    allowed = {}
    colors = tuple(frozenset(value) for value in combinations(sorted(ground), r - 1))
    color_index = {value: index for index, value in enumerate(colors)}
    allowed_with_colors = {}
    for phase in range(h):
        pairs = []
        next_index = indices[phase + 1]
        for left_index, left in enumerate(by_layer[phase]):
            for drop in left:
                for add in ground - left:
                    right = frozenset((left - {drop}) | {add})
                    if right in next_index:
                        pairs.append((left_index, next_index[right]))
        allowed[phase] = sorted(set(pairs))
        allowed_with_colors[phase] = [
            (
                left_index,
                right_index,
                color_index[by_layer[phase][left_index] & by_layer[phase + 1][right_index]],
                color_index[
                    ground
                    - (
                        by_layer[phase][left_index]
                        | by_layer[phase + 1][right_index]
                    )
                ],
            )
            for left_index, right_index in allowed[phase]
        ]

    model = cp_model.CpModel()
    position = {
        (root_index, phase): model.new_int_var(
            0, m - 1, f"p_{root_index}_{phase}"
        )
        for root_index in range(m)
        for phase in range(h + 1)
    }
    for root_index in range(m):
        model.add(position[root_index, 0] == root_index)
    if fix_prefix:
        canonical = canonical_root_paths(r)
        for root_index_value, root in enumerate(roots):
            for phase in range(min(fix_prefix, h) + 1):
                model.add(
                    position[root_index_value, phase]
                    == indices[phase][canonical[root][phase]]
                )
    for phase in range(h + 1):
        model.add_all_different(position[root_index, phase] for root_index in range(m))
    for root_index in range(m):
        for phase in range(h):
            model.add_allowed_assignments(
                (position[root_index, phase], position[root_index, phase + 1]),
                allowed[phase],
            )
    palette_variables = []
    if exact_palette or maximize_palette:
        for root_index in range(m):
            for phase in range(h):
                lower = model.new_int_var(0, len(colors) - 1, f"lo_{root_index}_{phase}")
                upper = model.new_int_var(0, len(colors) - 1, f"up_{root_index}_{phase}")
                model.add_allowed_assignments(
                    (
                        position[root_index, phase],
                        position[root_index, phase + 1],
                        lower,
                        upper,
                    ),
                    allowed_with_colors[phase],
                )
                palette_variables.extend((lower, upper))
        assert len(palette_variables) == len(colors)
        if exact_palette:
            model.add_all_different(palette_variables)
        else:
            kept = []
            representatives = []
            for index, color in enumerate(palette_variables):
                use_real = model.new_bool_var(f"keep_color_{index}")
                representative = model.new_int_var(
                    0, len(colors) + len(palette_variables) - 1, f"rep_{index}"
                )
                model.add(representative == color).only_enforce_if(use_real)
                model.add(representative == len(colors) + index).only_enforce_if(
                    use_real.Not()
                )
                kept.append(use_real)
                representatives.append(representative)
            model.add_all_different(representatives)
            model.maximize(sum(kept))

    middle_complement = [
        indices[h][ground - target] for target in by_layer[h]
    ]
    complement_pairs = [(index, mate) for index, mate in enumerate(middle_complement)]
    phase_pair_tables = {}
    for phase in range(1, h):
        permitted_distances = {2 * phase, 2 * phase + 1}
        phase_pair_tables[phase] = [
            (i, j)
            for i, left in enumerate(by_layer[phase])
            for j, right in enumerate(by_layer[phase])
            if len(left - right) in permitted_distances
        ]
    root_index = indices[0]
    used_pairs = set()
    for root in roots:
        mate = tau[root]
        a, b = root_index[root], root_index[mate]
        if min(a, b) in used_pairs:
            continue
        used_pairs.add(min(a, b))
        model.add_allowed_assignments(
            (position[a, h], position[b, h]), complement_pairs
        )
        for phase in range(1, h):
            model.add_allowed_assignments(
                (position[a, phase], position[b, phase]),
                phase_pair_tables[phase],
            )

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = seconds
    solver.parameters.num_search_workers = workers
    solver.parameters.log_search_progress = False
    status = solver.solve(model)
    result = {
        "r": r,
        "m": m,
        "root_adjacent_edges": root_edges,
        "transition_edge_counts": [len(allowed[t]) for t in range(h)],
        "status": solver.status_name(status),
        "wall_time": solver.wall_time,
        "branches": solver.num_branches,
        "conflicts": solver.num_conflicts,
        "fixed_prefix_phases": min(fix_prefix, h),
        "exact_palette_requested": exact_palette,
        "maximize_palette_requested": maximize_palette,
    }
    if status not in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        return result

    paths = {}
    endpoint_distance = Counter()
    swap_defect = Counter()
    pair_distance_sequences = Counter()
    palette_count = Counter()
    seen = set()
    for root_index_value, root in enumerate(roots):
        path = tuple(
            by_layer[phase][solver.value(position[root_index_value, phase])]
            for phase in range(h + 1)
        )
        paths[root] = path
        for left, right in zip(path, path[1:]):
            palette_count[left & right] += 1
            palette_count[ground - (left | right)] += 1
    for root in roots:
        mate = tau[root]
        if root in seen:
            continue
        seen.update((root, mate))
        assert paths[mate][-1] == ground - paths[root][-1]
        pair_distance_sequences[
            tuple(len(paths[root][phase] - paths[mate][phase]) for phase in range(h + 1))
        ] += 1
        full = paths[root] + tuple(
            ground - paths[mate][h - step] for step in range(1, h + 1)
        )
        assert len(full) == r + 1
        assert full[-1] == ground - mate
        assert all(len(left ^ right) == 2 for left, right in zip(full, full[1:]))
        endpoint_distance[len(root - mate)] += 1
        counts_by_label = Counter()
        for left, right in zip(full, full[1:]):
            counts_by_label.update(left - right)
            counts_by_label.update(right - left)
        defect = sum(max(value - 1, 0) for value in counts_by_label.values())
        swap_defect[defect] += 1
        assert defect <= 2
    result.update(
        {
            "verified_pairs": len(seen) // 2,
            "endpoint_distance_hist": dict(endpoint_distance),
            "swap_defect_hist": dict(swap_defect),
            "pair_distance_sequences": {
                str(key): value for key, value in pair_distance_sequences.items()
            },
            "palette_distinct": len(palette_count),
            "palette_holes": len(colors) - len(palette_count),
            "palette_max_load": max(palette_count.values()),
            "palette_load_hist": dict(Counter(palette_count.values())),
        }
    )
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--r", type=int, nargs="+", default=[2, 4, 6])
    parser.add_argument("--seconds", type=float, default=300.0)
    parser.add_argument("--workers", type=int, default=32)
    parser.add_argument("--fix-prefix", type=int, default=0)
    parser.add_argument("--exact-palette", action="store_true")
    parser.add_argument("--maximize-palette", action="store_true")
    args = parser.parse_args()
    for r in args.r:
        print(
            "DYCK_ADJACENT_PAIR_PHASE_LINKAGE",
            solve(
                r,
                args.seconds,
                args.workers,
                args.fix_prefix,
                args.exact_palette,
                args.maximize_palette,
            ),
            flush=True,
        )


if __name__ == "__main__":
    main()
