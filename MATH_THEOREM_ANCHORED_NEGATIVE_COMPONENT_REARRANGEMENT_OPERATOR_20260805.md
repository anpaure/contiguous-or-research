# Anchored negative-component rearrangement and an all-price iteration criterion

**Date:** 2026-08-05  
**Method:** pure mathematics; no search or solver  
**Status:** unconditional exact operator inequality.  Every negative
superlevel component of a signed kernel can be moved to an initial interval
using the anchored-window axiom.  This defines a deterministic nonlinear
kernel transform which lowers the pairing against every admissible price
measure and preserves Lebesgue integral.  For the Rayleigh kernel its first
iterate is exactly the equal-level transformed kernel.  Universal
Rayleigh positivity follows if the deterministic orbit tends to zero in
one explicit box norm.  That convergence is not proved here.

## 1. Anchored measures

Let `rho` be a locally finite nonnegative measure on `[0,infinity)` which
satisfies

\[
 \rho((x,x+t])\le\rho([0,t])
 \qquad(x,t>0).                                    \tag{1.1}
\]

These are exactly the Stieltjes measures of nonnegative nondecreasing
subadditive prices.

Let `H` be a continuous integrable signed kernel on `[0,infinity)` whose
positive and negative parts have finite integrals.  For `s>0`, write the
open negative superlevel set as its disjoint interval components

\[
 \{x:H_-(x)>s\}=\bigsqcup_j I_{s,j},
 \qquad \ell_{s,j}=|I_{s,j}|.                     \tag{1.2}
\]

Countably many components are allowed.  Define the anchored component
profile

\[
 C_H(t)=\int_0^\infty
          \sum_j {\bf1}_{\{t\le\ell_{s,j}\}}\,ds. \tag{1.3}
\]

It is nonnegative and nonincreasing.  Define the nonlinear transform

\[
 \boxed{(\mathcal RH)(t)=H_+(t)-C_H(t).}           \tag{1.4}
\]

## 2. Universal anchored-window inequality

### Theorem 2.1 (negative-component rearrangement)

For every anchored measure `rho` for which the displayed pairings are
defined,

\[
 \boxed{
 \int H\,d\rho\ge\int\mathcal RH\,d\rho.}         \tag{2.1}
\]

Moreover,

\[
 \boxed{
 \int_0^\infty C_H(t)dt
 =\int_0^\infty H_-(x)dx,}                        \tag{2.2}
\]

and hence

\[
 \boxed{
 \int\mathcal RH=\int H.}                        \tag{2.3}
\]

### Proof

Layer cake and disjointness of the components give

\[
 \int H_-\,d\rho
 =\int_0^\infty\sum_j\rho(I_{s,j})ds.
\]

For a component of length `ell_(s,j)`, the anchored inequality gives

\[
 \rho(I_{s,j})\le\rho([0,\ell_{s,j}]).
\]

Therefore, by Tonelli,

\[
\begin{aligned}
 \int H_-\,d\rho
 &\le\int_0^\infty\sum_j
       \rho([0,\ell_{s,j}])ds\\
 &=\int_0^\infty C_H(t)d\rho(t).
\end{aligned}
\]

Subtracting this inequality from `int H_+ d rho` proves (2.1).

Applying Tonelli with Lebesgue measure instead gives

\[
\begin{aligned}
 \int_0^\infty C_H(t)dt
 &=\int_0^\infty\sum_j\ell_{s,j}ds\\
 &=\int_0^\infty H_-(x)dx,
\end{aligned}
\]

which is (2.2); equation (2.3) follows. `square`

Endpoint conventions in (1.2) are immaterial after integration in `s`.
The weak inequality in (1.3) is chosen so that an atom of `rho` at a
component length is counted exactly in `rho([0,ell_(s,j)])`; it is of
course immaterial for the Lebesgue identities.

## 3. Exact variation identity

### Proposition 3.1

The transform obeys

\[
 \boxed{
 \|\mathcal RH\|_1
 =\|H\|_1-2\int_0^\infty
            \min\{H_+(t),C_H(t)\}\,dt.}           \tag{3.1}
\]

In particular it is `L^1`-nonexpansive, and it is strictly contracting
whenever the positive kernel and the rearranged negative profile overlap
on a set of positive measure.

### Proof

Pointwise,

\[
 |H_+-C_H|=H_++C_H-2\min(H_+,C_H).
\]

Integrate and use (2.2). `square`

If `int H=0`, then every iterate, whenever defined, again has integral
zero.  Thus finite arrival at a nonnegative kernel can occur only by exact
annihilation.

## 4. The first Rayleigh iterate is the equal-level transform

Let `K` be the Rayleigh signed-tail kernel, let `b` be its first zero and
`m` its minimum.  For `m<u<0`, let

\[
 \ell(u)<r(u),\qquad K(\ell(u))=K(r(u))=u,
\]

put `z(u)=r(u)-ell(u)`, and write `u(t)=z^{-1}(t)`.

At negative depth `s in (0,-m)`, the unique negative superlevel component
is

