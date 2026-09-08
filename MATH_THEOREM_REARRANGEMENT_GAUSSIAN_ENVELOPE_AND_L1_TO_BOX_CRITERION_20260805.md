# Rearrangement orbit: Gaussian-envelope propagation and an L1-to-box criterion

**Date:** 2026-08-05  
**Method:** pure mathematics; no search or solver  
**Status:** unconditional analytic support theorem.  It separates the
Rayleigh rearrangement-orbit lemma into three checkable rows: component
count, `L1` decay, and uniform local regularity.  It does not prove those
rows for every Rayleigh iterate.

## 1. Gaussian tails survive negative-component rearrangement

Let `H` be a continuous kernel on `[0,infinity)`.  Assume

\[
 H_-(x)\le C_-e^{-\alpha x^2}                     \tag{1.1}
\]

and that every negative superlevel set

\[
 \{x:H_-(x)>s\}
\]

has at most `M` interval components.  Let `C_H` be the anchored
negative-component profile and `\mathcal RH=H_+-C_H`.

### Theorem 1.1 (component-count tail propagation)

For every `t>=0`,

\[
 \boxed{C_H(t)\le MC_-e^{-\alpha t^2}.}            \tag{1.2}
\]

Consequently, if also

\[
 H_+(t)\le C_+e^{-\alpha t^2},                    \tag{1.3}
\]

then

\[
 \boxed{|\mathcal RH(t)|
 \le(C_++MC_-)e^{-\alpha t^2}.}                   \tag{1.4}
\]

### Proof

Fix a level `s` and a negative component of length at least `t`.  Since
the component lies in the nonnegative half-line, its right endpoint is at
least `t`.  By continuity, the level at that endpoint is at least `s` in
the limiting sense.  Equation (1.1) therefore implies

\[
 s\le C_-e^{-\alpha t^2}.                         \tag{1.5}
\]

Thus no level above the right side of (1.5) contributes to `C_H(t)`, and
at every contributing level there are at most `M` components.  Integrating
the component count over `s` gives (1.2).  Equation (1.4) follows from
`|H_+-C_H|<=H_++C_H`. `square`

In particular every such iterate has finite unit-block box norm.

## 2. Uniform regularity upgrades L1 decay

Let

\[
 \|H\|_\square
 =\sum_{j\ge0}\sup_{j\le t\le j+1}|H(t)|.
\]

### Theorem 2.1 (L1-to-box upgrade)

Let `(H_n)` be a sequence of kernels such that

1. `||H_n||_1 -> 0`;
2. every `H_n` is `L`-Lipschitz for one fixed finite `L`; and
3. there are fixed `C,alpha>0` with

   \[
   |H_n(t)|\le Ce^{-\alpha t^2}
   \qquad(n\ge0,t\ge0).                            \tag{2.1}
   \]

Then

\[
 \boxed{\|H_n\|_\square\longrightarrow0.}         \tag{2.2}
\]

### Proof

Fix `T`.  If `M_n(T)=sup_(0<=t<=T)|H_n(t)|`, the Lipschitz property
forces `|H_n|>=M_n(T)/2` on a one-sided interval of length at least

\[
 \min\{M_n(T)/(2L),T\}
\]

adjacent to a maximizing point (with the evident trivial interpretation
when `L=0`).  Hence `||H_n||_1->0` implies

\[
 M_n(T)\longrightarrow0                           \tag{2.3}
\]

for every fixed `T`.

Given `epsilon>0`, choose an integer `T` so large that

\[
 \sum_{j\ge T}Ce^{-\alpha j^2}<\epsilon/2.
\]

By (2.3), for all sufficiently large `n`, each of the first `T` unit
blocks has supremum below `epsilon/(2T)`.  The first `T` blocks contribute
less than `epsilon/2`, and (2.1) bounds the tail by less than
`epsilon/2`.  This proves (2.2). `square`

