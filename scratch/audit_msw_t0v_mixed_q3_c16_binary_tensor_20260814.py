#!/usr/bin/env python3
"""Hostile replay of the two binary-phase 13-root native C16 packets.

Substantive execution belongs on H100.  The script verifies the exact
13-root component action, physical root signs, common z-free binary phase,
typed support through q3, and the doubled G2 seam/casualties through m=10.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict

import audit_msw_t0v_tensor_residence_20260814 as base
import audit_msw_t0v_mixed_c8_c6_tensor_20260814 as mixed_tensor
import audit_msw_t0v_mixed_q3_relay_gate_compact_20260814 as compact
import search_msw_t0_mixed_q3_long_cycle_backup_20260814 as longsearch
import search_msw_t0_mixed_q3_pair_atlas_20260814 as pairsearch


P0 = "000011110111"
N0 = "100011010111"
P1 = "000010111111"
N1 = {
    4: "100010101111",
    5: "100010011111",
}


def difference(old, new):
    result = Counter(new)
    result.subtract(old)
    return Counter({value: amount for value, amount in result.items() if amount})


def cycle_support(row):
    return longsearch.cycle_support(
        tuple(map(base.bits, row["owners"])),
        tuple(map(base.bits, row["colours"])),
    )


def cycle_data(selected, canonical, m):
    lifted = base.lifted_edges(selected, canonical, 2 * m)
    histograms = []
    for rank in (m, m + 1):
        cycles = base.projected_cycles(lifted, rank)
        histograms.append(dict(sorted(Counter(map(len, cycles)).items())))
    assert histograms[0] == histograms[1]
    return histograms[0]


def physical_roles(selected, canonical):
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
    merged = next(cycle for cycle in new_cycles if len(cycle) == 169)
    roles = []
    for index, owner in enumerate(merged):
        if owner >= 1 << 12 or not base.dyck(owner, 6):
            continue
        forward = base.hmap(base.g(owner, 6), 6)
        sign = "+" if merged[(index + 1) % len(merged)] == forward else "-"
        roles.append({"root": base.bitword(owner, 12), "sign": sign})
    assert len(roles) == 13
    assert [row["sign"] for row in roles] == [
        "-", "+", "-", "+", "-", "-", "-", "+", "+", "-", "+", "+", "+",
    ]
    return roles


def dyck_count(s):
    return sum(1 for _ in base.dyck_words(s))


def audit_candidate(index, row, widths):
    fixed_c8, fixed_c6 = mixed_tensor.prefix_packet()
    c16 = cycle_support(row)
    supports = [fixed_c8, fixed_c6, c16]
    owner_banks = [{owner for owner, _ in support} for support in supports]
    assert all(
        not owner_banks[i] & owner_banks[j]
        for i in range(len(owner_banks)) for j in range(i)
    )

    base_canonical = base.canonical_edges(6)
    base_selected = pairsearch.apply_prefix_packet(base_canonical, supports, 6)
    assert pairsearch.common_binary_phase(base_canonical, base_selected)
    resources = {
        "owners": len(set().union(*owner_banks)),
        "colours": len({colour for support in supports for _, colour in support}),
        "incidences": len(set().union(*supports)),
    }
    roles = physical_roles(base_selected, base_canonical)

    runs = []
    for m in widths:
        s = m - 6
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
        for name in old:
            if name != "upper_q3":
                assert not casualties[name]
        assert pairsearch.common_binary_phase(canonical, selected)

        histogram = cycle_data(selected, canonical, m)
        catalan_m = dyck_count(m)
        packets = dyck_count(s)
        expected_histogram = {
            2 * m + 1: catalan_m - 13 * packets,
            13 * (2 * m + 1): packets,
        }
        assert histogram == expected_histogram

        fibre_rows = []
        if s >= 2:
            fibres = defaultdict(list)
            for suffix_word in base.dyck_words(s):
                suffix = base.bits(suffix_word)
                c0 = base.g(suffix, s)
                c1 = base.g(base.hmap(c0, s), s)
                fibres[c0 | c1].append(suffix_word)
            q3_current = difference(old["upper_q3"], new["upper_q3"])
            actual_boundary = Counter()
            mask = (1 << 12) - 1
            for value, amount in q3_current.items():
                if (value >> 12).bit_count() == s + 2:
                    actual_boundary[value] += amount
            expected_boundary = Counter()
            for g2, suffixes in fibres.items():
                amount = len(suffixes)
                for prefix, sign in ((P0, +1), (N0, -1), (P1, +1), (N1[index], -1)):
                    expected_boundary[base.bits(prefix) | (g2 << 12)] += sign * amount
            assert actual_boundary == expected_boundary
            for g2, suffixes in sorted(fibres.items()):
                for prefix in (N0, N1[index]):
                    target = base.bits(prefix) | (g2 << 12)
                    fibre_rows.append({
                        "prefix": prefix,
                        "G2": base.bitword(g2, 2 * s),
                        "suffixes": suffixes,
                        "fibre_size": len(suffixes),
                        "delta": q3_current[target],
                        "old_load": old["upper_q3"][target],
                        "new_load": new["upper_q3"][target],
                    })

        expected_q3_casualty_counts = {6: 0, 7: 0, 8: 0, 9: 2, 10: 4}
        assert len(casualties["upper_q3"]) == expected_q3_casualty_counts[m]
        runs.append({
            "m": m,
            "packets": packets,
            "cycle_histogram": histogram,
            "components": sum(histogram.values()),
            "common_binary_phase": True,
            "upper_q3_casualties": casualties["upper_q3"],
            "negative_G2_fibres": fibre_rows,
        })

    return {
        "index": index,
        "c16_owners": row["owners"],
        "c16_colours": row["colours"],
        "resources_per_packet": resources,
        "physical_roles": roles,
        "runs": runs,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("atlas")
    parser.add_argument("m", nargs="*", type=int, default=[6, 7, 8, 9, 10])
    args = parser.parse_args()
    assert args.m == list(range(6, 11))
    with open(args.atlas, "r", encoding="utf-8") as handle:
        atlas = json.load(handle)
    assert atlas["counts"]["all_q3_support_safe"] == 6
    candidates = [
        audit_candidate(index, atlas["solutions"][index], args.m)
        for index in (4, 5)
    ]
    print(json.dumps({"status": "PASS", "candidates": candidates}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
