#!/usr/bin/env python3
"""Finite audit for the one-giant unequal-block common-atlas theorem."""

from itertools import permutations

from verify_gate_c_unequal_odd_block_weighted_excursion_20260822 import (
    construction,
    direct_word,
    formula_data,
    primitive_after_delete,
)


def audit_instance(b, singleton_count):
    giant = b - singleton_count
    lengths = (giant,) + (1,) * singleton_count
    coordinate_maps = set()
    atlas = set()
    minimum_giant_flags = None

    for tail in permutations(range(1, singleton_count + 1)):
        order = (0,) + tail
        _, _, pi = construction(lengths, order)
        coordinate_maps.add(tuple(value % b for value in pi[:b]))
        giant_flags = 0
        for offset in range(1, giant):
            word, pi_here, row = direct_word(lengths, order, 0, offset)
            _, lower, upper = formula_data(lengths, order, 0, offset)
            origin = pi_here[row]
            selected = {pi_here[row + step] % (2 * b) for step in range(b + 1)}
            for shift in range(1, b):
                deleted = pi_here[row + shift] % (2 * b)
                step = (deleted - origin) % (2 * b)
                if primitive_after_delete(word, step):
                    giant_flags += 1
                    atlas.add(frozenset(selected - {deleted}))
            if upper + 1 <= offset <= giant - lower - 3:
                accepted = sum(
                    primitive_after_delete(
                        word, (pi_here[row + shift] - origin) % (2 * b)
                    )
                    for shift in range(1, b)
                )
                assert accepted == b - 2
        minimum_giant_flags = (giant_flags if minimum_giant_flags is None
                               else min(minimum_giant_flags, giant_flags))

    expected_floor = (b - 2) * max(0, b - 3 * singleton_count - 3)
    assert len(coordinate_maps) == __import__("math").factorial(singleton_count)
    assert minimum_giant_flags >= expected_floor
    assert len(atlas) <= b * b * 2 ** singleton_count
    if expected_floor:
        assert len(atlas) / expected_floor <= b * b * 2 ** singleton_count / expected_floor
    print(
        f"PASS: b={b} S={singleton_count} maps={len(coordinate_maps)} "
        f"atlas={len(atlas)} min_flags={minimum_giant_flags}"
    )


def audit():
    for b, singleton_count in ((7, 2), (9, 2), (9, 4), (11, 2), (11, 4)):
        audit_instance(b, singleton_count)


if __name__ == "__main__":
    audit()
