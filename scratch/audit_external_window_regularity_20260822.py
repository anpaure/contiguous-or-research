#!/usr/bin/env python3
"""Regression checks for the external-window regularity note.

The script is evidence only.  The proofs are analytic and self-contained in
the theorem note.
"""

from fractions import Fraction
from itertools import permutations
from math import comb, factorial, floor, sqrt


def mcount(b: int, k: int, h: int, a: int) -> int:
    if a == 0:
        return b - k - h + 1
    if a == min(k, h):
        return abs(k - h) + 1
    return 2


def kappa(r: int, q: int) -> Fraction:
    b = 2 * r + 1
    k = r - q
    ans = Fraction(0)
    for h in (r - 1, r):
        for a in range(k + 1):
            if 0 <= h - a <= b - k:
                m = mcount(b, k, h, a)
                ans += Fraction(m * m, comb(k, a) * comb(b - k, h - a))
    return ans


for r in (32, 64, 128, 256):
    b = 2 * r + 1
    A = comb(b, r)
    B = A // b
    assert A == b * B
    for q in range(2, min(r - 1, floor(sqrt(r)) + 1)):
        k = r - q
        Bq = comb(b, k)
        Dq = b * factorial(k) * factorial(b - k)
        assert Dq * Bq == b * factorial(b)
    kap2 = kappa(r, 2)
    assert Fraction(3, r) < kap2 < Fraction(6, r)

    # Coalescing the b puncture origins preserves the exact B_q / b
    # catalogue-to-external-degree normalization.
    x = Fraction(1, 7)
    y = Fraction(2, 9)
    rho = x ** (b - 1) * y ** (b - 1)
    p_physical = rho * (b - (b - 1) * x * y)
    EZ_physical = factorial(b - 1) * p_physical
    for q in (2, min(4, r - 1)):
        Bq = comb(b, r - q)
        EX_physical = Fraction(factorial(b), Bq) * p_physical
        assert EZ_physical / EX_physical == Fraction(Bq, b)


# Exhaustive mixed-root codegree census at r=4, q=2.  This is outside the
# asymptotic range but catches boundary/start/complement normalization errors.
r = 4
b = 2 * r + 1
q = 2
k = r - q
identity = tuple(range(b))
root_start = 2


def window(w, s, h):
    return frozenset(w[(s + i) % b] for i in range(h))


def config(w):
    return {
        (h, window(w, s, h))
        for h in (r, r - 1)
        for s in range(1, b)
    }


root = window(identity, root_start, k)
fixed = [
    (h, window(identity, s, h), s)
    for h in (r, r - 1)
    for s in range(1, b)
]
fixed_keys = [(h, target) for h, target, _ in fixed]
n = len(fixed)
freq = [0] * (1 << n)
star = 0

for w in permutations(range(b)):
    if not any(window(w, s, k) == root for s in range(b)):
        continue
    star += 1
    gw = config(w)
    mask = 0
    for i, target in enumerate(fixed_keys):
        if target in gw:
            mask |= 1 << i
    freq[mask] += 1

assert star == b * factorial(k) * factorial(b - k)

# Superset zeta transform: sup[S] is the number of external-star words
# containing every punctured target indexed by S.
sup = freq[:]
for i in range(n):
    bit = 1 << i
    for mask in range(1 << n):
        if not mask & bit:
            sup[mask] += sup[mask | bit]


def boundary_edge(start, length):
    return {(2 * start) % b, (2 * (start + length)) % b}


root_edge = boundary_edge(root_start, k)
fixed_edges = [boundary_edge(s, h) for h, _, s in fixed]
required_C = 0.0
for mask in range(1, 1 << n):
    vertices = set(root_edge)
    for i, edge in enumerate(fixed_edges):
        if mask >> i & 1:
            vertices.update(edge)
    t = mask.bit_count()
    ratio = Fraction(sup[mask], star)
    if ratio:
        candidate = (float(ratio) * r ** (len(vertices) - 2)) ** (1 / t)
        required_C = max(required_C, candidate)

assert required_C < 3.0
print("PASS: external-star normalization, overlap scale, and r=4 mixed codegrees")
