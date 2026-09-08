#!/usr/bin/env python3
"""Explore the BTK functional-root map on the odd middle layer."""

from itertools import combinations


def unmatched(word):
    stack = []
    free_ones = []
    for i, bit in enumerate(word):
        if bit == "0":
            stack.append(i)
        elif stack:
            stack.pop()
        else:
            free_ones.append(i)
    return free_ones, stack


def step(word):
    ones, zeros = unmatched(word)
    if len(ones) <= 1:
        return None
    out = list(word)
    out[ones[-1]] = "0"
    out[zeros[0]] = "1"
    return "".join(out)


def root_owner(word):
    while True:
        nxt = step(word)
        if nxt is None:
            return word
        word = nxt


def root_lower(word):
    root = root_owner(word)
    ones, zeros = unmatched(root)
    assert len(ones) == 1 and not zeros
    out = list(root)
    out[ones[0]] = "0"
    return "".join(out)


def ballot_lowers(r):
    n = 2 * r - 1
    for ones in combinations(range(n), r - 1):
        word = ["0"] * n
        for i in ones:
            word[i] = "1"
        word = "".join(word)
        free_ones, free_zeros = unmatched(word)
        if not free_ones and len(free_zeros) == 1:
            yield word


def main():
    for r in range(2, 6):
        print("r", r)
        for d in list(ballot_lowers(r))[:5]:
            rows = []
            for x, bit in enumerate(d):
                if bit == "0":
                    a = list(d)
                    a[x] = "1"
                    rows.append((x, root_lower("".join(a))))
            print(d, rows)
        print()


if __name__ == "__main__":
    main()
