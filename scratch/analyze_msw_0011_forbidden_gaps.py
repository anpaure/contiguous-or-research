#!/usr/bin/env python3
"""Classify the exact forbidden-gap witnesses for the 0011 packet.

All arithmetic is the symbolic tight-position reduction from the explicit
flip permutation.  This script is intended to run only on H100.
"""

from collections import Counter, defaultdict


def labelled_points(d, left, right, outside):
    m = left + right + outside + 2
    n = 2 * m + 1
    raw = {
        "b0": 0,
        "b1": left,
        "b2": left + 1,
        "b3": m + left + 1,
        "b4": m + left + 2,
        "b5": m + left + right + 2,
    }
    shift = m - d
    points = [(value % n, name) for name, value in raw.items()]
    points += [((value - shift) % n, "q" + name[1:]) for name, value in raw.items()]
    return n, sorted(points)


def gaps(d, left, right, outside):
    n, points = labelled_points(d, left, right, outside)
    answer = []
    for index, (value, name) in enumerate(points):
        next_value, next_name = points[(index + 1) % len(points)]
        if index + 1 == len(points):
            next_value += n
        answer.append((next_value - value, name, next_name, value % n))
    return answer


def sign(value):
    return "-" if value < 0 else "0" if value == 0 else "+"


def main():
    winners = Counter()
    winner_by_sign = defaultdict(Counter)
    failures = []
    for d in range(2, 41):
        for total in range(3 * d - 1, 3 * d + 16):
            for left in range(1, total):
                for right in range(1, total - left + 1):
                    outside = total - left - right
                    entries = gaps(d, left, right, outside)
                    good = [entry for entry in entries if entry[0] >= d + 1]
                    if not good:
                        failures.append((d, left, right, outside))
                        continue
                    gap, before, after, start = max(good)
                    key = (before, after)
                    winners[key] += 1
                    region = (sign(left - d), sign(right - d), sign(outside - (d - 1)))
                    winner_by_sign[region][key] += 1

    print("failure_count", len(failures))
    print("failures_head", failures[:100])
    print("winner_pairs")
    for pair, count in winners.most_common():
        print(pair, count)
    print("winner_by_sign")
    for region, counts in sorted(winner_by_sign.items()):
        print(region, dict(counts))

    print("boundary_tables")
    for d in range(2, 13):
        total = 3 * d - 1
        row = []
        for left in range(1, total):
            for right in range(1, total - left + 1):
                outside = total - left - right
                entries = gaps(d, left, right, outside)
                good = [entry for entry in entries if entry[0] >= d + 1]
                pair = None if not good else max(good)[1:3]
                if pair is None or (left, right, outside) == (d, d, d - 1):
                    row.append((left, right, outside, pair, entries))
        print("d", d, row)


if __name__ == "__main__":
    main()
