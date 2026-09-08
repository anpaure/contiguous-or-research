# Independent audit: Rayleigh equal-level one-well regeneration

**Date:** 2026-08-05  
**Method:** independent pure-mathematical reconstruction; no computation,
search, or solver  
**Audited theorem:**
`MATH_THEOREM_RAYLEIGH_EQUAL_LEVEL_ONE_WELL_REGENERATION_20260805.md`  
**Verdict:** **GO with no source correction.**  The global `8/5` curvature
ceiling, `2/5` left-slope floor, harmonic endpoint bound, and one-well
conclusion are valid.  The theorem licenses one further algebraic
equal-level subtraction; it does not assert that the resulting second
transform is feasible or iterable.  In fact a separate prefix-Hall audit
is required before any continuation.

## 1. Curvature ceiling

With `Q(x)=2x exp(-x^2)`, direct differentiation gives

\[
 K''(x)=Q'(A-x)+Q'(A+x)\quad(0<x<A),
\]

and `K''(x)=Q'(A+x)<0` beyond `A`.

On `[0,A]`, `Q'` is decreasing because `A<sqrt(3/2)`.  Thus, if
`v=A-x>=3/10`,

\[
 Q'(v)\le Q'(3/10)
 ={41\over25}e^{-9/100}<{8\over5}.
\]

The other summand is negative.  If `v<3/10`, then
`w=A+x=sqrt(pi)-v>7/5`.  The derivative `Q'` is increasing on the relevant
interval `[7/5,sqrt(pi)]`, so

\[
 Q'(w)\le Q'(\sqrt\pi)=-2(2\pi-1)e^{-\pi}<-{2\over5}.
\]

The displayed elementary exponential bounds in the theorem verify the
last rational inequality.  Since `Q'(v)<=2`, the sum is below `8/5`.
The two cases cover the whole compact branch and the noncompact branch is
negative, proving the global ceiling.

## 2. Location of the first zero

At `t=1/2`,

\[
 e^{-(A-t)^2}+e^{-(A+t)^2}
 =2e^{-(\pi+1)/4}\cosh A.
\]

The theorem proves

\[
 e^{(\pi+1)/4}<{203\over72},
 \qquad
 \cosh A>{203\over144}.
\]

Hence the preceding Gaussian sum is strictly above one and
`K(1/2)<0`.  Since `K` has one zero `b` before its minimum, `b<1/2`.
No decimal estimate is being used.

## 3. Left-slope floor

Putting `x=2At` gives the exact identity

\[
 {-K'(t)\over t}
 =4e^{-(A^2+t^2)}
 \left(2A^2{\sinh x\over x}-\cosh x\right).
\]

The bracket has series coefficients

\[
 {2A^2-(2n+1)\over(2n+1)!}.
\]

The constant coefficient is positive and all later coefficients are
negative, so the bracket is decreasing.  The theorem's factorial bound
gives `cosh x<10/7` for `0<=x<=A`; the lower Taylor bound for `sinh A`
then gives

\[
 A\sinh A-{1\over2}\cosh A>{3\over20}.
\]

Together with the exponential estimate this yields
`-K'(1/2)>1/5`.  Both positive factors in the ratio decrease, so

\[
                         {-K'(t)\over t}>{2\over5}
 \qquad(0<t\le1/2).
\]

The monotonicity and endpoint normalization are correct.

## 4. Harmonic transformed density

For an equal-level pair, write

\[
 d_-=c-\ell,qquad d_+=r-c,qquad d_-+d_+=t.
\]

The curvature ceiling and `K'(c)=0` give

\[
 q=-K'(\ell)<{8\over5}d_-,
 \qquad
 a=K'(r)<{8\over5}d_+.
\]

The harmonic map is increasing in each variable, so

\[
 u'(t)={aq\over a+q}
 <{8\over5}{d_-d_+\over d_-+d_+}
 \le {2\over5}t.
\]

Since `t<b<1/2`, the slope floor gives

\[
                         -K'(t)>u'(t).
\]

This independently verifies the main pointwise inequality.  As an
additional cross-check, a separate curvature/slope estimate gives
`u'(t)<19t/48` and `-K'(t)>248t/567`; the latter fractions have the same
strict ordering.

## 5. Signed-tail reconstruction and exact scope

The transformed signed-tail kernel is

\[
 \widetilde K(t)=K(t)+u(t)\quad(t<b),
 \qquad
 \widetilde K(t)=u(t)\quad(t\ge b).
\]

Thus its derivative is transformed-job density minus transformed-socket
density.  The main inequality makes it strictly negative before `b`, while
`u'>0` makes it strictly positive afterward.  The endpoint signs

\[
 \widetilde K(0)=K(0)+m>0,
 \qquad \widetilde K(b)=u(b)<0,
 \qquad \widetilde K(\infty)=0
\]

give one zero and one minimum exactly as claimed.

Cancelling the common overlap then produces another separated pair, and
its two inverse branches define one further equal-level subtraction as a
measure identity.  This is not an induction theorem.  In particular, the
next transformed pair may fail prefix Hall at the origin; the audited
source explicitly excludes later iteration and termination.  No complete
coagulation, discrete rounding, or OR-word claim follows.

