#!/usr/bin/env python3
"""Finite audit of the q1-repeat purge and all-depth hole ledger.

Intended execution environment: H100 only.
"""

from __future__ import annotations

from collections import Counter
from itertools import combinations


def dyck_words(m: int):
    def rec(pos: int, ones: int, word: list[str]):
        if pos == 2 * m:
            yield "".join(word)
            return
        if ones < m:
            word.append("1")
            yield from rec(pos + 1, ones + 1, word)
            word.pop()
        if pos - ones < ones:
            word.append("0")
            yield from rec(pos + 1, ones, word)
            word.pop()

    yield from rec(0, 0, [])


def mu(word: str) -> str:
    return word[::-1].translate(str.maketrans("01", "10"))


def rho(word: str) -> list[int]:
    if not word:
        return []
    height = 0
    close = None
    for i, bit in enumerate(word):
        height += 1 if bit == "1" else -1
        if height == 0:
            close = i
            break
    assert close is not None
    u, v = word[1:close], word[close + 1 :]
    d = len(u) + 2
    return [d] + [d - x for x in rho(mu(u))] + [1] + [d + x for x in rho(v)]


def canonical(order):
    order = tuple(order)
    rots = [order[i:] + order[:i] for i in range(len(order))]
    rev = tuple(reversed(order))
    rots.extend(rev[i:] + rev[:i] for i in range(len(order)))
    return min(rots)


def msw_row(word: str):
    r = len(word) // 2
    b = 2 * r + 1
    q = rho(word) + [b]
    return canonical(tuple(q[(-1 - 2 * j) % b] for j in range(b)))


def windows(order, k):
    b = len(order)
    return tuple(
        frozenset(order[(i + j) % b] for j in range(k)) for i in range(b)
    )


def canonical_factor(r):
    rows = tuple(sorted({msw_row(w) for w in dyck_words(r)}))
    middle = Counter(x for row in rows for x in windows(row, r))
    expected = {frozenset(x) for x in combinations(range(1, 2 * r + 2), r)}
    assert middle == Counter({x: 1 for x in expected})
    return rows


def maximum_path_cycle_matching(b, dirty):
    r = (b - 1) // 2
    clean = set(range(b)) - dirty
    adj = {i: [z for z in ((i + r) % b, (i - r) % b) if z in clean]
           for i in clean}
    seen = set()
    pairs = []
    if not dirty:
        start = min(clean)
        order = [start]
        prev = None
        cur = start
        while True:
            nxt = [z for z in adj[cur] if z != prev]
            z = nxt[0]
            if z == start:
                break
            order.append(z)
            prev, cur = cur, z
        assert len(order) == b
        for j in range(0, b - 1, 2):
            pairs.append((order[j], order[j + 1]))
        return pairs
    for start in clean:
        if start in seen or len(adj[start]) > 1:
            continue
        path = []
        prev = None
        cur = start
        while cur is not None and cur not in path:
            path.append(cur)
            nxt = [z for z in adj[cur] if z != prev]
            prev, cur = cur, (nxt[0] if nxt else None)
        seen.update(path)
        for j in range(0, len(path) - 1, 2):
            pairs.append((path[j], path[j + 1]))
    assert seen == clean
    return pairs


def audit_r(r):
    rows = canonical_factor(r)
    b = 2 * r + 1
    A = len(rows) * b
    profiles = {
        q: [windows(row, r - q) for row in rows]
        for q in range(1, r)
    }
    full = {
        q: Counter(t for deck in profiles[q] for t in deck)
        for q in profiles
    }
    q1_repeated = {t for t, value in full[1].items() if value >= 2}
    dirty = {
        (row, i)
        for row in range(len(rows))
        for i, target in enumerate(profiles[1][row])
        if target in q1_repeated
    }
    q1 = sum(value - 1 for value in full[1].values())
    assert len(dirty) == q1 + len(q1_repeated) <= 2 * q1

    clean_middle = []
    clean_q1 = []
    paired = 0
    pair_discard = 0
    for row in range(len(rows)):
        row_dirty = {i for rr, i in dirty if rr == row}
        pairs = maximum_path_cycle_matching(b, row_dirty)
        clean = b - len(row_dirty)
        pair_discard += clean - 2 * len(pairs)
        paired += 2 * len(pairs)
        middle = windows(rows[row], r)
        for i in range(b):
            if i not in row_dirty:
                clean_middle.append(middle[i])
                clean_q1.append(profiles[1][row][i])
        for i, j in pairs:
            assert middle[i].isdisjoint(middle[j])
    assert len(clean_middle) == len(set(clean_middle))
    assert len(clean_q1) == len(set(clean_q1))
    assert pair_discard <= len(rows) + len(dirty)
    assert paired == A - len(dirty) - pair_discard

    ledgers = []
    for q in range(1, r):
        universe = set(
            frozenset(x) for x in combinations(range(1, b + 1), r - q)
        )
        counts = full[q]
        holes = len(universe - counts.keys())
        excess = sum(value - 1 for value in counts.values())
        assert excess == A - len(universe) + holes
        retained = Counter(
            profiles[q][row][i]
            for row in range(len(rows))
            for i in range(b)
            if (row, i) not in dirty
        )
        new_holes = len(universe - retained.keys())
        new_excess = sum(value - 1 for value in retained.values())
        assert new_excess == A - len(dirty) - len(universe) + new_holes
        assert 0 <= new_holes - holes <= len(dirty)
        ledgers.append((q, holes, excess, new_holes, new_excess))
    return {
        "r": r,
        "b": b,
        "rows": len(rows),
        "dirty": len(dirty),
        "pair_discard": pair_discard,
        "ledgers": ledgers,
    }


def determinant3(matrix):
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def main():
    profiles = [
        ({1}, {1, 3}, {1, 2, 3}),
        ({2}, {1, 2}, {1, 2, 3}),
        ({1}, {1, 2}, {1, 2, 4}),
    ]
    assert all(set(x) < set(y) < set(z) for x, y, z in profiles)
    witness_rows = [
        (1, 3, 2, 5, 4, 6, 7, 8, 9),
        (2, 1, 3, 6, 4, 5, 7, 8, 9),
        (1, 2, 4, 7, 3, 5, 6, 8, 9),
    ]
    for row, profile in zip(witness_rows, profiles):
        assert (
            set(row[:1]), set(row[:2]), set(row[:3])
        ) == profile
    assert len({frozenset(row[:4]) for row in witness_rows}) == 3
    minor = [[1, 1, 0], [0, 1, 1], [1, 0, 1]]
    assert determinant3(minor) == 2
    summaries = [audit_r(r) for r in range(2, 6)]
    print("Q1_REPEAT_PURGE_ALL_DEPTH_COVERAGE_AUDIT_PASS", summaries)


if __name__ == "__main__":
    main()
