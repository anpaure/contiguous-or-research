#!/usr/bin/env python3
"""H100-only audit of the persistent crossed 001 exceptional-family cuts."""

import argparse
import sys


def canonical_permutation(d, outside):
    a = 2 * d + 2
    b = 2 * d + 2
    n = a + b + 2 * outside + 1
    fixed = tuple(range(a + b, n))
    return (
        tuple(range(a, a + b - 1))
        + tuple(range(1, a - 2))
        + (0, a - 2, a + b - 1, a - 1)
        + fixed
    )


def tight_map(permutation):
    n = len(permutation)
    inverse_two = (n + 1) // 2
    return tuple((permutation[(2 * index) % n] * inverse_two) % n for index in range(n))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("maximum_d", type=int)
    parser.add_argument("extra_outside", type=int)
    args = parser.parse_args()
    checks = 0
    for d in range(1, args.maximum_d + 1):
        for outside in range(d - 1, d - 1 + args.extra_outside + 1):
            mapping = tight_map(canonical_permutation(d, outside))
            n = 4 * d + 2 * outside + 5
            shift_minus_one = d + outside + 2
            first = d + 1
            second = 3 * d + outside + 3
            assert len(mapping) == n
            for offset in range(d):
                assert mapping[(second + offset) % n] == (first + shift_minus_one + offset) % n
                assert mapping[(second + shift_minus_one + offset) % n] == (first + offset) % n
                assert mapping[offset] == first + offset
                assert mapping[second + offset] == 2 * d + outside + 3 + offset
                checks += 1
    print(
        f"PASS maximum_d={args.maximum_d} extra_outside={args.extra_outside} "
        f"ordered_endpoint_checks={checks}"
    )


if __name__ == "__main__":
    main()
