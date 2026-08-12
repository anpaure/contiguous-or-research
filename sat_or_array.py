#!/usr/bin/env python3
"""Generate a DIMACS instance for a shortest universal subarray-OR array.

The generated instance asks for an array of ``length`` nonzero-target entries
whose contiguous subarray ORs contain every mask 1..(2**bits-1).  Zero is
handled separately: inserting one zero into such an array preserves all
nonzero ORs and represents zero.
"""

from __future__ import annotations

import argparse
from pathlib import Path


def build(
    bits: int,
    length: int,
    seed: list[int] | None = None,
    max_changes: int | None = None,
) -> tuple[int, list[list[int]], list[list[int]]]:
    next_var = 0
    clauses: list[list[int]] = []

    def new_var() -> int:
        nonlocal next_var
        next_var += 1
        return next_var

    entry = [[new_var() for _ in range(bits)] for _ in range(length)]
    interval_or: dict[tuple[int, int, int], int] = {}

    for left in range(length):
        for right in range(left, length):
            for bit in range(bits):
                out = new_var()
                interval_or[left, right, bit] = out
                if left == right:
                    source = entry[right][bit]
                    clauses.extend(([-out, source], [out, -source]))
                else:
                    previous = interval_or[left, right - 1, bit]
                    current = entry[right][bit]
                    clauses.extend(
                        ([-previous, out], [-current, out], [-out, previous, current])
                    )

    # A selector certifies that one particular interval has exactly `target`.
    for target in range(1, 1 << bits):
        selectors: list[int] = []
        for left in range(length):
            for right in range(left, length):
                selector = new_var()
                selectors.append(selector)
                for bit in range(bits):
                    value = interval_or[left, right, bit]
                    clauses.append(
                        [-selector, value if target & (1 << bit) else -value]
                    )
        clauses.append(selectors)

    # Break bit-permutation symmetry.  Relabeling bits lets us assume that
    # the first exact occurrences of 1,2,4,... appear in that order.
    singleton = [[new_var() for _ in range(length)] for _ in range(bits)]
    for bit in range(bits):
        for index in range(length):
            literals = [
                entry[index][other] if other == bit else -entry[index][other]
                for other in range(bits)
            ]
            flag = singleton[bit][index]
            for literal in literals:
                clauses.append([-flag, literal])
            clauses.append([flag, *(-literal for literal in literals)])

    for bit in range(1, bits):
        for index in range(length):
            clauses.append([-singleton[bit][index], *singleton[bit - 1][:index]])

    if seed is not None:
        if len(seed) != length:
            raise ValueError("seed length does not match the requested array length")
        if any(value < 0 or value >= 1 << bits for value in seed):
            raise ValueError("seed entries must be in [0, 2**bits)")
        if max_changes is None:
            max_changes = 0

        changed = [new_var() for _ in range(length)]
        for index, value in enumerate(seed):
            difference_literals: list[int] = []
            for bit, variable in enumerate(entry[index]):
                differs = -variable if value & (1 << bit) else variable
                difference_literals.append(differs)
                clauses.append([-differs, changed[index]])
            clauses.append([-changed[index], *difference_literals])

        # The intended repair neighborhoods are tiny (one or two positions),
        # so the direct subset encoding is compact and easy to audit.
        from itertools import combinations

        for forbidden in combinations(changed, max_changes + 1):
            clauses.append([-variable for variable in forbidden])

    return next_var, clauses, entry


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("bits", type=int)
    parser.add_argument("length", type=int)
    parser.add_argument("output", type=Path)
    parser.add_argument(
        "--seed",
        help="comma-separated seed array; optionally constrain its Hamming neighborhood",
    )
    parser.add_argument("--max-changes", type=int)
    args = parser.parse_args()

    seed = [int(value) for value in args.seed.split(",")] if args.seed else None
    variables, clauses, _ = build(args.bits, args.length, seed, args.max_changes)
    with args.output.open("w", encoding="ascii") as stream:
        stream.write(f"p cnf {variables} {len(clauses)}\n")
        for clause in clauses:
            stream.write(" ".join(map(str, clause)))
            stream.write(" 0\n")


if __name__ == "__main__":
    main()
