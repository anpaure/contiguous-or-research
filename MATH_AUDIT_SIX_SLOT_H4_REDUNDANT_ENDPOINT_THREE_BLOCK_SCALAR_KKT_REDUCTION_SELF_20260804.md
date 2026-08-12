# Self-audit: six-slot `h=4` redundant-endpoint scalar/KKT reduction

**Date:** 2026-08-04

**Audited source:**
`MATH_THEOREM_SIX_SLOT_H4_REDUNDANT_ENDPOINT_THREE_BLOCK_SCALAR_KKT_REDUCTION_20260804.md`

**Audited source SHA-256:**
`f410d86f5d544755c08f269ece1d47910f2d3c055be91c7a391bb548090f53d3`

**Method:** independent symbolic replay from the canonical Bellman table,
the literal endpoint comparison, and direct differentiation of the Gaussian
train.  No search, sampling, solver, or floating-point inequality is used.

## 1. Verdict

**PASS as a reduction.**  The three composite endpoint faces reduce to the
two scalar gates stated in the source.  The critical-point lemma and the
inner/outer derivative ledger are exact.  Neither scalar gate is signed, so
the source correctly does not claim complete `h=4` positivity.

## 2. Redundancy and coordinate replay

The canonical table is

\[
 (0,x,y,z,P,P+u,P+v).
\]

On the three inert faces,

\[
\begin{aligned}
v=x+u&\Longrightarrow P+v=x+(P+u),\\
v=y&\Longrightarrow P+v=y+P,\\
v=2z-P&\Longrightarrow P+v=2z.
\end{aligned}
\]

Replacing every size-six generator by the indicated lower configuration is
lossless in both capacity and value.  This proves equality of the complete
Bellman clocks, not merely a one-sided comparison.

Set

\[
 p=A-P,
 \qquad a=p-u,
 \qquad\delta=v-p,
 \qquad\tau=P+v.
\]

Then `tau=A+delta`.  The canonical bounds give

\[
 0<p\le A/3,
 \qquad0<a\le p.
\]

Maximum efficiency gives `P+v<=3P/2`, so, since `P<A`,

\[
                         0<\delta<A/2
\]

on every genuinely inert point.  Finally,

\[
\begin{aligned}
x+u-p&=x-a,\\
y-p&=y-p,\\
(2z-P)-p&=2z-A.
\end{aligned}
\]

Therefore endpoint saturation is exactly

\[
 \delta=\max\{x-a,y-p,2z-A\}.
\]

This proves all three displacement inequalities and the assertion that at
least one is tight.

## 3. Endpoint-period comparison

For every `q>=0` and `0<=r<=5`, `q` endpoint configurations plus the
size-`r` generator give value

\[
                         q\tau+c_r.
\]

At `q=0`, internal superadditivity gives `V_r=c_r`.  At `q>=1`, the
candidate is at least `tau>=A`, the Bellman optimum is no smaller, and `K`
is increasing on the Gaussian tail.  Hence

\[
                         K(V_{6q+r})\ge K(q\tau+c_r).
\]

Summing gives exactly

\[
 C(\tau)+F_\tau(x)+F_\tau(A-a)
 +F_\tau(y)+F_\tau(A-p)+F_\tau(z).
\]

No formal Apéry value or finite-head sign is used in this comparison.

## 4. Fresh critical-point calculation

For `0<=w<=A/2` and `tau>=A`, direct expansion gives

\[
 F_\tau(w)
 =1-e^{-(A-w)^2}
 -\sum_{q\ge0}e^{-(A+w+q\tau)^2}.
\]

With `phi(t)=t exp(-t^2)` and
`lambda(t)=1/t-2t`, a critical point satisfies

\[
 \sum_{q\ge0}\phi(A+w+q\tau)=\phi(A-w).
\]

Since `lambda` strictly decreases,

