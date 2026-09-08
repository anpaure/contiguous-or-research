#!/usr/bin/env python3
"""Finite audit for clustered two-stream product schedules.

The proof in MATH_THEOREM_CLUSTERED_PRODUCT_PHASE_ALIGNMENT_20260821.md
is independent of this script.  This checks the exact finite identities used
there for the listed odd alphabet-half sizes.
"""


def atom(b: int, r: int):
    schedule = "A" * r + "B" * (b - r)
    ia = ib = 0
    word = []
    for t in range(b * b):
        if schedule[t % b] == "A":
            word.append(("A", ia))
            ia = (ia + 1) % b
        else:
            word.append(("B", ib))
            ib = (ib + 1) % b
    return word


def cyclic_windows(word, length: int):
    size = len(word)
    return [
        frozenset(word[(t - j) % size] for j in range(length))
        for t in range(size)
    ]


def minimum_cyclic_gap(word):
    size = len(word)
    positions = {}
    for t, letter in enumerate(word):
        positions.setdefault(letter, []).append(t)
    answer = size
    for occurrences in positions.values():
        for i, left in enumerate(occurrences):
            right = occurrences[(i + 1) % len(occurrences)]
            if i + 1 == len(occurrences):
                right += size
            answer = min(answer, right - left)
    return answer


def check_size(b: int):
    for H in range((b - 4) // 2 + 1):
        floor = b + H + 2
        for r in range(H + 2, b - H - 1):
            word = atom(b, r)
            assert minimum_cyclic_gap(word) >= floor
            for length in range(b - H, b + H + 2):
                windows = cyclic_windows(word, length)
                assert len(set(windows)) == b * b

    h = (b - 1) // 2
    if h >= 2:
        lower_atom = atom(b, h)
        upper_atom = atom(b, h + 1)

        up_left = [
            target
            for target in cyclic_windows(lower_atom, b + 1)
            if sum(letter[0] == "A" for letter in target) == h + 1
        ]
        up_right = [
            target
            for target in cyclic_windows(upper_atom, b + 1)
            if sum(letter[0] == "A" for letter in target) == h + 1
        ]
        assert len(up_left) == h * b
        assert len(up_right) == h * b
        assert not (set(up_left) & set(up_right))
        assert len(set(up_left) | set(up_right)) == b * b - b

        down_left = [
            target
            for target in cyclic_windows(lower_atom, b - 1)
            if sum(letter[0] == "A" for letter in target) == h
        ]
        down_right = [
            target
            for target in cyclic_windows(upper_atom, b - 1)
            if sum(letter[0] == "A" for letter in target) == h
        ]
        assert len(down_left) == (h + 1) * b
        assert len(down_right) == (h + 1) * b
        assert len(set(down_left) | set(down_right)) == b * b
        assert len(set(down_left) & set(down_right)) == b

    for q in range(b + 1):
        for phase in range(b):
            extra = {(phase + j) % b for j in range(1, q + 1)}
            upper = [r + len(set(range(r)) & extra) for r in range(b + 1)]
            lower = [r - len(set(range(r)) & extra) for r in range(b + 1)]

            assert all(upper[r + 1] - upper[r] in (1, 2) for r in range(b))
            assert len(set(upper)) == b + 1
            assert len(set(range(b + q + 1)) - set(upper)) == q

            assert all(lower[r + 1] - lower[r] in (0, 1) for r in range(b))
            assert set(lower) == set(range(b - q + 1))

        for local_rank in range(2 * q, b - q + 1):
            contributing_phases = 0
            for phase in range(b):
                extra = {(phase + j) % b for j in range(1, q + 1)}
                contributors = [
                    r
                    for r in range(b + 1)
                    if r + len(set(range(r)) & extra) == local_rank
                ]
                assert len(contributors) <= 1
                contributing_phases += bool(contributors)
            assert contributing_phases == b - q


def main():
    for b in (5, 7, 11, 13, 17):
        check_size(b)
        print(f"PASS b={b}")
    print("ALL CLUSTERED-PHASE CHECKS PASS")


if __name__ == "__main__":
    main()
