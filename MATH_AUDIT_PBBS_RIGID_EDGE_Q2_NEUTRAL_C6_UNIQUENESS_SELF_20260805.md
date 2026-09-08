# Self-audit: uniqueness and graphic no-go for one clean `C6`

**Date:** 2026-08-05  
**Audited source:**
`MATH_THEOREM_PBBS_RIGID_EDGE_Q2_NEUTRAL_C6_UNIQUENESS_AND_GRAPHIC_NOGO_20260805.md`  
**Verdict:** **PASS**, conditional only on the already audited
common-deletion classification and two-soliton topology theorem.

## 1. Normalization

On a rigid mountain edge, root zero gives `P_0={1,...,m}`.  Its backward
and forward distinguished deletions are the first and last up-steps, so
`d=1`, `a_1=m`.  Since `K+a_0+a_1=P_0`, the remaining active `a_0=s`
lies in `2,...,m-1`; the fourth active `a_2=t` lies in the zero tail
`m+1,...,2m`.

## 2. Height forcing

For `P_1=P_0-s+t`, before `t` the maximal height is
`max(s-1,m-2)=m-2`.  At `t`, the number of ones and zeros in the prefix is
respectively `m` and `t-m`, so the height is `2m-t`.  Requiring `t` to be
the first global-maximum up-step gives

\[
 2m-t>m-2,qquad t\ge m+1,
\]

and hence `t=m+1`.

Then `P_2=P_0-m+(m+1)` has word `1^(m-1)010^(m-1)`.  Its first maximum is
at `m-1`; the later active up-step ties it.  Since the forward deletion is
required to be `a_0=s`, one gets `s=m-1`.  No alternate coordinate choice
survives.

## 3. Imported component calculation

With these forced labels, the companion shapes are exactly `A_1` and
`B_(m-2)` in the audited `(m-1,1)` shape rotor.  They lie on one lifted
component of period `(2m+1)(2m-3)`, and every position on that component is
max-height selected for `m>=4`.  The independently audited reconnection
calculus changes the two old completely selected cycles into two new
completely selected cycles.

Thus the theorem correctly excludes one q2-neutral clean common-core
`C6`, while leaving multi-switch and larger-circuit repairs open.
