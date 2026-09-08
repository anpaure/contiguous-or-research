# Six-slot chamber II: the stationary strip is redundant

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical reduction.  It proves that the
stationary two-compact strip is not an independent chamber-II obstruction:
after the repeated-gap and threshold faces are inserted, the whole chamber
follows from the single long-wrap boundary

\[
 \mathcal P_-(P,a)=\mathcal L_3(P;a,2a)>0.
\]

It also reduces that remaining two-variable boundary to at most one
one-dimensional stationary branch.  It does **not** sign that last branch,
and therefore does not by itself close chamber II, chamber I, complete
six-slot positivity, or an OR-word upper bound.

Put

\[
 A={\sqrt\pi\over2},\qquad
 F_P(w)=\sum_{q\ge0}K(qP+w),\qquad C(P)=F_P(0),
\tag{0.1}
\]

and

\[
 \mathcal L_3(P;a,b)=C(P)+F_P(a)+F_P(b).
\tag{0.2}
\]

The closed chamber-II polygon at fixed period is

\[
\boxed{
 \mathscr D_P=\{(a,b):a\ge0,\ b\ge2a,\ 2b\le P+a,
                              \ b\le A-P\},
 \qquad {A\over2}\le P<A .}
\tag{0.3}
\]

The literal chamber has the last inequality strict.  Passing to the
closure is proof-safe because every train is continuous and the threshold
face is already known positive.

## 1. Strict convexity of the train derivative

Write

\[
 h(x)=xe^{-\pi x^2/4},\qquad \rho={P\over A},
 \qquad x={w\over A}.
\tag{1.1}
\]

For

\[
 {1\over2}\le\rho<1,
 \qquad0\le x\le1-\rho,
\tag{1.2}
\]

the rows `q=0,1` are compact and all later rows are Gaussian tails.  The
exact derivative is

