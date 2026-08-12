# Rayleigh deviations: Lorenz closure and the residual interval core

**Date:** 2026-08-05  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional reduction.  The positive Rayleigh lobe Lorenz-dominates
the decreasing rearrangement of the negative lobe.  Hence every unrestricted
fractional degree/majorization cut passes.  The remaining obstruction is
genuinely the consecutive-interval constraint.  A single positive residual
renewal density would close the full all-price inequality, and its exact
Volterra equation is derived below.  Positivity of that density is not asserted.

## 1. The probabilistic identity

Let `R` have Rayleigh density

\[
        2r e^{-r^2}\,dr\qquad(r>0),
\]

and put

\[
        A=\frac{\sqrt\pi}{2}=\mathbb E R.
\]

Set

\[
        X=(A-R)_+,
        \qquad
        Y=(R-A)_+.
\]

Then, for every `x>=0`,

\[
 \Pr(X>x)=
 \begin{cases}
  1-e^{-(A-x)^2},&0\le x\le A,\\
  0,&x>A,
 \end{cases}
 \qquad
 \Pr(Y>x)=e^{-(A+x)^2}.
\]

Consequently the Rayleigh signed-tail kernel is exactly

\[
 \boxed{K(x)=\Pr(X>x)-\Pr(Y>x).}                 \tag{1.1}
\]

Thus the all-price inequality is equivalently

\[
 \boxed{\mathbb E f(X)\ge \mathbb E f(Y)}        \tag{1.2}
\]

for every nonnegative nondecreasing subadditive `f` with `f(0)=0` for
which the expectations exist.  Equality of the first moments of `X` and
`Y` is just `E(R-A)=0`, and is the identity

\[
             \int_0^\infty K(x)\,dx=0.           \tag{1.3}
\]

## 2. Positive and negative lobes

Let `b` be the unique zero of `K` and let `c>b` be its unique minimum.
Write

\[
 p(x)=K(x)_+=K(x){\bf1}_{[0,b)}(x),
 \qquad
 h(x)=K(x)_-=-K(x){\bf1}_{(b,\infty)}(x).
                                                               \tag{2.1}
\]

The function `p` is nonnegative and strictly decreasing on `[0,b]`.
The function `h` is nonnegative and unimodal, increasing on `(b,c)` and
decreasing on `(c,infinity)`.  Equation (1.3) gives

\[
             \int p=\int h=:W_0.                 \tag{2.2}
\]

Let `h^downarrow` be the decreasing rearrangement of `h` on
`[0,infinity)`.  Equivalently, if the two endpoints of the negative
superlevel interval at depth `v` are `ell(v)<r(v)`, then

\[
 h^\downarrow(t)=v
 \quad\Longleftrightarrow\quad
 r(v)-\ell(v)=t.                                 \tag{2.3}
\]

The authenticated first rearrangement theorem identifies

\[
 H_1=p-h^\downarrow                              \tag{2.4}
\]

and proves that `H_1` has exactly one sign crossing, from positive to
negative.  Of course `integral H_1=0` by equimeasurability.

## 3. Lorenz domination

### Theorem 3.1

For every `t>=0`,

\[
 \boxed{
   \int_0^t h^\downarrow(x)\,dx
   \le
   \int_0^t p(x)\,dx .
 }                                                 \tag{3.1}
\]

Equivalently, `p` majorizes `h` in the continuous Hardy--Littlewood
sense.  In particular, for every measurable set `E` of measure `t`,

\[
 \boxed{
   \int_E h(x)\,dx
   \le
   \int_0^t p(x)\,dx .
 }                                                 \tag{3.2}
\]

#### Proof

Let `a` be the unique sign crossing of `H_1`.  The primitive

\[
 D(t)=\int_0^t H_1(x)\,dx
\]

increases on `[0,a]` and decreases on `[a,infinity)`.  It starts at zero
and tends to zero by (2.2).  Therefore `D(t)>=0` for every `t`, which is
(3.1).  The Hardy--Littlewood rearrangement inequality gives

\[
 \int_Eh\le\int_0^{|E|}h^\downarrow,
\]

and (3.2) follows from (3.1). `square`

This closes every ordinary fractional degree cut.  What it does not do
is require each row of a realizing incidence matrix to be a consecutive
interval.

## 4. The prescribed interval-length measure

Put

\[
 M=p(0)=K(0)>0,
 \qquad
 \alpha(dy)=-p'(y)\,dy\quad(0<y<b).              \tag{4.1}
\]

Then `alpha` has mass `M`, and layer cake gives

\[
 \boxed{p(t)=\alpha([t,b])}.                     \tag{4.2}
\]

### Theorem 4.1 (residual interval certificate)

Suppose there is a positive measure `eta` on

\[
       \{(a,y):a\ge b,\ 0<y<b\}
\]

whose length marginal is `alpha` and whose occupation density is `h`:

\[
 (y)_\#\eta=\alpha,                              \tag{4.3}
\]

\[
 \int {\bf1}_{\{a\le x<a+y\}}\,d\eta(a,y)=h(x)
 \quad\text{for a.e. }x.                        \tag{4.4}
\]

Then

\[
 \boxed{\int K\,d\rho\ge0}                    \tag{4.5}
\]

for every anchored-window measure `rho`.  Hence every nonnegative
nondecreasing subadditive price passes the Rayleigh inequality.

