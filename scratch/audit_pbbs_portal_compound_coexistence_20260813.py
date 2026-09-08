#!/usr/bin/env python3
"""Finite H100 audit for portal/compound-low-spine coexistence.

This script is intentionally standard-library only.  Substantial instances
must be run on h100, never on the local Mac.

For the internal PBBS casualty set it constructs the explicit selected
positive inverse-triple rows, their literal two collared row blocks, and the
whole offset-zero first-aligned packet.  It then compares owner, immediate-
lower, and immediate-upper resources with the fixed seams of the compound
low-spine path.  It also reports cross-package nonmiddle upper collisions.
"""

from __future__ import annotations

import argparse
import collections
import json

import audit_msw_inverse_trade_portal_shadow_20260813 as base


def cyc_window(row, start, width):
    n = len(row)
    return frozenset(row[(start + j) % n] for j in range(width))


def height_owner(m: int, h: int) -> frozenset[int]:
    return frozenset(
        {0}
        | set(range(h + 1, 2 * h + 1))
        | set(range(2 * h + 2, 2 * m + 1, 2))
    )


def height_core(m: int, h: int) -> frozenset[int]:
    # H_h=U_h\{h+1,2h+2}.
    return height_owner(m, h) - {h + 1, 2 * h + 2}


def c_owner(m: int, h: int) -> frozenset[int]:
    return height_core(m, h) | {h + 1, 2 * h + 1}


def b_owner(m: int, h: int, z: int) -> frozenset[int]:
    return height_core(m, h) | {2 * h + 2, z}


def compound_fixed_edges(m: int, d: int):
    """Return fixed seams and all admissible U_h--B_h choices.

    The variable z is restricted only by owner rank and the displayed local
    freshness condition; global bridge/resource avoidance is deliberately not
    modeled here.
    """
    n = 2 * m + 1
    fixed = []
    variable = []
    for h in range(4, d + 1):
        u = height_owner(m, h)
        forbidden = u | (c_owner(m, h - 1) if h >= 5 else frozenset())
        for z in range(n):
            b = b_owner(m, h, z)
            if len(b) != m + 1 or z in forbidden:
                continue
            variable.append((f"U{h}-B{h}[{z}]", u, b))
        if h >= 5:
            fixed.append((f"C{h-1}-U{h}", c_owner(m, h - 1), u))
    fixed.append((f"C{d}-U{d+1}", c_owner(m, d), height_owner(m, d + 1)))
    return fixed, variable


def resource_triple(edge):
    name, a, b = edge
    assert len(a) == len(b) and len(a ^ b) == 2
    return name, a, b, a & b, a | b


def owner_edge_key(a, b):
    return frozenset((a, b))


def factor_owner_edges(rows, m: int):
    out = set()
    for row in rows:
        owners = [cyc_window(row, t, m + 1) for t in range(2 * m + 1)]
        out.update(
            owner_edge_key(owners[t], owners[(t + 1) % (2 * m + 1)])
            for t in range(2 * m + 1)
        )
    return out


def z_word(m: int, A: int, q: int) -> str:
    return (
        "1" * (A + q - 3)
        + "0" * (A - q)
        + "10" * (m - A - q + 1)
        + "0" * (2 * q - 3)
    )


def explicit_positive_rows(m: int, A: int, q: int):
    z = z_word(m, A, q)
    flip = base.rho(z)
    e = tuple([3 + x for x in flip[0::2]] + [2 * m])
    o = tuple(3 + x for x in flip[1::2])
    cpos = (2, 3) + e + (0, 1) + o
    dpos = (0, 2) + e + (1, 3) + o
    assert len(cpos) == len(dpos) == 2 * m + 1
    target = frozenset(
        {0}
        | set(range(A + q + 1, 2 * A + 1))
        | set(range(2 * A + 2, 2 * m + 1, 2))
    )
    start = q + 1
    assert cyc_window(cpos, start, m + 1 - q) == target
    # Rotate immediately after the pointed target, so pi=(D,C,I,S).
    end = (start + (m + 1 - q) - 1) % (2 * m + 1)
    pi = cpos[end + 1 :] + cpos[: end + 1]
    assert cyc_window(pi, 2 * m + 1 - (m + 1 - q), m + 1 - q) == target
    return z, cpos, dpos, pi, target


