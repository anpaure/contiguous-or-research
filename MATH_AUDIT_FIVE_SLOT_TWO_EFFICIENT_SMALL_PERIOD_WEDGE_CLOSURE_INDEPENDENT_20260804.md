# Independent audit: five-slot two-efficient small-period wedge

**Date:** 2026-08-04  
**Audited theorem:**
`MATH_THEOREM_FIVE_SLOT_TWO_EFFICIENT_SMALL_PERIOD_WEDGE_CLOSURE_20260804.md`  
**Method:** independent differentiation, interval geometry, and exact
rational Taylor bounds.  No search or floating-point sign test is used.  
**Verdict:** **PASS**.

## 1. Normalized domain

The five-slot two-efficient normal form has shift `s=T-2y` and satisfies

\[
 x\le z-y\le s\le y/2,
 \qquad c_4=2y.
\]

On the first-crossing face, `2y<A<=2y+s`.  Therefore

\[
 2A/5\le y<A/2,
 \qquad A-2y\le s\le y/2.
\]

After `y=At`, `s=Au`, this is exactly

\[
 2/5\le t\le1/2,
 \qquad1-2t\le u\le t/2.
\]

No part of the new wedge lies in the old `t>=1/2` proof except its boundary,
so a new argument is genuinely required.

## 2. Derivative identity

In this wedge, `u<1`, `t+u<1`, and `2t+u>=1`.  Thus precisely the first
two shifted terms use both compact Gaussian shores.  Differentiating them
and all later tail terms gives

\[
 {d\over du}F_{At}(Au)=-2A^2W_t(u),
\]

with

\[
 W_t(u)=h(1-u)+h(1-t-u)-\sum_{q\ge0}h(1+u+qt).
\]

The formula remains valid at `2t+u=1` because the two definitions of `K`
have the same derivative at `A`.

## 3. Integral-tail direction

With `x=1+t+u>=3/2`, the function `h` is decreasing.  For every `n>=2`,

\[
 h(x+nt)\le {1\over t}
 \int_{x+(n-1)t}^{x+nt}h(v)\,dv.
\]

Summing gives

\[
 \sum_{n\ge0}h(x+nt)
 \le h(x)+h(x+t)+{e^{-a(x+t)^2}\over2at}.
\]

Therefore the theorem's inequality `W>=H` has the correct direction.

## 4. Concavity audit

Throughout the wedge,

\[
 3/4\le1-u\le1+u\le5/4,
 \qquad1/4\le1-t-u\le1/2,
\]

and

\[
 1+t+u\ge3/2,
 \qquad1+2t+u\ge2.
\]

On `[3/4,5/4]`, `h'''` is positive, so `h''` is increasing.  On the
second interval `h''<0`, and on the last two intervals `h''>0`.  The
Gaussian remainder has positive second derivative.  Every term in
`H''` is consequently nonpositive and at least one is strictly negative.
Thus `H''<0`, and checking the two shift endpoints is sufficient.

## 5. Lower-edge audit

At `u=1-2t`, direct substitution gives

\[
 L(t)=h(2t)-h(2-2t)+h(t)-h(2-t)-h(2)
      -{e^{-\pi}\over2at}.
\]

Differentiation gives the five terms recorded in the theorem.  The
monotonicity bounds

\[
 h'(2t)\le0,
 \quad h'(2-2t)\le h'(1),
 \quad h'(t)\le h'(2/5),
 \quad h'(2-t)\le h'(8/5)
\]

all have the asserted directions.  Applying the rational Taylor bounds
reduces their sum to `D_L<-1/20`; hence `L` decreases.  Its minimum is

\[
 L(1/2)
 ={1\over2}e^{-\pi/16}-{3\over2}e^{-9\pi/16}
  -\left(2+{4\over\pi}\right)e^{-\pi}.
\]

The rational lower certificate `B_L>1/100` is termwise in the correct
direction: `Q_9` is used only on positive terms and `1/P_8` only on
subtracted terms.

## 6. Upper-edge audit

The decomposition `R=D_1+D_3-tail` is algebraically exact.  The derivative
tests reduce to

\[
 h'(3/4)+h'(6/5)<0,
 \qquad h'(2/5)+h'(8/5)>0.
\]

The theorem proves the stronger rational bounds `-1/4` and `1/5`.
Therefore `D_1` increases while `D_3` decreases, giving

\[
 D_1(t)\ge D_1(2/5),
 \qquad D_3(t)\ge D_3(1/2).
\]

The remaining negative arguments are minimized at `2`, and the Gaussian
remainder is at most `(5/pi)e^(-pi)`.  This produces exactly `B_R`, whose
rational expansion is greater than `1/100`.

## 7. Lattice and transient closure

Both endpoint bounds are strict, so concavity gives `H>0`, hence `W>0`.
Thus `F_(At)(Au)` decreases with `u`, and

\[
 \mathcal L_2(At;Au)
 \ge C(At)+F_{At}(At/2)=C(At/2)>0.
\]

For the original five-slot clock, both finite corrections are
nonnegative.  The inequalities

\[
 x\le s,
 \qquad z\le y+s<3A/4
\]

place them inside the decreasing interval of `K`.  Earlier threshold
crossings reduce to the independently proved `n<=4` theorem.

**Final verdict: PASS.**  Every five-slot table whose size-two generator
has maximal efficiency has strictly positive Bellman functional.  The
remaining five-slot branches are `h=3,4,5`; no all-slot conclusion is made.
