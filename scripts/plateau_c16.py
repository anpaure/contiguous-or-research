#!/usr/bin/env python3
"""C16 (block 62): sanity check for the random tail-MTF plateau.

Pure random (sigma+1)-tail MTF walk (uniform pick among the
sigma+1 oldest).  Checks, at n=13/15, sigma=3, slack 1.2:
  (a) coverage at ranks m..m+2 vs the Poisson plateau
      1 - exp(-L/C(n,k));
  (b) the aggregate repeat probability r_d = P(window at lag d
      equals window at t), vs the run bound
      beta = (sigma+1)!/(sigma+1)^(sigma+1) and vs 1/M;
  (c) empirical max window multiplicity.
Tiny run (seconds), 3 seeds.
"""
import math
import random
from collections import Counter


def run(n, sigma, slack, seed):
    m = (n - 1) // 2
    floor = n - sigma
    W = math.comb(n, m + 1)
    L = math.ceil(slack * W / n) * n
    last = {x: x for x in range(n)}
    w = list(range(n))
    rng = random.Random(seed)
    for t in range(n, L):
        elig = [x for x in range(n) if t - last[x] >= floor]
        pick = rng.choice(elig)
        w.append(pick)
        last[pick] = t
    return w, L


def main():
    slack = 1.2
    for n in (13, 15):
        m = (n - 1) // 2
        sigma = 3
        covs = {k: [] for k in (m, m + 1, m + 2)}
        rd_acc = Counter()
        rd_n = Counter()
        maxmult = 0
        for seed in range(3):
            w, L = run(n, sigma, slack, seed)
            k = m + 1
            wins = [frozenset(w[p:p + k]) for p in range(L - k + 1)]
            for kk in (m, m + 1, m + 2):
                C = set()
                for p in range(L):
                    s = frozenset(w[(p + q) % L] for q in range(kk))
                    if len(s) == kk:
                        C.add(s)
                covs[kk].append(len(C) / math.comb(n, kk))
            mult = Counter(wins)
            maxmult = max(maxmult, max(mult.values()))
            # r_d estimate on the focus rank, lag buckets
            for d in list(range(1, 3 * n)) + [50, 100, 200, 500, 1000]:
                if d >= len(wins):
                    continue
                hits = sum(1 for i in range(0, len(wins) - d, 7)
                           if wins[i] == wins[i + d])
                tot = len(range(0, len(wins) - d, 7))
                rd_acc[d] += hits
                rd_n[d] += tot
        M = math.comb(n, m + 1)
        beta = math.factorial(sigma + 1) / (sigma + 1) ** (sigma + 1)
        Lval = math.ceil(slack * math.comb(n, m + 1) / n) * n
        print(f"n={n} sigma={sigma} L={Lval} M={M} beta={beta:.4f} 1/M={1/M:.6f}")
        for kk in (m, m + 1, m + 2):
            tau = Lval / math.comb(n, kk)
            plat = 1 - math.exp(-tau)
            cv = sum(covs[kk]) / len(covs[kk])
            print(f"  k={kk}: coverage {cv:.4f}  Poisson plateau {plat:.4f}")
        nz = [(d, rd_acc[d] / rd_n[d]) for d in sorted(rd_n)
              if rd_acc[d] > 0]
        zero_thru = max([d for d in sorted(rd_n)
                         if all(rd_acc[e] == 0 for e in rd_n if e <= d)],
                        default=0)
        print(f"  r_d: zero for all sampled d <= {zero_thru}; nonzero:",
              " ".join(f"d={d}:{v:.5f}" for d, v in nz[:12]))
        print(f"  max window multiplicity: {maxmult}")
    print("STATUS:C16DONE")


if __name__ == "__main__":
    main()
