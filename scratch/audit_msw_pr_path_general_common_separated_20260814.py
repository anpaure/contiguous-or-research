#!/usr/bin/env python3
"""H100-only PR-path audit with the exact forced/maximal compatibility test.

This deliberately requires the two incident starts at every internal row to
be distinct and cyclically separated by d+1.  A PASS therefore needs no
same-start multiway coalescence or transitive history-class bookkeeping.
"""

import argparse
from functools import lru_cache


def ascent(word):
    return len(word) - len(word.lstrip("1"))


def flip(word):
    k = ascent(word)
    return "1" * (k - 1) + "01" + word[k + 1 :]


def insert(word):
    k = ascent(word)
    return "1" * (k + 1) + "00" + word[k + 1 :]


@lru_cache(None)
def family(n, k):
    if k == n:
        return ("1" * n + "0" * n,)
    if k == 1:
        return tuple(flip(word) for word in family(n, 2))
    return (
        tuple(flip(word) for word in reversed(family(n, k + 1)))
        + tuple(insert(word) for word in family(n - 1, k - 1))
    )


def pr_path(n):
    return sum((family(n, k) for k in range(n, 1, -1)), ()) + tuple(
        reversed(family(n, 1))
    )


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
    assert sorted(rho) == list(range(n))
    return tuple(rho[(2 * index) % n] for index in range(n))


def oriented_ports(root, m, d):
    order = tight_order(root, m)
    n = 2 * m + 1
    shift = m + 1 - d
    answer = []
    for _ in range(2):
        row = []
        for start in range(n):
            forced = []
            maximal = []
            for offset in range(d):
                positions = [order[(start + offset + step) % n] for step in range(shift)]
                forced.append((1 << positions[0]) | (1 << positions[-1]))
                maximal.append(sum(1 << position for position in positions))
            row.append((tuple(forced), tuple(maximal)))
        answer.append(tuple(row))
        order = tuple(reversed(order))
    return tuple(answer)


def compatible(left, right, d):
    left_forced, left_maximal = left
    right_forced, right_maximal = right
    return all(
        ((left_forced[j] | right_forced[j]) & ~(left_maximal[j] & right_maximal[j]))
        == 0
        for j in range(d)
    )


def edge_options(left, right, n, d):
    return [
        (left_orientation, left_start, right_orientation, right_start)
        for left_orientation in range(2)
        for left_start in range(n)
        for right_orientation in range(2)
        for right_start in range(n)
        if compatible(
            left[left_orientation][left_start],
            right[right_orientation][right_start],
            d,
        )
    ]


def cyclic_distance(first, second, n):
    delta = abs(first - second)
    return min(delta, n - delta)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("m", type=int)
    parser.add_argument("d", type=int)
    parser.add_argument("--witness")
    args = parser.parse_args()
    m, d = args.m, args.d
    n = 2 * m + 1
    path = pr_path(m)
    rows = [oriented_ports(word, m, d) for word in path]

    reachable = None
    predecessors = []
    minimum_options = None
    maximum_options = 0
    option_total = 0
    missing_edges = 0
    first_missing = None
    first_dp_failure = None

    for edge_index in range(len(path) - 1):
        options = edge_options(rows[edge_index], rows[edge_index + 1], n, d)
        option_total += len(options)
        minimum_options = len(options) if minimum_options is None else min(minimum_options, len(options))
        maximum_options = max(maximum_options, len(options))
        if not options:
            missing_edges += 1
            if first_missing is None:
                first_missing = edge_index

        if reachable is None:
            new_reachable = {option: None for option in options}
        elif reachable:
            available = {0: set(), 1: set()}
            representative = {}
            for previous in reachable:
                orientation, start = previous[2], previous[3]
                available[orientation].add(start)
                representative.setdefault((orientation, start), previous)
            new_reachable = {}
            for option in options:
                orientation, start = option[0], option[1]
                predecessor = next(
                    (
                        representative[orientation, old]
                        for old in available[orientation]
                        if old != start and cyclic_distance(old, start, n) >= d + 1
                    ),
                    None,
                )
                if predecessor is not None:
                    new_reachable[option] = predecessor
        else:
            new_reachable = {}
        predecessors.append(new_reachable)
        reachable = new_reachable
        if not reachable and first_dp_failure is None:
            first_dp_failure = edge_index

    feasible = bool(reachable)
    print(
        f"SUMMARY m={m} d={d} n={n} vertices={len(path)} edges={len(path)-1} "
        f"pairwise_missing_edges={missing_edges} minimum_options={minimum_options} "
        f"maximum_options={maximum_options} option_total={option_total} "
        f"strict_separated_path_feasible={int(feasible)} first_missing={first_missing} "
        f"first_dp_failure={first_dp_failure}"
    )
    if first_missing is not None:
        print("FIRST_MISSING", first_missing, path[first_missing], path[first_missing + 1])
    if first_dp_failure is not None and first_dp_failure > 0:
        index = first_dp_failure
        print("FIRST_DP_ROWS", path[index - 1], path[index], path[index + 1])

    if feasible and args.witness:
        option = next(iter(reachable))
        witness = [None] * (len(path) - 1)
        for edge_index in range(len(path) - 2, -1, -1):
            witness[edge_index] = option
            option = predecessors[edge_index][option]
        with open(args.witness, "w", encoding="utf-8") as output:
            output.write(f"H {m} {d} {n} {len(path)}\n")
            for index, (left_orientation, left_start, right_orientation, right_start) in enumerate(witness):
                output.write(
                    f"E {index} {left_orientation} {left_start} "
                    f"{right_orientation} {right_start}\n"
                )


if __name__ == "__main__":
    main()