## 3. A quantitative origin-overlap bound

### Proposition 3.1

Suppose `H_+` and `C_H` are both `L`-Lipschitz, with

\[
 a=H_+(0)>0,
 \qquad
 b=C_H(0)>0,
 \qquad
 m_0=\min\{a,b\}.
\]

Then

\[
 \boxed{
 \int_0^\infty\min\{H_+(t),C_H(t)\}dt
 \ge {m_0^2\over4L}}                              \tag{3.1}
\]

when `L>0`; for `L=0` use the evident constant-function interpretation.
Consequently

\[
 \boxed{
 \|\mathcal RH\|_1
 \le\|H\|_1-{m_0^2\over2L}.}                      \tag{3.2}
\]

### Proof

For

\[
 0\le t\le {m_0\over2L},
\]

both functions are at least `m_0/2`.  Integrating their minimum on that
interval gives (3.1).  Substitute it in the exact dissipation identity to
obtain (3.2). `square`

For the first Rayleigh step, `H_+(0)=K_0` and `C_H(0)=-m` are both
positive.  For the second, the authenticated count theorem gives

\[
 (\mathcal RK)_+(0)=P>q=C_{\mathcal RK}(0)>0.
\]

Thus the first two Rayleigh rearrangements have strict, quantitatively
local `L1` dissipation.  Iteration still requires uniform control of the
corresponding amplitudes and Lipschitz constants.

## 4. Exact fixed points and the sign-reversal obstruction

### Theorem 4.1 (fixed-point classification)

Let `H` be a zero-integral kernel in the domain of `\mathcal R`.  Then

\[
 \boxed{\mathcal RH=H}                             \tag{4.1}
\]

if and only if, up to null sets,

1. `H_-` is nonincreasing on an initial interval and vanishes afterward;
2. `H_+` vanishes on that initial interval.

Equivalently, every nonzero fixed point has the sign-reversed separated
form

\[
 \boxed{
 H(t)=-N(t)\text{ near the origin},
 \qquad
 H(t)=P(t)\ge0\text{ only after }N\text{ ends},}   \tag{4.2}
\]

where `N` is nonnegative and nonincreasing.

Moreover, if one step has zero overlap,

\[
 \int\min\{H_+,C_H\}=0,                           \tag{4.3}
\]

then `\mathcal RH` is already a fixed point.

### Proof

Suppose `\mathcal RH=H`.  On the set where `H>0`, equation

\[
 H=H_+-C_H

\]

forces `C_H=0`.  On the set where `H<0`, it forces

\[
 H_- = C_H.
\]

The profile `C_H` is nonincreasing and supported on an initial interval.
This proves the two stated properties.

Conversely, the negative superlevel sets of a nonincreasing initial
profile are themselves initial intervals.  Rearranging them therefore
does nothing: `C_H=H_-`.  Since the positive part is disjoint,

\[
 \mathcal RH=H_+-H_-=H.
\]

Finally, (4.3) says that `H_+` and the nonincreasing initial profile
`C_H` are disjoint.  Put `G=\mathcal RH=H_+-C_H`.  Then

\[
 G_+=H_+,
 \qquad
 G_-=C_H.
\]

The preceding converse applies to `G`, so `\mathcal RG=G`. `square`

Thus mere `L1` monotonicity cannot prove the Rayleigh orbit lemma.  One
must prevent the orbit from approaching a sign-reversed separated fixed
point.  A sufficient invariant would keep a quantitatively nonzero amount
of positive mass overlapping the initial rearranged-negative profile at
every scale.

## 5. Exact moment drift

### Proposition 5.1 (translation-moment identity)

Assume the first signed moment is finite.  If the negative superlevel
components are

\[
 I_{s,j}=(a_{s,j},a_{s,j}+\ell_{s,j}),
\]

then

