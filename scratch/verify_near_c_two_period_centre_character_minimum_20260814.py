#!/usr/bin/env python3
"""H100 audit of the sharp two-period near-C centre character bound."""

from __future__ import annotations

from fractions import Fraction as F
import argparse


def dual(q: int):
    if q == 2:
        return F(1), F(-1), F(0)
    if q == 3:
        return F(4, 3), F(1, 3), F(1)
    if q == 4:
        return F(3, 2), F(0), F(1, 2)
    if q % 3 == 0:
        return F(8*q-6, 3*q), F(12-q, 3*q), F(6-q, q)
    if q % 3 == 1:
        return F(8*q-8, 3*q), F(16-q, 3*q), F(8-q, q)
    return F(8*q-4, 3*q), F(8-q, 3*q), F(4-q, q)


def target(q: int) -> int:
    return q if q <= 4 else (4*q+1)//3


def profile(q: int):
    if q == 2:
        return [(0, 1)]*2 + [(-1, -1)]
    if q == 3:
        return [(-1, 0)]*3 + [(2, 1)]
    if q == 4:
        return [(-1, 1)]*2 + [(0, -1)]*2 + [(1, 1)]
    r = q//3
    if q % 3 == 0:
        return [(-1, 1)]*(2*r) + [(2, -1)]*r + [(-1, -(r-1))]
    if q % 3 == 1:
        return [(-1, 1)]*(2*r+1) + [(2, -1)]*r + [(0, -r)]
    return [(-1, 1)]*(2*r+1) + [(2, -1)]*(r+1) + [(-2, -(r-1))]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-q", type=int, default=1000)
    parser.add_argument("--box-multiple", type=int, default=20)
    args = parser.parse_args()
    checked = 0
    for q in range(2, args.max_q+1):
        gamma, x, y = dual(q)
        s = target(q)
        assert (q+1)*gamma-x+y == 2*s
        p = profile(q)
        assert len(p) == q+1
        assert sum(a for a,b in p) == -1
        assert sum(b for a,b in p) == 1
        assert all((2*a+3*b-1) % q == 0 for a,b in p)
        assert sum(abs(a)+abs(b) for a,b in p) == 2*s
        bound = args.box_multiple*q
        for h in (0,1):
            for a in range(-bound,bound+1):
                for b in range(-bound,bound+1):
                    if (2*a+3*b-h) % q == 0:
                        assert gamma*h+x*a+y*b <= abs(a)+abs(b)
                        checked += 1
    print(
        f"PASS q=2..{args.max_q} box=+-{args.box_multiple}q "
        f"lattice_points={checked} profiles=all"
    )


if __name__ == "__main__":
    main()
