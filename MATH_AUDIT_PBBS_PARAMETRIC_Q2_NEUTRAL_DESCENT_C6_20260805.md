# Audit: parametric q2-neutral three-sector PBBS C6

**Date:** 2026-08-05  
**Audited source:**
`MATH_THEOREM_PBBS_PARAMETRIC_Q2_NEUTRAL_THREE_SECTOR_DESCENT_C6_20260805.md`  
**Method:** independent symbolic block replay  
**Verdict:** PASS for `t>=1`, `h>=t+3`.

The four active coordinates and the sets `A,B,C,E` partition the ground
set, with `|H|=m-1` and `|K|=m-2`.  The deficit-three blocks of `H` are
literally `empty,M_t,M_h`.  Flipping `a_i` leaves forward root `a_(i+2)`;
the three normalized shapes are `M_h 10 M_t`, `1 M_t 0 M_h`, and
`M_t 1 M_h 0`.  Their reverse root is the first down-step `c` of `M_h`.
This reproduces all old edges.

For the companion calculation, complementing `X_i` and restoring its
displayed forward root gives `P_i`.  The normalized shapes in the source
are exact.  Their first mountain has height `h+1,h,h`, while every later
competitor has height at most `t,t+1,t+1`; hence the common reverse root is
the next coordinate `d`.  Intersecting `P_i` with `f^(-2)(P_i)` deletes
exactly `d` in all three rows.

Peak-pruning gives the unordered soliton partitions

\[
 (h,t,1),\qquad(h,t+1),\qquad(h+1,t).
\]

Their top gaps are at least `3,2,4`, respectively, so the separately
proved soliton-gap theorem makes all six occurrences forced selected.
Distinct partitions separate the three old components.  The
common-deletion classification then makes the clean C6 q2-neutral and its
three-cycle topology is a merger.

Finally

\[
 \Psi(h,t+1)-\Psi(h,t,1)=t,
 \qquad
 \Psi(h+1,t)-\Psi(h,t+1)=h-t,
\]

so the claimed quotient orientation is strictly descending.  No
angle-level expansion or rotated-copy count is inferred.
