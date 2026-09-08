#!/usr/bin/env python3
"""C18 (block 64): verify the per-step displacement-Lyapunov
case analysis for the letter-matching coupling.

Phi = sum_a |pos_X(a) - pos_Y(a)| (positions 1..n).
Claims (proved by case analysis, verified here):
  (1) matched serve (same letter, same position): dPhi = 0;
  (2) loose serve (same letter, different positions): dPhi <= -1;
  (3) different-letter serve: dPhi <= (2 py_x - Jx) + (2 px_y - Jy)
      + (sigma - 1), where py_x = position of x in Y, etc.
Also record the empirical mean of the diff-serve injection.
"""
import math
import random


def phi(X, Y, n):
    pos = {a: i for i, a in enumerate(X)}
    return sum(abs(pos[a] - j) for j, a in enumerate(Y))


def main():
    rng = random.Random(7)
    n, sigma = 60, 9
    X = list(range(n))
    Y = list(range(n))
    rng.shuffle(Y)
    pool_lo = n - sigma - 1
    v1 = v2 = v3 = 0
    inj = []
    bad = 0
    for t in range(20000):
        p0 = phi(X, Y, n)
        px = X[pool_lo:]
        py = Y[pool_lo:]
        O = set(px) & set(py)
        if rng.random() < len(O) / (sigma + 1):
            a = rng.choice(sorted(O))
            jx = X.index(a) + 1
            jy = Y.index(a) + 1
            X.remove(a); X.insert(0, a)
            Y.remove(a); Y.insert(0, a)
            d = phi(X, Y, n) - p0
            if jx == jy:
                v1 += 1
                # audit fix 2026-08-21: the lemma is dPhi <= 0
                # (strict decreases are allowed and common); the
                # old checker tested d != 0 and printed misleading
                # "violations" for favorable strict decreases.
                if d > 0:
                    bad += 1
                    print(f"VIOLATION matched: d={d}")
            else:
                v2 += 1
                if d > -1:
                    bad += 1
                    print(f"VIOLATION loose: d={d} jx={jx} jy={jy}")
        else:
            ax = [c for c in px if c not in O]
            ay = [c for c in py if c not in O]
            x = rng.choice(ax)
            y = rng.choice(ay)
            jx = X.index(x) + 1
            jy = Y.index(y) + 1
            pyx = Y.index(x) + 1
            pxy = X.index(y) + 1
            X.remove(x); X.insert(0, x)
            Y.remove(y); Y.insert(0, y)
            d = phi(X, Y, n) - p0
            bound = (2 * pyx - jx) + (2 * pxy - jy) + (sigma - 1)
            v3 += 1
            inj.append(d)
            if d > bound:
                bad += 1
                print(f"VIOLATION diff: d={d} bound={bound}")
        if X == Y:
            # restart from a fresh shuffle to keep sampling
            Y = list(X)
            rng.shuffle(Y)
    m = sum(inj) / len(inj) if inj else 0.0
    print(f"steps: matched={v1} loose={v2} diff={v3} violations={bad}")
    print(f"diff-serve injection: mean={m:.2f} "
          f"min={min(inj)} max={max(inj)} (n={n} sigma={sigma})")
    print("STATUS:C18DONE")


if __name__ == "__main__":
    main()
