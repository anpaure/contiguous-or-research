#!/usr/bin/env python3
"""Verify the exact four-pair/general-k exclusion recurrence (H100 only)."""

from __future__ import annotations

import itertools
import json
import random


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


def face_data(loads, outgoing, candidates):
    constant = sum(
        sum(remove_cost(loads[row]) for row in column)
        for column in outgoing
    ) + 2 * sum(
        len(left & right) for left, right in itertools.combinations(outgoing, 2)
    )
    scores = {
        candidate: (
            sum(add_cost(loads[row]) for row in candidate)
            - 2 * sum(len(candidate & column) for column in outgoing)
        )
        for candidate in candidates
    }
    return constant, scores


def prefix_score(scores, prefix):
    return (
        sum(scores[column] for column in prefix)
        + 2 * sum(
            len(left & right)
            for left, right in itertools.combinations(prefix, 2)
        )
    )


def exclusion_sum(scores, excluded, count):
    values = sorted(
        (score, tuple(sorted(column)))
        for column, score in scores.items()
        if column not in excluded
    )
    assert len(values) >= count
    return sum(score for score, _ in values[:count])


def layered_negative_set(loads, outgoing, candidates, depth):
    constant, scores = face_data(loads, outgoing, candidates)
    found = set()
    prefixes_visited = [0] * (depth + 1)
    prefixes_pruned = [0] * depth

    def visit(prefix, start):
        size = len(prefix)
        prefixes_visited[size] += 1
        q_value = prefix_score(scores, prefix)
        if size == depth:
            if constant + q_value < 0:
                found.add(tuple(prefix))
            return
        minimum = exclusion_sum(scores, frozenset(prefix), depth - size)
        if constant + q_value + minimum >= 0:
            prefixes_pruned[size] += 1
            return
        for position in range(start, len(candidates)):
            visit(prefix + (candidates[position],), position + 1)

    visit(tuple(), 0)
    return found, prefixes_visited, prefixes_pruned


def replay_suite(loads, selected, candidates, depth):
    direct_negative = set()
    layered_negative = set()
    formula_checks = 0
    prefix_implication_checks = 0
    total_visited = [0] * (depth + 1)
    total_pruned = [0] * depth
    faces = 0

    for outgoing in itertools.combinations(selected, depth):
        faces += 1
        constant, scores = face_data(loads, outgoing, candidates)
        negatives_here = set()
        for incoming in itertools.combinations(candidates, depth):
            direct = direct_delta(loads, outgoing, incoming)
            formula = constant + prefix_score(scores, incoming)
            assert direct == formula
            formula_checks += 1
            if direct < 0:
                negatives_here.add(tuple(incoming))
                direct_negative.add((outgoing, tuple(incoming)))
                for size in range(depth):
                    for prefix in itertools.combinations(incoming, size):
                        lower = (
                            constant + prefix_score(scores, prefix)
                            + exclusion_sum(
                                scores, frozenset(prefix), depth - size
                            )
                        )
                        assert lower < 0
                        prefix_implication_checks += 1

        found, visited, pruned = layered_negative_set(
            loads, outgoing, candidates, depth
        )
        assert found == negatives_here
        layered_negative.update((outgoing, incoming) for incoming in found)
        total_visited = [a + b for a, b in zip(total_visited, visited)]
        total_pruned = [a + b for a, b in zip(total_pruned, pruned)]

    assert layered_negative == direct_negative
    return {
        "depth": depth,
        "outgoing_faces": faces,
        "direct_formula_checks": formula_checks,
        "negative_exchanges": len(direct_negative),
        "negative_prefix_implication_checks": prefix_implication_checks,
        "prefixes_visited_by_size": total_visited,
        "prefixes_pruned_by_size": total_pruned,
    }


def main():
    scalar_cases = 0
    for load in range(9):
        for bits in itertools.product((0, 1), repeat=8):
            outgoing_bits = bits[:4]
            incoming_bits = bits[4:]
            direct = (
                load - sum(outgoing_bits) + sum(incoming_bits) - 1
            ) ** 2 - (load - 1) ** 2
            constant = (
                sum(bit * remove_cost(load) for bit in outgoing_bits)
                + 2 * sum(
                    outgoing_bits[i] * outgoing_bits[j]
                    for i, j in itertools.combinations(range(4), 2)
                )
            )
            formula = constant
            for incoming in incoming_bits:
                formula += incoming * (
                    add_cost(load) - 2 * sum(outgoing_bits)
                )
            formula += 2 * sum(
                incoming_bits[i] * incoming_bits[j]
                for i, j in itertools.combinations(range(4), 2)
            )
            assert direct == formula
            scalar_cases += 1

    generator = random.Random(20260814)
    row_count = 26
    column_size = 8
    columns = set()
    while len(columns) < 22:
        columns.add(frozenset(generator.sample(range(row_count), column_size)))
    columns = sorted(columns, key=lambda column: tuple(sorted(column)))
    selected = columns[:6]
    candidates = columns[6:]
    loads = [0] * row_count
    for column in selected:
        for row in column:
            loads[row] += 1

    suites = [
        replay_suite(loads, selected, candidates, depth)
        for depth in range(1, 5)
    ]
    assert suites[-1]["negative_exchanges"] > 0
    assert suites[-1]["negative_prefix_implication_checks"] > 0
    assert sum(suites[-1]["prefixes_pruned_by_size"]) > 0

    exact_selected = [
        frozenset(range(column_size * block, column_size * (block + 1)))
        for block in range(6)
    ]
    exact_candidates = set()
    while len(exact_candidates) < 16:
        candidate = frozenset(generator.sample(range(48), column_size))
        if candidate not in exact_selected:
            exact_candidates.add(candidate)
    exact_candidates = sorted(
        exact_candidates, key=lambda column: tuple(sorted(column))
    )
    exact_suite = replay_suite(
        [1] * 48, exact_selected, exact_candidates, depth=4
    )
    assert exact_suite["negative_exchanges"] == 0
    assert exact_suite["prefixes_pruned_by_size"][0] == 15

    print(json.dumps({
        "status": "PASS",
        "scalar_four_exchange_identity_cases": scalar_cases,
        "general_depth_suites": suites,
        "exact_cover_depth_four_suite": exact_suite,
        "all_direct_scores_equal_formula": True,
        "all_negative_prefixes_pass_exclusion_cut": True,
        "layered_oracle_finds_exact_negative_set": True,
        "scope": "synthetic formula/pruning audit only; no q4 pool search",
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
