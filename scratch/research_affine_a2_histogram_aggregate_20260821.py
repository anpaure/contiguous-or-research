#!/usr/bin/env python3
"""Aggregate odd-defect A2 ledger using exact histogram rho values."""

from __future__ import annotations

import argparse
import functools
import math
import numpy as np


def lc(n: int, k: int) -> float:
    if not 0 <= k <= n:
        return float("-inf")
    return math.lgamma(n + 1) - math.lgamma(k + 1) - math.lgamma(n - k + 1)


def lse(xs: list[float]) -> float:
    m = max(xs)
    return m + math.log(sum(math.exp(x - m) for x in xs))


def nodd(b: int, u: int, k: int, d: int) -> int:
    h = (b - 1) // 2
    if k == 0:
        return h - u if d == 0 else h + u + 1 if d == 1 else 0
    D = min(u, k) + 1
    if d == 0:
        return h - u - k
    if d == 1:
        return h - u - k + 3
    if 2 <= d < D:
        return 4
    if d == D:
        return 2 * (abs(u - k) + 1)
    return 0


def make_rho(b: int):
    h = (b - 1) // 2

    @functools.cache
    def rho(u: int, K: int) -> float:
        qlog = lc(b, h + 1 + K + u) + lc(b, h + K - u)
        if K == 0:
            terms = [math.log(2 * (h - u)) + 2 * lc(b, h + 1)]
        else:
            terms = []
            lo = max(0, K - u - 1, (K - 2) // 2)
            for k in range(lo, K + 1):
                d = K - k
                n = nodd(b, u, k, d)
                if n:
                    terms.append(math.log(n) + 2 * lc(b, h + 1 + k))
        lr = lse(terms) - math.log(b) - qlog
        return min(1.0, math.exp(-lr)) if lr < 745 else 0.0

    return rho


def window_sums(bits: np.ndarray, q: int, starts: np.ndarray) -> np.ndarray:
    b = len(bits)
    twice = np.concatenate([bits, bits])
    pref = np.concatenate([np.zeros(1, dtype=np.int32), np.cumsum(twice, dtype=np.int32)])
    left = starts + 1
    return pref[left + q] - pref[left]


def run(b: int, H: int, kmax: int) -> None:
    h = (b - 1) // 2
    rho = make_rho(b)
    logW = lc(2 * b, b)
    phases = np.arange(b, dtype=np.int64)
    total = 0.0
    eventmass = 0.0
    defect_support = 0.0
    qrows = []
    krows: dict[int, tuple[float, float]] = {}
    omitted_source = 0.0
    local_viol_mass = 0.0
    local_viol_max = (-1.0, None)
    for k in range(h // 2 + 1):
        r = h + 1 + k
        pair_source_mass = 2.0 * math.exp(2 * lc(b, r) - logW)
        if k > kmax:
            omitted_source += pair_source_mass
            continue
        phase_weight = pair_source_mass / b
        # Explicit physical upper word.  The lower word is its complement-reflection
        # and has the same defect-transition histogram.
        mult = h
        bits = (((mult * phases) % b) < r).astype(np.int8)
        ktot = 0.0
        kev = 0.0
        # u=0 is the schedule-independent q=1 row and is handled separately
        # in proofs; this probe covers the nontrivial odd histogram q>=3.
        for u in range(1, (H - 3) // 2 + 1):
            q = 2 * u + 1
            # q -> q+2 adds positions p+q+1,p+q+2.
            defect_p = phases[(bits[(phases + q + 1) % b] == 1) & (bits[(phases + q + 2) % b] == 1)]
            assert len(defect_p) == 2 * k + 1
            zs = window_sums(bits, q, defect_p)
            Ks = k + zs - u
            vals = np.array([max(rho(u + 1, int(K) + 1) - rho(u, int(K)), 0.0) for K in Ks])
            next_a = bits[(defect_p + q + 3) % b] + bits[(defect_p + q + 4) % b]
            assert np.all((next_a == 1) | (next_a == 2))
            K2s = Ks + next_a
            local = np.array([
                min(rho(u + 1, int(K) + 1), rho(u + 2, int(K2))) - rho(u, int(K))
                for K, K2 in zip(Ks, K2s)
            ])
            bad = (vals > 0) & (local > 1e-14)
            local_viol_mass += phase_weight * int(np.count_nonzero(bad))
            if np.any(bad):
                jj = int(np.argmax(np.where(bad, local, -1.0)))
                if local[jj] > local_viol_max[0]:
                    local_viol_max = (float(local[jj]), (k, q, int(defect_p[jj]), int(Ks[jj]), int(next_a[jj]), rho(u, int(Ks[jj])), rho(u + 1, int(Ks[jj]) + 1), rho(u + 2, int(K2s[jj]))))
            inc = phase_weight * float(vals.sum())
            ev = phase_weight * int(np.count_nonzero(vals > 0))
            total += inc
            eventmass += ev
            defect_support += phase_weight * len(defect_p)
            ktot += inc
            kev += ev
            qrows.append((inc, q, k, float(vals.max(initial=0.0)), len(defect_p), int(np.count_nonzero(vals > 0))))
        if ktot:
            krows[k] = (ktot, kev)
    print("AGG", b, H, kmax, "A2", total, "eventmass", eventmass, "defectsupport", defect_support, "omitted_source", omitted_source)
    print("scales", "b/H*A2", b / H * total, "b2/H2*A2", b * b / (H * H) * total, "sqrtb/H*A2", math.sqrt(b) / H * total, "H*A2", H * total)
    print("topqk", sorted(qrows, reverse=True)[:20])
    print("topk", sorted(((v[0], k, v[1]) for k, v in krows.items()), reverse=True)[:20])
    print("cache", rho.cache_info())
    print("local_return_viol", local_viol_mass, local_viol_max)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("b", type=int)
    ap.add_argument("H", type=int)
    ap.add_argument("kmax", type=int)
    z = ap.parse_args()
    run(z.b, z.H, z.kmax)


if __name__ == "__main__":
    main()
