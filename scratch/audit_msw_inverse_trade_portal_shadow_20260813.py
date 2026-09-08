#!/usr/bin/env python3
"""Portal-shadow census for the full canonical MSW inverse-triple atlas.

For every Dyck root z of semilength m-2 and every insertion gap, form the
canonical MSW pair obtained by inserting 1100/1010.  Recover its literal
two-row inverse separated-double-swap normal form, construct the positive
pair, and count which rank-(m+1-q) targets occur as cyclic intervals in a
positive row.  Such an occurrence is exactly a clean-package portal.

Substantial instances must be run on h100, not on the local Mac.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
import time
from collections import Counter


def dyck_words(m: int):
    def rec(pos: int, ones: int, bits: list[str]):
        if pos == 2 * m:
            yield "".join(bits)
            return
        if ones < m:
            bits.append("1")
            yield from rec(pos + 1, ones + 1, bits)
            bits.pop()
        zeros = pos - ones
        if zeros < ones:
            bits.append("0")
            yield from rec(pos + 1, ones, bits)
            bits.pop()

    yield from rec(0, 0, [])


def mu(word: str) -> str:
    return word[::-1].translate(str.maketrans("01", "10"))


def rho(word: str) -> list[int]:
    """One-based MSW flip permutation."""
    if not word:
        return []
    height = 0
    close = None
    for i, bit in enumerate(word):
        height += 1 if bit == "1" else -1
        if height == 0:
            close = i
            break
    assert close is not None and word[0] == "1" and word[close] == "0"
    u = word[1:close]
    v = word[close + 1 :]
    d = len(u) + 2
    return [d] + [d - x for x in rho(mu(u))] + [1] + [d + x for x in rho(v)]


def canonical_cycle(seq):
    seq = tuple(seq)
    rots = [seq[i:] + seq[:i] for i in range(len(seq))]
    rev = tuple(reversed(seq))
    rots.extend(rev[i:] + rev[:i] for i in range(len(seq)))
    return min(rots)


def msw_row(word: str) -> tuple[int, ...]:
    m = len(word) // 2
    n = 2 * m + 1
    q = [x - 1 for x in rho(word)] + [2 * m]
    row = tuple(q[(-1 - 2 * j) % n] for j in range(n))
    return canonical_cycle(row)


def windows(row: tuple[int, ...], size: int):
    n = len(row)
    return {
        tuple(sorted(row[(i + j) % n] for j in range(size)))
        for i in range(n)
    }


def recover_inverse_trade(p, q, m):
    """Return positive rows P',Q' from the inverse-pair normal form."""
    n = 2 * m + 1
    cq = canonical_cycle(q)
    for orient in (tuple(p), tuple(reversed(p))):
        for shift in range(n):
            r = orient[shift:] + orient[:shift]
            a, b = r[0], r[1]
            x = r[2:m]
            c, d = r[m], r[m + 1]
            y = r[m + 2 :]
            assert len(x) == m - 2 and len(y) == m - 1
            q_template = (b, d) + x + (a, c) + y
            if canonical_cycle(q_template) != cq:
                continue
            pp = canonical_cycle((b, a) + x + (d, c) + y)
            qp = canonical_cycle((d, b) + x + (c, a) + y)
            if windows(p, m) | windows(q, m) != windows(pp, m) | windows(qp, m):
                continue
            if windows(p, m) & windows(q, m):
                continue
            if windows(pp, m) & windows(qp, m):
                continue
            return pp, qp
    raise AssertionError((p, q, m))


def build_factor(m: int):
    roots = list(dyck_words(m))
    rows = {word: msw_row(word) for word in roots}
    seen = set()
    for row in rows.values():
        ws = windows(row, m)
        if seen & ws:
            raise AssertionError("MSW rows overlap")
        seen |= ws
    assert len(seen) == math.comb(2 * m + 1, m)
    return roots, rows


def pbbs_owner(m: int, height: int) -> frozenset[int]:
    word = "0" + "1" * height + "0" * height + "10" * (m - height)
    assert len(word) == 2 * m + 1
    return frozenset(i for i, bit in enumerate(word) if bit == "0")


def internal_pbbs_casualties(m: int, d: int, q0: int):
    """Definite casualties whose whole interval stays on the U_2,U_3,... spine."""
    out = []
    for h in range(4, d + 1):
        # This helper only certifies intervals wholly contained in the explicit
        # height spine U_2,...,U_m.  Intervals reaching either exterior context
        # are deliberately left out of the finite census.
        for start in range(max(2, h - q0 + 1), min(h, m - q0) + 1):
            owners = [pbbs_owner(m, t) for t in range(start, start + q0 + 1)]
            target = frozenset.intersection(*owners)
            if len(target) == m + 1 - q0:
                out.append((h, start, tuple(sorted(target))))
    return out


def audit(m: int, q_values: list[int], pbbs_d: int | None):
    started = time.time()
    roots, rows = build_factor(m)
    smaller = list(dyck_words(m - 2))
    trades = []
    negative_pair_seen = set()
    for z in smaller:
        for gap in range(len(z) + 1):
            x = z[:gap] + "1100" + z[gap:]
            y = z[:gap] + "1010" + z[gap:]
            p, r = rows[x], rows[y]
            neg = tuple(sorted((p, r)))
            assert neg not in negative_pair_seen
            negative_pair_seen.add(neg)
            pp, rr = recover_inverse_trade(p, r, m)
            trades.append((neg, (pp, rr)))

    assert len(trades) == (2 * m - 3) * math.comb(2 * (m - 2), m - 2) // (m - 1)

    out = {}
    n = 2 * m + 1
    for q0 in q_values:
        s = m + 1 - q0
        if not (1 <= s < n):
            continue
        degrees = Counter()
        occurrence_count = 0
        duplicate_within_trade = 0
        for _, pos in trades:
            occ = []
            for row in pos:
                ws = windows(row, s)
                occurrence_count += len(ws)
                occ.extend(ws)
            unique = set(occ)
            duplicate_within_trade += len(occ) - len(unique)
            for target in unique:
                degrees[target] += 1
        total_targets = math.comb(n, s)
        hist = Counter(degrees.values())
        hist[0] = total_targets - len(degrees)
        all_targets = set(itertools.combinations(range(n), s))
        missing = sorted(all_targets - set(degrees))
        out[str(q0)] = {
            "target_rank": s,
            "targets": total_targets,
            "covered_targets": len(degrees),
            "missing_targets": total_targets - len(degrees),
            "missing_target_sample": [list(x) for x in missing[:100]],
            "minimum_positive_degree": min(degrees.values(), default=0),
            "maximum_degree": max(degrees.values(), default=0),
            "degree_hist": {str(k): v for k, v in sorted(hist.items())},
            "portal_occurrences": occurrence_count,
            "average_occurrence_degree": occurrence_count / total_targets,
            "average_distinct_trade_degree": sum(degrees.values()) / total_targets,
            "duplicates_within_trade": duplicate_within_trade,
        }
        if pbbs_d is not None and pbbs_d <= m:
            casualties = internal_pbbs_casualties(m, pbbs_d, q0)
            out[str(q0)]["pbbs_internal_casualty_occurrences"] = len(casualties)
            out[str(q0)]["pbbs_internal_casualty_targets"] = len({x[2] for x in casualties})
            out[str(q0)]["pbbs_internal_casualty_missing_portal"] = [
                {"height": h, "start": a, "target": list(target)}
                for h, a, target in casualties if target not in degrees
            ]
            out[str(q0)]["pbbs_internal_casualty_min_degree"] = min(
                (degrees[target] for _, _, target in casualties), default=None
            )

    neg_row_degree = Counter()
    for neg, _ in trades:
        for row in neg:
            neg_row_degree[row] += 1
    return {
        "m": m,
        "n": n,
        "catalan": len(roots),
        "trades": len(trades),
        "negative_rows_used": len(neg_row_degree),
        "negative_row_trade_degree_hist": {
            str(k): v for k, v in sorted(Counter(neg_row_degree.values()).items())
        },
        "q": out,
        "seconds": time.time() - started,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("m", type=int)
    ap.add_argument("--q", type=int, action="append")
    ap.add_argument("--json")
    ap.add_argument("--pbbs-d", type=int)
    args = ap.parse_args()
    q_values = args.q or list(range(2, min(args.m, 8) + 1))
    result = audit(args.m, q_values, args.pbbs_d)
    payload = json.dumps(result, indent=2, sort_keys=True)
    print(payload)
    if args.json:
        with open(args.json, "w", encoding="utf-8") as out:
            out.write(payload + "\n")


if __name__ == "__main__":
    main()
