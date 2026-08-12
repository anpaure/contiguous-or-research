# Self-audit: Rayleigh equal-level one-well regeneration

**Date:** 2026-08-05  
**Method:** direct symbolic replay; no computation, search, or solver  
**Source:**
`MATH_THEOREM_RAYLEIGH_EQUAL_LEVEL_ONE_WELL_REGENERATION_20260805.md`  
**Source SHA-256:**
`910adbabec163e81d7896e155255561ec00463ca8fb67b9c7bf69aebd9588e20`  
**Verdict:** **SELF-GO**, with the finite-iteration scope stated in the
source.  An independent audit is still desirable before treating the new
pointwise inequality as authoritative.

## 1. Curvature bound

For `0<=x<=A`, differentiation gives

\[
 K''(x)=Q'(A-x)+Q'(A+x),
 \qquad Q'(z)=2(1-2z^2)e^{-z^2}.
\]

The second summand is negative.  If `A-x>=3/10`, monotonic decrease of
`Q'` through `[3/10,A]` gives the strict `8/5` bound directly.  Otherwise
`A+x=sqrt(pi)-(A-x)>7/5`; on this interval `Q'` is increasing, so it is at
most `Q'(sqrt(pi))<-2/5`, while the first summand is at most two.  The
elementary exponential comparison in the source proves the strict
`-2/5` value.  Above `A`, `K''=Q'(A+x)<0`.  Thus the global ceiling
`K''<8/5` is correctly scoped and directed.

## 2. Zero and slope bounds

At one half,

\[
 e^{-(A-1/2)^2}+e^{-(A+1/2)^2}
 =2e^{-(\pi+1)/4}\cosh A.
\]

The source's rational bounds give the two strict factors

\[
 e^{-(\pi+1)/4}>{72\over203},
 \qquad
 \cosh A>{203\over144},
\]

so their doubled product exceeds one.  Hence `K(1/2)<0`, and the unique
zero indeed obeys `b<1/2`.

For `x=2At`, direct hyperbolic expansion gives

\[
 {-K'(t)\over t}
 =4e^{-(A^2+t^2)}
 \left(2A^2{\sinh x\over x}-\cosh x\right).
\]

The bracket has one positive constant coefficient and strictly negative
higher even-power coefficients.  Its endpoint positivity follows from

\[
 A\sinh A-{1\over2}\cosh A>{3\over20}.
\]

It is therefore positive and decreasing through `x=A`; the exponential
factor is also decreasing.  The endpoint estimate gives
`-K'(1/2)>1/5`, hence `-K'(t)>(2/5)t` on the entire required interval.

## 3. Harmonic-slope comparison

For equal-level endpoints `ell<c<r` at separation `t`, set

\[
 d_-=c-\ell,
 \qquad d_+=r-c,
 \qquad d_-+d_+=t.
\]

Integrating the curvature ceiling from the minimum gives

\[
 -K'(\ell)<{8\over5}d_-,
 \qquad
 K'(r)<{8\over5}d_+.
\]

The transformed-job density is the harmonic parallel sum of these two
slopes.  Monotonicity of that parallel sum and
`d_-d_+<=t^2/4` give

\[
 u'(t)<{8\over5}{d_-d_+\over t}
 \le{2\over5}t<-K'(t).
\]

No comparison of the two endpoint slopes, no symmetry of the well, and no
cumulative-to-pointwise inference is used.  This verifies the central new
inequality.

## 4. Consequence and exact boundary

The transformed tail is `K+u` below the old zero and `u` above it.
Therefore its derivative is strictly negative below the old zero and
strictly positive above it.  Its endpoint signs were already proved in the
primary subtraction theorem, so it has exactly one zero and one minimum.
A second equal-level subtraction is consequently well defined.

The proof uses two numerical-shape bounds special to the original
Rayleigh kernel.  It does not show that the twice-transformed kernel obeys
their analogues.  Thus it proves one-well regeneration for the first
transform and existence of the second subtraction, but not indefinite
iteration, finite termination, an exact coagulation, all-price Bellman
positivity, or any discrete/literal OR-word theorem.

