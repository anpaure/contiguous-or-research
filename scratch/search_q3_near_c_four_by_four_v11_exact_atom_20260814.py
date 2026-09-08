#!/usr/bin/env python3
"""Search the exact q=3 four-by-four near-C atom on 11 reduced labels.

All substantive runs belong on H100.  The support layer enforces the exact
point-degree equations.  The full layer represents each rail by one directed
cycle (self loops mark support holes), derives every cyclic 3-window, and
requires simple positive/negative owner decks with

    positive owners = negative owners + {0,1,2,3}.
"""

from __future__ import annotations

import argparse
import itertools
import json
from collections import Counter

from ortools.sat.python import cp_model


V = tuple(range(11))
TARGET = frozenset(range(4))
TARGET_MASK = sum(1 << x for x in TARGET)

CENTER_CASES = {
    "same_target": (1, 1),
    "two_targets": (1, 2),
    "target_exterior": (1, 4),
    "same_exterior": (4, 4),
    "two_exteriors": (4, 5),
}


def rails_for(case):
    long_centres = CENTER_CASES[case]
    return [
        {"name": "p8a", "sign": 1, "period": 8, "center": 0},
        {"name": "p8b", "sign": 1, "period": 8, "center": 0},
        {"name": "p9a", "sign": 1, "period": 9, "center": long_centres[0]},
        {"name": "p9b", "sign": 1, "period": 9, "center": long_centres[1]},
        {"name": "n9", "sign": -1, "period": 9, "center": 0},
        {"name": "n8a", "sign": -1, "period": 8, "center": 1},
        {"name": "n8b", "sign": -1, "period": 8, "center": 2},
        {"name": "n8c", "sign": -1, "period": 8, "center": 3},
    ]


def mask(values):
    return sum(1 << value for value in values)


def decode(value):
    return [x for x in V if (value >> x) & 1]


def owner_deck(rail, cycle):
    n = len(cycle)
    return [
        frozenset((rail["center"], cycle[i], cycle[(i + 1) % n],
                   cycle[(i + 2) % n]))
        for i in range(n)
    ]


def build_model(case, full):
    rails = rails_for(case)
    model = cp_model.CpModel()
    selected = {}
    for r, rail in enumerate(rails):
        for x in V:
            selected[r, x] = model.NewBoolVar(f"sel_{rail['name']}_{x}")
            if x == rail["center"]:
                model.Add(selected[r, x] == 0)
        model.Add(sum(selected[r, x] for x in V) == rail["period"])

    # Exact point-degree equations: a centre contributes its whole period;
    # every selected toggle contributes exactly three cyclic windows.
    for x in V:
        terms = []
        for r, rail in enumerate(rails):
            if rail["center"] == x:
                terms.append(rail["sign"] * rail["period"])
            else:
                terms.append(rail["sign"] * 3 * selected[r, x])
        model.Add(sum(terms) == (1 if x in TARGET else 0))

    # Exchange identical rails only once at the support level.
    support_code = {
        r: sum((1 << x) * (1 - selected[r, x]) for x in V)
        for r in range(len(rails))
    }
    model.Add(support_code[0] <= support_code[1])
    if rails[2]["center"] == rails[3]["center"]:
        model.Add(support_code[2] <= support_code[3])

    arcs = {}
    occurrence = {}
    if full:
        for r, rail in enumerate(rails):
            center = rail["center"]
            circuit = []
            for u in V:
                self_arc = model.NewBoolVar(f"self_{rail['name']}_{u}")
                model.Add(self_arc + selected[r, u] == 1)
                circuit.append((u, u, self_arc))
            for u in V:
                if u == center:
                    continue
                for v in V:
                    if v == center or v == u:
                        continue
                    arc = model.NewBoolVar(f"arc_{rail['name']}_{u}_{v}")
                    arcs[r, u, v] = arc
                    model.Add(arc <= selected[r, u])
                    model.Add(arc <= selected[r, v])
                    circuit.append((u, v, arc))
            model.AddCircuit(circuit)

            paths = {}
            labels = [x for x in V if x != center]
            for u, v, w in itertools.permutations(labels, 3):
                path = model.NewBoolVar(f"path_{rail['name']}_{u}_{v}_{w}")
                model.Add(path <= arcs[r, u, v])
                model.Add(path <= arcs[r, v, w])
                model.Add(path >= arcs[r, u, v] + arcs[r, v, w] - 1)
                paths[u, v, w] = path

            for triple in itertools.combinations(labels, 3):
                owner = frozenset((center, *triple))
                occ = model.NewBoolVar(
                    f"occ_{rail['name']}_{'_'.join(map(str, sorted(owner)))}"
                )
                model.Add(occ == sum(paths[order] for order in itertools.permutations(triple)))
                occurrence[r, owner] = occ
            model.Add(sum(
                value for (rail_index, _), value in occurrence.items()
                if rail_index == r
            ) == rail["period"])

        all_owners = [frozenset(owner) for owner in itertools.combinations(V, 4)]
        for owner in all_owners:
            positive = [
                occurrence[r, owner] for r, rail in enumerate(rails)
                if rail["sign"] == 1 and (r, owner) in occurrence
            ]
            negative = [
                occurrence[r, owner] for r, rail in enumerate(rails)
                if rail["sign"] == -1 and (r, owner) in occurrence
            ]
            model.Add(sum(positive) <= 1)
            model.Add(sum(negative) <= 1)
            model.Add(sum(positive) - sum(negative) == (1 if owner == TARGET else 0))

        # The two identical positive short rails can be exchanged.  If one
        # of them carries the unmatched target owner, call it p8a.
        model.Add(occurrence[0, TARGET] >= occurrence[1, TARGET])

    return model, rails, selected, arcs


