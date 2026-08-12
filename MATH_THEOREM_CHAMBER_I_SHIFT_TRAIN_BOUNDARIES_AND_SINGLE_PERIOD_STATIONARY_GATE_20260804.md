# Chamber I: shift-train boundary closure and one period-stationary gate

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical reduction.  It proves both
lower-period boundary pieces of the complete chamber-I functional strictly
positive and proves that, for fixed `(a,b)`, the period fibre has at most one
interior minimum.  Consequently the former zero-gap endpoint, pure
repeated-gap endpoint, and late `b`-stationary exit all reduce to one common
period-stationary scalar gate.  This note does **not** sign that last gate and
therefore does not close chamber I or six-slot positivity.

Put

\[
 A={\sqrt\pi\over2},\qquad h(x)=xe^{-\pi x^2/4},
 \qquad F_P(w)=\sum_{q\ge0}K(qP+w).
\tag{0.1}
\]

The exact chamber-I functional is

\[
\begin{aligned}
 \mathcal G(p,a,b)={}&\mathcal L_3(p;a,2a)\\
 &+K(b-a)-K(a)+K(b)-K(2a)\\
 &+K(p+b)-K(p+2a)
\end{aligned}
\tag{0.2}
\]

on the closed physical domain

\[
 {A\over2}\le p,\qquad p\ge3a,\qquad
 0\le a\le b\le2a,\qquad p+b\le A.
\tag{0.3}
\]

The equality faces are interpreted by continuity.  Write

\[
 p_0(a)=\max\{A/2,3a\}.
\tag{0.4}
\]

For fixed feasible `(a,b)`, the period fibre is

\[
                         p_0(a)\le p\le A-b.
\tag{0.5}
\]

## 1. A shift train is decreasing on the density-tie wedge

Normalize

\[
                         t={P\over A},\qquad u={w\over A}.
\tag{1.1}
\]

For compact arguments put

\[
                         D(u)=h(1+u)-h(1-u).
\tag{1.2}
\]

### Theorem 1.1 (density-tie shift monotonicity)

For

\[
 {A\over2}\le P\le {3A\over4},
 \qquad {P\over3}\le w\le {2P\over3},
\tag{1.3}
\]

one has

