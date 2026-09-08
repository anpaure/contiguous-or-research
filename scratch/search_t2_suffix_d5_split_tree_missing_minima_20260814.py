#!/usr/bin/env python3
"""Search exact q2-safe minima on the 15 non-D4 edges of the D5 split tree.

Substantive execution belongs on H100.  The input tree is produced by
``build_t2_suffix_d5_first_return_split_tree_20260814.py``.  Every child-D3,
child-D2, and split-bridge edge is exhausted over all six T2 prefix channels
from its directed-distance bound through the first internal-owner,
owner/colour-simple q2-safe circuit.
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
    parser.add_argument("--maximum-owner-length", type=int, default=15)
    args = parser.parse_args()
    tree = json.loads(Path(args.tree).read_text(encoding="utf-8"))
    edges = [
        item for item in tree["tree_edges"] if item["role"] != "child_D4"
    ]
    assert len(edges) == 15

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

    def distances_to(target, maximum):
        distance = {target: 0}
        queue = deque([target])
        while queue:
            owner = queue.popleft()
            if distance[owner] >= maximum:
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

    reports = []
    for edge_index, edge in enumerate(edges):
        left, right = edge["suffix_edge"]
        prefix_data = []
        for prefix, _, _ in base.T2:
            a = base.bits(prefix) | (base.bits(left) << 12)
            b = base.bits(prefix) | (base.bits(right) << 12)
            distance_b = distances_to(b, args.maximum_owner_length)
            distance_a = distances_to(a, args.maximum_owner_length)
            assert a in distance_b and b in distance_a
            prefix_data.append({
                "prefix": prefix,
                "a": a,
                "b": b,
                "distance_b": distance_b,
                "distance_a": distance_a,
                "bound": distance_b[a] + distance_a[b],
            })
        global_bound = min(data["bound"] for data in prefix_data)
        checked = 0
        solution = None
        length_reports = []
        for total_length in range(global_bound, args.maximum_owner_length + 1):
            checked_at_length = 0
            for data in prefix_data:
                if data["bound"] > total_length:
                    continue
                a, b = data["a"], data["b"]
                for forward_length in range(
                    data["distance_b"][a],
                    total_length - data["distance_a"][b] + 1,
                ):
                    reverse_length = total_length - forward_length
                    forward = exact_paths(
                        a, b, forward_length, data["distance_b"]
                    )
                    reverse = exact_paths(
                        b, a, reverse_length, data["distance_a"]
                    )
                    found = False
                    for first in forward:
                        for second in reverse:
                            cycle = base.combine_cycle(first, second)
                            if cycle is None:
                                continue
                            checked += 1
                            checked_at_length += 1
                            _, losses, _ = base.q2_current(
                                cycle, by_owner, loads
                            )
                            if losses:
                                continue
                            owners, new_colours = cycle
                            solution = {
                                "prefix": data["prefix"],
                                "incidence_length": 2 * total_length,
                                "owners": [
                                    base.bitword(owner, n) for owner in owners
                                ],
                                "new_colours": [
                                    base.bitword(colour, n)
                                    for colour in new_colours
                                ],
                            }
                            found = True
                            break
                        if found:
                            break
                    if found:
                        break
                if solution is not None:
                    break
            length_reports.append({
                "incidence_length": 2 * total_length,
                "label_simple_cycles_checked": checked_at_length,
            })
            if solution is not None:
                break

        reports.append({
            "role": edge["role"],
            "child": edge["child"],
            "split_pair": edge["split_pair"],
            "suffix_edge": edge["suffix_edge"],
            "allprefix_directed_distance_incidence_bound": 2 * global_bound,
            "prefix_bounds": {
                data["prefix"]: 2 * data["bound"] for data in prefix_data
            },
            "length_reports": length_reports,
            "label_simple_cycles_checked": checked,
            "solution": solution,
        })
        print(
            f"c {edge_index}/{len(edges)} {edge['role']} {left} {right} "
            f"bound=C{2 * global_bound} "
            f"solution={None if solution is None else solution['incidence_length']}",
            file=sys.stderr,
            flush=True,
        )

    print(json.dumps({
        "status": "PASS",
        "suffix_semilength": 5,
        "reports": reports,
        "summary_by_role": {
            role: {
                "edges": sum(row["role"] == role for row in reports),
                "solved": sum(
                    row["role"] == role and row["solution"] is not None
                    for row in reports
                ),
                "minimum_length_histogram": dict(sorted(Counter(
                    row["solution"]["incidence_length"]
                    for row in reports
                    if row["role"] == role and row["solution"] is not None
                ).items())),
            }
            for role in ("child_D3", "child_D2", "split_bridge")
        },
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
