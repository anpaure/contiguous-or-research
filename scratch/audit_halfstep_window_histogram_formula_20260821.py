#!/usr/bin/env python3
"""Develop/check exact half-step window histograms."""

from __future__ import annotations

from collections import Counter
from math import comb


def direct(b: int, r: int, q: int) -> Counter[int]:
    m = (b - 1) // 2
    bits = [int((m * x) % b < r) for x in range(b)]
    return Counter(sum(bits[(p + j) % b] for j in range(1, q + 1)) for p in range(b))


def direct_joint(b: int, r: int, q: int) -> Counter[tuple[int, int]]:
    m = (b - 1) // 2
    bits = [int((m * x) % b < r) for x in range(b)]
    return Counter(
        (sum(bits[(p + j) % b] for j in range(1, q + 1)), bits[(p + q + 1) % b])
        for p in range(b)
    )


def reconstructed_joint(b: int, r: int, q: int) -> Counter[tuple[int, int]]:
    nq = direct(b, r, q)
    nq1 = direct(b, r, q + 1)
    ans: Counter[tuple[int, int]] = Counter()
    for z in range(q + 1):
        n0 = sum(nq1[t] for t in range(z + 1)) - sum(nq[t] for t in range(z))
        n1 = nq[z] - n0
        if n0:
            ans[(z, 0)] = n0
        if n1:
            ans[(z, 1)] = n1
    return +ans


def h(u: int, ell: int, j: int) -> int:
    if ell <= 0 or j <= 0 or j > min(u, ell):
        return 0
    if j < min(u, ell):
        return 2
    return abs(u - ell) + 1


def even_formula(b: int, r: int, q: int) -> Counter[int]:
    assert q % 2 == 0
    u = q // 2
    d = abs(2 * r - b)
    assert d % 2 == 1
    k = (d - 1) // 2
    eps = 1 if 2 * r > b else -1
    ans: Counter[int] = Counter()
    used = 0
    for j in range(1, min(u, k + 1) + 1):
        v = h(u, k, j) + h(u, k + 1, j)
        if v:
            ans[u + eps * j] += v
            used += v
    ans[u] += b - used
    return +ans


def odd_formula(b: int, r: int, q: int) -> Counter[int]:
    assert q % 2 == 1
    if q == 1:
        return Counter({0: b - r, 1: r})
    m = (b - 1) // 2
    u = (q - 1) // 2
    # Complementation reduces the upper-half case to r0=m-k.
    upper = r >= m + 1
    r0 = b - r if upper else r
    k = m - r0
    ans0: Counter[int] = Counter()
    if k == 0:
        ans0[u] = m + 1 + u
        ans0[u + 1] = m - u
    else:
        for j in range(1, min(u, k) + 1):
            ans0[u - j] = 2 * h(u, k, j)
        ans0[u] = r0 + 3 - u
        ans0[u + 1] = r0 - u
    if not upper:
        return +ans0
    return +Counter({q - z: n for z, n in ans0.items()})


def direct_capacity(b: int, q: int, s: int) -> int:
    return sum(direct(b, r, q).get(s - r, 0) * comb(b, r) ** 2 for r in range(1, b))


def all_direct_histograms(b: int) -> dict[tuple[int, int], Counter[int]]:
    """All payload/window histograms in O(b^3), including q=b."""
    m = (b - 1) // 2
    out: dict[tuple[int, int], Counter[int]] = {}
    for r in range(1, b):
        bits = [int((m * x) % b < r) for x in range(b)]
        weights = [0] * b
        for q in range(1, b + 1):
            for p in range(b):
                weights[p] += bits[(p + q) % b]
            out[r, q] = Counter(weights)
    return out


def cached_capacity(
    b: int, q: int, s: int, histograms: dict[tuple[int, int], Counter[int]]
) -> int:
    return sum(
        histograms[r, q].get(s - r, 0) * comb(b, r) ** 2
        for r in range(1, b)
    )


def even_capacity_formula(b: int, q: int, s: int) -> int:
    m = (b - 1) // 2
    u = q // 2
    kbig = s - (m + u + 1)
    if kbig < 0:
        return even_capacity_formula(b, q, b + q - s)
    B = lambda k: comb(b, m - k) ** 2 if 0 <= k <= m else 0
    meet = lambda ell: 0 if ell <= 0 else u + ell - 1
    ans = (b - meet(kbig) - meet(kbig + 1)) * B(kbig)
    for j in range(1, kbig + 1):
        ans += (h(u, kbig - j, j) + h(u, kbig - j + 1, j)) * B(kbig - j)
    return ans


def odd_capacity_formula(b: int, q: int, s: int) -> int:
    m = (b - 1) // 2
    u = (q - 1) // 2
    kbig = s - (m + u + 1)
    if kbig < 0:
        return odd_capacity_formula(b, q, b + q - s)
    B = lambda k: comb(b, m - k) ** 2 if 0 <= k <= m else 0
    if kbig == 0:
        return 2 * (m - u) * B(0)
    ans = (m - kbig - u) * B(kbig)
    d = m + 1 + u if kbig == 1 else m - kbig + 4 - u
    ans += d * B(kbig - 1)
    for j in range(1, kbig):
        ans += 2 * h(u, kbig - j - 1, j) * B(kbig - j - 1)
    return ans


def main() -> None:
    for b in range(3, 80, 2):
        histograms = all_direct_histograms(b)
        for r in range(1, b):
            for q in range(2, b, 2):
                if q // 2 > min(r, b - r):
                    continue
                got = histograms[r, q]
                want = even_formula(b, r, q)
                assert got == want, (b, r, q, got, want)
            for q in range(1, b + 1, 2):
                if q > 1 and (q - 1) // 2 > min(r, b - r):
                    continue
                got = histograms[r, q]
                want = odd_formula(b, r, q)
                assert got == want, (b, r, q, got, want)
        for s in range(1, b + 1):
            got = cached_capacity(b, 1, s, histograms)
            want = (b - s) * comb(b, s) ** 2 + (s - 1) * comb(b, s - 1) ** 2
            assert got == want, ("q1_capacity", b, s, got, want)
        for q in range(2, b + 1):
            for s in range(q, b + 1):
                got = cached_capacity(b, q, s, histograms)
                want = (even_capacity_formula if q % 2 == 0 else odd_capacity_formula)(b, q, s)
                assert got == want, ("capacity", b, q, s, got, want)
        if b < 40:
            for r in range(1, b):
                for q in range(1, b - 1):
                    assert direct_joint(b, r, q) == reconstructed_joint(b, r, q)
    for b, r, q in [(31, 15, 9), (31, 14, 9), (31, 13, 9), (31, 12, 9),
                    (31, 16, 9), (31, 17, 9), (31, 18, 9), (31, 19, 9),
                    (31, 12, 5), (31, 12, 7), (31, 12, 11), (31, 12, 13),
                    (31, 10, 5), (31, 10, 9), (31, 10, 13)]:
        print("ODD_SAMPLE", b, r, q, sorted(direct(b, r, q).items()))
    print("PASS exact half-step histograms, transitions, and profile sums")


if __name__ == "__main__":
    main()
