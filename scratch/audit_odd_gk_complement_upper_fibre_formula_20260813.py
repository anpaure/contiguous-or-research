#!/usr/bin/env python3
"""Test a direct formula for GK/complement central upper multiplicity."""

import argparse
import itertools
from collections import Counter


def masks(n, rank):
    for cc in itertools.combinations(range(n), rank):
        yield sum(1 << i for i in cc)


def unmatched(word, n):
    stack, free_ones = [], []
    for i in range(n):
        if (word >> i) & 1:
            if stack:
                stack.pop()
            else:
                free_ones.append(i)
        else:
            stack.append(i)
    return free_ones, stack


def gk_up(word, n):
    return word | (1 << unmatched(word, n)[1][0])


def gk_down(word, n):
    return word ^ (1 << unmatched(word, n)[0][-1])


def complement_up(word, n):
    full = (1 << n) - 1
    return full ^ gk_down(full ^ word, n)


def direct_fibre(upper, n):
    result = []
    bits = [i for i in range(n) if (upper >> i) & 1]
    for a, b in itertools.combinations(bits, 2):
        lower = upper ^ (1 << a) ^ (1 << b)
        if gk_up(lower, n) | complement_up(lower, n) == upper:
            result.append((a, b))
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("r", type=int)
    args = parser.parse_args()
    r, n = args.r, 2 * args.r - 1
    histogram = Counter()
    for upper in masks(n, r + 1):
        pairs = direct_fibre(upper, n)
        assert pairs
        histogram[len(pairs)] += 1
        assert len(pairs) <= 3
    print("r", r, "upper_fibre_hist", dict(sorted(histogram.items())))


if __name__ == "__main__":
    main()
