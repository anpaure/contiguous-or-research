#!/usr/bin/env python3
"""Classify the lower-q1 defect of the Catalan T0V tensor.

Substantive execution belongs on H100.  The script reconstructs the native
factor, applies every suffix packet, and prints only the per-suffix load of
the one base-prefix lower cell whose packet current is negative and can be
support-critical.
"""

from __future__ import annotations

import argparse
import json

import audit_msw_t0v_tensor_residence_20260814 as base
import audit_msw_t0v_tensor_typed_currents_20260814 as typed


BAD_PREFIX = "000011001101"


def first_return_split(word: str) -> tuple[int, int]:
    height = 0
    for index, char in enumerate(word):
        height += 1 if char == "1" else -1
        if height == 0:
            return (index // 2, (len(word) - index - 1) // 2)
    raise AssertionError


def heights_before(word: str) -> list[int]:
    height = 0
    answer = []
    for char in word:
        answer.append(height)
        height += 1 if char == "1" else -1
    return answer


def alpha_pairs(word: str) -> list[tuple[int, int]]:
    """Lemma 2.1 of the exact MSW alpha-inverse theorem, 0-based."""
    heights = heights_before(word)
    answer = []
    for p, char_p in enumerate(word):
        if char_p != "0" or heights[p] not in (0, 1):
            continue
        left = sum(
            word[index] == "0" and heights[index] == 1
            for index in range(p)
        )
        for q in range(p + 1, len(word)):
            if word[q] != "0" or heights[q] not in (-2, -1):
                continue
            if any(
                word[index] == "1" and heights[index] in (-2, -1)
                for index in range(p + 1, q)
            ):
                continue
            right = sum(
                word[index] == "0" and heights[index] == -2
                for index in range(q + 1, len(word))
            )
            if left == right:
                answer.append((p, q))
    return answer


def audit(m: int):
    old_selected = base.canonical_edges(m)
    old = typed.typed_decks(old_selected)["lower_q1"]
    new_selected = set(old_selected)
    packets, _ = base.apply_tensor(new_selected, m)
    new = typed.typed_decks(new_selected)["lower_q1"]
    rows = []
    for word in base.dyck_words(m - 6):
        value = base.bits(BAD_PREFIX + word)
        pairs = alpha_pairs(BAD_PREFIX + word)
        rows.append(
            {
                "suffix": word,
                "first_return_split": first_return_split(word) if word else None,
                "old_load": old[value],
                "new_load": new[value],
                "alpha_pairs": pairs,
                "alpha_pair_count": len(pairs),
                "load_minus_alpha": old[value] - len(pairs),
                "support_casualty": old[value] > 0 and new[value] == 0,
            }
        )
    return {
        "m": m,
        "packets": packets,
        "casualties": sum(row["support_casualty"] for row in rows),
        "load_histogram": {
            str(load): sum(row["old_load"] == load for row in rows)
            for load in sorted({row["old_load"] for row in rows})
        },
        "rows": rows,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("m", nargs="+", type=int)
    args = parser.parse_args()
    print(json.dumps({"status": "PASS", "runs": [audit(m) for m in args.m]}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
