#!/usr/bin/env python3
"""C12 (block 56): the beta-LIFO tail law vs the Sub-Poisson Walk
Question.

sigma-tail MTF word builder: at each step, eligible = age >= n-1
(the witness-spec floor).  Pull the j-th YOUNGEST eligible with
probability ~ beta^j (j = 0 youngest).  beta = 1.0 is uniform;
beta -> 0 is pure LIFO (starves); the n=9 witness's empirical law
decays like ~0.4^j.  Measure per-rank coverage and multiplicity
var/mean (sub-Poisson < 1) at ranks m..m+2.
"""
import math
import random
from collections import Counter


def build(n, L, beta, seed):
    floor = n - 1
    last = {x: x - n for x in range(n)}
    w = list(range(n))
    rng = random.Random(seed)
    for t in range(n, L):
        elig = sorted((x for x in range(n) if t - last[x] >= floor),
                      key=lambda x: -last[x])  # youngest eligible first
        if not elig:
            return None
        ws = [beta ** j for j in range(len(elig))]
        r = rng.random() * sum(ws)
        acc = 0.0
        pick = elig[-1]
        for x, wt in zip(elig, ws):
            acc += wt
            if r <= acc:
                pick = x
                break
        w.append(pick)
        last[pick] = t
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
        L = math.ceil(1.6 * W / n) * n
        for beta in (0.2, 0.35, 0.5, 0.7, 1.0):
            best = None
            for seed in range(5):
                w = build(n, L, beta, seed)
                if w is None:
                    continue
                st = stats(w, n)
                tot = sum(s[1] for s in st)
                if best is None or tot < best[0]:
                    best = (tot, st)
            if best is None:
                print(f"n={n} beta={beta}: infeasible", flush=True)
                continue
            tag = " ".join(f"{k}:{miss}/{Wk}(d={d:.2f})"
                           for k, miss, Wk, d in best[1])
            print(f"n={n} L={L} beta={beta}: missing {best[0]}  [{tag}]",
                  flush=True)
    print("STATUS:C12DONE")


if __name__ == "__main__":
    main()
