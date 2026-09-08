#!/usr/bin/env python3
"""Search quotient-self period-10 columns with a fixed lower bracelet.

Substantive execution belongs on H100.  One fixed rank-eight lower necklace
is translated to a literal x -> -x invariant set and rotated to edge 0.
No owner permutation (dihedral or otherwise) is imposed.  The reflected
necklaces of the two owners incident with that fixed lower edge must occur
somewhere among the ten owner windows; these two compulsory windows prune
the remaining five support positions before the full quotient-self test.
"""

from __future__ import annotations

import argparse
import itertools
import json
import multiprocessing as mp
from collections import Counter, defaultdict

import search_q4_k17_twisted_reflection_self_columns_20260814 as base
from search_q4_k17_z17_quotient_exact_cover_20260814 import (
    K,
    canonical_orbit_mask,
    deck_masks,
    subset_mask,
)


PERIOD = 10


def multiply_mask(mask, multiplier):
    """Apply x -> multiplier*x in Z_17 to a literal mask."""
    result = 0
    for value in base.values(mask):
        result |= 1 << ((multiplier * value) % K)
    return result


def fixed_lower_multiplier_orbits():
    """Return the ten Z_17^*/{+-1} orbits of fixed lower masks."""
    fixed = frozenset(base.fixed_literal_lower_masks())
    unseen = set(fixed)
    orbits = []
    while unseen:
        seed = min(unseen)
        orbit = frozenset(
            multiply_mask(seed, multiplier)
            for multiplier in range(1, K)
        )
        assert orbit <= fixed
        orbits.append(tuple(sorted(orbit)))
        unseen -= orbit
    assert sum(map(len, orbits)) == len(fixed) == 70
    assert len(orbits) == 10
    return tuple(sorted(orbits))


def window_positions(start):
    return frozenset((start + offset) % PERIOD for offset in range(4))


WINDOW_POSITIONS = tuple(window_positions(start) for start in range(PERIOD))


def orbit_windows(core):
    core_mask = subset_mask(core)
    complement = tuple(value for value in range(K) if value not in core)
    result = defaultdict(list)
    for window in itertools.combinations(complement, 4):
        representative = canonical_orbit_mask(core_mask | subset_mask(window))
        result[representative].append(frozenset(window))
    return result


def feasible_constraints(target, mapping, known):
    known_positions = frozenset(known)
    known_labels = frozenset(known.values())
    rows = []
    for window in mapping.get(target, ()):
        for start, positions in enumerate(WINDOW_POSITIONS):
            inside_known_positions = positions & known_positions
            inside_known_labels = frozenset(known[position] for position in inside_known_positions)
            # A known label belongs to the target window exactly when its
            # position belongs to this four-position cyclic interval.
            if window & known_labels != inside_known_labels:
                continue
            rows.append((start, positions - known_positions, window - known_labels))
    return rows


def compatible_tails(constraints0, constraints1, remaining):
    """Generate exactly the five-position tails satisfying both windows."""
    unknown_positions = frozenset(range(5, 10))
    remaining = frozenset(remaining)
    tails = set()
    compatible_pairs = 0
    for _, positions0, labels0 in constraints0:
        for _, positions1, labels1 in constraints1:
            position_classes = (
                positions0 & positions1,
                positions0 - positions1,
                positions1 - positions0,
            )
            label_classes = (
                labels0 & labels1,
                labels0 - labels1,
                labels1 - labels0,
            )
            if any(len(left) != len(right)
                   for left, right in zip(position_classes, label_classes)):
                continue
            if not (labels0 | labels1) <= remaining:
                continue
            outside_positions = unknown_positions - positions0 - positions1
            outside_labels = remaining - labels0 - labels1
            if len(outside_labels) < len(outside_positions):
                continue
            compatible_pairs += 1
            fixed_classes = [
                (tuple(sorted(positions)), tuple(sorted(labels)))
                for positions, labels in zip(position_classes, label_classes)
            ]
            for outside_choice in itertools.combinations(
                sorted(outside_labels), len(outside_positions)
            ):
                classes = fixed_classes + [
                    (tuple(sorted(outside_positions)), tuple(outside_choice))
                ]
                permutation_banks = [
                    tuple(itertools.permutations(labels))
                    for _, labels in classes
                ]
                for assignments in itertools.product(*permutation_banks):
                    by_position = {}
                    for (positions, _), assigned in zip(classes, assignments):
                        by_position.update(zip(positions, assigned))
                    assert set(by_position) == set(unknown_positions)
                    tails.add(tuple(by_position[position] for position in range(5, 10)))
    return tails, compatible_pairs


