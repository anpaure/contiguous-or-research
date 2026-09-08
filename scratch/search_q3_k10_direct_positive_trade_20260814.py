#!/usr/bin/env python3
"""H100-only exact search for a q=3 distance-one positive rail trade.

On ten reduced labels, enumerate every distinct centred cyclic 3-window
deck of period 8 or 9.  Seek two simple t-rail shores A+, A- with

    deck(A+) = deck(A-) disjoint_union {H}, H={0,1,2,3}.

The period equation is enforced in its primitive form: A+ has one more
period-9 and one fewer period-8 rail than A-.  A canonical H-containing
positive rail is fixed by the setwise stabilizer of H, separately for the
period-8 and period-9 cases.
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
H_INDEX = OWNER_INDEX[H]


def rail_deck(center: int, cycle: tuple[int, ...]) -> tuple[int, ...]:
    period = len(cycle)
    values = []
    for i in range(period):
        owner = tuple(sorted((center, cycle[i], cycle[(i + 1) % period], cycle[(i + 2) % period])))
        assert len(owner) == Q + 1
        values.append(OWNER_INDEX[owner])
    assert len(values) == len(set(values))
    return tuple(sorted(values))


def candidates():
    ans = []
    seen = set()
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


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--t", type=int, required=True)
    parser.add_argument("--h-period", type=int, choices=(8, 9), required=True)
    parser.add_argument("--seconds", type=float, default=1800)
    parser.add_argument("--workers", type=int, default=64)
    parser.add_argument("--output", required=True)
    parser.add_argument("--log", action="store_true")
    args = parser.parse_args()

    started = time.time()
    rails = candidates()
    by_owner = defaultdict(list)
    by_period = defaultdict(list)
    containing_h = []
    for i, rail in enumerate(rails):
        by_period[len(rail[1])].append(i)
        for owner in rail[2]:
            by_owner[owner].append(i)
        if H_INDEX in rail[2]:
            containing_h.append(i)

    canonical_cycle = tuple(range(1, args.h_period + 1))
    canonical_deck = rail_deck(0, canonical_cycle)
    canonical = next(
        i for i, rail in enumerate(rails)
        if rail[0] == 0 and rail[2] == canonical_deck
    )
    print(
        f"host={os.uname().nodename} t={args.t} h_period={args.h_period} "
        f"candidates={len(rails)} H_candidates={len(containing_h)} "
        f"generated_seconds={time.time()-started:.3f}",
        flush=True,
    )

    model = cp_model.CpModel()
    plus = [model.new_bool_var(f"p{i}") for i in range(len(rails))]
    minus = [model.new_bool_var(f"m{i}") for i in range(len(rails))]
    model.add(plus[canonical] == 1)
    for i in containing_h:
        if i != canonical:
            model.add(plus[i] == 0)
        model.add(minus[i] == 0)

    model.add(sum(plus) == args.t)
    model.add(sum(minus) == args.t)
    model.add(
        sum(plus[i] for i in by_period[9])
        == sum(minus[i] for i in by_period[9]) + 1
    )
    if args.t == 3:
        # The q=3 centre character forces the unique minimum short-period
        # profile: +2 at one H label and -1 at the other three; zero outside.
        centre_short = defaultdict(list)
        for i in by_period[8]:
            centre_short[rails[i][0]].append(i)
        for z in range(V):
            delta = sum(plus[i] for i in centre_short[z]) - sum(minus[i] for i in centre_short[z])
            if z in H:
                model.add_allowed_assignments([delta], [[-1], [2]])
            else:
                model.add(delta == 0)
    for owner in range(len(OWNERS)):
        p = sum(plus[i] for i in by_owner[owner])
        m = sum(minus[i] for i in by_owner[owner])
        model.add(p <= 1)
        model.add(m <= 1)
        model.add(p - m == (1 if owner == H_INDEX else 0))

    solver = cp_model.CpSolver()
    solver.parameters.num_search_workers = args.workers
    solver.parameters.max_time_in_seconds = args.seconds
    solver.parameters.random_seed = 20260814 + 100 * args.t + args.h_period
    solver.parameters.log_search_progress = args.log
    status = solver.solve(model)
    print(
        f"status={solver.status_name(status)} wall={solver.wall_time:.3f} "
        f"branches={solver.num_branches} conflicts={solver.num_conflicts}",
        flush=True,
    )
    if status not in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        raise SystemExit(2)

    psel = [i for i in range(len(rails)) if solver.boolean_value(plus[i])]
    msel = [i for i in range(len(rails)) if solver.boolean_value(minus[i])]
    pcov = Counter(owner for i in psel for owner in rails[i][2])
    mcov = Counter(owner for i in msel for owner in rails[i][2])
    assert set(pcov.values()) == {1} and set(mcov.values()) == {1}
    assert pcov - mcov == Counter({H_INDEX: 1}) and not (mcov - pcov)
    assert Counter(len(rails[i][1]) for i in psel)[9] == Counter(len(rails[i][1]) for i in msel)[9] + 1

    def show(i):
        center, cycle, values = rails[i]
        return {
            "center": center,
            "cycle": cycle,
            "period": len(cycle),
            "deck": [OWNERS[o] for o in values],
        }

    result = {
        "host": os.uname().nodename,
        "q": Q,
        "ground_size": V,
        "H": H,
        "t": args.t,
        "h_period": args.h_period,
        "candidate_count": len(rails),
        "status": solver.status_name(status),
        "wall_time": solver.wall_time,
        "plus": [show(i) for i in psel],
        "minus": [show(i) for i in msel],
    }
    with open(args.output, "w", encoding="utf-8") as handle:
        json.dump(result, handle, indent=2, sort_keys=True)
        handle.write("\n")
    print(
        f"FOUND plus_periods={sorted(len(rails[i][1]) for i in psel)} "
        f"minus_periods={sorted(len(rails[i][1]) for i in msel)} "
        f"collateral={len(mcov)} output={args.output}",
        flush=True,
    )


if __name__ == "__main__":
    main()
