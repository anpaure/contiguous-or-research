#!/usr/bin/env python3
"""C17 (block 64): does the letter-matching coupling for the
back-(sigma+1)-to-top walk coalesce, and at what rate?

Coupling: maximal coupling of the two uniform pool choices —
with prob |O|/(sigma+1) serve the same letter a uniform in
O = pool_X cap pool_Y (as letter sets); else serve independent
uniforms from pool_X \\ O and pool_Y \\ O.  Measure coalescence
time vs n at sigma = ceil(0.7 sqrt(n ln n)) and sigma = 1
(Rudvalis sanity: expect ~n^3 scaling), starting from a uniform
random relative permutation.  Deck: list, index 0 = top.
"""
import math
import random
import sys


def couple(n, sigma, seed, tmax):
    rng = random.Random(seed)
    X = list(range(n))
    Y = list(range(n))
    rng.shuffle(Y)
    pool_lo = n - sigma - 1  # list index of first pool slot
    for t in range(1, tmax + 1):
        px = X[pool_lo:]
        py = Y[pool_lo:]
        O = set(px) & set(py)
        if rng.random() < len(O) / (sigma + 1):
            a = rng.choice(sorted(O))
            X.remove(a); X.insert(0, a)
            Y.remove(a); Y.insert(0, a)
        else:
            ax = [c for c in px if c not in O]
            ay = [c for c in py if c not in O]
            x = rng.choice(ax)
            y = rng.choice(ay)
            X.remove(x); X.insert(0, x)
            Y.remove(y); Y.insert(0, y)
        if X == Y:
            return t
    return None


def main():
    reps = 3
    print("law A: sigma = ceil(0.7 sqrt(n ln n))")
    for n in (30, 50, 80, 120):
        sigma = math.ceil(0.7 * math.sqrt(n * math.log(n)))
        tmax = 60 * n * n  # generous; expect ~ (n/sigma)^2 * n-ish
        ts = [couple(n, sigma, 1000 + r, tmax) for r in range(reps)]
        scale = (n ** 3 / sigma ** 2) * math.log(n)
        s = " ".join(str(t) for t in ts)
        ok = [t for t in ts if t]
        rat = (sum(ok) / len(ok)) / scale if ok else float("nan")
        print(f"n={n} sigma={sigma}: times [{s}] "
              f"mean/(n^3 log n/s^2)={rat:.3f}", flush=True)
    print("sigma = 1 (inverse-Rudvalis sanity)")
    for n in (20, 30, 40):
        tmax = 40 * n ** 3
        ts = [couple(n, 1, 2000 + r, tmax) for r in range(reps)]
        s = " ".join(str(t) for t in ts)
        ok = [t for t in ts if t]
        rat = (sum(ok) / len(ok)) / (n ** 3 * math.log(n)) if ok else float("nan")
        print(f"n={n} sigma=1: times [{s}] mean/(n^3 log n)={rat:.3f}",
              flush=True)
    print("STATUS:C17DONE")


if __name__ == "__main__":
    main()
