#!/usr/bin/env python3
"""H100-only exact DP for the two-period near-C centre character."""

from __future__ import annotations

import argparse


def options(q: int, rhs: int, bound: int):
    raw = [
        (a, b, abs(a) + abs(b))
        for a in range(-bound, bound + 1)
        for b in range(-bound, bound + 1)
        if (2 * a + 3 * b - rhs) % q == 0
    ]
    # Keep only one cheapest representative of every local (a,b), then
    # discard choices already more expensive than the trivial O(q) shore.
    return [row for row in raw if row[2] <= q]


def extend(dp, opts, cap):
    out = {}
    for (sa, sb), (cost, rows) in dp.items():
        for a, b, w in opts:
            na, nb = sa + a, sb + b
            if abs(na) > cap or abs(nb) > cap:
                continue
            cand = (cost + w, rows + [(a, b)])
            if (na, nb) not in out or cand[0] < out[(na, nb)][0]:
                out[(na, nb)] = cand
    return out


def audit(q: int, exterior: int, bound: int):
    # An optimum of interest has total l1 at most 4q.  Any partial sum
    # outside this box cannot return at smaller l1 cost.
    cap = 4 * q
    dp = {(0, 0): (0, [])}
    for _ in range(q + 1):
        dp = extend(dp, options(q, 1, bound), cap)
    for _ in range(exterior):
        dp = extend(dp, options(q, 0, bound), cap)
    cost, rows = dp[(-1, 1)]
    pos = sum(max(a, 0) + max(b, 0) for a, b in rows)
    neg = sum(max(-a, 0) + max(-b, 0) for a, b in rows)
    assert pos == neg == cost // 2
    print(
        "CHAR_MIN", q,
        "exterior", exterior,
        "l1", cost,
        "shore", pos,
        "H", rows[:q + 1],
        "E", rows[q + 1:],
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--q-max", type=int, default=12)
    ap.add_argument("--exterior", type=int, default=4)
    ap.add_argument("--bound-factor", type=int, default=2)
    args = ap.parse_args()
    for q in range(2, args.q_max + 1):
        audit(q, args.exterior, args.bound_factor * q)


if __name__ == "__main__":
    main()
