# Final independent GO audit: `h=4` rectangle upper convexity and KKT pruning

**Date:** 2026-08-04  
**Audited source:**
`MATH_THEOREM_SIX_SLOT_H4_RECTANGLE_UPPER_CONVEXITY_AND_KKT_PRUNING_20260804.md`  
**Audited SHA256:**
`6f8daaba40de9d40c17d429fa4925d4d985d3374fa00d89a5d05651b2529aa11`

## Verdict

**PASS / GO in the exact pruning scope.**  The successor assigns the
endpoint `t=6/5` to the first tail-ratio case and uses the second case only
for `6/5<t<=3/2`.  This repairs the sole false strict endpoint in the
superseded SHA.  No curvature constant or KKT conclusion changes.

## Curvature ledger

For `h(r)=r exp(-r^2)`, the identities

\[
h'(r)=(1-2r^2)e^{-r^2},\qquad
h''(r)=2r(2r^2-3)e^{-r^2}
\]

and

\[
{1\over2}F_\tau''(w)=h'(A-w)+h'(A+w)
+\sum_{q\ge1}h'(A+q\tau+w)
\]

have the correct signs and multiplicities.  On
`2tau/3<=w<=A`, the near reflection is greater than `3/4`, the far compact
reflection is greater than `-2/5`, and the complete period tail is greater
than `-1/25`.

The tail proof is exhaustive.  For `1<=t<=6/5`,
`tau/r<=2/5` and `r^2>16/3`.  For `6/5<t<=3/2`,
`tau/r<=3/7` and `r^2>9pi/4>2997/424`.  The polynomial factors are below
`11/5`, while the exponent gap exceeds `19/4`, so every successive adverse
magnitude is below `1/50` of its predecessor.  The geometric ledger gives
the stated `1/25` tail bound.  Hence

\[
F_\tau''(w)>2\left({3\over4}-{2\over5}-{1\over25}\right)
={31\over50}>0.
\]

## KKT pruning

At a smooth interior branch-`C` point, stationarity requires distinct
upper-band points `P<P+u` to be two zeros of the strictly increasing
`T_tau`; this is impossible.

On branch `U`, the two shift equations give

\[
T_\tau(P)=T_\tau(u)=-T_\tau(P+u)<0,
\]

with `T_tau(P+u)>0`.  Since every `R_tau(w)` in the period equation is
strictly positive, the inactive `Gamma` side is impossible.  On the active
side the remaining equation is exactly

\[
R_\tau(0)+R_\tau(u)+R_\tau(P)+R_\tau(P+u)
=-{1\over2}T_A((A-\delta)/2).
\]

All coefficients and signs agree with the corrected literal rectangle
gate.

## Scope

The result eliminates only the constant-low smooth interior branch and
the inactive-`Gamma` moving-low interior branch.  Boundary and switch
strata and the active residual system remain.  The theorem does not claim
complete rectangle or six-slot positivity.

The superseded SHA
`07bc659e3a1eb6b0dbdab562559d2968de2af6c685d688e0ab6874b598594ff1`
remains fail-closed lineage solely because it used a false strict inequality
at `t=6/5`.
