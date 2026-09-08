#!/usr/bin/env python3
"""Verify the complete PPS/PSS/SSS depth-three oracle (H100 only)."""

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
    for config in outgoing:
        for row in config:
            changed[row] -= 1
    for config in incoming:
        for row in config:
            changed[row] += 1
    return energy(changed) - energy(loads)


def face_data(loads, outgoing, candidates):
    constant = sum(
        sum(remove_cost(loads[row]) for row in config)
        for config in outgoing
    ) + 2 * sum(
        len(left & right) for left, right in itertools.combinations(outgoing, 2)
    )
    scores = {
        config: (
            sum(add_cost(loads[row]) for row in config)
            - 2 * sum(len(config & old) for old in outgoing)
        )
        for config in candidates
    }
    return constant, scores


def formula_delta(constant, scores, incoming):
    return (
        constant + sum(scores[config] for config in incoming)
        + 2 * sum(
            len(left & right)
            for left, right in itertools.combinations(incoming, 2)
        )
    )


def ordered(configs):
    return tuple(sorted(configs, key=lambda config: tuple(sorted(config))))


def replay_pps(loads, selected_pairs, selected_self, pair_bank, self_menus):
    metrics = {
        "faces": 0, "dead_faces": 0, "direct_formula_checks": 0,
        "negative_triples": 0, "tested_leaves": 0,
    }
    for old_left, old_right in itertools.combinations(selected_pairs, 2):
        for group, old_self in selected_self.items():
            metrics["faces"] += 1
            outgoing = (old_left, old_right, old_self)
            self_menu = self_menus[group]
            candidates = pair_bank + self_menu
            constant, scores = face_data(loads, outgoing, candidates)
            pair_order = sorted(
                pair_bank, key=lambda config: (scores[config], tuple(sorted(config)))
            )
            b1, b2 = scores[pair_order[0]], scores[pair_order[1]]
            self_minimum = min(scores[config] for config in self_menu)
            dead = constant + b1 + b2 + self_minimum >= 0
            metrics["dead_faces"] += dead

            literal = set()
            for left, right in itertools.combinations(pair_bank, 2):
                for replacement in self_menu:
                    incoming = (left, right, replacement)
                    direct = direct_delta(loads, outgoing, incoming)
                    assert direct == formula_delta(constant, scores, incoming)
                    metrics["direct_formula_checks"] += 1
                    if direct < 0:
                        literal.add(incoming)
            metrics["negative_triples"] += len(literal)
            if dead:
                assert not literal
                continue

            retained_pairs = ordered(
                config for config in pair_bank
                if constant + scores[config]
                + scores[pair_order[1] if config == pair_order[0] else pair_order[0]]
                + self_minimum < 0
            )
            retained_self = ordered(
                config for config in self_menu
                if constant + scores[config] + b1 + b2 < 0
            )
            found = set()
            for left, right in itertools.combinations(retained_pairs, 2):
                prefix = scores[left] + scores[right] + 2 * len(left & right)
                if constant + prefix + self_minimum >= 0:
                    continue
                for replacement in retained_self:
                    if scores[replacement] >= -constant - prefix:
                        continue
                    metrics["tested_leaves"] += 1
                    incoming = (left, right, replacement)
                    if formula_delta(constant, scores, incoming) < 0:
                        found.add(incoming)
            assert found == literal
    return metrics


def replay_pss(loads, selected_pairs, selected_self, pair_bank, self_menus):
    metrics = {
        "faces": 0, "dead_faces": 0, "direct_formula_checks": 0,
        "negative_triples": 0, "tested_leaves": 0,
    }
    groups = sorted(selected_self)
    for old_pair in selected_pairs:
        for left_group, right_group in itertools.combinations(groups, 2):
            metrics["faces"] += 1
            outgoing = (
                old_pair, selected_self[left_group], selected_self[right_group]
            )
            left_menu = self_menus[left_group]
            right_menu = self_menus[right_group]
            candidates = pair_bank + left_menu + right_menu
            constant, scores = face_data(loads, outgoing, candidates)
            pair_minimum = min(scores[config] for config in pair_bank)
            left_minimum = min(scores[config] for config in left_menu)
            right_minimum = min(scores[config] for config in right_menu)
            dead = constant + pair_minimum + left_minimum + right_minimum >= 0
            metrics["dead_faces"] += dead

            literal = set()
            for pair in pair_bank:
                for left in left_menu:
                    for right in right_menu:
                        incoming = (pair, left, right)
                        direct = direct_delta(loads, outgoing, incoming)
                        assert direct == formula_delta(constant, scores, incoming)
                        metrics["direct_formula_checks"] += 1
                        if direct < 0:
                            literal.add(incoming)
            metrics["negative_triples"] += len(literal)
            if dead:
                assert not literal
                continue

            retained_pairs = ordered(
                config for config in pair_bank
                if constant + scores[config] + left_minimum + right_minimum < 0
            )
            retained_left = ordered(
                config for config in left_menu
                if constant + scores[config] + pair_minimum + right_minimum < 0
            )
            retained_right = ordered(
                config for config in right_menu
                if constant + scores[config] + pair_minimum + left_minimum < 0
            )
            found = set()
            for left in retained_left:
                for right in retained_right:
                    prefix = scores[left] + scores[right] + 2 * len(left & right)
                    if constant + prefix + pair_minimum >= 0:
                        continue
                    for pair in retained_pairs:
                        if scores[pair] >= -constant - prefix:
                            continue
                        metrics["tested_leaves"] += 1
                        incoming = (pair, left, right)
                        if formula_delta(constant, scores, incoming) < 0:
                            found.add(incoming)
            assert found == literal
    return metrics


