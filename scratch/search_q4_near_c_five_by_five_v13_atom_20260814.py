#!/usr/bin/env python3
"""Search the first q=4 five-by-five near-C atom on 13 labels.

Substantive runs belong on H100.  This searches the net-mass-four Profile-I
branch forced by the q=4 centre character, plus one cancelling rail on each
shore in the same centre/period class.  The support layer enforces exact
point degrees.  The full layer represents every rail by a directed cycle,
derives all cyclic 4-windows, and requires

    positive owner deck = negative owner deck + {0,1,2,3,4}

with each shore simple.
"""

from __future__ import annotations

import argparse
import itertools
import json
from collections import Counter, defaultdict

from ortools.sat.python import cp_model


V = tuple(range(13))
TARGET = frozenset(range(5))

# Profile I target types:
#   A=(-1,+1,t=0) at 0,1;
#   B=(+1,+1,t=-5) at 2;
#   C=(0,-1,t=+3) at 3,4.
# The extra cancelling centre is reduced by symmetry to one representative
# of A/B/C/exterior.
CANCEL_CENTRES = {"A": 0, "B": 2, "C": 3, "X": 5}

# Every no-cancellation (net centre mass five) profile allowed by the exact
# point equation and |toggle imbalance| <= 5.  Entries are (a,b) short/long
# signed centre counts.  Exterior states, if any, follow the five targets.
MASS5_PROFILES = (
    (((-3, 1), (0, -1), (0, -1), (1, 1), (1, 1)), ()),
    (((-2, 3), (0, -1), (0, -1), (0, -1), (1, 1)), ()),
    (((-1, 1), (-1, 1), (-1, 1), (0, -1), (0, -1)), ((2, 0),)),
    (((-1, 1), (-1, 1), (-1, 1), (0, -1), (2, -1)), ()),
    (((-1, 1), (0, -1), (0, -1), (0, -1), (1, 1)), ((-1, 2),)),
    (((-1, 1), (0, -1), (0, -1), (1, 1), (1, 1)), ((-2, 0),)),
)


def rails_for(cancel_period: int, cancel_type: str):
    centre = CANCEL_CENTRES[cancel_type]
    rails = [
        {"name": "p10B", "sign": 1, "period": 10, "center": 2},
        {"name": "p11A0", "sign": 1, "period": 11, "center": 0},
        {"name": "p11A1", "sign": 1, "period": 11, "center": 1},
        {"name": "p11B", "sign": 1, "period": 11, "center": 2},
        {"name": f"p{cancel_period}{cancel_type}", "sign": 1,
         "period": cancel_period, "center": centre},
        {"name": "n10A0", "sign": -1, "period": 10, "center": 0},
        {"name": "n10A1", "sign": -1, "period": 10, "center": 1},
        {"name": "n11C3", "sign": -1, "period": 11, "center": 3},
        {"name": "n11C4", "sign": -1, "period": 11, "center": 4},
        {"name": f"n{cancel_period}{cancel_type}", "sign": -1,
         "period": cancel_period, "center": centre},
    ]
    assert sum(r["period"] for r in rails if r["sign"] == 1) == 1 + sum(
        r["period"] for r in rails if r["sign"] == -1
    )
    return rails


def rails_for_mass5(profile_index: int):
    target_states, exterior_states = MASS5_PROFILES[profile_index - 1]
    states = list(enumerate(target_states)) + [
        (5 + j, state) for j, state in enumerate(exterior_states)
    ]
    rails = []
    serial = defaultdict(int)
    for centre, (short, long) in states:
        for period, signed_count in ((10, short), (11, long)):
            sign = 1 if signed_count > 0 else -1
            for _ in range(abs(signed_count)):
                key = (sign, period, centre)
                serial[key] += 1
                rails.append({
                    "name": f"{'p' if sign > 0 else 'n'}{period}c{centre}_{serial[key]}",
                    "sign": sign,
                    "period": period,
                    "center": centre,
                })
    assert len([r for r in rails if r["sign"] == 1]) == 5
    assert len([r for r in rails if r["sign"] == -1]) == 5
    assert sum(r["period"] for r in rails if r["sign"] == 1) == 1 + sum(
        r["period"] for r in rails if r["sign"] == -1
    )
    return rails


def owner_deck(rail, cycle):
    n = len(cycle)
    return [
        frozenset((rail["center"], *(cycle[(i + j) % n] for j in range(4))))
        for i in range(n)
    ]


