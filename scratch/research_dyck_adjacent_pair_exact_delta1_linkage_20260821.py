#!/usr/bin/env python3
"""CP-SAT search for simultaneous exact-delta-one mirrored phase linkage.

Research diagnostic; substantive runs are on H100 only.
"""

from __future__ import annotations

import argparse
from collections import Counter
from itertools import combinations
from math import comb

import networkx as nx
from ortools.sat.python import cp_model

from research_c8_orbit_phase_normal_form_20260821 import canonical_layers


def ordered(values):
    return tuple(sorted(values, key=lambda x: tuple(sorted(x))))


def adjacent_matching(roots):
    graph = nx.Graph()
    graph.add_nodes_from(roots)
    root_set = set(roots)
    for left in roots:
        for deleted in left:
            for added in (deleted - 1, deleted + 1):
                if added <= 0 or added in left:
                    continue
                right = frozenset((left - {deleted}) | {added})
                if right in root_set:
                    graph.add_edge(left, right)
    matching = nx.max_weight_matching(graph, maxcardinality=True)
    assert 2 * len(matching) == len(roots)
    return tuple(matching), graph.number_of_edges()


def solve(r, seconds, workers, exact_palette, maximize_palette, dump_paths=False):
    assert r % 2 == 0
    h = r // 2
    ground = frozenset(range(1, 2 * r + 1))
    layer, _, sizes = canonical_layers(r)
    assert set(sizes.values()) == {comb(2 * r, r) // (r + 1)}
    by_phase = {
        phase: ordered(x for x, value in layer.items() if value == phase)
        for phase in range(h + 1)
    }
    m = len(by_phase[0])
    index = {
        phase: {target: i for i, target in enumerate(by_phase[phase])}
        for phase in range(h + 1)
    }
    matching, root_edge_count = adjacent_matching(by_phase[0])
    root_index = index[0]

    colors = tuple(frozenset(x) for x in combinations(sorted(ground), r - 1))
    color_index = {color: i for i, color in enumerate(colors)}
    allowed = {}
    for phase in range(h):
        rows = []
        for left_index, left in enumerate(by_phase[phase]):
            for deleted in left:
                for added in ground - left:
                    right = frozenset((left - {deleted}) | {added})
                    if right not in index[phase + 1]:
                        continue
                    rows.append(
                        (
                            left_index,
                            index[phase + 1][right],
                            deleted,
                            added,
                            color_index[left & right],
                            color_index[ground - (left | right)],
                        )
                    )
        allowed[phase] = tuple(rows)

    model = cp_model.CpModel()
    position = {
        (root, phase): model.new_int_var(0, m - 1, f"p_{root}_{phase}")
        for root in range(m)
        for phase in range(h + 1)
    }
    changed = {
        (root, phase, x): model.new_bool_var(f"z_{root}_{phase}_{x}")
        for root in range(m)
        for phase in range(h)
        for x in ground
    }
    palette = []
    for root in range(m):
        model.add(position[root, 0] == root)
        for phase in range(h):
            deleted = model.new_int_var(1, 2 * r, f"d_{root}_{phase}")
            added = model.new_int_var(1, 2 * r, f"a_{root}_{phase}")
            lower = model.new_int_var(0, len(colors) - 1, f"lo_{root}_{phase}")
            upper = model.new_int_var(0, len(colors) - 1, f"up_{root}_{phase}")
            model.add_allowed_assignments(
                (position[root, phase], position[root, phase + 1], deleted, added, lower, upper),
                allowed[phase],
            )
            for x in ground:
                model.add_allowed_assignments(
                    (deleted, added, changed[root, phase, x]),
                    tuple(
                        (d, a, int(x in (d, a)))
                        for d in ground
                        for a in ground
                        if d != a
                    ),
                )
            palette.extend((lower, upper))
    for phase in range(h + 1):
        model.add_all_different(position[root, phase] for root in range(m))
    if exact_palette:
        assert len(palette) == len(colors)
        model.add_all_different(palette)
    if maximize_palette:
        assert not exact_palette
        assert len(palette) == len(colors)
        representatives = []
        decorated = []
        color_count = len(colors)
        for occurrence, value in enumerate(palette):
            selected = model.new_bool_var(f"palette_representative_{occurrence}")
            representative = model.new_int_var(
                0, 2 * color_count - 1, f"decorated_palette_{occurrence}"
            )
            model.add(representative == value).only_enforce_if(selected)
            model.add(representative == color_count + occurrence).only_enforce_if(
                selected.Not()
            )
            representatives.append(selected)
            decorated.append(representative)
        # Selected occurrences must have distinct real colours; every
        # unselected occurrence receives its own private dummy colour.
        # Maximizing selected occurrences is therefore exactly maximizing
        # the support size of the physical palette.
        model.add_all_different(decorated)
        model.maximize(sum(representatives))

    middle_complement = tuple(
        (left, index[h][ground - target])
        for left, target in enumerate(by_phase[h])
    )
    for P, Q in matching:
        p = root_index[P]
        q = root_index[Q]
        model.add_allowed_assignments(
            (position[p, h], position[q, h]), middle_complement
        )
        u = next(iter(P - Q))
        v = next(iter(Q - P))
        orientation = model.new_bool_var(f"orientation_{p}_{q}")
        for x in ground:
            total = sum(changed[p, phase, x] + changed[q, phase, x] for phase in range(h))
            if x == u:
                model.add(total == 2 * orientation)
            elif x == v:
                model.add(total == 2 * (1 - orientation))
            else:
                model.add(total == 1)

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = seconds
    solver.parameters.num_search_workers = workers
    status = solver.solve(model)
    result = {
        "r": r,
        "m": m,
        "root_adjacent_edges": root_edge_count,
        "status": solver.status_name(status),
        "wall_time": solver.wall_time,
        "branches": solver.num_branches,
        "conflicts": solver.num_conflicts,
        "exact_palette": exact_palette,
        "maximize_palette": maximize_palette,
    }
    if status not in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        return result
    if maximize_palette:
        result["palette_objective"] = solver.objective_value
        result["palette_best_bound"] = solver.best_objective_bound
    paths = {
        root: tuple(
            by_phase[phase][solver.value(position[root, phase])]
            for phase in range(h + 1)
        )
        for root in range(m)
    }
    defect_hist = Counter()
    palette_load = Counter()
    seen = set()
    for root, path in paths.items():
        for left, right in zip(path, path[1:]):
            palette_load[left & right] += 1
            palette_load[ground - (left | right)] += 1
    for P, Q in matching:
        p, q = root_index[P], root_index[Q]
        assert paths[q][-1] == ground - paths[p][-1]
        full = paths[p] + tuple(
            ground - paths[q][h - step] for step in range(1, h + 1)
        )
        counts = Counter()
        for left, right in zip(full, full[1:]):
            counts.update(left ^ right)
        defect = sum(max(0, value - 1) for value in counts.values())
        defect_hist[defect] += 1
        assert defect == 1
        seen.update((p, q))
    result.update(
        {
            "verified_paths": len(paths),
            "verified_pairs": len(matching),
            "defect_hist": dict(defect_hist),
            "palette_support": len(palette_load),
            "palette_holes": len(colors) - len(palette_load),
            "palette_max_load": max(palette_load.values()),
        }
    )
    if dump_paths:
        result["matching"] = tuple(
            ("".join("1" if i in P else "0" for i in sorted(ground)),
             "".join("1" if i in Q else "0" for i in sorted(ground)))
            for P, Q in matching
        )
        result["paths"] = {
            "".join("1" if i in by_phase[0][root] else "0" for i in sorted(ground)):
            tuple(
                "".join("1" if i in target else "0" for i in sorted(ground))
                for target in path
            )
            for root, path in paths.items()
        }
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--r", type=int, nargs="+", default=[2, 4, 6])
    parser.add_argument("--seconds", type=float, default=300.0)
    parser.add_argument("--workers", type=int, default=32)
    parser.add_argument("--exact-palette", action="store_true")
    parser.add_argument("--maximize-palette", action="store_true")
    parser.add_argument("--dump-paths", action="store_true")
    args = parser.parse_args()
    for r in args.r:
        print(
            "DYCK_ADJACENT_PAIR_EXACT_DELTA1_LINKAGE",
            solve(
                r,
                args.seconds,
                args.workers,
                args.exact_palette,
                args.maximize_palette,
                args.dump_paths,
            ),
            flush=True,
        )


if __name__ == "__main__":
    main()
