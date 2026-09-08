#!/usr/bin/env python3
"""Formula verifier for PBBS portal/compound coexistence claims.

Run substantive ranges only on h100.  This does not enumerate a full MSW
factor.  It checks two explicit packet trades, all selected internal portal
rows at the requested deadline, the fixed compound seams, and the claimed
linear upper-halo collision family.
"""

from __future__ import annotations

import argparse
import collections
import json

import audit_msw_inverse_trade_portal_shadow_20260813 as base
import audit_pbbs_portal_compound_coexistence_20260813 as co


def dyck(w: str) -> bool:
    h = 0
    for x in w:
        h += 1 if x == "1" else -1
        if h < 0:
            return False
    return h == 0


def edge_set(rows, m: int):
    ans = set()
    for row in rows:
        owners = [co.cyc_window(row, t, m + 1) for t in range(2 * m + 1)]
        ans.update(
            frozenset((owners[t], owners[(t + 1) % (2 * m + 1)]))
            for t in range(2 * m + 1)
        )
    return ans


def packet_obstruction(m: int):
    tail = "10" * (m - 7) + "00"
    w4 = "101110011100" + tail
    x4 = "101110011010" + tail
    w5 = "101111000110" + tail
    x5 = "101110100110" + tail
    assert all(len(w) == 2 * m and dyck(w) for w in (w4, x4, w5, x5))
    p4 = base.recover_inverse_trade(base.msw_row(w4), base.msw_row(x4), m)
    p5 = base.recover_inverse_trade(base.msw_row(w5), base.msw_row(x5), m)
    U4, C4, U5 = co.height_owner(m, 4), co.c_owner(m, 4), co.height_owner(m, 5)
    owners4 = [{frozenset(x) for x in base.windows(r, m + 1)} for r in p4]
    owners5 = [{frozenset(x) for x in base.windows(r, m + 1)} for r in p5]
    assert sum(U4 in x for x in owners4) == 1
    assert sum(C4 in x for x in owners4) == 1
    assert sum(U5 in x for x in owners5) == 1
    assert not any(U5 in x for x in owners4)
    assert not any(C4 in x for x in owners5)
    assert frozenset((C4, U5)) not in edge_set(p4 + p5, m)


def tasks(d: int):
    return [
        (A, q) for q in range(2, d) for A in range(q + 1, d + 1)
    ] + [(d + 1, d)]


def q_upper(m: int, A: int, q: int):
    return frozenset(
        {0, 1, 2 * m, 2 * A, 2 * A + 2}
        | set(range(5, 2 * m - 2 * q + 2, 2))
        | set(range(2 * m - 2 * q + 4, 2 * m, 2))
    )


def selected_portals(m: int, d: int):
    records = {}
    for A, q in tasks(d):
        _, _, _, pi, _ = co.explicit_positive_rows(m, A, q)
        records[(A, q)] = co.collared_resources(pi, m, q, d)

    fixed, variable = co.compound_fixed_edges(m, d)
    # Restrict z to the marker-clean bank.  This is still Theta(m) choices.
    variable = [
        e
        for e in variable
        if int(e[0].split("[")[1][:-1]) not in {1, 2, 3, 2 * m - 1}
    ]
    compound = [co.resource_triple(e) for e in fixed + variable]
    seam_o = {x for r in compound for x in (r[1], r[2])}
    seam_l = {r[3] for r in compound}
    seam_u = {r[4] for r in compound}
    for owners, lowers, uppers in records.values():
        assert not (owners & seam_o)
        assert not (lowers & seam_l)
        assert not (uppers & seam_u)

    expected = set()
    for q in range(2, d - 1):
        for A in (q + 1, q + 2):
            if A + 1 > d:
                continue
            shared = records[(A, q)][2] & records[(A + 1, q)][2]
            assert q_upper(m, A, q) in shared
            expected.add(q_upper(m, A, q))
    assert len(expected) == 2 * d - 7

    # The displayed values are guaranteed collisions.  Exhaustive
    # classification is checked separately on selected diagnostic m,d pairs;
    # avoiding its quadratic set census keeps the large symbolic replay fast.
    return len(records), len(expected)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--m-min", type=int, default=14)
    ap.add_argument("--m-max", type=int, default=150)
    ap.add_argument("--m-values", nargs="*", type=int)
    ap.add_argument("--json")
    args = ap.parse_args()
    out = []
    m_values = args.m_values or range(max(7, args.m_min), args.m_max + 1)
    for m in m_values:
        packet_obstruction(m)
        d = (m - 2) // 3
        if d < 4:
            continue
        t, c = selected_portals(m, d)
        out.append({"m": m, "d": d, "tasks": t, "upper_collisions": c})
    payload = json.dumps(out, indent=2, sort_keys=True)
    print(payload)
    if args.json:
        with open(args.json, "w", encoding="utf-8") as f:
            f.write(payload + "\n")


if __name__ == "__main__":
    main()
