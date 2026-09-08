#!/usr/bin/env python3
"""Finite audit for the explicit PBBS internal-spine MSW portal theorem.

Substantial instances must run on h100.  For every normalized (A,q), this
checks the target formula, Dyck/root data, flip-list suffix identity, literal
positive-row interval, inverse-trade support identity, negative-row
disjointness, and simultaneous exact-factor substitution.
"""

from __future__ import annotations

import argparse
import json
import math

import audit_msw_inverse_trade_portal_shadow_20260813 as base


def height_owner(m: int, h: int) -> frozenset[int]:
    return frozenset(
        {0}
        | set(range(h + 1, 2 * h + 1))
        | set(range(2 * h + 2, 2 * m + 1, 2))
    )


def target_formula(m: int, A: int, q: int) -> frozenset[int]:
    return frozenset(
        {0}
        | set(range(A + q + 1, 2 * A + 1))
        | set(range(2 * A + 2, 2 * m + 1, 2))
    )


def dyck(word: str) -> bool:
    bal = 0
    for bit in word:
        bal += 1 if bit == "1" else -1
        if bal < 0:
            return False
    return bal == 0


def portal_data(m: int, A: int, q: int, rows):
    z = "1" * (A + q - 3) + "0" * (A - q)
    z += "10" * (m - A - q + 1) + "0" * (2 * q - 3)
    assert len(z) == 2 * (m - 2) and dyck(z)

    target = target_formula(m, A, q)
    odd = base.rho(z)[0::2]
    tail = set(odd[q - 1 :])
    expected_tail = set(range(A + q - 2, 2 * A - 2))
    expected_tail |= set(range(2 * A - 1, 2 * m - 4, 2))
    assert tail == expected_tail

    x, y = "1100" + z, "1010" + z
    neg = (rows[x], rows[y])
    pos = base.recover_inverse_trade(*neg, m)
    hits = []
    for row in pos:
        for direction, seq in ((1, row), (-1, tuple(reversed(row)))):
            for start in range(2 * m + 1):
                block = frozenset(
                    seq[(start + j) % (2 * m + 1)]
                    for j in range(m + 1 - q)
                )
                if block == target:
                    hits.append((row, direction, start))
    assert hits
    assert base.windows(neg[0], m) | base.windows(neg[1], m) == (
        base.windows(pos[0], m) | base.windows(pos[1], m)
    )
    return z, neg, pos, hits


def audit(m: int):
    roots, rows = base.build_factor(m)
    original = {row for row in rows.values()}
    selected_neg = set()
    selected_pos = set()
    records = []

    for q in range(2, m // 2 + 1):
        # Literal internal starts A=q and A=q+1 give the same value.
        boundary = frozenset.intersection(
            *(height_owner(m, t) for t in range(q, 2 * q + 1))
        )
        assert boundary == target_formula(m, q + 1, q)
        normalized_A = list(range(q + 1, m - q + 1))
        if m == 2 * q:
            normalized_A.append(q + 1)
        for A in normalized_A:
            target = target_formula(m, A, q)
            if A + q <= m:
                literal = frozenset.intersection(
                    *(height_owner(m, t) for t in range(A, A + q + 1))
                )
                assert literal == target and len(target) == m + 1 - q
            z, neg, pos, hits = portal_data(m, A, q, rows)
            assert not (set(neg) & selected_neg)
            selected_neg.update(neg)
            selected_pos.update(pos)
            records.append(
                {
                    "q": q,
                    "A": A,
                    "z": z,
                    "target": sorted(target),
                    "portal_count": len(hits),
                }
            )

    assert len(selected_pos) == 2 * len(records)
    new_factor = (original - selected_neg) | selected_pos
    assert len(new_factor) == math.comb(2 * m + 1, m) // (2 * m + 1)
    seen = set()
    for row in new_factor:
        ws = base.windows(row, m)
        assert not (seen & ws)
        seen |= ws
    assert len(seen) == math.comb(2 * m + 1, m)
    return {
        "m": m,
        "roots": len(roots),
        "targets": len(records),
        "negative_rows": len(selected_neg),
        "positive_rows": len(selected_pos),
        "records": records,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("m", nargs="+", type=int)
    ap.add_argument("--json")
    args = ap.parse_args()
    result = [audit(m) for m in args.m]
    payload = json.dumps(result, indent=2, sort_keys=True)
    print(payload)
    if args.json:
        with open(args.json, "w", encoding="utf-8") as out:
            out.write(payload + "\n")


if __name__ == "__main__":
    main()