\[
 \boxed{
 \int_0^\infty t(\mathcal RH)(t)dt
 =\int_0^\infty tH(t)dt
  +\int_0^\infty\sum_j a_{s,j}\ell_{s,j}ds.}       \tag{5.1}
\]

In particular the signed first moment is nondecreasing along the orbit.

More generally, for every `p>=0` for which the moments are finite,

\[
 \int_0^\infty t^p C_H(t)dt
 ={1\over p+1}\int_0^\infty
   \sum_j\ell_{s,j}^{p+1}ds,                      \tag{5.2}
\]

whereas

\[
 \int_0^\infty t^pH_-(t)dt
 ={1\over p+1}\int_0^\infty\sum_j
 \left((a_{s,j}+\ell_{s,j})^{p+1}
       -a_{s,j}^{p+1}\right)ds.                   \tag{5.3}
\]

Thus every nonnegative power moment of the signed kernel is
nondecreasing under `\mathcal R`.

### Proof

For one interval,

\[
 \int_0^{\ell}t\,dt={\ell^2\over2},
 \qquad
 \int_a^{a+\ell}t\,dt=a\ell+{\ell^2\over2}.
\]

Layer cake and summation give (5.1).  Replacing `t` by `t^p` gives
(5.2)--(5.3); the latter integrand is at least the former because
`a>=0`. `square`

Every nonzero fixed point from Theorem 4.1 has strictly positive signed
first moment: its positive mass lies strictly to the right of an equal
amount of negative prefix mass.  Therefore a sufficient alternative to a
direct overlap contraction is to prove that the Rayleigh orbit's increasing
first moment never reaches zero.  By (5.1), this is the exact scalar bound

\[
 \sum_{n\ge0}\int_0^\infty\sum_j
 a^{(n)}_{s,j}\ell^{(n)}_{s,j}ds
 \le-\int_0^\infty tK(t)dt.                       \tag{5.4}
\]

No such cumulative translation bound is claimed here.

There is also a simple sign-order certificate.  If a nonzero zero-integral
kernel has one sign crossing

\[
 H(t)\ge0\ (t<b),
 \qquad
 H(t)\le0\ (t>b),                                 \tag{5.5}
\]

then

\[
 \int_0^\infty tH(t)dt
 =\int_0^\infty(t-b)H(t)dt<0.                     \tag{5.6}
\]

The original Rayleigh kernel has this sign order, and the authenticated
one-well theorem gives it for the first iterate as well.  Thus propagation
of positive-prefix/negative-tail sign order would automatically keep the
orbit away from every nonzero fixed point.  The second iterate's sign
order is not proved here.

## 6. Exact Rayleigh orbit checklist

Let

\[
 K_{n+1}=\mathcal RK_n,
 \qquad K_0=K
\]

be the anchored negative-component rearrangement orbit.  The all-price
orbit theorem is therefore proved by the following three statements:

1. **Dissipation:** the exact overlap identity forces

   \[
   \|K_n\|_1\to0;
   \]

2. **Shape:** negative superlevel component counts stay uniformly bounded,
   so Theorem 1.1 propagates one common Gaussian envelope; and
3. **Regularity:** the iterates have one common Lipschitz bound.

Under these rows Theorem 2.1 gives box-norm convergence, and the anchored
orbit criterion gives

\[
 \int K\,d\rho\ge0
\]

for every admissible price measure.

The first Rayleigh iterate has one negative component at every level by
the one-well theorem.  The remaining exact analytic frontier is therefore
to propagate a bounded-component/Lipschitz class and obtain a quantitative
lower bound on the `L1` overlap dissipation.  This note supplies the tail
and compactness implications once those estimates are known; it does not
assert them.

## 7. Frozen dependency

`MATH_THEOREM_ANCHORED_NEGATIVE_COMPONENT_REARRANGEMENT_OPERATOR_20260805.md`,
SHA at use
`d25d240c3bafc39e4b581dfa5fbb0379dfa6dd9a76e00458d24227a146e0ba8b`.
