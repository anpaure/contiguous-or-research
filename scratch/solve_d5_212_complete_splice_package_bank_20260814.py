#!/usr/bin/env python3
"""Closed-box resource-packing precheck for 212 splice packages.

Run on H100 only.  The adjacent and hard rank-7 witnesses are lifted to
rank 11 on 23 coordinates by four common-one and six unused-zero labels.
For each frozen D5 terminal triple, random cell-preserving coordinate
relabelings form a finite exact conflict hypergraph on owner, q1 and q2
resources.  Optional common-core pairs lift the whole finite instance.

This script does *not* compile cut-open D5 wires, refill the removed q1
incidences, or verify the global factor topology.  Even a positive result is
only a closed-box resource-space precheck.  Menu UNSAT is scoped only to the
generated finite menu.
"""

import argparse
import hashlib
import json
import random
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import solve_d5_tapped_c6_212_coinstantiation_20260814 as base_solver  # noqa:E402


BANK_NAMES = base_solver.BANK_NAMES
BASE_GROUND = 23
BASE_RANK = 11


def bitset(values):
    answer = 0
    for value in values:
        answer |= 1 << value
    return answer


def bits_of(value, ground):
    return {i for i in range(ground) if value >> i & 1}


def palettes(cycles, rank):
    result = [[] for _ in BANK_NAMES]
    for cycle in cycles:
        size = len(cycle)
        assert size == len(set(cycle))
        for i, owner in enumerate(cycle):
            one = cycle[(i + 1) % size]
            two = cycle[(i + 2) % size]
            assert len(owner) == rank and len(owner ^ one) == 2
            result[0].append(owner)
            result[1].append(owner & one)
            result[2].append(owner | one)
            result[3].append(owner & one & two)
            result[4].append(owner | one | two)
    return tuple(tuple(values) for values in result)


def package_template(path, expected_kind, lift_t):
    data = json.loads(Path(path).read_text())
    assert data["status"] == "SAT"
    w = data["witness"]
    labels = {i: f"b{i}" for i in range(13)}
    common = {f"g{i}" for i in range(4 + lift_t)}
    unused = {f"v{i}" for i in range(6 + lift_t)}
    universe = set(labels.values()) | common | unused

    def owner(raw):
        return frozenset({labels[i] for i in raw} | common)

    old = tuple(tuple(owner(value) for value in cycle) for cycle in w["old_cycles"])
    new = tuple(tuple(owner(value) for value in cycle) for cycle in w["new_cycles"])
    T = owner(w["terminal_tail"])
    B, C = map(owner, w["terminal_heads"])
    assert T not in {value for cycle in old for value in cycle}
    assert sum(B in cycle for cycle in old) == sum(C in cycle for cycle in old) == 1
    rank = BASE_RANK + lift_t
    ground = BASE_GROUND + 2 * lift_t
    old_banks = palettes(old, rank)
    new_banks = palettes(new, rank)
    assert all(Counter(old_banks[k]) == Counter(new_banks[k]) for k in range(5))
    assert all(len(values) == len(set(values)) == 36 for values in old_banks)
    signature = (
        len(T - B), len(T - C), len(B - C),
        len(T & B & C), len(T | B | C),
    )
    expected = (
        (1, 1, 1, 10 + lift_t, 13 + lift_t)
        if expected_kind == "adjacent"
        else (1, 1, 2, 9 + lift_t, 13 + lift_t)
    )
    assert signature == expected
    assert len(universe) == ground and all(len(value) == rank for cycle in old for value in cycle)
    return {
        "kind": expected_kind,
        "universe": universe,
        "old": old,
        "new": new,
        "T": T,
        "B": B,
        "C": C,
        "banks": old_banks,
        "source_sha256": hashlib.sha256(Path(path).read_bytes()).hexdigest(),
    }


def cells(sets, universe):
    out = defaultdict(list)
    for value in universe:
        out[tuple(value in item for item in sets)].append(value)
    return out


