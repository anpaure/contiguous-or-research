"""Scoped exact search, not an asymptotic theorem or an unbounded UNSAT claim.

Searches coordinate-developed k=9 words with 14 seed letters and graded
rank-four/rank-five window inventories. A bounded full-support window is
optional; the default counts all intervals of at most one period.
All nonempty target orbits are constrained simultaneously.
"""

import argparse
from itertools import combinations
from math import comb

import z3


def rotate(x, k, shift=1):
    shift %= k
    return ((x << shift) & ((1 << k) - 1)) | (x >> (k - shift)) if shift else x


def census(seed, k):
    word = [rotate(x, k, shift) for shift in range(k) for x in seed]
    seen = set()
    for start in range(len(word)):
        value = 0
        for length in range(1, len(word) + 1):
            value |= word[(start + length - 1) % len(word)]
            seen.add(value)
    return word, sorted(set(range(1, 1 << k)) - seen)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--timeout", type=int, default=120)
    parser.add_argument("--depth-four", type=int, default=3)
    parser.add_argument("--depth-five", type=int, default=4)
    parser.add_argument("--distance", type=int, default=-1)
    parser.add_argument("--window-cap", type=int, default=0)
    parser.add_argument("--random-seed", type=int, default=4471)
    args = parser.parse_args()
    k, length = 9, 14
    full = (1 << k) - 1
    cap = args.window_cap or k * length
    assert 1 <= cap <= k * length
    old = [1, 130, 136, 12, 36, 48, 80, 272, 18, 17, 9, 65, 96, 68]
    letters = [z3.BitVec(f"a_{i}", k) for i in range(length)]
    solver = z3.Solver()
    solver.set(timeout=1000 * args.timeout, random_seed=args.random_seed)
    solver.add(letters[0] == 1)
    solver.add(*(x != 0 for x in letters))
    if args.distance >= 0:
        solver.add(z3.PbLe([
            (z3.Extract(bit, bit, letters[i]) != ((old[i] >> bit) & 1), 1)
            for i in range(length) for bit in range(k)
        ], args.distance))
    windows = {}
    for start in range(length):
        value = z3.BitVecVal(0, k)
        for width in range(1, cap + 1):
            index = start + width - 1
            value = value | z3.RotateLeft(letters[index % length], index // length)
            windows[start, width] = value
        solver.add(value == full)

    for rank, width in [(4, args.depth_four), (5, args.depth_five)]:
        assert 1 <= width <= cap
        for start in range(length):
            value = windows[start, width]
            solver.add(z3.PbEq([
                (z3.Extract(bit, bit, value) == 1, 1) for bit in range(k)
            ], rank))
        for a, b in combinations(range(length), 2):
            solver.add(*(
                windows[a, width] != z3.RotateLeft(windows[b, width], shift)
                for shift in range(k)
            ))

    representatives = sorted({
        min(rotate(x, k, shift) for shift in range(k)) for x in range(1, 1 << k)
    })
    for target in representatives:
        rank = target.bit_count()
        if rank in (1, 4, 5, 9):
            continue
        possible_widths = range(1, args.depth_four) if rank < 4 else range(
            args.depth_five + 1, min(cap, args.depth_five + comb(rank, 5) - 1) + 1
        )
        variants = {rotate(target, k, shift) for shift in range(k)}
        solver.add(z3.Or([
            windows[start, width] == value
            for start in range(length) for width in possible_widths for value in variants
        ]))
    print("MODEL", {"period": k * length, "width": comb(k, k // 2),
                    "depths": (args.depth_four, args.depth_five),
                    "distance": args.distance, "window_cap": cap,
                    "timeout": args.timeout}, flush=True)
    result = solver.check()
    print("STATUS", result, flush=True)
    if result == z3.sat:
        model = solver.model()
        seed = [model.eval(x).as_long() for x in letters]
        word, holes = census(seed, k)
        assert not holes and len(word) == comb(k, k // 2)
        print("SEED", *seed)
        print("LITERAL_ALL_INTERVALS_PASS", len(word), (1 << k) - 1)
    elif result == z3.unknown:
        print("REASON", solver.reason_unknown())
    else:
        print("UNSAT_SCOPE: only the explicitly imposed developed, graded, window-cap model")


if __name__ == "__main__":
    main()
