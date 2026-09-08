#!/usr/bin/env python3
"""Exact replay for the Gate-B shore-difference current bound."""

from __future__ import annotations

from itertools import permutations


def window(word: tuple[int, ...], start: int, size: int) -> frozenset[int]:
    b = len(word)
    return frozenset(word[(start + offset) % b] for offset in range(size))


def harmonic(target: frozenset[int], pairs: tuple[tuple[int, int], ...]) -> int:
    answer = 1
    for left, right in pairs:
        answer *= (left in target) - (right in target)
    return answer


def current(word: tuple[int, ...], size: int, pairs: tuple[tuple[int, int], ...]) -> int:
    return sum(
        harmonic(window(word, start, size), pairs)
        for start in range(1, len(word))
    )


def direct_changed_start_audit(
    word: tuple[int, ...], r: int, pairs: tuple[tuple[int, int], ...]
) -> None:
    distinguished = {label for pair in pairs for label in pair}
    changed = 0
    total_difference = 0
    for start in range(1, len(word)):
        lower = window(word, start, r - 1)
        middle = window(word, start, r)
        added = word[(start + r - 1) % len(word)]
        difference = harmonic(middle, pairs) - harmonic(lower, pairs)
        if added not in distinguished:
            assert difference == 0
        if difference:
            changed += 1
            assert abs(difference) == 1
        total_difference += difference
    assert changed <= 2 * len(pairs)
    assert total_difference == current(word, r, pairs) - current(
        word, r - 1, pairs
    )
    assert abs(total_difference) <= 2 * len(pairs)


def blocker_sum_audit() -> None:
    # Exhaust the full r=3 catalogue.  The theorem itself allows any j;
    # this small replay uses two pairs and an arbitrary two-target blocker.
    r = 3
    b = 2 * r + 1
    pairs = ((0, 1), (2, 3))
    blocker = frozenset({0, 2, 4})
    degree = 0
    middle_sum = 0
    lower_sum = 0
    for word in permutations(range(b)):
        middle_targets = {
            window(word, start, r) for start in range(1, b)
        }
        if blocker not in middle_targets:
            continue
        degree += 1
        middle_sum += current(word, r, pairs)
        lower_sum += current(word, r - 1, pairs)
    assert degree > 0
    assert abs(middle_sum - lower_sum) <= 2 * len(pairs) * degree
    assert abs(middle_sum) <= 2 * r * degree
    assert abs(lower_sum) <= 2 * r * degree


def main() -> None:
    # Exhaust all 9! words at the first nontrivial program rank r=4,j=2.
    r = 4
    pairs = ((0, 1), (2, 3))
    tested = 0
    for word in permutations(range(2 * r + 1)):
        direct_changed_start_audit(word, r, pairs)
        tested += 1
    blocker_sum_audit()
    print(
        "GATE_B_SHORE_DIFFERENCE_CURRENT_PASS "
        f"exhaustive_words={tested} changed_starts<=2j=PASS "
        "blocker_sum=PASS"
    )


if __name__ == "__main__":
    main()
