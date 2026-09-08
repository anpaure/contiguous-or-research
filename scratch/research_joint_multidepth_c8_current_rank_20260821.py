#!/usr/bin/env python3
"""Rank of the joint all-depth abstract C8 current system.

Exact enumeration is used at r=4; random template sampling tests the precise
direct-sum conjecture at larger r.  Intended execution: H100 only.
"""

from __future__ import annotations

import argparse
import math
import random
from collections import Counter
from itertools import combinations, permutations


PRIMES = (2, 3, 5, 1_000_003)


class ModularRanker:
    def __init__(self, prime):
        self.prime = prime
        self.basis = {}

    def add(self, sparse):
        p = self.prime
        vector = {row: value % p for row, value in sparse.items() if value % p}
        while vector:
            pivot = min(vector)
            if pivot not in self.basis:
                inverse = pow(vector[pivot], p - 2, p)
                self.basis[pivot] = {
                    row: value * inverse % p for row, value in vector.items()
                }
                return True
            scale = vector[pivot]
            for row, value in self.basis[pivot].items():
                updated = (vector.get(row, 0) - scale * value) % p
                if updated:
                    vector[row] = updated
                elif row in vector:
                    del vector[row]
        return False

    @property
    def rank(self):
        return len(self.basis)


def target_system(n, r):
    offsets = {}
    indices = {}
    offset = 0
    for k in range(2, r):
        targets = tuple(frozenset(target) for target in combinations(range(n), k))
        offsets[k] = offset
        indices[k] = {target: offset + index for index, target in enumerate(targets)}
        offset += len(targets)
    return offsets, indices, offset


def transfer(counter, core, b, c, sign):
    if b in core or c in core:
        raise AssertionError
    counter[frozenset(core | {c})] += sign
    counter[frozenset(core | {b})] -= sign


def joint_current(P, Q, b, c, r, indices):
    sparse = {}
    for k in range(2, r):
        t = k - 1
        layer = Counter()
        transfer(layer, set(P[:t]), b, c, 1)
        transfer(layer, set(Q[:t]), b, c, 1)
        transfer(layer, set(P[-t:]), b, c, -1)
        transfer(layer, set(Q[-t:]), b, c, -1)
        layer = Counter({target: value for target, value in layer.items() if value})
        for target, value in layer.items():
            sparse[indices[k][target]] = value
        assert sum(layer.values()) == 0
        for point in range(2 * r + 1):
            assert sum(value for target, value in layer.items() if point in target) == 0
    return sparse


def exact_templates_r4(n):
    ground = tuple(range(n))
    for b, c in combinations(ground, 2):
        remaining = tuple(point for point in ground if point not in (b, c))
        for P in permutations(remaining, 3):
            after_p = tuple(point for point in remaining if point not in P)
            for Q in permutations(after_p, 2):
                yield P, Q, b, c


def random_templates(n, r, samples, seed):
    rng = random.Random(seed)
    ground = list(range(n))
    for _ in range(samples):
        rng.shuffle(ground)
        b, c = ground[0], ground[1]
        P = tuple(ground[2:r + 1])
        Q = tuple(ground[r + 1:2 * r - 1])
        yield P, Q, b, c


def audit_r(r, samples):
    n = 2 * r + 1
    offsets, indices, ambient = target_system(n, r)
    expected = sum(math.comb(n, k) - n for k in range(2, r))
    joint_rankers = {prime: ModularRanker(prime) for prime in PRIMES}
    layer_rankers = {
        k: {prime: ModularRanker(prime) for prime in PRIMES}
        for k in range(2, r)
    }
    templates = exact_templates_r4(n) if r == 4 else random_templates(
        n, r, samples, 20260821 + r
    )
    template_count = 0
    last_growth = 0
    for template_count, (P, Q, b, c) in enumerate(templates, 1):
        current = joint_current(P, Q, b, c, r, indices)
        grew = False
        for prime, ranker in joint_rankers.items():
            grew |= ranker.add(current)
        for k in range(2, r):
            lo = offsets[k]
            hi = lo + math.comb(n, k)
            layer = {row - lo: value for row, value in current.items()
                     if lo <= row < hi}
            for prime, ranker in layer_rankers[k].items():
                ranker.add(layer)
        if grew:
            last_growth = template_count
        if all(ranker.rank == expected for ranker in joint_rankers.values()):
            break
    return {
        "r": r,
        "ambient": ambient,
        "expected_direct_sum_kernel_rank": expected,
        "templates": template_count,
        "last_joint_growth": last_growth,
        "joint_ranks": {prime: ranker.rank
                        for prime, ranker in joint_rankers.items()},
        "layer_ranks": {
            k: {prime: ranker.rank for prime, ranker in rankers.items()}
            for k, rankers in layer_rankers.items()
        },
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--r-min", type=int, default=4)
    parser.add_argument("--r-max", type=int, default=6)
    parser.add_argument("--samples", type=int, default=500_000)
    arguments = parser.parse_args()
    for rank in range(arguments.r_min, arguments.r_max + 1):
        print("JOINT_MULTIDEPTH_C8_RANK", audit_r(rank, arguments.samples),
              flush=True)