def collared_resources(pi, m: int, q: int, d: int):
    n = 2 * m + 1
    blocks = [range(-d, q + d + 2), range(m - d, m + q + d + 3)]
    owner_indices = sorted({t % n for block in blocks for t in block})
    edge_indices = sorted(
        {
            t % n
            for block in blocks
            for t in range(block.start, block.stop - 1)
        }
    )
    owners = {cyc_window(pi, t - 1, m + 1) for t in owner_indices}
    lowers = {cyc_window(pi, t - 1, m) for t in edge_indices}
    uppers = {cyc_window(pi, t - 1, m + 2) for t in edge_indices}
    return owners, lowers, uppers


def full_first_aligned_packet(m: int):
    roots, rows = base.build_factor(m)
    selected_neg = set()
    selected_pos = set()
    paired_words = set()
    for w in roots:
        if w in paired_words:
            continue
        mate = None
        for j in range(0, 2 * m - 3, 4):
            block = w[j : j + 4]
            if block == "1100":
                mate = w[:j] + "1010" + w[j + 4 :]
                break
            if block == "1010":
                mate = w[:j] + "1100" + w[j + 4 :]
                break
        if mate is None:
            continue
        assert mate in rows
        paired_words.update((w, mate))
        neg = (rows[w], rows[mate])
        pos = base.recover_inverse_trade(*neg, m)
        assert not (set(neg) & selected_neg)
        selected_neg.update(neg)
        selected_pos.update(pos)
    original = set(rows.values())
    result = (original - selected_neg) | selected_pos
    assert len(result) == len(original)
    seen = set()
    for row in result:
        ws = base.windows(row, m)
        assert not (seen & ws)
        seen |= ws
    return selected_neg, selected_pos, result


