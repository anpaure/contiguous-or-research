#!/usr/bin/env python3
"""Audit owner/q1/lower-facet/q2 currents of the Catalan T0V tensor.

Substantive execution belongs on H100.  This reconstructs the complete
canonical factor for each requested m, applies every suffix packet, and
compares occurrence Counters.  It also prints the exact base-prefix current
at m=6, from which suffix tensoring follows by adjoining U(V).
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict

import audit_msw_t0v_tensor_residence_20260814 as base


def maps(selected):
    by_owner = defaultdict(list)
    by_colour = defaultdict(list)
    for owner, colour in selected:
        by_owner[owner].append(colour)
        by_colour[colour].append(owner)
    assert all(len(values) in (1, 2) for values in by_owner.values())
    assert all(len(values) == 2 for values in by_colour.values())
    return by_owner, by_colour


def typed_decks(selected):
    by_owner, by_colour = maps(selected)
    owner = Counter(by_owner.keys())
    upper_q1 = Counter(by_colour.keys())
    lower_q1 = Counter(
        owners[0] & owners[1] for owners in by_colour.values()
    )
    upper_q2 = Counter(
        colours[0] | colours[1]
        for colours in by_owner.values() if len(colours) == 2
    )
    lower_q2 = Counter(
        colours[0] & colours[1]
        for colours in by_owner.values() if len(colours) == 2
    )
    return {
        "owner": owner,
        "upper_q1": upper_q1,
        "lower_q1": lower_q1,
        "upper_q2": upper_q2,
        "lower_q2": lower_q2,
    }


def current(old, new, width):
    keys = set(old) | set(new)
    negatives = []
    positives = []
    for value in sorted(keys):
        delta = new[value] - old[value]
        row = {
            "value": base.bitword(value, width),
            "delta": delta,
            "old_load": old[value],
            "new_load": new[value],
        }
        if delta < 0:
            negatives.append(row)
        elif delta > 0:
            positives.append(row)
    casualties = [row for row in negatives if row["new_load"] == 0]
    return {
        "old_occurrences": sum(old.values()),
        "new_occurrences": sum(new.values()),
        "old_support": len(old),
        "new_support": len(new),
        "negative_values": len(negatives),
        "positive_values": len(positives),
        "negative_occurrences": -sum(row["delta"] for row in negatives),
        "positive_occurrences": sum(row["delta"] for row in positives),
        "support_casualties": casualties,
        "negative_rows": negatives,
        "positive_rows": positives,
    }


def audit(m: int):
    canonical = base.canonical_edges(m)
    old = typed_decks(canonical)
    selected = set(canonical)
    packets, changed_owners = base.apply_tensor(selected, m)
    new = typed_decks(selected)
    reports = {
        name: current(old[name], new[name], 2 * m)
        for name in old
    }
    return {
        "m": m,
        "packets": packets,
        "changed_owners": len(changed_owners),
        "typed_currents": reports,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("m", nargs="+", type=int)
    args = parser.parse_args()
    print(json.dumps({"status": "PASS", "runs": [audit(m) for m in args.m]}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
