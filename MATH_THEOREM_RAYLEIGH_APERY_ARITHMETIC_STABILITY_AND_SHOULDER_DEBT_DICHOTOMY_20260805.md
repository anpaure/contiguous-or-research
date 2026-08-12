# Rayleigh Apéry clocks: arithmetic stability and a shoulder-debt dichotomy

**Date:** 2026-08-05  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional quantitative stability theorem.  A formal
maximum-density Apéry clock sufficiently close to its reciprocal arithmetic
comb has a fixed positive Rayleigh margin.  After restoring the exact
finite availability shoulder, every nonpositive first-minimum-normalized
clock must therefore exhibit either a fixed relative Apéry displacement or
a fixed adverse shoulder debt.  The theorem does not show that the first
alternative itself produces physical configuration slack.

## 0. Setup

Let `K` be the Rayleigh kernel, let `zeta` be its unique global minimum,
and put

\[
 C(h)=\sum_{m\ge0}K(mh).                           \tag{0.1}
\]

The first-minimum theorem reduces every possible counterclock to a finite
Bellman clock `V` whose first `zeta` crossing is saturated.  Let

\[
 \lambda=\max_j{c_j\over j}>0
\]

be its maximum density.  Its formal Apéry clock has the form

\[
 U_m=\lambda m+\beta_{m\bmod g},
 \qquad \beta_0=0,
 \qquad \beta_r\le0,                              \tag{0.2}
\]

and the exact conductor theorem gives

\[
 V_m\le U_m,
 \qquad
 V_m=U_m\quad(m\ge L),                            \tag{0.3}
\]

where one may take `L=N(N-1)` for a normalized grid of size `N`.

Define the Apéry displacement and the genuinely adverse finite shoulder by

\[
 \Delta=\max_{0\le r<g}(-\beta_r),                \tag{0.4}
\]

\[
 \mathscr S^-=
 \sum_{m=0}^{L-1}
 \bigl(K(U_m)-K(V_m)\bigr)_+.                     \tag{0.5}
\]

Then the exact identity implies

\[
 \Phi(V)\ge\Phi(U)-\mathscr S^-.                 \tag{0.6}
\]

## 1. A bounded-variation sampling lemma

### Lemma 1.1

Let `f` be absolutely continuous on `[0,infinity)`, with `f'` integrable
and of bounded variation, and assume the two sampled series below converge
absolutely.  Let `h>0`, and suppose

\[
 |x_m-mh|\le\epsilon h\qquad(m\ge0),
 \qquad 0\le\epsilon\le{1\over2},                \tag{1.1}
\]

with `x_0=0`.  Then

\[
 \boxed{
 \left|\sum_{m\ge0}f(x_m)-\sum_{m\ge0}f(mh)\right|
 \le
 \epsilon\bigl(\|f'\|_1+h\operatorname {Var}(f')\bigr).
 }                                                  \tag{1.2}
\]

#### Proof

For `m>=1`, both `x_m` and `mh` lie in the cell

\[
 I_m=[(m-1/2)h,(m+1/2)h].
\]

Hence

\[
 |f(x_m)-f(mh)|
 \le\epsilon h\sup_{I_m}|f'|.                    \tag{1.3}
\]

For a nonnegative BV function `q` on an interval `I` of length `h`,

\[
 h\sup_Iq\le\int_Iq+h\operatorname {Var}_I(q).   \tag{1.4}
\]

Apply this to `q=|f'|`.  The cells `I_m`, `m>=1`, have disjoint interiors,
and variation of `|f'|` is at most variation of `f'`.  Summing (1.3)--(1.4)
gives

