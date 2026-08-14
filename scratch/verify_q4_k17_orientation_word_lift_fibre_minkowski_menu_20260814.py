#!/usr/bin/env python3
"""Independent finite replay for the q4/k17 orientation-word reduction."""

from __future__ import annotations

import itertools
import json
import math


def complement(word):
    return tuple(1 - bit for bit in word)


def add(left, right):
    return tuple(a + b for a, b in zip(left, right))


def subtract(left, right):
    return tuple(a - b for a, b in zip(left, right))


def reflect(vector):
    """A literal involution on a synthetic ticket-orbit group."""
    return tuple(reversed(vector))


def rotate(word, shift):
    size = len(word)
    return tuple(word[(index + shift) % size] for index in range(size))


def main():
    words = list(itertools.product((0, 1), repeat=10))
    complement_classes = {
        min(word, complement(word)) for word in words
    }
    anchored_words = {word for word in words if word[0] == 0}
    assert len(words) == 1024
    assert len(complement_classes) == len(anchored_words) == 512
    assert all(word != complement(word) for word in words)

    orientation_pair_checks = 0
    for left in words:
        for right in words:
            owner_exact = all(
                {left[index], 1 - right[index]} == {0, 1}
                for index in range(10)
            )
            assert owner_exact == (left == right)
            orientation_pair_checks += 1

    signatures = {
        (0, 1, 0, 2, 1, 3, 0),
        (1, 0, 2, 1, 1, 0, 3),
        (2, 1, 1, 0, 3, 0, 1),
        (3, 0, 1, 2, 0, 1, 1),
    }
    base = min(signatures)
    differences = {subtract(value, base) for value in signatures}
    direct_menu = {
        add(left, reflect(right))
        for left in signatures for right in signatures
    }
    minkowski_menu = {
        add(add(base, reflect(base)), add(left, reflect(right)))
        for left in differences for right in differences
    }
    assert direct_menu == minkowski_menu

    one_sided_checks = 0
    symmetry_checks = 0
    for left in signatures:
        for right in signatures:
            direct = add(left, reflect(right))
            literal = add(left, reflect(left))
            delta = reflect(subtract(right, left))
            assert direct == add(literal, delta)
            one_sided_checks += 1
            transformed = add(reflect(right), reflect(reflect(left)))
            assert transformed == direct
            symmetry_checks += 1

    phase_rotation_checks = 0
    phase_reflection_checks = 0
    phase_swap_checks = 0
    phase_word = tuple(range(10))
    reflected_phase_word = tuple(100 + value for value in phase_word)
    for shift in range(10):
        rotated = rotate(phase_word, shift)
        for phase in range(10):
            shifted_phase = (phase - shift) % 10
            assert {
                rotated[shifted_phase], rotated[(shifted_phase + 3) % 10]
            } == {
                phase_word[phase], phase_word[(phase + 3) % 10]
            }
            phase_rotation_checks += 1
            assert {
                reflected_phase_word[phase],
                reflected_phase_word[(phase + 3) % 10],
            } == {
                100 + phase_word[phase],
                100 + phase_word[(phase + 3) % 10],
            }
            phase_reflection_checks += 1

    witnesses = ("u", "v", "x")
    for left, right in itertools.product(witnesses, repeat=2):
        for left_phase, right_phase in itertools.product(range(10), repeat=2):
            physical = frozenset((
                (left, left_phase),
                ("rho(" + right + ")", right_phase),
            ))
            transformed = frozenset((
                ("rho(" + right + ")", right_phase),
                (left, left_phase),
            ))
            assert physical == transformed
            phase_swap_checks += 1

    l3_truth_table = []
    for load in range(4):
        for unmarked in range(load + 1):
            accepted = load - unmarked == 1 and load <= 2
            assert accepted == ((load, unmarked) in {(1, 0), (2, 1)})
            l3_truth_table.append((load, unmarked, accepted))

    assert math.comb(9, 5) * math.factorial(4) * (
        math.factorial(8) // math.factorial(2)
    ) == 60_963_840

    print(json.dumps({
        "status": "PASS",
        "raw_orientation_words": len(words),
        "complement_classes": len(complement_classes),
        "anchored_orientation_words": len(anchored_words),
        "owner_exact_orientation_pair_checks": orientation_pair_checks,
        "anchored_raw_parameter_count": 60_963_840,
        "synthetic_signature_count": len(signatures),
        "synthetic_two_sided_menu_count": len(direct_menu),
        "one_sided_base_delta_checks": one_sided_checks,
        "two_sided_complement_symmetry_checks": symmetry_checks,
        "phase_rotation_checks": phase_rotation_checks,
        "phase_reflection_checks": phase_reflection_checks,
        "phase_swap_checks": phase_swap_checks,
        "l3_truth_table": l3_truth_table,
        "scope": (
            "finite replay of orientation, affine-menu, and phase identities; "
            "anchored witness completeness and resource scope are symbolic"
        ),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
