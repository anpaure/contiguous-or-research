#!/usr/bin/env python3
"""Exact audit of the b-2 monochromatic genuine-wreath construction."""

from __future__ import annotations


def windows(order, size):
    b = len(order)
    return tuple(
        frozenset(order[(end - q) % b] for q in range(size))
        for end in range(b)
    )


def top_excess(x, y, b):
    h = 0
    mn = 0
    for q in range(b):
        h += 1 if q in x else -1
        mn = min(mn, h)
        h += 1 if q in y else -1
        mn = min(mn, h)
    assert h == 0
    return -mn


def prefix_orientation(x, z, b):
    d = 0
    mn = 0
    values = []
    for q in range(b):
        values.append(d)
        d += int(q in x) - int(q in z)
        mn = min(mn, d)
    assert d == 0
    return int(any(values[q] == mn and q not in x and q not in z for q in range(b)))


def audit(b):
    r = (b - 1) // 2
    alpha = (0,) + tuple(range(1, b - 2)) + (b - 1, b - 2)
    beta = (alpha[0],) + tuple(alpha[:0:-1])
    xs = windows(alpha, r)
    ys = windows(beta, r + 1)

    # Reverse-order complement identity.
    for j in range(b):
        assert set(range(b)) - ys[j] == xs[(-j - 1) % b]

    # Exactly two windows differ from the standard translated intervals.
    standard = windows(tuple(range(b)), r)
    e, f = r - 2, 2 * r - 1
    changed = [i for i in range(b) if xs[i] != standard[i]]
    assert changed == [e, f]
    assert xs[e] == standard[e] - {2 * r} | {2 * r - 1}
    assert xs[f] == standard[f] - {2 * r - 1} | {2 * r}

    phase = []
    for p in range(b):
        parities = []
        for i in range(b):
            j = (p - i) % b
            k = top_excess(xs[i], ys[j], b)
            z = set(range(b)) - ys[j]
            assert (k & 1) == prefix_orientation(xs[i], z, b)
            parities.append(k & 1)
        vals = set(parities)
        phase.append(next(iter(vals)) if len(vals) == 1 else None)

    expected = [None] + [0] * (r - 1) + [None] + [1] * r
    assert phase == expected, (b, phase, expected)

    # The persistent word has one equal edge; exhaust its cyclic shifts and
    # verify the displayed loose r+1 agreement bound.
    rank = lambda x: (r * x) % b
    tau = [int(rank(x) < r) for x in range(b)]
    assert sum(tau[p] == tau[(p + 1) % b] for p in range(b)) == 1
    best = max(
        sum(phase[p] is not None and phase[p] == (tau[(p + shift) % b] ^ flip) for p in range(b))
        for shift in range(b) for flip in (0, 1)
    )
    assert best <= r + 1
    return b, sum(x is not None for x in phase), best


def main():
    for b in range(5, 202, 2):
        print(audit(b))
    print("PASS audit_genuine_wreath_b_minus_two_gk_monochromatic_phases_20260821")


if __name__ == "__main__":
    main()
