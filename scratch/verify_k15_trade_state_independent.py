#!/usr/bin/env python3
"""Independent physical verifier for a k=15 quotient trade state.

This deliberately does not import the trade search/audit implementation.  It
expands every selected quotient diamond into its 15 physical translates,
reconstructs the rank-8 Johnson 2-factor from those incidences, and audits
every sliding intersection/union directly.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from hashlib import sha256
from itertools import combinations
import json
from math import comb
from pathlib import Path


K = 15
R = 8
FULL = (1 << K) - 1
W = comb(K, R)


def rotate(mask: int, shift: int) -> int:
    shift %= K
    return ((mask << shift) | (mask >> (K - shift))) & FULL if shift else mask


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("state", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    raw = args.state.read_bytes()
    payload = json.loads(raw)
    items = payload["selected"]
    assert len(items) == W // K == 429

    owner: dict[int, tuple[int, int]] = {}
    upper_declared = Counter()
    incidence = set()
    for item in items:
        lower0 = int(item["lower"])
        a0, b0 = map(int, item["add"])
        assert lower0.bit_count() == R - 1
        assert not (lower0 >> a0) & 1 and not (lower0 >> b0) & 1 and a0 != b0
        for shift in range(K):
            lower = rotate(lower0, shift)
            a, b = (a0 + shift) % K, (b0 + shift) % K
            endpoints = (lower | (1 << a), lower | (1 << b))
            assert all(x.bit_count() == R for x in endpoints)
            if lower in owner:
                raise AssertionError(f"duplicate physical lower owner {lower}")
            owner[lower] = endpoints
            upper_declared[lower | (1 << a) | (1 << b)] += 1
            incidence.add((lower, endpoints[0]))
            incidence.add((lower, endpoints[1]))

    assert len(owner) == W
    adjacency: dict[int, list[tuple[int, int]]] = defaultdict(list)
    for lower, (u, v) in owner.items():
        adjacency[u].append((v, lower))
        adjacency[v].append((u, lower))
    assert len(adjacency) == W
    assert all(len(row) == 2 for row in adjacency.values())

    unseen = set(adjacency)
    cycles = []
    while unseen:
        root = next(iter(unseen))
        cycle = []
        current, previous_lower = root, None
        while True:
            if current in cycle:
                assert current == root
                break
            cycle.append(current)
            unseen.discard(current)
            options = [item for item in adjacency[current] if item[1] != previous_lower]
            if previous_lower is None:
                assert len(options) == 2
                options = options[:1]
            else:
                assert len(options) == 1
            following, lower = options[0]
            assert current & following == lower
            previous_lower = lower
            current = following
        cycles.append(cycle)
    assert sum(map(len, cycles)) == W

    residence3 = coresidence3 = 0
    shadows = []
    for q in range(1, R):
        lower_load, upper_load = Counter(), Counter()
        for cycle in cycles:
            length = len(cycle)
            for i in range(length):
                window = [cycle[(i + t) % length] for t in range(q + 1)]
                lower = FULL
                upper = 0
                for value in window:
                    lower &= value
                    upper |= value
                if lower.bit_count() == R - q:
                    lower_load[lower] += 1
                if upper.bit_count() == R + q:
                    upper_load[upper] += 1
        shadows.append(
            {
                "q": q,
                "lower_distinct": len(lower_load),
                "lower_target": comb(K, R - q),
                "lower_holes": comb(K, R - q) - len(lower_load),
                "lower_histogram": dict(sorted(Counter(lower_load.values()).items())),
                "upper_distinct": len(upper_load),
                "upper_target": comb(K, R + q),
                "upper_holes": comb(K, R + q) - len(upper_load),
                "upper_histogram": dict(sorted(Counter(upper_load.values()).items())),
            }
        )

    cycle_rows = []
    for cycle_index, cycle in enumerate(cycles):
        length = len(cycle)
        residence_positions = []
        coresidence_positions = []
        for i, current in enumerate(cycle):
            following = cycle[(i + 1) % length]
            inserted = following & ~current
            deleted = current & ~following
            assert inserted.bit_count() == deleted.bit_count() == 1
            for t in range(1, 4):
                a, b = cycle[(i + t) % length], cycle[(i + t + 1) % length]
                if (a & ~b) & inserted:
                    residence3 += 1
                    residence_positions.append(i)
                    break
            for t in range(1, 4):
                a, b = cycle[(i + t) % length], cycle[(i + t + 1) % length]
                if (b & ~a) & deleted:
                    coresidence3 += 1
                    coresidence_positions.append(i)
                    break
        cycle_rows.append(
            {
                "index": cycle_index,
                "length": length,
                "residence3_positions": residence_positions,
                "coresidence3_positions": coresidence_positions,
                "vertices": cycle,
            }
        )

    complement_hits = sum(
        ((FULL ^ middle), (FULL ^ lower)) in incidence
        for lower, middle in incidence
    )
    report = {
        "status": "PASS",
        "state": str(args.state),
        "sha256": sha256(raw).hexdigest(),
        "selected_quotient_choices": len(items),
        "physical_lower_owners": len(owner),
        "physical_middle_vertices": len(adjacency),
        "physical_components": len(cycles),
        "physical_cycle_lengths": sorted(map(len, cycles)),
        "physical_cycles": cycle_rows,
        "residence3": residence3,
        "coresidence3": coresidence3,
        "complement_invariant_incidences": complement_hits,
        "declared_q1_upper_distinct": len(upper_declared),
        "declared_q1_upper_histogram": dict(
            sorted(Counter(upper_declared.values()).items())
        ),
        "all_depth_holes": sum(
            row["lower_holes"] + row["upper_holes"] for row in shadows
        ),
        "shadows": shadows,
    }
    if report["all_depth_holes"]:
        raise AssertionError("shadow hole found")
    output = args.output or args.state.with_suffix(".independent_audit.json")
    output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
