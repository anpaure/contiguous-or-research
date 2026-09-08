#!/usr/bin/env python3
"""Read-only source-factor audit of the literal answers, not a formula fit.

Positions and bit indices are zero-based; interval endpoints are inclusive.
The fixed-delay audit uses d = len(A) - binom(k, ceil(k/2)).  For nonflat
answers, also use one shortest, earliest witness per middle target, and all
middle witnesses.  These are different, explicitly named constraint systems.

--details --json includes every per-position decrement and omitted bit.
No answer, report, master, or index file is written.
"""

from __future__ import annotations

import argparse
from collections import Counter
from hashlib import sha256
from itertools import combinations, product
import json
from math import comb, prod
from pathlib import Path


def derivative(word: list[int], depth: int) -> list[int]:
    for _ in range(depth):
        word = [left | right for left, right in zip(word, word[1:])]
    return word


def interval_data(word: list[int], middle_rank: int):
    """All targets' shortest witnesses and intersections of ALL their witnesses.

    Suffixes with a given OR have a contiguous range of starting positions.
    Retaining its two endpoints avoids enumerating quadratically many windows.
    A profile is [shortest_length, earliest_shortest_start, core_left, core_right].
    Middle occurrences are materialized because their windows are short here.
    """
    profiles = {}
    middle = {}
    counts = Counter()
    suffixes = {}
    for right, letter in enumerate(word):
        current = {letter: (right, right)}
        for mask, (first, last) in suffixes.items():
            union = mask | letter
            if union in current:
                old_first, old_last = current[union]
                current[union] = min(first, old_first), max(last, old_last)
            else:
                current[union] = first, last
        for mask, (first, last) in current.items():
            counts[mask] += last - first + 1
            length = right - last + 1
            if mask not in profiles:
                profiles[mask] = [length, last, last, right]
            else:
                record = profiles[mask]
                if (length, last) < tuple(record[:2]):
                    record[:2] = length, last
                record[2] = max(record[2], last)
                record[3] = min(record[3], right)
            if mask.bit_count() == middle_rank:
                middle.setdefault(mask, []).extend(
                    (left, right, mask) for left in range(first, last + 1)
                )
        suffixes = current
    return profiles, middle, counts


def envelope(n: int, k: int, owners: list[tuple[int, int, int]]) -> list[int]:
    cap = [(1 << k) - 1] * n
    for left, right, mask in owners:
        for position in range(left, right + 1):
            cap[position] &= mask
    return cap


def interval_union(word: list[int], left: int, right: int) -> int:
    union = 0
    for position in range(left, right + 1):
        union |= word[position]
    return union


def residence(owners, n: int, k: int, delay: int, details: bool):
    """Residence for strictly increasing left AND right owner endpoints.

    For a positive run [u,v], neighboring zero owners give the allowed band
    [R_(u-1)+1, L_(v+1)-1], with boundaries 0 and n-1.  Every positive
    owner must meet that band.  Its width need not be run_length - delay.
    """
    assert all(
        a[0] < b[0] and a[1] < b[1] for a, b in zip(owners, owners[1:])
    )
    m = len(owners)
    internal = Counter()
    boundary = []
    parameter_cover = Counter()
    length_minus_width = Counter()
    violations = []
    all_runs = []
    for bit in range(k):
        index = 0
        while index < m:
            if not owners[index][2] & (1 << bit):
                index += 1
                continue
            first = index
            while index < m and owners[index][2] & (1 << bit):
                index += 1
            last = index - 1
            left = owners[first - 1][1] + 1 if first else 0
            right = owners[index][0] - 1 if index < m else n - 1
            valid = (
                left <= right
                and left <= owners[first][1]
                and owners[last][0] <= right
            )
            run = [bit, first, last, left, right]
            if not valid:
                violations.append(run)
            if first > 0 and index < m:
                length = index - first
                internal[length] += 1
                parameter_cover[(length, right - left + 1)] += 1
                length_minus_width[length - (right - left + 1)] += 1
            else:
                boundary.append(run)
            if details:
                all_runs.append(run)
    result = {
        "internal_run_length_histogram": dict(sorted(internal.items())),
        "internal_run_total": sum(internal.values()),
        "internal_runs_shorter_than_d_plus_1": sum(
            count for length, count in internal.items() if length <= delay
        ),
        "internal_length_allowed_band_width_count": [
            [length, width, count]
            for (length, width), count in sorted(parameter_cover.items())
        ],
        "internal_run_length_minus_band_width_histogram": dict(sorted(length_minus_width.items())),
        "boundary_runs_bit_first_last_allowed_left_right": boundary,
        "parameter_cover_violations": violations,
    }
    if details:
        result["all_runs_bit_first_last_allowed_left_right"] = all_runs
    return result


