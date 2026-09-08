#!/usr/bin/env python3
"""DP audit of the alternating Greene--Kleitman SCD and phase-cap clamp.

Computations are intended for ssh h100 only.
"""

from __future__ import annotations

import argparse
import math
from collections import defaultdict
from math import comb


def refined_top_counts(b: int):
    """Return n[r][k]: GK chains whose middle source has A-split r and top b+k.

    A coordinates are positions 1,3,...,2b-1.  A top word is a ballot word.
    For top excess k, its middle source loses ceil(k/2) A additions.
    """
    # DP (height, A-ones) after each position, retaining nonnegative prefixes.
    dp = {(0, 0): 1}
    for pos in range(1, 2 * b + 1):
        is_A = pos & 1
        nd = defaultdict(int)
        for (h, aones), val in dp.items():
            # bit 1 = up-step
            nd[(h + 1, aones + is_A)] += val
            # bit 0 = down-step, allowed only above zero
            if h:
                nd[(h - 1, aones)] += val
        dp = nd
    n = [[0] * (b + 1) for _ in range(b + 1)]
    for (height, a_top), val in dp.items():
        if height % 2:
            raise AssertionError((height, a_top))
        k = height // 2
        # total rank at top is b+k automatically.
        r = a_top - ((k + 1) // 2)
        if not (0 <= r <= b):
            raise AssertionError((height, a_top, r))
        n[r][k] += val
    return n


def audit(b: int, H: int):
    n = refined_top_counts(b)
    W = comb(2 * b, b)
    # Exact global SCD chain-top ledger.
    assert all(sum(n[r][k] for r in range(b + 1)) ==
               comb(2*b, b+k) - (comb(2*b, b+k+1) if k < b else 0)
               for k in range(b + 1))

    deficit = 0
    full = 0
    rows = []
    for r in range(b + 1):
        L = comb(b, r) ** 2
        d = abs(2 * r - b)
        nr = max(0, (b - d - H + 2) // 2)
        K = nr * L // b if b and L % b == 0 else nr * L / b
        tails = [[0] * (H + 1) for _ in range(2)]
        for q in range(1, H + 1):
            tails[0][q] = sum(n[r][k] for k in range(q, b + 1) if k & 1)  # A first
            tails[1][q] = sum(n[r][k] for k in range(q, b + 1) if not (k & 1))
            full += tails[0][q] + tails[1][q]
            deficit += max(0, tails[0][q] - K) + max(0, tails[1][q] - K)
        if L and abs(r-b/2) <= 2*math.sqrt(b):
            maximb = max(abs(tails[0][q] - tails[1][q]) for q in range(1, H+1))
            rows.append((r, d, float(K/L), maximb/L,
                         sum(max(0,tails[c][q]-K) for c in (0,1) for q in range(1,H+1))/L))
    expected_full = sum(comb(2*b, b+q) for q in range(1,H+1))
    assert full == expected_full, (full, expected_full)
    print({"b":b,"H":H,"W":W,"full/W":full/W,"deficit/W":deficit/W})
    print("central rows: r d K/L max_orientation_imbalance/L clamp_deficit/L")
    for row in rows:
        print(*row)


def dump(b: int):
    n=refined_top_counts(b)
    for r in range(b+1):
        if any(n[r]):
            tails=[]
            for q in range(0,b+1):
                tails.append(sum(((-1)**k)*n[r][k] for k in range(q,b+1)))
            print("r",r,"n",n[r],"signed_tails",tails)


if __name__ == "__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--b",type=int,required=True)
    ap.add_argument("--H",type=int)
    ap.add_argument("--dump",action="store_true")
    aa=ap.parse_args()
    H=aa.H if aa.H is not None else max(1,int(math.sqrt(aa.b*math.log(aa.b))))
    if aa.dump:
        dump(aa.b)
    else:
        audit(aa.b,H)
