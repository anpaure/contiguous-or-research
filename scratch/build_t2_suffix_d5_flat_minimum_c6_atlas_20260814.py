#!/usr/bin/env python3
"""Build a minimum-exposure minimum C6-router atlas for frozen D5.

Substantive execution belongs on H100.  Odd target cycles are written as
overlapping adjacent triples.  Even target cycles are paired: the first
``l-1`` points of each cycle are handled by the same chain, and the two
residual disjoint transpositions are handled by two triples.  The resulting
atlas is still minimum (226 triples), while every token occurs at most three
times instead of nine times in the earlier one-pivot decomposition.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path


def cycle_map(cycle):
    return {
        value: cycle[(index + 1) % len(cycle)]
        for index, value in enumerate(cycle)
    }


def apply_factors(value, factors):
    # Listed product; rightmost factor acts first.
    for factor in reversed(factors):
        mapping = cycle_map(factor)
        value = mapping.get(value, value)
    return value


def odd_chain(points):
    """Factor the odd cycle on ``points`` into overlapping triples."""
    assert len(points) >= 3 and len(points) % 2 == 1
    return [
        (points[index], points[index + 1], points[index + 2])
        for index in range(0, len(points) - 2, 2)
    ]


def decompose(records):
    odd = [record for record in records if len(record["cycle"]) % 2 == 1]
    even = [record for record in records if len(record["cycle"]) % 2 == 0]
    assert len(even) % 2 == 0

    factors = []
    provenance = []
    for record in odd:
        start = len(factors)
        factors.extend(odd_chain(record["cycle"]))
        provenance.append({
            "kind": "odd_adjacent_chain",
            "edge_indices": [record["edge_index"]],
            "factor_range": [start, len(factors)],
        })

    for pair_index in range(0, len(even), 2):
        left, right = even[pair_index:pair_index + 2]
        u = left["cycle"]
        v = right["cycle"]
        start = len(factors)
        factors.extend(odd_chain(u[:-1]))
        factors.extend(odd_chain(v[:-1]))

        # The two even cycles leave residual transpositions (a b),(c d).
        # With right factors acting first,
        #       (a b)(c d) = (a c b)(a c d).
        a, b = u[-2], u[-1]
        c, d = v[-2], v[-1]
        assert len({a, b, c, d}) == 4
        factors.extend(((a, c, b), (a, c, d)))
        provenance.append({
            "kind": "paired_even_adjacent_chains",
            "edge_indices": [left["edge_index"], right["edge_index"]],
            "residual_transpositions": [[a, b], [c, d]],
            "factor_range": [start, len(factors)],
        })

    return factors, provenance


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("selection")
    args = parser.parse_args()
    raw = Path(args.selection).read_bytes()
    selection = json.loads(raw)
    assert selection["status"] == "SAT"

    records = []
    all_tokens = set()
    target = {}
    for item in selection["selection"]:
        cycle = tuple(item["candidate"]["new_colours"])
        assert len(cycle) == len(set(cycle))
        assert not all_tokens.intersection(cycle)
        all_tokens.update(cycle)
        mapping = cycle_map(cycle)
        assert not set(target).intersection(mapping)
        target.update(mapping)
        records.append({"edge_index": item["edge_index"], "cycle": cycle})

    assert len(records) == 41 and len(all_tokens) == 477
    factors, provenance = decompose(records)
    assert all(
        apply_factors(token, factors) == target[token]
        for token in all_tokens
    )

    length_histogram = Counter(len(record["cycle"]) for record in records)
    odd_cycles = sum(len(record["cycle"]) % 2 for record in records)
    sign_exponent = sum(len(record["cycle"]) - 1 for record in records)
    lower_bound = (len(all_tokens) - odd_cycles) // 2
    appearances = Counter(token for factor in factors for token in factor)

    assert len(factors) == lower_bound == 226
    assert max(appearances.values()) == 3
    assert sum(appearances.values()) == 3 * len(factors) == 678
    assert set(appearances) == all_tokens

    report = {
        "status": "PASS",
        "selection_sha256": hashlib.sha256(raw).hexdigest(),
        "changed_head_tokens": len(all_tokens),
        "target_circuit_cycles": len(records),
        "target_cycle_length_histogram": dict(sorted(length_histogram.items())),
        "odd_length_target_cycles": odd_cycles,
        "even_length_target_cycles": len(records) - odd_cycles,
        "target_sign_exponent": sign_exponent,
        "minimum_three_cycle_lower_bound": lower_bound,
        "three_cycle_factors": len(factors),
        "minimality_attained": True,
        "port_token_appearance_histogram": dict(sorted(Counter(
            appearances.values()
        ).items())),
        "maximum_port_token_appearances": max(appearances.values()),
        "product_verified_on_all_tokens": True,
        "factor_convention": "listed product; rightmost factor acts first",
        "provenance": provenance,
        "factors": [list(factor) for factor in factors],
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