\[
                         \boxed{F_P'(w)<0.}
\tag{1.4}
\]

### Proof

Termwise differentiation is justified by a Gaussian summable majorant.
After division by `2A`, the derivative is

\[
 T(t,u)=D(u)+Q(t+u)+\sum_{q\ge2}h(1+qt+u),
\tag{1.5}
\]

where

\[
 Q(z)=
 \begin{cases}
  D(z),&z\le1,\\
  h(1+z),&z\ge1.
 \end{cases}
\tag{1.6}
\]

The two formulas agree at `z=1`.

The compact third-derivative theorem gives

\[
                         D''(u)>0\qquad(0<u<1).
\tag{1.7}
\]

Also

\[
 h''(x)={\pi\over2}x
 \left({\pi x^2\over2}-3\right)e^{-\pi x^2/4}>0
 \qquad(x\ge2).
\tag{1.8}
\]

Therefore `T` is convex on each of the two polygons obtained by cutting

\[
 {1\over2}\le t\le{3\over4},
 \qquad {t\over3}\le u\le{2t\over3}
\tag{1.9}
\]

with the line `t+u=1`.  On the compact side the vertices are

\[
 (1/2,1/6),\ (3/4,1/4),\ (3/5,2/5),\ (1/2,1/3),
\tag{1.10}
\]

and on the tail side they are

\[
                         (3/4,1/4),\ (3/5,2/5),\ (3/4,1/2).
\tag{1.11}
\]

A convex function on a compact polygon is bounded above by the maximum of
its vertex values.  The following exact rational Gaussian certificate signs
all five distinct vertices:

\[
\begin{array}{c|c}
 (t,u)&\text{certified upper bound for }T(t,u)\\ \hline
 (1/2,1/6)&-1/10\\
 (3/4,1/4)&-1/100\\
 (3/5,2/5)&-1/25\\
 (1/2,1/3)&-1/10\\
 (3/4,1/2)&-1/20.
\end{array}
\tag{1.12}
\]

For completeness, (1.12) is a finite rational certificate, not a numerical
sampling assertion.  Put

\[
 L={333\over106}<\pi<{355\over113}=U,
 \qquad N=80,
\tag{1.13}
\]

and, for rational `z>=0`, define

\[
 S_N(z)=\sum_{j=0}^{N}{z^j\over j!},
 \qquad
 E_N(z)=S_N(z)+{z^{N+1}\over(N+1)!}
                    {1\over1-z/(N+2)}.
\tag{1.14}
\]

Every argument used below is at most `33/4`, so

\[
 {Ux^2\over4}<54<N+2.
\]

The positive exponential series and the geometric bound on its tail give

\[
 S_N(z)<e^z<E_N(z)\qquad(0<z<N+2).
\]

Consequently every needed Gaussian has the exact rational enclosure

\[
 \boxed{
 {x\over E_N(Ux^2/4)}<h(x)<{x\over S_N(Lx^2/4)}.}
\tag{1.14a}
\]

Keep the terms through `q=8` in (1.5).  For the remaining tail,
consecutive arguments differ by at least `1/2`; the exact ratio

\[
 {h(x+\delta)\over h(x)}
 =\left(1+{\delta\over x}\right)
 e^{-(\pi/4)(2x\delta+\delta^2)}
\tag{1.15}
\]

and `pi>3` bound it by the first omitted term times `4/3`.  Indeed, from
`q=9` onward one has `x>=17/3` and `1/2<=delta<=3/4`; hence the ratio is
smaller than

\[
 {6\over5}e^{-4}<{1\over4}.
\]

For an upper bound on `T`, use the upper enclosure in (1.14a) on every
positive occurrence of `h` and the lower enclosure on every subtracted
occurrence.  Substitution followed by clearing positive denominators gives,
in the order of (1.12), the strict rational upper bounds

\[
 -{134207\over10^6},\quad-{21844\over10^6},
 -{51525\over10^6},\quad-{134210\over10^6},
 -{109793\over10^6}.
\tag{1.16}
\]

These are respectively smaller than the five simpler bounds displayed in
(1.12).

Thus `T<0` at every vertex and hence throughout both polygons.  Equations
(1.5) and (1.1) prove (1.4).  \(\square\)

## 2. The half-period lower boundary

Suppose first that

\[
                         p=p_0(a)=A/2.
\tag{2.1}
\]

Then `a<=A/6`, `b<=2a<=A/3`, and `x=b-a<=a`.  Put `H=A/2` and
`F=F_H`.  Rewrite (0.2) exactly as

\[
\begin{aligned}
 \mathcal G(H,a,b)={}&F(0)\\
 &+\{K(x)+\sum_{q\ge1}K(qH+a)\}\\
 &+\{K(b)+K(H+b)+\sum_{q\ge2}K(qH+2a)\}.
\end{aligned}
\tag{2.2}
\]

The kernel is decreasing on `[0,2A/3]`, so `K(x)>=K(a)`.  In the last
brace, every `q>=2` argument lies on the increasing Gaussian tail and
`2a>=b`; hence

\[
 K(qH+2a)\ge K(qH+b).
\tag{2.3}
\]

Therefore

\[
                         \mathcal G(H,a,b)
 \ge F(0)+F(a)+F(b).
\tag{2.4}
\]

The proved half-period theorem says `F'(w)<0` on `[0,A/3]`.  Since
`b<=2a`,

\[
 \mathcal G(H,a,b)
 \ge F(0)+F(a)+F(2a).
\tag{2.5}
\]

The right side decreases with `a` on `[0,A/6]`, and at `a=A/6` its
three residue classes form the complete arithmetic `A/6` lattice.  Thus

\[
 \boxed{\mathcal G(A/2,a,b)\ge C(A/6)>0.}
\tag{2.6}
\]

## 3. The density-tie lower boundary

Suppose next that

\[
                         p=p_0(a)=3a.
\tag{3.1}
\]

Feasibility gives

\[
                         A/6\le a\le A/4.
\tag{3.2}
\]

The upper equality is the threshold corner and is understood by
continuity, as in the closed-domain convention.

Put `P=3a` and `F=F_P`.  The same regrouping as in (2.2) gives

\[
                         \mathcal G(3a,a,b)
 \ge F(0)+F(a)+F(b).
\tag{3.3}
\]

Indeed the only tail comparison now begins at `q=2`, where
`qP+b>=7a>A`, so monotonicity on the Gaussian tail is again in the
correct direction.  Theorem 1.1 applies because

\[
 A/2\le P<3A/4,
 \qquad P/3=a\le b\le2a=2P/3.
\]

It gives `F(b)>=F(2a)`.  Hence

\[
 \boxed{
 \mathcal G(3a,a,b)
 \ge F(0)+F(a)+F(2a)=C(a)>0.}
\tag{3.4}

Thus both pieces of the complete lower-period boundary (0.4) are strictly
positive.

## 4. Strict convexity of the period derivative

For fixed `(a,b)`, differentiate the literal exact clock.  The first
period contributes the three compact points

\[
                         p,\quad p+a,\quad p+b,
\]

and every later period is the pure three-residue tail.  Therefore

\[
\begin{aligned}
 \Pi(p,a,b):={\partial\mathcal G\over\partial p}
 ={}&K'(p)+K'(p+a)+K'(p+b)\\
 &+\sum_{q\ge2}q\{K'(qp)+K'(qp+a)+K'(qp+2a)\}.
\end{aligned}
\tag{4.1}
\]

On `(0,A)`, the compact theorem gives `K'''>0`.  On the tail,

\[
 K'''(x)=4(A+x)\{2(A+x)^2-3\}e^{-(A+x)^2}>0
 \qquad(x\ge A),
\tag{4.2}
\]

because `A+x>=2A=sqrt(pi)` and `2pi-3>0`.  All `q=1` arguments in
(4.1) are compact, while all `q>=2` arguments are on the tail.  Hence

\[
\boxed{
 {\partial^3\mathcal G\over\partial p^3}
 =K'''(p)+K'''(p+a)+K'''(p+b)
 +\sum_{q\ge2}q^3\{K'''(qp)+K'''(qp+a)+K'''(qp+2a)\}>0.}
\tag{4.3}
\]

Thus `Pi=partial_p G` is strictly convex.  Define

\[
 \Omega(p,a,b):={\partial^2\mathcal G\over\partial p^2}
\tag{4.4}
\]

and the period-stationary set

\[
 \mathcal T_{a,b}=
 \{p\in(p_0(a),A-b):\Pi(p,a,b)=0,\ \Omega(p,a,b)\ge0\}.
\tag{4.5}
\]

Exactly as for the earlier `b`-fibre reduction, strict convexity of `Pi`
implies

\[
                         |\mathcal T_{a,b}|\le1.
\tag{4.6}
\]

Every interior minimum in the period direction belongs to this set.  The
upper endpoint `p=A-b` is the already-proved five-slot threshold endpoint
and is strictly positive.  Sections 2--3 prove the lower endpoint strictly
positive.  Therefore

\[
\boxed{
 \min_{p_0(a)\le p\le A-b}\mathcal G(p,a,b)
 =\min\left\{
   \mathcal G(p_0(a),a,b),\ \mathcal G(A-b,a,b),
   \{\mathcal G(p,a,b):p\in\mathcal T_{a,b}\}
            \right\}.}
\tag{4.7}
\]

The final set is omitted when empty, and both displayed endpoint values
are positive.

There is also a strict location restriction.  Every term in the second
line of (4.1) is positive.  If `p>=xi`, where `xi` is the positive compact
root of `K'`, then all three first-line terms are nonnegative.  Hence

\[
                         \boxed{p\in\mathcal T_{a,b}\Longrightarrow p<\xi.}
\tag{4.8}
\]

## 5. One common residual scalar

Define, when `mathcal T_(a,b)` is nonempty, its unique element
`p_*(a,b)`, and put

\[
 \boxed{
 \mathfrak S(a,b)=\mathcal G(p_*(a,b),a,b),
 \qquad
 \Pi(p_*,a,b)=0,\quad\Omega(p_*,a,b)\ge0,\quad p_*<\xi.}
\tag{5.1}
\]

If the stationary set is empty, set `mathfrak S(a,b)=+infinity`.  Then

\[
 \boxed{
 \text{complete chamber-I positivity is equivalent to }
 \mathfrak S(a,b)>0
 \text{ for every feasible }(a,b).}
\tag{5.2}
\]

This is the promised common collapse of the three former exits:

* the zero-first-gap endpoint is the slice `b=a` of (5.1);
* the pure repeated-gap endpoint is the slice `b=2a`;
* an interior late `b`-stationary exit must satisfy (5.1) as well as

  \[
  K'(b-a)+K'(b)+K'(p_*+b)=0,
  \qquad
  K''(b-a)+K''(b)+K''(p_*+b)\ge0.
  \tag{5.3}
  \]

In the last case the old late-strip theorem and (4.8) give the sharp
two-sided crossing

\[
                         \boxed{p_*<\xi<p_*+b<A.}
\tag{5.4}
\]

There is a further curvature filter which removes `b` entirely.  On the
compact branch

\[
 {1\over2}K''(Au)=h'(1+u)+h'(1-u).
\tag{5.5}
\]

The right side is strictly increasing on `[0,1/2]`, and a direct rational
endpoint estimate gives

\[
 h'(7/5)+h'(3/5)<-1/10.
\tag{5.6}
\]

For example, (5.6) follows from the same reciprocal enclosure used in
(1.14a), now with truncation order `12`; after positive denominators are
cleared its left side is below `-107/1000`.
Hence

\[
                         K''(u)<0\qquad(0\le u\le2A/5).
\tag{5.7}
\]

At a joint interior `(p,b)` minimum, the chamber inequalities imply

\[
 p\ge3a\ge{3b\over2},\qquad p+b<A,
\]

and therefore `b<2A/5`; also `0<=b-a<=b`.  Thus both low terms in

\[
 \Xi=K''(b-a)+K''(b)+K''(p+b)
\]

are negative.  Since `p+b>xi`, the high term is positive, and

\[
                         0\le\Xi<K''(p+b).
\tag{5.8}
\]

The `(p,b)` Hessian has mixed entry `K''(p+b)`.  Positive semidefiniteness
at a joint minimum consequently forces

\[
 \Omega\Xi\ge K''(p+b)^2,
 \qquad\text{hence}\qquad
 \Omega>K''(p+b).
\tag{5.9}
\]

After the common high term is cancelled, every joint late-stationary exit
must therefore pass the explicit `b`-free curvature scalar

\[
\boxed{
 \begin{aligned}
 \mathfrak C(p,a):={}&K''(p)+K''(p+a)\\
 &+\sum_{q\ge2}q^2\{K''(qp)+K''(qp+a)+K''(qp+2a)\}>0.
 \end{aligned}}
\tag{5.10}
\]

This condition is necessary, not asserted sufficient.  It is useful
because the complete joint stationary obstruction now has a scalar
curvature screen depending only on `(p,a)` before the value in (5.1) is
tested.

No endpoint value, degenerate arithmetic face, or second stationary point
remains.  What remains is the sign of the single literal scalar (5.1).

## 6. Exact scope and frozen dependencies

This theorem does not prove `mathfrak S>0`.  It therefore does not close
chamber I, complete six-slot Bellman positivity, an all-grid Bellman
inequality, or an OR-word upper bound.

| role | file | SHA-256 |
|---|---|---|
| exact chamber-I clock and `b` reduction | `MATH_THEOREM_SIX_SLOT_CHAMBER_I_EXACT_CLOCK_AND_UNIQUE_LATE_STATIONARY_REDUCTION_20260804.md` | `adcbced9bf28374e1df96466552dbe70704c720d4af81c2212978efd8e86895d` |
| half-period shift monotonicity | `MATH_THEOREM_HALF_PERIOD_TWO_COMPACT_TRAIN_AND_PRETHRESHOLD_REPEATED_GAP_CLOSURE_20260804.md` | `c35a9db78b5dc317fa319dd150c3abe0521b3043b9dc22d7066b2d14ae2afd4a` |
| five-slot threshold endpoint | `MATH_THEOREM_FIVE_SLOT_THREE_EFFICIENT_THRESHOLD_ENDPOINT_AND_DELAYED_CROSSING_REDUCTION_20260804.md` | `1e15d736592bce3103786fb965f62fe6f028436c0d35b763b195157a2cf3d0b6` |
| arithmetic ceiling positivity | `MATH_THEOREM_SMOOTH_BINOMIAL_CONFIGURATION_DUAL_AND_CEILING_PRICE_CLASSES_20260804.md` | `c3a2c1858f59fa32e61d2f9a9252085ad7fb01f3521ab5cb46998705123e103d` |
