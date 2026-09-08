#!/usr/bin/env python3
"""Finite audit for local deck entropy and its common-core obstruction."""

from itertools import combinations, permutations
from math import factorial


def mask_of(items):
    mask = 0
    for item in items:
        mask |= 1 << item
    return mask


def factor_member(flag, b):
    lower, middle, upper = flag
    n = 2 * b
    p = (middle ^ lower).bit_length() - 1
    q = (upper ^ middle).bit_length() - 1
    height = 0
    heights = []
    first_return = None
    for offset in range(n):
        coordinate = (p + offset) % n
        height += 1 if middle & (1 << coordinate) else -1
        heights.append(height)
        if height == 0 and first_return is None:
            first_return = offset + 1
    dyck = min(heights) >= 0 and height == 0
    ordinary = (
        q < p
        and (p, q) != (n - 1, 0)
        and dyck
        and first_return == (q - p) % n + 1
    )
    switched = (
        (p, q) == (0, n - 1)
        and height == 0
        and all(value > 0 for value in heights[:-1])
    )
    return ordinary or switched


def x_set(b, j):
    return {b - 1 - 4 * step for step in range(j)}


def tau_x(b, j, coordinate):
    return (
        (coordinate + b) % (2 * b)
        if coordinate % b in x_set(b, j)
        else coordinate
    )


def parity_permutations(interval):
    evens = tuple(value for value in interval if value % 2 == 0)
    odds = tuple(value for value in interval if value % 2 == 1)
    for even_image in permutations(evens):
        for odd_image in permutations(odds):
            mapping = dict(zip(evens, even_image))
            mapping.update(zip(odds, odd_image))
            yield mapping


def alpha_lift(mapping, b, coordinate):
    residue = coordinate % b
    image = mapping.get(residue, residue)
    return image + (b if coordinate >= b else 0)


def composed(b, j, mapping, coordinate):
    return alpha_lift(mapping, b, tau_x(b, j, coordinate))


def row_deck(b, j, mapping, r):
    n = 2 * b
    pi = lambda coordinate: composed(b, j, mapping, coordinate % n)
    full = {pi(r + offset) for offset in range(b + 1)}
    p = pi(r)
    q = pi(r - 1)
    answer = set()
    for t in range(1, b):
        middle = full - {pi(r + t)}
        middle_mask = mask_of(middle)
        answer.add(
            (
                middle_mask ^ (1 << p),
                middle_mask,
                middle_mask | (1 << q),
            )
        )
    assert len(answer) == b - 1
    return frozenset(answer)


def audit_commutation_and_safe_decks():
    for b in range(7, 20, 2):
        for j in range(1, (b - 1) // 4 + 1):
            forbidden = x_set(b, j)
            for a in range(b):
                for k in range(1, min(6, b - a) + 1):
                    interval = tuple(range(a, a + k))
                    if forbidden.intersection(interval):
                        continue
                    unsafe = set(interval) | {(a + k) % b}
                    base = {r: row_deck(b, j, {}, r) for r in range(b)}
                    for mapping in parity_permutations(interval):
                        for coordinate in range(2 * b):
                            left = alpha_lift(
                                mapping, b, tau_x(b, j, coordinate)
                            )
                            right = tau_x(
                                b,
                                j,
                                alpha_lift(mapping, b, coordinate),
                            )
                            assert left == right
                        for r in range(b):
                            if r not in unsafe:
                                assert row_deck(b, j, mapping, r) == base[r]
    print("PASS: commutation and exact safe-row deck identity")


def audit_overlap_and_core():
    for b in range(7, 18, 2):
        for j in range(1, (b - 1) // 4 + 1):
            forbidden = x_set(b, j)
            candidates = []
            for a in range(b):
                for k in range(1, min(6, b - a) + 1):
                    interval = tuple(range(a, a + k))
                    if not forbidden.intersection(interval):
                        candidates.append((a, interval))
            if not candidates:
                continue
            a, interval = max(candidates, key=lambda item: len(item[1]))
            unsafe = set(interval) | {(a + len(interval)) % b}
            base_rows = {r: row_deck(b, j, {}, r) for r in range(b)}
            base_factor = {
                flag
                for deck in base_rows.values()
                for flag in deck
                if factor_member(flag, b)
            }
            core = {
                flag
                for r, deck in base_rows.items()
                if r not in unsafe
                for flag in deck
                if factor_member(flag, b)
            }
            mappings = tuple(parity_permutations(interval))
            assert len(mappings) == factorial((len(interval) + 1) // 2) * factorial(
                len(interval) // 2
            )
            intersections = []
            for mapping in mappings:
                flags = {
                    flag
                    for r in range(b)
                    for flag in row_deck(b, j, mapping, r)
                    if factor_member(flag, b)
                }
                assert len(flags) >= len(base_factor) - len(unsafe) * (b - 1)
                assert core <= flags
                intersections.append(flags)
            if intersections:
                assert core <= set.intersection(*map(set, intersections))
    print("PASS: phase overlap bound, factorial count, and common factor core")


if __name__ == "__main__":
    audit_commutation_and_safe_decks()
    audit_overlap_and_core()
