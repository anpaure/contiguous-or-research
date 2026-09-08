# Independent audit: six-slot `h=4` redundant-endpoint scalar/KKT reduction

**Date:** 2026-08-04

**Audited theorem:**
`MATH_THEOREM_SIX_SLOT_H4_REDUNDANT_ENDPOINT_THREE_BLOCK_SCALAR_KKT_REDUCTION_20260804.md`

**Audited theorem SHA-256:**
`f410d86f5d544755c08f269ece1d47910f2d3c055be91c7a391bb548090f53d3`

**Method:** fresh derivation from the canonical Bellman table and the two
branches of the Rayleigh kernel.  No theorem text was reused as a proof,
and no search, sampling, solver, or floating-point inequality is used.

## 1. Verdict

**GO without source correction.**  Endpoint redundancy, the parameter
change, the literal endpoint train, all three envelope directions, the
half-period identity, and every smooth KKT coefficient check exactly.  The
result is a sufficient scalar reduction, not a positivity proof; the source
states this scope correctly.

## 2. Reconstruct the three redundant endpoints

Start with

\[
 (c_0,\ldots,c_6)=(0,x,y,z,P,P+u,P+v).
\]

The inert endpoint equalities give respectively

\[
\begin{array}{c|c|c}
\text{face}&\text{endpoint equality}&\text{lower realization}\\ \hline
X&v=x+u&c_6=x+(P+u)=c_1+c_5,\\
Y&v=y&c_6=y+P=c_2+c_4,\\
Z&v=2z-P&c_6=2z=2c_3.
\end{array}
\tag{2.1}
\]

Replacing a size-six part by its row in (2.1) preserves total capacity and
total value.  Replacing every such part proves that the configuration set
using sizes at most six has the same value projection as the configuration
set using sizes at most five.  Thus the Bellman clocks agree at every
capacity.  This is an equality statement, not merely deletion monotonicity.

The retained size-five value is `P+u<A`; consequently this observation does
not place the table inside the already-proved threshold-crossing five-slot
theorem.  It identifies a delayed-crossing prefix.

## 3. Parameter transformation and exact domain

Define independently

\[
 p=A-P,
 \qquad a=p-u,
 \qquad\delta=v-p,
 \qquad\tau=P+v.
\tag{3.1}
\]

Then

\[
                         \tau=A+\delta.
\tag{3.2}
\]

Since `2A/3<=P<A`,

\[
                         0<p\le A/3.
\]

Since `0<=u<p`,

\[
                         0<a\le p.
\]

On an inert face `v>p`, so `delta>0`.  Maximum efficiency gives
`v<=P/2`, hence

\[
 \tau=P+v\le3P/2<3A/2,
 \qquad0<\delta<A/2.
\tag{3.3}
\]

Subtracting `p` from endpoint saturation gives

\[
\begin{aligned}
(x+u)-p&=x-a,\\
y-p&=y-p,\\
(2z-P)-p&=2z-A.
\end{aligned}
\]

Therefore

\[
 \boxed{\delta=\max\{x-a,y-p,2z-A\}.}
\tag{3.4}
\]

It follows in the required directions that

\[
 x\le a+\delta,
 \qquad y\le p+\delta,
 \qquad2z\le A+\delta=\tau,
\tag{3.5}
\]

and one of these is tight.  Finally, `x<=u<p<=A/3` and
`y<=P/2<A/2` put both low members of the reflected pairs inside the half
band required later.

## 4. Literal endpoint-period comparison

For `q>=0` and `0<=r<=5`, use `q` endpoint configurations and one
size-`r` generator.  This supplies value

\[
                         q\tau+c_r
\]

at capacity `6q+r`.  When `q=0`, internal superadditivity gives
`V_r=c_r`.  When `q>=1`,

\[
                         V_{6q+r}\ge q\tau+c_r\ge A.
\]

On `[A,infinity)`,

\[
                         K'(w)=2(A+w)e^{-(A+w)^2}>0.
\]

Thus

\[
 K(V_{6q+r})\ge K(q\tau+c_r).
\]

Absolute Gaussian convergence permits summation over all residue classes,
giving

\[
\begin{aligned}
\Phi\ge{}&C(\tau)
+F_\tau(x)+F_\tau(P+u)\\
&+F_\tau(y)+F_\tau(P)+F_\tau(z).
\end{aligned}
\tag{4.1}
\]

Since `P+u=A-a` and `P=A-p`, this is exactly the ceiling, the two
reflected pairs `(x,A-a)` and `(y,A-p)`, and the singleton `z` used by the
source.  No Apéry-head correction is silently discarded.

## 5. Re-prove the period-uniform critical-point lemma

For `tau>=A` and `0<=w<=A/2`, expand the compact `q=0` term and all
positive-period tails:

\[
 F_\tau(w)
 =1-e^{-(A-w)^2}
 -\sum_{q\ge0}e^{-(A+w+q\tau)^2}.
\tag{5.1}
\]

Let

