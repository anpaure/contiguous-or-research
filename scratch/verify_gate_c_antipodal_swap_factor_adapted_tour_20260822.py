#!/usr/bin/env python3
"""Finite audit for exact factor-adapted antipodal-swap tours."""


def mask_of(items):
    mask = 0
    for item in items:
        mask |= 1 << item
    return mask


def is_dyck(mask, n):
    height = 0
    first_return = None
    for position in range(n):
        height += 1 if mask & (1 << position) else -1
        if height < 0:
            return False, None
        if height == 0 and first_return is None:
            first_return = position + 1
    return height == 0, first_return


def is_primitive_dyck(mask, n):
    dyck, first_return = is_dyck(mask, n)
    return dyck and first_return == n


def factor_criterion(flag, b):
    lower, middle, upper = flag
    n = 2 * b
    p = (middle ^ lower).bit_length() - 1
    q = (upper ^ middle).bit_length() - 1
    rotated = 0
    for offset in range(n):
        if middle & (1 << ((p + offset) % n)):
            rotated |= 1 << offset
    dyck, first_return = is_dyck(rotated, n)
    original = (
        q < p
        and (p, q) != (n - 1, 0)
        and dyck
        and first_return == n - p + q + 1
    )
    switched = (p, q) == (0, n - 1) and is_primitive_dyck(middle, n)
    return original or switched


def residue_set(b, j):
    return {b - 1 - 4 * step for step in range(j)}


def coordinate_permutation(b, j, coordinate):
    if coordinate % b in residue_set(b, j):
        return (coordinate + b) % (2 * b)
    return coordinate


def constructed_cycle(b, j):
    n = 2 * b
    cycle = [(-index) % n for index in range(n)]
    for step in range(j):
        position = 4 * step + 1
        cycle[position], cycle[position + b] = (
            cycle[position + b],
            cycle[position],
        )
    return tuple(cycle)


def template_flag(cycle, b, phase, stage, t):
    n = 2 * b
    offset = (phase + stage * (b + 1)) % n
    indices = [
        (offset + value) % n
        for value in (*range(t, b), *range(b + 1, b + t + 1))
    ]
    middle = mask_of(cycle[index] for index in indices)
    r_index = (offset + b + t) % n
    p = cycle[r_index]
    q = cycle[(r_index + 1) % n]
    return middle ^ (1 << p), middle, middle | (1 << q)


def canonical_swapped_flag(b, j, r, t):
    n = 2 * b
    middle = mask_of(
        coordinate_permutation(b, j, (r + offset) % n)
        for offset in range(b + 1)
        if offset != t
    )
    p = coordinate_permutation(b, j, r)
    q = coordinate_permutation(b, j, (r - 1) % n)
    return middle ^ (1 << p), middle, middle | (1 << q)


def audit_canonical_conversion():
    for b in range(5, 20, 2):
        for j in range(1, (b - 1) // 4 + 1):
            cycle = constructed_cycle(b, j)
            for phase in (0, 1):
                for stage in range(b):
                    offset = (phase + stage * (b + 1)) % (2 * b)
                    for t in range(1, b):
                        r = (-offset - b - t) % (2 * b)
                        assert template_flag(cycle, b, phase, stage, t) == (
                            canonical_swapped_flag(b, j, r, t)
                        )
    print("PASS: coherent templates equal swapped canonical intervals")


def direct_primitive_word(b, d_values, t):
    effective = set(d_values) - {t}
    height = 0
    for position in range(2 * b):
        is_one = position <= b and position != t
        if position in effective or position - b in effective:
            is_one = not is_one
        height += 1 if is_one else -1
        if position < 2 * b - 1 and height <= 0:
            return False
    return height == 0


def toggle_criterion(b, d_values, t):
    effective = sorted(set(d_values) - {t})
    before_t = sum(value < t for value in effective)
    if t < 2 * before_t + 2:
        return False
    size = len(effective)
    for index, value in enumerate(effective, start=1):
        if value < t and value < 2 * index:
            return False
        if value > t and value < 2 * index + 2:
            return False
        if value > b - 2 * (size - index + 1) - 1:
            return False
    return True


def audit_toggle_criterion():
    from itertools import combinations

    for b in range(3, 16, 2):
        for size in range(0, min(5, b - 1) + 1):
            for d_values in combinations(range(1, b), size):
                for t in range(1, b):
                    assert direct_primitive_word(b, d_values, t) == (
                        toggle_criterion(b, d_values, t)
                    )
    print("PASS: exhaustive primitive-toggle criterion for odd 3<=b<=15")


def admissible_from_table(b, j, r):
    x_values = residue_set(b, j)
    if r in x_values or (r - 1) % b in x_values or (r + 1) % b in x_values:
        return set()
    if (r - 2) % b in x_values:
        return {b - 2}

    if 4 * j == b - 1:
        assert r == 2
        return set(range(2, b)) - {3}

    c = b - 4 * j
    if 2 <= r <= c - 1:
        return set(range(2, b))
    if r == c:
        return set(range(3, b))
    if r == c + 1:
        return set(range(2, b)) - {3}
    raise AssertionError((b, j, r))


def height_admissible(b, j, r, t):
    x_values = residue_set(b, j)
    if r in x_values or (r - 1) % b in x_values:
        return False
    d_values = {(x_value - r) % b for x_value in x_values}
    assert 0 not in d_values and b - 1 not in d_values
    return toggle_criterion(b, d_values, t)


def expected_overlap(b, j):
    if 4 * j == b - 1:
        return b + j - 3
    return b * b - (4 * j + 2) * b + 9 * j - 2


def audit_case_table_and_formula():
    for b in range(5, 102, 2):
        for j in range(1, (b - 1) // 4 + 1):
            overlap = 0
            for r in range(b):
                actual = {
                    t for t in range(1, b) if height_admissible(b, j, r, t)
                }
                expected = admissible_from_table(b, j, r)
                assert actual == expected, (b, j, r, actual, expected)
                overlap += len(actual)
            assert overlap == expected_overlap(b, j)
    print("PASS: exact residue table and overlap formulas for odd 5<=b<=101")


def audit_full_factor_test():
    for b in range(5, 52, 2):
        for j in range(1, (b - 1) // 4 + 1):
            cycle = constructed_cycle(b, j)
            phase_overlaps = []
            for phase in (0, 1):
                overlap = 0
                for stage in range(b):
                    for t in range(1, b):
                        overlap += factor_criterion(
                            template_flag(cycle, b, phase, stage, t), b
                        )
                phase_overlaps.append(overlap)
            assert phase_overlaps == [expected_overlap(b, j)] * 2
    print("PASS: exact D* test, both phases, for odd 5<=b<=51")


if __name__ == "__main__":
    audit_canonical_conversion()
    audit_toggle_criterion()
    audit_case_table_and_formula()
    audit_full_factor_test()