def factor_report(word, cap, owners, profiles, k: int, rank: int, details: bool):
    assert all(letter & ~maximum == 0 for letter, maximum in zip(word, cap))
    assert all(interval_union(cap, left, right) == mask for left, right, mask in owners)
    cap_profiles, _, _ = interval_data(cap, rank)
    omissions = [maximum & ~letter for letter, maximum in zip(word, cap)]
    decrements = [mask.bit_count() for mask in omissions]
    changed = [position for position, mask in enumerate(omissions) if mask]
    lower = {mask for mask in profiles if 0 < mask.bit_count() < rank}
    missing = sorted(lower - cap_profiles.keys())
    first_relation = Counter()
    changed_first = Counter()
    changed_letters = Counter()
    first_cap = cap.copy()
    for mask in sorted(lower):
        length, left, _, _ = profiles[mask]
        if mask not in cap_profiles:
            relation = "absent_from_cap"
        else:
            cap_length = cap_profiles[mask][0]
            relation = (
                "raw_earlier" if length < cap_length else
                "raw_later" if length > cap_length else "same_length"
            )
        first_relation[(mask.bit_count(), relation)] += 1
        cap_cell = interval_union(cap, left, left + length - 1)
        if cap_cell != mask:
            changed_first[(mask.bit_count(), relation)] += 1
        for position in range(left, left + length):
            first_cap[position] &= mask
    for position in changed:
        mask = word[position]
        changed_letters[(mask.bit_count(), mask not in cap_profiles)] += 1
    assert all(letter & ~maximum == 0 for letter, maximum in zip(word, first_cap))
    assert all(interval_union(first_cap, left, right) == mask for left, right, mask in owners)
    assert all(
        interval_union(first_cap, profiles[mask][1], profiles[mask][1] + profiles[mask][0] - 1) == mask
        for mask in lower
    )
    first_profiles, _, _ = interval_data(first_cap, rank)
    first_extra = [
        [p, maximum & ~word[p]] for p, maximum in enumerate(first_cap) if maximum != word[p]
    ]

    # Inserting bit b at p kills target S iff b is absent from S and every
    # S-witness contains p.  Such targets cannot be recreated by that insertion.
    lost = {(p, bit): [] for p in changed for bit in range(k) if omissions[p] >> bit & 1}
    restore_lost = {p: set() for p in changed}
    for mask, (_, _, left, right) in profiles.items():
        for position in range(left, right + 1):
            forbidden = omissions[position] & ~mask
            while forbidden:
                bitmask = forbidden & -forbidden
                bit = bitmask.bit_length() - 1
                lost[position, bit].append(mask)
                restore_lost[position].add(mask)
                forbidden ^= bitmask
    criticality = Counter(len(targets) for targets in lost.values())
    lost_ranks = Counter(mask.bit_count() for targets in lost.values() for mask in targets)
    optional = [[p, bit] for (p, bit), targets in lost.items() if not targets]
    singleton_positions = [p for p, mask in enumerate(word) if mask.bit_count() == 1]
    singleton_edits = []
    for position in singleton_positions:
        if not omissions[position]:
            continue
        targets = sorted(restore_lost[position])
        singleton_edits.append({
            "position": position,
            "raw": word[position],
            "cap": cap[position],
            "lost_target_count": len(targets),
            "lost_by_rank": dict(sorted(Counter(mask.bit_count() for mask in targets).items())),
            "loses_its_singleton": word[position] in targets,
            **({"lost_targets": targets} if details else {}),
        })
    result = {
        "owner_count": len(owners),
        "factor_checks_pass": True,
        "equal_positions": len(word) - len(changed),
        "changed_positions": len(changed),
        "raw_bit_total": sum(mask.bit_count() for mask in word),
        "cap_bit_total": sum(mask.bit_count() for mask in cap),
        "omitted_bit_total": sum(decrements),
        "decrement_histogram": dict(sorted(Counter(decrements).items())),
        "cap_rank_raw_rank_position_count": [
            [upper, actual, count]
            for (upper, actual), count in sorted(Counter(
                (cap[p].bit_count(), word[p].bit_count()) for p in range(len(word))
            ).items())
        ],
        "omitted_count_by_bit": [sum(mask >> bit & 1 for mask in omissions) for bit in range(k)],
        "lower_targets_absent_from_cap_by_rank": dict(sorted(Counter(
            mask.bit_count() for mask in missing
        ).items())),
        "all_targets_absent_from_cap_by_rank": dict(sorted(Counter(
            mask.bit_count() for mask in profiles.keys() - cap_profiles.keys()
        ).items())),
        "lower_first_length_comparison_rank_relation_count": [
            [layer, relation, count] for (layer, relation), count in sorted(first_relation.items())
        ],
        "changed_canonical_first_cells_rank_relation_count": [
            [layer, relation, count] for (layer, relation), count in sorted(changed_first.items())
        ],
        "changed_letter_rank_absent_from_cap_count": [
            [layer, absent, count] for (layer, absent), count in sorted(changed_letters.items())
        ],
        "canonical_lower_first_witness_cap": {
            "equals_raw": first_cap == word,
            "erasures_forced_by_chosen_lower_first_cells": sum(
                (maximum & ~pinned).bit_count() for maximum, pinned in zip(cap, first_cap)
            ),
            "residual_omitted_bits": sum(mask.bit_count() for _, mask in first_extra),
            "residual_changed_positions": len(first_extra),
            "all_targets_still_covered": profiles.keys() <= first_profiles.keys(),
            "missing_target_ranks": dict(sorted(Counter(
                mask.bit_count() for mask in profiles.keys() - first_profiles.keys()
            ).items())),
            **({"residual_position_bits": first_extra} if details else {}),
        },
        "single_bit_reinsertion_lost_target_count_histogram": dict(sorted(criticality.items())),
        "single_bit_reinsertion_lost_target_rank_incidence": dict(sorted(lost_ranks.items())),
        "optional_single_bit_reinsertions": optional,
        "singleton_positions": len(singleton_positions),
        "singleton_local_restorations": singleton_edits,
        "restorable_whole_positions_without_coverage_loss": [
            p for p, targets in restore_lost.items() if not targets
        ],
    }
    if details:
        result.update({
            "maximal_factor": cap,
            "per_position_cardinality_decrement": decrements,
            "omitted_mask_by_position": omissions,
            "omitted_positions_by_bit": [
                [p for p, mask in enumerate(omissions) if mask >> bit & 1] for bit in range(k)
            ],
            "changes_position_raw_cap_omitted_mask": [
                [p, word[p], cap[p], omissions[p]] for p in changed
            ],
            "lower_targets_absent_from_cap": missing,
            "single_bit_reinsertion_losses": [
                [p, bit, sorted(targets)] for (p, bit), targets in lost.items()
            ],
        })
    return result


