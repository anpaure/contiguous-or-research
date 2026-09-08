#!/usr/bin/env python3
"""Enumerate all exact-minimum q2-safe circuits on one D5 split-tree edge.

Substantive execution belongs on H100.  The exact minimum length comes from
the two companion all-prefix searches.  This script exhausts every path split
at that length in all six T2 prefix channels, retaining every internal-owner,
owner/colour-simple q2-safe circuit without a candidate cap.
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
    parser.add_argument("extreme_minima")
    parser.add_argument("missing_minima")
    parser.add_argument("--edge-index", type=int, required=True)
    args = parser.parse_args()
    tree = json.loads(Path(args.tree).read_text(encoding="utf-8"))
    extreme = json.loads(Path(args.extreme_minima).read_text(encoding="utf-8"))
    missing = json.loads(Path(args.missing_minima).read_text(encoding="utf-8"))
    edges = tree["tree_edges"]
    assert 0 <= args.edge_index < len(edges)
    edge = edges[args.edge_index]
    key = tuple(sorted(edge["suffix_edge"]))

    minimum_by_edge = {}
    for item in extreme["reports"]:
        minimum_by_edge[tuple(sorted(item["image_suffix_edge"]))] = (
            item["solution"]["incidence_length"]
        )
    for item in missing["reports"]:
        minimum_by_edge[tuple(sorted(item["suffix_edge"]))] = (
            item["solution"]["incidence_length"]
        )
    assert len(minimum_by_edge) == 41
    minimum_owner_length = minimum_by_edge[key] // 2

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
            if distance[owner] >= minimum_owner_length:
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

    left, right = edge["suffix_edge"]
    candidates = {}
    prefix_reports = []
    for prefix, _, _ in base.T2:
        a = base.bits(prefix) | (base.bits(left) << 12)
        b = base.bits(prefix) | (base.bits(right) << 12)
        distance_b = distances_to(b)
        distance_a = distances_to(a)
        bound = distance_b[a] + distance_a[b]
        label_simple = 0
        safe = 0
        if bound <= minimum_owner_length:
            for forward_length in range(
                distance_b[a], minimum_owner_length - distance_a[b] + 1
            ):
                reverse_length = minimum_owner_length - forward_length
                forward = exact_paths(a, b, forward_length, distance_b)
                reverse = exact_paths(b, a, reverse_length, distance_a)
                for first in forward:
                    for second in reverse:
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
                        candidate_key = (tuple(owners), tuple(new_colours))
                        candidates[candidate_key] = {
                            "prefix": prefix,
                            "owners": [
                                base.bitword(owner, n) for owner in owners
                            ],
                            "new_colours": [
                                base.bitword(colour, n) for colour in new_colours
                            ],
                        }
        prefix_reports.append({
            "prefix": prefix,
            "directed_distance_incidence_bound": 2 * bound,
            "label_simple_cycles_at_minimum": label_simple,
            "q2_safe_cycles_at_minimum": safe,
        })
        print(
            f"c edge={args.edge_index} prefix={prefix} bound=C{2 * bound} "
            f"simple={label_simple} safe={safe}",
            file=sys.stderr,
            flush=True,
        )

    assert candidates, (args.edge_index, edge["suffix_edge"])
    print(json.dumps({
        "status": "PASS",
        "edge_index": args.edge_index,
        "edge": edge,
        "minimum_incidence_length": 2 * minimum_owner_length,
        "prefix_reports": prefix_reports,
        "candidates": list(candidates.values()),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
