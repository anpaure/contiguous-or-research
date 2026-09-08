#!/usr/bin/env python3
"""Computation C6 (block 49): age-priority word schedulers — does
Sturmian-perturbed FIFO inhabit the narrow band?

Build a cyclic-ish word letter by letter: at each time t choose one
letter among the ELIGIBLE (age >= GAP = n-1); rules:

  fifo    : always the oldest (control -- collapses to rigid
            rotation, coverage dies)
  sturm   : oldest, except when frac(t*phi) < q choose the
            2nd-oldest (Sturmian-perturbed FIFO, q = perturbation
            density; the 39.3/43.2 candidate species)
  sturm2  : two-level golden rule -- swap choice among top-2 by
            frac(t*phi), among top-3 by frac(t*phi^2) < q2
  randtie : uniform among the two oldest (random control)

Seed the word with one full round 0..n-1.  Ages measured from last
occurrence; if no letter is eligible the schedule FAILS at t
(reported).  Coverage measured on windows of lengths m..m+2 over
the final word (cyclic), matching the floored-LSGC spec.
"""
import math
import random
import sys
from collections import Counter

PHI = (5 ** 0.5 - 1) / 2
PHI2 = 2 ** 0.5 - 1


def build(n, L, rule, q=0.3, seed=1):
    GAP = n - 1
    last = {x: x - n for x in range(n)}  # seeded round at t=-n..-1
    w = list(range(n))
    rng = random.Random(seed)
    for t in range(n, L):
        elig = sorted((x for x in range(n) if t - last[x] >= GAP),
                      key=lambda x: last[x])
        if not elig:
            return None, t
        pick = elig[0]
        if rule == "sturm" and len(elig) >= 2:
            if (t * PHI) % 1.0 < q:
                pick = elig[1]
        elif rule == "sturm2" and len(elig) >= 2:
            if (t * PHI) % 1.0 < q:
                pick = elig[1]
            if len(elig) >= 3 and (t * PHI2) % 1.0 < q * q:
                pick = elig[2]
        elif rule == "randtie" and len(elig) >= 2:
            pick = elig[rng.randrange(2)]
        w.append(pick)
        last[pick] = t
    return w, None


def coverage(w, n):
    L = len(w)
    m = (n - 1) // 2
    out = []
    for k in (m, m + 1, m + 2):
        C = Counter()
        for p in range(L):
            s = frozenset(w[(p + t) % L] for t in range(k))
            if len(s) == k:
                C[s] += 1
        Wk = math.comb(n, k)
        miss = Wk - len(C)
        out.append((k, miss, Wk))
    return out


def main():
    for n in (7, 9, 11):
        m = (n - 1) // 2
        W = math.comb(n, m)
        L = math.ceil(1.6 * W / n) * n  # eps = 0.6, the n=7-proven slack
        for rule in ("fifo", "sturm", "sturm2", "randtie"):
            best = None
            for q in ((0.15, 0.3, 0.45) if rule.startswith("sturm")
                      else (0.0,)):
                w, fail = build(n, L, rule, q)
                if w is None:
                    print(f"n={n} {rule:7s} q={q:.2f}: FAILED at t={fail}",
                          flush=True)
                    continue
                cov = coverage(w, n)
                tot = sum(c[1] for c in cov)
                tag = " ".join(f"{k}:{miss}/{Wk}" for k, miss, Wk in cov)
                if best is None or tot < best[0]:
                    best = (tot, q, tag)
            if best:
                print(f"n={n} L={L} {rule:7s} q={best[1]:.2f}: "
                      f"missing {best[0]}  [{best[2]}]", flush=True)
    print("STATUS:C6DONE")


if __name__ == "__main__":
    main()
