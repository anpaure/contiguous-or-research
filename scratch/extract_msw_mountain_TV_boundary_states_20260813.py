#!/usr/bin/env python3
"""Extract symbolic-looking boundary-state data for T0 1^s0^s.

Heavy runs belong on h100.
"""

from __future__ import annotations

import argparse
import collections
import json
import math

import audit_msw_common_history_upper_deck_20260813 as up
import audit_msw_inverse_trade_portal_shadow_20260813 as base


def labels(mask, n):
    return [z for z in range(n) if mask >> z & 1]


def audit(m, suffix_type="mountain", d_override=None):
    R, n = m + 1, 2 * m + 1
    W, half = math.comb(n, R), 1 << (n - 1)
    d = 0
    while d * W + d * (d + 1) // 2 < half:
        d += 1
    if d_override is not None:
        d = d_override
    suffix = (("1" * (m - 6) + "0" * (m - 6))
              if suffix_type == "mountain" else "10" * (m - 6))
    word = "110011001111" + suffix
    U = sum((bit == "1") << i for i, bit in enumerate(word))
    roots = list(base.dyck_words(m))
    records = collections.defaultdict(list)
    for vi, root in enumerate(roots):
        row0 = list(base.msw_row(root))
        for oi, order in enumerate((row0, list(reversed(row0)))):
            owners = up.owner_cycle(order, 0, R)
            for shift in range(n):
                st = up.state(order, shift, d, R)
                left, right = owners[(shift - 1) % n], owners[shift]
                for side, owner in (("L", left), ("R", right)):
                    if owner & ~U or owner.bit_count() != R:
                        continue
                    missing = labels(U & ~owner, n)
                    assert len(missing) == 1
                    records[missing[0]].append({
                        "side": side, "orientation": oi, "shift": shift,
                        "root": root, "order": order,
                        "maximal": [labels(x, n) for x in st[0]],
                        "forced": [labels(x, n) for x in st[1]],
                    })
    failures = collections.Counter()
    necessary_stage = collections.Counter()
    failure_examples = []
    keys = sorted(records)
    for x in keys:
        for y in keys:
            if x >= y:
                continue
            for a in records[x]:
                for b in records[y]:
                    # Only opposite cross sides can be adjacent after a
                    # successor swap: L_x--R_y or L_y--R_x.
                    if a["side"] == b["side"]:
                        continue
                    first = None
                    forced_outside_common = set()
                    for j in range(d):
                        forced_outside_common |= ((set(a["forced"][j]) |
                                                   set(b["forced"][j])) -
                                                  (set(a["maximal"][j]) &
                                                   set(b["maximal"][j])))
                    outside_U_common = forced_outside_common & {x, y}
                    necessary_stage[(bool(outside_U_common),)] += 1
                    for j in range(d):
                        fa, fb = set(a["forced"][j]), set(b["forced"][j])
                        pa, pb = set(a["maximal"][j]), set(b["maximal"][j])
                        bad = sorted((fa | fb) - (pa & pb))
                        if bad:
                            first = (j, tuple(bad))
                            break
                    if first is None:
                        failures[("COMPATIBLE",)] += 1
                    else:
                        failures[first] += 1
                        if len(failure_examples) < 80:
                            failure_examples.append({
                                "missing": [x, y],
                                "states": [[a["side"], a["orientation"], a["shift"]],
                                           [b["side"], b["orientation"], b["shift"]]],
                                "first_failure": [first[0], list(first[1])],
                            })
    return {
        "m": m, "d": d, "word": word, "U": labels(U, n),
        "records_per_missing_label": {str(k): len(v) for k, v in records.items()},
        "records": records,
        "first_failure_histogram": {str(k): v for k, v in failures.items()},
        "failure_has_missing_label_histogram": {
            str(k): v for k, v in necessary_stage.items()},
        "failure_examples": failure_examples,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("m", type=int)
    ap.add_argument("--json")
    ap.add_argument("--suffix-type", choices=("mountain", "alternating"),
                    default="mountain")
    ap.add_argument("--d", type=int)
    args = ap.parse_args()
    ans = audit(args.m, args.suffix_type, args.d)
    payload = json.dumps(ans, indent=2, sort_keys=True)
    print(payload)
    if args.json:
        with open(args.json, "w", encoding="utf-8") as f:
            f.write(payload + "\n")


if __name__ == "__main__":
    main()
