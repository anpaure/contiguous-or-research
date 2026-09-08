#!/usr/bin/env python3
"""Exact verifier for the two cross-suffix T2 C16 switches.

Substantive runs belong on h100.  The verifier builds the exact m=8
canonical MSW factor, applies both T2 suffix packets 1100 and 1010, proves
the six directed-distance lower bounds, verifies two explicit alternating
C16s, and computes their complete q2 support effect.
"""

from __future__ import annotations

import json
import sys
from collections import Counter, defaultdict, deque
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from search_t2_cross_suffix_alternating_cycles_20260813 import (  # noqa:E402
    T2,
    apply_t2,
    bits,
    bitword,
    canonical_edges,
    directed_steps,
    dyck_words,
    factor_maps,
)


def exchange_dist(start, target, n, selected, by_colour, internal):
    q = deque([(start, 0)])
    seen = {start}
    while q:
        u, d = q.popleft()
        if u not in internal:
            continue
        missing = ((1 << n) - 1) ^ u
        while missing:
            bit = missing & -missing
            missing -= bit
            colour = u | bit
            if (u, colour) in selected:
                continue
            for v in by_colour[colour]:
                if v not in internal:
                    continue
                if v == target:
                    return d + 1
                if v not in seen:
                    seen.add(v)
                    q.append((v, d + 1))
    return None


def mask(xs):
    return sum(1 << x for x in xs)


def explicit_cycle(core, b):
    a, c, x, y, z = 0, 10, 13, 14, 15
    pairs = [
        (a, x), (x, y), (b, y), (a, y),
        (c, y), (c, z), (b, c), (b, x),
    ]
    removed = [
        (a, b, x), (a, x, y), (b, x, y), (a, b, y),
        (a, c, y), (c, y, z), (b, c, z), (b, c, x),
    ]
    added = removed[1:] + removed[:1]
    h = mask(core)
    return [
        (h | mask(pair), h | mask(old), h | mask(new))
        for pair, old, new in zip(pairs, removed, added)
    ]


def q2_rows(cycle, by_owner):
    rows = []
    for owner, removed, added in cycle:
        selected = by_owner[owner]
        assert removed in selected and added not in selected
        other = selected[0] if selected[1] == removed else selected[1]
        rows.append((owner, removed, added, other | removed, other | added))
    return rows


def main():
    m, n = 8, 16
    suffixes = list(dyck_words(2))
    assert suffixes == ["1100", "1010"]

    selected = canonical_edges(m)
    apply_t2(selected, suffixes)
    by_owner, by_colour = factor_maps(selected)
    internal = {o for o, cs in by_owner.items() if len(cs) == 2}
    loads = Counter(cs[0] | cs[1] for cs in by_owner.values() if len(cs) == 2)

    expected_dist = {
        "101010001101": (4, 7),
        "100011001101": (3, 5),
        "100010001111": (3, 5),
        "101011000101": (4, 6),
        "101001010101": (3, 5),
        "101001001101": (3, 5),
    }
    distance_rows = []
    for prefix, _, _ in T2:
        a = bits(prefix) | (bits("1100") << 12)
        b = bits(prefix) | (bits("1010") << 12)
        forward = exchange_dist(a, b, n, selected, by_colour, internal)
        reverse = exchange_dist(b, a, n, selected, by_colour, internal)
        assert (forward, reverse) == expected_dist[prefix]
        distance_rows.append(
            {
                "prefix": prefix,
                "forward": forward,
                "reverse": reverse,
                "minimum_incidence_cycle_length": 2 * (forward + reverse),
            }
        )

    specifications = [
        (4, {2, 5, 7, 9, 11, 12}),
        (6, {2, 5, 8, 9, 11, 12}),
    ]
    all_owners = set()
    all_colours = set()
    total_delta = Counter()
    cycle_reports = []
    toggled = set(selected)
    for b, core in specifications:
        cycle = explicit_cycle(core, b)
        owners = {o for o, _, _ in cycle}
        colours = {x for _, old, new in cycle for x in (old, new)}
        assert len(owners) == len(colours) == 8
        assert not (owners & all_owners)
        assert not (colours & all_colours)
        all_owners |= owners
        all_colours |= colours

        rows = q2_rows(cycle, by_owner)
        delta = Counter()
        for owner, removed, added, old_q2, new_q2 in rows:
            assert (owner, removed) in toggled
            assert (owner, added) not in toggled
            toggled.remove((owner, removed))
            toggled.add((owner, added))
            delta[old_q2] -= 1
            delta[new_q2] += 1
            total_delta[old_q2] -= 1
            total_delta[new_q2] += 1

        losses = [t for t, d in delta.items() if loads[t] + d == 0]
        assert not losses
        negative = [
            {
                "target": bitword(t, n),
                "old_load": loads[t],
                "delta": d,
                "new_load": loads[t] + d,
            }
            for t, d in sorted(delta.items()) if d < 0
        ]
        cycle_reports.append(
            {
                "active_b": b,
                "core": sorted(core),
                "owners": [bitword(o, n) for o, _, _ in cycle],
                "removed": [bitword(old, n) for _, old, _ in cycle],
                "added": [bitword(new, n) for _, _, new in cycle],
                "negative_q2_rows": negative,
            }
        )

    # Both switches simultaneously retain every old q2 support value.
    assert all(loads[t] + d >= 1 for t, d in total_delta.items() if loads[t])

    after_owner, after_colour = factor_maps(toggled)
    assert set(after_owner) == set(by_owner)
    assert set(after_colour) == set(by_colour)
    assert all(len(v) == len(by_owner[o]) for o, v in after_owner.items())
    assert all(len(v) == len(by_colour[c]) for c, v in after_colour.items())

    print(json.dumps({
        "m": m,
        "distance_scope": "intermediate owner vertices restricted to degree two in the open MSW forest",
        "distance_rows": distance_rows,
        "cycles": cycle_reports,
        "simultaneous_q2_support_losses": [],
        "owner_disjoint": True,
        "colour_disjoint": True,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
