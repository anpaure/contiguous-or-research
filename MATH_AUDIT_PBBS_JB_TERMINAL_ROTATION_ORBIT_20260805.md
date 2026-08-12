# Audit of the terminal `J_b` rotation-orbit theorem

**Date:** 2026-08-05  
**Method:** independent determinant and mod-three check; no computation or
search

## Verdict

The theorem
`MATH_THEOREM_PBBS_JB_TERMINAL_ROTATION_ORBIT_20260805.md` is exact.

For action `(3,2,1^r)`, the vacancy vector is `(7,3,1)` and direct
expansion of the displayed period matrix gives determinant `21n/gamma`.
The three Cramer minors are

\[
 3,\quad 2(r+7)/\gamma,\quad(16r+91)/\gamma.
\]

Their common gcd with the determinant is one unless `r=2 mod 3`, when it
is three.  In the latter case the character `x_1+x_2 mod 3` annihilates
the period lattice and PBBS translation but not spatial rotation.  Hence
rotation is transitive on the three PBBS cycles, rather than fixing each.

The stabilizing rotation subgroup on one component has order `n/delta`.
Dividing its component length `Delta/delta` by that order gives the exact
factor-time index `21/gamma`, at most 21.  Oddness of the component period
justifies transferring the result unchanged from `f` to `g=f^2`.

The theorem assumes, but does not reprove, the local claim that the named
phase has an alternate max-height occurrence with acceptable q2 payload.

