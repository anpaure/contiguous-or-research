#!/usr/bin/env python3
"""C19 (block 75): the INTERLEAVED rule — preregistered test of the
R'' route to LAL'.

Rule INTER(p): deterministic feedback times via Bresenham spacing
(feedback iff floor(t*p) > floor((t-1)*p)).  On a feedback step:
pick uniformly among fan-zeros at the focus rank if any, else
uniformly among eligible.  On a uniform step: pick uniformly among
ALL eligible letters (no preference — these steps are the mixing
half).  p = 1.0 is C15b's "fresh"; p = 0.0 is the pure random walk.

PREREGISTERED PREDICTIONS (recorded before running; block 75.5):
  (P1) at p in {0.75, 0.9} the final misses' late appearance
       counts (t0 = 3L/4) rise by >= 2x vs p = 1.0 (access
       restored by the uniform steps);
  (P2) final miss count is U-shaped in p: p = 0.9 (or 0.75)
       strictly beats BOTH p = 1.0 (grooved greedy) and p = 0.0
       (coupon wall) at equal budget;
  (P3) failure mode: if misses(p<1) >= misses(p=1) across the
       board and late-apps do not move, the R'' route is
       empirically dead.
n = 15, sigma in {4, 6}, slack 1.2, focus rank k = m+1, 2 seeds.
"""
import math
import random
from collections import Counter


def run(n, sigma, slack, seed, p):
    floor = n - sigma
    m = (n - 1) // 2
    kf = m + 1
    W = math.comb(n, kf)
    L = math.ceil(slack * W / n) * n
    t0 = 3 * L // 4
    last = {x: x for x in range(n)}
    w = list(range(n))
    rng = random.Random(seed)
    fib = Counter()
    seen = set()
    app = Counter()
    crowd = 0
    serves = 0
    for pos in range(n - kf + 1):
        s = frozenset(w[pos:pos + kf])
        fib[s] += 1
        seen.add(s)
    for t in range(n, L):
        elig = [x for x in range(n) if t - last[x] >= floor]
        if not elig:
            return None
        pref = w[t - kf + 1:t]
        fans = {x: s for x in elig
                for s in [frozenset(pref + [x])] if len(s) == kf}
        zf = [x for x, s in fans.items() if s not in seen]
        if t > t0:
            if len(zf) >= 2:
                crowd += len(zf) - 1
            for x in zf:
                app[fans[x]] += 1
        feedback = math.floor(t * p) > math.floor((t - 1) * p)
        if feedback and zf:
            pick = rng.choice(zf)
            serves += 1
        else:
            pick = rng.choice(elig)
        w.append(pick)
        last[pick] = t
        if pick in fans:
            s = fans[pick]
            fib[s] += 1
            seen.add(s)
    C = set()
    for pos in range(L):
        s = frozenset(w[(pos + q) % L] for q in range(kf))
        if len(s) == kf:
            C.add(s)
    import itertools
    allsets = {frozenset(c) for c in itertools.combinations(range(n), kf)}
    misses = allsets - C
    acounts = sorted(app[s] for s in misses) if misses else []
    meanapp = sum(acounts) / max(len(acounts), 1)
    return (L, len(misses), crowd, serves, meanapp, acounts[:5])


def main():
    slack = 1.2
    n = 15
    for sigma in (4, 6):
        for p in (0.0, 0.5, 0.75, 0.9, 1.0):
            for seed in range(2):
                r = run(n, sigma, slack, seed, p)
                if r is None:
                    print(f"n={n} sig={sigma} p={p} seed={seed}: "
                          f"infeasible", flush=True)
                    continue
                L, miss, crowd, serves, meanapp, low5 = r
                print(f"n={n} sig={sigma} p={p} seed={seed} L={L}: "
                      f"miss={miss} lateCrowd={crowd} serves={serves} "
                      f"missLateApp(mean={meanapp:.2f} low5={low5})",
                      flush=True)
    print("STATUS:C19DONE")


if __name__ == "__main__":
    main()
