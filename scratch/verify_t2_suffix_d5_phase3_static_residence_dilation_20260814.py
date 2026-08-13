#!/usr/bin/env python3
"""Verify the constant-clock phase-3 dilation of the D5 output cycle.

Substantive execution belongs on H100.  The unique 12,420-owner touched
lower-projection output cycle is expanded by the depth-two source word

    T_i, p_(i mod 2), q_(i mod 2).

The verifier checks the literal derived-owner formula, Johnson simplicity,
q1-colour simplicity, and q=2 residence of both the expanded lower trace and
its immediate-upper union trace.  This is a static post-switch residence
dilation, not by itself a common-history realization of the switch.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import search_t2_cross_suffix_alternating_cycles_20260813 as base  # noqa:E402
from audit_t2_cross_suffix_c16_full_ml_topology_20260813 import (  # noqa:E402
    lifted_edges,
)
from verify_t2_c16_suffix_component_residence_20260813 import (  # noqa:E402
    cyclic_run_minimum,
    projected_cycles,
    toggle,
)


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
    cycles = []
    touched = set()
    for item in data["selection"]:
        owners = tuple(
            base.bits(word) for word in item["candidate"]["owners"]
        )
        colours = tuple(
            base.bits(word) for word in item["candidate"]["new_colours"]
        )
        rows = [
            (owners[index], colours[index - 1], colours[index])
            for index in range(len(owners))
        ]
        cycles.append(rows)
        touched.update(owners)
    simultaneous = toggle(post, cycles)
    full_edges = lifted_edges(simultaneous, canonical, n)
    touched_cycles = [
        owners
        for owners, _ in projected_cycles(full_edges, m)
        if touched & set(owners)
    ]
    assert len(touched_cycles) == 1
    trace = touched_cycles[0]
    length = len(trace)
    assert length == 12420 and length % 2 == 0
    assert len(set(trace)) == length
    assert all(owner.bit_count() == m for owner in trace)

    p = [1 << (n + 1), 1 << (n + 2)]
    q = [1 << (n + 3), 1 << (n + 4)]
    expanded = []
    source = []
    for index, owner in enumerate(trace):
        colour = index & 1
        source.extend((owner, p[colour], q[colour]))
        next_owner = trace[(index + 1) % length]
        next_colour = (index + 1) & 1
        expanded.extend((
            owner | p[colour] | q[colour],
            next_owner | p[colour] | q[colour],
            next_owner | p[next_colour] | q[colour],
        ))

    expanded_length = 3 * length
    assert len(source) == len(expanded) == expanded_length
    # Literal depth-two source derivation.
    derived = [
        source[index]
        | source[(index + 1) % expanded_length]
        | source[(index + 2) % expanded_length]
        for index in range(expanded_length)
    ]
    assert derived == expanded
    assert all(owner.bit_count() == m + 2 for owner in expanded)
    assert len(set(expanded)) == expanded_length

    lower_supports = [
        expanded[index] ^ expanded[(index + 1) % expanded_length]
        for index in range(expanded_length)
    ]
    assert all(support.bit_count() == 2 for support in lower_supports)
    assert all(
        not lower_supports[index - 1] & lower_supports[index]
        for index in range(expanded_length)
    )

    upper = [
        expanded[index] | expanded[(index + 1) % expanded_length]
        for index in range(expanded_length)
    ]
    lower_colours = [
        expanded[index] & expanded[(index + 1) % expanded_length]
        for index in range(expanded_length)
    ]
    assert all(colour.bit_count() == m + 3 for colour in upper)
    assert all(colour.bit_count() == m + 1 for colour in lower_colours)
    assert len(set(upper)) == expanded_length
    upper_supports = [
        upper[index] ^ upper[(index + 1) % expanded_length]
        for index in range(expanded_length)
    ]
    assert all(support.bit_count() == 2 for support in upper_supports)
    assert all(
        not upper_supports[index - 1] & upper_supports[index]
        for index in range(expanded_length)
    )

    lower_positive, lower_positive_witness = cyclic_run_minimum(
        expanded, n + 5, 1
    )
    lower_zero, lower_zero_witness = cyclic_run_minimum(
        expanded, n + 5, 0
    )
    upper_positive, upper_positive_witness = cyclic_run_minimum(
        upper, n + 5, 1
    )
    upper_zero, upper_zero_witness = cyclic_run_minimum(
        upper, n + 5, 0
    )
    assert (lower_positive, lower_zero) == (3, 3)
    assert upper_positive >= 4 and upper_zero == 2

    screen_upper = {
        trace[index] | trace[(index + 1) % length]
        | p[index & 1] | q[index & 1]
        for index in range(length)
    }
    assert len(screen_upper) == length
    assert screen_upper <= set(upper)
    print(json.dumps({
        "status": "PASS",
        "selection_sha256": hashlib.sha256(raw).hexdigest(),
        "original_touched_output_owner_length": length,
        "expanded_owner_length": expanded_length,
        "source_depth": 2,
        "source_phase_modulus": 3,
        "fresh_clock_coordinates": 4,
        "expanded_owner_rank": m + 2,
        "expanded_ground_size": n + 5,
        "expanded_owner_simple": True,
        "expanded_immediate_upper_q1_simple": True,
        "expanded_immediate_lower_colour_distinct": (
            len(set(lower_colours)) == expanded_length
        ),
        "lower_q2_resident": True,
        "upper_q2_resident": True,
        "lower_minimum_positive_zero_runs": [
            lower_positive, lower_zero
        ],
        "upper_minimum_positive_zero_runs": [
            upper_positive, upper_zero
        ],
        "minimum_run_witnesses": {
            "lower_positive": lower_positive_witness,
            "lower_zero": lower_zero_witness,
            "upper_positive": upper_positive_witness,
            "upper_zero": upper_zero_witness,
        },
        "fresh_coordinate_classes": {
            str(n + 1): "p0", str(n + 2): "p1",
            str(n + 3): "q0", str(n + 4): "q1",
        },
        "screen_q1_colours_embedded_injectively": len(screen_upper),
        "component_count_on_dilated_touched_bank": 1,
        "scope": "static post-switch dilation; no dynamic switch lift",
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
