#!/usr/bin/env python3
"""Modular rank certificate for complete-r=4 compensated q=2 freedom."""

from itertools import combinations, permutations
from math import factorial, isqrt

import numpy as np


B = 9
R = 4
MODULUS = 1_000_003
ORBIT_COLUMNS = 900
LEHMER_STEP = 7_919

assert all(MODULUS % divisor
           for divisor in range(2, isqrt(MODULUS) + 1))
assert (MODULUS - 1) ** 2 < np.iinfo(np.int64).max

OMEGA = tuple(range(B))
MIDDLE = tuple(combinations(OMEGA, R))
LOWER = tuple(combinations(OMEGA, R - 1))
PAIRS = tuple(combinations(OMEGA, 2))
TARGETS = MIDDLE + LOWER
TARGET_ID = {target: i for i, target in enumerate(TARGETS)}
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


def lehmer_unrank(index):
    pool = list(OMEGA)
    word = []
    for size in range(B, 0, -1):
        block = factorial(size - 1)
        quotient, index = divmod(index, block)
        word.append(pool.pop(quotient))
    return tuple(word)


def rank_mod(matrix):
    matrix = np.asarray(matrix, dtype=np.int64).copy() % MODULUS
    rows, columns = matrix.shape
    pivot_row = 0
    for column in range(columns):
        candidates = np.flatnonzero(matrix[pivot_row:, column])
        if not len(candidates):
            continue
        row = pivot_row + int(candidates[0])
        matrix[[pivot_row, row]] = matrix[[row, pivot_row]]
        inverse = pow(int(matrix[pivot_row, column]), MODULUS - 2, MODULUS)
        matrix[pivot_row] = matrix[pivot_row] * inverse % MODULUS
        for other in np.flatnonzero(matrix[:, column]):
            if other != pivot_row:
                matrix[other] = (
                    matrix[other]
                    - matrix[other, column] * matrix[pivot_row]
                ) % MODULUS
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


BASE_WORD = OMEGA
BASE_IDS, BASE_MASK = punctured_configuration(BASE_WORD)

# One column of the unnormalised rooted duplicate-exposure matrix.
BASE_EXPOSURE = np.zeros(len(TARGETS), dtype=np.int64)
catalogue_masks = set()
for word in permutations(OMEGA):
    ids, mask = punctured_configuration(word)
    assert mask not in catalogue_masks
    catalogue_masks.add(mask)
    duplicate = max(0, (mask & BASE_MASK).bit_count() - 1)
    if duplicate:
        for target_id in ids:
            BASE_EXPOSURE[target_id] += duplicate
assert len(catalogue_masks) == factorial(B)

BASE_INCIDENCE = np.zeros(len(TARGETS), dtype=np.int64)
BASE_INCIDENCE[list(BASE_IDS)] = 1
BASE_Q2 = np.zeros(len(PAIRS), dtype=np.int64)
for start in range(B):
    BASE_Q2[PAIR_ID[interval(BASE_WORD, start, 2)]] = 1

central = np.empty((2 * len(TARGETS), ORBIT_COLUMNS), dtype=np.int64)
shallow = np.empty((len(PAIRS), ORBIT_COLUMNS), dtype=np.int64)

used_relabellings = set()
for column in range(ORBIT_COLUMNS):
    permutation_index = LEHMER_STEP * column % factorial(B)
    relabelling = lehmer_unrank(permutation_index)
    assert relabelling not in used_relabellings
    used_relabellings.add(relabelling)

    incidence = np.zeros(len(TARGETS), dtype=np.int64)
    exposure = np.zeros(len(TARGETS), dtype=np.int64)
    q2 = np.zeros(len(PAIRS), dtype=np.int64)

    for source_id, target in enumerate(TARGETS):
        image = tuple(sorted(relabelling[x] for x in target))
        image_id = TARGET_ID[image]
        incidence[image_id] = BASE_INCIDENCE[source_id]
        exposure[image_id] = BASE_EXPOSURE[source_id] % MODULUS

    for source_id, pair in enumerate(PAIRS):
        image = tuple(sorted(relabelling[x] for x in pair))
        q2[PAIR_ID[image]] = BASE_Q2[source_id]

    central[:, column] = np.concatenate((incidence, exposure)) % MODULUS
    shallow[:, column] = q2

# Replay the three B-row relations and the Hamilton-cycle degree relations
# used for the rational upper bounds.
incidence_block = central[:len(TARGETS)]
exposure_block = central[len(TARGETS):]
middle_count = len(MIDDLE)
assert np.all(incidence_block[:middle_count].sum(axis=0) == 8)
assert np.all(incidence_block[middle_count:].sum(axis=0) == 8)
assert np.all(
    exposure_block[:middle_count].sum(axis=0)
    == exposure_block[middle_count:].sum(axis=0)
)
d_zero = int(BASE_EXPOSURE[:middle_count].sum()) // 8
assert d_zero > 0
assert np.all(
    exposure_block[:middle_count].sum(axis=0) % MODULUS
    == (d_zero * incidence_block[:middle_count].sum(axis=0)) % MODULUS
)
vertex_pair = np.zeros((B, len(PAIRS)), dtype=np.int64)
for pair_id, pair in enumerate(PAIRS):
    for vertex in pair:
        vertex_pair[vertex, pair_id] = 1
assert rank_mod(vertex_pair) == B
assert np.all(vertex_pair @ shallow == 2)

rank_central = rank_mod(central)
rank_shallow = rank_mod(shallow)
rank_stacked = rank_mod(np.vstack((central, shallow)))

assert rank_central == 417
assert rank_shallow == 28
assert rank_stacked == 444

print(
    "PASS complete r=4 compensated q=2 rank certificate: "
    "rank(B)=417, rank(Q)=28, rank([B;Q])=444, quotient=27"
)