\[
 \sum_{m\ge1}|f(x_m)-f(mh)|
 \le\epsilon\left(\int_{h/2}^\infty|f'|
       +h\operatorname {Var}_{[h/2,\infty)}(f')\right),
\]

which is at most the right side of (1.2).  The `m=0` term vanishes.
`square`

## 2. Quantitative Apéry stability

The Rayleigh kernel has `K' in L^1` and `K'` has finite total variation.
Set

\[
 B(h)=\|K'\|_1+h\operatorname {Var}(K').          \tag{2.1}
\]

### Theorem 2.1 (formal-clock stability)

If

\[
 \Delta\le{\lambda\over2},                       \tag{2.2}
\]

then

\[
 \boxed{
 \Phi(U)\ge C(\lambda)-{\Delta\over\lambda}B(\lambda).
 }                                                  \tag{2.3}
\]

#### Proof

Equation (0.2) gives

\[
 |U_m-\lambda m|=-\beta_{m\bmod g}\le\Delta.
\]

Apply Lemma 1.1 with `f=K`, `h=lambda`, and
`epsilon=Delta/lambda`. `square`

This is a genuine all-period estimate: neither `g` nor the conductor
appears in the right side.

## 3. Small-mesh positive neighborhood

The exact comb asymptotic is

\[
 C(h)={K(0)\over2}+O(h).                          \tag{3.1}
\]

Choose `h_0>0` so small that

\[
 C(h)\ge {K(0)\over4}\qquad(0<h\le h_0),         \tag{3.2}
\]

and put

\[
 B_0=\|K'\|_1+h_0\operatorname {Var}(K'),
 \qquad
 \epsilon_0=min\left\{{1\over2},{K(0)\over16B_0}\right\}.
                                                               \tag{3.3}
\]

### Corollary 3.1 (arithmetic stability ball)

For `0<lambda<=h_0`, if

\[
 \Delta\le\epsilon_0\lambda,                    \tag{3.4}
\]

then

\[
 \boxed{\Phi(U)\ge {3K(0)\over16}.}             \tag{3.5}
\]

#### Proof

Equations (2.3), (3.2), and (3.3) give

\[
 \Phi(U)
 \ge {K(0)\over4}-\epsilon_0B_0
 \ge {3K(0)\over16}.
\]

`square`

At reciprocal meshes `lambda=A/q`, Poisson summation gives the sharper
strict comb value

\[
 C(A/q)={1\over2}-e^{-\pi/4}
 -2q\sum_{m\ge1}e^{-4\pi q^2m^2}.                \tag{3.6}
\]

No exact reciprocal comb has zero or negative margin.

## 4. Exact shoulder dichotomy

### Theorem 4.1

Let `V` be a saturated first-`zeta` clock, with formal Apéry clock `U`,
and suppose `0<lambda<=h_0`.  If

\[
 \Phi(V)\le0,                                    \tag{4.1}
\]

then at least one of the following holds:

\[
 \boxed{\Delta>\epsilon_0\lambda}                \tag{4.2}
\]

or

\[
 \boxed{\mathscr S^-\ge{3K(0)\over16}.}          \tag{4.3}
\]

#### Proof

If (4.2) fails, Corollary 3.1 gives
`Phi(U)>=3K(0)/16`.  Equation (0.6) and (4.1) then force (4.3).
`square`

Thus a near-arithmetic formal tail and a small adverse shoulder cannot
coexist in a counterexample.  Any small-mesh counterclock must carry a
dimension-free amount of one of two explicit defects:

1. relative Apéry displacement, or
2. literal adverse shoulder price.

This is the requested quantitative stability statement.  What remains is
not analytic: one must show that a displacement of size
`epsilon_0 lambda`, or a shoulder debt of size `3K(0)/16`, releases enough
actual Boolean configuration resource to fund the polynomial rounding
bank.  No such resource-conversion theorem is asserted here.

## 5. Boolean-scale interpretation

For the reciprocal comb scale `lambda asymp k^(-1/2)`, the normalized comb
margin is `Theta(k^(-1/2))`, and hence the unnormalized Boolean margin is
`Theta(W/sqrt(k))`.  This dominates every polynomial root-lattice bank.
Corollary 3.1 shows that the same conclusion survives a fixed relative
Apéry perturbation neighborhood.

The only potentially near-tight clocks are therefore outside that
neighborhood or have a macroscopically adverse finite shoulder.  The
theorem does not convert either defect into socket capacity; it isolates
the exact structural lemma needed for that conversion.

## 6. Dependencies

1. `MATH_THEOREM_RAYLEIGH_FIRST_MINIMUM_CROSSING_AND_COMPACT_PERIOD_APERTURE_20260805.md`;
2. `MATH_THEOREM_ALL_N_FIRST_CROSSING_AND_MAXIMUM_DENSITY_APERY_REDUCTION_20260804.md`;
3. `MATH_THEOREM_SMOOTH_BINOMIAL_CONFIGURATION_DUAL_AND_CEILING_PRICE_CLASSES_20260804.md`.
