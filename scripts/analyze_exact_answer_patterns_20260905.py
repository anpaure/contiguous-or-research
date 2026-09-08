"""Direct, dependency-free structural census of the sixteen exact OR words.

Input bodies are read in full and authenticated against answers/README.md.
No answer is modified. Positions and owner indices in JSON are zero-based.
"""

import argparse
from collections import Counter
from hashlib import sha256
from itertools import product
import json
from math import comb
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]


def interval_census(word, k):
    """Group equal suffix unions by their contiguous range of start indices."""
    limit = 1 << k
    counts = [0] * limit
    shortest = [len(word) + 1] * limit
    first = [None] * limit
    active = {}
    for right, letter in enumerate(word):
        following = {letter: (right, right)}
        for mask, (lo, hi) in active.items():
            value = mask | letter
            if value in following:
                old_lo, old_hi = following[value]
                following[value] = (min(lo, old_lo), max(hi, old_hi))
            else:
                following[value] = (lo, hi)
        assert sum(hi - lo + 1 for lo, hi in following.values()) == right + 1
        for mask, (lo, hi) in following.items():
            counts[mask] += hi - lo + 1
            shortest[mask] = min(shortest[mask], right - hi + 1)
            if first[mask] is None:
                first[mask] = (hi, right)
        active = following
    assert sum(counts) == len(word) * (len(word) + 1) // 2
    return counts, shortest, first


def census(k, expected_hash):
    path = ROOT / "answers" / f"k{k:02d}.word"
    raw = path.read_bytes()
    digest = sha256(raw).hexdigest()
    assert digest == expected_hash
    word = [int(token) for token in raw.split()]
    full = (1 << k) - 1
    assert word and all(0 < mask <= full for mask in word)
    n = len(word)
    rank = (k + 1) // 2
    width = comb(k, rank)
    lower = sum(comb(k, j) for j in range(1, rank))
    depth = 0
    while depth * width + comb(depth + 1, 2) < lower:
        depth += 1
    assert n == width + depth
    counts, shortest, first = interval_census(word, k)
    assert all(counts[1:])

    minimum_by_rank = [Counter() for _ in range(k + 1)]
    uniquely_witnessed = [0] * (k + 1)
    for mask in range(1, full + 1):
        size = mask.bit_count()
        minimum_by_rank[size][shortest[mask]] += 1
        uniquely_witnessed[size] += counts[mask] == 1
        if size < rank:
            assert shortest[mask] <= depth

    row = word
    exact_rows = []
    short_occurrences = Counter()
    short_lower = set()
    critical = None
    for length in range(1, min(n, k) + 1):
        occurrence_ranks = Counter(mask.bit_count() for mask in row)
        unique_ranks = Counter(mask.bit_count() for mask in set(row))
        exact_rows.append({"length": length, "occurrences": dict(occurrence_ranks),
                           "distinct_targets": dict(unique_ranks)})
        if length <= depth:
            short_occurrences.update(occurrence_ranks)
            short_lower.update(mask for mask in row if mask.bit_count() < rank)
        if length == depth + 1:
            critical = row
        row = [a | b for a, b in zip(row, row[1:])]
    assert critical is not None
    assert len(short_lower) == lower
    short_capacity = depth * width + comb(depth + 1, 2)
    assert sum(short_occurrences.values()) == short_capacity
    short_repeats = sum(v for s, v in short_occurrences.items() if s < rank) - lower
    short_intrusions = sum(v for s, v in short_occurrences.items() if s >= rank)
    assert short_repeats + short_intrusions == short_capacity - lower

    owners = sorted((*first[mask], mask) for mask in range(1, full + 1)
                    if mask.bit_count() == rank)
    assert len(owners) == width
    offsets = []
    for i, (left, right, _) in enumerate(owners):
        a, b = left - i, right - i
        assert 0 <= a <= b <= depth
        if offsets:
            assert offsets[-1][0] <= a and offsets[-1][1] <= b
        offsets.append((a, b))
    phases = []
    for i, offset in enumerate(offsets):
        if not phases or phases[-1]["offsets"] != offset:
            phases.append({"first_owner": i, "past_last_owner": i + 1,
                           "offsets": offset, "window_length": offset[1] - offset[0] + 1})
        else:
            phases[-1]["past_last_owner"] = i + 1
    assert len(phases) <= 2 * depth + 1
    chronology = [mask for _, _, mask in owners]
    transitions = Counter((a & ~b).bit_count() for a, b in zip(chronology, chronology[1:]))
    lower_shadows = {a & b for a, b in zip(chronology, chronology[1:])
                     if (a & b).bit_count() == rank - 1}
    upper_shadows = {a | b for a, b in zip(chronology, chronology[1:])
                     if (a | b).bit_count() == rank + 1}
    flat = (len(critical) == width and len(set(critical)) == width
            and all(mask.bit_count() == rank for mask in critical))
    upper_clock_defects = {
        s: sum(count for length, count in minimum_by_rank[s].items()
               if length != s - rank + depth + 1)
        for s in range(rank + 1, k + 1)
    }
    delayed_small_targets = [
        {"target": mask, "rank": mask.bit_count(), "shortest_length": shortest[mask]}
        for mask in range(1, full + 1)
        if mask.bit_count() <= rank - depth and shortest[mask] > 1
    ]
    upper_row_defects = {
        record["length"]: sum(count for size, count in record["occurrences"].items()
                              if size != min(k, rank + record["length"] - depth - 1))
        for record in exact_rows if record["length"] >= depth + 1
    }
    return {
        "k": k, "length": n, "width": width, "depth": depth, "middle_rank": rank,
        "sha256": digest, "verified_nonempty_targets": full,
        "letter_ranks": dict(Counter(mask.bit_count() for mask in word)),
        "distinct_letter_ranks": dict(Counter(mask.bit_count() for mask in set(word))),
        "repeated_letters": n - len(set(word)),
        "coordinate_frequencies": [sum(bool(mask & (1 << bit)) for mask in word)
                                   for bit in range(k)],
        "minimum_witness_lengths": [dict(c) for c in minimum_by_rank[1:]],
        "uniquely_witnessed_by_rank": uniquely_witnessed[1:],
        "exact_window_rows": exact_rows,
        "flat_critical_derivative": flat,
        "critical_derivative_ranks": dict(Counter(mask.bit_count() for mask in critical)),
        "critical_distinct_middle_targets": sum(mask.bit_count() == rank for mask in set(critical)),
        "middle_owner_lengths": dict(Counter(right - left + 1 for left, right, _ in owners)),
        "middle_offset_phases": phases,
        "middle_linear_johnson_distances": dict(transitions),
        "middle_closing_johnson_distance": (chronology[-1] & ~chronology[0]).bit_count(),
        "linear_adjacent_shadow_holes": {
            "lower": comb(k, rank - 1) - len(lower_shadows),
            "upper": (comb(k, rank + 1) if rank < k else 0) - len(upper_shadows),
        },
        "upper_shortest_clock_defects": upper_clock_defects,
        "upper_occurrence_row_defects": upper_row_defects,
        "delayed_small_targets": delayed_small_targets,
        "short_cell_ledger": {
            "capacity": short_capacity, "distinct_lower_targets": lower,
            "repeated_lower_occurrences": short_repeats, "rank_at_least_middle": short_intrusions,
            "slack": short_capacity - lower,
        },
    }


