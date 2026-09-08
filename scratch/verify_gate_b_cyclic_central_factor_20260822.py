#!/usr/bin/env python3
"""Exact audit of the cyclic Gate-B central-factor theorem."""

from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
from math import comb, factorial


def choose(n: int, k: int) -> int:
    return comb(n, k) if 0 <= k <= n else 0


def multinomial(total: int, cells: tuple[int, ...]) -> int:
    if min(cells) < 0 or sum(cells) != total:
        return 0
    ans = factorial(total)
    for x in cells:
        ans //= factorial(x)
    return ans


@lru_cache(maxsize=None)
def zeta(b: int, s: int, t: int, j: int, h: int) -> Fraction:
    if not max(0, s + t - b) <= h <= min(s, t):
        return Fraction(0)
    den = choose(b, s) * choose(s, h) * choose(b - s, t - h)
    num = 0
    for a in range(j + 1):
        cells = (h - a, s - j - h + a, t - j - h + a,
                 b - s - t + h - a)
        num += (-1) ** (j - a) * choose(j, a) * multinomial(b - 2*j, cells)
    return Fraction(2**j * num, den)


def kappa(b: int, s: int, j: int) -> Fraction:
    return Fraction(2**j * choose(b - 2*j, s - j), choose(b, s))


def overlap(b: int, s: int, a: int, t: int, c: int) -> int:
    left = {(a+i) % b for i in range(s)}
    right = {(c+i) % b for i in range(t)}
    return len(left & right)


def deck_inner(b: int, s: int, starts_s: range, t: int,
               starts_t: range, j: int) -> Fraction:
    return sum((zeta(b, s, t, j, overlap(b, s, a, t, c))
                for a in starts_s for c in starts_t), Fraction())


def central_angle(r: int, j: int) -> Fraction:
    b = 2*r+1
    k = r-2
    specs = ((r, range(1,b)), (r-1, range(1,b)), (k, range(b)))
    g = [[deck_inner(b, s, ss, t, tt, j) for t,tt in specs]
         for s,ss in specs]
    det = g[0][0]*g[1][1]-g[0][1]**2
    assert det > 0 and g[2][2] > 0
    correction = (g[2][0]**2*g[1][1]
                  -2*g[2][0]*g[2][1]*g[0][1]
                  +g[2][1]**2*g[0][0]) / det
    return (g[2][2]-correction)/g[2][2]


def audit_exact_difference(max_r: int = 80) -> int:
    cases = 0
    for r in range(4, max_r+1):
        b = 2*r+1
        for j in range(2, r-1):
            km = kappa(b,r,j); kl = kappa(b,r-1,j)
            J = j*(2*r-j+2)
            a11 = 2*(km-zeta(b,r,r,j,r-1))
            a22 = 2*(kl-zeta(b,r-1,r-1,j,r-2))
            a12 = (zeta(b,r,r-1,j,r-1)-zeta(b,r,r-1,j,r-2))
            assert a11 == 2*km*Fraction(J,r*(r+1))
            assert a22 == 2*kl*Fraction(J,(r-1)*(r+2))
            assert a12 == zeta(b,r,r-1,j,r-1)*Fraction(J,r*r-1)
            rho2 = a12*a12/(a11*a22)
            assert rho2 == Fraction((r-j)*(r-j+2),4*(r*r-1))
            assert rho2 <= Fraction(1,4)
            mu = Fraction(J,2*b*r*(r+1))
            assert mu >= Fraction(2,b*(r+1))
            # A >= (J/(r(r+1))) diag(kappa) in dimension two.
            q = Fraction(J,r*(r+1))
            m11=a11-q*km; m22=a22-q*kl
            assert m11 >= 0 and m22 >= 0 and m11*m22-a12*a12 >= 0
            cases += 1
    return cases


def audit_central_schur(max_r: int = 16) -> int:
    cases=0
    for r in range(4,max_r+1):
        b=2*r+1
        for j in range(2,r-1):
            a0=central_angle(r,j)
            mu=Fraction(j*(2*r-j+2),2*b*r*(r+1))
            theorem=mu/(2*(b-1)**2+mu)
            simple=Fraction(1,27*r**4)
            assert a0 >= theorem >= simple
            cases += 1
    return cases


if __name__ == '__main__':
    n1=audit_exact_difference()
    n2=audit_central_schur()
    print('GATE_B_CYCLIC_CENTRAL_FACTOR_PASS',
          f'difference_cases={n1}', f'central_schur_cases={n2}',
          'uniform_bound=1/(27r^4)')
