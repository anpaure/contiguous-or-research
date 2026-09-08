#!/usr/bin/env python3
"""Audit the exact weighted multidepth floor drift of physical C8 switches.

The exhaustive mode enumerates the complete canonical C8 component for
r<=4.  The greedy mode only supplies finite local-minimum diagnostics.
Intended execution environment: H100 only.
"""

from __future__ import annotations

import argparse
import random
from collections import Counter, deque
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from math import comb

from research_msw_c8_shadow_anneal_20260821 import (
    dyck_words,
    msw_row,
    switches,
    window_counter,
)


def floor_constants(r, H):
    b = 2 * r + 1
    total = comb(b, r)
    return tuple(total // comb(b, r - q) for q in range(1, H + 1))


def floor_q(loads, target_count, c):
    answer = (target_count - len(loads)) * c * (c + 1)
    answer += sum((value - c) * (value - c - 1) for value in loads.values())
    return answer


def state_profile(rows, r, H):
    b = 2 * r + 1
    constants = floor_constants(r, H)
    profile = []
    for q, c in enumerate(constants, start=1):
        loads = Counter()
        for row in rows:
            loads.update(window_counter(row, r - q))
        target_count = comb(b, r - q)
        value = floor_q(loads, target_count, c)
        assert Fraction(value, c) >= 2 * (target_count - len(loads))
        profile.append((q, c, value))
    weighted = sum((Fraction(value, c) for _, c, value in profile), Fraction())
    return tuple(profile), weighted


@lru_cache(maxsize=None)
def depth_delta(old1, old2, new1, new2, q):
    r = (len(old1) - 1) // 2
    old = window_counter(old1, r - q) + window_counter(old2, r - q)
    new = window_counter(new1, r - q) + window_counter(new2, r - q)
    new.subtract(old)
    return tuple((target, value) for target, value in new.items() if value)


def predicted_delta(loads_by_q, constants, old_pair, new_pair):
    direct = Fraction()
    formula = Fraction()
    footprint = []
    for q, (loads, c) in enumerate(zip(loads_by_q, constants), start=1):
        delta = depth_delta(old_pair[0], old_pair[1], new_pair[0], new_pair[1], q)
        direct_q = 0
        donors = []
        recipients = []
        for target, change in delta:
            before = loads[target]
            after = before + change
            direct_q += (after - c) * (after - c - 1)
            direct_q -= (before - c) * (before - c - 1)
            if change == -1:
                donors.append(target)
            elif change == 1:
                recipients.append(target)
            else:
                raise AssertionError((q, change))
        assert len(donors) == len(recipients)
        p = len(donors)
        formula_q = 2 * (
            sum(loads[target] for target in recipients)
            - sum(loads[target] for target in donors)
            + p
        )
        assert direct_q == formula_q, (q, direct_q, formula_q)
        direct += Fraction(direct_q, c)
        formula += Fraction(formula_q, c)
        footprint.append((q, p))
    assert direct == formula
    return direct, tuple(footprint)


def loads_for(rows, r, H):
    loads = []
    for q in range(1, H + 1):
        counter = Counter()
        for row in rows:
            counter.update(window_counter(row, r - q))
        loads.append(counter)
    return loads


def state_neighbours(state):
    for i, j in combinations(range(len(state)), 2):
        old_pair = (state[i], state[j])
        for new_pair in switches(*old_pair):
            nxt = tuple(
                sorted(
                    new_pair
                    + tuple(state[t] for t in range(len(state)) if t not in (i, j))
                )
            )
            if len(set(nxt)) == len(state):
                yield nxt, old_pair, new_pair


def exhaustive(r, H):
    start = tuple(sorted(msw_row(word) for word in dyck_words(r)))
    queue = deque([start])
    seen = {start}
    neighbours = {}
    footprint_hist = Counter()
    while queue:
        state = queue.popleft()
        loads = loads_for(state, r, H)
        constants = floor_constants(r, H)
        next_states = []
        for nxt, old_pair, new_pair in state_neighbours(state):
            delta, footprint = predicted_delta(loads, constants, old_pair, new_pair)
            footprint_hist[footprint] += 1
            next_states.append((nxt, delta))
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
        neighbours[state] = tuple(next_states)

    objective = {state: state_profile(state, r, H)[1] for state in seen}
    local = []
    for state in seen:
        assert all(objective[nxt] - objective[state] == delta
                   for nxt, delta in neighbours[state])
        if all(objective[nxt] >= objective[state] for nxt, _ in neighbours[state]):
            local.append(state)
    local_values = Counter(objective[state] for state in local)
    minimum = min(objective.values())
    canonical_profile, canonical_value = state_profile(start, r, H)
    return {
        "r": r,
        "H": H,
        "states": len(seen),
        "canonical_profile": canonical_profile,
        "canonical_weighted": str(canonical_value),
        "global_minimum": str(minimum),
        "global_minimizers": sum(value == minimum for value in objective.values()),
        "local_minima": len(local),
        "local_value_hist": {str(key): value for key, value in sorted(local_values.items())},
        "max_local_over_HA_over_r": float(max(local_values) / (H * comb(2 * r + 1, r) / r)),
        "footprint_hist": {str(key): value for key, value in footprint_hist.items()},
    }


class GreedyState:
    def __init__(self, r, H):
        self.r = r
        self.H = H
        self.rows = set(msw_row(word) for word in dyck_words(r))
        self.loads = loads_for(tuple(self.rows), r, H)
        self.constants = floor_constants(r, H)
        self.moves = {}
        for left, right in combinations(sorted(self.rows), 2):
            self.add_pair(left, right)

    def add_pair(self, left, right):
        key = tuple(sorted((left, right)))
        alternatives = switches(*key)
        if alternatives:
            self.moves[key] = alternatives

    def apply(self, key, answer):
        old1, old2 = key
        for pair in tuple(self.moves):
            if old1 in pair or old2 in pair:
                del self.moves[pair]
        self.rows.remove(old1)
        self.rows.remove(old2)
        self.rows.update(answer)
        for q, loads in enumerate(self.loads, start=1):
            for target, change in depth_delta(old1, old2, answer[0], answer[1], q):
                loads[target] += change
                if loads[target] == 0:
                    del loads[target]
        for row in answer:
            for other in self.rows:
                if row != other:
                    self.add_pair(row, other)

    def objective(self):
        b = 2 * self.r + 1
        values = []
        for q, (loads, c) in enumerate(zip(self.loads, self.constants), start=1):
            target_count = comb(b, self.r - q)
            value = floor_q(loads, target_count, c)
            assert Fraction(value, c) >= 2 * (target_count - len(loads))
            values.append(value)
        return sum((Fraction(value, c) for value, c in zip(values, self.constants)), Fraction()), values


def greedy(r, H, seeds, max_steps):
    results = []
    for seed in range(seeds):
        rng = random.Random(seed)
        state = GreedyState(r, H)
        steps = 0
        while steps < max_steps:
            candidates = []
            for key, alternatives in state.moves.items():
                for answer in alternatives:
                    delta, _ = predicted_delta(
                        state.loads, state.constants, key, answer
                    )
                    if delta < 0:
                        candidates.append((delta, rng.random(), key, answer))
            if not candidates:
                break
            best = min(delta for delta, _, _, _ in candidates)
            band = [item for item in candidates if item[0] <= best / 2]
            _, _, key, answer = rng.choice(band)
            state.apply(key, answer)
            steps += 1
        value, values = state.objective()
        results.append(
            {
                "seed": seed,
                "steps": steps,
                "weighted": str(value),
                "Q_profile": values,
                "legal_pairs": len(state.moves),
                "ratio_to_HA_over_r": float(value / (H * comb(2 * r + 1, r) / r)),
            }
        )
    return {"r": r, "H": H, "greedy_local_minima": results}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--exhaustive", action="store_true")
    parser.add_argument("--r", type=int, nargs="+", default=[3, 4])
    parser.add_argument("--H", type=int, nargs="+")
    parser.add_argument("--seeds", type=int, default=4)
    parser.add_argument("--max-steps", type=int, default=10_000)
    args = parser.parse_args()
    for r in args.r:
        heights = args.H or list(range(1, max(2, r - 1)))
        for H in heights:
            if not 1 <= H <= r - 2:
                continue
            result = exhaustive(r, H) if args.exhaustive else greedy(
                r, H, args.seeds, args.max_steps
            )
            print("C8_WEIGHTED_MULTIDEPTH_FLOOR", result, flush=True)


if __name__ == "__main__":
    main()
