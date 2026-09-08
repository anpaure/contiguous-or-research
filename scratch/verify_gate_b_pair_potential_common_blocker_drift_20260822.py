#!/usr/bin/env python3
"""Finite audit for the Gate-B pair-potential/common-blocker note."""

from fractions import Fraction
from itertools import combinations, permutations
from math import comb, factorial, isqrt


def check_finite_deletion_and_tangent():
    windows = [frozenset((0, 1)), frozenset((0, 2)),
               frozenset((1, 2)), frozenset((2, 3))]
    z = len(windows)
    targets = range(4)
    c = [[len(windows[f] & windows[g]) for g in range(z)] for f in range(z)]
    x = [sum(t in windows[f] for f in range(z)) for t in targets]
    s = sum(sum(row) for row in c)
    assert s == sum(v * v for v in x)

    # Closed neighborhoods of the path 0--1--2--3.
    gamma = []
    for h in range(z):
        gh = {h}
        if h:
            gh.add(h - 1)
        if h + 1 < z:
            gh.add(h + 1)
        gamma.append(gh)

    for bset in ({1}, {0, 2}, {1, 2, 3}):
        y = [sum(t in windows[f] for f in bset) for t in targets]
        rb = sum(a * b for a, b in zip(x, y))
        qb = sum(b * b for b in y)
        lb = 2 * rb - qb
        keep = [f for f in range(z) if f not in bset]
        sprime = sum(c[f][g] for f in keep for g in keep)
        assert sprime == s - lb
        lost = sum(c[f][g] for f in range(z) for g in range(z)
                   if f in bset or g in bset)
        assert lost == lb

    ch = [len(g) for g in gamma]
    lh = []
    for h in range(z):
        lh.append(sum(c[f][g] for f in range(z) for g in range(z)
                      if f in gamma[h] or g in gamma[h]))
    derivative_a = -Fraction(sum(lh), s) + 2 * Fraction(sum(ch), z)

    wf = [sum(c[f]) for f in range(z)]
    jfg = [[len(gamma[f] & gamma[g]) for g in range(z)] for f in range(z)]
    derivative_b = Fraction(
        sum(c[f][g] * jfg[f][g] for f in range(z) for g in range(z)), s
    ) + 2 * (Fraction(sum(ch), z) -
             Fraction(sum(wf[f] * ch[f] for f in range(z)), s))
    assert derivative_a == derivative_b
    return derivative_a


def check_independent_blocker_benchmark():
    windows = [frozenset((0, 1)), frozenset((1, 2)),
               frozenset((2, 3)), frozenset((3, 0))]
    z = len(windows)
    c = [[len(windows[f] & windows[g]) for g in range(z)] for f in range(z)]
    s = sum(sum(row) for row in c)
    gamma = [{h, (h - 1) % z, (h + 1) % z} for h in range(z)]
    c0 = len(gamma[0])
    assert all(len(g) == c0 for g in gamma)
    p = Fraction(1, 5)
    ez = Fraction(0)
    es = Fraction(0)
    for mask in range(1 << z):
        active = {h for h in range(z) if mask >> h & 1}
        probability = p ** len(active) * (1 - p) ** (z - len(active))
        deleted = set().union(*(gamma[h] for h in active)) if active else set()
        keep = [f for f in range(z) if f not in deleted]
        ez += probability * len(keep)
        es += probability * sum(c[f][g] for f in keep for g in keep)
    factor = (es / (ez * ez)) / Fraction(s, z * z)
    escort = Fraction(0)
    for f in range(z):
        for g in range(z):
            escort += Fraction(c[f][g], s) * (1 - p) ** (-len(gamma[f] & gamma[g]))
    assert factor == escort


def mpos(n, h1, h2, s):
    if s < 0 or s > min(h1, h2):
        return 0
    if s == 0:
        return n - h1 - h2 + 1
    if s < min(h1, h2):
        return 2
    return abs(h1 - h2) + 1


def codegree(r, h1, h2, s):
    n = 2 * r + 1
    m = mpos(n, h1, h2, s)
    if not m:
        return 0
    positional = (n - 2) * m + (s == min(h1, h2))
    cells = (s, h1 - s, h2 - s, n - h1 - h2 + s)
    if min(cells) < 0:
        return 0
    ans = positional
    for cell in cells:
        ans *= factorial(cell)
    return ans


def weight(r, q, h, a):
    n = 2 * r + 1
    k = r - q
    ell = n - k
    if not (0 <= a <= min(k, h) and 0 <= h - a <= ell):
        return Fraction(0)
    m = mpos(n, k, h, a)
    return Fraction(n - 1, n) * Fraction(
        m, comb(k, a) * comb(ell, h - a)
    )


def mult4(n, cells):
    if min(cells) < 0 or sum(cells) != n:
        return 0
    ans = factorial(n)
    for cell in cells:
        ans //= factorial(cell)
    return ans


def orbit_q(r, q):
    n = 2 * r + 1
    k = r - q
    ell = n - k
    total = Fraction(0)
    for h1 in (r - 1, r):
        for h2 in (r - 1, r):
            for a in range(k + 1):
                wa = weight(r, q, h1, a)
                if not wa:
                    continue
                for ap in range(k + 1):
                    wap = weight(r, q, h2, ap)
                    if not wap:
                        continue
                    for t in range(k + 1):
                        mt = mult4(k, (t, a - t, ap - t, k - a - ap + t))
                        if not mt:
                            continue
                        for u in range(ell + 1):
                            mu = mult4(ell, (
                                u, h1 - a - u, h2 - ap - u,
                                ell - h1 + a - h2 + ap + u,
                            ))
                            if mu:
                                total += mt * mu * wa * wap * codegree(
                                    r, h1, h2, t + u
                                )
    return total


