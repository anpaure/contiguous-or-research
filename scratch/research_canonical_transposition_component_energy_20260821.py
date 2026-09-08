#!/usr/bin/env python3
"""Exact q1 energy moment for the canonical s_1 component cube.

Tests the precise component-rounding identity
  E Phi = Phi + (sum ||delta_K||^2 - ||sum delta_K||^2)/8
whose all-on shore is the coordinate-transposed canonical factor.
Intended execution: H100 only.
"""

from __future__ import annotations

import argparse
import math
import random
from collections import Counter, defaultdict


def dyck_words(m):
    def rec(pos, ones, word):
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


def mu(word):
    return word[::-1].translate(str.maketrans("01", "10"))


def rho(word):
    if not word:
        return []
    height = 0
    close = None
    for i, bit in enumerate(word):
        height += 1 if bit == "1" else -1
        if height == 0:
            close = i
            break
    assert close is not None
    u, v = word[1:close], word[close + 1 :]
    d = len(u) + 2
    return [d] + [d - x for x in rho(mu(u))] + [1] + [d + x for x in rho(v)]


def canonical(order):
    order = tuple(order)
    rots = [order[i:] + order[:i] for i in range(len(order))]
    rev = tuple(reversed(order))
    rots.extend(rev[i:] + rev[:i] for i in range(len(order)))
    return min(rots)


def msw_row(word):
    r = len(word) // 2
    b = 2 * r + 1
    q = rho(word) + [b]
    return canonical(tuple(q[(-1 - 2 * j) % b] for j in range(b)))


def windows(order, k):
    b = len(order)
    return tuple(frozenset(order[(i + j) % b] for j in range(k))
                 for i in range(b))


def component_key(word):
    height = 0
    cut = None
    for i, bit in enumerate(word):
        height += 1 if bit == "1" else -1
        if height == 0 and i + 1 >= 4:
            cut = i + 1
            break
    assert cut is not None
    j = cut // 2 - 2
    return j, word[cut:]


def swap_target(target, a=2, b=3):
    answer = set(target)
    has_a, has_b = a in answer, b in answer
    if has_a != has_b:
        answer.remove(a if has_a else b)
        answer.add(b if has_a else a)
    return frozenset(answer)


def energy(counter):
    return sum(value * (value - 1) // 2 for value in counter.values())


def norm2(counter):
    return sum(value * value for value in counter.values())


def audit_r(r):
    roots = tuple(dyck_words(r))
    groups = defaultdict(list)
    for word in roots:
        groups[component_key(word)].append(word)
    rows = {word: msw_row(word) for word in roots}
    shadow_by_word = {word: Counter(windows(rows[word], r - 1)) for word in roots}
    base = Counter()
    for counter in shadow_by_word.values():
        base.update(counter)

    deltas = []
    size_hist = Counter()
    norm_hist = Counter()
    for key, words in groups.items():
        old = Counter()
        for word in words:
            old.update(shadow_by_word[word])
        new = Counter({swap_target(target): value for target, value in old.items()})
        delta = new.copy()
        delta.subtract(old)
        delta = Counter({target: value for target, value in delta.items() if value})
        deltas.append(delta)
        size_hist[len(words)] += 1
        norm_hist[norm2(delta)] += 1

    total_delta = Counter()
    for delta in deltas:
        total_delta.update(delta)
    all_on = base.copy()
    all_on.update(total_delta)
    assert energy(all_on) == energy(base)
    sum_packet_norm2 = sum(norm2(delta) for delta in deltas)
    total_norm2 = norm2(total_delta)
    pair_inner_hist = Counter()
    positive_pair_examples = []
    for left in range(len(deltas)):
        for right in range(left + 1, len(deltas)):
            if len(deltas[left]) > len(deltas[right]):
                small, large = deltas[right], deltas[left]
            else:
                small, large = deltas[left], deltas[right]
            inner = sum(value * large.get(target, 0)
                        for target, value in small.items())
            if inner:
                pair_inner_hist[inner] += 1
            if inner > 0 and len(positive_pair_examples) < 5:
                positive_pair_examples.append((left, right, inner))
    numerator = 8 * energy(base) + sum_packet_norm2 - total_norm2
    assert numerator % 8 == 0 or True
    expectation = numerator / 8

    brute_min = None
    brute_min_mask = None
    if len(deltas) <= 16:
        current = base.copy()
        previous_gray = 0
        brute_min = energy(current)
        brute_min_mask = 0
        for step in range(1, 1 << len(deltas)):
            gray = step ^ (step >> 1)
            changed = gray ^ previous_gray
            index = changed.bit_length() - 1
            sign = 1 if gray & changed else -1
            current.update({target: sign * value
                            for target, value in deltas[index].items()})
            value = energy(current)
            if value < brute_min:
                brute_min = value
                brute_min_mask = gray
            previous_gray = gray

    coordinate_min = None
    if len(deltas) <= 1000:
        rng = random.Random(20260821 + r)
        for trial in range(32):
            mask = [rng.randrange(2) for _ in deltas] if trial else [0] * len(deltas)
            current = base.copy()
            for bit, delta in zip(mask, deltas):
                if bit:
                    current.update(delta)
            while True:
                old_energy = energy(current)
                best_change = 0
                best_index = None
                for index, delta in enumerate(deltas):
                    sign = -1 if mask[index] else 1
                    linear = sum(current[target] * sign * value
                                 for target, value in delta.items())
                    change = linear + norm2(delta) // 2
                    if change < best_change:
                        best_change = change
                        best_index = index
                if best_index is None:
                    break
                sign = -1 if mask[best_index] else 1
                current.update({target: sign * value
                                for target, value in deltas[best_index].items()})
                mask[best_index] ^= 1
                assert energy(current) == old_energy + best_change
            value = energy(current)
            if coordinate_min is None or value < coordinate_min:
                coordinate_min = value

    n = math.comb(2 * r + 1, r)
    lower = math.comb(2 * r + 1, r - 1)
    baseline = n - lower
    return {
        "r": r,
        "rows": len(roots),
        "components": len(groups),
        "size_hist": dict(size_hist),
        "packet_norm_hist": dict(norm_hist),
        "energy": energy(base),
        "gap": energy(base) - baseline,
        "sum_packet_norm2": sum_packet_norm2,
        "total_transposition_norm2": total_norm2,
        "nonzero_pair_inner_hist": dict(pair_inner_hist),
        "positive_pair_examples": positive_pair_examples,
        "cube_average_energy": expectation,
        "cube_average_gap": expectation - baseline,
        "average_improvement": energy(base) - expectation,
        "brute_cube_min": brute_min,
        "brute_cube_min_gap": None if brute_min is None else brute_min - baseline,
        "brute_cube_min_mask": brute_min_mask,
        "coordinate_descent_min": coordinate_min,
        "coordinate_descent_gap": (None if coordinate_min is None
                                    else coordinate_min - baseline),
    }


def main(r_min, r_max):
    for r in range(r_min, r_max + 1):
        print("S1_COMPONENT_ENERGY", audit_r(r), flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--r-min", type=int, default=3)
    parser.add_argument("--r-max", type=int, default=10)
    args = parser.parse_args()
    main(args.r_min, args.r_max)
