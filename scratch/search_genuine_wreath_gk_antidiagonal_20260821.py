#!/usr/bin/env python3
"""Heuristic search for genuine wreath pairs with many correct GK antidiagonals."""

from __future__ import annotations

import argparse
import math
import random


def windows(order, size):
    b = len(order)
    out = []
    for end in range(b):
        mask = 0
        for q in range(size):
            mask |= 1 << order[(end - q) % b]
        out.append(mask)
    return out


def top_parity(x, y, b):
    h = 0
    mn = 0
    for i in range(b):
        h += 1 if x >> i & 1 else -1
        mn = min(mn, h)
        h += 1 if y >> i & 1 else -1
        mn = min(mn, h)
    return (-mn) & 1


def score(alpha, beta):
    b = len(alpha)
    r = (b - 1) // 2
    aa = windows(alpha, r)
    bb = windows(beta, r + 1)
    phase = []
    for p in range(b):
        vals = [top_parity(aa[i], bb[(p - i) % b], b) for i in range(b)]
        phase.append(vals[0] if len(set(vals)) == 1 else None)
    rank = lambda x: (r * x) % b
    tau = [1 if rank(x) < r else 0 for x in range(b)]
    correct = max(
        sum(phase[p] == (tau[(p + sh) % b] ^ flip) for p in range(b))
        for sh in range(b) for flip in (0, 1)
    )
    mono = sum(v is not None for v in phase)
    # Lexicographic: correct phases first, then all monochromatic phases.
    return correct * (b + 1) + mono, correct, mono, phase


def mutate(order, rng):
    z = list(order)
    i, j = rng.sample(range(len(z)), 2)
    z[i], z[j] = z[j], z[i]
    # Cyclically normalize label 0 into position zero.
    q = z.index(0)
    return tuple(z[q:] + z[:q])


def run(b, restarts, steps, seed):
    rng = random.Random(seed)
    best = None
    standard = tuple(range(b))
    reverse = (0,) + tuple(range(b - 1, 0, -1))
    starts = [(standard, reverse)]
    for _ in range(restarts - 1):
        a = list(range(b)); c = list(range(b))
        rng.shuffle(a); rng.shuffle(c)
        qa = a.index(0); qc = c.index(0)
        starts.append((tuple(a[qa:] + a[:qa]), tuple(c[qc:] + c[:qc])))
    for restart, (a, c) in enumerate(starts):
        cur = score(a, c)
        if best is None or cur[0] > best[0]:
            best = (*cur, a, c)
            print("best", b, restart, 0, best, flush=True)
        for it in range(1, steps + 1):
            na, nc = (mutate(a, rng), c) if rng.randrange(2) else (a, mutate(c, rng))
            nxt = score(na, nc)
            temp = max(0.05, 2.0 * (1 - it / steps))
            if nxt[0] >= cur[0] or rng.random() < math.exp((nxt[0] - cur[0]) / temp):
                a, c, cur = na, nc, nxt
            if cur[0] > best[0]:
                best = (*cur, a, c)
                print("best", b, restart, it, best, flush=True)
    print("FINAL", b, best, flush=True)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--b", type=int, nargs="+", required=True)
    p.add_argument("--restarts", type=int, default=20)
    p.add_argument("--steps", type=int, default=20000)
    p.add_argument("--seed", type=int, default=1)
    a = p.parse_args()
    for b in a.b:
        run(b, a.restarts, a.steps, a.seed + b)


if __name__ == "__main__":
    main()
