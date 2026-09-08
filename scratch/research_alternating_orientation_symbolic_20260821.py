#!/usr/bin/env python3
"""Symbolic factorization of orientation-retirement inequalities."""

import sympy as sp


b, r, u = sp.symbols("b r u", positive=True, integer=True)

# E_{u+1}/E_u from exact binomial ratios.
eratio = (b-r-u) * (r-u) / ((r+u+1) * (b-r+u+1))

ratio_a = sp.factor(
    eratio * (b-r-u-1)/(b-2*u-2) * (b+2*u+1)/(b-r-u)
)
ratio_b = sp.factor(
    eratio * (r-u-1)/(b-2*u-2) * (b+2*u+1)/(r-u)
)

print("RATIO_A", ratio_a)
print("ONE_MINUS_A_NUM", sp.factor(sp.together(1-ratio_a)).as_numer_denom()[0])
print("RATIO_B", ratio_b)
print("ONE_MINUS_B_NUM", sp.factor(sp.together(1-ratio_b)).as_numer_denom()[0])

a, c = sp.symbols("a c", positive=True, integer=True)
ra = sp.factor(a*(c-1)*(a+c+4*u+1)/((a+2*u+1)*(c+2*u+1)*(a+c-2)))
rb = sp.factor(c*(a-1)*(a+c+4*u+1)/((a+2*u+1)*(c+2*u+1)*(a+c-2)))
print("AC_DIFF_A", sp.factor((a+2*u+1)*(c+2*u+1)*(a+c-2)-a*(c-1)*(a+c+4*u+1)))
print("AC_DIFF_B", sp.factor((a+2*u+1)*(c+2*u+1)*(a+c-2)-c*(a-1)*(a+c+4*u+1)))
A, C = sp.symbols("A C", nonnegative=True, integer=True)
da = (a+2*u+1)*(c+2*u+1)*(a+c-2)-a*(c-1)*(a+c+4*u+1)
db = (a+2*u+1)*(c+2*u+1)*(a+c-2)-c*(a-1)*(a+c+4*u+1)
print("SHIFT_DIFF_A", sp.expand(da.subs({a:A+1,c:C+1})))
print("SHIFT_DIFF_B", sp.expand(db.subs({a:A+1,c:C+1})))
