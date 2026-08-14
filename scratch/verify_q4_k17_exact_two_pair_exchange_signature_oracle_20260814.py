#!/usr/bin/env python3
"""Independently verify the exact two-pair score/pruning oracle (H100 only)."""

from __future__ import annotations

import itertools
import json
import random
from collections import defaultdict


def add_cost(load):
    return 2 * load - 1


def remove_cost(load):
    return 3 - 2 * load


def energy(loads):
    return sum((load - 1) ** 2 for load in loads)


def direct_delta(loads, outgoing, incoming):
    changed = list(loads)
    for column in outgoing:
        for row in column:
            changed[row] -= 1
    for column in incoming:
        for row in column:
            changed[row] += 1
    return energy(changed) - energy(loads)


def face_terms(loads, left, right, candidate):
    add = sum(add_cost(loads[row]) for row in candidate)
    return add - 2 * len(candidate & left) - 2 * len(candidate & right)


def formula_delta(loads, left, right, first, second):
    constant = (
        sum(remove_cost(loads[row]) for row in left)
        + sum(remove_cost(loads[row]) for row in right)
        + 2 * len(left & right)
    )
    return (
        constant
        + face_terms(loads, left, right, first)
        + face_terms(loads, left, right, second)
        + 2 * len(first & second)
    )


def minimum_overlap_by_subset_query(candidate, bucket):
    """Literal 2^|N| subset query, implemented with Python integer bitsets."""
    if not bucket:
        return None
    ordered = sorted(candidate)
    all_members = (1 << len(bucket)) - 1
    incidence = {}
    for row in ordered:
        bits = 0
        for index, other in enumerate(bucket):
            if row in other:
                bits |= 1 << index
        incidence[row] = bits
    for size in range(len(ordered) + 1):
        for allowed_tuple in itertools.combinations(ordered, size):
            allowed = set(allowed_tuple)
            feasible = all_members
            for row in ordered:
                if row not in allowed:
                    feasible &= ~incidence[row]
            if feasible:
                index = (feasible & -feasible).bit_length() - 1
                return len(candidate & bucket[index])
    raise AssertionError("nonempty bucket had no subset-query result")


def main():
    scalar_cases = 0
    for load in range(5):
        for p, q, n, m in itertools.product((0, 1), repeat=4):
            direct = (load - p - q + n + m - 1) ** 2 - (load - 1) ** 2
            formula = (
                p * remove_cost(load)
                + q * remove_cost(load)
                + 2 * p * q
                + n * (add_cost(load) - 2 * p - 2 * q)
                + m * (add_cost(load) - 2 * p - 2 * q)
                + 2 * n * m
            )
            assert direct == formula
            scalar_cases += 1

    generator = random.Random(20260814)
    row_count = 26
    column_size = 10
    all_columns = set()
    while len(all_columns) < 48:
        all_columns.add(frozenset(generator.sample(range(row_count), column_size)))
    columns = sorted(all_columns, key=lambda column: tuple(sorted(column)))
    selected = columns[:6]
    candidates = columns[6:]
    loads = [0] * row_count
    for column in selected:
        for row in column:
            loads[row] += 1

    exchanges_checked = 0
    dead_faces = 0
    live_faces = 0
    negative_exchanges = 0
    retained_negative_endpoints = 0
    subset_queries = 0
    for left, right in itertools.combinations(selected, 2):
        constant = (
            sum(remove_cost(loads[row]) for row in left)
            + sum(remove_cost(loads[row]) for row in right)
            + 2 * len(left & right)
        )
        scores = {candidate: face_terms(loads, left, right, candidate)
                  for candidate in candidates}
        minimum = min(scores.values())
        threshold = -constant - minimum
        dead = constant + 2 * minimum >= 0
        dead_faces += dead
        live_faces += not dead
        retained = {candidate for candidate, score in scores.items()
                    if score < threshold}

        actual_negative = []
        for first, second in itertools.combinations(candidates, 2):
            direct = direct_delta(loads, (left, right), (first, second))
            formula = formula_delta(loads, left, right, first, second)
            assert direct == formula
            exchanges_checked += 1
            if direct < 0:
                negative_exchanges += 1
                actual_negative.append((first, second))
                assert first in retained and second in retained
                retained_negative_endpoints += 2
        if dead:
            assert not actual_negative

        buckets = defaultdict(list)
        for candidate in retained:
            buckets[scores[candidate]].append(candidate)
        for candidate in retained:
            for bucket in buckets.values():
                direct_minimum = min(len(candidate & other) for other in bucket)
                queried = minimum_overlap_by_subset_query(candidate, bucket)
                assert queried == direct_minimum
                subset_queries += 1

    # A second suite starts from an exact disjoint cover.  It supplies
    # nonvacuous dead-face certificates for the minimum cut.
    exact_row_count = 60
    exact_selected = [
        frozenset(range(10 * block, 10 * (block + 1))) for block in range(6)
    ]
    exact_candidates = set()
    while len(exact_candidates) < 42:
        candidate = frozenset(
            generator.sample(range(exact_row_count), column_size)
        )
        if candidate not in exact_selected:
            exact_candidates.add(candidate)
    exact_candidates = sorted(
        exact_candidates, key=lambda column: tuple(sorted(column))
    )
    exact_loads = [1] * exact_row_count
    exact_dead_faces = 0
    exact_exchange_pairs = 0
    for left, right in itertools.combinations(exact_selected, 2):
        constant = (
            sum(remove_cost(exact_loads[row]) for row in left)
            + sum(remove_cost(exact_loads[row]) for row in right)
            + 2 * len(left & right)
        )
        scores = [face_terms(exact_loads, left, right, candidate)
                  for candidate in exact_candidates]
        minimum = min(scores)
        assert constant + 2 * minimum >= 0
        exact_dead_faces += 1
        for first, second in itertools.combinations(exact_candidates, 2):
            assert direct_delta(
                exact_loads, (left, right), (first, second)
            ) >= 0
            exact_exchange_pairs += 1

    print(json.dumps({
        "status": "PASS",
        "scalar_square_identity_cases": scalar_cases,
        "synthetic_rows": row_count,
        "synthetic_selected_columns": len(selected),
        "synthetic_candidate_columns": len(candidates),
        "outgoing_faces": len(tuple(itertools.combinations(selected, 2))),
        "dead_faces_by_minimum_cut": dead_faces,
        "live_faces": live_faces,
        "two_exchange_pairs_checked": exchanges_checked,
        "negative_exchanges": negative_exchanges,
        "negative_endpoints_passing_strict_threshold": retained_negative_endpoints,
        "subset_bucket_queries_checked": subset_queries,
        "exact_cover_dead_faces": exact_dead_faces,
        "exact_cover_exchange_pairs_checked": exact_exchange_pairs,
        "all_direct_scores_equal_formula": True,
        "all_dead_face_cuts_sound": True,
        "all_negative_endpoints_retained": True,
        "all_subset_queries_equal_direct_minima": True,
        "scope": "formula/pruning/query audit only; no q4 owner search",
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
