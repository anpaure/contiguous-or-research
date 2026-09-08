#!/usr/bin/env python3
"""Finite audit for antipodal block-shuffle row rigidity."""

from itertools import combinations, permutations


def mask_of(items):
    mask = 0
    for item in items:
        mask |= 1 << item
    return mask


def primitive(mask, n):
    height = 0
    for position in range(n):
        height += 1 if mask & (1 << position) else -1
        if position < n - 1 and height <= 0:
            return False
    return height == 0


def heights(mask, n):
    answer = [0]
    for position in range(n):
        answer.append(
            answer[-1] + (1 if mask & (1 << position) else -1)
        )
    return answer


def deletion_formula(base_mask, y, n):
    base_heights = heights(base_mask, n)
    return (
        all(base_heights[length] > 0 for length in range(1, y + 1))
        and all(base_heights[length] > 2 for length in range(y + 1, n))
    )


def last_low(base_mask, n):
    base_heights = heights(base_mask, n)
    if min(base_heights[1:-1]) <= 0:
        return None
    return max(length for length in range(1, n) if base_heights[length] <= 2)


def audit_deletion_decks():
    for b in range(3, 8):
        n = 2 * b
        interior = range(1, n - 1)
        for chosen in combinations(interior, b):
            base_mask = mask_of((0, *chosen))
            assert base_mask.bit_count() == b + 1
            lam = last_low(base_mask, n)
            valid = []
            for y in (0, *chosen):
                actual = primitive(base_mask ^ (1 << y), n)
                formula = deletion_formula(base_mask, y, n)
                assert actual == formula
                if lam is None:
                    assert not actual
                else:
                    assert actual == (y >= lam)
                if actual:
                    valid.append(y)
            if lam is not None:
                base_heights = heights(base_mask, n)
                assert base_heights[lam] == 2
                assert len(valid) == (n - lam) // 2
    print("PASS: exact deletion/last-low deck formula for 3<=b<=7")


def signed_permutations(b):
    n = 2 * b
    for alpha in permutations(range(b)):
        for orientation in range(1 << b):
            pi = [0] * n
            for residue in range(b):
                pi[residue] = alpha[residue] + (
                    b if (orientation >> residue) & 1 else 0
                )
                pi[residue + b] = (pi[residue] + b) % n
            yield tuple(pi), alpha, orientation


def corrected_word(alpha, orientation):
    return tuple(
        (alpha[x] + ((orientation >> x) & 1) + x) % 2
        for x in range(len(alpha))
    )


def rotated_base_mask(pi, b, r):
    n = 2 * b
    p = pi[r]
    base_coordinates = {pi[(r + offset) % n] for offset in range(b + 1)}
    return mask_of((coordinate - p) % n for coordinate in base_coordinates)


def audit_good_rows():
    for b in (3, 5):
        n = 2 * b
        for pi, alpha, orientation in signed_permutations(b):
            c_word = corrected_word(alpha, orientation)
            for r in range(b):
                good = (
                    alpha[r] == (alpha[r - 1] + 1) % b
                    and c_word[r] == c_word[r - 1]
                )
                if not good:
                    continue
                assert pi[r] == (pi[r - 1] + 1) % n
                base_mask = rotated_base_mask(pi, b, r)
                assert base_mask.bit_count() == b + 1
                assert base_mask & 1
                assert not (base_mask & (1 << (n - 1)))
                lam = last_low(base_mask, n)
                for t in range(1, b):
                    p = pi[r]
                    deleted_offset = (pi[(r + t) % n] - p) % n
                    actual = primitive(base_mask ^ (1 << deleted_offset), n)
                    if lam is None:
                        assert not actual
                    else:
                        assert actual == (deleted_offset >= lam)
    print("PASS: good-row predecessor/deletion identity for full b=3,5 wreaths")


if __name__ == "__main__":
    audit_deletion_decks()
    audit_good_rows()
