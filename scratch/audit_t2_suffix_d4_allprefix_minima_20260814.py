#!/usr/bin/env python3
"""Audit shortest q2-safe actuator lengths on all D_4 edges/all T2 prefixes.

Substantive execution belongs on H100.  For every suffix transposition edge
and every one of the six T2 prefix owners, exhaust directed path-length sums
from the exchange-distance bound through the first q2-safe simple circuit.
"""

from __future__ import annotations

import json
import sys
from collections import Counter, deque
from itertools import combinations
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import search_t2_cross_suffix_alternating_cycles_20260813 as base  # noqa:E402


def main():
    m, n = 10, 20
    suffixes = list(base.dyck_words(4))
    suffix_edges = [
        (left, right)
        for left, right in combinations(suffixes, 2)
        if (base.bits(left) ^ base.bits(right)).bit_count() == 2
    ]
    certificate_path = Path(
        sys.argv[1] if len(sys.argv) > 1 else "d4_spanning_actuator.out"
    )
    certificate = json.loads(certificate_path.read_text(encoding="utf-8"))
    two_prefix_minimum = {
        tuple(row["suffix_edge"]): row["shortest_q2_safe_incidence_length"] // 2
        for row in certificate["edge_minimums"]
    }
    selected = base.canonical_edges(m)
    base.apply_t2(selected, suffixes)
    by_owner, by_colour = base.factor_maps(selected)
    internal = {owner for owner, colours in by_owner.items() if len(colours) == 2}
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
                if predecessor in internal and (predecessor, colour) not in selected:
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
            remainder = length - len(owners) + 1
            if distance.get(owner, 10**9) > remainder:
                return
            if remainder == 0:
                if owner == target:
                    answer.append((owners, colours))
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
    for edge_index, (left, right) in enumerate(suffix_edges):
        prefix_reports = []
        incumbent = two_prefix_minimum[(left, right)]
        # The companion exhaustive search already proves `incumbent` exact
        # for the final two T2 prefix channels.  Audit only whether one of
        # the other four channels has a strictly shorter safe circuit.
        for prefix, _, _ in base.T2[:4]:
            a = base.bits(prefix) | (base.bits(left) << 12)
            b = base.bits(prefix) | (base.bits(right) << 12)
            distance_b = distances_to(b, 16)
            distance_a = distances_to(a, 16)
            lower_bound = distance_b[a] + distance_a[b]
            checked = 0
            shortest = None
            witness = None
            for total_length in range(lower_bound, incumbent):
                found = False
                for forward_length in range(
                    distance_b[a], total_length - distance_a[b] + 1
                ):
                    reverse_length = total_length - forward_length
                    forward = exact_paths(a, b, forward_length, distance_b)
                    reverse = exact_paths(b, a, reverse_length, distance_a)
                    for p in forward:
                        for q in reverse:
                            cycle = base.combine_cycle(p, q)
                            if cycle is None:
                                continue
                            checked += 1
                            _, losses, _ = base.q2_current(
                                cycle, by_owner, loads
                            )
                            if losses:
                                continue
                            owners, colours = cycle
                            shortest = total_length
                            witness = {
                                "owners": [base.bitword(x, n) for x in owners],
                                "new_colours": [
                                    base.bitword(x, n) for x in colours
                                ],
                            }
                            found = True
                            break
                        if found:
                            break
                    if found:
                        break
                if found:
                    break
            prefix_reports.append({
                "prefix": prefix,
                "directed_distance_incidence_bound": 2 * lower_bound,
                "shortest_q2_safe_incidence_length": (
                    None if shortest is None else 2 * shortest
                ),
                "label_simple_cycles_checked_through_witness": checked,
                "witness": witness,
            })
        shorter_lengths = [
            row["shortest_q2_safe_incidence_length"]
            for row in prefix_reports
            if row["shortest_q2_safe_incidence_length"] is not None
        ]
        allprefix_minimum = min(
            [2 * incumbent] + shorter_lengths
        )
        reports.append({
            "suffix_edge": [left, right],
            "two_prefix_certified_minimum": 2 * incumbent,
            "allprefix_shortest_q2_safe_incidence_length": allprefix_minimum,
            "prefixes": prefix_reports,
        })
        print(
            f"c {edge_index}/{len(suffix_edges)} {left} {right}: "
            f"C{allprefix_minimum}",
            file=sys.stderr,
            flush=True,
        )

    print(json.dumps({
        "m": m,
        "edges": reports,
        "allprefix_shortest_histogram": dict(sorted(Counter(
            row["allprefix_shortest_q2_safe_incidence_length"]
            for row in reports
        ).items())),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
