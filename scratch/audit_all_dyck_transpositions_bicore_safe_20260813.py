#!/usr/bin/env python3
"""Audit whether every Dyck transposition has an h-safe MSW sign.

Heavy runs are intended for ssh h100 only.
"""

from __future__ import annotations

import argparse
from functools import lru_cache


@lru_cache(None)
def dyck_words(r: int) -> tuple[str, ...]:
    if r == 0:
        return ("",)
    out = []
    for a in range(r):
        for u in dyck_words(a):
            for v in dyck_words(r - 1 - a):
                out.append("1" + u + "0" + v)
    return tuple(out)


def mu(w: str) -> str:
    return "".join("1" if c == "0" else "0" for c in reversed(w))


@lru_cache(None)
def rho(w: str) -> tuple[int, ...]:
    if not w:
        return ()
    height = 0
    cut = None
    for i, c in enumerate(w):
        height += 1 if c == "1" else -1
        if height == 0:
            cut = i
            break
    assert cut is not None and w[0] == "1" and w[cut] == "0"
    u, v = w[1:cut], w[cut + 1 :]
    d = len(u) + 2
    return (d,) + tuple(d - x for x in rho(mu(u))) + (1,) + tuple(
        d + x for x in rho(v)
    )


def ranks(w: str):
    p = rho(w)
    ins = p[0::2]
    dele = p[1::2]
    return ({x: i + 1 for i, x in enumerate(ins)},
            {x: i + 1 for i, x in enumerate(dele)})


def audit(r: int, h: int):
    words = dyck_words(r)
    ws = set(words)
    rank = {w: ranks(w) for w in words}
    edges = plus = minus = both = neither = 0
    witness = None
    for x in words:
        ones = [i + 1 for i, c in enumerate(x) if c == "1"]
        zeros = [i + 1 for i, c in enumerate(x) if c == "0"]
        ix, dx = rank[x]
        for q in ones:
            for p in zeros:
                y_list = list(x)
                y_list[q - 1] = "0"
                y_list[p - 1] = "1"
                y = "".join(y_list)
                if y not in ws or x >= y:
                    continue
                iy, dy = rank[y]
                ps = dx[q] > h and dy[p] > h
                ms = ix[p] <= r - h and iy[q] <= r - h
                edges += 1
                plus += ps
                minus += ms
                both += ps and ms
                neither += not ps and not ms
                if witness is None and not ps and not ms:
                    witness = {
                        "x": x,
                        "y": y,
                        "p": p,
                        "q": q,
                        "dxq": dx[q],
                        "dyp": dy[p],
                        "ixp": ix[p],
                        "iyq": iy[q],
                    }
    return {
        "r": r,
        "h": h,
        "vertices": len(words),
        "edges": edges,
        "plus": plus,
        "minus": minus,
        "both": both,
        "neither": neither,
        "witness": witness,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--r-min", type=int, default=3)
    ap.add_argument("--r-max", type=int, default=11)
    ap.add_argument("--all-h", action="store_true")
    args = ap.parse_args()
    for r in range(args.r_min, args.r_max + 1):
        hs = range(1, (r - 1) // 2 + 1) if args.all_h else [max(1, int(r**0.5))]
        for h in hs:
            print(audit(r, h), flush=True)


if __name__ == "__main__":
    main()
