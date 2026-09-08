#!/usr/bin/env python3
"""H100-only audit: does primitive wrapping preserve full compatibility?"""

import argparse
from itertools import combinations


def dyck_words(m):
    answer = []

    def visit(position, up, down, word):
        if position == 2 * m:
            answer.append(word)
            return
        if up < m:
            visit(position + 1, up + 1, down, word + "1")
        if down < up:
            visit(position + 1, up, down + 1, word + "0")

    visit(0, 0, 0, "")
    return answer


def g(word):
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


def hmap(word):
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


def tight_order(root):
    m = len(root) // 2
    word = root
    rho = []
    for _ in range(m):
        word, first = g(word)
        word, second = hmap(word)
        rho += [first, second]
    rho.append(2 * m)
    n = 2 * m + 1
    return tuple(rho[(2 * index) % n] for index in range(n))


def ports(root, d):
    m = len(root) // 2
    n = 2 * m + 1
    shift = m + 1 - d
    order = tight_order(root)
    answer = []
    for _ in range(2):
        for start in range(n):
            forced = []
            maximal = []
            for offset in range(d):
                positions = [order[(start + offset + step) % n] for step in range(shift)]
                forced.append((1 << positions[0]) | (1 << positions[-1]))
                maximal.append(sum(1 << position for position in positions))
            answer.append((forced, maximal))
        order = tuple(reversed(order))
    return answer


def compatible(left, right, d):
    return any(
        all(
            ((lf[j] | rf[j]) & ~(lm[j] & rm[j])) == 0
            for j in range(d)
        )
        for lf, lm in left
        for rf, rm in right
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("m", type=int)
    parser.add_argument("d", type=int)
    args = parser.parse_args()
    roots = dyck_words(args.m)
    port_data = {root: ports(root, args.d) for root in roots}
    seen_edges = compatible_edges = failures = 0
    examples = []
    for left, right in combinations(roots, 2):
        if sum(a != b for a, b in zip(left, right)) != 2:
            continue
        seen_edges += 1
        if not compatible(port_data[left], port_data[right], args.d):
            continue
        compatible_edges += 1
        wrapped_left = "1" + left + "0"
        wrapped_right = "1" + right + "0"
        if not compatible(ports(wrapped_left, args.d), ports(wrapped_right, args.d), args.d):
            failures += 1
            if len(examples) < 20:
                examples.append((left, right, wrapped_left, wrapped_right))
    print(
        f"SUMMARY m={args.m} d={args.d} roots={len(roots)} "
        f"transposition_edges={seen_edges} compatible_edges={compatible_edges} "
        f"wrapping_failures={failures}"
    )
    for example in examples:
        print("FAIL", *example)


if __name__ == "__main__":
    main()
