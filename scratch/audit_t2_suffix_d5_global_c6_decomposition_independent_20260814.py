#!/usr/bin/env python3
"""Independent replay of the frozen 226-three-cycle D5 decomposition.

Run on H100 only.  This imports none of the constructor code.
"""

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path


def cycle_map(cycle):
    return {value: cycle[(i + 1) % len(cycle)] for i, value in enumerate(cycle)}


def apply_product(value, factors):
    for factor in reversed(factors):
        if value in factor:
            value = factor[(factor.index(value) + 1) % 3]
    return value


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("selection")
    parser.add_argument("decomposition")
    args = parser.parse_args()
    selection_raw = Path(args.selection).read_bytes()
    decomposition_raw = Path(args.decomposition).read_bytes()
    selection = json.loads(selection_raw)
    decomposition = json.loads(decomposition_raw)
    assert selection["status"] == "SAT" and decomposition["status"] == "PASS"
    assert decomposition["selection_sha256"] == hashlib.sha256(selection_raw).hexdigest()

    records = {
        item["edge_index"]: tuple(item["candidate"]["new_colours"])
        for item in selection["selection"]
    }
    assert len(records) == len(selection["selection"])
    cycles = list(records.values())
    tokens = set()
    target = {}
    for cycle in cycles:
        assert len(cycle) == len(set(cycle))
        assert not tokens.intersection(cycle)
        tokens.update(cycle)
        target.update(cycle_map(cycle))
    assert len(cycles) == 41 and len(tokens) == len(target) == 477

    factors = [tuple(factor) for factor in decomposition["factors"]]
    assert len(factors) == 226
    assert all(len(factor) == len(set(factor)) == 3 for factor in factors)
    assert all(set(factor) <= tokens for factor in factors)
    assert all(apply_product(token, factors) == target[token] for token in tokens)

    length_histogram = Counter(map(len, cycles))
    odd_cycles = sum(len(cycle) % 2 for cycle in cycles)
    even_cycles = len(cycles) - odd_cycles
    sign_exponent = sum(len(cycle) - 1 for cycle in cycles)
    lower_bound = (len(tokens) - odd_cycles) // 2
    assert (odd_cycles, even_cycles, sign_exponent, lower_bound) == (25, 16, 436, 226)
    appearances = Counter(token for factor in factors for token in factor)
    appearance_histogram = Counter(appearances.values())
    assert sum(appearances.values()) == 678
    assert sum(count for token, count in appearances.items() if count > 1) - sum(
        1 for count in appearances.values() if count > 1
    ) == 201
    assert appearance_histogram == {1: 436, 4: 6, 5: 11, 6: 10, 7: 10, 8: 3, 9: 1}

    ranges = []
    source_indices = []
    provenance_kinds = Counter()
    for item in decomposition["provenance"]:
        start, stop = item["factor_range"]
        assert 0 <= start < stop <= len(factors)
        ranges.extend(range(start, stop))
        provenance_kinds[item["kind"]] += stop - start
        indices = item["edge_indices"]
        assert len(indices) == len(set(indices))
        assert all(index in records for index in indices)
        source_indices.extend(indices)
        source_cycles = [records[index] for index in indices]
        local_support = set().union(*map(set, source_cycles))
        local_factors = factors[start:stop]
        assert all(set(factor) <= local_support for factor in local_factors)
        local_target = {}
        for cycle in source_cycles:
            assert not set(local_target).intersection(cycle)
            local_target.update(cycle_map(cycle))
        assert all(
            apply_product(token, local_factors) == local_target[token]
            for token in local_support
        )
        if item["kind"] == "odd_cycle":
            assert len(source_cycles) == 1 and len(source_cycles[0]) % 2 == 1
            assert stop - start == (len(source_cycles[0]) - 1) // 2
        elif item["kind"] == "even_cycle_pair":
            assert len(source_cycles) == 2
            assert all(len(cycle) % 2 == 0 for cycle in source_cycles)
            assert stop - start == sum(map(len, source_cycles)) // 2
        else:
            raise AssertionError(item["kind"])
    assert sorted(ranges) == list(range(226))
    assert Counter(source_indices) == Counter(records.keys())
    assert provenance_kinds == {"odd_cycle": 131, "even_cycle_pair": 95}

    print(json.dumps({
        "status": "PASS",
        "selection_sha256": hashlib.sha256(selection_raw).hexdigest(),
        "decomposition_sha256": hashlib.sha256(decomposition_raw).hexdigest(),
        "tokens": len(tokens),
        "target_cycles": len(cycles),
        "cycle_length_histogram": dict(sorted(length_histogram.items())),
        "odd_even_cycles": [odd_cycles, even_cycles],
        "target_sign_exponent": sign_exponent,
        "minimum_three_cycle_lower_bound": lower_bound,
        "factor_count": len(factors),
        "provenance_factor_counts": dict(provenance_kinds),
        "provenance_partition_verified": True,
        "each_provenance_product_verified": True,
        "product_verified_on_all_tokens": True,
        "port_appearances": sum(appearances.values()),
        "extra_port_appearances": sum(appearances.values()) - len(tokens),
        "appearance_histogram": dict(sorted(appearance_histogram.items())),
        "maximum_appearances": max(appearances.values()),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
