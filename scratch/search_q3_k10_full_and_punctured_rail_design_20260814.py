#!/usr/bin/env python3
"""H100-only CP-SAT search for q=3 K_10^4 and K_10^4-H rail designs.

Every candidate is a genuine centred cyclic 3-window rail of period 8 or 9.
The full target uses 24 period-8 and 2 period-9 rails.  The punctured target
uses 25 period-8 and 1 period-9 rail.  Exact owner constraints imply a
simple decomposition.  A full and punctured solution on the same ground
set give a positive one-owner trade.
"""

from __future__ import annotations

import argparse
import itertools
import json
import os
import time
from collections import Counter, defaultdict

from ortools.sat.python import cp_model


V = 10
Q = 3
H = tuple(range(Q + 1))
OWNERS = tuple(itertools.combinations(range(V), Q + 1))
OWNER_INDEX = {owner: i for i, owner in enumerate(OWNERS)}


def rail_deck(center: int, cycle: tuple[int, ...]) -> tuple[int, ...]:
    period = len(cycle)
    values = []
    for i in range(period):
        owner = tuple(sorted((center, cycle[i], cycle[(i + 1) % period], cycle[(i + 2) % period])))
        assert len(owner) == Q + 1
        values.append(OWNER_INDEX[owner])
    assert len(values) == len(set(values))
    return tuple(sorted(values))


def candidates() -> list[tuple[int, tuple[int, ...], tuple[int, ...]]]:
    ans: list[tuple[int, tuple[int, ...], tuple[int, ...]]] = []
    seen: set[tuple[int, tuple[int, ...]]] = set()
    for center in range(V):
        available = tuple(x for x in range(V) if x != center)
        for period in (8, 9):
            for support in itertools.combinations(available, period):
                root = min(support)
                tail = tuple(x for x in support if x != root)
                for perm in itertools.permutations(tail):
                    cycle = (root,) + perm
                    if cycle[1] > cycle[-1]:
                        continue
                    values = rail_deck(center, cycle)
                    key = (center, values)
                    if key in seen:
                        continue
                    seen.add(key)
                    ans.append((center, cycle, values))
    return ans


def solve(mode: str, output: str, workers: int, seconds: float, log: bool) -> None:
    started = time.time()
    rails = candidates()
    target = set(range(len(OWNERS)))
    if mode == "punctured":
        target.remove(OWNER_INDEX[H])
    period_counts = {8: 24, 9: 2} if mode == "full" else {8: 25, 9: 1}

    usable = [
        i for i, rail in enumerate(rails)
        if set(rail[2]) <= target
    ]
    by_owner: dict[int, list[int]] = defaultdict(list)
    by_period: dict[int, list[int]] = defaultdict(list)
    for i in usable:
        by_period[len(rails[i][1])].append(i)
        for owner in rails[i][2]:
            by_owner[owner].append(i)

    print(
        f"host={os.uname().nodename} mode={mode} candidates={len(rails)} "
        f"usable={len(usable)} generated_seconds={time.time()-started:.3f}",
        flush=True,
    )
    model = cp_model.CpModel()
    variables = {i: model.new_bool_var(f"r{i}") for i in usable}
    for owner in sorted(target):
        model.add_exactly_one(variables[i] for i in by_owner[owner])
    for period, count in period_counts.items():
        model.add(sum(variables[i] for i in by_period[period]) == count)

    # The symmetric group preserving the target is transitive on period-9
    # rails through a fixed owner: for the full target fix a canonical rail;
    # for the punctured target fix the omitted label's canonical rail.  This
    # is a labelled symmetry normalization, not an extra existence premise.
    canonical_center = 0 if mode == "full" else 4
    canonical_cycle = tuple(x for x in range(V) if x != canonical_center)
    canonical_deck = rail_deck(canonical_center, canonical_cycle)
    canonical = next(
        i for i in usable
        if rails[i][0] == canonical_center and rails[i][2] == canonical_deck
    )
    model.add(variables[canonical] == 1)

    solver = cp_model.CpSolver()
    solver.parameters.num_search_workers = workers
    solver.parameters.max_time_in_seconds = seconds
    solver.parameters.log_search_progress = log
    solver.parameters.random_seed = 20260814
    solver.parameters.cp_model_presolve = True
    status = solver.solve(model)
    print(
        f"status={solver.status_name(status)} wall={solver.wall_time:.3f} "
        f"branches={solver.num_branches} conflicts={solver.num_conflicts}",
        flush=True,
    )
    if status not in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        raise SystemExit(2)

    selected = [i for i in usable if solver.boolean_value(variables[i])]
    cover = Counter(owner for i in selected for owner in rails[i][2])
    assert set(cover) == target and set(cover.values()) == {1}
    assert Counter(len(rails[i][1]) for i in selected) == Counter(period_counts)
    result = {
        "host": os.uname().nodename,
        "mode": mode,
        "ground_size": V,
        "q": Q,
        "H": H,
        "target_owner_count": len(target),
        "period_counts": period_counts,
        "candidate_count": len(rails),
        "usable_candidate_count": len(usable),
        "status": solver.status_name(status),
        "wall_time": solver.wall_time,
        "rails": [
            {
                "center": rails[i][0],
                "cycle": rails[i][1],
                "period": len(rails[i][1]),
                "deck": [OWNERS[o] for o in rails[i][2]],
            }
            for i in selected
        ],
    }
    with open(output, "w", encoding="utf-8") as handle:
        json.dump(result, handle, indent=2, sort_keys=True)
        handle.write("\n")
    print(f"wrote={output} selected={len(selected)}", flush=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=("full", "punctured"))
    parser.add_argument("--output", required=True)
    parser.add_argument("--workers", type=int, default=64)
    parser.add_argument("--seconds", type=float, default=1800)
    parser.add_argument("--log", action="store_true")
    args = parser.parse_args()
    solve(args.mode, args.output, args.workers, args.seconds, args.log)


if __name__ == "__main__":
    main()
