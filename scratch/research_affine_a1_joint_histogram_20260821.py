#!/usr/bin/env python3
"""Exact-histogram aggregate of the affine A1 ledger (float rho arithmetic)."""

from __future__ import annotations

import argparse
import functools
import math
import numpy as np

from research_affine_histogram_recurrence_20260821 import (
    lc,
    neven,
    nodd,
    rho_even,
    rho_odd,
)


def hist(b: int, q: int, k: int) -> np.ndarray:
    h = (b - 1) // 2
    out = np.zeros(q + 1, dtype=np.int64)
    if q == 1:
        out[0] = h - k
        out[1] = h + 1 + k
        return out
    if q % 2 == 0:
        u = q // 2
        for d in range(min(u, k + 1) + 1):
            out[u + d] = neven(b, u, k, d)
    else:
        u = (q - 1) // 2
        for d in range(min(u, k) + 2):
            out[u + d] = nodd(b, u, k, d)
    assert int(out.sum()) == b, (b, q, k, out, out.sum())
    return out


def make_rho(b: int):
    h = (b - 1) // 2

    @functools.cache
    def rho(q: int, K: int) -> float:
        if q == 1:
            s = h + 1 + K
            ratio = (b - s + 1) / s
            t_over_p = ((b - s) * ratio + (s - 1) / ratio) / b
            return min(1.0, 1.0 / t_over_p)
        if q % 2 == 0:
            return rho_even(b, q // 2, K)
        return rho_odd(b, (q - 1) // 2, K)

    return rho


def profile_K(q: int, k: int, z: int) -> int:
    if q % 2 == 1:
        return k + z - (q - 1) // 2
    # Even target displacement is a half-integer.  The only crossing case
    # k=z-q/2=0 maps from +1/2 to -1/2 and has the same symmetric rho.
    raw = k + z - q // 2
    return raw if raw >= 0 else -raw - 1


def run(b: int, H: int, kmax: int) -> None:
    h = (b - 1) // 2
    logW = lc(2 * b, b)
    rho = make_rho(b)
    total = 0.0
    eventmass = 0.0
    qsum = np.zeros(H + 1)
    qevent = np.zeros(H + 1)
    ksum: dict[int, float] = {}
    omitted_source = 0.0
    cats: dict[tuple[str, int, int], list[float]] = {}
    for k in range(h - b // 4 + 1):
        r = h + 1 + k
        pair_source_mass = 2.0 * math.exp(2 * lc(b, r) - logW)
        if k > kmax:
            omitted_source += pair_source_mass
            continue
        phase_weight = pair_source_mass / b
        ktot = 0.0
        for q in range(1, H):
            n0 = hist(b, q, k)
            n1 = hist(b, q + 1, k)
            c0 = np.cumsum(n0)
            c1 = np.cumsum(n1)
            for z in np.flatnonzero(n0):
                z = int(z)
                prev_c0 = int(c0[z - 1]) if z else 0
                Nzero = int(c1[z]) - prev_c0
                None_count = int(n0[z]) - Nzero
                assert Nzero >= 0 and None_count >= 0
                oldK = profile_K(q, k, z)
                old = rho(q, oldK)
                for bit, number in ((0, Nzero), (1, None_count)):
                    if not number:
                        continue
                    newK = profile_K(q + 1, k, z + bit)
                    inc = max(rho(q + 1, newK) - old, 0.0)
                    mass = phase_weight * number
                    total += mass * inc
                    ktot += mass * inc
                    qsum[q + 1] += mass * inc
                    if inc > 0:
                        eventmass += mass
                        qevent[q + 1] += mass
                        dcur = z - (q // 2 if q % 2 == 0 else (q - 1) // 2)
                        key = (("E" if q % 2 == 0 else "O") + ("O" if (q + 1) % 2 else "E"), bit, dcur)
                        rec = cats.setdefault(key, [0.0, 0.0])
                        rec[0] += mass * inc
                        rec[1] += mass
        if ktot:
            ksum[k] = ktot
    print("A1AGG", b, H, kmax, "A1", total, "eventmass", eventmass, "omitted_source", omitted_source)
    print("scales", "b/H*A1", b / H * total, "sqrtb*A1", math.sqrt(b) * total, "H*A1", H * total)
    print("topq", sorted(((qsum[q], q, qevent[q]) for q in range(2, H + 1)), reverse=True)[:20])
    print("topk", sorted(((v, k) for k, v in ksum.items()), reverse=True)[:20])
    print("rhocache", rho.cache_info())
    print("topcats", sorted(((v[0], key, v[1]) for key, v in cats.items()), reverse=True)[:30])


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("b", type=int)
    ap.add_argument("H", type=int)
    ap.add_argument("kmax", type=int)
    z = ap.parse_args()
    run(z.b, z.H, z.kmax)


if __name__ == "__main__":
    main()