\[
\begin{aligned}
{1\over2}F_\tau''(w)
&=\sum_{q\ge0}\phi'(A+w+q\tau)+\phi'(A-w)\\
&\le
\bigl(\lambda(A+w)+\lambda(A-w)\bigr)\phi(A-w)\\
&=2A\left({1\over A^2-w^2}-2\right)\phi(A-w).
\end{aligned}
\]

For `w<=A/2`,

\[
 A^2-w^2\ge3\pi/16>1/2,
\]

so the last line is strictly negative.  Every interior critical point is a
strict maximum.  The minimum on any subinterval of `[0,A/2]` is therefore
at an endpoint.  This independently verifies the only analytic lemma used
to eliminate a physical low shift.

## 5. Envelope audit

Take one pair `(r,A-b)` from the endpoint train.  Both possible bases are
`b=a` or `b=p`, hence `0<=b<=A/3`.  The low shift satisfies

\[
 0\le r\le\min\{A/2,b+\delta\}=m_\delta(b).
\]

The critical-point lemma gives exactly

\[
 F_\tau(r)
 \ge\min\{F_\tau(0),F_\tau(m_\delta(b))\}.
\]

Adding the high shift and then minimizing over `b` proves the inactive
envelope `mathcal I(delta)`.

On face `X`, the active low shift is `x=a+delta`; on face `Y`, it is
`y=p+delta`.  For `X`, `x<=P/4` gives `3x<=P<=tau`.  For `Y`, internal
superadditivity gives `2y<=P`, hence `3y<=P+y=tau`.  Therefore the active
base satisfies

\[
 b\le{A-2\delta\over3}=B_\delta,
\]

which proves the exact domain of `mathcal H(delta)`.

The remaining endpoint inequality is `2z<=tau`, so the singleton is at
least `mathcal S(delta)`.  Allocating the unique ceiling to the active pair
gives

\[
                         \Phi\ge\mathcal H+\mathcal I+\mathcal S
\]

on `X` and `Y`.

On `Z`, `z=tau/2`, while both pairs satisfy the inactive bound.  Splitting
the half-step ceiling into its even and odd terms gives the exact identity

\[
 C(\tau)+F_\tau(\tau/2)=C(\tau/2).
\]

Thus

\[
                         \Phi\ge C(\tau/2)+2\mathcal I.
\]

All inequality directions are therefore correct.  In particular, if the
physical functional were nonpositive, its corresponding scalar lower gate
would necessarily be nonpositive as well.

## 6. KKT replay

Write

\[
 T_\tau(w)=F_\tau'(w),
 \qquad
 R_\tau(w)=\partial_\tau F_\tau(w).
\]

For the active pair objective

\[
 C(\tau)+F_\tau(b+\delta)+F_\tau(A-b),
\]

interior differentiation in `b` gives

\[
 T_\tau(b+\delta)-T_\tau(A-b)=0.
\]

For the inactive envelope, selecting the fixed low endpoint gives
`T_tau(A-b)=0`, while selecting the moving low endpoint gives the same
complementary derivative equality.  The only nonsmooth events are the
clipping boundary and equality of the two endpoint values.  For the
singleton, an interior minimizing critical point must lie at or above
`A/2`, because all lower critical points are strict maxima.

The outer derivative table follows term by term from

\[
 \partial_\tau F_\tau(w)
 =\sum_{q\ge1}qK'(q\tau+w)
\]

and the envelope theorem.  The shift `b+delta` has velocity one; at the
moving active endpoint `b=B_delta`, the two shifts are `tau/3` and
`2tau/3`, with velocities `1/3` and `2/3`; the singleton endpoint
`tau/2` has velocity `1/2`.  These are exactly the coefficients in the
source's equations (6.8)--(6.12).

## 7. Scope

The source does not estimate the signs of

\[
 \mathfrak G_{XY}(\delta)
 \quad\hbox{or}\quad
 \mathfrak G_Z(\delta).
\]

It therefore proves a strict dimensional and KKT reduction, not complete
positivity.  It makes no claim about the `h=3` or `h=5` branches, complete
grid-six positivity, the all-grid Bellman inequality, or an OR-word upper
bound.
