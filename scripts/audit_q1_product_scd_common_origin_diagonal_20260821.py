#!/usr/bin/env python3
"""Finite checks for the q=1 common-origin diagonal obstruction."""

from itertools import product


def mismatches(p, q, r, theta):
    b = len(p)
    a_diagonals = {(theta + step) % b for step in range(r)}
    bad = 0
    for u in range(b):
        for v in range(b):
            physical_a = (u + v) % b in a_diagonals
            desired_a = p[u] < q[v]
            desired_b = p[u] > q[v]
            bad += (desired_a and not physical_a) or (desired_b and physical_a)
    return bad


# Exhaust all bottom-rank sequences at the first nontrivial prime size.
b = 5
values = range(3)
checked = 0
for p in product(values, repeat=b):
    for q in product(values, repeat=b):
        active = any(x != y for x in p for y in q)
        for r in range(1, b):
            lower = min(r, b - r) if active else 0
            for theta in range(b):
                bad = mismatches(p, q, r, theta)
                assert bad >= lower
                if bad == 0:
                    assert len(set(p)) == len(set(q)) == 1 and p[0] == q[0]
        checked += 1


def phase_map_check(block_size, rank, theta):
    seen = set()
    for block in range(block_size):
        for phase in range(block_size):
            a_before = min(phase, rank)
            b_before = phase - a_before
            u = (rank * block + a_before) % block_size
            v = ((block_size - rank) * block + b_before + theta) % block_size
            assert phase == (u + v - theta) % block_size
            seen.add((u, v))
    assert len(seen) == block_size * block_size


for prime in (5, 7, 11, 13):
    for rank in range(1, prime):
        for origin in range(prime):
            phase_map_check(prime, rank, origin)

print("PASS")
print("exhaustive b=5 sequence pairs:", checked)
print("phase-cell bijection: primes 5,7,11,13 PASS")
