#!/usr/bin/env python3
"""Exhaustive finite audit of the Venn/gap refinement lemma.

Substantive runs are intended for H100.  For every nonempty target
subfamily at r=2,3,4,5, this script checks:

* every elementary boundary gap has size at most r+2;
* the exact factorial gap-majorization bound;
* V(T)/G(T) <= 8^(|T|-1); and
* every one-target extension U subset T satisfies
  (V(T)/G(T))/(V(U)/G(U)) <= 8.

Here V is the product of labelled Venn-cell factorials and G is the
product of elementary boundary-gap factorials.  The theorem is analytic;
this is an independent finite regression audit.
"""

from __future__ import annotations

import argparse
import json
import math


def audit(r: int) -> dict[str, object]:
    b = 2 * r + 1
    target_count = 4 * r
    endpoints: list[int] = []
    label_hits = [0] * b
    index = 0
    for length in (r, r - 1):
        for start in range(1, b):
            endpoints.append((1 << start) | (1 << ((start + length) % b)))
            target = 0
            for offset in range(length):
                target |= 1 << ((start + offset) % b)
            for label in range(b):
                if (target >> label) & 1:
                    label_hits[label] |= 1 << index
            index += 1
    assert index == target_count

    family_count = 1 << target_count
    endpoint_union = [0] * family_count
    merge_ratio = [0] * family_count
    maximum_extension_numerator = 0
    maximum_extension_denominator = 1
    maximum_extension_witness: tuple[int, int] | None = None

    for mask in range(1, family_count):
        last_flag = mask & -mask
        last_index = last_flag.bit_length() - 1
        endpoint_union[mask] = endpoint_union[mask ^ last_flag] | endpoints[last_index]
        cuts = [cut for cut in range(b) if (endpoint_union[mask] >> cut) & 1]
        gaps = [
            (cuts[(position + 1) % len(cuts)] - cut) % b
            for position, cut in enumerate(cuts)
        ]
        assert sum(gaps) == b
        assert max(gaps) <= r + 2
        gap_product = math.prod(math.factorial(gap) for gap in gaps)

        cells: dict[int, int] = {}
        for hit in label_hits:
            signature = hit & mask
            cells[signature] = cells.get(signature, 0) + 1
        venn_product = math.prod(math.factorial(size) for size in cells.values())
        assert venn_product % gap_product == 0
        ratio = venn_product // gap_product
        merge_ratio[mask] = ratio
        size = mask.bit_count()
        assert ratio <= 8 ** (size - 1)

        q = len(cuts)
        if q <= r:
            majorant = math.factorial(r + 2) * math.factorial(r - q + 1)
        else:
            majorant = math.factorial(2 * r - q + 2)
        assert gap_product <= majorant

        work = mask
        while work:
            flag = work & -work
            old = mask ^ flag
            if old:
                numerator = ratio
                denominator = merge_ratio[old]
                assert numerator <= 8 * denominator
                if (
                    numerator * maximum_extension_denominator
                    > maximum_extension_numerator * denominator
                ):
                    maximum_extension_numerator = numerator
                    maximum_extension_denominator = denominator
                    maximum_extension_witness = (mask, flag.bit_length() - 1)
            work ^= flag

    divisor = math.gcd(maximum_extension_numerator, maximum_extension_denominator)
    return {
        "r": r,
        "families_checked": family_count - 1,
        "maximum_extension_ratio": (
            f"{maximum_extension_numerator // divisor}/"
            f"{maximum_extension_denominator // divisor}"
        ),
        "maximum_extension_witness": maximum_extension_witness,
        "status": "PASS",
    }


def main(first: int, last: int) -> None:
    for r in range(first, last + 1):
        print(json.dumps(audit(r), sort_keys=True), flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--first", type=int, default=2)
    parser.add_argument("--last", type=int, default=5)
    arguments = parser.parse_args()
    main(arguments.first, arguments.last)
