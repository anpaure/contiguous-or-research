#!/usr/bin/env python3
"""Search H100 for a q=3 positive bridge atom: 5*10 -> 5*8+1*9.

The positive rails are chosen from the 33-rail cyclic factor on Z_11 and
must include its unique rail through H={0,1,2,3}.  For each five-rail
choice, enumerate every legal period-8/9 rail whose deck is contained in
the 49-owner punctured union, then solve the exact cover.
"""

from __future__ import annotations

import argparse
import itertools
import json
import multiprocessing as mp
import os
import sys
import time
from collections import Counter


M = 11
H = frozenset({0, 1, 2, 3})
BASE = (
    (1, 2, 3, 4, 6, 9, 5, 10, 7, 8),
    (1, 5, 9, 2, 4, 8, 7, 6, 3, 10),
    (1, 6, 9, 3, 8, 10, 2, 4, 5, 7),
)


def deck(centre: int, cycle: tuple[int, ...]) -> frozenset[frozenset[int]]:
    n = len(cycle)
    return frozenset(
        frozenset({centre, cycle[i], cycle[(i + 1) % n], cycle[(i + 2) % n]})
        for i in range(n)
    )


FACTOR = tuple(
    (shift, base_index, tuple((x + shift) % M for x in base))
    for shift in range(M)
    for base_index, base in enumerate(BASE)
)
FACTOR_DECKS = tuple(deck(centre, cycle) for centre, _, cycle in FACTOR)


def role_feasible(indices: tuple[int, ...]) -> bool:
    """Point/core/unused ledger for five period-8 plus one period-9 rail."""
    core_count = Counter(FACTOR[i][0] for i in indices)
    options = []
    for x in range(M):
        target_degree = 15 + 7 * core_count[x] - (x in H)
        ox = []
        for a in range(6):
            for b in range(2):
                for u in range(12):
                    if 18 + 5 * a + 6 * b - 3 * u == target_degree:
                        ox.append((a, b, u))
        if not ox:
            return False
        options.append(ox)

    states = {(0, 0, 0)}
    for ox in options:
        new_states = set()
        for state in states:
            for add in ox:
                value = tuple(state[j] + add[j] for j in range(3))
                if value[0] <= 5 and value[1] <= 1 and value[2] <= 11:
                    new_states.add(value)
        states = new_states
        if not states:
            return False
    return (5, 1, 11) in states


def candidate_rails(target: frozenset[frozenset[int]]):
    candidates = []
    seen = set()
    for centre in range(M):
        allowed = {
            frozenset(owner - {centre})
            for owner in target
            if centre in owner
        }
        available = tuple(x for x in range(M) if x != centre)
        for period in (8, 9):
            for first in available:
                later = tuple(x for x in available if x > first)
                for second in later:
                    path = [first, second]

                    def extend() -> None:
                        if len(path) == period:
                            if path[1] > path[-1]:
                                return
                            if frozenset((path[-2], path[-1], path[0])) not in allowed:
                                return
                            if frozenset((path[-1], path[0], path[1])) not in allowed:
                                return
                            cycle = tuple(path)
                            values = deck(centre, cycle)
                            key = (centre, values)
                            if key not in seen:
                                seen.add(key)
                                candidates.append((period, centre, cycle, values))
                            return
                        a, b = path[-2:]
                        for x in later:
                            if x in path:
                                continue
                            if frozenset((a, b, x)) in allowed:
                                path.append(x)
                                extend()
                                path.pop()

                    extend()
    return candidates


