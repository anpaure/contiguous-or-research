#!/usr/bin/env python3
"""C20 (block 75.8): scale test of the DILUTION TAX.

C19 showed at n = 15: INTER(0.9) loses to greedy INTER(1.0) by a
factor ~1.4-1.6 in final misses at slack 1.2, while restoring late
access.  The conditional route 75.5 is asymptotic; its live/dead
test is whether the tax ratio

    R(n) = miss(INTER(0.9)) / miss(INTER(1.0))

shrinks toward 1 as n grows (route alive: provability tax vanishes)
or grows (route dead at fixed slack).  PREREGISTERED: the 75.5
reading predicts R(n) non-increasing in n at fixed slack and sigma
law; if R(n) grows, mark 75.5 empirically dead at fixed slack.
n in {17, 19}, sigma in {round(0.7 sqrt(n ln n)), round(1.1 sqrt(n
ln n))}, p in {0.9, 1.0}, slack 1.2, 2 seeds.
"""
import math
import random
from collections import Counter


def run(n, sigma, slack, seed, p):
    floor = n - sigma
    m = (n - 1) // 2
    kf = m + 1
    W = math.comb(n, kf)
    L = math.ceil(slack * W / n) * n
    t0 = 3 * L // 4
    last = {x: x for x in range(n)}
    w = list(range(n))
    rng = random.Random(seed)
    seen = set()
    app = Counter()
    crowd = 0
    serves = 0
    for pos in range(n - kf + 1):
        seen.add(frozenset(w[pos:pos + kf]))
    for t in range(n, L):
        elig = [x for x in range(n) if t - last[x] >= floor]
        if not elig:
            return None
        pref = w[t - kf + 1:t]
        fans = {x: s for x in elig
                for s in [frozenset(pref + [x])] if len(s) == kf}
        zf = [x for x, s in fans.items() if s not in seen]
        if t > t0:
            if len(zf) >= 2:
                crowd += len(zf) - 1
            for x in zf:
                app[fans[x]] += 1
        feedback = math.floor(t * p) > math.floor((t - 1) * p)
        if feedback and zf:
            pick = rng.choice(zf)
            serves += 1
        else:
            pick = rng.choice(elig)
        w.append(pick)
        last[pick] = t
        if pick in fans:
            seen.add(fans[pick])
    C = set()
    for pos in range(L):
        s = frozenset(w[(pos + q) % L] for q in range(kf))
        if len(s) == kf:
            C.add(s)
    import itertools
    allsets = {frozenset(c) for c in itertools.combinations(range(n), kf)}
    misses = allsets - C
    acounts = sorted(app[s] for s in misses) if misses else []
    meanapp = sum(acounts) / max(len(acounts), 1)
    return (L, W, len(misses), crowd, serves, meanapp)


def main():
    slack = 1.2
    for n in (17, 19):
        s_lo = round(0.7 * math.sqrt(n * math.log(n)))
        s_hi = round(1.1 * math.sqrt(n * math.log(n)))
        for sigma in sorted({s_lo, s_hi}):
            for p in (0.9, 1.0):
                for seed in range(2):
                    r = run(n, sigma, slack, seed, p)
                    if r is None:
                        print(f"n={n} sig={sigma} p={p} seed={seed}: "
                              f"infeasible", flush=True)
                        continue
                    L, W, miss, crowd, serves, meanapp = r
                    print(f"n={n} sig={sigma} p={p} seed={seed} "
                          f"L={L} W={W}: miss={miss} "
                          f"frac={miss/W:.4f} lateCrowd={crowd} "
                          f"serves={serves} "
                          f"missLateApp(mean={meanapp:.2f})",
                          flush=True)
    print("STATUS:C20DONE")


if __name__ == "__main__":
    main()
