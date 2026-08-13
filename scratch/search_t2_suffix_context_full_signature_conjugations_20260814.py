#!/usr/bin/env python3
"""Exhaust every Boolean coordinate-injection image of frozen context edges.

Substantive execution belongs on H100.  Unlike the frontier-local audit, this
search even permits arbitrary permutation of all old prefix and suffix
coordinates.  The only endpoint constraint is that the two named source
owners map to the two requested target-context owners in one of the six T2
prefix channels.  Complete resource membership signatures quotient exactly
the coordinate permutations that induce the same finite circuit image.
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


def signature_assignments(counter, positions):
    classes = list(counter.items())

    def rec(index, remaining, assignment):
        if index == len(classes):
            if not remaining:
                yield dict(assignment)
            return
        signature, count = classes[index]
        if index + 1 == len(classes):
            if len(remaining) == count:
                assignment[signature] = tuple(remaining)
                yield dict(assignment)
                del assignment[signature]
            return
        for chosen in combinations(remaining, count):
            chosen_set = set(chosen)
            rest = tuple(position for position in remaining if position not in chosen_set)
            assignment[signature] = tuple(chosen)
            yield from rec(index + 1, rest, assignment)
            del assignment[signature]

    yield from rec(0, tuple(positions), {})


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "certificate",
        nargs="?",
        default="search_t2_suffix_d4_spanning_actuator_sat_20260813.h100.out",
    )
    parser.add_argument("--source-s", type=int, choices=(3, 4), required=True)
    parser.add_argument("--actuator-index", type=int)
    parser.add_argument("--context", choices=("10", "wrap"))
    parser.add_argument("--target-prefix-index", type=int)
    args = parser.parse_args()
    certificate = json.loads(Path(args.certificate).read_text(encoding="utf-8"))
    actuators = [
        item for item in frozen_actuators(certificate)
        if item["source_s"] == args.source_s
    ]
    if args.actuator_index is not None:
        assert 0 <= args.actuator_index < len(actuators)
        actuators = [actuators[args.actuator_index]]
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
        left_source = base.bits(actuator["prefix"]) | (
            base.bits(actuator["suffix_edge"][0]) << 12
        )
        right_source = base.bits(actuator["prefix"]) | (
            base.bits(actuator["suffix_edge"][1]) << 12
        )
        left_indices = [i for i, value in enumerate(values) if value == left_source]
        right_indices = [i for i, value in enumerate(values) if value == right_source]
        assert left_indices and right_indices
        left_index, right_index = left_indices[0], right_indices[0]

        signature_counter = Counter()
        for coordinate in range(old_n):
            signature = sum(
                ((value >> coordinate) & 1) << index
                for index, value in enumerate(values)
            )
            signature_counter[signature] += 1
        signature_counter[(1 << len(values)) - 1] += 1
        signature_counter[0] += 1

        source_classes = {}
        for signature, count in signature_counter.items():
            key = (
                (signature >> left_index) & 1,
                (signature >> right_index) & 1,
            )
            source_classes.setdefault(key, Counter())[signature] += count

        contexts = (args.context,) if args.context is not None else ("10", "wrap")
        for context in contexts:
            suffix_map = (
                (lambda word: "10" + word)
                if context == "10"
                else (lambda word: "1" + word + "0")
            )
            left_suffix, right_suffix = map(
                suffix_map, actuator["suffix_edge"]
            )
            target_prefixes = prefix_words
            if args.target_prefix_index is not None:
                assert 0 <= args.target_prefix_index < len(prefix_words)
                target_prefixes = [prefix_words[args.target_prefix_index]]
            for target_prefix in target_prefixes:
                left_target = base.bits(target_prefix) | (
                    base.bits(left_suffix) << 12
                )
                right_target = base.bits(target_prefix) | (
                    base.bits(right_suffix) << 12
                )
                target_positions = {}
                for position in range(target_n):
                    key = (
                        (left_target >> position) & 1,
                        (right_target >> position) & 1,
                    )
                    target_positions.setdefault(key, []).append(position)
                assert {
                    key: sum(counter.values())
                    for key, counter in source_classes.items()
                } == {
                    key: len(positions) for key, positions in target_positions.items()
                }

                class_options = []
                for key in sorted(source_classes):
                    class_options.append((
                        key,
                        signature_assignments(
                            source_classes[key], target_positions[key]
                        ),
                    ))

                distinct_images = 0
                selection_valid = 0
                q2_safe = 0
                witness = None

                def visit_class(index, assignment):
                    nonlocal distinct_images, selection_valid, q2_safe, witness
                    if witness is not None:
                        return
                    if index < len(class_options):
                        _, options = class_options[index]
                        # Recreate the generator after its first consumption.
                        key = sorted(source_classes)[index]
                        for partial in signature_assignments(
                            source_classes[key], target_positions[key]
                        ):
                            assignment.update(partial)
                            visit_class(index + 1, assignment)
                            for signature in partial:
                                del assignment[signature]
                            if witness is not None:
                                return
                        return

                    distinct_images += 1
                    mapped_values = [0] * len(values)
                    for signature, count in signature_counter.items():
                        positions = assignment[signature]
                        assert len(positions) == count
                        for position in positions:
                            bits = signature
                            while bits:
                                bit = bits & -bits
                                bits -= bit
                                mapped_values[bit.bit_length() - 1] |= 1 << position
                    rows = [
                        tuple(mapped_values[3 * row:3 * row + 3])
                        for row in range(len(actuator["rows"]))
                    ]
                    if not all(
                        (owner, old) in post
                        and (owner, new) not in post
                        and len(by_owner.get(owner, ())) == 2
                        for owner, old, new in rows
                    ):
                        return
                    selection_valid += 1
                    owners = tuple(owner for owner, _, _ in rows)
                    new_colours = tuple(new for _, _, new in rows)
                    _, losses, _ = base.q2_current(
                        (owners, new_colours), by_owner, loads
                    )
                    if losses:
                        return
                    q2_safe += 1
                    witness = {
                        "signature_positions": {
                            str(signature): positions
                            for signature, positions in assignment.items()
                        },
                        "owners": [base.bitword(owner, target_n) for owner in owners],
                        "new_colours": [
                            base.bitword(colour, target_n) for colour in new_colours
                        ],
                    }

                visit_class(0, {})
                reports.append({
                    "source_s": source_s,
                    "context": context,
                    "source_suffix_edge": actuator["suffix_edge"],
                    "target_suffix_edge": [left_suffix, right_suffix],
                    "source_prefix": actuator["prefix"],
                    "target_prefix": target_prefix,
                    "full_signature_multiplicities": sorted(
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
                    f"images={distinct_images} selection={selection_valid} q2={q2_safe}",
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
                    row["context"] == context and row["q2_safe_images"] > 0
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
