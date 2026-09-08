#!/usr/bin/env python3
"""General floored-LSGC annealing search (blocks 34/44/45).

Cyclic word over Z_N, all cyclic letter-gaps >= GAP, windows of
each length in KS must cover all C(N,k) k-subsets.  Start from the
rigid p-repeat word (gaps exactly N), drift with near-adjacent
swaps (tau-local flow, block 42.1).  Usage:

  python3 lsgc_general.py <n> [workers]

Configs: n=7 (GAP 6, KS 3-5), n=9 (GAP 8, KS 4-6), n=11
(GAP 10, KS 5-7).  L values are multiples of n from just above
the coverage lower bound max_k C(N,k) upward.
"""
import itertools
import random
import sys
import time
from collections import Counter
from multiprocessing import Pool

CFG = {
    7: dict(GAP=6, KS=(3, 4, 5), LS=(42, 49, 56, 63, 70), budget=120),
    9: dict(GAP=8, KS=(4, 5, 6), LS=(126, 135, 144, 153, 162, 180),
            budget=300),
    # n=11 retuned 2026-08-21: witnesses sit at slack ~1.57-1.60
    # (n=7: 56/35=1.60, n=9: 198/126=1.571); scan 1.50-1.62.
    11: dict(GAP=10, KS=(5, 6, 7), LS=(693, 704, 715, 726, 737, 748),
             budget=3600),
}

N = GAP = None
KS = ()
TARGETS = {}


def init_globals(n):
    global N, GAP, KS, TARGETS
    N = n
    GAP = CFG[n]["GAP"]
    KS = CFG[n]["KS"]
    TARGETS = {k: {frozenset(c)
                   for c in itertools.combinations(range(N), k)}
               for k in KS}


def win(word, L, p, k):
    s = {word[(p + t) % L] for t in range(k)}
    return frozenset(s) if len(s) == k else None


def build_counters(word, L):
    C = {k: Counter() for k in KS}
    for k in KS:
        for p in range(L):
            w = win(word, L, p, k)
            if w:
                C[k][w] += 1
    return C


def miss_of(C):
    return sum(len(TARGETS[k]) - len(C[k]) for k in KS)


def letter_gap_ok(word, L, x):
    ps = [q for q, y in enumerate(word) if y == x]
    if len(ps) < 2:
        return True
    return all(b - a >= GAP for a, b in zip(ps, ps[1:] + [ps[0] + L]))


def affected(L, i):
    return {((i - s) % L, k) for k in KS for s in range(k)}


def anneal(args):
    n, L, seed, budget = args
    init_globals(n)
    rng = random.Random(seed)
    start = time.time()
    assert L % N == 0
    p = list(range(N))
    rng.shuffle(p)
    w = p * (L // N)
    C = build_counters(w, L)
    cur = miss_of(C)
    best = (cur, w[:])
    it = 0
    while time.time() - start < budget:
        it += 1
        T = max(0.03, 1.0 * (1 - (it % 400000) / 400000.0))
        i = rng.randrange(L)
        j = (i + rng.choice((1, 2, 3, -1, -2, -3))) % L
        a, b = w[i], w[j]
        if a == b:
            continue
        aff = affected(L, i) | affected(L, j)
        olds = [(q, k, win(w, L, q, k)) for (q, k) in aff]
        w[i], w[j] = b, a
        if not (letter_gap_ok(w, L, a) and letter_gap_ok(w, L, b)):
            w[i], w[j] = a, b
            continue
        for (q, k, ow) in olds:
            if ow:
                C[k][ow] -= 1
                if not C[k][ow]:
                    del C[k][ow]
        for (q, k, _) in olds:
            nw = win(w, L, q, k)
            if nw:
                C[k][nw] += 1
        m = miss_of(C)
        if m <= cur or rng.random() < 2.71828 ** (-(m - cur) / T):
            cur = m
            if m < best[0]:
                best = (m, w[:])
                if m == 0:
                    return best
        else:
            for (q, k, _) in olds:
                nw = win(w, L, q, k)
                if nw:
                    C[k][nw] -= 1
                    if not C[k][nw]:
                        del C[k][nw]
            w[i], w[j] = a, b
            for (q, k, ow) in olds:
                if ow:
                    C[k][ow] += 1
    return best


def main():
    n = int(sys.argv[1])
    workers = int(sys.argv[2]) if len(sys.argv) > 2 else 16
    init_globals(n)
    budget = CFG[n]["budget"]
    # round-robin L values so early rounds sample every L
    tasks = [(n, L, s * 104729 + L, budget)
             for s in range(workers)
             for L in CFG[n]["LS"]]
    per_L = {}
    with Pool(workers) as pool:
        for m, w in pool.imap_unordered(anneal, tasks):
            L = len(w)
            if L not in per_L or m < per_L[L][0]:
                per_L[L] = (m, w)
                print(f"best so far: n={n} L={L} missing={m}",
                      flush=True)
                if m == 0:
                    print(f"PERFECT WITNESS n={n} L={L}")
                    print("word:", w, flush=True)
    print("summary per L:",
          {L: v[0] for L, v in sorted(per_L.items())}, flush=True)
    print("STATUS:DONE")


if __name__ == "__main__":
    main()