def singleton_erosions(word, delay: int, counts, details: bool):
    """All proper A[p] -> {b} subset edits preserving D^d A and universality.

    A preserved D^d freezes every window of length at least d+1.  Count deltas
    for the at most d(d+1)/2 affected shorter windows therefore suffice.
    """
    row = derivative(word, delay)
    n = len(word)
    candidates = 0
    safe = []
    failed = Counter()
    for position, letter in enumerate(word):
        if letter.bit_count() == 1:
            continue
        forced = 0
        for left in range(max(0, position - delay), min(position, n - delay - 1) + 1):
            other = 0
            for p in range(left, left + delay + 1):
                if p != position:
                    other |= word[p]
            forced |= row[left] & ~other
        remaining = letter
        while remaining:
            singleton = remaining & -remaining
            remaining ^= singleton
            if forced & ~singleton:
                continue
            candidates += 1
            changes = Counter()
            for length in range(1, delay + 1):
                for left in range(max(0, position - length + 1), min(position, n - length) + 1):
                    other = 0
                    for p in range(left, left + length):
                        if p != position:
                            other |= word[p]
                    before, after = other | letter, other | singleton
                    changes[before] -= 1
                    changes[after] += 1
            lost = [mask for mask, delta in changes.items() if counts[mask] + delta == 0]
            if lost:
                failed[len(lost)] += 1
            else:
                safe.append([position, letter, singleton])
    return {
        "fixed_derivative_preserving_candidates": candidates,
        "universal_singleton_erosions_count": len(safe),
        "rejected_lost_target_count_histogram": dict(sorted(failed.items())),
        "universal_edits_position_before_after": safe if details else safe[:12],
        "edits_list_complete": details or len(safe) <= 12,
    }


