#!/usr/bin/env python3
"""H100 exploration of local/product atom overlap matrices at b=7."""

from __future__ import annotations

import itertools
import random
from collections import defaultdict, deque

import numpy as np


def cyclic_deck(order, rank):
    b = len(order)
    return frozenset(
        frozenset(order[(i + j) % b] for j in range(rank))
        for i in range(b)
    )


def exact_rank3_factor_b7():
    ground = range(7)
    universe = frozenset(frozenset(x) for x in itertools.combinations(ground, 3))
    by_deck = {}
    for tail in itertools.permutations(range(1, 7)):
        order = (0,) + tail
        if order[1] > order[-1]:
            continue
        deck = cyclic_deck(order, 3)
        by_deck.setdefault(deck, order)
    decks = list(by_deck)
    candidates = defaultdict(list)
    for i, deck in enumerate(decks):
        for triple in deck:
            candidates[triple].append(i)

    def search(uncovered, chosen):
        if not uncovered:
            return chosen
        triple = min(
            uncovered,
            key=lambda x: sum(decks[i] <= uncovered for i in candidates[x]),
        )
        for i in candidates[triple]:
            deck = decks[i]
            if deck <= uncovered:
                result = search(uncovered - deck, chosen + [i])
                if result is not None:
                    return result
        return None

    solution = search(universe, [])
    assert solution is not None and len(solution) == 5
    orders = [by_deck[decks[i]] for i in solution]
    assert frozenset().union(*(cyclic_deck(x, 3) for x in orders)) == universe
    return orders


def walecki_factor(b):
    h = (b - 1) // 2
    inf = b - 1
    base = [inf]
    for j in range(h):
        base.extend([j, (-j - 1) % (b - 1)])
    return [
        tuple(inf if x == inf else (x + shift) % (b - 1) for x in base)
        for shift in range(h)
    ]


def base_factors():
    b = 7
    rank3 = exact_rank3_factor_b7()
    rank2 = walecki_factor(b)
    return {
        1: [tuple(range(b))],
        2: rank2,
        3: rank3,
        4: rank3,
        5: rank2,
        6: [tuple(range(b))],
    }


def conjugated_decks(orders, rank, perm):
    return [cyclic_deck(tuple(perm[x] for x in order), rank) for order in orders]


def comp_count(matrix):
    nl, nr = matrix.shape
    seen = set()
    count = 0
    for start in range(nl + nr):
        if start in seen:
            continue
        count += 1
        seen.add(start)
        queue = deque([start])
        while queue:
            v = queue.popleft()
            if v < nl:
                neighbors = (nl + int(j) for j in np.flatnonzero(matrix[v]))
            else:
                neighbors = (int(i) for i in np.flatnonzero(matrix[:, v - nl]))
            for w in neighbors:
                if w not in seen:
                    seen.add(w)
                    queue.append(w)
    return count


def main():
    rng = random.Random(20260821)
    factors = base_factors()
    b = 7
    for trial in range(12):
        print("TRIAL", trial)
        for rank in range(1, b):
            p = list(range(b))
            q = list(range(b))
            rng.shuffle(p)
            rng.shuffle(q)
            left = conjugated_decks(factors[rank], rank, p)
            right = conjugated_decks(factors[rank], rank, q)
            matrix = np.array([[len(x & y) for y in right] for x in left], float)
            assert np.all(matrix.sum(axis=0) == b)
            assert np.all(matrix.sum(axis=1) == b)
            singular = np.linalg.svd(matrix / b, compute_uv=False)
            print(
                rank,
                {
                    "decks": len(left),
                    "components": comp_count(matrix),
                    "singular": [round(float(x), 6) for x in singular],
                    "matrix": matrix.astype(int).tolist(),
                },
            )


if __name__ == "__main__":
    main()

