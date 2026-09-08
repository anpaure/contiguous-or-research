#!/usr/bin/env python3
"""Test every canonical marked-gap pair for the universal 2x2 wreath switch."""

from __future__ import annotations

import argparse
from collections import Counter


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
    h = 0
    close = None
    for i, bit in enumerate(word):
        h += 1 if bit == "1" else -1
        if h == 0:
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


def msw_order(word):
    r = len(word) // 2
    b = 2 * r + 1
    q = [x - 1 for x in rho(word)] + [b - 1]
    return canonical(tuple(q[(-1 - 2 * j) % b] for j in range(b)))


def dihedral_forms(order):
    order = tuple(order)
    b = len(order)
    for base in (order, tuple(reversed(order))):
        for shift in range(b):
            yield base[shift:] + base[:shift]


def switch_from_pair(row1, row2, r):
    row2_forms = set(dihedral_forms(row2))
    answers = set()
    for R1 in dihedral_forms(row1):
        a, b = R1[:2]
        P = R1[2 : r + 1]
        c, d = R1[r + 1 : r + 3]
        Q = R1[r + 3 :]
        R2 = (c, a) + P + (d, b) + Q
        if R2 not in row2_forms:
            continue
        A1 = canonical((a, c) + P + (b, d) + Q)
        A2 = canonical((b, a) + P + (d, c) + Q)
        answers.add(tuple(sorted((A1, A2))))
    # Either old row can play the first role.
    for answer in switch_from_pair_one_direction(row2, row1, r):
        answers.add(answer)
    return answers


def switch_from_pair_one_direction(row1, row2, r):
    row2_forms = set(dihedral_forms(row2))
    answers = set()
    for R1 in dihedral_forms(row1):
        a, b = R1[:2]
        P = R1[2 : r + 1]
        c, d = R1[r + 1 : r + 3]
        Q = R1[r + 3 :]
        R2 = (c, a) + P + (d, b) + Q
        if R2 in row2_forms:
            A1 = canonical((a, c) + P + (b, d) + Q)
            A2 = canonical((b, a) + P + (d, c) + Q)
            answers.add(tuple(sorted((A1, A2))))
    return answers


def windows(order, k):
    b = len(order)
    return tuple(
        frozenset(order[(i + j) % b] for j in range(k)) for i in range(b)
    )


def main(max_r):
    for r in range(3, max_r + 1):
        canonical_rows = tuple(msw_order(w) for w in dyck_words(r))
        global_load = Counter(x for row in canonical_rows for x in windows(row, r - 1))
        pointed = []
        pairs = Counter()
        failures = []
        alternatives = Counter()
        effect = Counter()
        global_effect = Counter()
        for outer in dyck_words(r - 2):
            for gap in range(len(outer) + 1):
                roots = (
                    outer[:gap] + "1100" + outer[gap:],
                    outer[:gap] + "1010" + outer[gap:],
                )
                rows = tuple(msw_order(w) for w in roots)
                key = tuple(sorted(rows))
                pairs[key] += 1
                answers = switch_from_pair(rows[0], rows[1], r)
                alternatives[len(answers)] += 1
                if not answers:
                    failures.append((outer, gap, roots, rows))
                    continue
                old_lower = Counter(x for row in rows for x in windows(row, r - 1))
                # Record the best q1 collision reduction over switch alignments.
                best = None
                for answer in answers:
                    new_lower = Counter(x for row in answer for x in windows(row, r - 1))
                    old_excess = sum(v - 1 for v in old_lower.values() if v > 1)
                    new_excess = sum(v - 1 for v in new_lower.values() if v > 1)
                    delta_units = sum((old_lower - new_lower).values())
                    score = (old_excess - new_excess, -delta_units)
                    if best is None or score > best:
                        best = score
                    delta = new_lower.copy()
                    delta.subtract(old_lower)
                    dphi = 0
                    dholes = 0
                    for target, dv in delta.items():
                        if not dv:
                            continue
                        before = global_load[target]
                        after = before + dv
                        dphi += after * (after - 1) // 2 - before * (before - 1) // 2
                        dholes += int(before > 0 and after == 0) - int(before == 0 and after > 0)
                    global_effect[(dphi, dholes)] += 1
                effect[best] += 1
                pointed.append((outer, gap, key, len(answers)))
        expected = (2 * r - 3) * len(list(dyck_words(r - 2)))
        assert len(pointed) + len(failures) == expected
        print(
            {
                "r": r,
                "pointed": expected,
                "unique_pairs": len(pairs),
                "pair_multiplicity_hist": sorted(Counter(pairs.values()).items()),
                "alternative_count_hist": sorted(alternatives.items()),
                "failures": len(failures),
                "q1_internal_excess_effect": sorted(effect.items()),
                "canonical_global_effect": sorted(global_effect.items()),
            },
            flush=True,
        )
        if failures:
            print("FIRST_FAILURE", failures[0], flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-r", type=int, default=10)
    args = parser.parse_args()
    main(args.max_r)
