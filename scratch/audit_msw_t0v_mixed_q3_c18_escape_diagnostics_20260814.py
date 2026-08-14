#!/usr/bin/env python3
"""Concise hostile diagnostics for the complete native C18 q3-safe atlas.

Substantive execution belongs on H100.  For every base-q3-safe candidate,
this reports the common binary-phase verdict, the exact base component
histogram, the two-suffix-colour q3 boundary at m=8, and literal q3
casualties at m=9 and m=10.  The output is intentionally compact enough
to audit all candidates side by side.
"""

from __future__ import annotations

import argparse
import json
import multiprocessing as mp
from collections import Counter

import audit_msw_t0v_tensor_residence_20260814 as base
import audit_msw_t0v_mixed_c8_c6_tensor_20260814 as mixed_tensor
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


def histogram(canonical, selected, m):
    cycles = base.projected_cycles(base.lifted_edges(selected, canonical, 2 * m), m)
    return dict(sorted(Counter(map(len, cycles)).items()))


def boundary_rows(old, new, m, suffix_weight):
    mask = (1 << 12) - 1
    rows = []
    for value, delta in sorted(difference(old, new).items()):
        suffix = value >> 12
        if suffix.bit_count() != suffix_weight:
            continue
        rows.append({
            "prefix": base.bitword(value & mask, 12),
            "suffix": base.bitword(suffix, 2 * (m - 6)),
            "delta": delta,
            "old": old[value],
            "new": new[value],
        })
    return rows


def casualty_rows(old, new, m):
    return [
        {
            "value": base.bitword(value, 2 * m),
            "old": old[value],
            "new": new[value],
            "delta": new[value] - old[value],
        }
        for value in sorted(old)
        if new[value] == 0
    ]


def audit_candidate(task):
    index, candidate, widths = task
    fixed_c8, fixed_c6 = mixed_tensor.prefix_packet()
    supports = [fixed_c8, fixed_c6, support(candidate)]
    owner_banks = [{owner for owner, _ in packet} for packet in supports]
    assert all(
        not owner_banks[i] & owner_banks[j]
        for i in range(len(owner_banks)) for j in range(i)
    )

    canonical6 = base.canonical_edges(6)
    selected6 = pairsearch.apply_prefix_packet(canonical6, supports, 6)
    binary = pairsearch.common_binary_phase(canonical6, selected6)
    row = {
        "index": index,
        "binary": binary,
        "base_histogram": histogram(canonical6, selected6, 6),
        "owners": candidate["owners"],
        "colours": candidate["colours"],
    }

    for m in widths:
        canonical = base.canonical_edges(m)
        selected = pairsearch.apply_prefix_packet(canonical, supports, m)
        assert pairsearch.common_binary_phase(canonical, selected) == binary
        old = compact.all_decks(canonical)["upper_q3"]
        new = compact.all_decks(selected)["upper_q3"]
        row[f"m{m}_casualties"] = casualty_rows(old, new, m)
        if m == 8:
            row["m8_two_suffix_boundary"] = boundary_rows(old, new, m, 4)
    return row


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("atlas")
    parser.add_argument("--workers", type=int, default=15)
    parser.add_argument("--through-m10", action="store_true")
    args = parser.parse_args()
    with open(args.atlas, "r", encoding="utf-8") as handle:
        atlas = json.load(handle)
    candidates = atlas["solutions"]
    assert atlas["counts"]["all_q3_support_safe"] == 15 == len(candidates)

    widths = (8, 9, 10) if args.through_m10 else (8, 9)
    tasks = [(index, candidate, widths) for index, candidate in enumerate(candidates)]
    with mp.get_context("fork").Pool(processes=args.workers) as pool:
        rows = pool.map(audit_candidate, tasks)

    print(json.dumps({
        "status": "PASS",
        "atlas_counts": atlas["counts"],
        "candidates": rows,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