def owner_parameter_cover(word, middle, all_cap, k: int, delay: int):
    """Exhaust every actual one-witness-per-middle-target selection.

    The literal nonflat answers have only 2, 2, and 16 selections.  Fail closed
    rather than silently substituting a sample if another input is much larger.
    """
    ambiguous = [(mask, windows) for mask, windows in sorted(middle.items()) if len(windows) > 1]
    count = prod(len(windows) for _, windows in ambiguous)
    assert count <= 4096, f"too many owner selections to exhaust: {count}"
    common = [windows[0] for windows in middle.values() if len(windows) == 1]
    records = []
    distinct = set()
    for choice in product(*(range(len(windows)) for _, windows in ambiguous)):
        owners = sorted(common + [windows[index] for index, (_, windows) in zip(choice, ambiguous)])
        cap = envelope(len(word), k, owners)
        assert all(a & ~b == 0 for a, b in zip(word, cap))
        assert all(interval_union(cap, left, right) == mask for left, right, mask in owners)
        runs = residence(owners, len(word), k, delay, False)
        assert not runs["parameter_cover_violations"]
        extra = [(p, a & ~b) for p, (a, b) in enumerate(zip(cap, all_cap)) if a != b]
        assert all(b & ~a == 0 for a, b in zip(cap, all_cap))
        distinct.add(tuple(extra))
        decrements = [(a & ~b).bit_count() for a, b in zip(cap, word)]
        cap_profiles, _, _ = interval_data(cap, (k + 1) // 2)
        missing_ranks = Counter(mask.bit_count() for mask in range(1, 1 << k) if mask not in cap_profiles)
        records.append({
            "choice_indices": choice,
            "changed_positions": sum(value > 0 for value in decrements),
            "omitted_bit_total": sum(decrements),
            "decrement_histogram": dict(sorted(Counter(decrements).items())),
            "cap_extra_position_bits_over_all_occurrences": extra,
            "all_targets_absent_from_cap_by_rank": dict(sorted(missing_ranks.items())),
            "internal_runs_shorter_than_d_plus_1": runs["internal_runs_shorter_than_d_plus_1"],
            "residence_length_minus_band_width_histogram": runs["internal_run_length_minus_band_width_histogram"],
        })
    return {
        "exhaustive_selection_count": count,
        "distinct_maximal_factors": len(distinct),
        "ambiguous_mask_and_intervals": [
            [mask, [[left, right] for left, right, _ in windows]] for mask, windows in ambiguous
        ],
        "selections": records,
        "all_parameter_covers_valid": True,
    }


def analyze(path: Path, k: int, details: bool):
    original = path.read_bytes()
    word = [int(token) for token in original.split()]
    assert word and all(0 < mask < 1 << k for mask in word)
    rank = (k + 1) // 2
    width = comb(k, rank)
    delay = len(word) - width
    assert 0 <= delay < len(word)
    profiles, middle, counts = interval_data(word, rank)
    assert set(profiles) == set(range(1, 1 << k)), f"k={k}: not universal"
    row = derivative(word, delay)
    flat = len(set(row)) == width and all(mask.bit_count() == rank for mask in row)
    owners = [(i, i + delay, mask) for i, mask in enumerate(row)]
    cap = envelope(len(word), k, owners)
    fixed = factor_report(word, cap, owners, profiles, k, rank, details)
    assert derivative(cap, delay) == row
    fixed["residence"] = residence(owners, len(word), k, delay, details)
    assert not fixed["residence"]["parameter_cover_violations"]
    assert not fixed["residence"]["internal_runs_shorter_than_d_plus_1"]
    full_runs = sum(
        first == 0 and last == len(row) - 1
        for _, first, last, _, _ in fixed["residence"]["boundary_runs_bit_first_last_allowed_left_right"]
    )
    residence_mass = (
        sum(mask.bit_count() for mask in row)
        - delay * fixed["residence"]["internal_run_total"] + delay * full_runs
    )
    assert residence_mass == fixed["cap_bit_total"]
    fixed["cap_bit_total_independently_from_residence"] = residence_mass
    result = {
        "k": k,
        "input_sha256": sha256(original).hexdigest(),
        "critical_rank": rank,
        "delay": delay,
        "flat_exact_middle_derivative": flat,
        "fixed_delay": fixed,
        "singleton_erosions": singleton_erosions(word, delay, counts, details),
    }
    if not flat:
        selected = sorted(
            min(windows, key=lambda item: (item[1] - item[0], item[0]))
            for windows in middle.values()
        )
        selected_cap = envelope(len(word), k, selected)
        selected_report = factor_report(word, selected_cap, selected, profiles, k, rank, details)
        selected_report["residence"] = residence(selected, len(word), k, delay, details)
        assert not selected_report["residence"]["parameter_cover_violations"]
        all_owners = sorted(window for windows in middle.values() for window in windows)
        all_cap = envelope(len(word), k, all_owners)
        selected_report["cap_equals_all_middle_occurrences_cap"] = selected_cap == all_cap
        selected_report["middle_targets_with_multiple_witness_intervals"] = sum(
            len(windows) > 1 for windows in middle.values()
        )
        result["shortest_earliest_middle_owners"] = selected_report
        result["all_middle_occurrences"] = factor_report(
            word, all_cap, all_owners, profiles, k, rank, details
        )
        result["middle_owner_parameter_cover"] = owner_parameter_cover(word, middle, all_cap, k, delay)
        if details:
            selected_report["owners_left_right_mask"] = selected
            result["middle_occurrences_mask_intervals"] = [
                [mask, [[left, right] for left, right, _ in windows]]
                for mask, windows in sorted(middle.items())
            ]
    assert path.read_bytes() == original, f"input changed during analysis: {path}"
    return result


def self_test():
    # Exhaustively check compressed witness cores and insertion-loss predictions.
    for n in range(1, 6):
        for values in product(range(1, 4), repeat=n):
            word = list(values)
            profiles, middle, counts = interval_data(word, 1)
            brute = {}
            for left in range(n):
                for right in range(left, n):
                    mask = interval_union(word, left, right)
                    brute.setdefault(mask, []).append((left, right, mask))
            assert set(profiles) == set(brute)
            for mask, windows in brute.items():
                length, left = min((b - a + 1, a) for a, b, _ in windows)
                assert profiles[mask] == [length, left, max(a for a, _, _ in windows), min(b for _, b, _ in windows)]
                assert counts[mask] == len(windows)
                if mask.bit_count() == 1:
                    assert sorted(middle[mask]) == sorted(windows)
            for p in range(n):
                for bit in range(2):
                    modified = word.copy()
                    modified[p] |= 1 << bit
                    after, _, _ = interval_data(modified, 1)
                    predicted = {
                        mask for mask, (_, _, left, right) in profiles.items()
                        if left <= p <= right and not mask & (1 << bit)
                    }
                    assert set(profiles) - set(after) == predicted
            for delay in range(min(3, n)):
                expected = []
                for p, letter in enumerate(word):
                    if letter != 3:
                        continue
                    for singleton in (1, 2):
                        modified = word.copy()
                        modified[p] = singleton
                        after, _, _ = interval_data(modified, 1)
                        if derivative(word, delay) == derivative(modified, delay) and set(after) >= set(profiles):
                            expected.append([p, letter, singleton])
                observed = singleton_erosions(word, delay, counts, True)
                assert observed["universal_edits_position_before_after"] == expected
    # Exhaustive binary fixed-window factorability, allowing empty letters.
    for m in range(1, 6):
        for delay in range(3):
            for row_values in product(range(2), repeat=m):
                row = list(row_values)
                owners = [(i, i + delay, mask) for i, mask in enumerate(row)]
                cap = envelope(m + delay, 1, owners)
                runs = residence(owners, m + delay, 1, delay, False)
                valid = derivative(cap, delay) == row
                assert valid == (not runs["parameter_cover_violations"])
                assert valid == (not runs["internal_runs_shorter_than_d_plus_1"])
    # Independently test the variable-endpoint criterion, including uncovered
    # positions and widely separated positive owners.
    for n in range(1, 6):
        for m in range(1, n + 1):
            for lefts in combinations(range(n), m):
                for rights in combinations(range(n), m):
                    if any(left > right for left, right in zip(lefts, rights)):
                        continue
                    for masks in product(range(2), repeat=m):
                        owners = list(zip(lefts, rights, masks))
                        cap = envelope(n, 1, owners)
                        valid = all(interval_union(cap, left, right) == mask for left, right, mask in owners)
                        runs = residence(owners, n, 1, 0, False)
                        assert valid == (not runs["parameter_cover_violations"])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--k", nargs="+", type=int, choices=range(1, 17), default=list(range(1, 17)))
    parser.add_argument("--json", action="store_true", help="print structured results")
    parser.add_argument("--details", action="store_true", help="include every omission and local loss")
    parser.add_argument("--self-test", action="store_true", help="run exhaustive small independent checks first")
    args = parser.parse_args()
    if args.self_test:
        self_test()
    root = Path(__file__).resolve().parents[1]
    results = [analyze(root / "answers" / f"k{k:02d}.word", k, args.details) for k in args.k]
    if args.json:
        print(json.dumps(results, indent=2, sort_keys=True))
        return
    for result in results:
        print(f"k={result['k']} d={result['delay']} flat={result['flat_exact_middle_derivative']}")
        for label in ("fixed_delay", "shortest_earliest_middle_owners", "all_middle_occurrences"):
            if label not in result:
                continue
            report = result[label]
            print(
                f"  {label}: changed={report['changed_positions']} "
                f"bits={report['omitted_bit_total']} "
                f"cap/raw={report['cap_bit_total']}/{report['raw_bit_total']} "
                f"decrements={report['decrement_histogram']}"
            )
            print(
                f"    cap_missing_by_rank={report['all_targets_absent_from_cap_by_rank']} "
                f"optional_bits={len(report['optional_single_bit_reinsertions'])} "
                f"safe_whole_restores={len(report['restorable_whole_positions_without_coverage_loss'])}"
            )
            print(f"    omitted_by_bit={report['omitted_count_by_bit']}")
            print(f"    first_length_comparison={report['lower_first_length_comparison_rank_relation_count']}")
            print(f"    changed_first_cells={report['changed_canonical_first_cells_rank_relation_count']}")
            print(f"    bit_restore_loss_hist={report['single_bit_reinsertion_lost_target_count_histogram']}")
            print(f"    canonical_lower_first_cap={report['canonical_lower_first_witness_cap']}")
            if "residence" in report:
                runs = report["residence"]
                print(f"    internal_residence={runs['internal_run_length_histogram']}")
                print(f"    run_length_allowed_width_count={runs['internal_length_allowed_band_width_count']}")
            if args.details:
                print(f"    changes={report['changes_position_raw_cap_omitted_mask']}")
        print(f"  singleton_erosions={result['singleton_erosions']}")
        if "middle_owner_parameter_cover" in result:
            cover = result["middle_owner_parameter_cover"]
            print(
                f"  owner_parameter_cover: selections={cover['exhaustive_selection_count']} "
                f"distinct_caps={cover['distinct_maximal_factors']} "
                f"all_valid={cover['all_parameter_covers_valid']}"
            )
            print(f"    ambiguous={cover['ambiguous_mask_and_intervals']}")
            for selection in cover["selections"]:
                print(
                    f"    choice={selection['choice_indices']} bits={selection['omitted_bit_total']} "
                    f"extra_vs_all={selection['cap_extra_position_bits_over_all_occurrences']} "
                    f"residence_deficit={selection['residence_length_minus_band_width_histogram']}"
                )


if __name__ == "__main__":
    main()
