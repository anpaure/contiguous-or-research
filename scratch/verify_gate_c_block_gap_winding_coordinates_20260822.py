#!/usr/bin/env python3
"""Exact finite audit for Gate-C gap/winding coordinates."""

from itertools import permutations
from random import Random


def inverse(order):
    answer = [0] * len(order)
    for position, value in enumerate(order):
        answer[value] = position
    return answer


def gaps(order):
    sigma = inverse(order)
    k = len(order)
    return [(sigma[(a + 1) % k] - sigma[a]) % k for a in range(k)]


def direct_sign(order, a, u):
    sigma = inverse(order)
    k = len(order)
    position_distance = (sigma[(a + u) % k] - sigma[a]) % k
    return 1 if position_distance % 2 == u % 2 else -1


def winding_sign(ds, a, u):
    k = len(ds)
    segment = [ds[(a + t) % k] for t in range(u)]
    even_count = sum(d % 2 == 0 for d in segment)
    winding = sum(segment) // k
    return 1 if (even_count + winding) % 2 == 0 else -1


def is_good(order, a):
    k = len(order)
    word = [direct_sign(order, a, u) for u in range(1, k)]
    terminal = sum(word)
    height = 0
    for sign in word:
        height += sign
        if not 0 <= height <= terminal:
            return False
    return True


def component_count(vertices, k):
    if not vertices:
        return 0
    assert len(vertices) < k
    return sum(a in vertices and (a - 1) % k not in vertices for a in range(k))


def audit(order):
    k = len(order)
    sigma = inverse(order)
    ds = gaps(order)
    assert all(1 <= d < k for d in ds)
    assert sum(ds) % k == 0
    h = sum(ds) // k
    even_total = sum(d % 2 == 0 for d in ds)
    assert h % 2 == (k - even_total) % 2

    for a in range(k):
        running = 0
        for u in range(1, k):
            running += ds[(a + u - 1) % k]
            remainder = running % k
            assert remainder == (sigma[(a + u) % k] - sigma[a]) % k
            assert direct_sign(order, a, u) == winding_sign(ds, a, u)

    good = {a for a in range(k) if is_good(order, a)}
    bad = set(range(k)) - good
    for a in good:
        assert ds[a] % 2 == 1
        assert ds[(a - 1) % k] % 2 == 1
    even_edges = {a for a, d in enumerate(ds) if d % 2 == 0}
    assert all(a in bad and (a + 1) % k in bad for a in even_edges)
    if len(bad) < k:
        assert len(even_edges) <= len(bad) - component_count(bad, k)

    rebuilt = [sigma[0]]
    for a in range(k - 1):
        rebuilt.append((rebuilt[-1] + ds[a]) % k)
    assert rebuilt == sigma
    assert len(set(rebuilt)) == k


def main():
    total = 0
    for k in (3, 5, 7):
        for order in permutations(range(k)):
            audit(order)
            total += 1

    rng = Random(20260822)
    for k in (9, 11, 13, 21):
        for _ in range(2500):
            order = list(range(k))
            rng.shuffle(order)
            audit(order)
            total += 1

    print("GATE_C_BLOCK_GAP_WINDING_COORDINATES_PASS", f"orders={total}")


if __name__ == "__main__":
    main()
