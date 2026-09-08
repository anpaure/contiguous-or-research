#!/usr/bin/env python3
"""Exact diagnostics for the MNW Dyck cycle factor as a wreath bank.

Run only on H100.  This reconstructs the cycle C(x) for every Dyck word x,
extracts its edge-hole order, converts that order to an ordinary cyclic
coordinate order, and audits window decks at every rank.
"""

from __future__ import annotations

import argparse
from collections import Counter
from itertools import combinations
from math import comb


def dyck_words(r: int):
    def rec(pos: int, up: int, down: int, bits: list[int]):
        if pos == 2 * r:
            if up == down == r:
                yield tuple(bits)
            return
        if up < r:
            bits.append(1)
            yield from rec(pos + 1, up + 1, down, bits)
            bits.pop()
        if down < up:
            bits.append(0)
            yield from rec(pos + 1, up, down + 1, bits)
            bits.pop()
    yield from rec(0, 0, 0, [])


def mirror(x: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(1 - z for z in reversed(x))


def pi_dyck(x: tuple[int, ...]) -> tuple[int, ...]:
    """MNW recursion, with positions numbered 0,...,|x|-1."""
    if not x:
        return ()
    height = 0
    cut = None
    for i, bit in enumerate(x):
        height += 1 if bit else -1
        if height == 0:
            cut = i
            break
    assert cut is not None and x[0] == 1 and x[cut] == 0
    u = x[1:cut]
    v = x[cut + 1 :]
    pivot = len(u) + 1  # zero-based version of |u|+2
    return (
        (pivot,)
        + tuple(pivot - 1 - j for j in pi_dyck(mirror(u)))
        + (0,)
        + tuple(pivot + 1 + j for j in pi_dyck(v))
    )


def mask(bits: tuple[int, ...]) -> int:
    return sum(bit << i for i, bit in enumerate(bits))


def odd_vertex(bits: tuple[int, ...], r: int) -> int:
    first = mask(bits)
    if sum(bits) == r:
        return first
    assert sum(bits) == r + 1
    low_full = (1 << (2 * r)) - 1
    return (low_full ^ first) | (1 << (2 * r))


def cycle_and_holes(x: tuple[int, ...], r: int):
    b = 2 * r + 1
    full = (1 << b) - 1
    p = pi_dyck(x)
    state = list(x)
    vertices = [odd_vertex(tuple(state), r)]
    for a in p:
        state[a] ^= 1
        vertices.append(odd_vertex(tuple(state), r))
    assert len(vertices) == b
    holes = []
    for i in range(b):
        u, v = vertices[i], vertices[(i + 1) % b]
        assert not (u & v)
        h = full ^ (u | v)
        assert h and not h & (h - 1)
        holes.append(h.bit_length() - 1)
    return tuple(vertices), tuple(holes)


def coordinate_order_from_holes(holes: tuple[int, ...], r: int):
    """Choose c with hole at jump-cycle time t equal c[tr-1]."""
    b = 2 * r + 1
    c = [None] * b
    for t, h in enumerate(holes):
        c[(t * r - 1) % b] = h
    assert sorted(c) == list(range(b))
    return tuple(c)


def windows(order: tuple[int, ...], ell: int):
    b = len(order)
    return tuple(
        sum(1 << order[(i + j) % b] for j in range(ell)) for i in range(b)
    )


def one_r(r: int):
    b = 2 * r + 1
    bank = []
    central = Counter()
    rank_counts = [Counter() for _ in range(b + 1)]
    for x in dyck_words(r):
        verts, holes = cycle_and_holes(x, r)
        assert holes[:-1] == pi_dyck(x)
        assert holes[-1] == 2 * r
        order = coordinate_order_from_holes(holes, r)
        assert set(windows(order, r)) == set(verts)
        bank.append((x, order, verts))
        central.update(verts)
        for ell in range(1, b):
            rank_counts[ell].update(windows(order, ell))
    assert len(bank) == comb(2 * r, r) // (r + 1)
    assert len(central) == comb(b, r)
    assert set(central.values()) == {1}
    print(
        "R",
        r,
        "B",
        b,
        "CYCLES",
        len(bank),
        "CENTRAL_PARTITION",
        len(central),
        flush=True,
    )
    for ell in range(1, b):
        vals = rank_counts[ell]
        hist = Counter(vals.values())
        missing = comb(b, ell) - len(vals)
        print(
            "RANK",
            ell,
            "TARGETS",
            comb(b, ell),
            "SUPPORT",
            len(vals),
            "MISSING",
            missing,
            "MULT_MIN_MAX",
            (min(vals.values(), default=0), max(vals.values(), default=0)),
            "HIST",
            sorted(hist.items())[:20],
            flush=True,
        )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--r-min", type=int, default=2)
    parser.add_argument("--r-max", type=int, default=6)
    args = parser.parse_args()
    for r in range(args.r_min, args.r_max + 1):
        one_r(r)


if __name__ == "__main__":
    main()