def and_var(model, variables, name):
    out = model.NewBoolVar(name)
    for value in variables:
        model.Add(out <= value)
    model.Add(out >= sum(variables) - len(variables) + 1)
    return out


def build_model(rails, full, fixed_supports=None):
    model = cp_model.CpModel()
    selected = {}
    for r, rail in enumerate(rails):
        for x in V:
            selected[r, x] = model.NewBoolVar(f"sel_{rail['name']}_{x}")
            if x == rail["center"]:
                model.Add(selected[r, x] == 0)
            if fixed_supports is not None:
                model.Add(selected[r, x] == int(x in fixed_supports[rail["name"]]))
        model.Add(sum(selected[r, x] for x in V) == rail["period"])

    # Exact point-degree current.  A centre occurs in every owner of its
    # rail; every selected toggle occurs in exactly q=4 cyclic windows.
    for x in V:
        terms = []
        for r, rail in enumerate(rails):
            if rail["center"] == x:
                terms.append(rail["sign"] * rail["period"])
            else:
                terms.append(rail["sign"] * 4 * selected[r, x])
        model.Add(sum(terms) == (1 if x in TARGET else 0))

    # Exchange truly identical rail slots only once at support level.
    groups = defaultdict(list)
    for r, rail in enumerate(rails):
        groups[(rail["sign"], rail["period"], rail["center"])].append(r)
    support_code = {
        r: sum((1 << x) * (1 - selected[r, x]) for x in V)
        for r in range(len(rails))
    }
    for group in groups.values():
        for left, right in zip(group, group[1:]):
            model.Add(support_code[left] <= support_code[right])

    # Labels outside the target and the chosen centre set are completely
    # interchangeable.  Sort their rail-hole incidence columns to quotient
    # this factorial symmetry exactly.
    centres = {rail["center"] for rail in rails}
    anonymous = [x for x in V if x not in TARGET and x not in centres]
    hole_code = {
        x: sum((1 << r) * (1 - selected[r, x]) for r in range(len(rails)))
        for x in anonymous
    }
    for left, right in zip(anonymous, anonymous[1:]):
        model.Add(hole_code[left] <= hole_code[right])

    arcs = {}
    occurrence = {}
    if full:
        for r, rail in enumerate(rails):
            centre = rail["center"]
            circuit = []
            for u in V:
                self_arc = model.NewBoolVar(f"self_{rail['name']}_{u}")
                model.Add(self_arc + selected[r, u] == 1)
                circuit.append((u, u, self_arc))
            for u in V:
                if u == centre:
                    continue
                for v in V:
                    if v == centre or v == u:
                        continue
                    arc = model.NewBoolVar(f"arc_{rail['name']}_{u}_{v}")
                    arcs[r, u, v] = arc
                    model.Add(arc <= selected[r, u])
                    model.Add(arc <= selected[r, v])
                    circuit.append((u, v, arc))
            model.AddCircuit(circuit)

            labels = [x for x in V if x != centre]
            for four in itertools.combinations(labels, 4):
                owner = frozenset((centre, *four))
                paths = []
                for order in itertools.permutations(four):
                    path = and_var(
                        model,
                        [arcs[r, order[j], order[j + 1]] for j in range(3)],
                        f"path_{rail['name']}_{'_'.join(map(str, order))}",
                    )
                    paths.append(path)
                occ = model.NewBoolVar(
                    f"occ_{rail['name']}_{'_'.join(map(str, sorted(owner)))}"
                )
                model.Add(occ == sum(paths))
                occurrence[r, owner] = occ
            model.Add(
                sum(value for (rr, _), value in occurrence.items() if rr == r)
                == rail["period"]
            )

        all_owners = [frozenset(owner) for owner in itertools.combinations(V, 5)]
        for owner in all_owners:
            positive = [
                occurrence[r, owner]
                for r, rail in enumerate(rails)
                if rail["sign"] == 1 and (r, owner) in occurrence
            ]
            negative = [
                occurrence[r, owner]
                for r, rail in enumerate(rails)
                if rail["sign"] == -1 and (r, owner) in occurrence
            ]
            model.Add(sum(positive) <= 1)
            model.Add(sum(negative) <= 1)
            model.Add(
                sum(positive) - sum(negative) == (1 if owner == TARGET else 0)
            )

    return model, rails, selected, arcs


