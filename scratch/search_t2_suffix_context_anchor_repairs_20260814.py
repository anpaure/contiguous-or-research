#!/usr/bin/env python3
"""Repair raw Catalan-context transports by splicing directed anchor paths.

Substantive execution belongs on H100.  A transported alternating circuit
keeps a cyclic list of anchor owners.  Some transported arc colours cease to
be selected at the next anchor.  This search retains every anchor in cyclic
order and replaces only failed arcs by directed exchange paths.  It exhausts
total path length from the sum of directed-distance bounds upward, imposing
global owner/colour simplicity and exact q2 support.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, deque
from itertools import product
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import search_t2_cross_suffix_alternating_cycles_20260813 as base  # noqa:E402
from audit_t2_suffix_context_raw_transport_20260814 import (  # noqa:E402
    frozen_actuators,
    insert_10,
    primitive_wrap,
)


CONTEXTS = {
    "10": (lambda word: "10" + word, insert_10),
    "wrap": (lambda word: "1" + word + "0", primitive_wrap),
}


def compositions(total, lower):
    """Yield tuples summing to total and coordinatewise at least lower."""
    if not lower:
        if total == 0:
            yield ()
        return

    def rec(index, remaining, current):
        if index + 1 == len(lower):
            value = remaining
            if value >= lower[index]:
                yield tuple(current + [value])
            return
        minimum_tail = sum(lower[index + 1:])
        for value in range(lower[index], remaining - minimum_tail + 1):
            yield from rec(index + 1, remaining - value, current + [value])

    yield from rec(0, total, [])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "certificate",
        nargs="?",
        default="search_t2_suffix_d4_spanning_actuator_sat_20260813.h100.out",
    )
    parser.add_argument("--source-s", type=int, choices=(3, 4), required=True)
    parser.add_argument("--maximum-incidence-length", type=int, default=32)
    args = parser.parse_args()
    certificate = json.loads(Path(args.certificate).read_text(encoding="utf-8"))
    actuators = [
        item for item in frozen_actuators(certificate)
        if item["source_s"] == args.source_s
    ]

    source_s = args.source_s
    old_n = 12 + 2 * source_s
    target_s = source_s + 1
    target_m = 6 + target_s
    target_n = 2 * target_m
    suffixes = list(base.dyck_words(target_s))
    post = base.canonical_edges(target_m)
    base.apply_t2(post, suffixes)
    by_owner, by_colour = base.factor_maps(post)
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
                    and (predecessor, colour) not in post
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

    path_cache = {}

    def exact_paths(start, target, length, distance):
        key = (start, target, length)
        if key in path_cache:
            return path_cache[key]
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
                owner, target_n, post, by_colour
            ):
                if next_owner in owners or colour in colours:
                    continue
                rec(next_owner, owners + [next_owner], colours + [colour])

        rec(start, [start], [])
        path_cache[key] = answer
        return answer

    reports = []
    for actuator_index, actuator in enumerate(actuators):
        for context_name, (suffix_map, value_map) in CONTEXTS.items():
            raw_rows = [
                tuple(value_map(value, old_n) for value in row)
                for row in actuator["rows"]
            ]
            anchors = tuple(owner for owner, _, _ in raw_rows)
            raw_colours = tuple(new for _, _, new in raw_rows)
            arc_valid = tuple(
                (anchors[index], raw_colours[index]) not in post
                and (anchors[(index + 1) % len(anchors)], raw_colours[index]) in post
                for index in range(len(anchors))
            )
            broken = tuple(
                index for index, valid in enumerate(arc_valid) if not valid
            )
            distance_maps = {}
            lower_lengths = []
            for index in broken:
                start = anchors[index]
                target = anchors[(index + 1) % len(anchors)]
                distance = distances_to(target, args.maximum_incidence_length // 2)
                assert start in distance, (context_name, actuator["suffix_edge"], index)
                distance_maps[index] = distance
                lower_lengths.append(distance[start])

            fixed_arc_count = len(anchors) - len(broken)
            lower_owner_length = fixed_arc_count + sum(lower_lengths)
            maximum_owner_length = args.maximum_incidence_length // 2
            checked_simple_cycles = 0
            checked_q2_cycles = 0
            solution = None

            for total_owner_length in range(
                lower_owner_length, maximum_owner_length + 1
            ):
                broken_total = total_owner_length - fixed_arc_count
                for path_lengths in compositions(broken_total, lower_lengths):
                    path_options = {}
                    impossible = False
                    for index, length in zip(broken, path_lengths):
                        options = exact_paths(
                            anchors[index],
                            anchors[(index + 1) % len(anchors)],
                            length,
                            distance_maps[index],
                        )
                        if not options:
                            impossible = True
                            break
                        path_options[index] = options
                    if impossible:
                        continue

                    option_groups = [path_options[index] for index in broken]
                    for choices in product(*option_groups):
                        choice_by_arc = dict(zip(broken, choices))
                        cycle_owners = []
                        cycle_colours = []
                        for index in range(len(anchors)):
                            if arc_valid[index]:
                                path_owners = (anchors[index], anchors[(index + 1) % len(anchors)])
                                path_colours = (raw_colours[index],)
                            else:
                                path_owners, path_colours = choice_by_arc[index]
                            cycle_owners.extend(path_owners[:-1])
                            cycle_colours.extend(path_colours)
                        if (
                            len(set(cycle_owners)) != len(cycle_owners)
                            or len(set(cycle_colours)) != len(cycle_colours)
                        ):
                            continue
                        checked_simple_cycles += 1
                        _, losses, _ = base.q2_current(
                            (cycle_owners, cycle_colours), by_owner, loads
                        )
                        checked_q2_cycles += 1
                        if losses:
                            continue
                        solution = {
                            "incidence_length": 2 * len(cycle_owners),
                            "owners": [
                                base.bitword(owner, target_n)
                                for owner in cycle_owners
                            ],
                            "new_colours": [
                                base.bitword(colour, target_n)
                                for colour in cycle_colours
                            ],
                            "broken_arc_path_lengths": {
                                str(index): len(choice_by_arc[index][1])
                                for index in broken
                            },
                        }
                        break
                    if solution is not None:
                        break
                if solution is not None:
                    break

            reports.append({
                "source_s": source_s,
                "context": context_name,
                "source_suffix_edge": actuator["suffix_edge"],
                "mapped_suffix_edge": [
                    suffix_map(word) for word in actuator["suffix_edge"]
                ],
                "prefix": actuator["prefix"],
                "raw_incidence_length": 2 * len(anchors),
                "broken_arcs": list(broken),
                "broken_arc_directed_distances": dict(zip(
                    map(str, broken), lower_lengths
                )),
                "anchor_preserving_incidence_lower_bound": 2 * lower_owner_length,
                "checked_simple_cycles": checked_simple_cycles,
                "checked_q2_cycles": checked_q2_cycles,
                "solution": solution,
            })
            print(
                f"c {actuator_index}/{len(actuators)} {context_name} "
                f"{actuator['suffix_edge'][0]} {actuator['suffix_edge'][1]} "
                f"broken={len(broken)} lower=C{2 * lower_owner_length} "
                f"solution={None if solution is None else solution['incidence_length']}",
                file=sys.stderr,
                flush=True,
            )

    print(json.dumps({
        "status": "PASS",
        "source_s": source_s,
        "target_s": target_s,
        "maximum_incidence_length": args.maximum_incidence_length,
        "reports": reports,
        "summary": {
            context: {
                "tested": sum(row["context"] == context for row in reports),
                "solved": sum(
                    row["context"] == context and row["solution"] is not None
                    for row in reports
                ),
                "solution_length_histogram": dict(sorted(Counter(
                    row["solution"]["incidence_length"]
                    for row in reports
                    if row["context"] == context and row["solution"] is not None
                ).items())),
            }
            for context in CONTEXTS
        },
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
