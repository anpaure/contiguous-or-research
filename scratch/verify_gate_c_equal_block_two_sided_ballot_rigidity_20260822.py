#!/usr/bin/env python3
"""Finite audit for equal-block two-sided-ballot row rigidity."""

from itertools import permutations


def residue_permutation(order, block_length):
    return tuple(
        value_block * block_length + offset
        for value_block in order
        for offset in range(block_length)
    )


def signed_lift(order, block_length):
    alpha = residue_permutation(order, block_length)
    b = len(alpha)
    pi = [0] * (2 * b)
    for x in range(b):
        epsilon = (alpha[x] + x) % 2
        pi[x] = alpha[x] + b * epsilon
        pi[x + b] = (pi[x] + b) % (2 * b)
    return tuple(pi)


def block_word(order, block_index):
    block_count = len(order)
    inverse = [0] * block_count
    for position, value in enumerate(order):
        inverse[value] = position
    answer = []
    for value_distance in range(1, block_count):
        position_distance = (
            inverse[(order[block_index] + value_distance) % block_count]
            - block_index
        ) % block_count
        answer.append(1 if position_distance % 2 == value_distance % 2 else -1)
    return tuple(answer)


def predicted_row_word(order, block_length, block_index, offset):
    word = block_word(order, block_index)
    answer = [1] * (block_length - offset)
    for sign in word:
        answer.extend([sign] * block_length)
    answer.extend([1] * (offset + 1))
    answer.extend([-1] * (block_length - offset - 1))
    for sign in word:
        answer.extend([-sign] * block_length)
    answer.extend([-1] * offset)
    return tuple(answer)


def direct_row_word(order, block_length, block_index, offset):
    pi = signed_lift(order, block_length)
    b = len(pi) // 2
    n = 2 * b
    r = block_index * block_length + offset
    p = pi[r]
    selected = {pi[(r + step) % n] for step in range(b + 1)}
    return tuple(
        1 if (p + coordinate_offset) % n in selected else -1
        for coordinate_offset in range(n)
    )


def prefix_heights(word):
    answer = []
    height = 0
    for sign in word:
        height += sign
        answer.append(height)
    return tuple(answer)


def two_sided_ballot(word):
    height = 0
    prefixes = []
    for sign in word:
        height += sign
        prefixes.append(height)
    return min(prefixes) >= 0 and max(prefixes) <= prefixes[-1]


def exact_row_overlap(order, block_length, block_index, offset):
    pi = signed_lift(order, block_length)
    b = len(pi) // 2
    n = 2 * b
    r = block_index * block_length + offset
    p = pi[r]
    base = {pi[(r + step) % n] for step in range(b + 1)}
    overlap = 0
    for column in range(1, b):
        deleted = pi[(r + column) % n]
        height = 0
        primitive = True
        for coordinate_offset in range(n):
            coordinate = (p + coordinate_offset) % n
            height += 1 if coordinate in base and coordinate != deleted else -1
            if coordinate_offset < n - 1 and height <= 0:
                primitive = False
        overlap += primitive and height == 0
    return overlap


def audit_exact_words_and_trichotomy():
    for block_count, block_length in ((3, 3), (3, 5), (5, 3), (5, 5), (7, 3)):
        b = block_count * block_length
        for order in permutations(range(block_count)):
            for block_index in range(block_count):
                word = block_word(order, block_index)
                prefixes = prefix_heights(word)
                terminal = prefixes[-1]
                ballot = two_sided_ballot(word)
                for offset in range(1, block_length):
                    predicted = predicted_row_word(
                        order, block_length, block_index, offset
                    )
                    direct = direct_row_word(order, block_length, block_index, offset)
                    assert predicted == direct
                    heights = prefix_heights(direct)
                    if ballot:
                        assert min(heights[:-1]) > 0
                    if min(prefixes) < 0:
                        assert min(heights[:-1]) <= 0
                        assert exact_row_overlap(
                            order, block_length, block_index, offset
                        ) == 0
                    if max(prefixes) > terminal and offset <= block_length - 2:
                        assert min(heights[:-1]) <= 0
                        assert exact_row_overlap(
                            order, block_length, block_index, offset
                        ) == 0
                assert len(predicted) == 2 * b
    print("PASS: exact row word and positivity trichotomy")


def audit_bad_cut_loss():
    for block_count, block_length in ((3, 3), (3, 5), (5, 3), (5, 5), (7, 3)):
        b = block_count * block_length
        for order in permutations(range(block_count)):
            bad = sum(
                not two_sided_ballot(block_word(order, block_index))
                for block_index in range(block_count)
            )
            interior_deficit = 0
            retained_from_ballot_core = 0
            for block_index in range(block_count):
                ballot = two_sided_ballot(block_word(order, block_index))
                for offset in range(1, block_length):
                    overlap = exact_row_overlap(
                        order, block_length, block_index, offset
                    )
                    interior_deficit += (b - 1) - overlap
                    if ballot and offset <= block_length - 3:
                        assert overlap == b - 2
                        retained_from_ballot_core += overlap
            assert interior_deficit >= bad * (block_length - 2) * (b - 1)
            assert retained_from_ballot_core == (
                (block_count - bad) * (block_length - 3) * (b - 2)
            )
    print("PASS: exact deletion decks imply the bad-cut loss bound")


if __name__ == "__main__":
    audit_exact_words_and_trichotomy()
    audit_bad_cut_loss()
