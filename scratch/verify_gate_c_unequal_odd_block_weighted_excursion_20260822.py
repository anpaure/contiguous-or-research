#!/usr/bin/env python3
"""Finite audit for unequal odd blocks and weighted-excursion loss."""

from itertools import permutations, product


def odd_compositions(total, parts):
    if parts == 1:
        if total > 0 and total % 2 == 1:
            yield (total,)
        return
    for first in range(1, total, 2):
        for tail in odd_compositions(total - first, parts - 1):
            yield (first,) + tail


def starts(lengths):
    answer = [0]
    for length in lengths[:-1]:
        answer.append(answer[-1] + length)
    return answer


def construction(lengths, target_order):
    b = sum(lengths)
    k = len(lengths)
    domain_start = starts(lengths)
    rank = [0] * k
    for position, block in enumerate(target_order):
        rank[block] = position
    target_start = [0] * k
    cursor = 0
    for block in target_order:
        target_start[block] = cursor
        cursor += lengths[block]
    alpha = [None] * b
    for block in range(k):
        for offset in range(lengths[block]):
            alpha[domain_start[block] + offset] = target_start[block] + offset
    pi = [alpha[x] + b * ((alpha[x] + x) % 2) for x in range(b)]
    pi += [value + b for value in pi]
    return domain_start, rank, pi


def direct_word(lengths, target_order, block, offset):
    b = sum(lengths)
    domain_start, _, pi = construction(lengths, target_order)
    row = domain_start[block] + offset
    selected = {pi[row + step] % (2 * b) for step in range(b + 1)}
    origin = pi[row]
    return tuple(1 if (origin + step) % (2 * b) in selected else -1
                 for step in range(2 * b)), pi, row


def formula_data(lengths, target_order, block, offset):
    k = len(lengths)
    rank = [0] * k
    for position, value in enumerate(target_order):
        rank[value] = position
    others = [target_order[(rank[block] + u) % k] for u in range(1, k)]
    signs = [1 if (((other - block) % k - u) % 2 == 0) else -1
             for u, other in enumerate(others, 1)]
    word = [1] * (lengths[block] - offset)
    for other, sign in zip(others, signs):
        word.extend([sign] * lengths[other])
    word.extend([1] * (offset + 1))
    word.extend([-1] * (lengths[block] - offset - 1))
    for other, sign in zip(others, signs):
        word.extend([-sign] * lengths[other])
    word.extend([-1] * offset)
    prefixes = [0]
    for other, sign in zip(others, signs):
        prefixes.append(prefixes[-1] + lengths[other] * sign)
    endpoint = prefixes[-1]
    lower = -min(prefixes)
    upper = max(value - endpoint for value in prefixes)
    return tuple(word), lower, upper


def positive(word):
    height = 0
    for sign in word[:-1]:
        height += sign
        if height <= 0:
            return False
    return sum(word) == 2


def primitive_after_delete(word, step):
    changed = list(word)
    assert changed[step] == 1
    changed[step] = -1
    height = 0
    for sign in changed[:-1]:
        height += sign
        if height <= 0:
            return False
    return sum(changed) == 0


def audit_instance(lengths, target_order):
    b = sum(lengths)
    domain_start, _, pi = construction(lengths, target_order)
    total_flags = 0
    killed = 0
    deep = 0
    lower_upper_sum = 0
    for block, length in enumerate(lengths):
        # Excursions do not depend on the row offset.
        _, lower, upper = formula_data(lengths, target_order, block, 1 if length > 1 else 0)
        predicted_killed = min(length - 1, lower + max(0, upper - 2))
        actual_killed = 0
        for offset in range(1, length):
            direct, pi_here, row = direct_word(lengths, target_order, block, offset)
            formula, lower_here, upper_here = formula_data(
                lengths, target_order, block, offset
            )
            assert direct == formula
            assert (lower_here, upper_here) == (lower, upper)
            is_positive = positive(direct)
            predicted_positive = (max(1, upper - 1) <= offset
                                  <= length - lower - 1)
            assert is_positive == predicted_positive
            actual_killed += not is_positive

            origin = pi_here[row]
            deletion_steps = [
                (pi_here[row + shift] - origin) % (2 * b)
                for shift in range(1, b)
            ]
            accepted = sum(primitive_after_delete(direct, step)
                           for step in deletion_steps)
            total_flags += accepted
            if not is_positive:
                assert accepted == 0
            is_deep = upper + 1 <= offset <= length - lower - 3
            if is_deep:
                deep += 1
                assert accepted == b - 2
        assert actual_killed == predicted_killed
        killed += actual_killed
        lower_upper_sum += lower + upper + 3

    q = b * (b - 1)
    assert q - total_flags >= (b - 1) * killed
    assert total_flags >= (b - 2) * deep
    assert q - total_flags <= b + (b - 2) * lower_upper_sum


def audit():
    instances = 0
    for b in (5, 7, 9):
        for k in range(3, b + 1, 2):
            for lengths in odd_compositions(b, k):
                # Exhaust every order up to K=5; use deterministic samples
                # beyond that to keep the checker fast.
                orders = list(permutations(range(k))) if k <= 5 else [
                    tuple(range(k)), tuple(reversed(range(k)))
                ]
                for order in orders:
                    audit_instance(lengths, order)
                    instances += 1
    print(f"PASS: {instances} unequal odd-block instances and all loss ledgers")


if __name__ == "__main__":
    audit()
