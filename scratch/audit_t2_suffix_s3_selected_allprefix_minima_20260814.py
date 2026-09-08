#!/usr/bin/env python3
"""Audit the selected D_3 actuator lengths over all six T2 prefix channels.

Substantive execution belongs on H100.  For each of the four frozen D_3
suffix-tree circuits, the frozen witness supplies an incumbent.  This audit
exhausts every shorter internal-owner, owner/colour-simple alternating circuit
through the corresponding endpoint owners in every T2 prefix channel.
"""

from __future__ import annotations

import json
import sys
from collections import Counter, deque
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import search_t2_cross_suffix_alternating_cycles_20260813 as base  # noqa:E402
from verify_t2_suffix_s3_actuator_catalogue_20260813 import (  # noqa:E402
    CATALOGUE,
    integer_rows,
)


def main():
    m, n = 9, 18
    suffixes = list(base.dyck_words(3))
    selected = base.canonical_edges(m)
    base.apply_t2(selected, suffixes)
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
    for item in CATALOGUE:
        left, right = item["suffix_edge"]
        rows = integer_rows(item)
        incumbent = len(rows)
        assert all(owner in internal for owner, _, _ in rows)
        witness_owners = tuple(owner for owner, _, _ in rows)
        witness_colours = tuple(new for _, _, new in rows)
        _, witness_losses, _ = base.q2_current(
            (witness_owners, witness_colours), by_owner, loads
        )
        assert not witness_losses

        prefix_reports = []
        for prefix, _, _ in base.T2:
            a = base.bits(prefix) | (base.bits(left) << 12)
            b = base.bits(prefix) | (base.bits(right) << 12)
            assert a in internal and b in internal
            distance_b = distances_to(b, incumbent)
            distance_a = distances_to(a, incumbent)
            bound = distance_b[a] + distance_a[b]
            checked = 0
            shorter_safe = None
            for total_length in range(bound, incumbent):
                found = False
                for forward_length in range(
                    distance_b[a], total_length - distance_a[b] + 1
                ):
                    reverse_length = total_length - forward_length
                    forward = exact_paths(a, b, forward_length, distance_b)
                    reverse = exact_paths(b, a, reverse_length, distance_a)
                    for first in forward:
                        for second in reverse:
                            cycle = base.combine_cycle(first, second)
                            if cycle is None:
                                continue
                            checked += 1
                            _, losses, _ = base.q2_current(
                                cycle, by_owner, loads
                            )
                            if not losses:
                                shorter_safe = 2 * total_length
                                found = True
                                break
                        if found:
                            break
                    if found:
                        break
                if found:
                    break
            assert shorter_safe is None, (left, right, prefix, shorter_safe)
            prefix_reports.append({
                "prefix": prefix,
                "directed_distance_incidence_bound": 2 * bound,
                "shorter_label_simple_cycles_checked": checked,
                "shorter_q2_safe_incidence_length": shorter_safe,
            })

        reports.append({
            "suffix_edge": [left, right],
            "witness_prefix": item["prefix"],
            "exact_allprefix_internal_owner_minimum": 2 * incumbent,
            "prefixes": prefix_reports,
        })
        print(
            f"c {left} {right}: exact internal-owner C{2 * incumbent}",
            file=sys.stderr,
            flush=True,
        )

    print(json.dumps({
        "m": m,
        "status": "PASS",
        "selected_edges": reports,
        "exact_minimum_histogram": dict(sorted(Counter(
            row["exact_allprefix_internal_owner_minimum"]
            for row in reports
        ).items())),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
