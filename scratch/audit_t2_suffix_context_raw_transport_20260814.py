#!/usr/bin/env python3
"""Audit literal T2 suffix-actuator transport under two Catalan contexts.

Substantive execution belongs on H100.  The map ``10`` inserts a fixed
up/down pair immediately after the twelve-coordinate T2 prefix.  The map
``wrap`` replaces a suffix X by 1X0.  Both maps are Boolean-lattice
incidence embeddings (coordinate injection plus one fixed up coordinate).
The audit asks whether they also preserve selection in the exact post-T2
MSW factor, q2 support, and lifted component action.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import search_t2_cross_suffix_alternating_cycles_20260813 as base  # noqa:E402
from audit_t2_cross_suffix_c16_full_ml_topology_20260813 import (  # noqa:E402
    graph_components,
    lifted_edges,
)
from verify_t2_c16_suffix_component_residence_20260813 import (  # noqa:E402
    toggle,
)
from verify_t2_suffix_s3_actuator_catalogue_20260813 import (  # noqa:E402
    CATALOGUE,
    integer_rows,
)


PREFIX_WIDTH = 12


def insert_10(value: int, old_n: int) -> int:
    low_mask = (1 << PREFIX_WIDTH) - 1
    return (
        (value & low_mask)
        | (1 << PREFIX_WIDTH)
        | ((value >> PREFIX_WIDTH) << (PREFIX_WIDTH + 2))
    )


def insert_01_phase(value: int, old_n: int) -> int:
    low_mask = (1 << PREFIX_WIDTH) - 1
    return (
        (value & low_mask)
        | (1 << (PREFIX_WIDTH + 1))
        | ((value >> PREFIX_WIDTH) << (PREFIX_WIDTH + 2))
    )


def primitive_wrap(value: int, old_n: int) -> int:
    low_mask = (1 << PREFIX_WIDTH) - 1
    return (
        (value & low_mask)
        | (1 << PREFIX_WIDTH)
        | ((value >> PREFIX_WIDTH) << (PREFIX_WIDTH + 1))
    )


CONTEXTS = {
    "10": (lambda word: "10" + word, insert_10),
    "01_phase": (lambda word: "01" + word, insert_01_phase),
    "wrap": (lambda word: "1" + word + "0", primitive_wrap),
}


def frozen_actuators(certificate):
    answer = []
    for item in CATALOGUE:
        answer.append({
            "source_s": 3,
            "suffix_edge": list(item["suffix_edge"]),
            "prefix": item["prefix"],
            "rows": integer_rows(item),
        })
    for item in certificate["selection"]:
        owners = tuple(base.bits(word) for word in item["owners"])
        new_colours = tuple(base.bits(word) for word in item["new_colours"])
        rows = [
            (owners[i], new_colours[i - 1], new_colours[i])
            for i in range(len(owners))
        ]
        answer.append({
            "source_s": 4,
            "suffix_edge": item["suffix_edge"],
            "prefix": item["prefix"],
            "rows": rows,
        })
    return answer


def difference_word(actual: int, expected: int, n: int) -> str:
    return base.bitword(actual ^ expected, n)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "certificate",
        nargs="?",
        default="search_t2_suffix_d4_spanning_actuator_sat_20260813.h100.out",
    )
    args = parser.parse_args()
    certificate = json.loads(Path(args.certificate).read_text(encoding="utf-8"))

    reports = []
    factor_cache = {}
    for actuator in frozen_actuators(certificate):
        source_s = actuator["source_s"]
        old_n = 12 + 2 * source_s
        target_s = source_s + 1
        target_m = 6 + target_s
        target_n = 2 * target_m
        if target_s not in factor_cache:
            canonical = base.canonical_edges(target_m)
            post = set(canonical)
            suffixes = list(base.dyck_words(target_s))
            base.apply_t2(post, suffixes)
            by_owner, by_colour = base.factor_maps(post)
            loads = Counter(
                colours[0] | colours[1]
                for colours in by_owner.values() if len(colours) == 2
            )
            components, which = graph_components(
                lifted_edges(post, canonical, target_n)
            )
            factor_cache[target_s] = (
                canonical, post, by_owner, by_colour, loads, components, which
            )
        (
            canonical, post, by_owner, by_colour, loads,
            components, which,
        ) = factor_cache[target_s]

        for context_name, (suffix_map, value_map) in CONTEXTS.items():
            rows = [
                tuple(value_map(value, old_n) for value in row)
                for row in actuator["rows"]
            ]
            row_reports = []
            valid = True
            for index, (owner, old, new) in enumerate(rows):
                selected_at_owner = sorted(by_owner.get(owner, ()))
                old_selected = (owner, old) in post
                new_unselected = (owner, new) not in post
                internal_owner = len(selected_at_owner) == 2
                incidence_legal = owner & ~old == 0 and owner & ~new == 0
                valid &= (
                    old_selected and new_unselected
                    and internal_owner and incidence_legal
                )
                closest_old = None
                if selected_at_owner:
                    closest_old = min(
                        selected_at_owner,
                        key=lambda colour: (colour ^ old).bit_count(),
                    )
                row_reports.append({
                    "row": index,
                    "old_selected": old_selected,
                    "new_unselected": new_unselected,
                    "internal_owner": internal_owner,
                    "incidence_legal": incidence_legal,
                    "selected_degree": len(selected_at_owner),
                    "old_to_closest_selected_distance": (
                        None if closest_old is None
                        else (closest_old ^ old).bit_count()
                    ),
                    "old_to_closest_selected_difference": (
                        None if closest_old is None
                        else difference_word(closest_old, old, target_n)
                    ),
                })

            owners = [owner for owner, _, _ in rows]
            colours = [new for _, _, new in rows]
            simple = len(set(owners)) == len(owners) and len(set(colours)) == len(colours)
            support_losses = None
            component_report = None
            if valid and simple:
                cycle = (owners, colours)
                _, losses, _ = base.q2_current(cycle, by_owner, loads)
                support_losses = len(losses)
                toggled = toggle(post, [rows])
                after, after_which = graph_components(
                    lifted_edges(toggled, canonical, target_n)
                )
                old_components = {which[owner] for owner in owners}
                new_components = {after_which[owner] for owner in owners}
                component_report = {
                    "old_components_met": len(old_components),
                    "new_components_on_touched_owners": len(new_components),
                    "component_reduction": len(components) - len(after),
                    "new_owner_lengths": sorted(
                        len(after[component]) // 2
                        for component in new_components
                    ),
                }

            mapped_suffix_edge = [
                suffix_map(word) for word in actuator["suffix_edge"]
            ]
            reports.append({
                "source_s": source_s,
                "context": context_name,
                "source_suffix_edge": actuator["suffix_edge"],
                "mapped_suffix_edge": mapped_suffix_edge,
                "prefix": actuator["prefix"],
                "incidence_length": 2 * len(rows),
                "literal_transport_valid": valid and simple,
                "q2_support_losses": support_losses,
                "component_action": component_report,
                "failure_counts": {
                    "old_not_selected": sum(
                        not row["old_selected"] for row in row_reports
                    ),
                    "new_already_selected": sum(
                        not row["new_unselected"] for row in row_reports
                    ),
                    "noninternal_owner": sum(
                        not row["internal_owner"] for row in row_reports
                    ),
                    "illegal_incidence": sum(
                        not row["incidence_legal"] for row in row_reports
                    ),
                },
                "rows": row_reports,
            })
            print(
                f"c D{source_s} {context_name} "
                f"{actuator['suffix_edge'][0]} {actuator['suffix_edge'][1]} "
                f"valid={valid and simple}",
                file=sys.stderr,
                flush=True,
            )

    print(json.dumps({
        "status": "PASS",
        "reports": reports,
        "summary": {
            context: {
                "tested": sum(row["context"] == context for row in reports),
                "valid": sum(
                    row["context"] == context
                    and row["literal_transport_valid"]
                    for row in reports
                ),
                "old_not_selected": sum(
                    row["failure_counts"]["old_not_selected"]
                    for row in reports if row["context"] == context
                ),
                "new_already_selected": sum(
                    row["failure_counts"]["new_already_selected"]
                    for row in reports if row["context"] == context
                ),
                "noninternal_owner": sum(
                    row["failure_counts"]["noninternal_owner"]
                    for row in reports if row["context"] == context
                ),
            }
            for context in CONTEXTS
        },
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
