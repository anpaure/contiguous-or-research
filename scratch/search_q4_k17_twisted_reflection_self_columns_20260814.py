#!/usr/bin/env python3
"""Enumerate quotient-twisted reflection-self q4/k17 period-10 columns.

Substantive execution belongs on H100.  The target class has owner action
i -> 1-i on the ten starts (no fixed owner bracelets) and exactly two
fixed rank-eight immediate-lower bracelets.  We normalize the lower edge
between starts 0 and 1 to a literal x -> -x invariant eight-set; the other
fixed lower edge is then searched without imposing a common physical lift.
"""

from __future__ import annotations

import argparse
import itertools
import json
import multiprocessing as mp
from collections import Counter

from search_q4_k17_z17_quotient_exact_cover_20260814 import (
    K,
    FULL_MASK,
    canonical_orbit_mask,
    deck_masks,
    rotate_mask,
    subset_mask,
)


Q = 4
OWNER_RANK = 9
LOWER_RANK = 8
PERIOD = 10


def negate_mask(mask: int) -> int:
    answer = 0
    for value in range(K):
        if mask >> value & 1:
            answer |= 1 << ((-value) % K)
    return answer


def reflected_orbit(mask: int) -> int:
    return canonical_orbit_mask(negate_mask(mask))


def fixed_necklace(mask: int) -> bool:
    representative = canonical_orbit_mask(mask)
    return reflected_orbit(representative) == representative


def values(mask: int):
    return tuple(value for value in range(K) if mask >> value & 1)


def shift_to(source: int, target: int):
    shifts = [
        shift for shift in range(K)
        if rotate_mask(source, shift) == target
    ]
    assert len(shifts) <= 1
    return shifts[0] if shifts else None


def induced_permutation(representatives):
    position = {representative: i for i, representative in enumerate(representatives)}
    if len(position) != len(representatives):
        return None
    result = []
    for representative in representatives:
        mate = position.get(reflected_orbit(representative))
        if mate is None:
            return None
        result.append(mate)
    assert all(result[result[i]] == i for i in range(len(result)))
    return tuple(result)


def dihedral_name(permutation):
    n = len(permutation)
    for shift in range(n):
        if permutation == tuple((i + shift) % n for i in range(n)):
            return f"rotation:{shift}"
        if permutation == tuple((shift - i) % n for i in range(n)):
            return f"reflection:{shift}"
    return "nondihedral"


def fixed_literal_lower_masks():
    result = []
    for chosen in itertools.combinations(range(1, 9), 4):
        mask = subset_mask(
            value
            for pair in chosen
            for value in (pair, (-pair) % K)
        )
        assert mask.bit_count() == LOWER_RANK
        assert negate_mask(mask) == mask
        result.append(mask)
    assert len(result) == 70
    return result


def encode_candidate(core, order, owners, lowers, owner_perm, lower_perm, shifts):
    return {
        "core": list(core),
        "order": list(order),
        "owner_orbits": list(owners),
        "lower_orbits": list(lowers),
        "owner_permutation": list(owner_perm),
        "owner_action": dihedral_name(owner_perm),
        "lower_permutation": list(lower_perm),
        "lower_action": dihedral_name(lower_perm),
        "owner_translation_twist": list(shifts),
        "constant_owner_translation": len(set(shifts)) == 1,
    }


