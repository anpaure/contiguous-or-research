#!/usr/bin/env python3
"""C10 (block 52): quantitative test of the depth-one staleness DE
(block 50.2).

Scheduler = the DE's model exactly: at each step, eligible =
letters with age >= floor = n - sigma_nom; among eligible, the
FRESH subset = those whose placement completes an unseen k-window
for the FOCUS rank k = m+1; pick uniformly from fresh if nonempty,
else uniformly from eligible.  (Depth one: freshness is judged at
the focus rank only; other ranks ride along and are reported.)

DE prediction per rank j: d rho_j / d tau = 1 - rho_j^sigma with
tau = t/W_j, integrated to tau_final = L/W_j; sigma = measured
mean eligible-pool size.  Report simulated vs DE-predicted final
coverage.  Averages over 5 seeds.
"""
import math
import random
from collections import Counter


def simulate(n, sigma_nom, slack, seed):
    m = (n - 1) // 2
    kf = m + 1
    W = math.comb(n, kf)
    L = math.ceil(slack * W / n) * n
    floor = n - sigma_nom
    # seeded word w = [0..n-1] placed at times 0..n-1, so
    # last[x] = x (audit fix 2026-08-21: was x - n, inconsistent
    # with the seed and inflating early eligibility)
    last = {x: x for x in range(n)}
    w = list(range(n))
    rng = random.Random(seed)
    seen = set()
    for p in range(n - kf + 1):
        seen.add(frozenset(w[p:p + kf]))
    pool_sum = 0
    for t in range(n, L):
        elig = [x for x in range(n) if t - last[x] >= floor]
        pool_sum += len(elig)
        if not elig:
            return None
        fresh = []
        for x in elig:
            s = frozenset(w[t - kf + 1:t] + [x])
            if len(s) == kf and s not in seen:
                fresh.append(x)
        pick = rng.choice(fresh) if fresh else rng.choice(elig)
        w.append(pick)
        last[pick] = t
        s = frozenset(w[t - kf + 1:t + 1])
        if len(s) == kf:
            seen.add(s)
    covs = {}
    for k in (m, m + 1, m + 2):
        C = set()
        for p in range(L):
            s = frozenset(w[(p + q) % L] for q in range(k))
            if len(s) == k:
                C.add(s)
        covs[k] = len(C) / math.comb(n, k)
    return covs, pool_sum / (L - n), L


def de_predict(sigma, tau_final, steps=20000):
    rho = 0.0
    dt = tau_final / steps
    for _ in range(steps):
        rho += dt * (1 - rho ** sigma)
    return rho


def main():
    slack = 1.2
    for n in (11, 13):
        m = (n - 1) // 2
        for sig in (1, 2, 3, 4):
            acc, pools, Lv = None, [], None
            runs = []
            for seed in range(5):
                r = simulate(n, sig, slack, seed)
                if r is None:
                    continue
                covs, pool, Lv = r
                runs.append(covs)
                pools.append(pool)
            if not runs:
                print(f"n={n} sigma_nom={sig}: infeasible (pool empty)")
                continue
            pool = sum(pools) / len(pools)
            k = m + 1
            sim = sum(r[k] for r in runs) / len(runs)
            tau = Lv / math.comb(n, k)
            pred = de_predict(max(pool, 1.0), tau)
            others = {kk: round(sum(r[kk] for r in runs) / len(runs), 3)
                      for kk in (m, m + 2)}
            print(f"n={n} sigma_nom={sig} (measured pool {pool:.2f}): "
                  f"focus-rank cov sim={sim:.3f} DE={pred:.3f} "
                  f"| side ranks {others}", flush=True)
    print("STATUS:C10DONE")


if __name__ == "__main__":
    main()
