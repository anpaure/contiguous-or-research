#!/usr/bin/env python3
"""Audit complete cyclic owner-interval decks across the explicit GK C10.

This constructs the literal odd GK/complement factor, performs the five
edge switch, and compares old/new *support sets* of unions of all cyclic
owner intervals.  Substantive runs belong on h100.
"""

from __future__ import annotations

import argparse
import itertools
from collections import defaultdict


def masks(n, rank):
    for cc in itertools.combinations(range(n), rank):
        z = 0
        for x in cc:
            z |= 1 << x
        yield z


def unmatched(word, n):
    stack = []
    ones = []
    for i in range(n):
        if word >> i & 1:
            if stack:
                stack.pop()
            else:
                ones.append(i)
        else:
            stack.append(i)
    return ones, stack


def gk_up(word, n):
    return word | (1 << unmatched(word, n)[1][0])


def gk_down(word, n):
    return word ^ (1 << unmatched(word, n)[0][-1])


def complement_up(word, n):
    full = (1 << n) - 1
    return full ^ gk_down(full ^ word, n)


def explicit_c10(m):
    def bits(s):
        assert len(s) == 2 * m + 1
        return sum((c == "1") << i for i, c in enumerate(s))

    A = [
        bits("0" * (m - 1) + "1" * (m + 1) + "0"),
        bits("1" + "0" * (m - 2) + "1" * m + "00"),
        bits("11" + "0" * (m - 3) + "1" * (m - 1) + "000"),
        bits("1" + "0" * (m - 2) + "1" * (m - 1) + "010"),
        bits("0" * (m - 1) + "1" * (m - 1) + "011"),
    ]
    B = [
        bits("0" * m + "1" * (m + 1)),
        bits("1" + "0" * (m - 1) + "1" * m + "0"),
        bits("11" + "0" * (m - 2) + "1" * (m - 1) + "00"),
        bits("11" + "0" * (m - 2) + "1" * (m - 2) + "010"),
        bits("1" + "0" * (m - 1) + "1" * (m - 2) + "011"),
    ]
    return A, B


def build_edges(m):
    n = 2 * m + 1
    edges = []
    for low in masks(n, m):
        a = gk_up(low, n)
        b = complement_up(low, n)
        assert a != b and (a ^ b).bit_count() == 2
        edges.append(tuple(sorted((a, b))))
    assert len(set(edges)) == len(edges)
    return n, edges


def cycles(edges):
    adj = defaultdict(list)
    for eid, (a, b) in enumerate(edges):
        adj[a].append((b, eid))
        adj[b].append((a, eid))
    assert all(len(xs) == 2 for xs in adj.values())
    used = set()
    out = []
    for seed in range(len(edges)):
        if seed in used:
            continue
        a, _ = edges[seed]
        vertices = [a]
        cur = a
        eid = seed
        while True:
            assert eid not in used
            used.add(eid)
            x, y = edges[eid]
            nxt = y if cur == x else x
            if nxt == vertices[0]:
                break
            vertices.append(nxt)
            opts = [ne for _, ne in adj[nxt] if ne != eid]
            assert len(opts) == 1
            cur, eid = nxt, opts[0]
        out.append(vertices)
    return out


def deck(cycs, full):
    support = {}
    for cid, cyc in enumerate(cycs):
        length = len(cyc)
        for start in range(length):
            value = 0
            for width in range(1, length + 1):
                value |= cyc[(start + width - 1) % length]
                support.setdefault(value, (width, cid, start))
                if value == full:
                    break
    return support


def word(mask, n):
    return "".join("1" if mask >> i & 1 else "0" for i in range(n))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("m", type=int)
    args = ap.parse_args()
    m = args.m
    n, old_edges = build_edges(m)
    A, B = explicit_c10(m)
    old_set = set(old_edges)
    removed = {tuple(sorted((A[i], B[i]))) for i in range(5)}
    added = {tuple(sorted((A[i], B[(i + 1) % 5]))) for i in range(5)}
    assert len(removed) == len(added) == 5 and removed <= old_set
    new_edges = [e for e in old_edges if e not in removed] + sorted(added)
    assert len(set(new_edges)) == len(new_edges) == len(old_edges)

    old_cycles = cycles(old_edges)
    new_cycles = cycles(new_edges)
    full = (1 << n) - 1
    old_deck = deck(old_cycles, full)
    new_deck = deck(new_cycles, full)
    casualties = set(old_deck) - set(new_deck)
    births = set(new_deck) - set(old_deck)
    print(
        "GK_C10_DECK",
        f"m={m}",
        f"owners={len(old_edges)}",
        f"components={len(old_cycles)}->{len(new_cycles)}",
        f"support={len(old_deck)}->{len(new_deck)}",
        f"casualties={len(casualties)}",
        f"births={len(births)}",
    )
    if casualties:
        target = min(casualties, key=lambda z: (old_deck[z][0], z.bit_count(), z))
        width, cid, start = old_deck[target]
        cyc = old_cycles[cid]
        vals = [cyc[(start + j) % len(cyc)] for j in range(width)]
        print(
            "MIN_CASUALTY",
            f"owner_width={width}",
            f"rank={target.bit_count()}",
            f"component_length={len(cyc)}",
            f"target={word(target,n)}",
        )
        print("INTERVAL", " ".join(word(z, n) for z in vals))


if __name__ == "__main__":
    main()
