#!/usr/bin/env python3
"""Diagnose every base-q3-safe native C16 alternative on the direct gates.

Substantive execution belongs on H100.  The candidate list is the complete
parallel target-relevant C16 output.  Each candidate is tensored at m=7,8
and checked for typed support, boundary suffix-weight strata, component
cost, and a common binary phase.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter

import audit_msw_t0v_tensor_residence_20260814 as base
import audit_msw_t0v_mixed_c8_c6_tensor_20260814 as mixed_tensor
import audit_msw_t0v_mixed_q3_closed_tensor_20260814 as q3closed
import audit_msw_t0v_mixed_q3_relay_gate_compact_20260814 as compact
import search_msw_t0_mixed_q3_long_cycle_backup_20260814 as longsearch
import search_msw_t0_mixed_q3_pair_atlas_20260814 as pairsearch


def difference(old, new):
    result = Counter(new)
    result.subtract(old)
    return Counter({value: amount for value, amount in result.items() if amount})


def support(row):
    return longsearch.cycle_support(
        tuple(map(base.bits, row["owners"])),
        tuple(map(base.bits, row["colours"])),
    )


def current_rows_by_suffix_weight(old, new, m):
    result = []
    mask = (1 << 12) - 1
    for value, amount in sorted(difference(old, new).items()):
        result.append({
            "value": base.bitword(value, 2 * m),
            "delta": amount,
            "old_load": old[value],
            "new_load": new[value],
            "suffix_weight": (value & ~mask).bit_count(),
        })
    return result


def root_action(canonical, selected):
    old_cycles = base.projected_cycles(base.lifted_edges(canonical, canonical, 12), 6)
    new_cycles = base.projected_cycles(base.lifted_edges(selected, canonical, 12), 6)
    owner_to_root = {}
    for cycle in old_cycles:
        roots = [
            owner for owner in cycle
            if owner < (1 << 12) and base.dyck(owner, 6)
        ]
        assert len(roots) == 1
        for owner in cycle:
            owner_to_root[owner] = roots[0]
    actions = []
    for cycle in new_cycles:
        roots = sorted({owner_to_root[owner] for owner in cycle})
        if len(roots) > 1:
            actions.append({
                "new_cycle_length": len(cycle),
                "old_root_count": len(roots),
                "old_roots": [base.bitword(root, 12) for root in roots],
            })
    return actions


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input")
    args = parser.parse_args()
    with open(args.input, "r", encoding="utf-8") as handle:
        atlas = json.load(handle)
    candidates = atlas["solutions"]
    assert atlas["counts"]["all_q3_support_safe"] == len(candidates)

    fixed_c8, fixed_c6 = mixed_tensor.prefix_packet()
    fixed_supports = [fixed_c8, fixed_c6]
    rows = []
    for index, candidate in enumerate(candidates):
        supports = fixed_supports + [support(candidate)]
        widths = {}
        for m in (6, 7, 8):
            canonical = base.canonical_edges(m)
            selected = pairsearch.apply_prefix_packet(canonical, supports, m)
            old = compact.all_decks(canonical)
            new = compact.all_decks(selected)
            casualties = {
                name: [
                    base.bitword(value, 2 * m)
                    for value in old[name] if new[name][value] == 0
                ]
                for name in old
            }
            assert not any(casualties.values())
            q3_rows = current_rows_by_suffix_weight(
                old["upper_q3"], new["upper_q3"], m
            )
            topology = pairsearch.component_data(canonical, selected, m)
            frozen = set(canonical)
            mixed_tensor.apply_tensor(frozen, m)
            frozen_topology = pairsearch.component_data(canonical, frozen, m)
            suffix_histogram = Counter(
                (row["suffix_weight"], 1 if row["delta"] > 0 else -1)
                for row in q3_rows
            )
            widths[str(m)] = {
                "topology": topology,
                "frozen_topology": frozen_topology,
                "net_component_cost": topology["components"] - frozen_topology["components"],
                "q3_current_suffix_weight_histogram": {
                    f"{weight}:{sign}": count
                    for (weight, sign), count in sorted(suffix_histogram.items())
                },
                "two_suffix_colour_rows": [
                    row for row in q3_rows
                    if m == 8 and row["suffix_weight"] == 4
                ],
            }
        canonical = base.canonical_edges(6)
        selected = pairsearch.apply_prefix_packet(canonical, supports, 6)
        binary = pairsearch.common_binary_phase(canonical, selected)
        odd_cycle = q3closed.shortest_odd_phase_cycle(canonical, selected, 12)
        assert binary == (odd_cycle is None)
        rows.append({
            "index": index,
            "owners": candidate["owners"],
            "colours": candidate["colours"],
            "common_binary_phase": binary,
            "shortest_odd_phase_cycle": odd_cycle,
            "base_root_action": root_action(canonical, selected),
            "widths": widths,
        })

    print(json.dumps({
        "status": "PASS",
        "candidate_count": len(rows),
        "candidates": rows,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