#### Proof

For one interval `(a,a+y]`, anchoredness gives

\[
       \rho((a,a+y])\le\rho([0,y]).
\]

Integrate this inequality against `eta`.  By (4.4), the left side is
`integral h d rho`.  By (4.3), Tonelli, and (4.2), the right side is

\[
 \int\rho([0,y])\,d\alpha(y)
 =\int p(t)\,d\rho(t).
\]

Thus `integral h d rho<=integral p d rho`, which is (4.5). `square`

Theorem 3.1 is precisely the unrestricted fractional relaxation of this
certificate.  The interval requirement in (4.4) is extra and cannot be
dropped.

## 5. Why ordinary majorization is insufficient

The obstruction already occurs in a three-column integer example.  Let
the desired unimodal occupation profile be

\[
                   (2,1,1),                      \tag{5.1}
\]

and prescribe two rows, each of length two.  The Gale--Ryser inequalities
hold: the nonincreasing rearrangement `(2,1,1)` is majorized by the
conjugate profile `(2,2,0)`.  Nevertheless two consecutive length-two
intervals on three columns can produce only

\[
 (2,2,0),\quad(1,2,1),\quad(0,2,2),              \tag{5.2}
\]

and never (5.1).  Hence even a unimodal target plus every ordinary
degree-majorization inequality does not imply a consecutive-interval
realization.

This shows that Theorem 3.1 is a genuine relaxation closure, not a hidden
proof of Theorem 4.1.

## 6. A one-function renewal criterion

A particularly strong sufficient instance of Theorem 4.1 makes the
interval start independent of its length.  Seek a probability measure
`q` supported on `[b,infinity)` such that

\[
 \boxed{h=q*p}                                    \tag{6.1}
\]

(ordinary convolution, with `p` extended by zero).  Then

\[
 d\eta(a,y)=q(da)\,\alpha(dy)                    \tag{6.2}
\]

has length marginal `alpha`, and its occupation density is

\[
 \int q(da)\alpha([x-a,b])=(q*p)(x)=h(x).
\]

Thus (6.1) implies the full all-price inequality.

The candidate `q` is unique as a distribution.  Define the probability
density

\[
            g(y)={-p'(y)\over M}{\bf1}_{(0,b)}(y).
                                                               \tag{6.3}
\]

If `q` has a density, differentiating (6.1) gives the exact renewal
equation

\[
 \boxed{
 q(x)={h'(x)\over M}+(q*g)(x),
 \qquad x>b.
 }                                                 \tag{6.4}
\]

Equivalently, if

\[
 P(s)=\int_0^b e^{-sy}p(y)\,dy,
 \qquad
 H(s)=\int_b^\infty e^{-sx}h(x)\,dx,
\]

then

\[
 \boxed{\widehat q(s)={H(s)\over P(s)}}.         \tag{6.5}
\]

The denominator has the useful zero-free representation

\[
 P(s)={M\over s}\bigl(1-\widehat g(s)\bigr).    \tag{6.6}
\]

For `Re(s)>0`, one has `|widehat g(s)|<1`, so (6.5) has no pole in the
open right half-plane.  Positivity is nevertheless not automatic: it is
equivalent, by Bernstein's theorem, to complete monotonicity of `H/P` on
the positive real axis.

There is one unconditional initial interval.  Since `h'(x)>=0` on
`(b,c]`, iteration of (6.4) from the zero history gives

\[
 \boxed{q(x)>0\qquad(b<x\le c).}                 \tag{6.7}
\]

Hence any failure of this strong renewal certificate first occurs strictly
after the Rayleigh minimum `c`, and is governed by the finite-memory delay
balance

\[
 q(x)={-K'(x)\over M}
      +\int_0^b q(x-y){-K'(y)\over M}\,dy.       \tag{6.8}
\]

The sign of its unique solution after `c` is the exact remaining scalar
for this strong subface.  The raw Rayleigh iid-renewal no-go does not by
itself decide (6.8): (6.8) uses the residual lobe length law `alpha`, not
the original socket law.  Conversely, no positivity of (6.8) is claimed
here.

## 7. Exact frontier

The direct all-price problem now has the following strict hierarchy:

1. deviation identity (1.1): exact;
2. unrestricted Lorenz/degree majorization (3.1): exact;
3. consecutive-interval realization (4.3)--(4.4): sufficient and open;
4. the still stronger state-independent residual renewal (6.4): sufficient,
   positive through `c`, and open after `c`.

Thus a counterexample, if one exists, cannot be detected by total work,
ordinary degree Hall cuts, or Hardy--Littlewood majorization.  It must use
the physical contiguity/state-dependence of interval placement.

## 8. Dependencies

1. `MATH_THEOREM_SUBADDITIVE_PRICE_MEASURE_AND_SUPERADDITIVE_CLOCK_REDUCTION_20260804.md`;
2. `MATH_THEOREM_RAYLEIGH_EQUAL_LEVEL_ONE_WELL_REGENERATION_20260805.md`;
3. `MATH_THEOREM_ANCHORED_NEGATIVE_COMPONENT_REARRANGEMENT_OPERATOR_20260805.md`;
4. `MATH_THEOREM_RAYLEIGH_INTERVAL_FLOW_DUAL_CLOSEDNESS_AND_RENEWAL_OBSTRUCTION_20260804.md`.
