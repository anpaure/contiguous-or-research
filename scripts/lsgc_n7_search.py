#!/usr/bin/env python3
"""LSGC finite test, n = 7, d = 2 (block 34 reduction).

By Lemma 34.1 (MATH_CANDIDATE_COHORT_CONSTRUCTION_20260820.md §5.16),
the n = 7, d = 2 floored LSGC exists iff there is a cyclic word over
Z_7 with all letter-gaps >= 6 whose 3-, 4-, and 5-windows (as sets)
cover all 35, 35, and 21 subsets respectively.  Zero-slack version
(L = 35, all windows distinct) is the doubly-exact (7,3) ucycle
(wreath-hard); the test probes whether ~20-40% length slack unlocks
coverage.

Run on a big box (this is CPU-only, embarrassingly parallel over
seeds):  python3 lsgc_n7_search.py [n_workers]
"""
import itertools
import random
import sys
import time
from collections import Counter
from multiprocessing import Pool

N = 7
LETTERS = list(range(N))
GAP = 6  # run floor: every 6 consecutive letters distinct
TARGETS = {k: {frozenset(c) for c in itertools.combinations(LETTERS, k)}
           for k in (3, 4, 5)}
FULL = sum(len(v) for v in TARGETS.values())  # 91


def win(word, L, p, k):
    s = {word[(p + t) % L] for t in range(k)}
    return frozenset(s) if len(s) == k else None


def build_counters(word, L):
    C = {k: Counter() for k in (3, 4, 5)}
    for k in (3, 4, 5):
        for p in range(L):
            w = win(word, L, p, k)
            if w:
                C[k][w] += 1
    return C


def miss_of(C):
    return sum(len(TARGETS[k]) - len(C[k]) for k in (3, 4, 5))


def letter_gap_ok(word, L, x):
    ps = [q for q, y in enumerate(word) if y == x]
    if len(ps) < 2:
        return True
    return all(b - a >= GAP for a, b in zip(ps, ps[1:] + [ps[0] + L]))


def affected(L, i):
    return {((i - s) % L, k) for k in (3, 4, 5) for s in range(k)}


def anneal(args):
    L, seed, budget = args
    rng = random.Random(seed)
    start = time.time()
    # Valid start: one random permutation repeated (L must be a
    # multiple of N) -- every letter-gap is exactly N >= GAP.  The
    # old rejection sampler had acceptance ~1e-12 and never returned.
    assert L % N == 0, "L must be a multiple of N for the rigid start"
    p = LETTERS[:]
    rng.shuffle(p)
    w = p * (L // N)
    C = build_counters(w, L)
    cur = miss_of(C)
    best = (cur, w[:])
    it = 0
    while time.time() - start < budget:
        it += 1
        T = max(0.03, 1.0 * (1 - (it % 400000) / 400000.0))
        # Near-adjacent proposals: from the rigid start the only
        # gap-legal moves are small local drifts (tau-local flow,
        # block 42.1), so distant swaps just burn rejections.
        i = rng.randrange(L)
        j = (i + rng.choice((1, 2, 3, -1, -2, -3))) % L
        a, b = w[i], w[j]
        if a == b:
            continue
        aff = affected(L, i) | affected(L, j)
        olds = [(p, k, win(w, L, p, k)) for (p, k) in aff]
        w[i], w[j] = b, a
        if not (letter_gap_ok(w, L, a) and letter_gap_ok(w, L, b)):
            w[i], w[j] = a, b
            continue
        for (p, k, ow) in olds:
            if ow:
                C[k][ow] -= 1
                if not C[k][ow]:
                    del C[k][ow]
        for (p, k, _) in olds:
            nw = win(w, L, p, k)
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
            for (p, k, _) in olds:
                nw = win(w, L, p, k)
                if nw:
                    C[k][nw] -= 1
                    if not C[k][nw]:
                        del C[k][nw]
            w[i], w[j] = a, b
            for (p, k, ow) in olds:
                if ow:
                    C[k][ow] += 1
    return best


def main():
    workers = int(sys.argv[1]) if len(sys.argv) > 1 else 16
    budget = 120  # seconds per task
    tasks = [(L, s * 104729 + L, budget)
             for L in (42, 49, 56, 63, 70)
             for s in range(workers)]
    overall = None
    with Pool(workers) as pool:
        for m, w in pool.imap_unordered(anneal, tasks):
            if overall is None or m < overall[0]:
                overall = (m, w)
                print(f"best so far: missing={m} L={len(w)}", flush=True)
            if m == 0:
                pool.terminate()
                break
    m, w = overall
    L = len(w)
    C = build_counters(w, L)
    print("missing =", m, "at L =", L,
          "cov:", len(C[3]), "/35,", len(C[4]), "/35,", len(C[5]), "/21")
    print("word:", w)
    if m == 0:
        print("PERFECT WITNESS; floor verified:",
              all(letter_gap_ok(w, L, x) for x in LETTERS))
    else:
        for k in (3, 4, 5):
            print(f"missing {k}-sets:",
                  [sorted(s) for s in TARGETS[k] - set(C[k])])


if __name__ == "__main__":
    main()