def solve(case, mode, seconds, workers, seed, log_search):
    full = mode == "full"
    model, rails, selected, arcs = build_model(case, full)
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = seconds
    solver.parameters.num_search_workers = workers
    solver.parameters.random_seed = seed
    solver.parameters.log_search_progress = log_search
    status = solver.Solve(model)
    result = {
        "case": case,
        "mode": mode,
        "status": solver.StatusName(status),
        "wall_time": solver.WallTime(),
        "branches": solver.NumBranches(),
        "conflicts": solver.NumConflicts(),
    }
    if status not in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        return result

    support = {}
    cycles = {}
    for r, rail in enumerate(rails):
        values = [x for x in V if solver.Value(selected[r, x])]
        support[rail["name"]] = values
        if full:
            start = min(values)
            cycle = [start]
            current = start
            while True:
                successor = next(
                    v for v in values if v != current
                    and solver.Value(arcs[r, current, v])
                )
                if successor == start:
                    break
                assert successor not in cycle
                cycle.append(successor)
                current = successor
            assert len(cycle) == rail["period"]
            cycles[rail["name"]] = cycle

    result["supports"] = support
    result["holes"] = {
        rail["name"]: [x for x in V if x != rail["center"] and x not in support[rail["name"]]]
        for rail in rails
    }

    # Independent direct verification of point degrees and, in full mode,
    # every named-owner equality and simplicity assertion.
    point = Counter()
    for rail in rails:
        point[rail["center"]] += rail["sign"] * rail["period"]
        for x in support[rail["name"]]:
            point[x] += rail["sign"] * 3
    assert [point[x] for x in V] == [1, 1, 1, 1] + [0] * 7
    if full:
        positive = Counter()
        negative = Counter()
        for rail in rails:
            deck = owner_deck(rail, cycles[rail["name"]])
            assert len(deck) == rail["period"] == len(set(deck))
            target = positive if rail["sign"] == 1 else negative
            target.update(deck)
        assert all(value == 1 for value in positive.values())
        assert all(value == 1 for value in negative.values())
        difference = positive.copy()
        difference.subtract(negative)
        assert {owner: value for owner, value in difference.items() if value} == {TARGET: 1}
        result["cycles"] = cycles
        result["positive_owner_count"] = sum(positive.values())
        result["negative_owner_count"] = sum(negative.values())
        result["common_owner_count"] = len(set(positive) & set(negative))
        result["target_owner"] = sorted(TARGET)
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--case", choices=["all", *CENTER_CASES], default="all")
    parser.add_argument("--mode", choices=["support", "full"], default="support")
    parser.add_argument("--time-limit", type=float, default=300.0)
    parser.add_argument("--workers", type=int, default=32)
    parser.add_argument("--seed", type=int, default=20260814)
    parser.add_argument("--log-search", action="store_true")
    args = parser.parse_args()
    cases = CENTER_CASES if args.case == "all" else (args.case,)
    reports = [
        solve(case, args.mode, args.time_limit, args.workers, args.seed,
              args.log_search)
        for case in cases
    ]
    print(json.dumps({"status": "PASS", "reports": reports}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
