#!/usr/bin/env python3
"""Anneal total cell agreement with an almost-alternating phase word."""

from __future__ import annotations

import argparse
import math
import random

from search_genuine_wreath_gk_antidiagonal_20260821 import windows, top_parity, mutate


def evaluate(alpha, beta):
    b = len(alpha); r = (b - 1) // 2
    aa = windows(alpha, r); bb = windows(beta, r + 1)
    matrix = [[top_parity(aa[i], bb[j], b) for j in range(b)] for i in range(b)]
    rank = lambda x: (r * x) % b
    tau = [1 if rank(x) < r else 0 for x in range(b)]
    vals = []
    for sh in range(b):
        agree = sum(matrix[i][j] == tau[(i + j + sh) % b] for i in range(b) for j in range(b))
        vals.extend((agree, b * b - agree))
    return max(vals), vals.index(max(vals)), matrix


def run(b, restarts, steps, seed):
    rng = random.Random(seed); best = None
    for restart in range(restarts):
        a = list(range(b)); c = list(range(b)); rng.shuffle(a); rng.shuffle(c)
        qa = a.index(0); qc = c.index(0)
        a = tuple(a[qa:] + a[:qa]); c = tuple(c[qc:] + c[:qc])
        cur = evaluate(a, c)
        if best is None or cur[0] > best[0]:
            best = (*cur, a, c); print("best", b, restart, 0, best[0], best[1], a, c, flush=True)
        for it in range(1, steps + 1):
            na, nc = (mutate(a, rng), c) if rng.randrange(2) else (a, mutate(c, rng))
            nxt = evaluate(na, nc)
            temp = max(.05, 3 * (1 - it / steps))
            if nxt[0] >= cur[0] or rng.random() < math.exp((nxt[0] - cur[0]) / temp):
                a, c, cur = na, nc, nxt
            if cur[0] > best[0]:
                best = (*cur, a, c); print("best", b, restart, it, best[0], best[1], a, c, flush=True)
    print("FINAL", b, "agreement", best[0], "ratio", best[0] / b**2,
          "shift", best[1], "alpha", best[-2], "beta", best[-1], flush=True)


def main():
    p = argparse.ArgumentParser(); p.add_argument("--b", nargs="+", type=int, required=True)
    p.add_argument("--restarts", type=int, default=20); p.add_argument("--steps", type=int, default=10000)
    p.add_argument("--seed", type=int, default=1); a = p.parse_args()
    for b in a.b: run(b, a.restarts, a.steps, a.seed + b)


if __name__ == "__main__": main()
