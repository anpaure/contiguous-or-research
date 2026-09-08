# The second Rayleigh rearrangement still has one sign crossing

**Date:** 2026-08-05  
**Method:** pure analysis; no search or solver  
**Status:** unconditional.  This proves the exact shape requested by the
rearrangement-orbit programme for the second iterate only.  It does not
assert the same shape for every later iterate.

## 1. Setup

Let

\[
 A={\sqrt\pi\over2},
 \qquad
 K(t)=
 \begin{cases}
  1-e^{-(A-t)^2}-e^{-(A+t)^2},&0\le t\le A,\\
  -e^{-(A+t)^2},&t>A.
 \end{cases}
\]

Let `b` and `c` be the zero and minimum of `K`.  If `m=K(c)` and
`z(v)=r(v)-ell(v)` is the distance between the two points of level `v`,
write `u=z^{-1}`.  The first rearranged kernel is

\[
 H(t):=(\mathcal RK)(t)=
 \begin{cases}
  K(t)+u(t),&0\le t<b,\\
  u(t),&t\ge b.
 \end{cases}                                      \tag{1.1}
\]

The one-well theorem gives a unique zero `a in (0,b)`, strict decrease on
`(0,b)`, strict increase on `(b,infinity)`, and minimum

\[
 H(b)=u(b)=-q<0.                                  \tag{1.2}
\]

For `0<s<q`, let

\[
 L(s)\in(a,b),\qquad R(s)>b,
 \qquad H(L(s))=H(R(s))=-s,
\]

and put

\[
 Z(s)=R(s)-L(s).
\]

Then `Z` decreases strictly from infinity to zero.  If

\[
 C(t)=Z^{-1}(t),                                  \tag{1.3}
\]

where the inverse is taken in the decreasing sense, the negative-component
rearrangement profile of `H` is exactly `C`.  Thus

\[
 (\mathcal R^2K)(t)=H_+(t)-C(t).                 \tag{1.4}
\]

We prove that the right side has exactly one zero.

## 2. The exact inverse-branch derivative

Put

\[
 g(x)=-H'(x)>0\quad(a<x<b),
 \qquad
 f(x)=H'(x)=u'(x)>0\quad(x>b).
\]

Differentiating the two level equations gives

\[
 L'(s)={1\over g(L(s))},
 \qquad
 R'(s)=-{1\over f(R(s))}.
\]

Consequently

\[
 Z'(s)=-\left({1\over g(L(s))}+{1\over f(R(s))}\right),
\]

and inverse differentiation in (1.3) gives

\[
 \boxed{
 -C'(t)=
 {g(L(C(t)))f(R(C(t)))
  \over g(L(C(t)))+f(R(C(t)))}.}                 \tag{2.1}
\]

In particular,

\[
 0<-C'(t)<f(R(C(t))).                             \tag{2.2}
\]

The previously proved residual-job theorem says that `u'=f` is strictly
decreasing on `(b,infinity)`.  Since `R(C(t))>b`, (2.2) yields the uniform
bound

\[
 \boxed{-C'(t)<u'(b)\qquad(t>0).}                \tag{2.3}
\]

This is the key simplification: no detailed analysis of the second pair of
inverse branches is needed.

## 3. Rational Gaussian certificate

The following elementary bounds will be used:

\[
\begin{array}{rclcrcl}
 b&>&469/1000,&& e:=\ell(u(b))&>&113/200,\\
 K(9/50)&>&71/1000,&&-K'(9/50)&>&17/100,\\
 K(69/100)&>&-23/500,&&K(87/100)&>&-23/500,\\
 K(57/100)&>&-1/40,&&K(207/200)&>&-1/40,\\
 K(9/25)&<&31/1000,&&K(121/200)&<&-4/125,\\
 K(121/125)&<&-4/125,&&-K'(113/200)&<&23/100.
\end{array}                                      \tag{3.1}
\]

Moreover,

\[
 K''(t)<0\quad(0\le t\le9/25),                 \tag{3.2}
\]

and on the increasing branch after the minimum,

\[
 0<K'(x)<4/25.                                   \tag{3.3}
\]

For completeness, all bounds in (3.1)--(3.3) are finite rational
Gaussian checks.  One may use

\[
 {4431\over5000}<A<{8863\over10000}
\]

and, for rational `0<=x<=4`,

\[
 \sum_{j=0}^{20}{x^j\over j!}
 <e^x<
 \sum_{j=0}^{20}{x^j\over j!}
 +{x^{21}\over21!}\,{1\over1-x/22}.             \tag{3.4}
\]

Substitution in `K`, `K'`, and `K''` gives (3.1), with strict slack in
every row.  To see (3.2) without a grid, write

\[
 Q'(x)=2(1-2x^2)e^{-x^2},
 \qquad K''(t)=Q'(A-t)+Q'(A+t).
\]

On the relevant interval `K'''(t)=-Q''(A-t)+Q''(A+t)>0`: the function

\[
 -Q''(x)=4x(3-2x^2)e^{-x^2}
\]

is decreasing after `x= A-9/25`, up to its zero at `sqrt(3/2)`, and the
case beyond that zero is immediate.  Hence `K''` is increasing there;
the endpoint substitution gives `K''(9/25)<-1/5`.  This proves (3.2).
Finally `K'` increases from zero to `K'(A)=4Ae^{-pi}` on `(c,A)` and is
`2(A+x)e^{-(A+x)^2}` and decreasing after `A`; (3.3) follows from
`4Ae^{-pi}<4/25`.

