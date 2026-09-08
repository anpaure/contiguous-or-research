#!/usr/bin/env python3
"""Exact finite audit of the minimum b=9 vertical row trade.

For every set R of at most four canonical rows, the checker enumerates every
exact replacement cover of the same middle targets and verifies that none
covers all q1 targets.  It then verifies the displayed five-row trade covers
every lower depth.  Intended execution environment: H100 only.
"""

from __future__ import annotations

from itertools import combinations, permutations

from audit_b9_five_wreath_shadow_switch_20260821 import (
    ADDED,
    REMOVED,
    canonical,
    dyck_words,
    msw_row,
)


def window_mask(order, length, target_id):
    b = len(order)
    mask = 0
    for start in range(b):
        target = frozenset(order[(start + j) % b] for j in range(length))
        mask |= 1 << target_id[target]
    assert mask.bit_count() == b
    return mask


def main():
    b, r = 9, 4
    layers = {
        k: tuple(map(frozenset, combinations(range(1, b + 1), k)))
        for k in range(1, r + 1)
    }
    target_id = {k: {target: i for i, target in enumerate(layer)} for k, layer in layers.items()}
    full = {k: (1 << len(layer)) - 1 for k, layer in layers.items()}

    rows = []
    row_id = {}
    for tail in permutations(range(2, b + 1)):
        order = (1,) + tail
        if order[1] > order[-1]:
            continue
        key = canonical(order)
        row_id[key] = len(rows)
        rows.append((
            key,
            *(window_mask(key, k, target_id[k]) for k in range(1, r + 1)),
        ))
    assert len(rows) == len(row_id) == 20160

    canonical_ids = tuple(sorted(row_id[msw_row(word)] for word in dyck_words(r)))
    assert len(canonical_ids) == 14
    by_middle = [[] for _ in layers[r]]
    for index, row in enumerate(rows):
        middle = row[r]
        while middle:
            bit = middle & -middle
            by_middle[bit.bit_length() - 1].append(index)
            middle ^= bit

    canonical_q1 = 0
    for index in canonical_ids:
        canonical_q1 |= rows[index][r - 1]
    assert (full[r - 1] ^ canonical_q1).bit_count() == 4

    removed_sets = 0
    exact_replacement_covers = 0
    for size in range(1, 5):
        for removed_tuple in combinations(canonical_ids, size):
            removed_sets += 1
            removed = set(removed_tuple)
            middle_pool = 0
            retained_q1 = 0
            for index in canonical_ids:
                if index in removed:
                    middle_pool |= rows[index][r]
                else:
                    retained_q1 |= rows[index][r - 1]
            assert middle_pool.bit_count() == b * size

            def search(remaining, chosen_q1):
                nonlocal exact_replacement_covers
                if not remaining:
                    exact_replacement_covers += 1
                    assert retained_q1 | chosen_q1 != full[r - 1], (
                        size,
                        removed_tuple,
                    )
                    return
                first = (remaining & -remaining).bit_length() - 1
                for candidate in by_middle[first]:
                    candidate_middle = rows[candidate][r]
                    if candidate_middle & remaining != candidate_middle:
                        continue
                    search(
                        remaining ^ candidate_middle,
                        chosen_q1 | rows[candidate][r - 1],
                    )

            search(middle_pool, 0)

    removed = {row_id[canonical(row)] for row in REMOVED}
    added = {row_id[canonical(row)] for row in ADDED}
    assert len(removed) == len(added) == 5
    final_ids = set(canonical_ids) - removed | added
    assert len(final_ids) == 14
    for k in range(1, r + 1):
        support = 0
        for index in final_ids:
            support |= rows[index][k]
        assert support == full[k]

    print("B9_MINIMUM_VERTICAL_ROW_TRADE_AUDIT_PASS", {
        "canonical_removed_sets_checked": removed_sets,
        "exact_replacement_covers_checked": exact_replacement_covers,
        "minimum_row_replacements": 5,
        "final_holes_q1_q2_q3": (0, 0, 0),
    })


if __name__ == "__main__":
    main()
