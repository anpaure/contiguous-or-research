#!/usr/bin/env python3
"""C15b (block 73): measure the 65.5 time-split snub quantities.

For the cover-first rule (C15) AND single-rank freshness-greedy
(zero-preferring at focus rank), at the focus rank k = m+1:
for t0 in {0.5 L, 0.75 L} report
  late crowd  = sum_{t > t0} (c_t - 1)^+,
  late appearance counts a_{>t0}(S) for the FINAL misses,
  the 65.5 bound min_J [ #{S miss: a_{>t0}(S) < J} + crowd/J ],
  and the actual miss count.
n = 15, sigma in {4, 6}, 2 seeds, slack 1.2.
"""
import math
import random
from collections import Counter


def run(n, sigma, slack, seed, rule):
    floor = n - sigma
    m = (n - 1) // 2
    ks = (m, m + 1, m + 2)
    kf = m + 1
    W = math.comb(n, kf)
    L = math.ceil(slack * W / n) * n
    t0s = (L // 2, 3 * L // 4)
    last = {x: x for x in range(n)}
    w = list(range(n))
    rng = random.Random(seed)
    fib = {k: Counter() for k in ks}
    seen = {k: set() for k in ks}
    app = {t0: Counter() for t0 in t0s}   # focus-rank appearances > t0
    crowd = {t0: 0 for t0 in t0s}
    for k in ks:
        for p in range(n - k + 1):
            s = frozenset(w[p:p + k])
            fib[k][s] += 1
            seen[k].add(s)
    for t in range(n, L):
        elig = [x for x in range(n) if t - last[x] >= floor]
        if not elig:
            return None
        fans = {}
        for k in ks:
            pref = w[t - k + 1:t]
            fans[k] = {x: s for x in elig
                       for s in [frozenset(pref + [x])] if len(s) == k}
        zf = [x for x, s in fans[kf].items() if s not in seen[kf]]
        cz = len(zf)
        for t0 in t0s:
            if t > t0:
                if cz >= 2:
                    crowd[t0] += cz - 1
                for x in zf:
                    app[t0][fans[kf][x]] += 1

        def pot(x):
            return sum(fib[k][fans[k][x]] for k in ks if x in fans[k])

        if rule == "fresh":
            pick = rng.choice(zf) if zf else rng.choice(elig)
        else:  # cover-first
            def newcount(x):
                return sum(1 for k in ks
                           if x in fans[k] and fans[k][x] not in seen[k])
            cands = [x for x in elig if newcount(x) > 0]
            pool2 = cands if cands else elig
            mn = min(pot(x) for x in pool2)
            pick = rng.choice([x for x in pool2 if pot(x) == mn])
        w.append(pick)
        last[pick] = t
        for k in ks:
            if pick in fans[k]:
                s = fans[k][pick]
                fib[k][s] += 1
                seen[k].add(s)
    # final misses at focus rank (cyclic closure)
    C = set()
    for p in range(L):
        s = frozenset(w[(p + q) % L] for q in range(kf))
        if len(s) == kf:
            C.add(s)
    import itertools
    allsets = {frozenset(c) for c in itertools.combinations(range(n), kf)}
    misses = allsets - C
    out = []
    for t0 in t0s:
        acounts = sorted(app[t0][s] for s in misses)
        best = None
        for J in (1, 2, 3, 4, 6, 8, 12, 16, 24, 32):
            few = sum(1 for a in acounts if a < J)
            b = few + crowd[t0] / J
            if best is None or b < best[0]:
                best = (b, J, few)
        out.append((t0, len(misses), crowd[t0], acounts[:5],
                    sum(acounts) / max(len(acounts), 1), best))
    return L, out


def main():
    slack = 1.2
    n = 15
    for sigma in (4, 6):
        for rule in ("fresh", "cover"):
            for seed in range(2):
                r = run(n, sigma, slack, seed, rule)
                if r is None:
                    print(f"sigma={sigma} {rule} seed={seed}: infeasible",
                          flush=True)
                    continue
                L, rows = r
                for t0, miss, crowd, lowapp, meanapp, best in rows:
                    b, J, few = best
                    print(f"n={n} sig={sigma} {rule} seed={seed} "
                          f"t0={t0}/{L}: miss={miss} lateCrowd={crowd} "
                          f"missLateApp(mean={meanapp:.1f} "
                          f"low5={lowapp}) bound65.5={b:.0f} "
                          f"(J={J}, few={few})", flush=True)
    print("STATUS:C15BDONE")


if __name__ == "__main__":
    main()
