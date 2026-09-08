# Independent audit: Chamber-I shift boundaries and period-stationary gate

**Date:** 2026-08-04  
**Verdict:** **GO after one proof-certificate repair and one boundary
typo correction.**  The shift-train
formula, polygonal convexity, five vertex signs, both lower-period boundary
closures, strict period-derivative convexity, endpoint reductions, common
stationary scalar, late crossing, and joint Hessian filter are correct.

The original source described a signed alternating Taylor truncation which,
although formally valid, is far too coarse at the largest retained Gaussian
arguments to certify the claimed negative vertex bounds.  The source has
been patched to use a fixed reciprocal positive-Taylor enclosure.  That
replacement gives exact rational bounds strictly stronger than the five
claimed margins.  No numerical search or floating-point premise enters the
corrected proof.

## 1. Exact binding

Audited and corrected source:

`MATH_THEOREM_CHAMBER_I_SHIFT_TRAIN_BOUNDARIES_AND_SINGLE_PERIOD_STATIONARY_GATE_20260804.md`

Current SHA-256:

`4a80c1bdf2e23d5b495799d41b7b30755d6500df509078cc2ec7bfdc8a134af9`.

The pre-repair workspace SHA
`5490c7db57e70f19b3b99f537021c1f7e55a4baf0b7978f3e8ffd1ddb9e90531`
is superseded and must not be cited.

The source's density-tie boundary now correctly records the closed
threshold corner as `a<=A/4`; the literal open face has `a<A/4`, and the
corner is inherited by continuity.  This correction changes no formula or
interior argument.

Frozen dependencies checked in this audit are:

| role | file | SHA-256 |
|---|---|---|
| exact Chamber-I clock and late-`b` theorem | `MATH_THEOREM_SIX_SLOT_CHAMBER_I_EXACT_CLOCK_AND_UNIQUE_LATE_STATIONARY_REDUCTION_20260804.md` | `adcbced9bf28374e1df96466552dbe70704c720d4af81c2212978efd8e86895d` |
| half-period monotonicity | `MATH_THEOREM_HALF_PERIOD_TWO_COMPACT_TRAIN_AND_PRETHRESHOLD_REPEATED_GAP_CLOSURE_20260804.md` | `c35a9db78b5dc317fa319dd150c3abe0521b3043b9dc22d7066b2d14ae2afd4a` |
| five-slot threshold endpoint | `MATH_THEOREM_FIVE_SLOT_THREE_EFFICIENT_THRESHOLD_ENDPOINT_AND_DELAYED_CROSSING_REDUCTION_20260804.md` | `1e15d736592bce3103786fb965f62fe6f028436c0d35b763b195157a2cf3d0b6` |
| arithmetic ceiling positivity | `MATH_THEOREM_SMOOTH_BINOMIAL_CONFIGURATION_DUAL_AND_CEILING_PRICE_CLASSES_20260804.md` | `c3a2c1858f59fa32e61d2f9a9252085ad7fb01f3521ab5cb46998705123e103d` |

All dependency hashes agree with the current bytes.

## 2. Exact shift derivative and polygon

For `t=P/A` and `u=w/A`, direct differentiation of

\[
 F_P(w)=\sum_{q\ge0}K(qP+w)
\]

gives