The first line of (3.1), including the stronger previously authenticated
bound `e>0.565`, is also contained in the first-residual density theorem.

## 4. Three consequences of the certificate

Set

\[
 T={9\over50}.
\]

### 4.1 The positive branch stays above the negative depth through `T`

At level `-23/500`, the two original inverse branches lie strictly between
`69/100` and `87/100` by (3.1).  Therefore

\[
 z(-23/500)<18/100=T,
\]

and monotonicity of `z` gives

\[
 u(T)>-23/500.                                   \tag{4.1}
\]

At level `-1/40`, (3.1) puts the branches strictly between `57/100` and
`207/200`.  Hence

\[
 z(-1/40)<465/1000<b=z(u(b)),
\]

so

\[
 q=-u(b)<1/40.                                   \tag{4.2}
\]

Equations (3.1), (4.1), and (4.2) now give

\[
 \boxed{H(T)=K(T)+u(T)>71/1000-46/1000=1/40>q.} \tag{4.3}
\]

### 4.2 The first positive endpoint is before `9/25`

At level `-4/125`, (3.1) gives

\[
 \ell(-4/125)<121/200,
 \qquad
 r(-4/125)>121/125.
\]

Thus

\[
 z(-4/125)>121/125-121/200>9/25,
\]

so `u(9/25)<-4/125`.  With (3.1),

\[
 H(9/25)<31/1000-32/1000<0.
\]

Since `H` decreases on `(0,b)`, its zero obeys

\[
 \boxed{a<9/25.}                                 \tag{4.4}
\]

### 4.3 The socket slope dominates every second-stage right slope

For `0<t<b`, the original equal-level endpoints lie beyond the endpoints
belonging to `t=b` toward the minimum.  Hence the left slope is below
`23/100` by `e>113/200` and (3.1); the right slope is below `4/25` by
(3.3).  The parallel-slope formula and arithmetic--geometric mean give

\[
 u'(t)={\alpha\beta\over\alpha+\beta}
 \le{\alpha+\beta\over4}
 <{1\over4}\left({4\over25}+{23\over100}\right)
 ={39\over400}.                                  \tag{4.5}
\]

At `t=b`, the sharper authenticated right-slope estimate is
`alpha<1/10`.  Therefore

\[
 u'(b)<{(1/10)(23/100)\over1/10+23/100}
 ={23\over330}<{7\over100}.                     \tag{4.6}
\]

By (3.2), `-K'` is increasing through `[T,a]`.  Equations (3.1), (4.4),
and (4.5) consequently imply

\[
\begin{aligned}
 g(t)&=-H'(t)=-K'(t)-u'(t)\\
 &>{17\over100}-{39\over400}
 ={29\over400}>{7\over100}>u'(b)
 \qquad(T\le t\le a).                           \tag{4.7}
\end{aligned}
\]

## 5. One-crossing theorem

### Theorem 5.1

There is a unique `a_2 in (T,a)` such that

\[
 \boxed{
 (\mathcal R^2K)(t)>0\ (0\le t<a_2),
 \qquad
 (\mathcal R^2K)(t)<0\ (t>a_2).}                \tag{5.1}
\]

In addition, `\mathcal R^2K` is strictly decreasing on `[T,a]`.

### Proof

The profile `C` is nonincreasing and `C(0)=q`.  Since `H` is decreasing
on `[0,a]`, (4.3) gives, for `0<=t<=T`,

\[
 H(t)-C(t)\ge H(T)-q>0.                           \tag{5.2}
\]

For `T<=t<=a`, equations (1.4), (2.3), and (4.7) give

\[
 (\mathcal R^2K)'(t)
 =H'(t)-C'(t)
 =-g(t)+[-C'(t)]<0.                              \tag{5.3}
\]

At the right endpoint,

\[
 (\mathcal R^2K)(a)=-C(a)<0.
\]

Together with (5.2), strict decrease and continuity give one and only one
zero in `(T,a)`.  For `t>a`, equation (1.4) is simply
`(\mathcal R^2K)(t)=-C(t)<0`.  This proves (5.1). `square`

## 6. Exact consequence and remaining gap

The first two rearranged Rayleigh kernels both have positive-prefix,
negative-tail sign order.  Therefore neither can be a nonzero
sign-reversed fixed point of `\mathcal R`.

This is genuine progress toward the deterministic orbit lemma, but it is
not an induction.  Rectangular examples show that arbitrarily many
positive-prefix/negative-tail iterates can still end at a nonzero
sign-reversed fixed point.  To prove the full Rayleigh inequality one still
needs an all-iterate invariant, for example nonpositivity of every signed
first moment, or a differential cone that propagates the slope domination
used in (4.7).

## 7. Dependencies

1. `MATH_THEOREM_ANCHORED_NEGATIVE_COMPONENT_REARRANGEMENT_OPERATOR_20260805.md`.
2. `MATH_THEOREM_RAYLEIGH_EQUAL_LEVEL_ONE_WELL_REGENERATION_20260805.md`.
3. `MATH_THEOREM_RAYLEIGH_FIRST_RESIDUAL_JOB_DENSITY_DECREASE_20260805.md`.
4. `MATH_THEOREM_RAYLEIGH_FIRST_TRANSFORM_EXACT_TWO_THREE_COUNT_WINDOW_20260805.md`.
