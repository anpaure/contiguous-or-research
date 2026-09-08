#!/usr/bin/env python3
"""Finite audit of the balanced first-UHD two-seam Dyck atom."""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict

from audit_dyck_tail_seam_automaton_20260822 import (
    BITS,
    canonical_path,
    dyck_words,
    macro,
    rank_map,
    rho,
    unmacro,
)


def first_uhd(path: str) -> int | None:
    return next(
        (
            i + 1
            for i in range(len(path) - 2)
            if path[i] == "U" and path[i + 1] in {"A", "B"} and path[i + 2] == "D"
        ),
        None,
    )


def lift(path: tuple[frozenset[int], ...], r: int):
    ground = frozenset(range(1, 2 * r + 1))
    anchor = 2 * r + 1
    answer = [path[0]]
    for left, right in zip(path, path[1:]):
        answer.extend((frozenset({anchor}) | (ground - (left | right)), right))
    return tuple(answer)


def edge_holes(cycle: tuple[frozenset[int], ...], r: int):
    ground = frozenset(range(1, 2 * r + 2))
    answer = []
    for left, right in zip(cycle, cycle[1:] + cycle[:1]):
        assert not (left & right)
        hole = ground - left - right
        assert len(hole) == 1
        answer.append(next(iter(hole)))
    return tuple(answer)


def cycle_from_hole_permutation(holes: tuple[int, ...]):
    """The unique shortest odd-graph cycle with the prescribed holes."""
    b = len(holes)
    r = (b - 1) // 2
    assert b == 2 * r + 1 and len(set(holes)) == b
    vertices = tuple(
        frozenset(holes[(i + 2 * j + 1) % b] for j in range(r))
        for i in range(b)
    )
    assert edge_holes(vertices, r) == holes
    return vertices


def cyclic_windows(row: tuple[int, ...], length: int):
    return tuple(
        frozenset(row[(i + j) % len(row)] for j in range(length))
        for i in range(len(row))
    )


def edge_multiset(walk: tuple[frozenset[int], ...]):
    return Counter(
        frozenset((left, right))
        for left, right in zip(walk, walk[1:] + walk[:1])
    )


