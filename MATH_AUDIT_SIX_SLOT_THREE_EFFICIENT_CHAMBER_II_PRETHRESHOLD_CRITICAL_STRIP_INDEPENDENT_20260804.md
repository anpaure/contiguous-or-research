# Independent audit: six-slot `h=3` chamber-II prethreshold critical strip

**Date:** 2026-08-04  
**Method:** pure differentiation and endpoint algebra only; no numerical
search or enumeration.  
**Audited source:**
`MATH_THEOREM_SIX_SLOT_THREE_EFFICIENT_CHAMBER_II_PRETHRESHOLD_CRITICAL_STRIP_REDUCTION_20260804.md`  
**Audited source SHA-256:**
`8101f952bdfc4900f2fdd9d4b6396642c694c850cb420c7ef8dc03e24f19c1f3`

## Verdict

**PASS as a reduction.**  The exact two-compact-row formula, the
critical-point curvature implication, and the endpoint split are all
correct.  Three residual prethreshold/stationary gates remain unsigned.

## 1. Exact train and derivatives

For `0<=w<A-p` with `p>=A/2`, exactly `w` and `p+w` are compact; every
later row is at or beyond threshold.  Expanding the two compact kernels
and combining their outward Gaussian terms with the tail gives

\[
 F_p(w)=2-e^{-(A-w)^2}-e^{-(A-p-w)^2}
 -\sum_{q\ge0}e^{-(A+w+qp)^2}.
\]

This remains valid by continuity at `w=A-p`.  Differentiating termwise
gives exactly equations (1.4) and (1.5) of the source with
`phi(x)=x e^{-x^2}`.

## 2. Critical curvature calculation

At a critical point, put

\[
 z=A+w,\qquad w_0=A-w,\qquad w_1=A-p-w.
\]

Since `lambda=phi'/phi=1/x-2x` is strictly decreasing,

\[
 \sum_{q\ge0}\phi'(z+qp)
 \le \lambda(z)\sum_{q\ge0}\phi(z+qp).
\]

Substituting the critical equation yields the two coefficients

\[
 2A\left({1\over A^2-w^2}-2\right)
\]

and

\[
 (2A-p)\left({1\over(A+w)(A-p-w)}-2\right).
\]

Because `w<A-p<=A/2`,
`A^2-w^2>3A^2/4=3\pi/16>1/2`; the first coefficient is strictly
negative.  If `(A+w)(A-p-w)>=1/2`, the second is nonpositive, so
`F_p''(w)<0`.  Hence an interior local minimum must satisfy the strict
reverse inequality.  This is exactly the claimed critical strip; no
converse is asserted.

## 3. Endpoint split

For fixed feasible `(p,a)`, the compactified interval has upper endpoint

\[
 B(p,a)=\min\{(p+a)/2,A-p\}.
\]

A global minimum on this compact interval is either an endpoint or an
interior critical point.  The curvature lemma excludes every interior
minimum outside `C_{p,a}`.  The source correctly uses a one-sided limit
when `B=A-p`, matching the strict physical condition `b<A-p`.

The endpoint comparison is exact:

\[
 B=A-p\iff3p+a\ge2A,
 \qquad
 B=(p+a)/2\iff3p+a\le2A.
\]

On the threshold endpoint, the five-slot table

\[
 (0,a,A-p,p,p+a,A)
\]

is internally superadditive.  Besides the immediate chamber inequalities,
the only non-obvious condition is `2p>=A+a`.  It follows by splitting at
`a=A/5`: if `a<=A/5`, use `3p+a>=2A`; if `a>=A/5`, use `p>=3a`.
The remaining endpoint inequalities follow from `A-p>=2a` and
`3p+a>=2A`.  All entries before the endpoint are below `A`, so complete
five-slot positivity applies.

At the other endpoint, setting `beta=(p-a)/2` gives

\[
 p=a+2\beta,
 \qquad
 (p+a)/2=a+\beta,
\]

and the last compact value is `(3p+a)/2<=A`, exactly the stated
prethreshold repeated-gap train.  At the lower endpoint, the honest
chamber condition gives `p+2a<A`.

## 4. Scope check

The source correctly leaves unsigned:

1. the lower prethreshold endpoint `L_3(p;a,2a)`;
2. the prethreshold repeated-gap endpoint;
3. the stationary critical strip.

It proves neither chamber-II positivity nor any larger Bellman theorem.
