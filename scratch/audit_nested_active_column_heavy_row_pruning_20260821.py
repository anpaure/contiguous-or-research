#!/usr/bin/env python3
"""Finite audit of nested active-column heavy-row pruning.

Intended execution environment: H100 only.  The asymptotic estimates in the
companion note are analytic.
"""

from __future__ import annotations

import math
import random
from collections import Counter
from itertools import combinations


def audit_system(rows, b, h):
    # rows[row][start] is a tuple of (depth, target) active incidences.
    multiplicities = Counter(
        (q, target)
        for row in rows
        for column in row
        for q, target in column
    )
    q_star = sum(value - 1 for value in multiplicities.values() if value >= 2)
    repeated = {key for key, value in multiplicities.items() if value >= 2}
    e_star = sum(value for key, value in multiplicities.items() if value >= 2)

    bad = []
    for row in rows:
        bad.append([
            any((q, target) in repeated for q, target in column)
            for column in row
        ])
    b_star = sum(sum(bits) for bits in bad)
    assert b_star <= e_star <= 2 * q_star if q_star else b_star == e_star == 0

    total_value = sum(len(column) for row in rows for column in row)
    summaries = []
    for c in range(1, b + 1):
        deleted = {i for i, bits in enumerate(bad) if sum(bits) > c}
        if deleted:
            assert len(deleted) < 2 * q_star / c
        surviving = []
        lost = 0
        removed_starts = 0
        for i, row in enumerate(rows):
            if i in deleted:
                lost += sum(len(column) for column in row)
                removed_starts += b
                continue
            assert sum(bad[i]) <= c
            for j, column in enumerate(row):
                if bad[i][j]:
                    lost += len(column)
                    removed_starts += 1
                else:
                    surviving.extend(column)
        assert len(surviving) == len(set(surviving))
        assert lost <= 2 * h * q_star + 2 * b * h * q_star / c + 1e-9
        assert removed_starts <= 2 * q_star + 2 * b * q_star / c + 1e-9
        assert total_value - len(surviving) == lost
        summaries.append((c, len(deleted), lost, removed_starts))
    return q_star, e_star, b_star, total_value, summaries


def structured_systems():
    # Exhaust all prefix-lifetime choices for a small deterministic label
    # bank, and use several label maps which realize different collision
    # geometries (same row, cross row, all equal, and mixed depths).
    h = 2
    m = 2
    b = 2
    for code in range((h + 1) ** (m * b)):
        z = code
        life = []
        for _ in range(m * b):
            life.append(z % (h + 1))
            z //= h + 1
        for mode in range(6):
            rows = []
            for i in range(m):
                row = []
                for j in range(b):
                    ell = life[i * b + j]
                    column = []
                    for q in range(1, ell + 1):
                        if mode == 0:
                            target = (i, j)
                        elif mode == 1:
                            target = j
                        elif mode == 2:
                            target = i
                        elif mode == 3:
                            target = 0
                        elif mode == 4:
                            target = (i + j + q) % 2
                        else:
                            target = (i * j + q) % 3
                        column.append((q, target))
                    row.append(tuple(column))
                rows.append(tuple(row))
            yield tuple(rows), b, h


def random_systems(seed=20260821, count=2000):
    rng = random.Random(seed)
    for _ in range(count):
        m = rng.randint(1, 8)
        b = rng.randint(1, 8)
        h = rng.randint(1, 6)
        rows = []
        for i in range(m):
            row = []
            for j in range(b):
                ell = rng.randint(0, h)
                column = tuple((q, rng.randrange(max(1, m * b // 2)))
                               for q in range(1, ell + 1))
                row.append(column)
            rows.append(tuple(row))
        yield tuple(rows), b, h


def dyck_words(m: int):
    def rec(pos, ones, word):
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


def mu(word):
    return word[::-1].translate(str.maketrans("01", "10"))


def rho(word):
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


def msw_row(word):
    r = len(word) // 2
    b = 2 * r + 1
    q = rho(word) + [b]
    return canonical(tuple(q[(-1 - 2 * j) % b] for j in range(b)))


def windows(order, k):
    b = len(order)
    return tuple(frozenset(order[(i + j) % b] for j in range(k))
                 for i in range(b))


def canonical_factor(r):
    rows = tuple(sorted({msw_row(word) for word in dyck_words(r)}))
    middle = Counter(target for row in rows for target in windows(row, r))
    expected = {frozenset(x) for x in combinations(range(1, 2 * r + 2), r)}
    assert middle == Counter({target: 1 for target in expected})
    return rows


def audit_full_nested_factors():
    summaries = []
    for r in range(2, 5):
        rows = canonical_factor(r)
        b = 2 * r + 1
        n = math.comb(b, r)
        q_sum = 0
        unavoidable = 0
        depths = []
        for q in range(1, r):
            counts = Counter(target for row in rows for target in windows(row, r - q))
            assert sum(counts.values()) == n
            q_q = sum(value - 1 for value in counts.values() if value >= 2)
            layer = math.comb(b, r - q)
            assert q_q == n - len(counts) >= n - layer
            product_num = 1
            product_den = 1
            for j in range(q):
                product_num *= r - j
                product_den *= r + 2 + j
            assert layer * product_den == n * product_num
            q_sum += q_q
            unavoidable += n - layer
            depths.append((q, q_q, n - layer))
        assert q_sum >= unavoidable
        summaries.append((r, b, len(rows), q_sum, unavoidable, depths))
    return summaries


def main():
    cases = 0
    max_q = 0
    for system in structured_systems():
        q, _, _, _, _ = audit_system(*system)
        max_q = max(max_q, q)
        cases += 1
    for system in random_systems():
        q, _, _, _, _ = audit_system(*system)
        max_q = max(max_q, q)
        cases += 1
    factors = audit_full_nested_factors()
    print("NESTED_ACTIVE_COLUMN_HEAVY_ROW_PRUNING_AUDIT_PASS",
          {"systems": cases, "max_q": max_q, "factors": factors})


if __name__ == "__main__":
    main()