\[
 I_s=(\ell(-s),r(-s))
\]

and has length `z(-s)`.  Consequently

\[
\begin{aligned}
 C_K(t)
 &=\int_0^{-m}{\bf1}_{\{t\le z(-s)\}}ds\\
 &=-u(t).                                         \tag{4.1}
\end{aligned}
\]

Since `K_+=K` on `[0,b)` and vanishes after `b`,

\[
 \boxed{
 (\mathcal RK)(t)=
 \begin{cases}
 K(t)+u(t),&0\le t<b,\\
 u(t),&t\ge b.
 \end{cases}}                                     \tag{4.2}
\]

Thus `\mathcal RK` is literally the first equal-level transformed kernel.
The one-well theorem proves that it has one negative superlevel component
at every depth.

Let

\[
 P=K(0)+m,
 \qquad q=-u(b).
\]

The exact two-to-three count theorem says

\[
 0<q<P<2q.                                        \tag{4.3}
\]

Since the depth of the unique negative lobe of `\mathcal RK` is `q`,

\[
 \boxed{(\mathcal R^2K)(0)=P-q>0.}                \tag{4.4}
\]

The separate second-stage prefix-Hall no-go concerns a literal repeated
socket coupling.  It does not invalidate the dual inequality

\[
 \int\mathcal RK\,d\rho
 \ge\int\mathcal R^2K\,d\rho,                    \tag{4.5}
\]

which follows directly from Theorem 2.1.

## 5. A deterministic all-price convergence criterion

For a bounded kernel `H`, define

\[
 \|H\|_{\square}
 =\sum_{j=0}^\infty
   \sup_{j\le t\le j+1}|H(t)|.                   \tag{5.1}
\]

### Theorem 5.1 (orbit criterion)

Suppose every iterate

\[
 K_n=\mathcal R^nK
\]

is defined and

\[
 \boxed{\|K_n\|_{\square}\longrightarrow0.}      \tag{5.2}
\]

Then

\[
 \boxed{
 \int K\,d\rho\ge0}                              \tag{5.3}
\]

for every anchored measure `rho` for which the Rayleigh pairing is finite.
Equivalently, every nonnegative nondecreasing subadditive covering price
passes the Rayleigh configuration inequality.

### Proof

Iterating Theorem 2.1 gives

\[
 \int K\,d\rho\ge\int K_n\,d\rho.                \tag{5.4}
\]

If `rho([0,1])=0`, the anchored inequality forces `rho=0`, and there is
nothing to prove.  Otherwise normalize `rho([0,1])=1`.  Applying (1.1) to
each unit interval gives

\[
 \rho((j,j+1])\le1.
\]

Hence

\[
 \left|\int K_n\,d\rho\right|
 \le\sum_{j\ge0}\sup_{j\le t\le j+1}|K_n(t)|
 =\|K_n\|_{\square}.                              \tag{5.5}
\]

Let `n` tend to infinity in (5.4).  Equations (5.2)--(5.5) give (5.3).
`square`

The same proof works with any summable unit-block envelope, not only the
specific norm (5.1).

## 6. Exact surviving scalar lemma

The all-grid Bellman/anchored-window gate is therefore closed by the
following deterministic one-dimensional statement:

> **Rayleigh rearrangement-orbit lemma.**  Every iterate of `mathcal R`
> applied to the Rayleigh kernel has summable unit-block envelope, and
> `||mathcal R^nK||_square -> 0`.

Proposition 3.1 supplies the exact `L^1` dissipation at every step:

\[
 \|K_{n+1}\|_1
 =\|K_n\|_1
 -2\int\min\{(K_n)_+,C_{K_n}\}.                  \tag{6.1}
\]

Thus a sufficient quantitative route is a uniform lower bound on the
overlap in (6.1), together with propagation of a Gaussian unit-block
envelope.  Neither estimate is proved here.  `L^1` convergence alone is
not enough for arbitrary singular anchored measures, which is why
Theorem 5.1 uses the stronger box norm.

This operator route bypasses grid enumeration, Apéry branch
classification, and literal packet feasibility.  Its sole remaining input
is the analytic orbit lemma above.

## 7. Frozen dependencies

1. `MATH_THEOREM_SUBADDITIVE_PRICE_MEASURE_AND_SUPERADDITIVE_CLOCK_REDUCTION_20260804.md`.
2. `MATH_THEOREM_RAYLEIGH_EQUAL_LEVEL_PRIMARY_SUBTRACTION_20260805.md`.
3. `MATH_THEOREM_RAYLEIGH_EQUAL_LEVEL_ONE_WELL_REGENERATION_20260805.md`,
   SHA at use
   `910adbabec163e81d7896e155255561ec00463ca8fb67b9c7bf69aebd9588e20`.
4. `MATH_THEOREM_RAYLEIGH_FIRST_TRANSFORM_EXACT_TWO_THREE_COUNT_WINDOW_20260805.md`,
   SHA at use
   `1931d629efdcf12c2ec0167a004ead83e547050d44bc23464252dc0a1e062a10`.
