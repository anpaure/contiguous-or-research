#!/usr/bin/env python3
"""H100-only audit of the Proskurowski--Ruskey path inside MSW G_sf."""

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
def family(n, k, reflected=False):
    if k == n:
        return ("1" * n + "0" * n,)
    if k == 1:
        return tuple(flip(word) for word in family(n, 2, reflected))
    first = tuple(flip(word) for word in reversed(family(n, k + 1, reflected)))
    second = tuple(insert(word) for word in family(n - 1, k - 1, reflected))
    if reflected:
        return second + first
    return first + second


def pr_path(n, reflected=False):
    blocks = tuple(family(n, k, reflected) for k in range(n, 1, -1))
    tail = tuple(reversed(family(n, 1, reflected)))
    return sum(blocks, ()) + tail


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


def signatures(root, m, d, reverse=False):
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


def transposition(left, right):
    difference = [i for i, pair in enumerate(zip(left, right)) if pair[0] != pair[1]]
    return len(difference) == 2 and left[difference[0]] != left[difference[1]]


def cyclic_distance(first, second, n):
    delta = abs(first - second)
    return min(delta, n - delta)


def pair_options(left_signatures, right_signatures):
    return [
        (left_orientation, left_start, right_orientation, right_start)
        for left_orientation, left_rows in enumerate(left_signatures)
        for right_orientation, right_rows in enumerate(right_signatures)
        for left_start, signature in enumerate(left_rows)
        for right_start, other in enumerate(right_rows)
        if signature == other
    ]


def path_port_dp(edge_options, n, d):
    # State at an internal row is its global orientation and the incoming
    # edge's row-side port. Reuse or distance >=d+1 is the degree-two gate.
    if not edge_options:
        return True, []
    states = {
        (right_orientation, right): [option]
        for option in edge_options[0]
        for _, _, right_orientation, right in (option,)
    }
    for options in edge_options[1:]:
        next_states = {}
        for option in options:
            left_orientation, left, right_orientation, right = option
            for (incoming_orientation, incoming), witness in states.items():
                if left_orientation != incoming_orientation:
                    continue
                if left == incoming or cyclic_distance(left, incoming, n) >= d + 1:
                    next_states.setdefault(
                        (right_orientation, right), witness + [option]
                    )
                    break
        states = next_states
        if not states:
            return False, []
    return True, next(iter(states.values()))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("m", type=int)
    parser.add_argument("d", type=int)
    parser.add_argument("--reflected", action="store_true")
    args = parser.parse_args()
    m, d = args.m, args.d
    path = pr_path(m, args.reflected)
    assert len(path) > 1 and len(set(path)) == len(path)
    assert all(transposition(left, right) for left, right in zip(path, path[1:]))

    n = 2 * m + 1
    signature_rows = [
        (signatures(word, m, d, False), signatures(word, m, d, True))
        for word in path
    ]
    edge_options = [
        pair_options(left, right)
        for left, right in zip(signature_rows, signature_rows[1:])
    ]
    missing = [index for index, options in enumerate(edge_options) if not options]
    feasible, witness = path_port_dp(edge_options, n, d)
    print(
        f"ALL_ORIENTATIONS edges={len(edge_options)} "
        f"missing_edges={len(missing)} minimum_options={min(map(len, edge_options))} "
        f"maximum_options={max(map(len, edge_options))} separated_path_feasible={int(feasible)}"
    )
    if missing:
        index = missing[0]
        print("FIRST_MISSING", index, path[index], path[index + 1])
    if not feasible and not missing:
        # Find the earliest infeasible prefix for a frozen obstruction.
        for length in range(2, len(edge_options) + 1):
            prefix_feasible, _ = path_port_dp(edge_options[:length], n, d)
            if not prefix_feasible:
                index = length - 1
                print(
                    "FIRST_PORT_DP_OBSTRUCTION",
                    index,
                    path[index - 1],
                    path[index],
                    path[index + 1],
                    "left_options", edge_options[index - 1],
                    "right_options", edge_options[index],
                )
                break
    if feasible:
        distinct_hist = {1: 0, 2: 0}
        for index in range(1, len(path) - 1):
            incoming = witness[index - 1][3]
            outgoing = witness[index][1]
            distinct_hist[1 if incoming == outgoing else 2] += 1
        print("WITNESS_DISTINCT_PORT_HIST", distinct_hist)


if __name__ == "__main__":
    main()