def direct_target_q(r, q):
    n = 2 * r + 1
    k = r - q
    tset = frozenset(range(k))
    vertices = []
    for h in (r - 1, r):
        for v in combinations(range(n), h):
            v = frozenset(v)
            vertices.append((h, v, weight(r, q, h, len(v & tset))))
    total = Fraction(0)
    for h1, v1, w1 in vertices:
        if not w1:
            continue
        for h2, v2, w2 in vertices:
            if w2:
                total += w1 * w2 * codegree(r, h1, h2, len(v1 & v2))
    return total


def dominant_q2(r):
    n = 2 * r + 1
    ell = r + 3
    dm = 2 * r * factorial(r) * factorial(r + 1)
    dl = Fraction(r + 2, r) * dm
    lam = 2 * (2 * r - 1) * factorial(r - 2) * factorial(r + 1)
    c0 = Fraction(n - 1, n) * Fraction(2, ell)
    return c0 * c0 * (ell * dl + ell * (ell - 1) * lam)


def check_orbit_formula():
    rows = []
    for r, q in ((3, 2), (4, 2), (5, 2), (5, 3)):
        a = orbit_q(r, q)
        b = direct_target_q(r, q)
        assert a == b
        dm = 2 * r * factorial(r) * factorial(r + 1)
        if q == 2:
            dom = dominant_q2(r)
            assert 0 < dom <= a
        rows.append((r, q, float(a / dm), float(r * a / dm)))
    return rows


def brute_i_r3():
    # A direct bitset audit of I_q <= Q_q at r=3,q=2.
    r, q = 3, 2
    n = 2 * r + 1
    perms = list(permutations(range(n)))
    lower = list(combinations(range(n), r - 1))
    middle = list(combinations(range(n), r))
    lid = {frozenset(v): i for i, v in enumerate(lower)}
    mid = {frozenset(v): len(lower) + i for i, v in enumerate(middle)}
    vertex_data = ([('L', frozenset(v)) for v in lower]
                   + [('M', frozenset(v)) for v in middle])
    decks = []
    stars = [0] * (len(lower) + len(middle))
    for idx, p in enumerate(perms):
        deck = []
        for start in range(1, n):
            lv = frozenset(p[(start + j) % n] for j in range(r - 1))
            mv = frozenset(p[(start + j) % n] for j in range(r))
            deck.extend((lid[lv], mid[mv]))
        deck = frozenset(deck)
        decks.append(deck)
        bit = 1 << idx
        for v in deck:
            stars[v] |= bit

    # Independent exhaustive checks of the central pair-codegree and
    # mixed-root one-target formulas.
    for i, (_, vi) in enumerate(vertex_data):
        hi = len(vi)
        expected_weight = weight(r, q, hi, len(vi & frozenset((0,))))
        assert Fraction(stars[i].bit_count(), len(perms)) == expected_weight
        for j, (_, vj) in enumerate(vertex_data):
            actual = (stars[i] & stars[j]).bit_count()
            assert actual == codegree(r, hi, len(vj), len(vi & vj))
    all_bits = (1 << len(perms)) - 1  # every row contains a singleton T
    isum = 0
    for deck in decks:
        neigh = 0
        for v in deck:
            neigh |= stars[v]
        a = (neigh & all_bits).bit_count()
        isum += a * a
    dq = n * factorial(r - q) * factorial(r + 1 + q)
    iq = Fraction(isum, dq * dq)
    qq = orbit_q(r, q)
    assert iq <= qq
    return float(iq / (2 * r * factorial(r) * factorial(r + 1)))


def check_reciprocal_binomial_scales():
    records = []
    for r in (64, 100, 144, 256, 400, 1024):
        n = 2 * r + 1
        qmax = isqrt(r) // 4
        for q in range(2, qmax + 1):
            k = r - q
            ell = n - k
            norm = Fraction(0)
            for h in (r - 1, r):
                for a in range(k + 1):
                    w = weight(r, q, h, a)
                    if w:
                        norm += comb(k, a) * comb(ell, h - a) * w * w
            if q == 2:
                c0 = Fraction(n - 1, n) * Fraction(2, r + 3)
                lower = (r + 3) * c0 * c0
                assert 0 <= norm - lower <= Fraction(19, r * r)
                dm = 2 * r * factorial(r) * factorial(r + 1)
                scaled = Fraction(r) * dominant_q2(r) / dm
                assert 4 <= scaled <= Fraction(17, 4)
            else:
                assert norm <= Fraction(19, r * r)
        records.append((r, qmax))
    return records


def main():
    derivative = check_finite_deletion_and_tangent()
    check_independent_blocker_benchmark()
    rows = check_orbit_formula()
    i3 = brute_i_r3()
    scale_records = check_reciprocal_binomial_scales()
    print("finite deletion/tangent identity: PASS", derivative)
    print("orbit formula/direct target sum: PASS")
    for row in rows:
        print("r=%d q=%d Q/DM=%.12g rQ/DM=%.12g" % row)
    print("direct r=3 q=2 I/DM=%.12g and I<=Q: PASS" % i3)
    print("reciprocal-binomial shallow scales: PASS", scale_records)
    print("PASS")


if __name__ == "__main__":
    main()
