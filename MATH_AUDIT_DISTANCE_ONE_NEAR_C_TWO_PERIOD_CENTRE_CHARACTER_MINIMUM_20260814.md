# Independent audit: two-period near-C centre-character minimum

**Date:** 2026-08-14
**Source:** `MATH_THEOREM_DISTANCE_ONE_NEAR_C_TWO_PERIOD_CENTRE_CHARACTER_MINIMUM_20260814.md`
**Verdict:** PASS

## 1. Result audited

The source proves that every two-period distance-one near-`C` trade with
periods `2q+2` and `2q+3` obeys

\[
 2a_z+3b_z\equiv\mathbf1_{H_0}(z)\pmod q,
 \qquad \sum_za_z=-1,\qquad\sum_zb_z=1,
\]

and hence uses at least

\[
 s_q=
 \begin{cases}
 q,&2\le q\le4,\\
 \lfloor(4q+1)/3\rfloor,&q\ge5
 \end{cases}
\]

rails on each physical shore.  The bound is sharp for the integer centre
ledger.  The source correctly does not claim that an extremal ledger has a
simple cyclic-window realization.

## 2. Symbolic supporting-plane audit

For `q>=5`, substituting `2a+3b=h+qk` and multiplying the claimed dual
inequality by `3q` reduces its three residue classes exactly to

\[
 L(a,b)\ge ck+8h,
 \qquad L=3(|a|+|b|)+a+3b,
 \qquad c=6,8,4
\]

for `q mod 3=0,1,2`.  The source's four-orthant proof is complete:

- in the nonnegative orthant, `L=2(h+qk)` and the impossible equation
  `2a+3b=1` forces `k>=1` when `h=1`;
- in either mixed orthant, `L=2(h+qk)+6t`, where `t>=1` is the magnitude
  of the negative coordinate;
- all negative-`k` cases are automatic except the displayed boundary
  `h=1,k=-1`, whose two mixed subcases are resolved by the congruence;
- in the negative orthant the only delicate row is `q mod 3=2`, where
  `|a|=1` contradicts the residue and therefore `L>=4`.

The separate `q=2,3,4` arguments are also exact.  In particular, for
`q=4,h=1`, the cases `b=0,2` are impossible and `b=1` forces `a` odd.
The proof treats `h=0` pointwise, so arbitrarily many exterior centres
cannot lower the dual bound.

## 3. Ledger and extremal-profile audit

The distinction between net ledger mass and physical shore size is now
correct: each physical shore dominates the positive or negative mass of
the net centre ledger, with equality precisely when no centre/period class
appears on both shores.  Literal cancellation alone need not remove
aggregate cancellation between different cyclic orders in one class.
Summing the supporting plane and using the two global sums gives exactly
`2s_q`.

Every profile in (3.8)--(3.9) has exactly `q+1` entries, has coordinate
sums `(-1,1)`, satisfies residue one in every entry, and has `ell_1` norm
`2s_q`.  Thus sharpness at the integer-ledger level is proved.  No
classification of all equality pairs is used.

## 4. Independent finite replay

An exact-rational H100 replay checked:

- the dual identity and all displayed profiles for `q=2..1000`; and
- the pointwise supporting inequality for both `h=0,1` in the box
  `|a|,|b|<=5q` for `q=2..100`.

This replay is corroborative only; the all-`q` proof is the symbolic
orthant argument above.

## 5. Scope

The theorem is an algebraic obstruction and exact finite-design reduction.
It does not prove a positive rail decomposition, simplicity, forbidden-owner
avoidance, residence compatibility, or a global factor.

The source and this audit are frozen by their SHA-256 values reported with
the checkpoint.