def self_test():
    cases = 0
    for k in range(1, 4):
        for n in range(1, 5):
            for word in product(range(1, 1 << k), repeat=n):
                counts, shortest, first = interval_census(word, k)
                expected_counts = [0] * (1 << k)
                expected_shortest = [n + 1] * (1 << k)
                witnesses = [[] for _ in range(1 << k)]
                for left in range(n):
                    value = 0
                    for right in range(left, n):
                        value |= word[right]
                        expected_counts[value] += 1
                        expected_shortest[value] = min(expected_shortest[value], right - left + 1)
                        witnesses[value].append((left, right))
                expected_first = [min(v, key=lambda pair: (pair[1], -pair[0])) if v else None
                                  for v in witnesses]
                assert (counts, shortest, first) == (expected_counts, expected_shortest, expected_first)
                cases += 1
    print(f"PASS: {cases} exhaustive interval-census tests")


def compact(histogram):
    return ",".join(f"{key}:{value}" for key, value in sorted(histogram.items()))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
    manifest = (ROOT / "answers" / "README.md").read_text()
    hashes = {int(k): digest for k, digest in re.findall(
        r"\|\s*(\d+)\s*\|\s*\d+\s*\|\s*`([0-9a-f]{64})`", manifest)}
    reports = [census(k, hashes[k]) for k in range(1, 17)]
    if args.json:
        print(json.dumps(reports, sort_keys=True, indent=2))
        return
    print("| k | n | d | letter ranks (rank:positions) | repeated letters | flat | owner lengths | phases | short repeats / intrusions |")
    print("|---:|---:|---:|---|---:|---|---|---:|---|")
    for r in reports:
        ledger = r["short_cell_ledger"]
        print(f'| {r["k"]} | {r["length"]} | {r["depth"]} | {compact(r["letter_ranks"])} '
              f'| {r["repeated_letters"]} | {r["flat_critical_derivative"]} '
              f'| {compact(r["middle_owner_lengths"])} | {len(r["middle_offset_phases"])} '
              f'| {ledger["repeated_lower_occurrences"]} / {ledger["rank_at_least_middle"]} |')
    print("\nCritical derivative and linear transition profiles:")
    for r in reports:
        print(f'k={r["k"]}: critical={compact(r["critical_derivative_ranks"])}, '
              f'Johnson={compact(r["middle_linear_johnson_distances"])}, '
              f'closing={r["middle_closing_johnson_distance"]}, '
              f'shadow holes={r["linear_adjacent_shadow_holes"]}')
    print("\nCanonical middle-witness phases for nonflat words:")
    for r in reports:
        if not r["flat_critical_derivative"]:
            print(f'k={r["k"]}: {r["middle_offset_phases"]}')
    print("\nDistinct letters by rank and minimum witness lengths by rank:")
    for r in reports:
        print(f'k={r["k"]}: letters={compact(r["distinct_letter_ranks"])}; '
              f'shortest={r["minimum_witness_lengths"]}')
    print("\nUpper shortest-clock versus full-row defects (zero entries omitted):")
    for r in reports:
        print(f'k={r["k"]}: shortest={compact({s: v for s, v in r["upper_shortest_clock_defects"].items() if v})}; '
              f'rows={compact({s: v for s, v in r["upper_occurrence_row_defects"].items() if v})}; '
              f'delayed small count={len(r["delayed_small_targets"])}')
        if 0 < len(r["delayed_small_targets"]) <= 5:
            print(f'  delayed targets={r["delayed_small_targets"]}')
    print("\nPASS: all sixteen complete input bodies authenticated and universal")


if __name__ == "__main__":
    main()
