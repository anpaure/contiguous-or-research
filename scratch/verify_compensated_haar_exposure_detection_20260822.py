#!/usr/bin/env python3
"""Exact r=4 audit: rooted exposure detects the Haar q=2 current.

All arithmetic is integral.  The complete directed punctured catalogue has
9! configurations, so the exhaustive loop is small enough to be literal.
"""

from itertools import combinations, permutations
from math import factorial


B = 9
R = 4
OMEGA = tuple(range(B))
MIDDLE = tuple(combinations(OMEGA, R))
LOWER = tuple(combinations(OMEGA, R - 1))
PAIRS = tuple(combinations(OMEGA, 2))
MIDDLE_ID = {target: i for i, target in enumerate(MIDDLE)}
LOWER_ID = {target: len(MIDDLE) + i for i, target in enumerate(LOWER)}
PAIR_ID = {target: i for i, target in enumerate(PAIRS)}


def interval(word, start, length):
    return tuple(sorted(word[(start + j) % B] for j in range(length)))


def punctured_configuration(word):
    ids = [MIDDLE_ID[interval(word, start, R)] for start in range(1, B)]
    ids += [LOWER_ID[interval(word, start, R - 1)] for start in range(1, B)]
    mask = 0
    for target_id in ids:
        mask |= 1 << target_id
    assert len(ids) == 16 and mask.bit_count() == 16
    return tuple(ids), mask


NEGATIVE_Q = (
    (1, 8, 6, 7, 4, 5, 3, 9, 2),
    (1, 9, 8, 6, 7, 4, 5, 2, 3),
    (1, 5, 3, 9, 8, 6, 7, 2, 4),
    (1, 7, 3, 9, 4, 5, 8, 2, 6),
)
POSITIVE_Q = (
    (1, 9, 3, 5, 4, 7, 6, 8, 2),
    (1, 5, 4, 7, 6, 8, 9, 2, 3),
    (1, 7, 6, 8, 9, 3, 5, 2, 4),
    (1, 8, 5, 4, 9, 3, 7, 2, 6),
)


def physical_order(q):
    """Convert the theorem's step-two omitted-label order to consecutive order."""
    q0 = tuple(x - 1 for x in q)
    return tuple(q0[(2 * j) % B] for j in range(B))


NEGATIVE = tuple(map(physical_order, NEGATIVE_Q))
POSITIVE = tuple(map(physical_order, POSITIVE_Q))


def step_two_deck(q, length):
    q0 = tuple(x - 1 for x in q)
    return sorted(
        tuple(sorted(q0[(start + 2 * offset) % B]
                     for offset in range(length)))
        for start in range(B)
    )


# Audit the step-two/consecutive orientation conversion and the two central
# Haar ledgers before puncturing.
for q, word in zip(NEGATIVE_Q + POSITIVE_Q, NEGATIVE + POSITIVE):
    for length in (R, R - 1, R - 2):
        assert step_two_deck(q, length) == sorted(
            interval(word, start, length) for start in range(B)
        )
for length in (R, R - 1):
    negative_deck = sorted(
        target for word in NEGATIVE
        for target in (interval(word, start, length) for start in range(B))
    )
    positive_deck = sorted(
        target for word in POSITIVE
        for target in (interval(word, start, length) for start in range(B))
    )
    assert negative_deck == positive_deck


def build_signed_puncture_average():
    coefficient = {}
    for sign, rows in ((-1, NEGATIVE), (1, POSITIVE)):
        for word in rows:
            for shift in range(B):
                rotated = word[shift:] + word[:shift]
                _, mask = punctured_configuration(rotated)
                coefficient[mask] = coefficient.get(mask, 0) + sign
    return tuple((value, mask) for mask, value in coefficient.items() if value)


SIGNED = build_signed_puncture_average()
assert len(SIGNED) == 72
assert sum(value for value, _ in SIGNED) == 0


# Central incidence must cancel before the more expensive exposure audit.
incidence = [0] * (len(MIDDLE) + len(LOWER))
for value, mask in SIGNED:
    remaining = mask
    while remaining:
        bit = remaining & -remaining
        incidence[bit.bit_length() - 1] += value
        remaining -= bit
assert incidence == [0] * len(incidence)


# The unpunctured physical depth-two current J.
current = [0] * len(PAIRS)
for sign, rows in ((-1, NEGATIVE), (1, POSITIVE)):
    for word in rows:
        for start in range(B):
            current[PAIR_ID[interval(word, start, 2)]] += sign

expected = {
    (0, 2): -1,
    (1, 2): 1,
    (0, 3): 1,
    (1, 3): -1,
    (0, 4): 1,
    (1, 4): -1,
    (0, 8): -1,
    (1, 8): 1,
}
assert {PAIRS[i]: value for i, value in enumerate(current) if value} == expected


# Rooted duplicate-exposure numerator P~ delta.
exposure = [0] * len(incidence)
catalogue_masks = set()
for word in permutations(OMEGA):
    ids, mask = punctured_configuration(word)
    assert mask not in catalogue_masks
    catalogue_masks.add(mask)
    signed_duplicate = 0
    for value, signed_mask in SIGNED:
        overlap = (mask & signed_mask).bit_count()
        signed_duplicate += value * max(0, overlap - 1)
    if signed_duplicate:
        for target_id in ids:
            exposure[target_id] += signed_duplicate
assert len(catalogue_masks) == factorial(B)


down_middle = [0] * len(PAIRS)
down_lower = [0] * len(PAIRS)
for target_id, target in enumerate(MIDDLE):
    for pair in combinations(target, 2):
        down_middle[PAIR_ID[pair]] += exposure[target_id]
for local_id, target in enumerate(LOWER):
    target_id = len(MIDDLE) + local_id
    for pair in combinations(target, 2):
        down_lower[PAIR_ID[pair]] += exposure[target_id]

assert down_middle == [425 * value for value in current]
assert down_lower == [8832 * value for value in current]

print(
    "PASS compensated Haar exposure detection: "
    "catalogue=9!, signed-configurations=72, "
    "down_M=425 J, down_L=8832 J"
)
