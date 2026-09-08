#!/usr/bin/env python3
"""Classify Dyck-root pairs supporting a canonical legal C8 switch.

Intended execution: H100 only.
"""

from __future__ import annotations

import argparse
from collections import Counter
from itertools import combinations

from research_b9_c8_current_lattice_20260821 import dyck_words, msw_row, switches


def pair_signature(left, right):
    prefix = 0
    while prefix < len(left) and left[prefix] == right[prefix]:
        prefix += 1
    suffix = 0
    while (suffix < len(left) - prefix
           and left[-1 - suffix] == right[-1 - suffix]):
        suffix += 1
    left_mid = left[prefix:len(left) - suffix if suffix else len(left)]
    right_mid = right[prefix:len(right) - suffix if suffix else len(right)]
    return prefix, suffix, left_mid, right_mid


def audit_r(r, show):
    words = tuple(dyck_words(r))
    row_to_word = {msw_row(word): word for word in words}
    records = []
    histogram = Counter()
    candidate_histogram = Counter()
    supported_histogram = Counter()
    word_set = set(words)
    for word in words:
        height = 0
        for position in range(2 * r - 1):
            if word[position:position + 2] == "10":
                mate = word[:position] + "01" + word[position + 2:]
                if mate in word_set:
                    signature = (position, height)
                    candidate_histogram[signature] += 1
                    if switches(msw_row(word), msw_row(mate), r):
                        supported_histogram[signature] += 1
            height += 1 if word[position] == "1" else -1
    for row_left, row_right in combinations(row_to_word, 2):
        count = len(switches(row_left, row_right, r))
        if not count:
            continue
        left, right = row_to_word[row_left], row_to_word[row_right]
        signature = pair_signature(left, right)
        histogram[(signature[2], signature[3])] += count
        records.append((left, right, count, signature))
    return {
        "r": r,
        "pairs": sum(record[2] for record in records),
        "middle_pair_hist": dict(histogram),
        "candidate_position_height_hist": dict(candidate_histogram),
        "supported_position_height_hist": dict(supported_histogram),
        "records": records if show else None,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--r", type=int, default=4)
    parser.add_argument("--show", action="store_true")
    arguments = parser.parse_args()
    print("CANONICAL_C8_ROOT_PAIR_TYPES", audit_r(arguments.r, arguments.show))
