#!/usr/bin/env python3
"""Exact checks for the product-hook SCD color ledger.

This script uses only integer arithmetic for the identities and Decimal only
for human-readable normalized output.
"""

from decimal import Decimal, getcontext
from math import comb, isqrt


def chain_counts(b):
    h = (b - 1) // 2
    return [comb(b, d) - (comb(b, d - 1) if d else 0) for d in range(h + 1)]


def rectangle_size(b, q, a, c):
    gap = abs(a - c)
    return max(0, b - 2 * max(a, c) + 1 - max(0, q - gap))


def hook_color(q, a, c):
    # Equal-bottom rectangles use the vertical-then-horizontal convention,
    # hence their post-middle leg is all A.
    if a >= c:
        return max(0, q - (a - c))
    return min(q, c - a)


def global_ledger(b, q):
    cc = chain_counts(b)
    load = [0] * (q + 1)
    equal = 0
    for a, ca in enumerate(cc):
        for c, cb in enumerate(cc):
            n = rectangle_size(b, q, a, c)
            value = ca * cb * n
            load[hook_color(q, a, c)] += value
            if a == c:
                equal += value
    return load, equal


def profile_ledger(b, q):
    """Enumerate the exact source-profile ledger of the canonical hooks."""
    cc = chain_counts(b)
    out = [[0] * (q + 1) for _ in range(b + 1)]
    for a, ca in enumerate(cc):
        for c, cb in enumerate(cc):
            z = hook_color(q, a, c)
            if a >= c:
                # Source split r=a+k; height above the middle is b-c-r.
                lo, hi = a, min(b - a, b - c - q)
            else:
                # Source split r=b-c-k; height above the middle is r-a.
                lo, hi = max(c, a + q), b - c
            for r in range(max(0, lo), min(b, hi) + 1):
                out[r][z] += ca * cb
    return out


def direct_hooks(b, a, c):
    """Return the coordinate chains of the canonical rectangle hook SCD."""
    p, s = b - 2 * a, b - 2 * c
    chains = []
    if a >= c:  # p <= s: vertical B, then horizontal A
        for k in range(p + 1):
            chain = [(k, j) for j in range(s - k + 1)]
            chain += [(i, s - k) for i in range(k + 1, p + 1)]
            chains.append(chain)
    else:  # s < p: horizontal A, then vertical B
        for k in range(s + 1):
            chain = [(i, k) for i in range(p - k + 1)]
            chain += [(p - k, j) for j in range(k + 1, s + 1)]
            chains.append(chain)
    return chains


def exact_checks():
    for b in range(3, 20, 2):
        h = (b - 1) // 2
        for a in range(h + 1):
            for c in range(h + 1):
                p, s = b - 2 * a, b - 2 * c
                hooks = direct_hooks(b, a, c)
                cells = [cell for chain in hooks for cell in chain]
                assert len(cells) == (p + 1) * (s + 1)
                assert len(set(cells)) == len(cells)
                for chain in hooks:
                    ranks = [i + j for i, j in chain]
                    assert ranks == list(range(ranks[0], ranks[-1] + 1))
                    assert ranks[0] + ranks[-1] == p + s
                for q in range(1, b + 1):
                    active = sum(
                        1
                        for chain in hooks
                        if any(i + j == (p + s) // 2 + q for i, j in chain)
                    )
                    assert active == rectangle_size(b, q, a, c)

        wb = comb(2 * b, b)
        for q in range(1, b + 1):
            load, equal = global_ledger(b, q)
            profiles = profile_ledger(b, q)
            assert sum(load) == comb(2 * b, b + q)
            assert [sum(profiles[r][z] for r in range(b + 1)) for z in range(q + 1)] == load
            cc = chain_counts(b)
            expected_equal = sum(
                cc[d] ** 2 * max(0, b - 2 * d - q + 1)
                for d in range((b - 1) // 2 + 1)
            )
            assert equal == expected_equal
            interior_formula = 2 * sum(
                cc[a] * cc[c] * rectangle_size(b, q, a, c)
                for a in range(h + 1)
                for c in range(a + 1, min(h, a + q - 1) + 1)
            )
            assert sum(load[1:q]) == interior_formula
            # The total clustered capacity of all interior colors, even
            # before restricting to the genuine payload interval.
            if q > 1:
                # For any central payload interval, the convenient upper
                # bound replaces its sum of L_r by the full Vandermonde W_b.
                interior_cap_numerator = 2 * (q - 1) * (wb - 2)
                assert interior_cap_numerator == sum(
                    2 * comb(b, r) ** 2
                    for r in range(1, b)
                    for _z in range(1, q)
                )
                assert interior_cap_numerator <= 2 * (q - 1) * wb


def asymptotic_table():
    getcontext().prec = 30
    print("b q target/W interior/W interior-cap/W forced-delete/W equal/W sum_q_equal/W")
    for b in [101, 251, 503, 1009, 2003]:
        q = isqrt(b)
        load, equal = global_ledger(b, q)
        wb = comb(2 * b, b)
        interior = sum(load[1:q])
        cap_num = 2 * (q - 1) * wb
        forced_num = max(0, b * interior - cap_num)
        vals = [
            Decimal(comb(2 * b, b + q)) / Decimal(wb),
            Decimal(interior) / Decimal(wb),
            Decimal(cap_num) / Decimal(b * wb),
            Decimal(forced_num) / Decimal(b * wb),
            Decimal(equal) / Decimal(wb),
            Decimal(
                sum(
                    cd * cd * ell * (ell + 1) // 2
                    for d, cd in enumerate(chain_counts(b))
                    for ell in [b - 2 * d]
                )
            )
            / Decimal(wb),
        ]
        print(b, q, *(f"{v:.12g}" for v in vals))


if __name__ == "__main__":
    exact_checks()
    print("exact hook/ledger checks: PASS")
    asymptotic_table()
