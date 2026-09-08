#!/usr/bin/env python3
"""Independent replay of q4/k17 labelled-core cycle schedules.

Run substantively on H100 only.  This file does not import the solver.  It
rebuilds the 72 states and exact transition relation, reads one or more JSON
certificates, and checks every state occurrence, cyclic wrap, multiplicity,
period count, and aggregate frozen type count for all fourteen mixed faces.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import sys
from collections import Counter
from pathlib import Path


CORE = frozenset(range(5))
TYPES = (
    (1, 5, 2, 1),
    (1, 6, 1, 1),
    (2, 5, 1, 1),
    (3, 3, 2, 1),
    (3, 4, 1, 1),
    (4, 3, 1, 1),
    (5, 1, 2, 1),
    (5, 2, 1, 1),
    (6, 1, 1, 1),
)
TYPE_COUNTS = (139, 297, 8, 20, 20, 140, 127, 237, 442)


def partitions(sizes):
    values = tuple(CORE)
    for middle in itertools.combinations(values, sizes[1]):
        middle = frozenset(middle)
        remaining = tuple(x for x in values if x not in middle)
        for old in itertools.combinations(remaining, sizes[2]):
            old = frozenset(old)
            fresh = CORE - middle - old
            assert len(fresh) == sizes[0]
            yield fresh, middle, old


def catalogue():
    states = []
    for type_id, kind in enumerate(TYPES):
        sizes = tuple(value - 1 for value in kind[:3])
        for parts in partitions(sizes):
            states.append((type_id, parts))
    arcs = {
        (i, j)
        for i, old in enumerate(states)
        for j, new in enumerate(states)
        if new[1][1] <= old[1][0] and new[1][2] <= old[1][1]
    }
    assert len(states) == 72
    return states, arcs


def encoded_states(states):
    return [
        {
            "state_id": state_id,
            "type_id": type_id,
            "type": list(TYPES[type_id]),
            "core_classes": [sorted(part) for part in parts],
        }
        for state_id, (type_id, parts) in enumerate(states)
    ]


def check_report(report, states, arcs):
    t = report["t"]
    number10 = 143 - 11 * t
    number11 = 10 * t
    assert report["status"] in ("OPTIMAL", "FEASIBLE")
    assert report["number_period_10"] == number10
    assert report["number_period_11"] == number11
    periods = Counter()
    counts = Counter()
    expanded_cycles = 0
    for row in report["cycle_multiset"]:
        period = row["period"]
        word = tuple(row["state_ids"])
        multiplicity = row["multiplicity"]
        assert period in (10, 11) and len(word) == period
        assert isinstance(multiplicity, int) and multiplicity > 0
        assert all(isinstance(state, int) and 0 <= state < len(states) for state in word)
        assert all((word[i], word[(i + 1) % period]) in arcs for i in range(period))
        periods[period] += multiplicity
        expanded_cycles += multiplicity
        for state in word:
            counts[states[state][0]] += multiplicity
    assert periods == Counter({10: number10, 11: number11}) - Counter({key: 0 for key in (10, 11)})
    assert tuple(counts[i] for i in range(len(TYPES))) == TYPE_COUNTS
    assert sum(period * value for period, value in periods.items()) == 1430
    return {
        "t": t,
        "period_10_cycles": number10,
        "period_11_cycles": number11,
        "expanded_cycles": expanded_cycles,
        "distinct_cycle_words": len(report["cycle_multiset"]),
        "type_counts": list(TYPE_COUNTS),
    }


def main():
    source = Path(sys.argv[1])
    certificate_paths = [Path(value) for value in sys.argv[2:]]
    assert certificate_paths
    source_hash = hashlib.sha256(source.read_bytes()).hexdigest()
    states, arcs = catalogue()
    expected_states = encoded_states(states)
    reports = []
    seen = set()
    certificate_hashes = {}
    for path in certificate_paths:
        raw = path.read_bytes()
        data = json.loads(raw)
        assert data["status"] == "PASS"
        assert data["source_sha256"] == source_hash
        assert data["states"] == expected_states
        assert data["transition_arcs"] == len(arcs)
        assert "no owner-column" in data["scope"]
        assert "rank-seven-pin coupling" in data["scope"]
        certificate_hashes[str(path)] = hashlib.sha256(raw).hexdigest()
        for report in data["reports"]:
            assert report["t"] not in seen
            seen.add(report["t"])
            reports.append(check_report(report, states, arcs))
    assert seen == set(range(14))
    reports.sort(key=lambda item: item["t"])
    print(json.dumps({
        "status": "PASS",
        "scope": (
            "factor-independent labelled-core/type cycle schedules only; "
            "rank-seven representative pins are not present and are not inferred"
        ),
        "source_sha256": source_hash,
        "certificate_sha256": certificate_hashes,
        "states": len(states),
        "transition_arcs": len(arcs),
        "feasible_faces": [item["t"] for item in reports],
        "reports": reports,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
