#!/usr/bin/env python3
"""Search all bounded T2-prefix permutation corrections to context transport.

Substantive execution belongs on H100.  Suffix coordinates keep their literal
order under X -> 10X or X -> 1X0.  The fixed new up coordinate is inserted as
required by the target Dyck suffix.  On the twelve-coordinate T2 prefix, allow
an arbitrary coordinate permutation carrying the source endpoint prefix to
any of the six T2 endpoint prefixes.  Exhaust all such permutations and test
the complete transported circuit in the exact post-T2 factor.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from itertools import permutations
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import search_t2_cross_suffix_alternating_cycles_20260813 as base  # noqa:E402
from audit_t2_suffix_context_raw_transport_20260814 import (  # noqa:E402
    frozen_actuators,
)


PREFIX_WIDTH = 12
PREFIX_MASK = (1 << PREFIX_WIDTH) - 1


def permute_prefix(value, mapping):
    prefix = value & PREFIX_MASK
    answer = 0
    while prefix:
        bit = prefix & -prefix
        prefix -= bit
        answer |= 1 << mapping[bit.bit_length() - 1]
    return answer


def context_value(value, old_n, mapping, context):
    prefix = permute_prefix(value, mapping)
    suffix = value >> PREFIX_WIDTH
    if context == "10":
        return prefix | (1 << PREFIX_WIDTH) | (suffix << (PREFIX_WIDTH + 2))
    assert context == "wrap"
    return prefix | (1 << PREFIX_WIDTH) | (suffix << (PREFIX_WIDTH + 1))


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
    post = base.canonical_edges(target_m)
    base.apply_t2(post, list(base.dyck_words(target_s)))
    by_owner, _ = base.factor_maps(post)
    loads = Counter(
        colours[0] | colours[1]
        for colours in by_owner.values() if len(colours) == 2
    )

    prefix_words = [prefix for prefix, _, _ in base.T2]
    prefix_bits = {word: base.bits(word) for word in prefix_words}
    reports = []
    for actuator_index, actuator in enumerate(actuators):
        source_prefix = actuator["prefix"]
        source_up = [
            index for index in range(PREFIX_WIDTH)
            if prefix_bits[source_prefix] >> index & 1
        ]
        source_down = [
            index for index in range(PREFIX_WIDTH)
            if not (prefix_bits[source_prefix] >> index & 1)
        ]
        assert len(source_up) == len(source_down) == 6
        for context in ("10", "wrap"):
            suffix_map = (
                (lambda word: "10" + word)
                if context == "10"
                else (lambda word: "1" + word + "0")
            )
            for target_prefix in prefix_words:
                target_up = [
                    index for index in range(PREFIX_WIDTH)
                    if prefix_bits[target_prefix] >> index & 1
                ]
                target_down = [
                    index for index in range(PREFIX_WIDTH)
                    if not (prefix_bits[target_prefix] >> index & 1)
                ]
                tested = 0
                selection_valid = 0
                q2_safe = 0
                witness = None
                for up_image in permutations(target_up):
                    for down_image in permutations(target_down):
                        tested += 1
                        mapping = [None] * PREFIX_WIDTH
                        for old, new in zip(source_up, up_image):
                            mapping[old] = new
                        for old, new in zip(source_down, down_image):
                            mapping[old] = new

                        rows = []
                        valid = True
                        for owner, old, new in actuator["rows"]:
                            mapped = (
                                context_value(owner, old_n, mapping, context),
                                context_value(old, old_n, mapping, context),
                                context_value(new, old_n, mapping, context),
                            )
                            mapped_owner, mapped_old, mapped_new = mapped
                            if (
                                (mapped_owner, mapped_old) not in post
                                or (mapped_owner, mapped_new) in post
                                or len(by_owner.get(mapped_owner, ())) != 2
                            ):
                                valid = False
                                break
                            rows.append(mapped)
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
                            "prefix_coordinate_mapping": mapping,
                            "owners": [
                                base.bitword(owner, 2 * target_m)
                                for owner in owners
                            ],
                            "new_colours": [
                                base.bitword(colour, 2 * target_m)
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
                    "source_prefix": source_prefix,
                    "target_prefix": target_prefix,
                    "permutations_tested": tested,
                    "selection_valid_permutations": selection_valid,
                    "q2_safe_permutations": q2_safe,
                    "witness": witness,
                })
                print(
                    f"c {actuator_index}/{len(actuators)} {context} "
                    f"{source_prefix}->{target_prefix} tested={tested} "
                    f"selection={selection_valid} q2={q2_safe}",
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
                "source_actuators": len(actuators),
                "phase_pairs_tested": sum(
                    row["context"] == context for row in reports
                ),
                "phase_pairs_with_selection_conjugation": sum(
                    row["context"] == context
                    and row["selection_valid_permutations"] > 0
                    for row in reports
                ),
                "phase_pairs_with_q2_safe_conjugation": sum(
                    row["context"] == context
                    and row["q2_safe_permutations"] > 0
                    for row in reports
                ),
                "actuators_with_q2_safe_conjugation": len({
                    tuple(row["source_suffix_edge"])
                    for row in reports
                    if row["context"] == context
                    and row["q2_safe_permutations"] > 0
                }),
            }
            for context in ("10", "wrap")
        },
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
