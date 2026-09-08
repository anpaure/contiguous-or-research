#!/usr/bin/env python3
"""H100-only CP-SAT search for the first feasible q=3 near-C atom.

The centre-support theorem reduces every four-rail shore to four placement
types.  This script exhaustively generates every cyclic period-8/9 rail on
the reduced ten-label ground and solves the complete named-owner equality
with shore simplicity.  It is a finite search, not part of the symbolic
obstruction proof.
"""

import argparse
import itertools
import json
from collections import Counter, defaultdict

from ortools.sat.python import cp_model


V = tuple(range(10))
TARGET = frozenset((0, 1, 2, 3))
OWNER_ID = {frozenset(x): i for i, x in enumerate(itertools.combinations(V, 4))}
OWNER_SET = tuple(OWNER_ID)


def cyclic_orders(labels):
    labels = tuple(sorted(labels))
    root = labels[0]
    for tail in itertools.permutations(labels[1:]):
        order = (root,) + tail
        if order[1] < order[-1]:
            yield order


def rail_candidates(center, period, forbid_target):
    available = tuple(x for x in V if x != center)
    supports = (available,) if period == 9 else itertools.combinations(available, 8)
    out = []
    seen = set()
    for support in supports:
        support = tuple(support)
        for order in cyclic_orders(support):
            deck_sets = tuple(
                frozenset((center,
                           order[i],
                           order[(i + 1) % period],
                           order[(i + 2) % period]))
                for i in range(period)
            )
            if len(set(deck_sets)) != period:
                raise AssertionError((center, period, order))
            deck = tuple(sorted(OWNER_ID[x] for x in deck_sets))
            if deck in seen:
                continue
            seen.add(deck)
            if forbid_target and OWNER_ID[TARGET] in deck:
                continue
            out.append({
                "order": order,
                "support_mask": sum(1 << x for x in support),
                "deck": deck,
            })
    return out


PLACEMENTS = {
    # Multiplicity-two positive long centre on one non-distinguished target.
    "same_target": (1, 1),
    # Two different non-distinguished target centres.
    "two_targets": (1, 2),
    # One target and one exterior centre.
    "target_exterior": (1, 4),
    # Two different exterior centres.
    "two_exteriors": (4, 5),
}


def group_specs(placement):
    u, v = PLACEMENTS[placement]
    positive = Counter(((0, 8), (0, 8), (u, 9), (v, 9)))
    negative = Counter(((0, 9), (1, 8), (2, 8), (3, 8)))
    specs = []
    for sign, counter in ((1, positive), (-1, negative)):
        for (center, period), count in sorted(counter.items()):
            specs.append({
                "sign": sign,
                "center": center,
                "period": period,
                "count": count,
                "name": f"{'P' if sign > 0 else 'N'}_{center}_{period}",
            })
    return specs


def solve(placement, time_limit, workers, output_path):
    specs = group_specs(placement)
    cache = {}
    model = cp_model.CpModel()
    variables = {}
    candidates = {}

    for spec in specs:
        key = (spec["center"], spec["period"], spec["sign"] < 0)
        if key not in cache:
            cache[key] = rail_candidates(*key)
        group_candidates = cache[key]
        candidates[spec["name"]] = group_candidates
        variables[spec["name"]] = [
            model.NewBoolVar(f"{spec['name']}_{i}")
            for i in range(len(group_candidates))
        ]
        model.Add(sum(variables[spec["name"]]) == spec["count"])

    owner_terms = {oid: {1: [], -1: []} for oid in range(len(OWNER_SET))}
    for spec in specs:
        sign = spec["sign"]
        name = spec["name"]
        for var, cand in zip(variables[name], candidates[name]):
            for oid in cand["deck"]:
                owner_terms[oid][sign].append(var)

    target_id = OWNER_ID[TARGET]
    for oid in range(len(OWNER_SET)):
        pos = owner_terms[oid][1]
        neg = owner_terms[oid][-1]
        model.Add(sum(pos) - sum(neg) == (1 if oid == target_id else 0))
        model.Add(sum(pos) <= 1)
        model.Add(sum(neg) <= 1)

    # Exact point equations yield the signed toggle-support counts.  They
    # are redundant with the complete owner equations but greatly strengthen
    # propagation and independently protect the centre-profile convention.
    centre_a = Counter()
    centre_b = Counter()
    for spec in specs:
        ledger = centre_a if spec["period"] == 8 else centre_b
        ledger[spec["center"]] += spec["sign"] * spec["count"]
    for z in V:
        h = int(z in TARGET)
        num = h - 8 * centre_a[z] - 9 * centre_b[z]
        assert num % 3 == 0
        needed = num // 3
        terms = []
        for spec in specs:
            name = spec["name"]
            for var, cand in zip(variables[name], candidates[name]):
                if cand["support_mask"] & (1 << z):
                    terms.append(spec["sign"] * var)
        model.Add(sum(terms) == needed)

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = time_limit
    solver.parameters.num_search_workers = workers
    solver.parameters.log_search_progress = True
    status = solver.Solve(model)
    status_name = solver.StatusName(status)
    result = {
        "placement": placement,
        "status": status_name,
        "wall_time": solver.WallTime(),
        "conflicts": solver.NumConflicts(),
        "branches": solver.NumBranches(),
        "candidate_counts": {k: len(v) for k, v in candidates.items()},
        "selected": [],
    }
    if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        for spec in specs:
            name = spec["name"]
            for i, (var, cand) in enumerate(zip(variables[name], candidates[name])):
                if solver.Value(var):
                    result["selected"].append({
                        "group": name,
                        "candidate": i,
                        "center": spec["center"],
                        "period": spec["period"],
                        "sign": spec["sign"],
                        "order": cand["order"],
                        "owners": [sorted(OWNER_SET[x]) for x in cand["deck"]],
                    })
    with open(output_path, "w", encoding="utf-8") as handle:
        json.dump(result, handle, indent=2, sort_keys=True)
        handle.write("\n")
    print(json.dumps({k: v for k, v in result.items() if k != "selected"},
                     sort_keys=True))
    if result["selected"]:
        print(f"SAT selected={len(result['selected'])} output={output_path}")
    return 0 if status in (cp_model.OPTIMAL, cp_model.FEASIBLE, cp_model.INFEASIBLE) else 2


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--placement", choices=sorted(PLACEMENTS), required=True)
    parser.add_argument("--time-limit", type=float, default=600.0)
    parser.add_argument("--workers", type=int, default=32)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    raise SystemExit(solve(args.placement, args.time_limit, args.workers, args.output))


if __name__ == "__main__":
    main()