def classify(core, order):
    core_mask = subset_mask(core)
    owners_physical = deck_masks(core, order)
    owners = tuple(map(canonical_orbit_mask, owners_physical))
    if len(set(owners)) != PERIOD:
        return "owner_nonsimple", None
    owner_perm = base.induced_permutation(owners)
    if owner_perm is None:
        return "owner_not_self", None
    lowers_physical = tuple(
        core_mask | subset_mask(
            order[(i + offset) % PERIOD] for offset in (1, 2, 3)
        )
        for i in range(PERIOD)
    )
    lowers = tuple(map(canonical_orbit_mask, lowers_physical))
    if len(set(lowers)) != PERIOD:
        return "lower_nonsimple", None
    lower_perm = base.induced_permutation(lowers)
    fixed_owners = sum(base.fixed_necklace(row) for row in owners)
    fixed_lowers = sum(base.fixed_necklace(row) for row in lowers)
    shifts = []
    for i, owner in enumerate(owners_physical):
        shift = base.shift_to(base.negate_mask(owner), owners_physical[owner_perm[i]])
        assert shift is not None
        shifts.append(shift)
    return "owner_self", {
        "core": list(core),
        "order": list(order),
        "owner_orbits": list(owners),
        "lower_orbits": list(lowers),
        "owner_permutation": list(owner_perm),
        "owner_action": base.dihedral_name(owner_perm),
        "lower_permutation": None if lower_perm is None else list(lower_perm),
        "lower_action": None if lower_perm is None else base.dihedral_name(lower_perm),
        "fixed_owner_rows": fixed_owners,
        "fixed_lower_rows": fixed_lowers,
        "owner_translation_twist": shifts,
        "constant_owner_translation": len(set(shifts)) == 1,
    }


def worker(tasks):
    counts = Counter()
    unique = {}
    for lower0, core_tuple in tasks:
        core = set(core_tuple)
        mapping = orbit_windows(core_tuple)
        active = tuple(sorted(set(base.values(lower0)) - core))
        outside_lower = tuple(value for value in range(K) if not lower0 >> value & 1)
        for middle in itertools.permutations(active):
            for s0, s4 in itertools.permutations(outside_lower, 2):
                counts["fixed_lower_boundary_seeds"] += 1
                first = (s0,) + middle + (s4,)
                known = dict(enumerate(first))
                core_mask = subset_mask(core_tuple)
                owner0 = core_mask | subset_mask(first[:4])
                owner1 = core_mask | subset_mask(first[1:])
                target0 = base.reflected_orbit(owner0)
                target1 = base.reflected_orbit(owner1)
                constraints0 = feasible_constraints(target0, mapping, known)
                if not constraints0:
                    continue
                constraints1 = feasible_constraints(target1, mapping, known)
                if not constraints1:
                    continue
                counts["seeds_with_two_target_windows"] += 1

                remaining = tuple(value for value in range(K) if value not in core and value not in first)
                assert len(remaining) == 7
                tails, compatible_pairs = compatible_tails(
                    constraints0, constraints1, remaining
                )
                counts["compatible_constraint_pairs"] += compatible_pairs
                counts["deduplicated_compatible_tails"] += len(tails)
                for tail in tails:
                    order = first + tail
                    counts["completed_orders"] += 1
                    owner_reps = tuple(map(canonical_orbit_mask, deck_masks(core_tuple, order)))
                    if target0 not in owner_reps or target1 not in owner_reps:
                        continue
                    counts["completed_orders_with_incident_mates"] += 1
                    status, report = classify(core_tuple, order)
                    counts[status] += 1
                    if report is None:
                        continue
                    key = (
                        tuple(sorted(report["owner_orbits"])),
                        tuple(sorted(report["lower_orbits"])),
                    )
                    unique.setdefault(key, report)
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
    lower_orbits = fixed_lower_multiplier_orbits()
    lower_representatives = tuple(orbit[0] for orbit in lower_orbits)
    tasks = [
        (lower, core)
        for lower in lower_representatives
        for core in itertools.combinations(base.values(lower), 5)
    ]
    assert len(tasks) == 560
    work = chunks(tasks, args.workers)
    with mp.get_context("fork").Pool(processes=len(work)) as pool:
        rows = pool.map(worker, work)
    counts = Counter()
    unique = {}
    for partial_counts, partial_unique in rows:
        counts.update(partial_counts)
        unique.update(partial_unique)
    signature = Counter(
        (row["fixed_owner_rows"], row["fixed_lower_rows"], row["owner_action"])
        for row in unique.values()
    )
    print(json.dumps({
        "status": "PASS",
        "multiplier_normalization": {
            "all_fixed_lower_masks": 70,
            "multiplier_orbits": len(lower_orbits),
            "orbit_sizes": [len(orbit) for orbit in lower_orbits],
            "representative_tasks": len(tasks),
            "unreduced_tasks": 70 * 56,
            "completeness": (
                "multiplication by every nonzero element of Z_17 commutes "
                "with reflection x->-x and preserves translation necklaces, "
                "cyclic-window incidence, quotient simplicity, and all fixed-"
                "row signatures; hence one fixed-lower representative per "
                "multiplier orbit is exhaustive"
            ),
        },
        "counts": dict(sorted(counts.items())),
        "unique_quotient_self_columns": len(unique),
        "fixed_row_owner_action_signature": {
            f"{owner},{lower},{action}": amount
            for (owner, lower, action), amount in sorted(signature.items())
        },
        "examples": list(unique.values())[:args.limit],
        "scope": (
            "all period-10 q4 columns with at least one fixed rank-eight "
            "lower bracelet, normalized to lower edge0 and literal reflection; "
            "full owner quotient-self test with no assumed induced involution"
        ),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
