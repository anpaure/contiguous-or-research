"""An exact fractional [4]^6 chain-pair cover of cost 1248, not an OR word."""

import argparse
from collections import Counter
from itertools import product


# The weights below have denominator 15. Develop each pair uniformly under
# coordinate permutations and simultaneous reflection of all six coordinates.
DATA = [
    (96, "000 100 110 111 211 221 222 232 233 333",
     "000 001 002 003 013 023 033 133 233 333"),
    (176, "000 010 110 210 211 212 312 322 332 333",
     "000 001 002 003 013 023 033 133 233 333"),
    (60, "110 111 211 212 222 232", "011 111 112 122 222 223"),
    (56, "00 01 02 12 13 23 33", "0111 0112 0113 0123 0223 1223 2223"),
    (92, "00 01 02 03 13 23 33", "0111 0112 1112 1113 1123 1223 2223"),
    (44, "000 100 200 201 301 302 312 313 323",
     "001 002 012 013 023 123 133 233"),
    (52, "000 100 200 201 301 302 312 313 323 333",
     "001 002 012 013 023 123 133 233"),
    (52, "010 020 030 130 230 231 331 332",
     "001 002 012 013 113 123 223 233"),
    (60, "010 020 120 130 230 330 331 332 333",
     "001 011 012 022 023 123 133 233"),
    (48, "100 200 300 310 311 312 322 323",
     "001 002 003 013 113 123 223 233"),
    (60, "00 10 20 21 31 32 33",
     "0001 0111 0112 0122 1122 1123 1223 2223 2333"),
    (62, "011 021 022 122 222 223", "011 012 022 122 222 223"),
    (28, "000 001 002 012 022 122 222 223", "011 012 022 122 222 223 233 333"),
    (224, "010 110 120 121 122 222 232 233 333",
     "000 001 011 012 013 113 123 223 233"),
]


def rows():
    return [(weight, tuple(tuple(map(int, p)) for p in left.split()),
             tuple(tuple(map(int, p)) for p in right.split()))
            for weight, left, right in DATA]


def orbit(point):
    count = tuple(point.count(i) for i in range(4))
    return min(count, count[::-1])


def check():
    populations = Counter(orbit(p) for p in product(range(4), repeat=6))
    occurrences = Counter()
    cost, volume = 0, 0
    for weight, left, right in rows():
        assert len(left[0]) + len(right[0]) == 6
        for chain in (left, right):
            assert all(len(p) == len(chain[0]) and all(0 <= x < 4 for x in p) for p in chain)
            assert all(x != y and all(a <= b for a, b in zip(x, y))
                       for x, y in zip(chain, chain[1:]))
        for x, y in product(left, right):
            occurrences[orbit(x + y)] += weight
        cost += weight * (len(left) + len(right))
        volume += weight * len(left) * len(right)
    assert all(occurrences[p] >= 15 * count for p, count in populations.items())
    assert cost == 15 * 1248
    print(f"PASS exact fractional cover: 14 orbit types, 44 point orbits, cost={cost}/15=1248")
    print(f"Indexed target volume={volume}/15; excess={volume - 15*4096}/15")
    return [(left, right) for _, left, right in rows()]


def check_ternary():
    c = "000 001 002 012 022 122 222"
    data = [(1, "111", "111"),
            (6, c, "000 001 011 021 121 221 222"),
            (5, c, "000 010 110 111 121 122 222"),
            (4, c, "100 101 111 121 221"),
            (2, c, "001 002 012 022 122"),
            (3, "011 111 112", "011 021 121"),
            (6, "001 011 111 112 122", "010 020 021 121 221")]

    def kind(point):
        counts = tuple(point.count(i) for i in range(3))
        return min(counts, counts[::-1])

    populations = Counter(kind(p) for p in product(range(3), repeat=6))
    coverage, cost, volume = Counter(), 0, 0
    for weight, raw_left, raw_right in data:
        left = tuple(tuple(map(int, p)) for p in raw_left.split())
        right = tuple(tuple(map(int, p)) for p in raw_right.split())
        for chain in (left, right):
            assert all(x != y and all(a <= b for a, b in zip(x, y))
                       for x, y in zip(chain, chain[1:]))
        for x, y in product(left, right):
            coverage[kind(x + y)] += weight
        cost += weight * (len(left) + len(right))
        volume += weight * len(left) * len(right)
    assert all(coverage[p] >= count for p, count in populations.items())
    assert cost == 306 and volume == 927
    print("PASS exact fractional [3]^6 cover: cost=306, volume=927, excess=198")


def check_integral_baseline():
    chains = [tuple((x,) for x in range(4))]
    for _ in range(2):
        following = []
        for chain in chains:
            for j in range(2):
                last = len(chain) - 1 - j
                following.append(tuple([chain[i] + (j,) for i in range(last + 1)]
                                       + [chain[last] + (y,) for y in range(j + 1, 4)]))
        chains = following
    row_orders = [((0, 1, 2), (3, 4, 5)), ((1, 2, 4), (3, 5, 0)),
                  ((1, 4, 3), (5, 2, 0)), ((0, 4, 1), (2, 3, 5)),
                  ((4, 2, 3), (5, 0, 1))]
    coverage, cost, count = Counter(), 0, 0
    for left, right in row_orders:
        for c, d in product(chains, repeat=2):
            cost += len(c) + len(d)
            count += 1
            for x, y in product(c, d):
                point = [0] * 6
                for i, value in zip(left + right, x + y):
                    point[i] = value
                coverage[tuple(point)] += 1
    assert set(coverage) == set(product(range(4), repeat=6))
    assert cost == 1280 and count == 80 and sum(coverage.values()) == 5120
    print("PASS integral [4]^6 baseline: cost=1280, rectangles=80, excess=1024")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--integer-seconds", type=float, default=0)
    parser.add_argument("--two-exchange", action="store_true")
    args = parser.parse_args()
    check_ternary()
    check_integral_baseline()
    seeds = check()
    if args.integer_seconds or args.two_exchange:
        from qary_template_search_20260906_c52e9 import orbit_integer_cover
        orbit_integer_cover(4, 6, seeds, -1 if args.two_exchange else args.integer_seconds)
