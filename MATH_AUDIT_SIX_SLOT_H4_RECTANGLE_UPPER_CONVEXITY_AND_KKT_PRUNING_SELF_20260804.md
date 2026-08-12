# Self-audit: `h=4` rectangle upper convexity and KKT pruning

**Date:** 2026-08-04  
**Verdict:** **GO in the stated pruning scope.**  The theorem eliminates
one smooth interior branch and reduces the other to a signed residual
system; it does not claim full rectangle positivity.

## 1. Audited artifact

| file | SHA-256 |
|---|---|
| `MATH_THEOREM_SIX_SLOT_H4_RECTANGLE_UPPER_CONVEXITY_AND_KKT_PRUNING_20260804.md` | `07bc659e3a1eb6b0dbdab562559d2968de2af6c685d688e0ab6874b598594ff1` |

## 2. Second-derivative identity

For `0<=w<=A`,

\[
 K'(w)=2h(A+w)-2h(A-w),
\]

so

\[
 {1\over2}K''(w)=h'(A+w)+h'(A-w).
\]

Every positive-period term lies on the tail branch and contributes
`h'(A+q tau+w)` to one half of `F_tau''`.  Thus (1.2) has the correct
signs and multiplicities.

## 3. Three curvature ledgers

For `s=A-w in [0,A/3]`,

\[
 h''(s)=2s(2s^2-3)e^{-s^2}<0.
\]

The endpoint calculation is

\[
 h'(A/3)
 >{52\over63}{115\over126}
 ={5980\over7938}>{3\over4},
\]

since `4(5980)=23920>23814=3(7938)`.

For `r=A+w>=5A/3`, the adverse magnitude decreases with `r`.  Its
endpoint bound is

\[
 {212\over63}{23\over200}
 ={4876\over12600}<{2\over5}.
\]

For the period tail, the first adverse magnitude is below

\[
 {641\over63\cdot260}.
\]

The two `tau` subranges correctly give the common coefficient-ratio bound
`11/5`:

\[
 {49\over25}{32\over29}<{11\over5},
\]

and

\[
 {100\over49}{2997\over2785}<{11\over5};
\]

the latter cross-product is

\[
 5(299700)=1498500<1501115=11(136465).
\]

The exponent gap is greater than `19/4`, so `e^(19/4)>110` makes the
complete ratio smaller than `1/50`.  Therefore

\[
 {641\over63\cdot260}{50\over49}<{1\over25};
\]

indeed `25(32050)=801250<802620`.

Adding the three ledgers gives

\[
 {1\over2}F_\tau''>{3\over4}-{2\over5}-{1\over25}
 ={31\over100},
\]

hence `F_tau''>31/50`.  The curvature margin and strict increase of
`T_tau` are correct.

## 4. Branch `C` audit

At a smooth interior branch-`C` point, differentiation in `u` gives
`T_tau(P+u)=0`; differentiation in `P` then gives `T_tau(P)=0`.
Interior feasibility has

\[
 2\tau/3<P<P+u<A.
\]

Strict increase of `T_tau` on this band forbids two distinct zeros.  Thus
the branch is eliminated without an unproved global critical-point count.

## 5. Branch `U` audit

The two shift equations imply

\[
 T_\tau(P)=T_\tau(u)=-T_\tau(P+u).
\]

Since `P+u>P` and `T_tau` is strictly increasing on the upper band,

\[
 T_\tau(P)<0<T_\tau(P+u).
\]

This verifies the orientation in (3.2).

Every term in `R_tau(w)` is positive.  Therefore the outer derivative
cannot vanish when `Gamma'=0`.  On the active side,

\[
 \Gamma'=-\tfrac12T_A((A-\delta)/2),
\]

and the remaining period equation is exactly (3.3), with four positive
period trains and one compact threshold slope.

## 6. Scope

Boundary minima, low-branch switches, the `Gamma` switch itself, and the
active residual system remain.  The theorem does not assert their
absence.  Within the claimed curvature and KKT-pruning scope, the audit
verdict is **GO**.
