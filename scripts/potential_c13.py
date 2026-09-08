#!/usr/bin/env python3
"""C13 (block 58): multi-rank potential-greedy — the balance rule.

At each step, for each eligible letter x, the would-be window at
each shallow rank k is top-(k-1) union {x} = the last k-1 letters
plus x.  Score(x) = sum over ranks of the CURRENT fiber count of
that window's set.  Pick the eligible x with minimal score (ties
random).  This minimizes a global potential (sum of squared fiber
deviations grows slowest by picking low-count fibers) at every
rank simultaneously — dense gradient, unlike rare-event freshness.

Measure: per-rank missing and var/mean at slacks 1.2/1.4/1.6,
n = 9, 11, 13; 3 seeds.
"""
import math
import random
from collections import Counter


def build(n, L, seed):
    floor = n - 1
    m = (n - 1) // 2
    ks = (m, m + 1, m + 2)
    last = {x: x - n for x in range(n)}
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

        mn = min(score(x) for x in elig)
        pick = rng.choice([x for x in elig if score(x) == mn])
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
    for n in (9, 11, 13):
        m = (n - 1) // 2
        W = math.comb(n, m)
        for slack in (1.2, 1.4, 1.6):
            L = math.ceil(slack * W / n) * n
            best = None
            for seed in range(3):
                w = build(n, L, seed)
                if w is None:
                    continue
                st = stats(w, n)
                tot = sum(s[1] for s in st)
                if best is None or tot < best[0]:
                    best = (tot, st)
            if best is None:
                print(f"n={n} slack={slack}: infeasible", flush=True)
                continue
            tag = " ".join(f"{k}:{miss}/{Wk}(d={d:.2f})"
                           for k, miss, Wk, d in best[1])
            print(f"n={n} L={L} (slack {slack}) potential: "
                  f"missing {best[0]}  [{tag}]", flush=True)
    print("STATUS:C13DONE")


if __name__ == "__main__":
    main()
