#!/usr/bin/env python3
"""Greedy/tabu q1 balancing using only universal 2x2/C8 wreath switches."""

from __future__ import annotations

import argparse
import random
from collections import Counter
from functools import lru_cache
from itertools import combinations


def dyck_words(m: int):
    def rec(pos: int, ones: int, word: list[str]):
        if pos == 2 * m:
            yield "".join(word)
            return
        if ones < m:
            word.append("1")
            yield from rec(pos + 1, ones + 1, word)
            word.pop()
        if pos - ones < ones:
            word.append("0")
            yield from rec(pos + 1, ones, word)
            word.pop()

    yield from rec(0, 0, [])


def mu(word: str) -> str:
    return word[::-1].translate(str.maketrans("01", "10"))


def rho(word: str) -> list[int]:
    if not word:
        return []
    h = 0
    close = None
    for i, bit in enumerate(word):
        h += 1 if bit == "1" else -1
        if h == 0:
            close = i
            break
    assert close is not None
    u, v = word[1:close], word[close + 1 :]
    d = len(u) + 2
    return [d] + [d - x for x in rho(mu(u))] + [1] + [d + x for x in rho(v)]


@lru_cache(maxsize=None)
def canonical(order):
    order = tuple(order)
    rots = [order[i:] + order[:i] for i in range(len(order))]
    rev = tuple(reversed(order))
    rots.extend(rev[i:] + rev[:i] for i in range(len(order)))
    return min(rots)


def msw_row(word: str):
    r = len(word) // 2
    b = 2 * r + 1
    q = rho(word) + [b]
    return canonical(tuple(q[(-1 - 2 * j) % b] for j in range(b)))


@lru_cache(maxsize=None)
def forms(order):
    order = tuple(order)
    b = len(order)
    answer = []
    for base in (order, tuple(reversed(order))):
        for shift in range(b):
            answer.append(base[shift:] + base[:shift])
    return tuple(answer)


@lru_cache(maxsize=None)
def switches(row1, row2):
    if row2 < row1:
        row1, row2 = row2, row1
    r = (len(row1) - 1) // 2
    answers = set()
    for left, right in ((row1, row2), (row2, row1)):
        right_forms = set(forms(right))
        for R1 in forms(left):
            a, b = R1[:2]
            P = R1[2 : r + 1]
            c, d = R1[r + 1 : r + 3]
            Q = R1[r + 3 :]
            if (c, a) + P + (d, b) + Q not in right_forms:
                continue
            answer = tuple(
                sorted(
                    (
                        canonical((a, c) + P + (b, d) + Q),
                        canonical((b, a) + P + (d, c) + Q),
                    )
                )
            )
            if answer != (row1, row2):
                answers.add(answer)
    return tuple(sorted(answers))


@lru_cache(maxsize=None)
def window_counter(row, k):
    b = len(row)
    return Counter(
        frozenset(row[(i + j) % b] for j in range(k)) for i in range(b)
    )


@lru_cache(maxsize=None)
def move_delta(old1, old2, new1, new2):
    r = (len(old1) - 1) // 2
    old = window_counter(old1, r - 1) + window_counter(old2, r - 1)
    new = window_counter(new1, r - 1) + window_counter(new2, r - 1)
    delta = new.copy()
    delta.subtract(old)
    return tuple((x, v) for x, v in delta.items() if v)


def binom(n, k):
    if k < 0 or k > n:
        return 0
    z = 1
    for i in range(1, k + 1):
        z = z * (n - k + i) // i
    return z


