#!/usr/bin/env python3
"""C8: freshness-greedy (self-avoiding) scheduler.

At each t, among eligible letters (age >= n-1) pick the one whose
placement completes the FEWEST already-seen window contents (ranks
m..m+2), tie-break by oldest.  Zero design bits: deterministic
given history — the entropy-ledger-compatible feedback species.
"""
import math
from collections import Counter


def build(n, L):
    GAP = n - 1
    m = (n - 1) // 2
    ks = (m, m + 1, m + 2)
    last = {x: x - n for x in range(n)}
    w = list(range(n))
    seen = {k: set() for k in ks}
    for k in ks:
        for p in range(n - k + 1):
            seen[k].add(frozenset(w[p:p + k]))
    for t in range(n, L):
        elig = [x for x in range(n) if t - last[x] >= GAP]
        if not elig:
            return None, t

        def stale(x):
            c = 0
            for k in ks:
                s = frozenset(w[t - k + 1:t] + [x])
                if len(s) == k and s in seen[k]:
                    c += 1
            return c

        pick = min(elig, key=lambda x: (stale(x), last[x]))
        w.append(pick)
        last[pick] = t
        for k in ks:
            s = frozenset(w[t - k + 1:t + 1])
            if len(s) == k:
                seen[k].add(s)
    return w, None


def coverage(w, n):
    L = len(w)
    m = (n - 1) // 2
    out = []
    for k in (m, m + 1, m + 2):
        C = set()
        for p in range(L):
            s = frozenset(w[(p + t) % L] for t in range(k))
            if len(s) == k:
                C.add(s)
        out.append((k, math.comb(n, k) - len(C), math.comb(n, k)))
    return out


def main():
    for n in (7, 9, 11, 13):
        m = (n - 1) // 2
        W = math.comb(n, m)
        for slack in (1.2, 1.4, 1.6):
            L = math.ceil(slack * W / n) * n
            w, fail = build(n, L)
            if w is None:
                print(f"n={n} L={L}: FAILED at t={fail}", flush=True)
                continue
            cov = coverage(w, n)
            tot = sum(c[1] for c in cov)
            tag = " ".join(f"{k}:{ms}/{Wk}" for k, ms, Wk in cov)
            print(f"n={n} L={L} (slack {slack}): missing {tot}  [{tag}]",
                  flush=True)
    print("STATUS:C8DONE")


if __name__ == "__main__":
    main()
