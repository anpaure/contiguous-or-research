#!/usr/bin/env python3
"""Census canonical C6/C8 completions for the 212 D5 reset rows.

Run on H100 only.  For every nontrivial three-state row, test whether the
canonical complementary Johnson edge needed by its triangle/square circuit
is selected in the post-T2 factor and census owner/colour reuse.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import search_t2_cross_suffix_alternating_cycles_20260813 as base  # noqa:E402


def jdist(a, b):
    return (a ^ b).bit_count() // 2


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("selection")
    parser.add_argument("certificate")
    args = parser.parse_args()
    selection = json.loads(Path(args.selection).read_text())
    certificate = json.loads(Path(args.certificate).read_text())

    m, n = 11, 22
    selected = set(base.canonical_edges(m))
    base.apply_t2(selected, list(base.dyck_words(5)))
    _, by_colour = base.factor_maps(selected)
    state = {
        base.bits(word): value
        for word, value in certificate["owner_union_graph"][
            "three_state_assignment"
        ]
    }

    records = []
    all_rows = []
    owner_load = Counter()
    colour_load = Counter()
    complementary_selected = 0
    complementary_absent = 0
    for item in selection["selection"]:
        owners = tuple(base.bits(word) for word in item["candidate"]["owners"])
        colours = tuple(base.bits(word) for word in item["candidate"]["new_colours"])
        rows = [
            (owners[index], colours[index - 1], colours[index])
            for index in range(len(owners))
        ]
        all_rows.extend(rows)
    removed = {(tail, old) for tail, old, _ in all_rows}
    added = {(tail, new) for tail, _, new in all_rows}
    assert removed <= selected and not (added & selected)
    switched = (selected - removed) | added

    for item in selection["selection"]:
        owners = tuple(base.bits(word) for word in item["candidate"]["owners"])
        colours = tuple(base.bits(word) for word in item["candidate"]["new_colours"])
        rows = [
            (owners[index], colours[index - 1], colours[index])
            for index in range(len(owners))
        ]
        removed_owner = {old: owner for owner, old, _ in rows}
        for tail, old_colour, new_colour in rows:
            old_head = next(o for o in by_colour[old_colour] if o != tail)
            new_head = next(
                o for o in by_colour[new_colour] if o != removed_owner[new_colour]
            )
            if state[old_head] == state[new_head]:
                continue
            distance = jdist(old_head, new_head)
            assert distance in (1, 2)
            if distance == 2:
                removed_old = tail & ~old_head
                inserted_old = old_head & ~tail
                removed_new = tail & ~new_head
                inserted_new = new_head & ~tail
                assert all(x.bit_count() == 1 for x in (
                    removed_old, inserted_old, removed_new, inserted_new
                ))
                core = tail & old_head & new_head
                dummy = core | inserted_old | inserted_new
                assert dummy.bit_count() == m
                complementary_colour = dummy | new_head
                assert complementary_colour.bit_count() == m + 1
                required_old = (dummy, complementary_colour)
                required_new_colour = dummy | old_head
                old_edge_selected = (
                    (dummy, complementary_colour) in selected
                    and (new_head, complementary_colour) in selected
                )
                new_edge_selected = (
                    (dummy, required_new_colour) in switched
                    and (old_head, required_new_colour) in switched
                )
            else:
                # Top triangle: all three owners share one lower facet and
                # have three distinct upper pair-unions.  The complementary
                # old incidence is the unique old-factor incidence of the
                # third owner at the third triangle colour, if present.
                common = tail & old_head & new_head
                assert common.bit_count() == m - 1
                dummy = new_head
                complementary_colour = old_head | new_head
                required_old = (new_head, complementary_colour)
                required_new_colour = tail | new_head
                old_edge_selected = (
                    (new_head, complementary_colour) in selected
                    and (old_head, complementary_colour) in selected
                )
                new_edge_selected = (
                    (new_head, required_new_colour) in switched
                    and (tail, required_new_colour) in switched
                )

            if required_old in selected:
                complementary_selected += 1
            else:
                complementary_absent += 1
            owner_load[dummy] += 1
            colour_load[complementary_colour] += 1
            records.append({
                "distance": distance,
                "required_old_selected": required_old in selected,
                "required_new_absent": (dummy, required_new_colour) not in selected,
                "old_complementary_edge_selected": old_edge_selected,
                "new_complementary_edge_selected": new_edge_selected,
            })

    histogram = Counter(
        (r["distance"], r["required_old_selected"], r["required_new_absent"])
        for r in records
    )
    edge_histogram = Counter(
        (
            r["distance"],
            r["old_complementary_edge_selected"],
            r["new_complementary_edge_selected"],
        )
        for r in records
    )
    print(json.dumps({
        "status": "PASS",
        "rows": len(records),
        "histogram": {str(key): value for key, value in sorted(histogram.items())},
        "complete_edge_histogram": {
            str(key): value for key, value in sorted(edge_histogram.items())
        },
        "complementary_selected": complementary_selected,
        "complementary_absent": complementary_absent,
        "distinct_dummy_owners": len(owner_load),
        "dummy_owner_max_load": max(owner_load.values()),
        "dummy_owner_load_histogram": dict(sorted(Counter(owner_load.values()).items())),
        "distinct_complementary_colours": len(colour_load),
        "complementary_colour_max_load": max(colour_load.values()),
        "complementary_colour_load_histogram": dict(
            sorted(Counter(colour_load.values()).items())
        ),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
