#!/usr/bin/env python3
"""Independent replay of the flat minimum D5 three-cycle atlas.

This audit deliberately does not import the constructor.  Substantive
execution belongs on H100.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path


def cycle_action(points):
    return {
        point: points[(index + 1) % len(points)]
        for index, point in enumerate(points)
    }


def apply_product(point, factors):
    for factor in factors[::-1]:
        point = cycle_action(factor).get(point, point)
    return point


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("selection")
    parser.add_argument("certificate")
    args = parser.parse_args()

    selection_bytes = Path(args.selection).read_bytes()
    certificate_bytes = Path(args.certificate).read_bytes()
    selection = json.loads(selection_bytes)
    certificate = json.loads(certificate_bytes)
    assert selection["status"] == "SAT"
    assert certificate["status"] == "PASS"
    assert certificate["selection_sha256"] == hashlib.sha256(
        selection_bytes
    ).hexdigest()

    target = {}
    records = {}
    cycle_lengths = []
    tokens = set()
    for item in selection["selection"]:
        cycle = item["candidate"]["new_colours"]
        edge_index = item["edge_index"]
        assert edge_index not in records
        records[edge_index] = tuple(cycle)
        assert len(cycle) == len(set(cycle))
        assert tokens.isdisjoint(cycle)
        tokens.update(cycle)
        target.update(cycle_action(cycle))
        cycle_lengths.append(len(cycle))

    factors = certificate["factors"]
    assert len(factors) == 226
    assert all(len(factor) == len(set(factor)) == 3 for factor in factors)
    assert all(apply_product(token, factors) == target[token] for token in tokens)

    odd_cycles = sum(length % 2 for length in cycle_lengths)
    lower_bound = (len(tokens) - odd_cycles) // 2
    assert (len(tokens), len(cycle_lengths), odd_cycles, lower_bound) == (
        477, 41, 25, 226
    )

    appearances = Counter(point for factor in factors for point in factor)
    assert set(appearances) == tokens
    assert sum(appearances.values()) == 678
    assert max(appearances.values()) == 3
    assert Counter(appearances.values()) == {1: 292, 2: 169, 3: 16}

    # Check the stronger shape claim: within each target cycle, all ordinary
    # chain joints occur twice, and only the two selected penultimate points
    # in an even-cycle pair can acquire a third occurrence.
    provenance = certificate["provenance"]
    covered_factor_indices = []
    covered_source_indices = []
    residual_penultimate = set()
    for record in provenance:
        lo, hi = record["factor_range"]
        assert 0 <= lo < hi <= len(factors)
        covered_factor_indices.extend(range(lo, hi))
        source_indices = record["edge_indices"]
        assert len(source_indices) == len(set(source_indices))
        assert all(index in records for index in source_indices)
        covered_source_indices.extend(source_indices)
        source_cycles = [records[index] for index in source_indices]
        local_factors = [tuple(factor) for factor in factors[lo:hi]]
        local_support = set().union(*map(set, source_cycles))
        assert all(set(factor) <= local_support for factor in local_factors)
        local_target = {}
        for cycle in source_cycles:
            assert set(local_target).isdisjoint(cycle)
            local_target.update(cycle_action(cycle))
        assert all(
            apply_product(token, local_factors) == local_target[token]
            for token in local_support
        )
        if record["kind"] == "odd_adjacent_chain":
            assert len(source_cycles) == 1 and len(source_cycles[0]) % 2 == 1
            cycle = source_cycles[0]
            expected = [tuple(cycle[i:i + 3]) for i in range(0, len(cycle) - 2, 2)]
            assert local_factors == expected
        elif record["kind"] == "paired_even_adjacent_chains":
            assert len(source_cycles) == 2
            assert all(len(cycle) % 2 == 0 for cycle in source_cycles)
            left, right = source_cycles
            pairs = record["residual_transpositions"]
            assert pairs == [list(left[-2:]), list(right[-2:])]
            a, b = left[-2:]
            c, d = right[-2:]
            expected = (
                [tuple(left[i:i + 3]) for i in range(0, len(left) - 3, 2)]
                + [tuple(right[i:i + 3]) for i in range(0, len(right) - 3, 2)]
                + [(a, c, b), (a, c, d)]
            )
            assert local_factors == expected
            residual_penultimate.update(pair[0] for pair in pairs)
        else:
            raise AssertionError(record["kind"])
    assert sorted(covered_factor_indices) == list(range(len(factors)))
    assert Counter(covered_source_indices) == Counter(records.keys())
    assert len(residual_penultimate) == 16
    assert all(appearances[token] == 3 for token in residual_penultimate)
    assert all(
        count <= (3 if token in residual_penultimate else 2)
        for token, count in appearances.items()
    )

    by_count = defaultdict(list)
    for token, count in appearances.items():
        by_count[count].append(token)
    report = {
        "status": "PASS",
        "selection_sha256": hashlib.sha256(selection_bytes).hexdigest(),
        "certificate_sha256": hashlib.sha256(certificate_bytes).hexdigest(),
        "target_verified_on_all_tokens": True,
        "minimum_router_count": lower_bound,
        "factor_count": len(factors),
        "maximum_token_appearances": max(appearances.values()),
        "appearance_histogram": {
            str(count): len(points) for count, points in sorted(by_count.items())
        },
        "only_even_pair_penultimate_tokens_can_have_three": True,
        "factor_ranges_partition_certificate": True,
        "source_cycles_partition_selection": True,
        "canonical_local_factors_verified": True,
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
