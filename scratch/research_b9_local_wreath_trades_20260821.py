#!/usr/bin/env python3
"""Enumerate small exact row trades around the canonical b=9 MSW factor."""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from itertools import combinations, permutations


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


def msw_row(word: str):
    m = len(word) // 2
    b = 2 * m + 1
    q = [x - 1 for x in rho(word)] + [b - 1]
    return canonical(tuple(q[(-1 - 2 * j) % b] for j in range(b)))


def window_masks(order, k):
    b = len(order)
    return tuple(
        sorted(
            sum(1 << order[(i + j) % b] for j in range(k))
            for i in range(b)
        )
    )


def first_nontrivial_cover(universe, candidate_ids, row_bits, old_ids, by_vertex):
    old_set = frozenset(old_ids)

    def rec(uncovered, chosen):
        if not uncovered:
            answer = frozenset(chosen)
            return answer if answer != old_set else None
        best = None
        support = None
        bits = uncovered
        while bits:
            lsb = bits & -bits
            v = lsb.bit_length() - 1
            viable = [i for i in by_vertex[v] if i in candidate_ids and not (row_bits[i] & ~uncovered)]
            if not viable:
                return None
            if support is None or len(viable) < len(support):
                best, support = v, viable
                if len(support) == 1:
                    break
            bits ^= lsb
        assert best is not None and support is not None
        # Noncanonical rows first so the trivial cover does not dominate.
        support.sort(key=lambda i: (i in old_set, i))
        for i in support:
            ans = rec(uncovered ^ row_bits[i], chosen + [i])
            if ans is not None:
                return ans
        return None

    return rec(universe, [])


def main(max_support):
    b, m = 9, 4
    middle = [sum(1 << q for q in c) for c in combinations(range(b), m)]
    mid_id = {x: i for i, x in enumerate(middle)}
    rows = []
    for tail in permutations(range(1, b)):
        order = (0,) + tail
        if order[1] > order[-1]:
            continue
        vertices = tuple(mid_id[x] for x in window_masks(order, m))
        bits = sum(1 << x for x in vertices)
        rows.append((order, vertices, bits))
    row_id = {canonical(order): i for i, (order, _, _) in enumerate(rows)}
    old_ids = tuple(row_id[msw_row(w)] for w in dyck_words(m))
    assert len(set(old_ids)) == 14
    owner = {}
    for j, i in enumerate(old_ids):
        for v in rows[i][1]:
            assert v not in owner
            owner[v] = j
    assert len(owner) == len(middle)

    owner_masks = []
    by_owner_mask = defaultdict(list)
    row_bits = []
    by_vertex = [[] for _ in middle]
    for i, (_, vertices, bits) in enumerate(rows):
        om = 0
        for v in vertices:
            om |= 1 << owner[v]
            by_vertex[v].append(i)
        owner_masks.append(om)
        by_owner_mask[om].append(i)
        row_bits.append(bits)
    print("owner_count_hist", sorted(Counter(x.bit_count() for x in owner_masks).items()), flush=True)

    old_pos_to_id = dict(enumerate(old_ids))
    all_trade_rows = set()
    trade_examples = {}
    trade_subsets = Counter()
    for s in range(2, max_support + 1):
        for S_tuple in combinations(range(14), s):
            S = sum(1 << x for x in S_tuple)
            universe = 0
            for x in S_tuple:
                universe |= row_bits[old_pos_to_id[x]]
            candidates = {
                i for om, ids in by_owner_mask.items() if om & ~S == 0 for i in ids
            }
            if len(candidates) == s:
                continue
            alt = first_nontrivial_cover(
                universe,
                candidates,
                row_bits,
                [old_pos_to_id[x] for x in S_tuple],
                by_vertex,
            )
            if alt is None:
                continue
            added = alt - {old_pos_to_id[x] for x in S_tuple}
            removed = {old_pos_to_id[x] for x in S_tuple} - alt
            assert len(added) == len(removed)
            # Strip any rows common to the old and new covers; the true support
            # may be smaller than S when S contained irrelevant old rows.
            true_s = len(removed)
            trade_subsets[(s, true_s)] += 1
            all_trade_rows.update(added)
            trade_examples.setdefault(true_s, (removed, added))
        print(
            {"searched_support": s, "trade_subset_hist": sorted(trade_subsets.items()), "new_rows_seen": len(all_trade_rows)},
            flush=True,
        )

    for s, (removed, added) in sorted(trade_examples.items()):
        print("EXAMPLE", s)
        for label, ids in (("REMOVE", removed), ("ADD", added)):
            for i in sorted(ids):
                print(label, " ".join(str(q + 1) for q in rows[i][0]))
    print("tradeable_new_rows", len(all_trade_rows), "of", len(rows) - 14)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-support", type=int, default=5)
    args = parser.parse_args()
    main(args.max_support)