def replay_sss(loads, selected_self, self_menus):
    metrics = {
        "faces": 0, "dead_faces": 0, "direct_formula_checks": 0,
        "negative_triples": 0, "tested_leaves": 0,
    }
    groups = sorted(selected_self)
    for left_group, middle_group, right_group in itertools.combinations(groups, 3):
        metrics["faces"] += 1
        outgoing = (
            selected_self[left_group], selected_self[middle_group],
            selected_self[right_group],
        )
        left_menu = self_menus[left_group]
        middle_menu = self_menus[middle_group]
        right_menu = self_menus[right_group]
        candidates = left_menu + middle_menu + right_menu
        constant, scores = face_data(loads, outgoing, candidates)
        left_minimum = min(scores[config] for config in left_menu)
        middle_minimum = min(scores[config] for config in middle_menu)
        right_minimum = min(scores[config] for config in right_menu)
        dead = constant + left_minimum + middle_minimum + right_minimum >= 0
        metrics["dead_faces"] += dead

        literal = set()
        for left in left_menu:
            for middle in middle_menu:
                for right in right_menu:
                    incoming = (left, middle, right)
                    direct = direct_delta(loads, outgoing, incoming)
                    assert direct == formula_delta(constant, scores, incoming)
                    metrics["direct_formula_checks"] += 1
                    if direct < 0:
                        literal.add(incoming)
        metrics["negative_triples"] += len(literal)
        if dead:
            assert not literal
            continue

        retained_left = ordered(
            config for config in left_menu
            if constant + scores[config] + middle_minimum + right_minimum < 0
        )
        retained_middle = ordered(
            config for config in middle_menu
            if constant + scores[config] + left_minimum + right_minimum < 0
        )
        retained_right = ordered(
            config for config in right_menu
            if constant + scores[config] + left_minimum + middle_minimum < 0
        )
        found = set()
        for left in retained_left:
            for middle in retained_middle:
                prefix = (
                    scores[left] + scores[middle] + 2 * len(left & middle)
                )
                if constant + prefix + right_minimum >= 0:
                    continue
                for right in retained_right:
                    if scores[right] >= -constant - prefix:
                        continue
                    metrics["tested_leaves"] += 1
                    incoming = (left, middle, right)
                    if formula_delta(constant, scores, incoming) < 0:
                        found.add(incoming)
        assert found == literal
    return metrics


def unique_config(generator, used, row_count, size):
    while True:
        config = frozenset(generator.sample(range(row_count), size))
        if config not in used:
            used.add(config)
            return config


def random_suite(generator):
    row_count = 32
    used = set()
    selected_pairs = tuple(
        unique_config(generator, used, row_count, 10) for _ in range(5)
    )
    pair_bank = ordered(
        unique_config(generator, used, row_count, 10) for _ in range(10)
    )
    selected_self = {
        group: unique_config(generator, used, row_count, 4)
        for group in range(5)
    }
    self_menus = {
        group: tuple(
            unique_config(generator, used, row_count, 4) for _ in range(3)
        )
        for group in range(5)
    }
    loads = [0] * row_count
    for config in selected_pairs + tuple(selected_self.values()):
        for row in config:
            loads[row] += 1
    return loads, selected_pairs, selected_self, pair_bank, self_menus


def exact_cover_suite(generator):
    pair_count = group_count = 4
    row_count = pair_count * 10 + group_count * 4
    selected_pairs = tuple(
        frozenset(range(10 * block, 10 * (block + 1)))
        for block in range(pair_count)
    )
    selected_self = {
        group: frozenset(range(40 + 4 * group, 40 + 4 * (group + 1)))
        for group in range(group_count)
    }
    used = set(selected_pairs) | set(selected_self.values())
    pair_bank = ordered(
        unique_config(generator, used, row_count, 10) for _ in range(8)
    )
    self_menus = {
        group: tuple(
            unique_config(generator, used, row_count, 4) for _ in range(2)
        )
        for group in range(group_count)
    }
    return (
        [1] * row_count, selected_pairs, selected_self, pair_bank, self_menus
    )


def run_all(suite):
    loads, selected_pairs, selected_self, pair_bank, self_menus = suite
    return {
        "PPS": replay_pps(
            loads, selected_pairs, selected_self, pair_bank, self_menus
        ),
        "PSS": replay_pss(
            loads, selected_pairs, selected_self, pair_bank, self_menus
        ),
        "SSS": replay_sss(loads, selected_self, self_menus),
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
                    add_cost(load) - 2 * sum(outgoing_bits)
                )
            formula += 2 * sum(
                incoming_bits[i] * incoming_bits[j]
                for i, j in itertools.combinations(range(3), 2)
            )
            assert direct == formula
            scalar_cases += 1

    generator = random.Random(20260814)
    random_results = run_all(random_suite(generator))
    exact_results = run_all(exact_cover_suite(generator))
    for kind in ("PPS", "PSS", "SSS"):
        assert random_results[kind]["negative_triples"] > 0
        assert exact_results[kind]["negative_triples"] == 0
        assert exact_results[kind]["dead_faces"] > 0

    print(json.dumps({
        "status": "PASS",
        "scalar_square_identity_cases": scalar_cases,
        "random_suite": random_results,
        "exact_cover_suite": exact_results,
        "all_direct_scores_equal_formula": True,
        "all_layered_oracles_equal_literal_negative_sets": True,
        "scope": "synthetic typed-menu audit only; no q4 pool search",
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
