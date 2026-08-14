#!/usr/bin/env python3
"""List exact native providers of the mixed T0 tensor's suffix seam debt.

Substantive execution belongs on H100.  For every nonempty Dyck suffix V,
the endpoint C6 creates the extra upper-q2 current
P_plus[g(V)] - P_minus[g(V)].  This script lists every old canonical turn
providing the negative target, with root, owner position, and two colours.
"""

from __future__ import annotations

import argparse
import json

import audit_msw_t0v_tensor_residence_20260814 as base


NEGATIVE_PREFIX = "100011010111"
POSITIVE_PREFIX = "000011110111"


def gamma_pairs(target_word):
    height = 0
    before = []
    for char in target_word:
        before.append(height)
        height += 1 if char == "1" else -1
    answer = []
    for p, char in enumerate(target_word):
        if char != "1" or before[p] not in (0, 1):
            continue
        left = sum(
            target_word[index] == "1" and before[index] == 0
            for index in range(p)
        )
        for q in range(p + 1, len(target_word)):
            if target_word[q] != "1" or before[q] not in (2, 3):
                continue
            if any(
                target_word[index] == "0" and before[index] in (2, 3)
                for index in range(p + 1, q)
            ):
                continue
            right = sum(
                target_word[index] == "1" and before[index] == 3
                for index in range(q + 1, len(target_word))
            )
            if left == right:
                answer.append([p + 1, q + 1])
    return answer


def all_occurrences(m):
    answer = {}
    for root_word in base.dyck_words(m):
        root = base.bits(root_word)
        owner = root
        colours = []
        owners = [owner]
        for _ in range(m):
            colour = base.g(owner, m)
            owner = base.hmap(colour, m)
            colours.append(colour)
            owners.append(owner)
        for position in range(1, m):
            target = colours[position - 1] | colours[position]
            answer.setdefault(target, []).append({
                "root": root_word,
                "position": position,
                "owner": base.bitword(owners[position], 2 * m),
                "left_colour": base.bitword(colours[position - 1], 2 * m),
                "right_colour": base.bitword(colours[position], 2 * m),
            })
    return answer


def audit(m):
    suffix_m = m - 6
    occurrences = all_occurrences(m)
    rows = []
    for suffix_word in base.dyck_words(suffix_m):
        if suffix_m == 0:
            continue
        suffix_owner = base.bits(suffix_word)
        suffix_colour = base.g(suffix_owner, suffix_m)
        negative = base.bits(NEGATIVE_PREFIX) | suffix_colour << 12
        positive = base.bits(POSITIVE_PREFIX) | suffix_colour << 12
        providers = occurrences.get(negative, [])
        assert len(providers) >= 2
        rows.append({
            "suffix": suffix_word,
            "suffix_first_colour": base.bitword(suffix_colour, 2 * suffix_m),
            "negative_target": base.bitword(negative, 2 * m),
            "positive_target": base.bitword(positive, 2 * m),
            "old_negative_load": len(providers),
            "gamma_pairs": gamma_pairs(base.bitword(negative, 2 * m)),
            "providers": providers,
        })
    return {"m": m, "rows": rows}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("m", nargs="+", type=int)
    args = parser.parse_args()
    print(json.dumps({"status": "PASS", "runs": [audit(m) for m in args.m]}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
