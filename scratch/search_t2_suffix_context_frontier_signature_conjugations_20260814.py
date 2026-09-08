#!/usr/bin/env python3
"""Exhaust all context-frontier coordinate-injection conjugations.

Substantive execution belongs on H100.  Old suffix coordinates retain their
literal relative order under X -> 10X or X -> 1X0.  The two new frontier
coordinates and all twelve old T2-prefix coordinates may otherwise be
arbitrarily reassigned among the fourteen target frontier coordinates,
subject only to carrying the named source endpoint prefix to one of the six
target T2 endpoint prefixes.

Coordinate assignments that act identically on every circuit resource are
quotiented by their complete membership signature.  Enumerating the distinct
signature placements is therefore exactly equivalent to enumerating every
coordinate injection, not a heuristic symmetry reduction.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from itertools import combinations
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import search_t2_cross_suffix_alternating_cycles_20260813 as base  # noqa:E402
from audit_t2_suffix_context_raw_transport_20260814 import (  # noqa:E402
    frozen_actuators,
)


PREFIX_WIDTH = 12
PREFIX_MASK = (1 << PREFIX_WIDTH) - 1


def signature_assignments(counter, positions):
    """Yield maps signature -> chosen position tuple for a multiset."""
    classes = list(counter.items())

    def rec(index, remaining, assignment):
        if index + 1 == len(classes):
            signature, count = classes[index]
            if len(remaining) == count:
                yield dict(assignment, **{str(signature): tuple(remaining)})
            return
        signature, count = classes[index]
        for chosen in combinations(remaining, count):
            chosen_set = set(chosen)
            rest = tuple(pos for pos in remaining if pos not in chosen_set)
            assignment[str(signature)] = tuple(chosen)
            yield from rec(index + 1, rest, assignment)
            del assignment[str(signature)]

    if not classes:
        yield {}
    else:
        yield from rec(0, tuple(positions), {})


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "certificate",
        nargs="?",
        default="search_t2_suffix_d4_spanning_actuator_sat_20260813.h100.out",
    )
    parser.add_argument("--source-s", type=int, choices=(3, 4), required=True)
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
    post = base.canonical_edges(target_m)
    base.apply_t2(post, list(base.dyck_words(target_s)))
    by_owner, _ = base.factor_maps(post)
    loads = Counter(
        colours[0] | colours[1]
        for colours in by_owner.values() if len(colours) == 2
    )
    prefix_words = [prefix for prefix, _, _ in base.T2]

    reports = []
    for actuator_index, actuator in enumerate(actuators):
        values = [value for row in actuator["rows"] for value in row]
        signature_counter = Counter()
        for coordinate in range(PREFIX_WIDTH):
            signature = sum(
                ((value >> coordinate) & 1) << index
                for index, value in enumerate(values)
            )
            signature_counter[signature] += 1
        all_signature = (1 << len(values)) - 1
        zero_signature = 0
        signature_counter[all_signature] += 1  # fixed new up coordinate
        signature_counter[zero_signature] += 1  # unused new down coordinate

        endpoint_value = base.bits(actuator["prefix"]) | (
            base.bits(actuator["suffix_edge"][0]) << PREFIX_WIDTH
        )
        endpoint_indices = [
            index for index, value in enumerate(values) if value == endpoint_value
        ]
        assert endpoint_indices
        endpoint_index = endpoint_indices[0]
        up_counter = Counter({
            signature: count
            for signature, count in signature_counter.items()
            if signature >> endpoint_index & 1
        })
        down_counter = signature_counter - up_counter
        assert sum(up_counter.values()) == sum(down_counter.values()) == 7

        for context in ("10", "wrap"):
            if context == "10":
                frontier = tuple(range(14))
                suffix_shift = 2
                suffix_map = lambda word: "10" + word
            else:
                frontier = tuple(range(13)) + (target_n - 1,)
                suffix_shift = 1
                suffix_map = lambda word: "1" + word + "0"
            suffix_parts = []
            for value in values:
                suffix = value >> PREFIX_WIDTH
                suffix_parts.append(suffix << (PREFIX_WIDTH + suffix_shift))

            for target_prefix in prefix_words:
                target_prefix_bits = base.bits(target_prefix)
                target_up = tuple(
                    position for position in frontier
                    if (
                        (position < PREFIX_WIDTH
                         and target_prefix_bits >> position & 1)
                        or position == PREFIX_WIDTH
                    )
                )
                target_down = tuple(
                    position for position in frontier if position not in target_up
                )
                assert len(target_up) == len(target_down) == 7

                up_assignments = list(signature_assignments(up_counter, target_up))
                down_assignments = list(
                    signature_assignments(down_counter, target_down)
                )
                distinct_images = 0
                selection_valid = 0
                q2_safe = 0
                witness = None
                for up_assignment in up_assignments:
                    for down_assignment in down_assignments:
                        distinct_images += 1
                        assignment = dict(up_assignment)
                        assignment.update(down_assignment)
                        mapped_values = list(suffix_parts)
                        for signature, count in signature_counter.items():
                            positions = assignment[str(signature)]
                            assert len(positions) == count
                            for position in positions:
                                bits = signature
                                while bits:
                                    bit = bits & -bits
                                    bits -= bit
                                    mapped_values[bit.bit_length() - 1] |= 1 << position

                        rows = [
                            tuple(mapped_values[3 * index:3 * index + 3])
                            for index in range(len(actuator["rows"]))
                        ]
                        valid = all(
                            (owner, old) in post
                            and (owner, new) not in post
                            and len(by_owner.get(owner, ())) == 2
                            for owner, old, new in rows
                        )
                        if not valid:
                            continue
                        selection_valid += 1
                        owners = tuple(owner for owner, _, _ in rows)
                        new_colours = tuple(new for _, _, new in rows)
                        _, losses, _ = base.q2_current(
                            (owners, new_colours), by_owner, loads
                        )
                        if losses:
                            continue
                        q2_safe += 1
                        witness = {
                            "signature_positions": assignment,
                            "owners": [
                                base.bitword(owner, target_n) for owner in owners
                            ],
                            "new_colours": [
                                base.bitword(colour, target_n)
                                for colour in new_colours
                            ],
                        }
                        break
                    if witness is not None:
                        break

                reports.append({
                    "source_s": source_s,
                    "context": context,
                    "source_suffix_edge": actuator["suffix_edge"],
                    "target_suffix_edge": [
                        suffix_map(word) for word in actuator["suffix_edge"]
                    ],
                    "source_prefix": actuator["prefix"],
                    "target_prefix": target_prefix,
                    "frontier_signature_multiplicities": sorted(
                        signature_counter.values(), reverse=True
                    ),
                    "distinct_coordinate_images_tested": distinct_images,
                    "selection_valid_images": selection_valid,
                    "q2_safe_images": q2_safe,
                    "witness": witness,
                })
                print(
                    f"c {actuator_index}/{len(actuators)} {context} "
                    f"{actuator['prefix']}->{target_prefix} "
                    f"images={distinct_images} selection={selection_valid} "
                    f"q2={q2_safe}",
                    file=sys.stderr,
                    flush=True,
                )

    print(json.dumps({
        "status": "PASS",
        "source_s": source_s,
        "target_s": target_s,
        "reports": reports,
        "summary": {
            context: {
                "phase_pairs_tested": sum(
                    row["context"] == context for row in reports
                ),
                "phase_pairs_with_selection_conjugation": sum(
                    row["context"] == context
                    and row["selection_valid_images"] > 0
                    for row in reports
                ),
                "phase_pairs_with_q2_safe_conjugation": sum(
                    row["context"] == context
                    and row["q2_safe_images"] > 0
                    for row in reports
                ),
                "actuators_with_q2_safe_conjugation": len({
                    tuple(row["source_suffix_edge"])
                    for row in reports
                    if row["context"] == context and row["q2_safe_images"] > 0
                }),
            }
            for context in ("10", "wrap")
        },
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