def map_candidate(row, tpl, rng, ground, rank):
    source = cells((tpl["T"], tpl["B"], tpl["C"]), tpl["universe"])
    actual_sets = tuple(bits_of(row[name], ground) for name in ("T", "B", "C"))
    target = cells(actual_sets, range(ground))
    assert {key: len(values) for key, values in source.items()} == {
        key: len(values) for key, values in target.items()
    }
    mapping = {}
    for key, labels in source.items():
        labels = sorted(labels)
        values = list(target[key])
        rng.shuffle(values)
        mapping.update(zip(labels, values))
    assert len(mapping) == len(set(mapping.values())) == ground

    mapped = tuple(
        tuple(frozenset(mapping[label] for label in owner) for owner in cycle)
        for cycle in tpl["old"]
    )
    banks = tuple(
        tuple(bitset(value) for value in values)
        for values in palettes(mapped, rank)
    )
    mapped_t = bitset(mapping[label] for label in tpl["T"])
    mapped_b = bitset(mapping[label] for label in tpl["B"])
    mapped_c = bitset(mapping[label] for label in tpl["C"])
    assert (mapped_t, mapped_b, mapped_c) == (row["T"], row["B"], row["C"])
    typed = (
        tuple(value for value in banks[0] if value not in {row["B"], row["C"]}),
    ) + banks[1:]
    assert len(typed[0]) == 34 and all(len(values) == len(set(values)) for values in typed)
    labels = tuple(sorted(tpl["universe"]))
    return {
        "mapping_labels": labels,
        "mapping": tuple(mapping[label] for label in labels),
        "typed": typed,
    }


def generate(rows, templates, protected, menu_size, attempts_factor, seed, ground, rank):
    menus = []
    diagnostics = []
    for index, row in enumerate(rows):
        rng = random.Random(seed + 104729 * index)
        menu = []
        seen = set()
        rejects = Counter()
        attempts = 0
        while len(menu) < menu_size and attempts < menu_size * attempts_factor:
            attempts += 1
            candidate = map_candidate(row, templates[row["kind"]], rng, ground, rank)
            if candidate["mapping"] in seen:
                rejects["duplicate"] += 1
                continue
            seen.add(candidate["mapping"])
            collision = next((
                BANK_NAMES[k] for k, values in enumerate(candidate["typed"])
                if set(values) & protected["typed"][k]
            ), None)
            if collision:
                rejects[f"protected_{collision}"] += 1
                continue
            menu.append(candidate)
        menus.append(menu)
        diagnostics.append({
            "row": index, "kind": row["kind"], "attempts": attempts,
            "accepted": len(menu), "rejects": dict(sorted(rejects.items())),
        })
    return menus, diagnostics


def greedy(menus, seed, passes):
    best = {}
    for trial in range(passes):
        rng = random.Random(seed + 15485863 * trial)
        order = sorted(range(len(menus)), key=lambda i: (len(menus[i]), rng.random()))
        used = [set() for _ in BANK_NAMES]
        selected = {}
        for row in order:
            options = list(range(len(menus[row])))
            rng.shuffle(options)
            choice = next((option for option in options if all(
                not (set(values) & used[k])
                for k, values in enumerate(menus[row][option]["typed"])
            )), None)
            if choice is None:
                break
            selected[row] = choice
            for k, values in enumerate(menus[row][choice]["typed"]):
                used[k].update(values)
        if len(selected) > len(best):
            best = selected
        if len(best) == len(menus):
            return best, trial + 1
    return best, passes


def exact_select(menus, time_limit, workers):
    from ortools.sat.python import cp_model

    model = cp_model.CpModel()
    variables = [
        [model.NewBoolVar(f"x_{row}_{option}") for option in range(len(menu))]
        for row, menu in enumerate(menus)
    ]
    active = [model.NewBoolVar(f"active_{row}") for row in range(len(menus))]
    resource_users = defaultdict(list)
    for row, menu in enumerate(menus):
        model.Add(sum(variables[row]) == active[row])
        for option, candidate in enumerate(menu):
            var = variables[row][option]
            for bank, values in enumerate(candidate["typed"]):
                for value in values:
                    resource_users[(bank, value)].append(var)
    for users in resource_users.values():
        if len(users) > 1:
            model.AddAtMostOne(users)
    model.AddAssumptions(active)

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = time_limit
    solver.parameters.num_search_workers = workers
    solver.parameters.core_minimization_level = 2
    status = solver.Solve(model)
    stats = {
        "status_name": solver.StatusName(status),
        "wall_time": solver.WallTime(),
        "branches": solver.NumBranches(),
        "conflicts": solver.NumConflicts(),
        "resource_constraints": sum(len(users) > 1 for users in resource_users.values()),
    }
    if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        selected = {
            row: next(option for option, var in enumerate(variables[row]) if solver.Value(var))
            for row in range(len(menus))
        }
        return "SAT", selected, [], stats
    if status == cp_model.INFEASIBLE:
        by_index = {var.Index(): row for row, var in enumerate(active)}
        core = sorted(by_index[index] for index in solver.SufficientAssumptionsForInfeasibility())
        stats["core_is_provably_smallest"] = len(core) == 1
        return "UNSAT", {}, core, stats
    return "UNKNOWN", {}, [], stats


