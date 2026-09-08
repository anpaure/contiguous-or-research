#!/usr/bin/env python3
"""H100 audit for the half-step affine isolated-spike coefficient maps.

This checker uses exact integers/Fractions.  It independently checks:

* the closed odd/even central profile-load formulae against literal cyclic
  word enumeration;
* the elementary binomial-ratio inequalities used by the coefficient maps;
* the isolated two-step-spike implication on every bulk affine path in a
  collection of finite exact instances; and
* the exact reachability formula for the two exits from the unique 1-run.

The finite rows are an audit of the proof kernel, not an asymptotic proof.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb


def lam(h: int, j: int) -> Fraction:
    return Fraction(h - j, h + j + 2)


def lval(b: int, j: int) -> int:
    h = (b - 1) // 2
    return comb(b, h + 1 + j) ** 2


def fodd(b: int, u: int, K: int) -> int:
    """Return b*T_(2u+1,h+1+u+K) in the untruncated central range."""
    h = (b - 1) // 2
    L = lambda j: lval(b, j)
    if u == 0:
        if K == 0:
            return 2 * h * L(0)
        # At q=1 the d=1 term is also the nominal endpoint, so it must
        # not be counted twice by the u>=1 large-K display below.
        return (h - K) * L(K) + (h + K) * L(K - 1)
    if K == 0:
        return 2 * (h - u) * L(0)
    if K == 1:
        return (h - u - 1) * L(1) + (h + u + 1) * L(0)
    A = h - u - K
    ans = A * L(K) + (A + 4) * L(K - 1)
    if K <= 2 * u:
        if K % 2 == 0:
            v = K // 2
            ans += 4 * sum(L(j) for j in range(v, K - 1))
        else:
            v = (K - 1) // 2
            ans += 4 * sum(L(j) for j in range(v + 1, K - 1))
            ans += 2 * (u - v + 1) * L(v)
    else:
        ans += 4 * sum(L(j) for j in range(K - u, K - 1))
        ans += 2 * (K - 2 * u) * L(K - u - 1)
    return ans


def feven(b: int, u: int, K: int) -> int:
    """Return b*T_(2u,h+1+u+K) in the untruncated central range."""
    h = (b - 1) // 2
    L = lambda j: lval(b, j)
    if K == 0:
        return (2 * h + 1 - u) * L(0)
    A = h + 1 - u - K
    ans = 2 * A * L(K)
    if K <= 2 * u:
        if K % 2 == 0:
            v = K // 2
            ans += 4 * sum(L(j) for j in range(v + 1, K))
            ans += (u - v + 3) * L(v)
        else:
            v = (K - 1) // 2
            ans += 4 * sum(L(j) for j in range(v + 1, K))
            ans += (u - v) * L(v)
    else:
        ans += 4 * sum(L(j) for j in range(K - u + 1, K))
        ans += (2 * (K - 2 * u) + 3) * L(K - u)
    return ans


def quota(b: int, q: int, s: int) -> int:
    if not (0 <= s <= b and 0 <= s - q <= b):
        return 0
    return comb(b, s) * comb(b, s - q)


def rho_formula(b: int, q: int, K: int) -> Fraction:
    h = (b - 1) // 2
    if q % 2:
        u = (q - 1) // 2
        s = h + 1 + u + K
        F = fodd(b, u, K)
    else:
        u = q // 2
        s = h + 1 + u + K
        F = feven(b, u, K)
    x = Fraction(b * quota(b, q, s), F)
    return min(Fraction(1), x)


def literal_profile_loads(b: int, H: int) -> list[list[int]]:
    """Return F=b*T as exact integers for the retained source band."""
    h = (b - 1) // 2
    g = b // 4
    m = h
    out = [[0] * (2 * b + 1) for _ in range(H + 1)]
    for r in range(g, b - g + 1):
        bits = [int((m * x) % b < r) for x in range(b)]
        for p in range(b):
            z = 0
            for q in range(1, H + 1):
                z += bits[(p + q) % b]
                out[q][r + z] += comb(b, r) ** 2
    return out


def check_closed_forms() -> int:
    checks = 0
    for b, H in [(61, 7), (101, 9), (151, 10), (203, 11)]:
        h = (b - 1) // 2
        direct = literal_profile_loads(b, H)
        for q in range(1, H + 1):
            u = q // 2 if q % 2 == 0 else (q - 1) // 2
            for K in range(0, 2 * H + 1):
                s = h + 1 + u + K
                if s > 2 * b:
                    continue
                got = fodd(b, u, K) if q % 2 else feven(b, u, K)
                assert got == direct[q][s], (b, q, K, got, direct[q][s])
                checks += 1
    return checks


def check_ratio_kernel() -> int:
    checks = 0
    # These deliberately use much broader ranges than the theorem's
    # G+H=o(h) bulk.  The asserted inequalities are the exact coefficient
    # comparisons used in the proof.
    for h in [64, 96, 128, 192, 256, 384, 512]:
        H = h // 16 - 2
        for u in range(1, H // 2 + 1):
            for K in range(0, 2 * H + 1):
                x = u + K
                if x + 4 >= h:
                    continue
                A = h - x
                R2 = lam(h, x) * lam(h, x + 1)
                assert Fraction(A - 2, A) * lam(h, K) ** 2 >= R2
                checks += 1
                R4 = Fraction(1)
                for t in range(4):
                    R4 *= lam(h, x + t)
                assert Fraction(A - 4, A) * lam(h, K) ** 2 * lam(h, K + 1) ** 2 >= R4
                checks += 1
                # Path-feasible boundary-normal comparison, K=2k, k<=u.
                if K % 2 == 0 and K // 2 <= u and K >= 2:
                    y = K - u - 2
                    Rb = lam(h, x) * lam(h, x + 1) * lam(h, x + 2) / lam(h, y)
                    assert Fraction(A - 3, A) * lam(h, K) ** 2 >= Rb
                    for j in range(K // 2, K - 1):
                        assert lam(h, j) ** 2 >= Rb
                    checks += 1
    return checks


def check_isolated_paths() -> int:
    checks = 0
    for b, H, G in [(101, 9, 7), (151, 11, 9), (251, 15, 12), (401, 19, 15)]:
        h = (b - 1) // 2
        m = h
        # Formula loads are exact on all upper profiles reached here because
        # K<=G+ceil(H/2) lies strictly inside the retained source band.
        for k in range(G + 1):
            r = h + 1 + k
            bits = [int((m * x) % b < r) for x in range(b)]
            for p in range(b):
                z = 0
                vals: list[Fraction] = []
                Ks: list[int] = []
                for q in range(1, H + 1):
                    z += bits[(p + q) % b]
                    u = q // 2 if q % 2 == 0 else (q - 1) // 2
                    K = r + z - (h + 1 + u)
                    assert K >= 0
                    Ks.append(K)
                    vals.append(rho_formula(b, q, K))
                for j in range(H - 4):
                    if vals[j + 2] > vals[j]:
                        assert vals[j + 4] <= vals[j], (
                            b,
                            H,
                            k,
                            p,
                            j + 1,
                            Ks[j],
                            vals[j],
                            vals[j + 2],
                            vals[j + 4],
                        )
                    checks += 1
        # The lower half is the complement-shift image and has identical
        # rho values.  Check the profile symmetry directly from literal T.
        direct = literal_profile_loads(b, H)
        for q in range(1, H + 1):
            for s in range(2 * b + 1):
                ss = b + q - s
                if 0 <= ss <= 2 * b:
                    assert direct[q][s] == direct[q][ss]
                    checks += 1
    return checks


def check_run_exit_formula() -> int:
    checks = 0
    for b in [61, 101, 151, 251]:
        h = (b - 1) // 2
        m = h
        for k in range(1, 14):
            r = h + 1 + k
            bits = [int((m * x) % b < r) for x in range(b)]
            for u in range(1, 12):
                for j in range(2 * k + 1):
                    x = (-2 * k + j) % b
                    assert bits[x] == bits[(x + 1) % b] == 1
                    p = (x - 2 * u - 2) % b
                    z = sum(bits[(p + t) % b] for t in range(1, 2 * u + 2))
                    K = k + z - u
                    assert K == k + min(u + 1, (j + 1) // 2)
                    next_is_aa = bits[(x + 2) % b] == bits[(x + 3) % b] == 1
                    assert next_is_aa == (j <= 2 * k - 2)
                    if not next_is_aa:
                        assert K == k + min(u + 1, k)
                    checks += 1
    return checks


def main() -> None:
    counts = {
        "closed_forms": check_closed_forms(),
        "ratio_kernel": check_ratio_kernel(),
        "isolated_paths": check_isolated_paths(),
        "run_exits": check_run_exit_formula(),
    }
    print("AFFINE_ISOLATED_SPIKE_COEFFICIENT_MAP_AUDIT_PASS", counts)


if __name__ == "__main__":
    main()