\[
 {F_P'(Au)\over2A}
 =D(u)+Q(t+u)+\sum_{q\ge2}h(1+qt+u),
\]

where

\[
 D(v)=h(1+v)-h(1-v)
\]

and `Q(z)=D(z)` before the compact threshold and `Q(z)=h(1+z)`
after it.  The two expressions agree at `z=1`, because `h(0)=0`.
There is no missing compact source or period coefficient.

The physical wedge is

\[
 {1\over2}\le t\le{3\over4},\qquad
 {t\over3}\le u\le{2t\over3}.
\]

The line `t+u=1` meets the lower rail at `(3/4,1/4)` and the upper
rail at `(3/5,2/5)`.  Hence the compact polygon has vertices

\[
 (1/2,1/6),\ (3/4,1/4),\ (3/5,2/5),\ (1/2,1/3),
\]

and the tail polygon has vertices

\[
 (3/4,1/4),\ (3/5,2/5),\ (3/4,1/2).
\]

On the compact side, every nonlinear term is a convex `D` composed with
an affine form, or a convex `h` at argument at least two.  On the tail
side the crossing term is also such an `h`.  Thus the complete infinite
sum is convex on each polygon.  A convex function on a polygon is at most
the maximum of its vertex values, so the five signs are sufficient.

## 3. Independent exact vertex certificate

Put

\[
 L={333\over106},\qquad U={355\over113},\qquad N=80,
\]

and

\[
 S_N(z)=\sum_{j=0}^{N}{z^j\over j!},\qquad
 E_N(z)=S_N(z)+{z^{N+1}\over(N+1)!}
                  {1\over1-z/(N+2)}.
\]

For every required rational argument `x`, including the first omitted
tail term, `x<=33/4`, so `Ux^2/4<54<N+2`.  The positive exponential
series and its geometric tail give

\[
 S_N(z)<e^z<E_N(z).
\]

Monotonicity in `pi` therefore yields the exact rational enclosure

\[
 {x\over E_N(Ux^2/4)}<h(x)<{x\over S_N(Lx^2/4)}.
\tag{3.1}
\]

For an upper bound on a vertex value, use the right side of (3.1) on
every positive `h` occurrence and the left side on every subtracted
occurrence.  Retain `q=2,...,8`.  From `q=9` onward, consecutive arguments
differ by `delta=t`, and

\[
 {h(x+\delta)\over h(x)}
 =\left(1+{\delta\over x}\right)
 e^{-(\pi/4)(2x\delta+\delta^2)}.
\]

Here `x>=17/3`, `1/2<=delta<=3/4`, and hence the ratio is below

\[
 {6\over5}e^{-4}<{1\over4}.
\]

Thus the omitted tail is strictly less than `4/3` times its first term.
Substitution in the five vertices and clearing the positive factorial
denominators gives, in their displayed order,

\[
 -{134207\over10^6},\quad-{21844\over10^6},
 -{51525\over10^6},\quad-{134210\over10^6},
 -{109793\over10^6}.
\]

These are respectively smaller than

\[
 -{1\over10},\quad-{1\over100},\quad-{1\over25},
 -{1\over10},\quad-{1\over20}.
\]

This independently certifies `F_P'(w)<0` throughout the complete
density-tie wedge.

## 4. Half-period boundary

At `p=A/2`, exact cancellation of the finite pulses rewrites the
Chamber-I functional as the three braces shown in the source.  Since

\[
 0\le b-a\le a\le A/6,
\]

compact monotonicity gives `K(b-a)>=K(a)`.  In the final brace, every
term from `q=2` onward lies on the increasing Gaussian tail, and
`2a>=b`, so

\[
 K(qA/2+2a)\ge K(qA/2+b).
\]

Therefore

\[
 \mathcal G(A/2,a,b)
 \ge F_{A/2}(0)+F_{A/2}(a)+F_{A/2}(b).
\]

The independently proved half-period theorem makes `F_(A/2)` strictly
decreasing on `[0,A/3]`.  Since `b<=2a`, the right side is at least

\[
 F_{A/2}(0)+F_{A/2}(a)+F_{A/2}(2a),
\]

which decreases with `a` on `[0,A/6]`.  At `a=A/6`, the three residues
modulo `A/2` are the complete arithmetic `A/6` lattice.  Hence the lower
bound is `C(A/6)>0`, exactly as claimed.

## 5. Density-tie boundary

At `p=3a`, feasibility gives `A/6<=a<=A/4`.  The same regrouping is
valid.  The altered occurrences begin at `q=2`, and

\[
 q(3a)+b\ge7a>A
\]

on every nondegenerate fibre; the equality endpoint follows by
continuity.  Thus the tail comparison again has the favorable direction.

The shift theorem applies with

\[
 P=3a,\qquad P/3=a\le b\le2a=2P/3,
 \qquad A/2\le P\le3A/4.
\]

It gives `F_P(b)>=F_P(2a)`, whence

\[
 \mathcal G(3a,a,b)
 \ge F_P(0)+F_P(a)+F_P(2a)=C(a)>0.
\]

Both pieces of the lower-period boundary are therefore rigorously closed.

## 6. Period derivative and endpoint reduction

Differentiating the literal functional cancels the `q=1` occurrence
`K'(p+2a)` and replaces it by `K'(p+b)`.  This gives exactly

\[
\begin{aligned}
 \Pi(p,a,b)={}&K'(p)+K'(p+a)+K'(p+b)\\
 &+\sum_{q\ge2}q\{K'(qp)+K'(qp+a)+K'(qp+2a)\}.
\end{aligned}
\]

The compact identity `K'''(Au)=(2/A)(h''(1+u)-h''(1-u))` is strictly
positive for `0<u<1`.  On the tail,

\[
 K'''(x)=4(A+x)\{2(A+x)^2-3\}e^{-(A+x)^2}>0
 \qquad(x\ge A).
\]

All `q=1` arguments are compact and every `q>=2` argument is in the
tail.  Consequently

\[
 \partial_p^2\Pi=\partial_p^3\mathcal G>0.
\]

Thus `Pi` is strictly convex and has at most one zero with
`Omega=partial_p Pi>=0`.  The lower endpoint is one of Sections 4--5;
the upper endpoint `p=A-b` is the already-proved threshold face.  Hence
the exact period minimum is one of these two positive endpoints or the
unique stationary value.  No period endpoint or second local-minimum
root is omitted.

If `p>=xi`, all three compact `q=1` derivatives are nonnegative and all
later derivatives are strictly positive.  Therefore a period-stationary
minimum must satisfy `p<xi`.

## 7. Common residual and joint stationary system

For each feasible `(a,b)`, let `p_*(a,b)` be the unique period-stationary
minimum when it exists.  Since both period endpoints are positive,
complete Chamber-I positivity is equivalent to positivity of

\[
 \mathfrak S(a,b)=\mathcal G(p_*(a,b),a,b)
\]

on this stationary family.  The former exits are literal slices of this
same scalar:

* `b=a` is the zero-first-gap endpoint;
* `b=2a` is the pure long-wrap endpoint;
* an interior late-`b` exit additionally satisfies

  \[
  K'(b-a)+K'(b)+K'(p_*+b)=0
  \]

  and the corresponding nonnegative second derivative.

The authenticated late-strip theorem gives `xi<p_*+b<A`; together with
the period result this is the exact crossing

\[
                         p_*<\xi<p_*+b<A.
\]

No claim of positivity for `mathfrak S` is made.

## 8. Independent curvature-filter audit

On the compact branch,

\[
 {1\over2}K''(Au)=h'(1+u)+h'(1-u).
\]

Its derivative is `h''(1+u)-h''(1-u)>0` on `[0,1/2]`.  At `u=2/5`,
put

\[
 z_1={U(7/5)^2\over4},\qquad
 z_2={L(3/5)^2\over4}.
\]

The function `g(z)=e^{-z}(1-2z)` is increasing above `3/2` and
decreasing below `3/2`.  Applying the same exact reciprocal enclosure as
in Section 3, now with `N=12`, gives after denominator clearing

\[
 h'(7/5)+h'(3/5)<-{118\over1000}<-{107\over1000}<-{1\over10}.
\]

Therefore `K''(u)<0` for `0<=u<=2A/5`.

At a joint interior `(p,b)` minimum,

\[
 p\ge3a\ge{3b\over2},\qquad p+b<A,
\]

so `b<2A/5` and both `K''(b-a)` and `K''(b)` are negative.  The late
crossing `p+b>xi`, strict compact convexity, and the two roots
`K'(0)=K'(xi)=0` imply `K''(p+b)>0`.  Thus

\[
 0\le\Xi<K''(p+b).
\]

The `(p,b)` Hessian has diagonal entries `Omega,Xi` and mixed entry
`K''(p+b)`.  Positive semidefiniteness gives

\[
 \Omega\Xi\ge K''(p+b)^2.
\]

In particular `Xi>0`, and since `Xi<K''(p+b)`,

\[
 \Omega>K''(p+b).
\]

Subtracting that common high term from `Omega` leaves exactly

\[
\begin{aligned}
 \mathfrak C(p,a)={}&K''(p)+K''(p+a)\\
 &+\sum_{q\ge2}q^2\{K''(qp)+K''(qp+a)+K''(qp+2a)\}>0.
\end{aligned}
\]

The multiplicities and mixed Hessian term are therefore correct.  This is
only a necessary filter, exactly as scoped in the source.

## 9. Scope verdict

**GO after repair:** the corrected theorem closes both lower-period
boundaries and reduces every former Chamber-I exit to one
period-stationary literal scalar with the stated late-crossing and Hessian
filters.

It does **not** prove that scalar positive, close Chamber I, prove complete
six-slot or all-grid Bellman positivity, or imply any OR-word upper bound.