def worker(tasks):
    counts = Counter()
    unique = {}
    for lower0, core_tuple in tasks:
        core = set(core_tuple)
        active = tuple(sorted(set(values(lower0)) - core))
        assert len(core) == 5 and len(active) == 3
        outside_lower = tuple(value for value in range(K) if not lower0 >> value & 1)
        core_mask = subset_mask(core)
        for middle in itertools.permutations(active):
            s1, s2, s3 = middle
            for s0 in outside_lower:
                owner0 = lower0 | 1 << s0
                target_owner1 = reflected_orbit(owner0)
                for s4 in outside_lower:
                    if s4 == s0:
                        continue
                    owner1 = lower0 | 1 << s4
                    if canonical_orbit_mask(owner1) != target_owner1:
                        continue
                    counts["boundary_seeds"] += 1
                    used = core | {s0, s1, s2, s3, s4}
                    remaining = tuple(value for value in range(K) if value not in used)
                    assert len(remaining) == 7
                    for triple in itertools.permutations(remaining, 3):
                        s6, s7, s8 = triple
                        lower5 = core_mask | subset_mask(triple)
                        if not fixed_necklace(lower5):
                            continue
                        counts["fixed_second_lower_triples"] += 1
                        rest = tuple(value for value in remaining if value not in triple)
                        for s5, s9 in itertools.permutations(rest, 2):
                            order = (s0, s1, s2, s3, s4, s5, s6, s7, s8, s9)
                            owners_physical = deck_masks(core_tuple, order)
                            owners = tuple(map(canonical_orbit_mask, owners_physical))
                            if len(set(owners)) != PERIOD:
                                counts["owner_nonsimple"] += 1
                                continue
                            owner_perm = induced_permutation(owners)
                            if owner_perm is None:
                                continue
                            counts["owner_self"] += 1
                            fixed_owners = sum(
                                representative == reflected_orbit(representative)
                                for representative in owners
                            )
                            if fixed_owners != 0:
                                counts[f"fixed_owner_rows:{fixed_owners}"] += 1
                                continue
                            expected_owner_perm = tuple((1 - i) % PERIOD for i in range(PERIOD))
                            if owner_perm != expected_owner_perm:
                                counts[f"owner_action:{dihedral_name(owner_perm)}"] += 1
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
                            lower_perm = induced_permutation(lowers)
                            if lower_perm is None:
                                counts["lower_not_self"] += 1
                                continue
                            fixed_lowers = sum(
                                representative == reflected_orbit(representative)
                                for representative in lowers
                            )
                            counts[f"fixed_lower_rows:{fixed_lowers}"] += 1
                            if fixed_lowers != 2:
                                continue
                            counts["target_raw_orders"] += 1

                            shifts = []
                            for i, physical in enumerate(owners_physical):
                                reflected = negate_mask(physical)
                                target = owners_physical[owner_perm[i]]
                                shift = shift_to(reflected, target)
                                assert shift is not None
                                shifts.append(shift)
                            key = (tuple(sorted(owners)), tuple(sorted(lowers)))
                            unique.setdefault(
                                key,
                                encode_candidate(
                                    core_tuple, order, owners, lowers,
                                    owner_perm, lower_perm, tuple(shifts),
                                ),
                            )
    return counts, unique


def chunked(values_, number):
    answer = [[] for _ in range(number)]
    for index, value in enumerate(values_):
        answer[index % number].append(value)
    return [row for row in answer if row]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=64)
    parser.add_argument("--limit", type=int, default=20)
    args = parser.parse_args()

    tasks = [
        (lower0, core)
        for lower0 in fixed_literal_lower_masks()
        for core in itertools.combinations(values(lower0), 5)
    ]
    assert len(tasks) == 70 * 56
    work = chunked(tasks, args.workers)
    with mp.get_context("fork").Pool(processes=len(work)) as pool:
        reports = pool.map(worker, work)
    counts = Counter()
    unique = {}
    for partial_counts, partial_unique in reports:
        counts.update(partial_counts)
        unique.update(partial_unique)

    lower_actions = Counter(row["lower_action"] for row in unique.values())
    twist_histogram = Counter(
        len(set(row["owner_translation_twist"])) for row in unique.values()
    )
    print(json.dumps({
        "status": "PASS",
        "normalization": (
            "owner action i->1-i; lower edge 0 normalized to a literal "
            "x->-x invariant rank-eight set"
        ),
        "normalized_fixed_lower_masks": 70,
        "normalized_core_choices": len(tasks),
        "counts": dict(sorted(counts.items())),
        "unique_joint_owner_lower_columns": len(unique),
        "unique_lower_action_histogram": dict(sorted(lower_actions.items())),
        "unique_owner_twist_distinct_shift_histogram": dict(sorted(twist_histogram.items())),
        "examples": list(unique.values())[:args.limit],
        "scope": (
            "quotient-simple period-10 q4 columns with owner reflection action "
            "i->1-i, zero fixed owner bracelets, ten distinct lower bracelets, "
            "and exactly two fixed lower bracelets; per-owner translations allowed"
        ),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
