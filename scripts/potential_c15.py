#!/usr/bin/env python3
"""C15 (block 65): cover-first multi-rank rule + snub-inequality
accounting.

Rule: among the sigma+1 eligible letters, prefer those whose
placement creates at least one NEW window at SOME shallow rank
(cover-first); tie-break by potential-greedy (min summed fiber
counts); if none creates new, potential-greedy among all
eligible.  This is the C15 rule proposed in block 60.4.

Per rank k we track the three snub-inequality terms (60.1 with
the cross-rank extension):
  miss^k <= N0^k + crowd^k + cross^k
  N0^k    = #k-sets never appearing in the rank-k fan while
            uncovered;
  crowd^k = sum_t (c_t^k - 1)^+ counted ONLY at steps where the
            step covers at rank k (snubs);
  cross^k = #steps where the rank-k fan contained a zero but the
            step did NOT cover at rank k.
(The inequality proof maps each surviving zero either to N0 or
to its last snub/cross event, so miss <= N0 + crowd + cross;
we report all terms and the actual misses.)

n = 13, 15; sigma in {round(0.7 sqrt(n ln n)), m-1}; slack 1.2;
2 seeds.  Reports which failure channel dominates.
"""
import math
import random
from collections import Counter


def run(n, sigma, slack, seed):
    floor = n - sigma
    m = (n - 1) // 2
    ks = (m, m + 1, m + 2)
    W = math.comb(n, m + 1)
    L = math.ceil(slack * W / n) * n
    last = {x: x for x in range(n)}
    w = list(range(n))
    rng = random.Random(seed)
    fib = {k: Counter() for k in ks}
    seen = {k: set() for k in ks}
    appeared = {k: set() for k in ks}
    crowd = {k: 0 for k in ks}
    cross = {k: 0 for k in ks}
    for k in ks:
        for p in range(n - k + 1):
            s = frozenset(w[p:p + k])
            fib[k][s] += 1
            seen[k].add(s)
    for t in range(n, L):
        elig = [x for x in range(n) if t - last[x] >= floor]
        if not elig:
            return None
        # fan structure and zero counts per rank
        fans = {}
        czero = {}
        for k in ks:
            pref = w[t - k + 1:t]
            fan = {}
            for x in elig:
                s = frozenset(pref + [x])
                if len(s) == k:
                    fan[x] = s
            fans[k] = fan
            zn = 0
            for x, s in fan.items():
                if s not in seen[k]:
                    zn += 1
                    appeared[k].add(s)
            czero[k] = zn

        def newcount(x):
            return sum(1 for k in ks
                       if x in fans[k] and fans[k][x] not in seen[k])

        def pot(x):
            return sum(fib[k][fans[k][x]] for k in ks if x in fans[k])

        cands = [x for x in elig if newcount(x) > 0]
        if cands:
            mn = min(pot(x) for x in cands)
            pick = rng.choice([x for x in cands if pot(x) == mn])
        else:
            mn = min(pot(x) for x in elig)
            pick = rng.choice([x for x in elig if pot(x) == mn])
        for k in ks:
            covered_here = (pick in fans[k]
                            and fans[k][pick] not in seen[k])
            if czero[k] >= 1:
                if covered_here:
                    crowd[k] += czero[k] - 1
                else:
                    cross[k] += 1
        w.append(pick)
        last[pick] = t
        for k in ks:
            if pick in fans[k]:
                s = fans[k][pick]
                fib[k][s] += 1
                seen[k].add(s)
    out = {}
    for k in ks:
        Wk = math.comb(n, k)
        # cyclic closure coverage for honest miss counts
        C = set()
        for p in range(L):
            s = frozenset(w[(p + q) % L] for q in range(k))
            if len(s) == k:
                C.add(s)
        miss = Wk - len(C)
        n0 = sum(1 for _ in range(1))  # placeholder replaced below
        never = Wk - len(appeared[k] | set(seen[k]))
        # N0 = sets never covered and never appeared in a fan
        allsets = None  # avoid enumerating for n=15 rank 7 (6435) fine
        n0 = 0
        # enumerate misses only (small) and check appearance
        # (appeared contains only sets seen as zeros in fans)
        # a set never appeared and never covered <-> not in seen
        # and not in appeared
        n0 = Wk - len(set(seen[k]) | appeared[k])
        out[k] = (miss, Wk, n0, crowd[k], cross[k])
    return out


def main():
    slack = 1.2
    for n in (13, 15):
        m = (n - 1) // 2
        for sigma in sorted({round(0.7 * math.sqrt(n * math.log(n))),
                             m - 1}):
            agg = None
            for seed in range(2):
                r = run(n, sigma, slack, seed)
                if r is None:
                    continue
                if agg is None:
                    agg = {k: [0] * 5 for k in r}
                for k, v in r.items():
                    for i in range(5):
                        agg[k][i] += v[i] / 2
            if agg is None:
                print(f"n={n} sigma={sigma}: infeasible", flush=True)
                continue
            for k, (miss, Wk, n0, crowd, cross) in sorted(agg.items()):
                print(f"n={n} sigma={sigma} k={k}: miss {miss:.0f}/{Wk:.0f} "
                      f"({miss / Wk:.4f}) | N0={n0:.0f} crowd={crowd:.0f} "
                      f"cross={cross:.0f} | bound {(n0 + crowd + cross):.0f}",
                      flush=True)
    print("STATUS:C15DONE")


if __name__ == "__main__":
    main()
