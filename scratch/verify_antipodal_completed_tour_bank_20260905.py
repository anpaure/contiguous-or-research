#!/usr/bin/env python3
"""Finite audit for antipodal completed coherent-tour banks."""

from collections import Counter


def completed_word(b: int, state_mask: int) -> tuple[int, ...]:
    state = [(state_mask >> j) & 1 for j in range(b)]
    word: list[int] = []
    for s in range(b):
        for k in range(1, b):
            j = (s + k) % b
            state[j] ^= 1
            word.append(2 * j + state[j])
        word.append(2 * s + state[s])
    return tuple(word)


def support(word: tuple[int, ...], ell: int) -> frozenset[int]:
    n = len(word)
    ans = set()
    for a in range(n):
        mask = 0
        for j in range(ell):
            mask |= 1 << word[(a + j) % n]
        assert mask.bit_count() == ell
        ans.add(mask)
    return frozenset(ans)


def audit_antipode(b: int) -> None:
    all_state = (1 << b) - 1
    base = completed_word(b, 0)
    anti = completed_word(b, all_state)
    assert all(y == (x ^ 1) for x, y in zip(base, anti))

    actual = {}
    for h in (-1, 0, 1):
        first = support(base, b + h)
        second = support(anti, b + h)
        assert len(first) == len(second) == b * b
        actual[h] = len(first & second)
    assert actual == {-1: 2 * b, 0: 0, 1: 0}, (b, actual)


def audit_collision_differences(b: int) -> None:
    supports = {
        x: tuple(
            support(completed_word(b, x), b + h) for h in (-1, 0, 1)
        )
        for x in range(1 << b)
    }
    hist = {h: Counter() for h in (-1, 0, 1)}
    collision_sets = {h: set() for h in (-1, 0, 1)}
    for difference in range(1, 1 << b):
        for index, rank_offset in enumerate((-1, 0, 1)):
            overlap = len(supports[0][index] & supports[difference][index])
            hist[rank_offset][overlap] += 1
            if overlap:
                collision_sets[rank_offset].add(difference)

    all_state = (1 << b) - 1
    assert all_state in collision_sets[-1]
    assert all_state not in collision_sets[0]
    assert all_state not in collision_sets[1]

    # The two-state code <1> has the exact bank ledger in Theorem 2.2.
    for index, rank_offset in enumerate((-1, 0, 1)):
        union = supports[0][index] | supports[all_state][index]
        expected = 2 * b * (b - 1) if rank_offset == -1 else 2 * b * b
        assert len(union) == expected

    print(
        f"b={b}: |B_-|={len(collision_sets[-1])}, "
        f"|B_0|={len(collision_sets[0])}, |B_+|={len(collision_sets[1])}"
    )


def main() -> None:
    for b in range(5, 52, 2):
        audit_antipode(b)
    for b in (5, 7, 9):
        audit_collision_differences(b)
    print("PASS: antipodal inventory for every odd 5 <= b <= 51")
    print("PASS: complete difference audit and two-tour ledger for b=5,7,9")


if __name__ == "__main__":
    main()