def exact_cover(target: frozenset[frozenset[int]], candidates):
    period8 = [r for r in candidates if r[0] == 8]
    period9 = [r for r in candidates if r[0] == 9]
    by_owner = {owner: [] for owner in target}
    for index, rail in enumerate(period8):
        for owner in rail[3]:
            by_owner[owner].append(index)

    for rail9 in period9:
        remaining = target - rail9[3]
        if len(remaining) != 40:
            continue
        solution = []

        def search(uncovered: frozenset[frozenset[int]]) -> bool:
            if not uncovered:
                return len(solution) == 5
            if len(solution) >= 5 or len(uncovered) != 8 * (5 - len(solution)):
                return False
            best_options = None
            for owner in uncovered:
                options = [
                    index for index in by_owner[owner]
                    if period8[index][3] <= uncovered
                ]
                if not options:
                    return False
                if best_options is None or len(options) < len(best_options):
                    best_options = options
                    if len(options) == 1:
                        break
            assert best_options is not None
            for index in best_options:
                solution.append(index)
                if search(frozenset(uncovered - period8[index][3])):
                    return True
                solution.pop()
            return False

        if search(frozenset(remaining)):
            return tuple(period8[index] for index in solution) + (rail9,)
    return None


def audit_choice(choice: tuple[int, ...]):
    indices = (0,) + choice
    if not role_feasible(indices):
        return None
    positive = frozenset().union(*(FACTOR_DECKS[i] for i in indices))
    assert len(positive) == 50 and H in positive
    target = frozenset(positive - {H})
    candidates = candidate_rails(target)
    solution = exact_cover(target, candidates)
    if solution is None:
        return None
    negative = frozenset().union(*(rail[3] for rail in solution))
    assert negative == target
    assert sum(len(rail[3]) for rail in solution) == len(target)
    return {
        "positive_indices": indices,
        "positive": [
            {
                "centre": FACTOR[i][0],
                "base_index": FACTOR[i][1],
                "cycle": FACTOR[i][2],
                "deck": sorted(map(sorted, FACTOR_DECKS[i])),
            }
            for i in indices
        ],
        "negative": [
            {
                "period": rail[0],
                "centre": rail[1],
                "cycle": rail[2],
                "deck": sorted(map(sorted, rail[3])),
            }
            for rail in solution
        ],
        "target": sorted(map(sorted, target)),
        "candidate_counts": {
            "period8": sum(rail[0] == 8 for rail in candidates),
            "period9": sum(rail[0] == 9 for rail in candidates),
        },
    }


def choices(scope_centres: int):
    pool = [
        i for i in range(1, len(FACTOR))
        if FACTOR[i][0] < scope_centres
    ]
    yield from itertools.combinations(pool, 4)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--scope-centres", type=int, default=11)
    parser.add_argument("--chunksize", type=int, default=4)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    factor_owners = Counter(owner for values in FACTOR_DECKS for owner in values)
    assert len(factor_owners) == 330 and set(factor_owners.values()) == {1}
    assert [i for i, values in enumerate(FACTOR_DECKS) if H in values] == [0]

    all_choices = list(choices(args.scope_centres))
    role_choices = [choice for choice in all_choices if role_feasible((0,) + choice)]
    print(
        f"host={os.uname().nodename} pid={os.getpid()} workers={args.workers} "
        f"scope_centres={args.scope_centres} choices={len(all_choices)} "
        f"role_feasible={len(role_choices)}",
        flush=True,
    )
    started = time.time()
    with mp.Pool(args.workers) as pool:
        for checked, result in enumerate(
            pool.imap_unordered(audit_choice, role_choices, chunksize=args.chunksize),
            1,
        ):
            if checked % 1000 == 0:
                print(f"checked={checked} elapsed={time.time()-started:.2f}", flush=True)
            if result is not None:
                result["host"] = os.uname().nodename
                result["elapsed_seconds"] = time.time() - started
                result["scope_centres"] = args.scope_centres
                result["role_feasible_choices"] = len(role_choices)
                with open(args.output, "w", encoding="utf-8") as handle:
                    json.dump(result, handle, indent=2, sort_keys=True)
                    handle.write("\n")
                print(f"FOUND checked={checked} output={args.output}", flush=True)
                pool.terminate()
                return
    print(f"NONE checked={len(role_choices)} elapsed={time.time()-started:.2f}", flush=True)
    sys.exit(2)


if __name__ == "__main__":
    main()