def first_support(rails):
    model, _, selected, _ = build_model(rails, False)
    solver = cp_model.CpSolver()
    solver.parameters.num_search_workers = 8
    status = solver.Solve(model)
    if status not in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        return None
    return {
        rail["name"]: [x for x in V if solver.Value(selected[r, x])]
        for r, rail in enumerate(rails)
    }


def solve(case, rails, mode, seconds, workers, seed, log_search, fix_support):
    full = mode == "full"
    fixed_supports = first_support(rails) if full and fix_support else None
    if full and fix_support and fixed_supports is None:
        return {"case": case, "mode": mode, "status": "SUPPORT_INFEASIBLE"}
    model, rails, selected, arcs = build_model(rails, full, fixed_supports)
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
        "support_fixed": bool(fixed_supports),
    }
    if status not in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        return result

    supports = {}
    cycles = {}
    for r, rail in enumerate(rails):
        values = [x for x in V if solver.Value(selected[r, x])]
        supports[rail["name"]] = values
        if full:
            start = min(values)
            cycle = [start]
            current = start
            while True:
                successor = next(
                    v for v in values
                    if v != current and solver.Value(arcs[r, current, v])
                )
                if successor == start:
                    break
                assert successor not in cycle
                cycle.append(successor)
                current = successor
            assert len(cycle) == rail["period"]
            cycles[rail["name"]] = cycle

    result["supports"] = supports
    result["holes"] = {
        rail["name"]: [
            x for x in V
            if x != rail["center"] and x not in supports[rail["name"]]
        ]
        for rail in rails
    }

    point = Counter()
    for rail in rails:
        point[rail["center"]] += rail["sign"] * rail["period"]
        for x in supports[rail["name"]]:
            point[x] += rail["sign"] * 4
    assert [point[x] for x in V] == [1] * 5 + [0] * 8
    if full:
        positive = Counter()
        negative = Counter()
        for rail in rails:
            deck = owner_deck(rail, cycles[rail["name"]])
            assert len(deck) == rail["period"] == len(set(deck))
            (positive if rail["sign"] == 1 else negative).update(deck)
        assert all(value == 1 for value in positive.values())
        assert all(value == 1 for value in negative.values())
        difference = positive.copy()
        difference.subtract(negative)
        assert {owner: value for owner, value in difference.items() if value} == {
            TARGET: 1
        }
        result["cycles"] = cycles
        result["positive_owner_count"] = sum(positive.values())
        result["negative_owner_count"] = sum(negative.values())
        result["common_owner_count"] = len(set(positive) & set(negative))
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--cancel-period", choices=["all", "10", "11"], default="all")
    parser.add_argument("--cancel-type", choices=["all", *CANCEL_CENTRES], default="all")
    parser.add_argument("--branch", choices=["mass4", "mass5"], default="mass4")
    parser.add_argument("--mass5-profile", choices=["all", "1", "2", "3", "4", "5", "6"], default="all")
    parser.add_argument("--mode", choices=["support", "full"], default="support")
    parser.add_argument("--time-limit", type=float, default=300.0)
    parser.add_argument("--workers", type=int, default=32)
    parser.add_argument("--seed", type=int, default=20260814)
    parser.add_argument("--log-search", action="store_true")
    parser.add_argument("--fix-support", action="store_true")
    parser.add_argument("--ground-size", type=int, default=13)
    args = parser.parse_args()
    if args.ground_size < 12:
        parser.error("ground size must be at least 12")
    global V
    V = tuple(range(args.ground_size))
    if args.branch == "mass4":
        periods = (10, 11) if args.cancel_period == "all" else (int(args.cancel_period),)
        types = tuple(CANCEL_CENTRES) if args.cancel_type == "all" else (args.cancel_type,)
        cases = [
            (f"mass4_p{period}_{kind}", rails_for(period, kind))
            for period in periods for kind in types
        ]
    else:
        profiles = range(1, 7) if args.mass5_profile == "all" else (int(args.mass5_profile),)
        cases = [(f"mass5_{profile}", rails_for_mass5(profile)) for profile in profiles]
    reports = [
        solve(case, rails, args.mode, args.time_limit, args.workers,
              args.seed, args.log_search, args.fix_support)
        for case, rails in cases
    ]
    print(json.dumps({"status": "PASS", "reports": reports}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
