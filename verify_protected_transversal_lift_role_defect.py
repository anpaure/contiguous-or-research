#!/usr/bin/env python3
"""Verify protected transversal-lift owner/lower role formulas.

Run substantive checks on H100.  This script is a finite identity checker;
it does not solve the nonuniform weighted-core, Hall, or named-order gates.
"""

from __future__ import annotations

import argparse
import json
import math
from collections import Counter


def verify_case(p: int, q: int) -> dict[str, object]:
    k = 2 * p + 1
    r = p + 1
    c = r - q
    width = math.comb(k, r)
    catalan = width // k
    assert catalan * k == width

    gray = [t ^ (t >> 1) for t in range(1 << p)]
    direction_counts = [0] * p
    lowers: list[frozenset[int]] = []
    owners: list[frozenset[int]] = []
    for index, word in enumerate(gray):
        following = gray[(index + 1) % len(gray)]
        changed = word ^ following
        assert changed and changed & (changed - 1) == 0
        direction_counts[changed.bit_length() - 1] += 1
        lower = frozenset(2 * i + ((word >> i) & 1) for i in range(p))
        next_lower = frozenset(2 * i + ((following >> i) & 1) for i in range(p))
        lowers.append(lower)
        owners.append(lower | next_lower)
    assert len(set(lowers)) == 1 << p
    assert len(set(owners)) == 1 << p
    assert sum(direction_counts) == 1 << p
    assert all(count > 0 and count % 2 == 0 for count in direction_counts)

    owner_degrees = Counter()
    lower_degrees = Counter()
    for owner in owners:
        owner_degrees.update(owner)
    for lower in lowers:
        lower_degrees.update(lower)

    support_targets: list[int] = []
    core_targets: list[int] = []
    support_defects: list[int] = []
    core_defects: list[int] = []
    for i, count in enumerate(direction_counts):
        for coordinate in (2 * i, 2 * i + 1):
            assert lower_degrees[coordinate] == 1 << (p - 1)
            assert owner_degrees[coordinate] == (1 << (p - 1)) + count // 2
            support_defect = count // 2
            core_defect = (1 << (p - 1)) - (q - 1) * count // 2
            support_targets.append(catalan - support_defect)
            core_targets.append(c * catalan - core_defect)
            support_defects.append(support_defect)
            core_defects.append(core_defect)

    sentinel = 2 * p
    assert owner_degrees[sentinel] == lower_degrees[sentinel] == 0
    support_targets.append(catalan)
    core_targets.append(c * catalan)
    support_defects.append(0)
    core_defects.append(0)

    owner_point_degree = math.comb(k - 1, r - 1)
    lower_point_degree = math.comb(k - 1, r - 2)
    for coordinate in range(k):
        assert (
            core_targets[coordinate] + q * support_targets[coordinate]
            == owner_point_degree - owner_degrees[coordinate]
        )
        assert (
            core_targets[coordinate] + (q - 1) * support_targets[coordinate]
            == lower_point_degree - lower_degrees[coordinate]
        )
    assert sum(support_defects) == 1 << p
    assert sum(core_defects) == c * (1 << p)
    assert sum(support_targets) == width - (1 << p)
    assert sum(core_targets) == c * (width - (1 << p))
    assert support_defects[-1] == core_defects[-1] == 0
    assert any(value > 0 for value in support_defects[:-1])
    assert any(value > 0 for value in core_defects[:-1])

    return {
        "p": p,
        "q": q,
        "k": k,
        "R": r,
        "c": c,
        "W": width,
        "W_over_k": catalan,
        "direction_counts": direction_counts,
        "support_defects_by_pair": [count // 2 for count in direction_counts],
        "weighted_core_defects_by_pair": [
            (1 << (p - 1)) - (q - 1) * count // 2
            for count in direction_counts
        ],
        "sentinel_defects": [support_defects[-1], core_defects[-1]],
        "total_support_defect": sum(support_defects),
        "total_weighted_core_defect": sum(core_defects),
        "residual_support_range": [min(support_targets), max(support_targets)],
        "residual_weighted_core_range": [min(core_targets), max(core_targets)],
        "whole_regular_orbit_span": "constant role vectors only",
        "protected_defect_is_nonconstant": True,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--case",
        action="append",
        default=[],
        help="case p,q (repeatable); defaults to 3,2; 5,2; and 7,3",
    )
    args = parser.parse_args()
    cases = [(3, 2), (5, 2), (7, 3)]
    if args.case:
        cases = [tuple(map(int, raw.split(","))) for raw in args.case]
    print(
        json.dumps(
            {
                "status": "PASS",
                "scope": (
                    "finite identity checks for reflected-Gray protected role "
                    "defects and orbit nonconstancy; not a weighted-core, Hall, "
                    "or integral named-order solver"
                ),
                "cases": [verify_case(p, q) for p, q in cases],
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()

