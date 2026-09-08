#!/usr/bin/env python3
"""Find exact per-prefix minima on one edge of the D5 minimum-SDR core.

Substantive execution belongs on H100.  For one of the three core edges,
each of the six T2 prefix channels is searched independently from its
directed-distance bound upward.  Every q2-safe simple circuit at that
channel's first safe length is retained without a cap.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, deque
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import search_t2_cross_suffix_alternating_cycles_20260813 as base  # noqa:E402


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("tree")
    parser.add_argument("--edge-index", type=int, required=True)
    parser.add_argument("--maximum-owner-length", type=int, default=16)
    parser.add_argument("--prefix-index", type=int)
    parser.add_argument("--candidate-cap", type=int)
    args = parser.parse_args()
    tree = json.loads(Path(args.tree).read_text(encoding="utf-8"))
    assert 0 <= args.edge_index < len(tree["tree_edges"])
    edge = tree["tree_edges"][args.edge_index]
    left, right = edge["suffix_edge"]

    m, n = 11, 22
    selected = base.canonical_edges(m)
    base.apply_t2(selected, list(base.dyck_words(5)))
    by_owner, by_colour = base.factor_maps(selected)
    internal = {
        owner for owner, colours in by_owner.items() if len(colours) == 2
    }
    base.INTERNAL_OWNERS = internal
    loads = Counter(
        colours[0] | colours[1]
        for colours in by_owner.values() if len(colours) == 2
    )

    def reverse_steps(owner):
        for colour in by_owner[owner]:
            remainder = colour
            while remainder:
                bit = remainder & -remainder
                remainder -= bit
                predecessor = colour ^ bit
                if (
                    predecessor in internal
                    and (predecessor, colour) not in selected
                ):
                    yield predecessor, colour

    def distances_to(target):
        distance = {target: 0}
        queue = deque([target])
        while queue:
            owner = queue.popleft()
            if distance[owner] >= args.maximum_owner_length:
                continue
            for predecessor, _ in reverse_steps(owner):
                if predecessor not in distance:
                    distance[predecessor] = distance[owner] + 1
                    queue.append(predecessor)
        return distance

    def exact_paths(start, target, length, distance):
        answer = []

        def rec(owner, owners, colours):
            remainder = length - len(colours)
            if distance.get(owner, 10**9) > remainder:
                return
            if remainder == 0:
                if owner == target:
                    answer.append((tuple(owners), tuple(colours)))
                return
            for next_owner, colour in base.directed_steps(
                owner, n, selected, by_colour
            ):
                if next_owner in owners or colour in colours:
                    continue
                rec(next_owner, owners + [next_owner], colours + [colour])

        rec(start, [start], [])
        return answer

    def streamed_paths(
        start,
        target,
        length,
        distance,
        forbidden_internal=frozenset(),
        forbidden_colours=frozenset(),
    ):
        def rec(owner, owners, colours):
            remainder = length - len(colours)
            if distance.get(owner, 10**9) > remainder:
                return
            if remainder == 0:
                if owner == target:
                    yield tuple(owners), tuple(colours)
                return
            for next_owner, colour in base.directed_steps(
                owner, n, selected, by_colour
            ):
                if colour in colours or colour in forbidden_colours:
                    continue
                if next_owner in owners:
                    continue
                if next_owner != target and next_owner in forbidden_internal:
                    continue
                yield from rec(
                    next_owner,
                    owners + [next_owner],
                    colours + [colour],
                )

        yield from rec(start, [start], [])

    reports = []
    prefix_rows = base.T2
    if args.prefix_index is not None:
        assert 0 <= args.prefix_index < len(base.T2)
        prefix_rows = [base.T2[args.prefix_index]]
    for prefix, _, _ in prefix_rows:
        a = base.bits(prefix) | (base.bits(left) << 12)
        b = base.bits(prefix) | (base.bits(right) << 12)
        distance_b = distances_to(b)
        distance_a = distances_to(a)
        bound = distance_b[a] + distance_a[b]
        solution_length = None
        candidates = {}
        length_reports = []
        for total_length in range(bound, args.maximum_owner_length + 1):
            label_simple = 0
            safe = 0
            found_at_length = {}
            truncated_at_cap = False
            for forward_length in range(
                distance_b[a], total_length - distance_a[b] + 1
            ):
                reverse_length = total_length - forward_length
                if args.candidate_cap is None:
                    forward = exact_paths(a, b, forward_length, distance_b)
                    reverse = exact_paths(b, a, reverse_length, distance_a)
                    pairs = (
                        (first, second)
                        for first in forward for second in reverse
                    )
                else:
                    pairs = (
                        (first, second)
                        for first in streamed_paths(
                            a, b, forward_length, distance_b
                        )
                        for second in streamed_paths(
                            b,
                            a,
                            reverse_length,
                            distance_a,
                            frozenset(first[0][1:-1]),
                            frozenset(first[1]),
                        )
                    )
                for first, second in pairs:
                    cycle = base.combine_cycle(first, second)
                    if cycle is None:
                        continue
                    label_simple += 1
                    _, losses, _ = base.q2_current(
                        cycle, by_owner, loads
                    )
                    if losses:
                        continue
                    safe += 1
                    owners, new_colours = cycle
                    found_at_length[(tuple(owners), tuple(new_colours))] = {
                        "prefix": prefix,
                        "owners": [
                            base.bitword(owner, n) for owner in owners
                        ],
                        "new_colours": [
                            base.bitword(colour, n) for colour in new_colours
                        ],
                    }
                    if (
                        args.candidate_cap is not None
                        and len(found_at_length) >= args.candidate_cap
                    ):
                        truncated_at_cap = True
                        break
                if truncated_at_cap:
                    break
            length_reports.append({
                "incidence_length": 2 * total_length,
                "label_simple_cycles": label_simple,
                "q2_safe_cycles": safe,
                "enumeration_complete": not truncated_at_cap,
            })
            if found_at_length:
                solution_length = 2 * total_length
                candidates = found_at_length
                break
        reports.append({
            "prefix": prefix,
            "directed_distance_incidence_bound": 2 * bound,
            "shortest_q2_safe_incidence_length": solution_length,
            "length_reports": length_reports,
            "candidates": list(candidates.values()),
            "candidate_enumeration_complete_at_solution": (
                solution_length is None
                or length_reports[-1]["enumeration_complete"]
            ),
        })
        print(
            f"c edge={args.edge_index} prefix={prefix} bound=C{2 * bound} "
            f"solution={solution_length} candidates={len(candidates)}",
            file=sys.stderr,
            flush=True,
        )

    print(json.dumps({
        "status": "PASS",
        "edge_index": args.edge_index,
        "edge": edge,
        "maximum_incidence_length": 2 * args.maximum_owner_length,
        "prefixes": reports,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
