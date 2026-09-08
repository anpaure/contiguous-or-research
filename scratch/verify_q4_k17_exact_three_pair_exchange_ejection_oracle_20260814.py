#!/usr/bin/env python3
"""Verify the exact three-pair score and exclusion pruning (H100 only)."""

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
    scores = {}
    for candidate in candidates:
        scores[candidate] = (
            sum(add_cost(loads[row]) for row in candidate)
            - 2 * sum(len(candidate & column) for column in outgoing)
        )
    return constant, scores


def formula_delta(constant, scores, incoming):
    return (
        constant
        + sum(scores[column] for column in incoming)
        + 2 * sum(
            len(left & right)
            for left, right in itertools.combinations(incoming, 2)
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


def replay_suite(loads, selected, candidates):
    faces = negative = tested = 0
    dead_faces = live_faces = 0
    negative_found = set()
    negative_direct = set()
    formula_checks = 0
    candidate_prunes = pair_prunes = 0
    for outgoing in itertools.combinations(selected, 3):
        faces += 1
        constant, scores = face_data(loads, outgoing, candidates)
        minima3 = exclusion_sum(scores, frozenset(), 3)
        dead = constant + minima3 >= 0
        dead_faces += dead
        live_faces += not dead

        retained = {
            candidate for candidate in candidates
            if constant + scores[candidate]
            + exclusion_sum(scores, frozenset((candidate,)), 2) < 0
        }
        candidate_prunes += len(candidates) - len(retained)

        for incoming in itertools.combinations(candidates, 3):
            direct = direct_delta(loads, outgoing, incoming)
            formula = formula_delta(constant, scores, incoming)
            assert direct == formula
            formula_checks += 1
            key = (outgoing, incoming)
            if direct < 0:
                negative += 1
                negative_direct.add(key)
                assert not dead
                assert set(incoming) <= retained

        ordered_retained = sorted(
            retained, key=lambda column: tuple(sorted(column))
        )
        for first_position, first in enumerate(ordered_retained):
            for second_position in range(first_position + 1, len(ordered_retained)):
                second = ordered_retained[second_position]
                pair_score = (
                    scores[first] + scores[second] + 2 * len(first & second)
                )
                if constant + pair_score + exclusion_sum(
                    scores, frozenset((first, second)), 1
                ) >= 0:
                    pair_prunes += 1
                    continue
                for third in ordered_retained[second_position + 1:]:
                    if scores[third] >= -constant - pair_score:
                        continue
                    tested += 1
                    incoming = (first, second, third)
                    delta = (
                        constant + pair_score + scores[third]
                        + 2 * len(third & first)
                        + 2 * len(third & second)
                    )
                    assert delta == formula_delta(constant, scores, incoming)
                    if delta < 0:
                        negative_found.add((outgoing, incoming))

    assert negative_found == negative_direct
    return {
        "outgoing_faces": faces,
        "dead_faces": dead_faces,
        "live_faces": live_faces,
        "direct_formula_checks": formula_checks,
        "negative_triples": negative,
        "retained_triples_tested": tested,
        "candidate_prunes": candidate_prunes,
        "pair_prunes": pair_prunes,
    }


def main():
    scalar_cases = 0
    for load in range(7):
        for bits in itertools.product((0, 1), repeat=6):
            outgoing_bits = bits[:3]
            incoming_bits = bits[3:]
            direct = (
                load - sum(outgoing_bits) + sum(incoming_bits) - 1
            ) ** 2 - (load - 1) ** 2
            constant = (
                sum(bit * remove_cost(load) for bit in outgoing_bits)
                + 2 * sum(
                    outgoing_bits[i] * outgoing_bits[j]
                    for i, j in itertools.combinations(range(3), 2)
                )
            )
            formula = constant
            for incoming in incoming_bits:
                formula += incoming * (
                    add_cost(load)
                    - 2 * sum(outgoing_bits)
                )
            formula += 2 * sum(
                incoming_bits[i] * incoming_bits[j]
                for i, j in itertools.combinations(range(3), 2)
            )
            assert direct == formula
            scalar_cases += 1

    generator = random.Random(20260814)
    row_count = 28
    column_size = 10
    columns = set()
    while len(columns) < 34:
        columns.add(frozenset(generator.sample(range(row_count), column_size)))
    columns = sorted(columns, key=lambda column: tuple(sorted(column)))
    selected = columns[:6]
    candidates = columns[6:]
    loads = [0] * row_count
    for column in selected:
        for row in column:
            loads[row] += 1
    random_suite = replay_suite(loads, selected, candidates)
    assert random_suite["negative_triples"] > 0

    exact_selected = [
        frozenset(range(10 * block, 10 * (block + 1))) for block in range(6)
    ]
    exact_candidates = set()
    while len(exact_candidates) < 28:
        candidate = frozenset(generator.sample(range(60), column_size))
        if candidate not in exact_selected:
            exact_candidates.add(candidate)
    exact_candidates = sorted(
        exact_candidates, key=lambda column: tuple(sorted(column))
    )
    exact_suite = replay_suite([1] * 60, exact_selected, exact_candidates)
    assert exact_suite["dead_faces"] == 20
    assert exact_suite["negative_triples"] == 0

    print(json.dumps({
        "status": "PASS",
        "scalar_square_identity_cases": scalar_cases,
        "random_suite": random_suite,
        "exact_cover_suite": exact_suite,
        "all_direct_scores_equal_formula": True,
        "all_dead_face_cuts_sound": True,
        "all_negative_candidates_pass_exclusion_threshold": True,
        "all_negative_pairs_pass_exclusion_threshold": True,
        "retained_ejection_scan_finds_exact_negative_set": True,
        "scope": "synthetic formula/pruning audit only; no q4 pool search",
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