def audit(r: int):
    pair_count = 0
    unmatched = 0
    phase_ledger = Counter()
    distance_ledger = Counter()
    fifo_ledger = Counter()
    template_ledger = Counter()
    cross_splice_ledger = Counter()

    for peak in dyck_words(r):
        encoded = macro(peak)
        location = first_uhd(encoded)
        if location is None:
            unmatched += 1
            continue
        if encoded[location] == "B":
            continue
        pair_count += 1
        valley_code = encoded[:location] + "B" + encoded[location + 1 :]
        valley = unmacro(valley_code)
        assert first_uhd(valley_code) == location

        changed = [i + 1 for i, (x, y) in enumerate(zip(peak, valley)) if x != y]
        u, v = changed
        ranks_p, ranks_q = rank_map(peak), rank_map(valley)
        seam_ii = next(
            t
            for t in range(1, r + 1)
            if (
                ranks_p[u] - t,
                ranks_p[v] - t,
                ranks_q[u] - t,
                ranks_q[v] - t,
            )
            == (0, 1, 0, 1)
        )
        seam_i = next(
            t
            for t in range(1, r + 1)
            if (
                ranks_p[u] - t,
                ranks_p[v] - t,
                ranks_q[u] - t,
                ranks_q[v] - t,
            )
            == (-1, 0, -1, 0)
        )
        assert seam_i == seam_ii + 1

        pairs_p = tuple(zip(rho(peak)[::2], rho(peak)[1::2]))
        pairs_q = tuple(zip(rho(valley)[::2], rho(valley)[1::2]))
        s = seam_ii - 1
        assert pairs_p[:s] == pairs_q[:s]
        assert pairs_p[seam_i:] == pairs_q[seam_i:]
        c, pu = pairs_p[s]
        pv, z = pairs_p[s + 1]
        assert (pu, pv) == (u, v)
        assert pairs_q[s : s + 2] == ((u, z), (c, v))
        template_ledger[(seam_ii, c, z)] += 1

        path_p, path_q = canonical_path(peak), canonical_path(valley)
        first = path_p[:seam_ii] + path_q[seam_ii:]
        second = path_q[:seam_i] + path_p[seam_i:]
        phase_bad = tuple(
            t
            for t in range(r + 1)
            if Counter((first[t], second[t])) != Counter((path_p[t], path_q[t]))
        )
        assert phase_bad == (seam_ii,)
        phase_ledger[phase_bad] += 1

        cycle = lift(first, r) + lift(second, r)
        holes = edge_holes(cycle, r)
        loads = Counter(holes)
        assert set(loads.values()) == {2}
        positions = defaultdict(list)
        for index, label in enumerate(holes):
            positions[label].append(index)
        distances = {
            label: min(
                (right - left) % (2 * (2 * r + 1)),
                (left - right) % (2 * (2 * r + 1)),
            )
            for label, (left, right) in positions.items()
        }
        assert distances[u] == distances[v] == 3
        assert all(distance == 2 * r + 1 for label, distance in distances.items() if label not in {u, v})
        distance_ledger[tuple(sorted(Counter(distances.values()).items()))] += 1

        insertions, removals = holes[::2], holes[1::2]
        assert len(set(insertions)) == len(set(removals)) == 2 * r + 1
        removal_position = {label: index for index, label in enumerate(removals)}
        delays = {
            label: (removal_position[label] - index) % (2 * r + 1)
            for index, label in enumerate(insertions)
        }
        assert sum(delay != r for delay in delays.values()) == 2
        assert sorted(delay for delay in delays.values() if delay != r) == [1, 2 * r - 1]
        fifo_ledger[tuple(sorted(Counter(delays.values()).items()))] += 1

        # Exact internal resolution of the two ports.  The two length-b
        # halves have respectively v and u duplicated.  Cross the second
        # occurrences to obtain two rainbow hole permutations.
        b = 2 * r + 1
        first_holes = list(holes[:b])
        second_holes = list(holes[b:])
        first_ports = [i for i, label in enumerate(first_holes) if label == v]
        second_ports = [i for i, label in enumerate(second_holes) if label == u]
        assert len(first_ports) == len(second_ports) == 2
        assert first_ports == second_ports
        first_holes[first_ports[1]] = u
        second_holes[second_ports[1]] = v
        first_holes = tuple(first_holes)
        second_holes = tuple(second_holes)
        assert set(first_holes) == set(second_holes) == set(range(1, b + 1))

        first_cycle = cycle_from_hole_permutation(first_holes)
        second_cycle = cycle_from_hole_permutation(second_holes)
        assert Counter(cycle) == Counter(first_cycle + second_cycle)
        assert edge_multiset(cycle) == edge_multiset(first_cycle) + edge_multiset(second_cycle)

        # The second cycle is canonical Q.  The first differs from canonical
        # P by two disjoint adjacent transpositions in cyclic row order.
        canonical_p_holes = rho(peak) + (b,)
        canonical_q_holes = rho(valley) + (b,)
        assert second_holes == canonical_q_holes
        canonical_p_cycle = cycle_from_hole_permutation(canonical_p_holes)
        canonical_q_cycle = cycle_from_hole_permutation(canonical_q_holes)
        difference = Counter(first_cycle + second_cycle)
        difference.subtract(Counter(canonical_p_cycle + canonical_q_cycle))
        positive = sum(value for value in difference.values() if value > 0)
        negative = -sum(value for value in difference.values() if value < 0)
        assert positive == negative == 3

        canonical_p_row = tuple(canonical_p_holes[(2 * j) % b] for j in range(b))
        repaired_p_row = tuple(first_holes[(2 * j) % b] for j in range(b))
        changed_positions = [
            j for j, (left, right) in enumerate(zip(canonical_p_row, repaired_p_row))
            if left != right
        ]
        assert len(changed_positions) == 4
        position_edges = {
            frozenset((j, (j + 1) % b))
            for j in changed_positions
            if (j + 1) % b in changed_positions
        }
        assert len(position_edges) == 2
        assert set().union(*position_edges) == set(changed_positions)
        for length in range(1, b):
            old = cyclic_windows(canonical_p_row, length)
            new = cyclic_windows(repaired_p_row, length)
            assert sum(left != right for left, right in zip(old, new)) <= 4
        cross_splice_ledger[(positive, negative)] += 1

    catalan = sum(1 for _ in dyck_words(r))
    assert 2 * pair_count + unmatched == catalan
    return {
        "r": r,
        "Catalan": catalan,
        "pairs": pair_count,
        "unmatched": unmatched,
        "phase_ledgers": dict(phase_ledger),
        "distance_ledgers": dict(distance_ledger),
        "fifo_ledgers": dict(fifo_ledger),
        "cross_splice_ledgers": dict(cross_splice_ledger),
        "template_cases": len(template_ledger),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--r", type=int, nargs="+", default=[4, 5, 6, 7, 8, 9])
    args = parser.parse_args()
    for r in args.r:
        print("DYCK_UHD_TWO_SEAM_ATOM", audit(r), flush=True)


if __name__ == "__main__":
    main()