\[
 \phi(t)=te^{-t^2},
 \qquad
 \lambda(t)={\phi'(t)\over\phi(t)}={1\over t}-2t.
\]

The function `lambda` strictly decreases on the positive axis.  At an
interior critical point of (5.1),

\[
 \sum_{q\ge0}\phi(A+w+q\tau)=\phi(A-w).
\tag{5.2}
\]

Therefore

\[
\begin{aligned}
{1\over2}F_\tau''(w)
&=\sum_{q\ge0}\phi'(A+w+q\tau)+\phi'(A-w)\\
&\le\{\lambda(A+w)+\lambda(A-w)\}\phi(A-w)\\
&=2A\left({1\over A^2-w^2}-2\right)\phi(A-w).
\end{aligned}
\tag{5.3}
\]

The coefficient is negative because

\[
 A^2-w^2\ge{3A^2\over4}={3\pi\over16}>{1\over2}.
\]

Thus every interior critical point is a strict local maximum.  An interior
global minimum would be critical by Fermat's theorem, so every closed
subinterval of `[0,A/2]` attains its minimum at an endpoint.  This proves
the source's Lemma 3.1 for every period in its stated range.

## 6. Audit the three envelopes and both gate directions

### 6.1 Inactive pair

For either physical pair, write the high member as `A-b`; then
`b` is `a` or `p`, so

\[
                         0\le b\le A/3.
\]

Its low member `r` satisfies

\[
 0\le r\le\min\{A/2,b+\delta\}=m_\delta(b).
\]

The critical-point lemma gives

\[
 F_\tau(r)
 \ge\min\{F_\tau(0),F_\tau(m_\delta(b))\}.
\]

After adding `F_tau(A-b)` and minimizing over the enlarged base interval,
the physical pair is bounded **below** by `mathcal I(delta)`.  Enlarging the
domain can only decrease the minimum, so the source's direction is safe.

### 6.2 Active pair and ceiling

On `X`, the low member is `ell=x=a+delta`.  Since `x<=P/4`,
`3ell<=P<=tau`.  On `Y`, `ell=y=p+delta` and `2y<=P`, so
`3ell<=P+y=tau`.  Hence in either case

\[
 b=\ell-\delta\le{A-2\delta\over3}=B_\delta.
\]

The physical ceiling-plus-active-pair value is therefore at least the
minimum `mathcal H(delta)` on the stated interval.  This step is exact
apart from the harmless enlargement of the base interval; it incurs no
reflection estimate.

### 6.3 Singleton and allocation

Equation (3.5) gives `0<=z<=tau/2`, hence

\[
                         F_\tau(z)\ge\mathcal S(\delta).
\]

On `X` or `Y`, allocate the one ceiling to the active pair, the other pair
to `mathcal I`, and the singleton to `mathcal S`.  This yields

\[
                         \Phi\ge\mathfrak G_{XY}(\delta).
\]

On `Z`, `2z=tau`, and both reflected pairs still satisfy the inactive-pair
bound.  Separating even and odd multiples gives

\[
\begin{aligned}
C(\tau)+F_\tau(\tau/2)
&=\sum_{q\ge0}K(2q\,\tau/2)
 +\sum_{q\ge0}K((2q+1)\tau/2)\\
&=C(\tau/2).
\end{aligned}
\]

Thus

\[
                         \Phi\ge\mathfrak G_Z(\delta).
\]

If the corresponding gate is positive, the physical functional is
positive.  Conversely, `Phi>=gate` and `Phi<=0` imply `gate<=0`, exactly
as the source states.

## 7. Independent KKT and velocity ledger

Define

\[
 T_\tau(w)=F_\tau'(w),
 \qquad
 R_\tau(w)=\partial_\tau F_\tau(w)
 =\sum_{q\ge1}qK'(q\tau+w).
\]

### Inner equations

For the active objective

\[
 C(\tau)+F_\tau(b+\delta)+F_\tau(A-b),
\]

the `b` derivative is

\[
                         T_\tau(b+\delta)-T_\tau(A-b).
\]

For an inactive branch with selected low endpoint `0` or `A/2`, the only
`b` derivative is `-T_tau(A-b)`.  On the moving branch it is again
`T_tau(b+delta)-T_tau(A-b)`.  The clipping point and equality of the two
low-endpoint values are exactly the two nonsmooth cases listed in the
source.  The singleton equation is `T_tau(w)=0`; Section 5 excludes any
interior minimizing solution below `A/2`.

### Outer derivatives

At an interior active-pair minimizer, the envelope theorem gives

\[
 R_\tau(0)+R_\tau(b+\delta)+T_\tau(b+\delta)
 +R_\tau(A-b),
\]

matching (6.8).  At `b=0` the same formula applies because that endpoint is
fixed.  At the moving endpoint

\[
 b=B_\delta,
 \qquad b+\delta=\tau/3,
 \qquad A-b=2\tau/3,
\]

the two shift velocities are `1/3` and `2/3`, yielding exactly (6.8a).

For `mathcal I`, a fixed low endpoint contributes only its period residual;
the moving endpoint `b+delta` contributes one additional `T_tau` term.
This reproduces every row of (6.9).  An interior singleton minimizer has
zero shift derivative and therefore contributes `R_tau(w)`; the fixed zero
endpoint contributes `R_tau(0)`, and `tau/2` contributes

\[
 R_\tau(\tau/2)+{1\over2}T_\tau(\tau/2).
\]

Finally, with `s=tau/2`, `ds/d delta=1/2`, so

\[
 {d\over d\delta}C(\tau/2)
 ={1\over2}\sum_{q\ge1}qK'(q\tau/2).
\]

No period residual, explicit shift velocity, or factor of two is missing.
At the listed nonsmooth switches the appropriate objects are one-sided
derivatives or subgradients; the theorem does not incorrectly apply a
smooth equation there.

## 8. Final scope audit

The theorem proves a dimensional reduction:

\[
 (X,Y,Z)\quad\longrightarrow\quad
 \mathfrak G_{XY}(\delta),\ \mathfrak G_Z(\delta).
\]

It does not prove either scalar positive.  It also does not claim closure
of the `h=3` or `h=5` branches, all six-slot clocks, the all-grid Bellman
inequality, or an OR-word construction.  That is the exact proof boundary
supported by the derivation above.
