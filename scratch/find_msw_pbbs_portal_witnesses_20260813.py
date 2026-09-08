#!/usr/bin/env python3
"""Find explicit MSW inverse-triple portals for structured PBBS spine targets.

Substantial instances belong on h100.  This is a witness extractor, not a
proof: it records the Dyck roots, insertion gap, positive row, orientation,
and start for the first few portals of every definite internal-spine target.
"""

from __future__ import annotations

import argparse
import json

import audit_msw_inverse_trade_portal_shadow_20260813 as base


def oriented_occurrences(row: tuple[int, ...], target: frozenset[int]):
    n = len(row)
    s = len(target)
    ans = []
    for direction, seq in ((1, row), (-1, tuple(reversed(row)))):
        for start in range(n):
            block = frozenset(seq[(start + j) % n] for j in range(s))
            if block == target:
                ans.append({"direction": direction, "start": start})
    return ans


def audit(m: int, d: int, q_values: list[int], limit: int):
    _, rows = base.build_factor(m)
    targets = {}
    for q in q_values:
        for h, start, target in base.internal_pbbs_casualties(m, d, q):
            key = (q, target)
            targets.setdefault(key, {"heights_starts": []})
            targets[key]["heights_starts"].append([h, start])
            targets[key].setdefault("witnesses", [])

    for z in base.dyck_words(m - 2):
        for gap in range(len(z) + 1):
            x = z[:gap] + "1100" + z[gap:]
            y = z[:gap] + "1010" + z[gap:]
            neg_rows = (rows[x], rows[y])
            pos_rows = base.recover_inverse_trade(*neg_rows, m)
            for (q, target_tuple), record in targets.items():
                if len(record["witnesses"]) >= limit:
                    continue
                target = frozenset(target_tuple)
                for which, row in enumerate(pos_rows):
                    occ = oriented_occurrences(row, target)
                    if occ:
                        record["witnesses"].append(
                            {
                                "z": z,
                                "gap": gap,
                                "negative_roots": [x, y],
                                "negative_rows": [list(r) for r in neg_rows],
                                "positive_row_index": which,
                                "positive_row": list(row),
                                "occurrences": occ,
                            }
                        )
                        break

    return {
        "m": m,
        "d": d,
        "q": q_values,
        "targets": [
            {
                "q": q,
                "target": list(target),
                **record,
            }
            for (q, target), record in sorted(targets.items())
        ],
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("m", type=int)
    ap.add_argument("d", type=int)
    ap.add_argument("--q", action="append", type=int)
    ap.add_argument("--limit", type=int, default=3)
    ap.add_argument("--json")
    args = ap.parse_args()
    result = audit(args.m, args.d, args.q or list(range(2, args.d + 1)), args.limit)
    payload = json.dumps(result, indent=2, sort_keys=True)
    print(payload)
    if args.json:
        with open(args.json, "w", encoding="utf-8") as out:
            out.write(payload + "\n")


if __name__ == "__main__":
    main()
