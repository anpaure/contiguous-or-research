#!/usr/bin/env python3
"""Classify inherited and seam-created q=2 defects of the D5 bank.

Substantive execution belongs on H100.  The analysis rebuilds both projected
owner chronologies before and after the frozen 41-circuit toggle.  Every bad
adjacent-transition window is classified by whether zero, one, or two of its
two suppressed-label edges changed.  It also audits endpoint-role reuse for
prospective common-history source cuts.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import search_t2_cross_suffix_alternating_cycles_20260813 as base  # noqa:E402
from audit_t2_cross_suffix_c16_full_ml_topology_20260813 import (  # noqa:E402
    lifted_edges,
)
from verify_t2_c16_suffix_component_residence_20260813 import (  # noqa:E402
    projected_cycles,
    seam_collar_report,
    toggle,
)


def collision_events(edges, owner_rank, ground_size, changed_labels):
    events = set()
    bad_windows = set()
    category_events = Counter()
    category_windows = Counter()
    value_events = Counter()
    cycle_count = 0
    for owners, labels in projected_cycles(edges, owner_rank):
        cycle_count += 1
        length = len(owners)
        supports = [
            owners[index] ^ owners[(index + 1) % length]
            for index in range(length)
        ]
        for index, owner in enumerate(owners):
            left_label = labels[index - 1]
            right_label = labels[index]
            repeated = supports[index - 1] & supports[index]
            if not repeated:
                continue
            changed = int(left_label in changed_labels) + int(
                right_label in changed_labels
            )
            category = ("inherited", "one_seam", "two_seams")[changed]
            window = (
                owner,
                min(left_label, right_label),
                max(left_label, right_label),
            )
            bad_windows.add(window)
            category_windows[category] += 1
            while repeated:
                bit = repeated & -repeated
                repeated -= bit
                coordinate = bit.bit_length() - 1
                value = int(bool(owner & bit))
                event = window + (coordinate, value)
                events.add(event)
                category_events[category] += 1
                value_events[(category, value)] += 1
    assert sum(category_windows.values()) == len(bad_windows)
    assert sum(category_events.values()) == len(events)
    return {
        "cycle_count": cycle_count,
        "events": events,
        "bad_windows": bad_windows,
        "category_events": category_events,
        "category_windows": category_windows,
        "value_events": value_events,
    }


def histogram(counter):
    return dict(sorted(counter.items(), key=lambda item: str(item[0])))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("selection")
    args = parser.parse_args()
    raw = Path(args.selection).read_bytes()
    data = json.loads(raw)
    assert data["status"] == "SAT" and len(data["selection"]) == 41

    m, n = 11, 22
    suffixes = list(base.dyck_words(5))
    canonical = base.canonical_edges(m)
    post = set(canonical)
    base.apply_t2(post, suffixes)
    by_owner, by_colour = base.factor_maps(post)

    cycles = []
    changed_lower_labels = set()
    changed_upper_labels = set()
    upper_untouched_mates = Counter()
    lower_changed_roles = Counter()
    lower_external_roles = Counter()
    role_rows = []
    for item in data["selection"]:
        candidate = item["candidate"]
        owners = tuple(base.bits(word) for word in candidate["owners"])
        colours = tuple(
            base.bits(word) for word in candidate["new_colours"]
        )
        rows = [
            (owners[index], colours[index - 1], colours[index])
            for index in range(len(owners))
        ]
        removed_owner = {old: owner for owner, old, _ in rows}
        assert len(removed_owner) == len(rows)
        cycles.append(rows)
        changed_lower_labels.update(owners)
        changed_upper_labels.update(colours)
        for owner, old, new in rows:
            other = next(colour for colour in by_owner[owner] if colour != old)
            old_external = next(x for x in by_colour[old] if x != owner)
            new_external = next(
                x for x in by_colour[new] if x != removed_owner[new]
            )
            upper_untouched_mates[other] += 1
            lower_changed_roles[owner] += 1
            lower_external_roles[old_external] += 1
            lower_external_roles[new_external] += 1
            role_rows.append({
                "edge_index": item["edge_index"],
                "owner": base.bitword(owner, n),
                "old_external": base.bitword(old_external, n),
                "new_external": base.bitword(new_external, n),
                "upper_untouched_mate": base.bitword(other, n),
            })

    simultaneous = toggle(post, cycles)
    before_edges = lifted_edges(post, canonical, n)
    after_edges = lifted_edges(simultaneous, canonical, n)
    shores = {}
    for name, owner_rank, changed in (
        ("upper", m + 1, changed_lower_labels),
        ("lower", m, changed_upper_labels),
    ):
        before = collision_events(before_edges, owner_rank, n + 1, set())
        after = collision_events(after_edges, owner_rank, n + 1, changed)
        inherited = {
            event for event in after["events"]
            if event[1] not in changed and event[2] not in changed
        }
        assert inherited <= before["events"]
        new_events = after["events"] - before["events"]
        resolved_events = before["events"] - after["events"]
        marked = seam_collar_report(
            after_edges,
            owner_rank,
            (
                (lambda label, pair: label in changed_lower_labels)
                if name == "upper"
                else (lambda label, pair: label in changed_upper_labels)
            ),
            n + 1,
        )
        marked_events_with_multiplicity = sum(
            len(seam["collisions"]) for seam in marked["seams"]
        )
        shores[name] = {
            "changed_transition_labels": len(changed),
            "before_cycles": before["cycle_count"],
            "after_cycles": after["cycle_count"],
            "before_bad_windows": len(before["bad_windows"]),
            "after_bad_windows": len(after["bad_windows"]),
            "before_collision_events": len(before["events"]),
            "after_collision_events": len(after["events"]),
            "after_window_categories": histogram(after["category_windows"]),
            "after_event_categories": histogram(after["category_events"]),
            "after_event_category_values": {
                f"{category}:value{value}": count
                for (category, value), count in sorted(
                    after["value_events"].items()
                )
            },
            "literal_inherited_events_retained": len(inherited),
            "new_collision_events": len(new_events),
            "resolved_collision_events": len(resolved_events),
            "marked_bad_seam_labels": sum(
                bool(seam["collisions"]) for seam in marked["seams"]
            ),
            "marked_collision_events_with_multiplicity": (
                marked_events_with_multiplicity
            ),
            "minimum_marked_seam_gap": min(marked["seam_gaps"]),
        }

    print(json.dumps({
        "status": "PASS",
        "selection_sha256": hashlib.sha256(raw).hexdigest(),
        "selected_circuits": len(cycles),
        "selected_rows": sum(map(len, cycles)),
        "shores": shores,
        "prospective_common_history_roles": {
            "distinct_changed_lower_owners": len(lower_changed_roles),
            "maximum_changed_lower_owner_multiplicity": max(
                lower_changed_roles.values()
            ),
            "distinct_lower_external_owners": len(lower_external_roles),
            "lower_external_owner_multiplicity_histogram": histogram(
                Counter(lower_external_roles.values())
            ),
            "maximum_lower_external_owner_multiplicity": max(
                lower_external_roles.values()
            ),
            "distinct_upper_untouched_mates": len(upper_untouched_mates),
            "upper_untouched_mate_multiplicity_histogram": histogram(
                Counter(upper_untouched_mates.values())
            ),
            "maximum_upper_untouched_mate_multiplicity": max(
                upper_untouched_mates.values()
            ),
        },
        "role_rows": role_rows,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
