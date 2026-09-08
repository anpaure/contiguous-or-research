#!/usr/bin/env python3
"""Verify the finite counts in the D5/MSW scale dichotomy.

Substantive execution belongs on H100.  The symbolic lower bound is that a
degree-two final factor can expose at most two exceptional edges per touched
owner occurrence.  This script independently reconstructs the flat-atlas
incidence graph and evaluates the resulting Catalan thresholds.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import Counter, defaultdict
from pathlib import Path


def catalan(index: int) -> int:
    return math.comb(2 * index, index) // (index + 1)


def first_excess(capacity: int):
    m = 6
    while catalan(m - 6) <= capacity:
        m += 1
    return {
        "m": m,
        "hole_family_size": catalan(m - 6),
        "preceding_m": m - 1,
        "preceding_hole_family_size": catalan(m - 7),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("flat_certificate")
    args = parser.parse_args()

    raw = Path(args.flat_certificate).read_bytes()
    certificate = json.loads(raw)
    assert certificate["status"] == "PASS"
    factors = certificate["factors"]
    assert len(factors) == 226
    assert all(len(factor) == len(set(factor)) == 3 for factor in factors)

    by_token = defaultdict(list)
    for router_index, factor in enumerate(factors):
        for port_index, token in enumerate(factor):
            by_token[token].append([router_index, port_index])
    token_degrees = Counter(len(incidences) for incidences in by_token.values())
    assert token_degrees == Counter({1: 292, 2: 169, 3: 16})
    assert len(by_token) == 477
    assert sum(degree * count for degree, count in token_degrees.items()) == 678

    c6_collars = token_degrees[1] + token_degrees[2]
    c8_collars = token_degrees[3]
    dummy_identity_cuts = token_degrees[1]
    assert (c6_collars, c8_collars, dummy_identity_cuts) == (461, 16, 292)

    router_packages = len(factors)
    owners_per_closed_package = 36
    router_owner_budget = router_packages * owners_per_closed_package
    collar_owner_budget = 6 * c6_collars + 8 * c8_collars
    generous_total_touched_budget = router_owner_budget + collar_owner_budget
    router_only_target_capacity = 2 * router_owner_budget
    generous_total_target_capacity = 2 * generous_total_touched_budget

    rows = []
    for m in range(12, 25):
        holes = catalan(m - 6)
        rows.append({
            "m": m,
            "catalan_holes": holes,
            "minimum_36_owner_packages_from_degree_two_bound": (
                holes + 2 * owners_per_closed_package - 1
            ) // (2 * owners_per_closed_package),
            "constant_226_router_only_capacity_sufficient": (
                holes <= router_only_target_capacity
            ),
            "constant_226_plus_collars_capacity_sufficient": (
                holes <= generous_total_target_capacity
            ),
        })

    report = {
        "status": "PASS",
        "flat_certificate_sha256": hashlib.sha256(raw).hexdigest(),
        "router_nodes": router_packages,
        "router_degree_histogram": {"3": router_packages},
        "token_nodes": len(by_token),
        "token_degree_histogram": {
            str(degree): count for degree, count in sorted(token_degrees.items())
        },
        "router_token_incidences": sum(map(len, factors)),
        "maximum_bipartite_degree": max(3, max(token_degrees)),
        "proposed_token_collar_counts": {
            "C6_for_degree_1_or_2": c6_collars,
            "C8_for_degree_3": c8_collars,
            "dummy_identity_cuts_for_degree_1": dummy_identity_cuts,
        },
        "owner_budgets_if_all_collar_owners_are_exceptional": {
            "226_times_36_router_package_owners": router_owner_budget,
            "461_times_6_plus_16_times_8_collar_owners": collar_owner_budget,
            "total": generous_total_touched_budget,
        },
        "degree_two_upper_target_capacity_bounds": {
            "router_packages_only": router_only_target_capacity,
            "router_packages_plus_all_collar_owners": generous_total_target_capacity,
        },
        "first_catalan_hole_excess": {
            "router_packages_only": first_excess(router_only_target_capacity),
            "router_packages_plus_all_collar_owners": first_excess(
                generous_total_target_capacity
            ),
        },
        "sample_scale_rows": rows,
        "symbolic_bound": (
            "P disjoint 36-owner packages touch at most 36P owner "
            "occurrences and hence at most 72P final degree-two edges; "
            "Cat_(m-6) distinct holes require P >= ceil(Cat_(m-6)/72)"
        ),
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
