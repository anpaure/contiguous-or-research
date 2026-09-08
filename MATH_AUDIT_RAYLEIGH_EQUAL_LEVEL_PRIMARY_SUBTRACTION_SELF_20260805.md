# Self-audit: Rayleigh equal-level primary subtraction

**Date:** 2026-08-05  
**Audited source:**
`MATH_THEOREM_RAYLEIGH_EQUAL_LEVEL_PRIMARY_SUBTRACTION_20260805.md`  
**Method:** independent symbolic replay inside the main mathematical lane;
no computation, search, or solver  
**Verdict:** GO at the stated reduction-only scope.

## 1. Branch and measure replay

The signed-tail identity is

\[
 K'=j-s\quad(0<t<A),\qquad K'=j\quad(t>A).
\]

The unique-minimum theorem therefore makes `-K' dt` on `(0,c)` the
socket-only Jordan part and `K' dt` on `(c,infinity)` the job-only Jordan
part after diagonal cancellation.  On the negative kernel levels
`m<u<0`, change of variables along the decreasing and increasing inverse
branches gives respectively

\[
 -K'(y)dy=du,
 \qquad K'(x)dx=du.
\]

Thus the equal-level coupling uses every occurrence in `(y_*,c)` and every
residual job exactly once.  No sign or orientation is missing.

## 2. Remainder density replay

With

\[
 a=K'(r(u))>0,\qquad b=-K'(\ell(u))>0,
\]

one has

\[
 z'(u)=r'(u)-\ell'(u)={1\over a}+{1\over b}
 ={a+b\over ab}.
\]

Consequently the pushforward density is `ab/(a+b)`.  The endpoint limits
of the two inverse branches give `z:(m,0)->(0,infinity)` bijectively.
The work identity is exactly the old residual work equality minus
`integral ell(u)du` on both shores.

## 3. Count-slack replay

Writing `c=A theta`, the critical equation gives

\[
 K(c)=1-{2\over1+\theta}e^{-A^2(1-\theta)^2}.
\]

The elementary comparisons used in the source imply

\[
 \theta>{17\over20},\qquad
 e^{-\pi/4}<{17\over37}.
\]

Hence

\[
 e^{-\pi/4}
 +{e^{-A^2(1-\theta)^2}\over1+\theta}
 <{17\over37}+{20\over37}=1,
\]

which is exactly `K(0)>-K(c)`.  The argument uses only strict elementary
bounds and has the correct direction.

## 4. Lifting replay

Because `z` is bijective, a transformed job value determines its unique
level `u`; appending `ell(u)` changes its total from `z(u)` to `r(u)`.
The appended occurrence marginal is precisely the previously removed
socket branch.  Adding back the common one-piece density restores both
original marginals.  Finiteness of transformed configurations is preserved
by adjoining one piece.

## 5. Additional exact recurrence, not used by the theorem

Let `u(t)=z^{-1}(t)` and `b=y_*`.  The signed-tail kernel of the transformed
pair is

\[
 \widetilde K(t)=
 \begin{cases}
 K(t)+u(t),&0\le t<b,\\
 u(t),&t\ge b.
 \end{cases}
\]

Therefore

\[
 \widetilde K(0)=K(0)+K(c)>0,
 \qquad \widetilde K(\infty)=0,
 \qquad \int_0^\infty\widetilde K(t)dt=0.
\]

This recurrence is a useful next target but is deliberately not promoted
to an iteration theorem.  The cumulative prefix inequality

\[
 K(0)-K(t)\ge u(t)-K(c)
\]

only says `widetilde K(t)<=widetilde K(0)`.  It is **not** equivalent to
the stronger pointwise density comparison

\[
 -K'(t)\ge u'(t).
\]

The latter would force `widetilde K` to decrease on `(0,b)` and would be
a substantive new scalar theorem.  No such claim appears in the audited
source.

## 6. Scope

The audit confirms only a structured sufficient reduction.  It does not
prove coagulation of the transformed pair, closure of the transformation
under iteration, finite termination, the all-grid Bellman inequality,
discrete rounding, named containment, chronology, or an OR-word upper
bound.
