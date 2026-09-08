#!/usr/bin/env python3
"""Search short alternating incidence cycles joining two T2 suffix copies.

This script is intended for H100 only for substantive instances.  It builds
the exact canonical MSW incidence factor, applies every suffix-tensored T2
macro, and searches the directed exchange graph

    owner -- unselected colour -- selected owner.

A directed owner cycle is precisely an alternating incidence cycle.  The
script records its exact q2 support current.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict, deque


def bits(word: str) -> int:
    return sum((c == "1") << i for i, c in enumerate(word))


def bitword(x: int, n: int) -> str:
    return format(x, f"0{n}b")[::-1]


def dyck_words(m: int):
    def rec(pos: int, bal: int, ones: int, out: list[str]):
        if pos == 2 * m:
            if bal == 0:
                yield "".join(out)
            return
        if ones < m:
            out.append("1")
            yield from rec(pos + 1, bal + 1, ones + 1, out)
            out.pop()
        zeros = pos - ones
        if zeros < ones:
            out.append("0")
            yield from rec(pos + 1, bal - 1, ones, out)
            out.pop()

    yield from rec(0, 0, 0, [])


def dyck(x: int, m: int) -> bool:
    h = 0
    for i in range(2 * m):
        h += 1 if x >> i & 1 else -1
        if h < 0:
            return False
    return h == 0


def g(x: int, m: int) -> int:
    before = []
    h = d0 = 0
    for i in range(2 * m):
        before.append(h)
        if not (x >> i & 1) and h == 0:
            d0 += 1
        h += 1 if x >> i & 1 else -1
    seen = 0
    for i in range(2 * m):
        if not (x >> i & 1) and before[i] in (0, 1):
            seen += 1
            if seen == d0 + 1:
                return x | 1 << i
    raise AssertionError


def hmap(y: int, m: int) -> int:
    before = []
    h = u1 = 0
    for i in range(2 * m):
        before.append(h)
        if y >> i & 1 and h == 1:
            u1 += 1
        h += 1 if y >> i & 1 else -1
    seen = 0
    for i in range(2 * m):
        if y >> i & 1 and before[i] in (0, 1):
            seen += 1
            if seen == u1:
                return y & ~(1 << i)
    raise AssertionError


def canonical_edges(m: int):
    selected = set()
    for root in range(1 << (2 * m)):
        if root.bit_count() != m or not dyck(root, m):
            continue
        x = root
        for _ in range(m):
            y = g(x, m)
            nx = hmap(y, m)
            selected.add((x, y))
            selected.add((nx, y))
            x = nx
    return selected


T2 = [
    ("101010001101", "101011001101", "101010001111"),
    ("100011001101", "100011001111", "101011001101"),
    ("100010001111", "101010001111", "100011001111"),
    ("101011000101", "101011010101", "101011001101"),
    ("101001010101", "101001011101", "101011010101"),
    ("101001001101", "101011001101", "101001011101"),
]


def apply_t2(selected, suffix_words):
    for word in suffix_words:
        u = bits(word) << 12
        for owner, minus, plus in T2:
            old = (bits(owner) | u, bits(minus) | u)
            new = (bits(owner) | u, bits(plus) | u)
            assert old in selected and new not in selected, (word, owner)
            selected.remove(old)
            selected.add(new)


def factor_maps(selected):
    by_owner = defaultdict(list)
    by_colour = defaultdict(list)
    for o, c in selected:
        by_owner[o].append(c)
        by_colour[c].append(o)
    # The canonical complementary path factor has degree-one owner endpoints
    # and degree-two internal owners.  We search only internal-owner circuits.
    assert all(len(v) in (1, 2) for v in by_owner.values())
    assert all(len(v) == 2 for v in by_colour.values())
    return by_owner, by_colour


def directed_steps(o, n, selected, by_colour):
    if o not in INTERNAL_OWNERS:
        return
    missing = ((1 << n) - 1) ^ o
    while missing:
        bit = missing & -missing
        missing -= bit
        c = o | bit
        if (o, c) in selected:
            continue
        for nxt in by_colour[c]:
            if nxt in INTERNAL_OWNERS:
                yield nxt, c


def paths_to_target(start, target, max_steps, n, selected, by_colour, cap):
    out = []

    def dfs(cur, owners, colours):
        if len(owners) - 1 >= max_steps:
            return
        for nxt, c in directed_steps(cur, n, selected, by_colour):
            if c in colours:
                continue
            if nxt == target:
                out.append((owners + [nxt], colours + [c]))
                if len(out) >= cap:
                    return
                continue
            if nxt in owners:
                continue
            dfs(nxt, owners + [nxt], colours + [c])
            if len(out) >= cap:
                return

    dfs(start, [start], [])
    return out


def combine_cycle(p, q):
    po, pc = p
    qo, qc = q
    # p: A -> B, q: B -> A.  Endpoints are intentionally shared.
    if set(po[1:-1]) & set(qo[1:-1]):
        return None
    if set(pc) & set(qc):
        return None
    owners = po[:-1] + qo[:-1]
    colours = pc + qc
    assert len(owners) == len(colours)
    return owners, colours


def q2_current(cycle, by_owner, loads):
    owners, new_colours = cycle
    k = len(owners)
    changes = Counter()
    rows = []
    for i, o in enumerate(owners):
        removed = new_colours[i - 1]
        added = new_colours[i]
        assert removed in by_owner[o] and added not in by_owner[o]
        other = by_owner[o][0] if by_owner[o][1] == removed else by_owner[o][1]
        old = other | removed
        new = other | added
        changes[old] -= 1
        changes[new] += 1
        rows.append((o, removed, added, old, new))
    losses = [t for t, d in changes.items() if loads[t] + d == 0]
    return changes, losses, rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("suffix_m", type=int)
    ap.add_argument("--max-owner-steps", type=int, default=6)
    ap.add_argument("--path-cap", type=int, default=2000)
    ap.add_argument("--json")
    args = ap.parse_args()

    s = args.suffix_m
    m = 6 + s
    n = 2 * m
    suffixes = list(dyck_words(s))
    selected = canonical_edges(m)
    apply_t2(selected, suffixes)
    by_owner, by_colour = factor_maps(selected)
    global INTERNAL_OWNERS
    INTERNAL_OWNERS = {o for o, cs in by_owner.items() if len(cs) == 2}
    loads = Counter(cs[0] | cs[1] for cs in by_owner.values() if len(cs) == 2)

    adjacent = []
    for i, v in enumerate(suffixes):
        uv = bits(v)
        for w in suffixes[i + 1 :]:
            uw = bits(w)
            if (uv ^ uw).bit_count() == 2:
                adjacent.append((v, w))

    results = []
    prefixes = [x[0] for x in T2]
    for v, w in adjacent:
        uv = bits(v) << 12
        uw = bits(w) << 12
        for pword in prefixes:
            a = bits(pword) | uv
            b = bits(pword) | uw
            pab = paths_to_target(
                a, b, args.max_owner_steps, n, selected, by_colour,
                args.path_cap,
            )
            pba = paths_to_target(
                b, a, args.max_owner_steps, n, selected, by_colour,
                args.path_cap,
            )
            best = None
            for p in pab:
                for q in pba:
                    cyc = combine_cycle(p, q)
                    if cyc is None:
                        continue
                    changes, losses, rows = q2_current(cyc, by_owner, loads)
                    key = (len(cyc[0]), len(losses))
                    if best is None or key < best[0]:
                        best = (key, cyc, losses, rows)
            item = {
                "suffix_pair": [v, w],
                "prefix": pword,
                "paths_ab": len(pab),
                "paths_ba": len(pba),
                "best": None,
            }
            if best is not None:
                (_, cyc, losses, rows) = best
                item["best"] = {
                    "owner_steps": len(cyc[0]),
                    "incidence_length": 2 * len(cyc[0]),
                    "q2_support_losses": [bitword(x, n) for x in losses],
                    "rows": [
                        {
                            "owner": bitword(o, n),
                            "removed": bitword(r, n),
                            "added": bitword(a2, n),
                            "old_q2": bitword(old, n),
                            "new_q2": bitword(new, n),
                        }
                        for o, r, a2, old, new in rows
                    ],
                }
            results.append(item)

    payload = {
        "suffix_m": s,
        "m": m,
        "n": n,
        "suffixes": len(suffixes),
        "adjacent_pairs": len(adjacent),
        "results": results,
    }
    text = json.dumps(payload, indent=2, sort_keys=True)
    print(text)
    if args.json:
        with open(args.json, "w", encoding="utf-8") as fh:
            fh.write(text + "\n")


if __name__ == "__main__":
    main()
