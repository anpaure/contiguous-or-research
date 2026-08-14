#!/usr/bin/env python3
"""Build a minimum three-cycle decomposition of the frozen D5 matching.

Substantive execution belongs on H100.  For every selected alternating
circuit, the old head at row i is colour i-1 and the new head is colour i.
Thus the relative head permutation is the displayed colour cycle.  Odd
cycles are factored directly; even cycles are paired and their residual
disjoint transpositions are factored by two three-cycles.
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


def three_cycle_map(cycle):
    assert len(cycle) == 3 and len(set(cycle)) == 3
    return cycle_map(cycle)


def apply_factors(value, factors):
    # The listed product is left-to-right; rightmost factor acts first.
    for factor in reversed(factors):
        mapping = three_cycle_map(factor)
        value = mapping.get(value, value)
    return value


def pivot_pairs(cycle, leave_transposition):
    """Return 3-cycles plus an optional final pivot transposition."""
    pivot = cycle[0]
    transpositions = [
        (pivot, cycle[index]) for index in range(len(cycle) - 1, 0, -1)
    ]
    residual = None
    if leave_transposition:
        assert len(transpositions) % 2 == 1
        residual = transpositions.pop()
    else:
        assert len(transpositions) % 2 == 0
    factors = []
    for index in range(0, len(transpositions), 2):
        (a, b), (a2, c) = transpositions[index:index + 2]
        assert a == a2
        # (a b)(a c) = (a c b), with right factors acting first.
        factors.append((a, c, b))
    return factors, residual


def decompose(cycles):
    odd = [record for record in cycles if len(record["cycle"]) % 2 == 1]
    even = [record for record in cycles if len(record["cycle"]) % 2 == 0]
    assert len(even) % 2 == 0
    factors = []
    provenance = []
    odd_count = 0
    paired_count = 0
    for record in odd:
        local, residual = pivot_pairs(record["cycle"], False)
        assert residual is None
        start = len(factors)
        factors.extend(local)
        odd_count += len(local)
        provenance.append({
            "kind": "odd_cycle",
            "edge_indices": [record["edge_index"]],
            "factor_range": [start, len(factors)],
        })
    for pair_index in range(0, len(even), 2):
        left, right = even[pair_index:pair_index + 2]
        left_local, left_t = pivot_pairs(left["cycle"], True)
        right_local, right_t = pivot_pairs(right["cycle"], True)
        start = len(factors)
        factors.extend(left_local)
        factors.extend(right_local)
        a, b = left_t
        c, d = right_t
        assert len({a, b, c, d}) == 4
        # (a b)(c d) = (a c b)(a c d).
        factors.extend(((a, c, b), (a, c, d)))
        paired_count += len(factors) - start
        provenance.append({
            "kind": "even_cycle_pair",
            "edge_indices": [left["edge_index"], right["edge_index"]],
            "factor_range": [start, len(factors)],
        })
    return factors, provenance, odd_count, paired_count


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
        records.append({
            "edge_index": item["edge_index"],
            "cycle": cycle,
        })
    assert len(records) == 41 and len(all_tokens) == 477

    factors, provenance, odd_count, paired_count = decompose(records)
    assert len(factors) == 226
    assert all(
        apply_factors(token, factors) == target[token] for token in all_tokens
    )

    length_histogram = Counter(len(record["cycle"]) for record in records)
    odd_cycles = sum(1 for record in records if len(record["cycle"]) & 1)
    even_cycles = len(records) - odd_cycles
    sign_exponent = sum(len(record["cycle"]) - 1 for record in records)
    assert (sign_exponent, odd_cycles, even_cycles) == (436, 25, 16)
    lower_bound = (len(all_tokens) - odd_cycles) // 2
    assert lower_bound == len(factors)

    appearances = Counter(token for factor in factors for token in factor)
    report = {
        "status": "PASS",
        "selection_sha256": hashlib.sha256(raw).hexdigest(),
        "changed_head_tokens": len(all_tokens),
        "target_circuit_cycles": len(records),
        "target_cycle_length_histogram": dict(sorted(
            length_histogram.items()
        )),
        "odd_length_target_cycles": odd_cycles,
        "even_length_target_cycles": even_cycles,
        "target_sign_exponent": sign_exponent,
        "target_sign": 1,
        "minimum_three_cycle_lower_bound": lower_bound,
        "three_cycle_factors": len(factors),
        "minimality_attained": True,
        "odd_cycle_internal_factors": odd_count,
        "paired_even_cycle_factors": paired_count,
        "even_cycle_pairs": even_cycles // 2,
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
