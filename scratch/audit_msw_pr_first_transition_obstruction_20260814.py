#!/usr/bin/env python3
"""H100-only targeted audit of the first PR same-forced obstruction."""

import argparse


def g(word, m):
    before = []
    height = down_zero = 0
    for bit in word:
        before.append(height)
        if bit == "0" and height == 0:
            down_zero += 1
        height += 1 if bit == "1" else -1
    seen = 0
    for position, bit in enumerate(word):
        if bit == "0" and before[position] in (0, 1):
            seen += 1
            if seen == down_zero + 1:
                return word[:position] + "1" + word[position + 1 :], position
    raise AssertionError


def hmap(word, m):
    before = []
    height = up_one = 0
    for bit in word:
        before.append(height)
        if bit == "1" and height == 1:
            up_one += 1
        height += 1 if bit == "1" else -1
    seen = 0
    for position, bit in enumerate(word):
        if bit == "1" and before[position] in (0, 1):
            seen += 1
            if seen == up_one:
                return word[:position] + "0" + word[position + 1 :], position
    raise AssertionError


def tight_order(root, m):
    word = root
    rho = []
    for _ in range(m):
        word, first = g(word, m)
        word, second = hmap(word, m)
        rho += [first, second]
    rho.append(2 * m)
    n = 2 * m + 1
    return tuple(rho[(2 * index) % n] for index in range(n))


def signatures(root, m, d, reverse):
    order = tight_order(root, m)
    if reverse:
        order = tuple(reversed(order))
    n = 2 * m + 1
    shift = m + 1 - d
    return tuple(
        tuple(
            sorted(
                (
                    order[(start + offset) % n],
                    order[(start + shift - 1 + offset) % n],
                )
            )
            for offset in range(d)
        )
        for start in range(n)
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("maximum_d", type=int)
    args = parser.parse_args()
    for d in range(2, args.maximum_d + 1):
        m = 3 * d + 1
        left = "1" * (3 * d) + "0" * d + "1" + "0" * (2 * d + 1)
        right = "1" * (3 * d) + "0" * (d + 1) + "1" + "0" * (2 * d)
        assert len(left) == len(right) == 2 * m
        left_rows = (signatures(left, m, d, False), signatures(left, m, d, True))
        right_rows = (signatures(right, m, d, False), signatures(right, m, d, True))
        matches = []
        for left_orientation, left_signatures in enumerate(left_rows):
            for right_orientation, right_signatures in enumerate(right_rows):
                for left_start, signature in enumerate(left_signatures):
                    for right_start, other in enumerate(right_signatures):
                        if signature == other:
                            matches.append(
                                (left_orientation, left_start, right_orientation, right_start)
                            )
        print(
            f"d={d} m={m} left={left} right={right} "
            f"oriented_common_history_options={len(matches)}"
        )


if __name__ == "__main__":
    main()
