#!/usr/bin/env python3
"""Computation C5 (block 49): interval-content discrepancy of
transposition-walk schedules.

Model: a cyclic arrangement of n letters; each round applies a set
of adjacent transpositions given by a schedule rule; after each
round we record the contents of all n cyclic k-intervals
(k = m = (n-1)//2 -- central rank via complement bijection).
Run R = ceil((1+eps) * C(n,m) / n) rounds so slots = n*R ~=
(1+eps) * W, the MDCU budget.  Report distinct/W (coverage),
multiplicity var/mean (dispersion; Poisson = 1), for schedules:

  rand1   : one uniform random adjacent swap per round
  rand2   : two uniform random adjacent swaps per round
  gold1   : one swap at position floor(r*n*phi) mod n  (golden)
  gold2   : swaps at golden and silver rotation positions
  brick   : odd-even brick-wall (periodic control)
  static  : no swaps (recycling control)

The MDCU needs coverage -> 1 with var/mean < 1 (sub-Poisson).
Poisson baseline: coverage 1 - exp(-lambda), var/mean ~ 1.
"""
import math
import random
import sys
from collections import Counter

PHI = (5 ** 0.5 - 1) / 2
SIL = 2 ** 0.5 - 1


def run(n, eps, rule, seed=1):
    m = (n - 1) // 2
    W = math.comb(n, m)
    R = math.ceil((1 + eps) * W / n)
    arr = list(range(n))
    rng = random.Random(seed)
    C = Counter()
    for r in range(R):
        if rule == "rand1":
            swaps = [rng.randrange(n)]
        elif rule == "rand2":
            swaps = [rng.randrange(n), rng.randrange(n)]
        elif rule == "gold1":
            swaps = [int(r * n * PHI) % n]
        elif rule == "gold2":
            swaps = [int(r * n * PHI) % n, int(r * n * SIL) % n]
        elif rule == "brick":
            swaps = list(range(r % 2, n - 1, 2))
        elif rule == "static":
            swaps = []
        for i in swaps:
            j = (i + 1) % n
            arr[i], arr[j] = arr[j], arr[i]
        for p in range(n):
            s = frozenset(arr[(p + t) % n] for t in range(m))
            C[s] += 1
    slots = n * R
    lam = slots / W
    cov = len(C) / W
    mults = list(C.values())
    mean = sum(mults) / len(mults)
    var = sum((x - mean) ** 2 for x in mults) / len(mults)
    poiss_cov = 1 - math.exp(-lam)
    return (f"n={n} {rule:6s}: cov={cov:.3f} (poisson {poiss_cov:.3f}) "
            f"var/mean={var / mean:.2f} slots={slots} W={W}")


def main():
    eps = 0.2
    for n in (9, 11, 13, 15):
        for rule in ("rand1", "rand2", "gold1", "gold2", "brick",
                     "static"):
            print(run(n, eps, rule), flush=True)
    print("STATUS:C5DONE")


if __name__ == "__main__":
    main()