\[
 {F_P'(Ax)\over2A}=T_\rho(x),
\tag{1.3}
\]

where

\[
 \boxed{
 T_\rho(x)=\sum_{q\ge0}h(1+x+q\rho)
              -h(1-x)-h(1-\rho-x).}
\tag{1.4}
\]

Termwise differentiation is justified uniformly on the compact parameter
domain by a Gaussian summable majorant.

### Lemma 1.1 (reflected second-derivative order)

For every `0<=x<=1/2`,

\[
                         h''(1+x)\ge h''(1-x),
\tag{1.5}
\]

with strict inequality for `x>0`.

#### Proof

The exact derivatives are

\[
 h''(z)={\pi\over2}z\left({\pi z^2\over2}-3\right)
           e^{-\pi z^2/4}
\tag{1.6}
\]

and

\[
 h'''(z)={\pi\over2}e^{-\pi z^2/4}
 \left(-4\eta^2+12\eta-3\right),
 \qquad \eta={\pi z^2\over4}.
\tag{1.7}
\]

The roots of the quadratic in (1.7) are

\[
 \eta_-={3-\sqrt6\over2},\qquad
 \eta_+={3+\sqrt6\over2}.
\]

If `0<=x<=2/5`, the interval `[1-x,1+x]` is contained in
`[3/5,7/5]`.  On this latter interval,

\[
 {\pi(3/5)^2\over4}={9\pi\over100}>{7\over25}>\eta_-,
\]

because `pi>157/50` and `sqrt(6)>61/25`, while

\[
 {\pi(7/5)^2\over4}={49\pi\over100}
 <{539\over350}< {5\over2}<\eta_+.
\]

Thus `h'''>0` throughout `[1-x,1+x]`, proving (1.5) on this
subinterval.

If `2/5<=x<=1/2`, then `1+x>=7/5` and `1-x<=3/5`.  The bounds
`pi>157/50` and `pi<22/7` give

\[
 \pi(7/5)^2>6,
 \qquad \pi(3/5)^2<6.
\]

Equation (1.6) therefore gives

\[
 h''(1+x)>0>h''(1-x).
\]

This proves the lemma. \(\square\)

### Theorem 1.2 (strict derivative convexity)

On (1.2),

\[
                         \boxed{T_\rho''(x)>0.}
\tag{1.8}
\]

Equivalently, `w -> F_P'(w)` is strictly convex on `[0,A-P]`.

#### Proof

Differentiating (1.4) twice gives

\[
\begin{aligned}
 T_\rho''(x)={}&h''(1+x)-h''(1-x)\\
 &+\sum_{q\ge1}h''(1+x+q\rho)
   -h''(1-\rho-x).
\end{aligned}
\tag{1.9}
\]

The first line is nonnegative by Lemma 1.1.  Every summand in the sum is
strictly positive: its argument is at least `1+rho>=3/2`, and
`3/2>sqrt(6/pi)`.  Finally,

\[
 0\le1-\rho-x\le{1\over2}<\sqrt{6/\pi},
\]

so the last displayed term is nonnegative.  The infinite sum already
contains a strictly positive first term, proving (1.8). \(\square\)

### Corollary 1.3

For fixed `P`, the function `F_P` has at most one interior local minimum
on `[0,A-P]`.

#### Proof

Put `T=F_P'`.  By Theorem 1.2, `T` is strictly convex.  If
`u<v` were two zeros of `T` at which `T'>=0`, strict convexity would give

\[
 T(v)>T(u)+T'(u)(v-u)\ge0,
\]

a contradiction.  Every differentiable interior local minimum of `F_P`
supplies exactly such a zero. \(\square\)

## 2. Elimination of the chamber-II stationary strip

### Lemma 2.1 (the zero-left boundary is positive)

For every \((0,b)\in\mathscr D_P\),

\[
                         2C(P)+F_P(b)>0.
\tag{2.1}
\]

#### Proof

The chamber inequality gives `2b<=P`.  Consider the four-slot table

\[
                         (0,b,P,P+b,2P).
\tag{2.2}
\]

It is nondecreasing and internally superadditive: the only nontrivial
inequality is `P+2b<=2P`.  Its endpoint obeys `2P>=A`.  Its Bellman clock
is

\[
 V_{2q}=qP,\qquad V_{2q+1}=qP+b,
\]

and therefore its Bellman functional is

\[
                         C(P)+F_P(b)>0
\]

by complete four-slot positivity.  Arithmetic-ceiling positivity gives
`C(P)>0`; adding the two inequalities proves (2.1). \(\square\)

### Theorem 2.2 (chamber II has only the long-wrap obstruction)

If a fixed-period chamber-II fibre contains a nonpositive point, its
minimum on the closed fibre is attained on

\[
                         \boxed{b=2a.}
\tag{2.3}
\]

Consequently, positivity of the single family

\[
 \boxed{
 \mathcal P_-(P,a):=\mathcal L_3(P;a,2a)>0}
\tag{2.4}
\]

on

\[
 {A\over2}\le P<A,\qquad
 0\le a\le {P\over3},\qquad P+2a\le A
\tag{2.5}
\]

proves all of chamber II positive.  In particular the stationary strip
from the earlier fixed-`a` reduction contributes no independent gate.

#### Proof

Fix `P` and minimize (0.2) on the compact polygon \(\mathscr D_P\).
Every boundary face except `b=2a` is positive:

* `a=0` is Lemma 2.1;
* `2b=P+a` is the now-proved prethreshold repeated-gap gate;
* `b=A-P` is the already-proved threshold upper endpoint.

If a nonpositive minimum were interior in the `(a,b)` fibre, then

\[
 F_P'(a)=F_P'(b)=0,
 \qquad F_P''(a)\ge0,\quad F_P''(b)\ge0.
\tag{2.6}
\]

But interior chamber II has `0<a<b`.  Thus (2.6) gives two distinct
interior local-minimum zeros of `F_P'`, contradicting Corollary 1.3.
It follows that every nonpositive fibre minimum lies on `b=2a`.
Therefore (2.4) implies positivity of the whole chamber. \(\square\)

The theorem is stronger than merely signing the old critical fibre.  It
shows that no value or curvature estimate on that fibre is needed once
the four literal boundary faces are priced.

## 3. The surviving long-wrap gate is one stationary curve

For fixed `P`, put

\[
 Q_P(a)=\mathcal L_3(P;a,2a),
 \qquad
 0\le a\le m(P):=\min\left\{{P\over3},{A-P\over2}\right\}.
\tag{3.1}
\]

### Lemma 3.1

The derivative `a -> Q_P'(a)` is strictly convex.  Consequently `Q_P`
has at most one interior local minimum.

#### Proof

One has

\[
 Q_P'(a)=F_P'(a)+2F_P'(2a).
\tag{3.2}
\]

Theorem 1.2 is equivalent to `F_P'''(w)>0` on the relevant interval.
Differentiating (3.2) twice gives

\[
 {d^2\over da^2}Q_P'(a)
 =F_P'''(a)+8F_P'''(2a)>0.
\tag{3.3}
\]

The final assertion follows by the same strict-convex-zero argument as
Corollary 1.3. \(\square\)

All endpoint minima are already positive:

\[
 Q_P(0)=3C(P)>0;
\tag{3.4}
\]

if `P<=3A/5`, then `m(P)=P/3` and

\[
 Q_P(P/3)=C(P/3)>0;
\tag{3.5}
\]

while if `P>=3A/5`, then `m(P)=(A-P)/2` and the last compact value is
`P+2m(P)=A`, so threshold-face positivity applies.

At the half-period boundary `P=A/2`, the new two-compact monotonicity
theorem gives

\[
 F_{A/2}'(w)<0\qquad(0\le w\le A/3).
\]

Thus `Q_(A/2)` decreases on `[0,A/6]`, and

\[
 \min Q_{A/2}=Q_{A/2}(A/6)=C(A/6)>0.
\tag{3.6}
\]

### Corollary 3.2 (smallest remaining chamber-II scalar gate)

Every nonpositive value of the long-wrap family forces a point on the
single stationary branch

\[
\boxed{
\begin{gathered}
 {A\over2}<P<A,\qquad0<a<m(P),\\
 F_P'(a)+2F_P'(2a)=0,\\
 F_P''(a)+4F_P''(2a)\ge0.
\end{gathered}}
\tag{3.7}
\]

For each fixed `P`, there is at most one `a` satisfying (3.7).  Therefore
(3.7) is an honest one-dimensional residual curve, not a two-dimensional
gate.  Positivity of `Q_P` on this curve proves (2.4), and Theorem 2.2
then closes all of chamber II.  The same long-wrap gate is the pure
endpoint exit in chamber I.

There is a sharper necessary system for an actual chamber-II
counterexample.  All outer boundaries of the `(P,a)` long-wrap domain are
already positive: `a=0`, `P=A/2`, `P=3a`, and `P+2a=A`.  Hence a
nonpositive chamber-II global minimum must satisfy the strict inequalities

\[
 P>{A\over2},\qquad P>3a,\qquad P+2a<A,
\tag{3.8}
\]

and the Karush--Kuhn--Tucker conditions on `b=2a` give

\[
\boxed{
\begin{aligned}
 F_P'(2a)&\ge0,\\
 F_P'(a)+2F_P'(2a)&=0,\\
 \sum_{q\ge1}q\{K'(qP)+K'(qP+a)+K'(qP+2a)\}&=0.
\end{aligned}}
\tag{3.9}
\]

Thus necessarily

\[
                         F_P'(a)\le0\le F_P'(2a).
\tag{3.10}
\]

The first line in (3.9) is the inward derivative in the feasible
direction which increases `b`; the second is the derivative tangent to
the face `b=2a`; and the third is the period derivative.  No endpoint or
stationary-strip case is hidden in this system.

## 4. Frozen dependencies and exact scope

| role | file | SHA-256 |
|---|---|---|
| chamber-II critical-strip reduction and threshold face | `MATH_THEOREM_SIX_SLOT_THREE_EFFICIENT_CHAMBER_II_PRETHRESHOLD_CRITICAL_STRIP_REDUCTION_20260804.md` | `8101f952bdfc4900f2fdd9d4b6396642c694c850cb420c7ef8dc03e24f19c1f3` |
| prethreshold repeated-gap closure and half-period monotonicity | `MATH_THEOREM_HALF_PERIOD_TWO_COMPACT_TRAIN_AND_PRETHRESHOLD_REPEATED_GAP_CLOSURE_20260804.md` | `c35a9db78b5dc317fa319dd150c3abe0521b3043b9dc22d7066b2d14ae2afd4a` |
| complete four-slot positivity | `MATH_THEOREM_FOUR_SLOT_BELLMAN_COMPLETE_POSITIVITY_20260804.md` | `1624cff37c4f6b45edd16234e054d43c99ceb722d7dac4b57d058a40465b68b9` |
| strict arithmetic-ceiling positivity | `MATH_THEOREM_SMOOTH_BINOMIAL_CONFIGURATION_DUAL_AND_CEILING_PRICE_CLASSES_20260804.md` | `c3a2c1858f59fa32e61d2f9a9252085ad7fb01f3521ab5cb46998705123e103d` |

This note proves a reduction, not the remaining sign.  It makes no claim
about the stationary long-wrap curve (3.7), chamber-I retained pulses,
the other six-slot efficiency branches, arbitrary-grid Bellman
positivity, integral carrier construction, or `nu(k)<=B(k)+O(1)`.
