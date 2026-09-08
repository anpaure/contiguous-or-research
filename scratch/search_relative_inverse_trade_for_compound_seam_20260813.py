#!/usr/bin/env python3
"""Search a minimal universal two-row relative trade installing C4--U5.

Substantial runs belong on h100.  The host is the complete offset-zero
first-aligned MSW packet factor.  Negative rows belonging to the selected
internal-portal bank are forbidden.  Candidates are exact at ranks m and
m+1 by the universal identity; the script separately measures rank-(m+2)
upper current.
"""

from __future__ import annotations

import argparse
import collections
import json

import audit_msw_inverse_trade_portal_shadow_20260813 as base
import audit_pbbs_portal_compound_coexistence_20260813 as co


def upper_counter(rows, m):
    return collections.Counter(
        frozenset(x) for row in rows for x in base.windows(row, m + 2)
    )


def owner_edges(row, m):
    n = 2 * m + 1
    owners = [co.cyc_window(row, t, m + 1) for t in range(n)]
    return {
        frozenset((owners[t], owners[(t + 1) % n])) for t in range(n)
    }


def selected_portal_rows(m, d):
    out = set()
    _, canonical_rows = base.build_factor(m)
    tasks = [
        (A, q)
        for q in range(2, d)
        for A in range(q + 1, d + 1)
        if A <= m - q
    ]
    if d + 1 <= m - d:
        tasks.append((d + 1, d))
    for A, q in tasks:
        z = co.z_word(m, A, q)
        neg = (canonical_rows["1100" + z], canonical_rows["1010" + z])
        out.update(base.recover_inverse_trade(*neg, m))
    return out


def candidate_from_normalized_c(r, m):
    delta, gamma = r[0], r[1]
    E = r[2 : m + 1]
    beta, alpha = r[m + 1], r[m + 2]
    O = r[m + 3 :]
    assert len(E) == m - 1 and len(O) == m - 2
    d = (beta, delta) + E + (alpha, gamma) + O
    cp = (delta, beta) + E + (gamma, alpha) + O
    dp = (gamma, delta) + E + (alpha, beta) + O
    return (
        base.canonical_cycle(d),
        base.canonical_cycle(cp),
        base.canonical_cycle(dp),
    )


def search(m, d):
    neg_packet, pos_packet, factor = co.full_first_aligned_packet(m)
    factor = set(factor)
    protected = selected_portal_rows(m, d)
    assert protected <= factor
    target = frozenset((co.c_owner(m, 4), co.height_owner(m, 5)))
    found = {}
    seen_pairs = set()
    for p in factor:
        if p in protected:
            continue
        for orient in (p, tuple(reversed(p))):
            for shift in range(2 * m + 1):
                r = orient[shift:] + orient[:shift]
                mate, cp, dp = candidate_from_normalized_c(r, m)
                if mate not in factor or mate in protected or mate == p:
                    continue
                neg = tuple(sorted((p, mate)))
                if neg in seen_pairs:
                    continue
                seen_pairs.add(neg)
                pos = tuple(sorted((cp, dp)))
                if target not in owner_edges(cp, m) and target not in owner_edges(dp, m):
                    continue
                assert (
                    base.windows(p, m) | base.windows(mate, m)
                    == base.windows(cp, m) | base.windows(dp, m)
                )
                upper_neg = upper_counter(neg, m)
                upper_pos = upper_counter(pos, m)
                key = "upper_exact" if upper_neg == upper_pos else "upper_changed"
                if key not in found:
                    found[key] = {
                        "negative_rows": [list(x) for x in neg],
                        "positive_rows": [list(x) for x in pos],
                        "upper_removed": [
                            list(x) for x in sorted((upper_neg - upper_pos).elements())
                        ],
                        "upper_added": [
                            list(x) for x in sorted((upper_pos - upper_neg).elements())
                        ],
                    }
                if "upper_exact" in found and "upper_changed" in found:
                    return {
                        "m": m,
                        "d": d,
                        "factor_rows": len(factor),
                        "protected_rows": len(protected),
                        "pairs_examined": len(seen_pairs),
                        "found": found,
                    }
    return {
        "m": m,
        "d": d,
        "factor_rows": len(factor),
        "protected_rows": len(protected),
        "pairs_examined": len(seen_pairs),
        "found": found,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pairs", nargs="+", help="m:d")
    ap.add_argument("--json")
    args = ap.parse_args()
    out = [search(*map(int, x.split(":"))) for x in args.pairs]
    payload = json.dumps(out, indent=2, sort_keys=True)
    print(payload)
    if args.json:
        with open(args.json, "w", encoding="utf-8") as f:
            f.write(payload + "\n")


if __name__ == "__main__":
    main()