def audit(m: int, d: int):
    # The structural coexistence census also permits small diagnostic pairs
    # outside the asymptotic deadline.  The JSON records whether the theorem's
    # deadline m>=3d+2 holds.
    assert m >= d + 2 and d >= 4
    tasks = []
    selected_rows = set()
    protected_owners = set()
    protected_lowers = set()
    protected_upper_occ = collections.defaultdict(list)
    for q in range(2, d):
        for A in range(q + 1, d + 1):
            z, cpos, dpos, pi, target = explicit_positive_rows(m, A, q)
            owners, lowers, uppers = collared_resources(pi, m, q, d)
            key = (A, q)
            tasks.append((key, target, cpos, dpos, owners, lowers, uppers))
            selected_rows.update((base.canonical_cycle(cpos), base.canonical_cycle(dpos)))
            assert not (protected_owners & owners)
            assert not (protected_lowers & lowers)
            protected_owners |= owners
            protected_lowers |= lowers
            for u in uppers:
                protected_upper_occ[u].append(key)
    # Depth-d boundary value A=d+1,q=d.
    A, q = d + 1, d
    z, cpos, dpos, pi, target = explicit_positive_rows(m, A, q)
    owners, lowers, uppers = collared_resources(pi, m, q, d)
    key = (A, q)
    tasks.append((key, target, cpos, dpos, owners, lowers, uppers))
    selected_rows.update((base.canonical_cycle(cpos), base.canonical_cycle(dpos)))
    assert not (protected_owners & owners)
    assert not (protected_lowers & lowers)
    protected_owners |= owners
    protected_lowers |= lowers
    for u in uppers:
        protected_upper_occ[u].append(key)

    fixed, variable = compound_fixed_edges(m, d)
    fixed_resources = [resource_triple(x) for x in fixed]
    variable_resources = [resource_triple(x) for x in variable]
    seam_owners = {x for r in fixed_resources + variable_resources for x in (r[1], r[2])}
    seam_lowers = {r[3] for r in fixed_resources + variable_resources}
    seam_uppers = {r[4] for r in fixed_resources + variable_resources}

    neg, all_pos, factor = full_first_aligned_packet(m)
    _, original_rows = base.build_factor(m)
    original_edges = factor_owner_edges(set(original_rows.values()), m)
    packet_edges = factor_owner_edges(factor, m)
    all_pos_owner = {
        frozenset(x) for row in all_pos for x in base.windows(row, m + 1)
    }
    all_pos_lower = {
        frozenset(x) for row in all_pos for x in base.windows(row, m)
    }
    all_pos_upper = {
        frozenset(x) for row in all_pos for x in base.windows(row, m + 2)
    }
    neg_upper = {
        frozenset(x) for row in neg for x in base.windows(row, m + 2)
    }

    upper_collisions = [
        {"upper": sorted(u), "tasks": [list(x) for x in ks]}
        for u, ks in protected_upper_occ.items()
        if len(ks) > 1
    ]
    return {
        "m": m,
        "d": d,
        "deadline_holds": m >= 3 * d + 2,
        "tasks": len(tasks),
        "selected_positive_rows": len(selected_rows),
        "protected_owner_values": len(protected_owners),
        "protected_lower_values": len(protected_lowers),
        "protected_upper_values": len(protected_upper_occ),
        "protected_upper_collision_values": len(upper_collisions),
        "protected_upper_collision_max_multiplicity": max(
            (len(x["tasks"]) for x in upper_collisions), default=1
        ),
        "protected_upper_collision_sample": upper_collisions[:20],
        "compound_fixed_edges": len(fixed_resources),
        "compound_variable_edge_choices": len(variable_resources),
        "selected_halo_vs_compound": {
            "owner": len(protected_owners & seam_owners),
            "lower": len(protected_lowers & seam_lowers),
            "upper": len(set(protected_upper_occ) & seam_uppers),
        },
        "whole_packet": {
            "negative_rows": len(neg),
            "positive_rows": len(all_pos),
            "factor_rows": len(factor),
            "positive_vs_compound_owner": len(all_pos_owner & seam_owners),
            "positive_vs_compound_lower": len(all_pos_lower & seam_lowers),
            "positive_vs_compound_upper": len(all_pos_upper & seam_uppers),
            "negative_vs_compound_upper": len(neg_upper & seam_uppers),
            "fixed_edges_installed_original": [
                r[0]
                for r in fixed_resources
                if owner_edge_key(r[1], r[2]) in original_edges
            ],
            "fixed_edges_installed_packet": [
                r[0]
                for r in fixed_resources
                if owner_edge_key(r[1], r[2]) in packet_edges
            ],
            "variable_edges_installed_original": [
                r[0]
                for r in variable_resources
                if owner_edge_key(r[1], r[2]) in original_edges
            ],
            "variable_edges_installed_packet": [
                r[0]
                for r in variable_resources
                if owner_edge_key(r[1], r[2]) in packet_edges
            ],
            "old_spine_edges_installed_original": [
                h
                for h in range(4, d + 1)
                if owner_edge_key(height_owner(m, h), height_owner(m, h + 1))
                in original_edges
            ],
            "old_spine_edges_installed_packet": [
                h
                for h in range(4, d + 1)
                if owner_edge_key(height_owner(m, h), height_owner(m, h + 1))
                in packet_edges
            ],
        },
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pairs", nargs="+", help="m:d")
    ap.add_argument("--json")
    args = ap.parse_args()
    out = []
    for pair in args.pairs:
        m, d = map(int, pair.split(":"))
        out.append(audit(m, d))
    payload = json.dumps(out, indent=2, sort_keys=True)
    print(payload)
    if args.json:
        with open(args.json, "w", encoding="utf-8") as f:
            f.write(payload + "\n")


if __name__ == "__main__":
    main()
