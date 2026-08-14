#!/usr/bin/env python3
"""Audit every linear upper-colour window across the frozen T0 relay.

The even canonical MSW factor is a union of owner--q1-colour paths.  For
q>=2 an upper-q occurrence on the linear factor is the union of q
consecutive q1 colours.  This script toggles the literal H1,H2 incidences
from the frozen theorem and compares the complete global support by width.
Heavy use belongs on h100 only.
"""

from collections import Counter, defaultdict, deque


def bits(word: str) -> int:
    return sum((c == "1") << i for i, c in enumerate(word))


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


def paths(selected):
    adj = defaultdict(list)
    for owner, colour in selected:
        adj[(0, owner)].append((1, colour))
        adj[(1, colour)].append((0, owner))
    assert all(len(v) <= 2 for v in adj.values())
    endpoints = [v for v, ns in adj.items() if len(ns) == 1]
    seen = set()
    out = []
    for start in endpoints:
        if start in seen:
            continue
        seq = []
        prev = None
        cur = start
        while True:
            seen.add(cur)
            if cur[0] == 1:
                seq.append(cur[1])
            nxt = [z for z in adj[cur] if z != prev]
            if not nxt:
                break
            prev, cur = cur, nxt[0]
        out.append(seq)
    assert len(seen) == len(adj), (len(seen), len(adj))
    return out


def decks(path_colours, m: int):
    out = {q: Counter() for q in range(1, m + 1)}
    for seq in path_colours:
        for q in range(1, m + 1):
            for i in range(len(seq) - q + 1):
                value = 0
                for z in seq[i : i + q]:
                    value |= z
                out[q][value] += 1
    return out


def main():
    m = 6
    selected = canonical_edges(m)
    old_paths = paths(selected)
    old = decks(old_paths, m)

    h1 = [
        ("101010001101", "101011001101", "101010001111"),
        ("100011001101", "100011001111", "101011001101"),
        ("100010001111", "101010001111", "100011001111"),
    ]
    h2 = [
        ("101011000101", "101011010101", "101011001101"),
        ("101001010101", "101001011101", "101011010101"),
        ("101001001101", "101011001101", "101001011101"),
    ]
    for owner, minus, plus in h1 + h2:
        e_minus = (bits(owner), bits(minus))
        e_plus = (bits(owner), bits(plus))
        assert e_minus in selected
        assert e_plus not in selected
        selected.remove(e_minus)
        selected.add(e_plus)

    new_paths = paths(selected)
    new = decks(new_paths, m)
    assert len(old_paths) == len(new_paths)
    print(
        "path_length_hist old=",
        dict(sorted(Counter(map(len, old_paths)).items())),
        "new=",
        dict(sorted(Counter(map(len, new_paths)).items())),
    )
    for q in range(1, m + 1):
        casualties = sorted(t for t in old[q] if new[q][t] == 0)
        births = sorted(t for t in new[q] if old[q][t] == 0)
        min_after = min((new[q][t] for t in old[q]), default=0)
        print(
            f"q={q} old_support={len(old[q])} new_support={len(new[q])} "
            f"casualties={len(casualties)} births={len(births)} "
            f"min_after_on_old={min_after}"
        )
        for t in casualties[:20]:
            print(
                "  LOST",
                format(t, f"0{2*m}b")[::-1],
                "old_load",
                old[q][t],
            )
        for t in births[:20]:
            print(
                "  BIRTH",
                format(t, f"0{2*m}b")[::-1],
                "new_load",
                new[q][t],
            )


if __name__ == "__main__":
    main()
