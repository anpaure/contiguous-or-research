#!/usr/bin/env python3
"""Complete normalized owner-edge-axis quotient-self column catalogue.

Substantive execution belongs on H100.  Translation normalizes the
five-core to its necklace representative and cyclic rotation normalizes
the fixed owner-cycle edges to (0,1) and (5,6), so the owner involution is
i -> 1-i.  The two adjacent reflected-pair constraints split the ten
support positions into two disjoint five-label boundary words.  No common
physical reflection lift and no alignment of fixed lower tickets with the
owner axis is assumed.
"""

from __future__ import annotations

import argparse
import itertools
import json
import multiprocessing as mp
from collections import Counter

import search_q4_k17_twisted_reflection_self_columns_20260814 as aligned
from search_q4_k17_z17_quotient_exact_cover_20260814 import (
    K,
    canonical_orbit_mask,
    deck_masks,
    subset_mask,
)


PERIOD = 10
CORE_SIZE = 5


def canonical_cores():
    result = []
    for core in itertools.combinations(range(K), CORE_SIZE):
        mask = subset_mask(core)
        if canonical_orbit_mask(mask) == mask:
            result.append(core)
    assert len(result) == 364
    return result


def boundary_words(core):
    """All s0..s4 with [-(C+s0..s3)]=[C+s1..s4]."""
    core_mask = subset_mask(core)
    complement = tuple(value for value in range(K) if value not in core)
    rows = []
    for first in itertools.permutations(complement, 4):
        owner0 = core_mask | subset_mask(first)
        target = aligned.reflected_orbit(owner0)
        used = set(first)
        middle = first[1:]
        for final in complement:
            if final in used:
                continue
            owner1 = core_mask | subset_mask(middle + (final,))
            if canonical_orbit_mask(owner1) == target:
                rows.append(first + (final,))
    return rows


def encode(core, order, owners, lowers, owner_perm, lower_perm, shifts):
    return {
        "core": list(core),
        "order": list(order),
        "owner_orbits": list(owners),
        "lower_orbits": list(lowers),
        "owner_permutation": list(owner_perm),
        "owner_action": aligned.dihedral_name(owner_perm),
        "lower_permutation": list(lower_perm),
        "lower_action": aligned.dihedral_name(lower_perm),
        "owner_translation_twist": list(shifts),
        "constant_owner_translation": len(set(shifts)) == 1,
        "fixed_lower_positions": [
            i for i, row in enumerate(lowers)
            if aligned.fixed_necklace(row)
        ],
    }


def worker(cores):
    counts = Counter()
    unique = {}
    expected_owner_perm = tuple((1 - i) % PERIOD for i in range(PERIOD))
    for core in cores:
        bank = boundary_words(core)
        counts["boundary_words"] += len(bank)
        core_mask = subset_mask(core)
        encoded_bank = [(row, frozenset(row)) for row in bank]
        for left, left_set in encoded_bank:
            for right, right_set in encoded_bank:
                if left_set & right_set:
                    continue
                counts["disjoint_boundary_pairs"] += 1
                order = left + right
                owners_physical = deck_masks(core, order)
                owners = tuple(map(canonical_orbit_mask, owners_physical))
                if len(set(owners)) != PERIOD:
                    counts["owner_nonsimple"] += 1
                    continue
                owner_perm = aligned.induced_permutation(owners)
                if owner_perm is None:
                    counts["owner_not_self"] += 1
                    continue
                if owner_perm != expected_owner_perm:
                    counts[f"owner_action:{aligned.dihedral_name(owner_perm)}"] += 1
                    continue
                counts["owner_edge_axis"] += 1

                lowers_physical = tuple(
                    core_mask | subset_mask(
                        order[(i + offset) % PERIOD]
                        for offset in (1, 2, 3)
                    )
                    for i in range(PERIOD)
                )
                lowers = tuple(map(canonical_orbit_mask, lowers_physical))
                if len(set(lowers)) != PERIOD:
                    counts["lower_nonsimple"] += 1
                    continue
                lower_perm = aligned.induced_permutation(lowers)
                if lower_perm is None:
                    counts["lower_not_self"] += 1
                    continue
                fixed_lowers = sum(aligned.fixed_necklace(row) for row in lowers)
                counts[f"fixed_lower_rows:{fixed_lowers}"] += 1
                if fixed_lowers != 2:
                    continue
                counts["target_raw_orders"] += 1

                shifts = []
                for i, physical in enumerate(owners_physical):
                    shift = aligned.shift_to(
                        aligned.negate_mask(physical),
                        owners_physical[owner_perm[i]],
                    )
                    assert shift is not None
                    shifts.append(shift)
                key = (tuple(sorted(owners)), tuple(sorted(lowers)))
                unique.setdefault(
                    key,
                    encode(
                        core, order, owners, lowers,
                        owner_perm, lower_perm, tuple(shifts),
                    ),
                )
    return counts, unique


def chunks(values_, number):
    result = [[] for _ in range(number)]
    for index, value in enumerate(values_):
        result[index % number].append(value)
    return [row for row in result if row]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=64)
    parser.add_argument("--limit", type=int, default=20)
    args = parser.parse_args()
    cores = canonical_cores()
    work = chunks(cores, args.workers)
    with mp.get_context("fork").Pool(processes=len(work)) as pool:
        reports = pool.map(worker, work)
    counts = Counter()
    unique = {}
    for partial_counts, partial_unique in reports:
        counts.update(partial_counts)
        unique.update(partial_unique)

    lower_actions = Counter(row["lower_action"] for row in unique.values())
    fixed_position_patterns = Counter(
        tuple(row["fixed_lower_positions"]) for row in unique.values()
    )
    twist_histogram = Counter(
        len(set(row["owner_translation_twist"])) for row in unique.values()
    )
    print(json.dumps({
        "status": "PASS",
        "canonical_core_necklaces": len(cores),
        "counts": dict(sorted(counts.items())),
        "unique_joint_owner_lower_columns": len(unique),
        "unique_lower_action_histogram": dict(sorted(lower_actions.items())),
        "unique_fixed_lower_position_histogram": {
            ",".join(map(str, key)): value
            for key, value in sorted(fixed_position_patterns.items())
        },
        "unique_owner_twist_distinct_shift_histogram": dict(sorted(twist_histogram.items())),
        "examples": list(unique.values())[:args.limit],
        "scope": (
            "all translation-normalized quotient-simple q4 period-10 columns "
            "whose owner reflection action is the edge axis i->1-i; filters "
            "to ten distinct lower bracelets, lower-set reflection invariance, "
            "and exactly two fixed lower bracelets; owner translations vary by row"
        ),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
