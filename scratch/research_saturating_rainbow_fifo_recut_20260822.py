#!/usr/bin/env python3
"""Finite evidence for FIFO recuts of the m=3 rainbow saturating path.

This is a research diagnostic, not an exhaustive proof.  It generates
rainbow Hamilton cycles of J(7,2), suppresses them to the corresponding
21-owner saturating cycles, tries every opening used in Theorem 4.1 of
MATH_THEOREM_SECOND_SHADOW_CANONICAL_NO_AND_RAINBOW_TWO_SDR_REDUCTION_20260813.md,
and computes the exact minimum number of contiguous wreath-row arcs.

The exact arc test uses the port map from the accompanying proof:
for edge i, the departure label occupies row position i and the arrival
label occupies row position i+m modulo n.  A path interval of fewer than n
edges extends to one cyclic permutation row iff equal positions receive
equal labels and distinct positions receive distinct labels.
"""

from __future__ import annotations

import argparse
import itertools
import random
from collections import Counter


N_GROUND = 7
RANK = 3


def subset(items: tuple[int, ...]) -> int:
    return sum(1 << item for item in items)


PAIRS = [subset(c) for c in itertools.combinations(range(N_GROUND), 2)]
TRIPLES = {subset(c) for c in itertools.combinations(range(N_GROUND), RANK)}


PAIR_ADJ: dict[int, list[tuple[int, int]]] = {x: [] for x in PAIRS}
for ix, x in enumerate(PAIRS):
    for y in PAIRS[ix + 1 :]:
        if (x & y).bit_count() == 1:
            colour = x | y
            PAIR_ADJ[x].append((y, colour))
            PAIR_ADJ[y].append((x, colour))


def random_rainbow_pair_cycle(seed: int, call_cap: int = 200_000) -> tuple[int, ...] | None:
    """Find one rainbow Hamilton cycle of J(7,2) by seeded DFS."""

    rng = random.Random(seed)
    start = PAIRS[0]
    path = [start]
    used_vertices = {start}
    used_colours: set[int] = set()
    calls = 0

    def visit() -> bool:
        nonlocal calls
        calls += 1
        if calls > call_cap:
            return False
        if len(path) == len(PAIRS):
            return (
                (path[-1] & start).bit_count() == 1
                and (path[-1] | start) not in used_colours
            )

        candidates = []
        for nxt, colour in PAIR_ADJ[path[-1]]:
            if nxt in used_vertices or colour in used_colours:
                continue
            onward = sum(
                z not in used_vertices and c not in used_colours
                for z, c in PAIR_ADJ[nxt]
            )
            candidates.append((onward, rng.random(), nxt, colour))
        candidates.sort()

        for _, __, nxt, colour in candidates:
            path.append(nxt)
            used_vertices.add(nxt)
            used_colours.add(colour)
            if visit():
                return True
            used_colours.remove(colour)
            used_vertices.remove(nxt)
            path.pop()
        return False

    return tuple(path) if visit() else None


def edge_ports(owner_path: tuple[int, ...]) -> list[tuple[int, int]]:
    ports = []
    for old, new in zip(owner_path, owner_path[1:]):
        departure = (old & ~new).bit_length() - 1
        arrival = (new & ~old).bit_length() - 1
        assert departure >= 0 and arrival >= 0
        ports.append((departure, arrival))
    return ports


def port_conflict_intervals(owner_path: tuple[int, ...]) -> list[tuple[int, int]]:
    """Return all exact FIFO conflicts, plus intervals enforcing row length."""

    ports = edge_ports(owner_path)
    tokens: list[tuple[int, int, int]] = []
    for edge, (departure, arrival) in enumerate(ports):
        tokens.append((edge % N_GROUND, departure, edge))
        tokens.append(((edge + RANK) % N_GROUND, arrival, edge))

    intervals: set[tuple[int, int]] = set()
    for left in range(len(tokens)):
        phase_x, label_x, edge_x = tokens[left]
        for right in range(left + 1, len(tokens)):
            phase_y, label_y, edge_y = tokens[right]
            if edge_x == edge_y:
                continue
            # Same phase requires the same label; distinct phases require
            # distinct labels.  Failure of either implication is a conflict.
            if (phase_x == phase_y) != (label_x == label_y):
                intervals.add((min(edge_x, edge_y), max(edge_x, edge_y)))

    # A simple path fragment in one n-cycle has at most n-1 retained edges.
    for first in range(len(ports) - N_GROUND + 1):
        intervals.add((first, first + N_GROUND - 1))
    return sorted(intervals, key=lambda interval: (interval[1], interval[0]))


def minimum_fifo_blocks(owner_path: tuple[int, ...]) -> int:
    """Exact interval-transversal number plus one, by right-endpoint greedy."""

    cuts: list[int] = []
    last_cut = -1
    for left, right in port_conflict_intervals(owner_path):
        if last_cut < left:
            last_cut = right
            cuts.append(last_cut)
    return len(cuts) + 1


def canonical_cycle_key(cycle: tuple[int, ...]) -> tuple[int, ...]:
    rev = cycle[::-1]
    candidates = [cycle[i:] + cycle[:i] for i in range(len(cycle))]
    candidates += [rev[i:] + rev[:i] for i in range(len(rev))]
    return min(candidates)


def theorem_41_openings(lower_cycle: tuple[int, ...]) -> list[tuple[int, ...]]:
    owners = tuple(
        lower_cycle[i] | lower_cycle[(i + 1) % len(lower_cycle)]
        for i in range(len(lower_cycle))
    )
    unused = TRIPLES - set(owners)
    openings = []
    for new_owner in unused:
        for cut, colour in enumerate(lower_cycle):
            if colour & ~new_owner:
                continue
            # Delete owners[cut-1]--owners[cut] and attach new_owner to
            # owners[cut-1].  The displayed orientation traverses the opened
            # old cycle in reverse; reversal does not change FIFO eligibility.
            openings.append(
                (new_owner,)
                + tuple(owners[(cut - 1 - step) % len(owners)] for step in range(len(owners)))
            )
    return openings


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seeds", type=int, default=2_000)
    args = parser.parse_args()

    seen: set[tuple[int, ...]] = set()
    best_block_histogram: Counter[int] = Counter()
    opening_histogram: Counter[int] = Counter()
    for seed in range(args.seeds):
        cycle = random_rainbow_pair_cycle(seed)
        if cycle is None:
            continue
        key = canonical_cycle_key(cycle)
        if key in seen:
            continue
        seen.add(key)
        values = [minimum_fifo_blocks(path) for path in theorem_41_openings(cycle)]
        for value in values:
            opening_histogram[value] += 1
        best_block_histogram[min(values)] += 1

    print(f"distinct sampled cycles: {len(seen)}")
    print("best opening per cycle:", dict(sorted(best_block_histogram.items())))
    print("all openings:", dict(sorted(opening_histogram.items())))
    print("desired number of rows: 5")


if __name__ == "__main__":
    main()
