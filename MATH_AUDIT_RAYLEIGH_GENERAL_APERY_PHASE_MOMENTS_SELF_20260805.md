# Self-audit of the general Apéry phase-moment reduction

**Date:** 2026-08-05  
**Method:** independent algebraic replay; pure mathematics; no computation,
search, or solver  
**Audited source:**
`MATH_THEOREM_RAYLEIGH_GENERAL_APERY_PHASE_MOMENTS_AND_VARIANCE_GATE_20260805.md`  
**Verdict:** **PASS.**  The phase-branch endpoints, two telescoping moments,
Parseval constants, normalized variance gate, and pair-difference reduction
all check.  The cyclic variance inequality remains explicitly conjectural.

## 1. Branch geometry and telescoping

With `a_r=r-e_r`, the branch between consecutive phase points has length

\[
 a_{r+1}-a_r=1+e_r-e_{r+1}
\]

and discrepancy descending from `1+e_r` to `e_(r+1)`.  Hence its first
and second raw integrals are respectively

\[
 {1\over2}\bigl((1+e_r)^2-e_{r+1}^2\bigr)
\]

and

\[
 {1\over3}\bigl((1+e_r)^3-e_{r+1}^3\bigr).
\]

Cyclic summation cancels the pure square and cube terms, giving

\[
 \mathbb ED={1\over2}+\bar e,
 \qquad
 \mathbb ED^2={1\over3}+\bar e+\overline{e^2}.
\]

Subtracting the square of the mean yields

\[
 \operatorname {Var}(D)={1\over12}+\operatorname {Var}(e).
\]

Repeated phases create zero-length branches and do not disturb the sum.

## 2. Fourier factor audit

For real periodic `D`,

\[
 \sum_{n\ge1}|\widehat D_n|^2
 ={1\over2}\operatorname {Var}(D).
\]

Pairing Fourier signs and using the transform bound gives

\[
 |N|<{BP^2\over2\pi^2}
       \sum_{n\ge1}{|\widehat D_n|\over n^2}.
\]

Cauchy--Schwarz with `zeta(4)=pi^4/90` yields

\[
 |N|<{BP^2\over2\sqrt{90}}
      \sqrt{{\operatorname {Var}(D)\over2}}.
\]

Using `BP^2<12 sqrt(15)M`, the coefficient becomes

\[
 {12\sqrt{15}\over2\sqrt{90}}{1\over\sqrt2}
 =\sqrt3,
\]

so

\[
 |N|<M\sqrt{3\operatorname {Var}(D)}
 =M\sqrt{{1\over4}+3\operatorname {Var}(e)}.
\]

The zeroth mode is `M(1/2+bar e)`.  Thus the source's lower bound and the
equivalence of its sufficient variance inequality are exact.

## 3. Equality calibrations

For `e=0`, both sides of the residue inequality vanish.  For
`e_r=r`,

\[
 \bar e={g-1\over2},
 \qquad
 \operatorname {Var}(e)={g^2-1\over12}
 ={\bar e(\bar e+1)\over3}.
\]

For a mechanical floor clock, the full cell discrepancy is
`A_h+(g/h)V`; the same square difference used in the source is

\[
 2(g/h-1/h)(1-1/h)\ge0.
\]

Thus all stated calibrations are consistent.

## 4. Pair-difference reduction

Subadditivity gives

\[
 e_{r+t}-e_r\le e_t,
 \qquad
 e_{r+t}-e_r\ge-e_{-t}.
\]

For fixed `t`, the differences average to zero.  A zero-mean variable in
`[-a,b]` has second moment at most `ab`, yielding the source's fixed-shift
bound.  Averaging over `t` uses

\[
 {1\over g^2}\sum_{r,t}(e_{r+t}-e_r)^2
 =2\operatorname {Var}(e),
\]

and gives

\[
 \operatorname {Var}(e)
 \le {1\over2g}\sum_t e_t e_{-t}.
\]

The proposed product inequality has exactly the coefficient needed to
imply the variance gate.  It is an open sufficient statement, not claimed
as proved.

## 5. Scope

The theorem is an exact analytic reduction of the periodic formal clock.
It does not prove the cyclic metric inequality and does not include the
nonperiodic finite shoulder.  Those exclusions are explicit.

**Final verdict: PASS.**
