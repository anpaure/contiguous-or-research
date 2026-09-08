#!/usr/bin/env python3
"""Hostile tensor replay of the five typed-q3-safe native C6+C10 pairs.

Substantive execution belongs on H100.  The script reconstructs both
circuits from the exhaustive pair-atlas certificate, checks disjointness,
typed support and common binary phase, then records the exact two-suffix
q3 boundary and literal casualties through m=10.
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


def circuit_support(owners, colours):
    return longsearch.cycle_support(tuple(owners), tuple(colours))


def hex_support(name, canonical):
    wanted = (name["index"], name["core"], tuple(name["active_one_based"]))
    for row in pairsearch.catalogue("c6", canonical):
        got = (
            row["name"]["index"],
            row["name"]["core"],
            tuple(row["name"]["active_one_based"]),
        )
        if got == wanted:
            return row["support"]
    raise AssertionError(wanted)


def histogram(canonical, selected, m):
    cycles = base.projected_cycles(base.lifted_edges(selected, canonical, 2 * m), m)
    return dict(sorted(Counter(map(len, cycles)).items()))


def boundary_rows(old, new, m, suffix_weight):
    mask = (1 << 12) - 1
    return [
        {
            "prefix": base.bitword(value & mask, 12),
            "suffix": base.bitword(value >> 12, 2 * (m - 6)),
            "delta": delta,
            "old": old[value],
            "new": new[value],
        }
        for value, delta in sorted(difference(old, new).items())
        if (value >> 12).bit_count() == suffix_weight
    ]


def casualties(old, new, m):
    return [
        {
            "value": base.bitword(value, 2 * m),
            "old": old[value],
            "new": new[value],
        }
        for value in sorted(old)
        if new[value] == 0
    ]


def audit_candidate(task):
    index, row, through_m10 = task
    canonical6 = base.canonical_edges(6)
    fixed_c8, fixed_c6 = mixed_tensor.prefix_packet()
    c6 = hex_support(row["left"], canonical6)
    c10 = circuit_support(
        tuple(map(base.bits, row["right"]["owners"])),
        tuple(map(base.bits, row["right"]["colours"])),
    )
    supports = [fixed_c8, fixed_c6, c6, c10]
    owner_banks = [{owner for owner, _ in packet} for packet in supports]
    assert all(
        not owner_banks[i] & owner_banks[j]
        for i in range(len(owner_banks)) for j in range(i)
    )

    selected6 = pairsearch.apply_prefix_packet(canonical6, supports, 6)
    assert pairsearch.common_binary_phase(canonical6, selected6)
    old_decks = compact.all_decks(canonical6)
    new_decks = compact.all_decks(selected6)
    assert all(all(new_decks[name][value] for value in old_decks[name]) for name in old_decks)

    result = {
        "index": index,
        "left": row["left"],
        "right": row["right"],
        "base_histogram": histogram(canonical6, selected6, 6),
    }
    widths = (8, 9, 10) if through_m10 else (8, 9)
    for m in widths:
        canonical = base.canonical_edges(m)
        selected = pairsearch.apply_prefix_packet(canonical, supports, m)
        assert pairsearch.common_binary_phase(canonical, selected)
        old = compact.all_decks(canonical)
        new = compact.all_decks(selected)
        typed_casualties = {
            name: casualties(old[name], new[name], m)
            for name in old
        }
        assert not any(
            typed_casualties[name]
            for name in typed_casualties if name != "upper_q3"
        )
        result[f"m{m}_q3_casualties"] = typed_casualties["upper_q3"]
        if m == 8:
            result["m8_two_suffix_boundary"] = boundary_rows(
                old["upper_q3"], new["upper_q3"], m, 4
            )
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("atlas")
    parser.add_argument("--through-m10", action="store_true")
    args = parser.parse_args()
    with open(args.atlas, "r", encoding="utf-8") as handle:
        atlas = json.load(handle)
    assert atlas["menu"] == "c6c10"
    assert atlas["counts"]["typed_q3_safe"] == 5
    assert len(atlas["solutions"]) == 5
    tasks = [
        (index, row, args.through_m10)
        for index, row in enumerate(atlas["solutions"])
    ]
    with mp.get_context("fork").Pool(processes=5) as pool:
        rows = pool.map(audit_candidate, tasks)
    print(json.dumps({
        "status": "PASS",
        "atlas_counts": atlas["counts"],
        "candidates": rows,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