class State:
    def __init__(self, rows):
        self.rows = set(rows)
        self.r = (len(next(iter(self.rows))) - 1) // 2
        self.loads = Counter()
        for row in self.rows:
            self.loads.update(window_counter(row, self.r - 1))
        self.moves = {}
        for x, y in combinations(sorted(self.rows), 2):
            self._add_pair(x, y)

    def _add_pair(self, x, y):
        key = tuple(sorted((x, y)))
        answers = switches(*key)
        if answers:
            self.moves[key] = answers

    def statistics(self):
        b = 2 * self.r + 1
        A = binom(b, self.r)
        N = binom(b, self.r - 1)
        phi = sum(v * (v - 1) // 2 for v in self.loads.values())
        return {
            "holes": N - len(self.loads),
            "phi": phi,
            "baseline": A - N,
            "gap": phi - (A - N),
            "max_mult": max(self.loads.values()),
            "available_pairs": len(self.moves),
        }

    def availability_profile(self):
        incidence = Counter()
        drift_hist = Counter()
        for key, answers in self.moves.items():
            for answer in answers:
                dphi, dholes = self.predicted(key, answer)
                drift_hist[(dphi, dholes)] += 1
                for target, dv in move_delta(key[0], key[1], answer[0], answer[1]):
                    incidence[(target, dv)] += 1
        targets = {target for target, _ in incidence}
        b = 2 * self.r + 1
        all_targets = binom(b, self.r - 1)
        hole_incidence = Counter()
        for (target, dv), count in incidence.items():
            if self.loads[target] == 0:
                hole_incidence[dv] += count
        by_load = {}
        for target in targets:
            load = self.loads[target]
            donor = incidence[(target, -1)]
            recipient = incidence[(target, 1)]
            item = by_load.setdefault(
                load,
                {"targets": 0, "donor": 0, "recipient": 0, "eta": 0},
            )
            item["targets"] += 1
            item["donor"] += donor
            item["recipient"] += recipient
            item["eta"] += donor - recipient
        return {
            "distinct_touched_targets": len(targets),
            "untouched_targets": all_targets - len(targets),
            "touched_holes": sum(1 for x in targets if self.loads[x] == 0),
            "all_holes": all_targets - len(self.loads),
            "hole_signed_incidence": sorted(hole_incidence.items()),
            "target_load_at_incidence": sorted(
                Counter(self.loads[target] for target in targets).items()
            ),
            "drift_hist": sorted(drift_hist.items()),
            "total_drift": sum(dphi * count for (dphi, _), count in drift_hist.items()),
            "incidence_by_load": sorted(by_load.items()),
        }

    def predicted(self, key, answer):
        delta = move_delta(key[0], key[1], answer[0], answer[1])
        dphi = 0
        dholes = 0
        for x, dv in delta:
            old = self.loads[x]
            new = old + dv
            dphi += new * (new - 1) // 2 - old * (old - 1) // 2
            if old == 0 and new > 0:
                dholes -= 1
            if old > 0 and new == 0:
                dholes += 1
            assert new >= 0
        return dphi, dholes

    def apply(self, key, answer):
        old1, old2 = key
        for pair in list(self.moves):
            if old1 in pair or old2 in pair:
                del self.moves[pair]
        self.rows.remove(old1)
        self.rows.remove(old2)
        self.rows.update(answer)
        for x, dv in move_delta(old1, old2, answer[0], answer[1]):
            self.loads[x] += dv
            if self.loads[x] == 0:
                del self.loads[x]
        for x in answer:
            for y in self.rows:
                if x != y:
                    self._add_pair(x, y)


def run(r, steps, seed, plateau_random):
    rng = random.Random(seed)
    initial = tuple(msw_row(w) for w in dyck_words(r))
    state = State(initial)
    best = state.statistics().copy()
    best_step = 0
    neutral_run = 0
    row_use = Counter()
    A = binom(2 * r + 1, r)
    max_drift_gap_excess = None
    for step in range(1, steps + 1):
        candidates = []
        for key, answers in state.moves.items():
            for answer in answers:
                dphi, dholes = state.predicted(key, answer)
                candidates.append((dphi, dholes, rng.random(), key, answer))
        if not candidates:
            break
        current_gap = state.statistics()["gap"]
        drift_gap_excess = sum(z[0] for z in candidates) + current_gap - A / r
        if max_drift_gap_excess is None or drift_gap_excess > max_drift_gap_excess:
            max_drift_gap_excess = drift_gap_excess
        candidates.sort(key=lambda z: (z[0], z[1], z[2]))
        best_delta = candidates[0][0]
        if best_delta < 0:
            chosen = candidates[0]
            neutral_run = 0
        else:
            neutral_run += 1
            band = [z for z in candidates if z[0] <= (0 if neutral_run < plateau_random else 1)]
            if not band:
                band = candidates[: max(1, min(16, len(candidates)))]
            chosen = rng.choice(band)
            if neutral_run >= plateau_random:
                neutral_run = 0
        _, _, _, key, answer = chosen
        for row in key:
            row_use[row] += 1
        state.apply(key, answer)
        stats = state.statistics()
        if (stats["phi"], stats["holes"], stats["max_mult"]) < (
            best["phi"], best["holes"], best["max_mult"]
        ):
            best = stats.copy()
            best_step = step
            print(
                {"r": r, "seed": seed, "step": step, "best": best, "max_row_use": max(row_use.values())},
                flush=True,
            )
            if best["gap"] == 0:
                break
    print(
        {
            "FINAL": True,
            "r": r,
            "seed": seed,
            "best_step": best_step,
            "best": best,
            "current": state.statistics(),
            "distinct_consumed_rows": len(row_use),
            "max_row_use": max(row_use.values(), default=0),
            "availability_profile": state.availability_profile(),
            "max_total_drift_plus_gap_minus_A_over_r": max_drift_gap_excess,
        },
        flush=True,
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--r", type=int, nargs="+", required=True)
    parser.add_argument("--steps", type=int, default=10000)
    parser.add_argument("--seeds", type=int, default=4)
    parser.add_argument("--plateau-random", type=int, default=20)
    args = parser.parse_args()
    for r in args.r:
        for seed in range(args.seeds):
            run(r, args.steps, seed, args.plateau_random)