def lift_problem(rows, protected, lift_t):
    if lift_t == 0:
        return rows, protected
    common_mask = bitset(range(BASE_GROUND, BASE_GROUND + lift_t))
    lifted_rows = []
    for row in rows:
        copy = dict(row)
        for name in ("T", "B", "C"):
            copy[name] |= common_mask
        lifted_rows.append(copy)
    lifted_protected = dict(protected)
    lifted_protected["typed"] = tuple(
        {value | common_mask for value in bank} for bank in protected["typed"]
    )
    lifted_protected["counts"] = dict(protected["counts"])
    lifted_protected["counts"]["common_core_pairs"] = lift_t
    return lifted_rows, lifted_protected


def verify(rows, menus, selected, protected):
    assert len(selected) == len(rows)
    used = [set() for _ in BANK_NAMES]
    for row, option in sorted(selected.items()):
        candidate = menus[row][option]
        for k, values in enumerate(candidate["typed"]):
            assert not (set(values) & protected["typed"][k])
            assert not (set(values) & used[k])
            used[k].update(values)
    return dict(zip(BANK_NAMES, map(len, used)))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("selection")
    parser.add_argument("certificate")
    parser.add_argument("adjacent_witness")
    parser.add_argument("hard_witness")
    parser.add_argument("--menu-size", type=int, default=32)
    parser.add_argument("--attempts-factor", type=int, default=2000)
    parser.add_argument("--passes", type=int, default=200)
    parser.add_argument("--common-core-pairs", type=int, default=0)
    parser.add_argument("--exact-time-limit", type=float, default=300.0)
    parser.add_argument("--workers", type=int, default=32)
    parser.add_argument("--seed", type=int, default=20260814)
    args = parser.parse_args()
    selection = json.loads(Path(args.selection).read_text())
    certificate = json.loads(Path(args.certificate).read_text())
    rows, old, new = base_solver.extract_rows(selection, certificate)
    protected = base_solver.protected_banks(rows, old, new)
    rows, protected = lift_problem(rows, protected, args.common_core_pairs)
    ground = BASE_GROUND + 2 * args.common_core_pairs
    rank = BASE_RANK + args.common_core_pairs
    templates = {
        "adjacent": package_template(
            args.adjacent_witness, "adjacent", args.common_core_pairs
        ),
        "distance_two": package_template(
            args.hard_witness, "distance_two", args.common_core_pairs
        ),
    }
    menus, diagnostics = generate(
        rows, templates, protected, args.menu_size, args.attempts_factor,
        args.seed, ground, rank,
    )
    greedy_selected, trials = greedy(menus, args.seed + 1, args.passes)
    exact_status, exact_selected, core, exact_stats = exact_select(
        menus, args.exact_time_limit, args.workers
    )
    selected = exact_selected if exact_status == "SAT" else greedy_selected
    status = {
        "SAT": "PRECHECK_SAT",
        "UNSAT": "FINITE_MENU_UNSAT",
        "UNKNOWN": "MENU_UNRESOLVED",
    }[exact_status]
    counts = (
        verify(rows, menus, selected, protected)
        if status == "PRECHECK_SAT" else None
    )
    result = {
        "status": status,
        "scope": (
            "closed-box resource-packing precheck only; does not reconnect "
            "cut-open D5 darts, refill deleted q1 incidences, or verify global "
            "component topology"
        ),
        "rank_ground": [rank, ground],
        "common_core_pairs": args.common_core_pairs,
        "template_sha256": {key: value["source_sha256"] for key, value in templates.items()},
        "menu_size_histogram": dict(sorted(Counter(map(len, menus)).items())),
        "kind_histogram": dict(sorted(Counter(row["kind"] for row in rows).items())),
        "protected": protected["counts"],
        "rows_selected": len(selected),
        "greedy_trials": trials,
        "greedy_rows_selected": len(greedy_selected),
        "exact_solver": exact_stats,
        "unsat_core_rows": core,
        "unsat_core": [
            {
                "row": row,
                "source_row": rows[row]["source_row"],
                "kind": rows[row]["kind"],
                "accepted_menu_size": len(menus[row]),
            }
            for row in core
        ],
        "selected_resource_counts": counts,
        "diagnostics": diagnostics,
        "chosen": [] if status != "PRECHECK_SAT" else [
            {
                "row": row,
                "source_row": rows[row]["source_row"],
                "kind": rows[row]["kind"],
                "T": base_solver.base.bitword(rows[row]["T"], ground),
                "B": base_solver.base.bitword(rows[row]["B"], ground),
                "C": base_solver.base.bitword(rows[row]["C"], ground),
                "mapping_labels": menus[row][option]["mapping_labels"],
                "mapping": menus[row][option]["mapping"],
            }
            for row, option in sorted(selected.items())
        ],
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    if status != "PRECHECK_SAT":
        raise SystemExit(2)


if __name__ == "__main__":
    main()
