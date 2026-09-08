#!/usr/bin/env python3
"""C14 (block 61): scaling of the potential-greedy balance rule with
the pool at its asymptotic shape.

Question (NEXT item ii, blocks 58/59): at FIXED slack, does the miss
fraction of the multi-rank potential-greedy walk fall as n grows,
when the pool is sigma+1 with sigma at the asymptotic shape
C*sqrt(n ln n), capped at m-1 so floor = n - sigma >= m+2 (the MTF
compilation validity boundary found in block 58 / C13b)?

Pool laws:
  A: sigma = min(round(0.7*sqrt(n ln n)), m-1)   asymptotic shape
  B: sigma = m-1                                 max valid pool
  C: sigma = 1                                   witness shape (contrast)
n = 11, 13, 15, 17, 19; slack 1.2; ranks m, m+1, m+2; 3 seeds.
Seeding is audit-consistent (block 59): word 0..n-1 placed at times
0..n-1, last[x] = x.  Reports per-rank miss fraction and var/mean.
"""
import math
import random
from collections import Counter


def build(n, L, sigma, seed):
    floor = n - sigma
    m = (n - 1) // 2
    ks = (m, m + 1, m + 2)
    last = {x: x for x in range(n)}
    w = list(range(n))
    rng = random.Random(seed)
    fib = {k: Counter() for k in ks}
    for k in ks:
        for p in range(n - k + 1):
            fib[k][frozenset(w[p:p + k])] += 1
    for t in range(n, L):
        elig = [x for x in range(n) if t - last[x] >= floor]
        if not elig:
            return None

        def score(x):
            s = 0
            for k in ks:
                st = frozenset(w[t - k + 1:t] + [x])
                if len(st) == k:
                    s += fib[k][st]
            return s

        sc = {x: score(x) for x in elig}
        mn = min(sc.values())
        pick = rng.choice([x for x in elig if sc[x] == mn])
        w.append(pick)
        last[pick] = t
        for k in ks:
            st = frozenset(w[t - k + 1:t + 1])
            if len(st) == k:
                fib[k][st] += 1
    return w


def stats(w, n):
    L = len(w)
    m = (n - 1) // 2
    out = []
    for k in (m, m + 1, m + 2):
        C = Counter()
        for p in range(L):
            s = frozenset(w[(p + q) % L] for q in range(k))
            if len(s) == k:
                C[s] += 1
        Wk = math.comb(n, k)
        miss = Wk - len(C)
        mult = list(C.values())
        mean = sum(mult) / len(mult)
        var = sum((x - mean) ** 2 for x in mult) / len(mult)
        out.append((k, miss, Wk, var / mean))
    return out


def main():
    slack = 1.2
    for n in (11, 13, 15, 17, 19):
        m = (n - 1) // 2
        W = math.comb(n, m + 1)
        L = math.ceil(slack * W / n) * n
        cap = m - 1
        laws = (
            ("A(0.7sqrt)", min(round(0.7 * math.sqrt(n * math.log(n))), cap)),
            ("B(max=m-1)", cap),
            ("C(sigma=1)", 1),
        )
        for tag, sigma in laws:
            accs = []
            for seed in range(3):
                w = build(n, L, sigma, seed)
                if w is None:
                    continue
                accs.append(stats(w, n))
            if not accs:
                print(f"n={n} {tag} sigma={sigma}: infeasible", flush=True)
                continue
            rows = []
            for i, k in enumerate((m, m + 1, m + 2)):
                mf = sum(a[i][1] / a[i][2] for a in accs) / len(accs)
                dd = sum(a[i][3] for a in accs) / len(accs)
                rows.append(f"k={k}: miss {mf:.4f} disp {dd:.2f}")
            print(f"n={n} L={L} {tag} sigma={sigma} | " + " | ".join(rows),
                  flush=True)
    print("STATUS:C14DONE")


if __name__ == "__main__":
    main()
