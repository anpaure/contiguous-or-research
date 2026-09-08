# Self-audit: second Rayleigh rearrangement one-crossing theorem

**Date:** 2026-08-05  
**Audited theorem:**
`MATH_THEOREM_RAYLEIGH_SECOND_REARRANGEMENT_ONE_CROSSING_20260805.md`  
**Method:** independent re-derivation of orientations and exact rational
interval arithmetic; no search or solver  
**Verdict:** **GO**, subject only to the theorem's explicit second-iterate
scope.  No all-iterate statement is licensed.

## 1. Dependency binding

The proof uses the following frozen inputs.

| file | SHA-256 | imported fact |
|---|---|---|
| `MATH_THEOREM_ANCHORED_NEGATIVE_COMPONENT_REARRANGEMENT_OPERATOR_20260805.md` | `d25d240c3bafc39e4b581dfa5fbb0379dfa6dd9a76e00458d24227a146e0ba8b` | exact negative-component rearrangement |
| `MATH_THEOREM_RAYLEIGH_EQUAL_LEVEL_ONE_WELL_REGENERATION_20260805.md` | `910adbabec163e81d7896e155255561ec00463ca8fb67b9c7bf69aebd9588e20` | `H=RK` decreases to its corner minimum and increases afterward |
| `MATH_THEOREM_RAYLEIGH_FIRST_RESIDUAL_JOB_DENSITY_DECREASE_20260805.md` | `a93f28d2364a84f4c4a5d3a1581c11c22419db3059ac8ea8fbbebf8684db5afa` | `u'` decreases on `(b,infinity)`, `e>0.565`, and the right original slope at `t=b` is below `1/10` |
| `MATH_THEOREM_RAYLEIGH_FIRST_TRANSFORM_EXACT_TWO_THREE_COUNT_WINDOW_20260805.md` | `1931d629efdcf12c2ec0167a004ead83e547050d44bc23464252dc0a1e062a10` | first-transform scalar orientation and endpoint lineage |

All imported inequalities are used in their proved directions.

## 2. Exact branch-orientation audit

### 2.1 Original level-gap map

For `m<v<0`, the original left branch `ell(v)` lies in `(b,c)` where `K`
decreases, and the right branch `r(v)` lies in `(c,infinity)` where `K`
increases.  As `v` rises from `m` to zero,

* `ell(v)` moves left;
* `r(v)` moves right;
* `z(v)=r(v)-ell(v)` increases from zero to infinity.

Therefore

\[
 z(v_0)<t\Longleftrightarrow v_0<u(t),
 \qquad
 z(v_0)>t\Longleftrightarrow v_0>u(t).           \tag{2.1}
\]

This checks all three level comparisons in the theorem:

* `z(-23/500)<9/50` gives `u(9/50)>-23/500`;
* `z(-1/40)<b=z(u(b))` gives `-1/40<u(b)`, hence `q<1/40`;
* `z(-4/125)>9/25` gives `u(9/25)<-4/125`.

### 2.2 Second negative component

For `s` increasing from zero to the depth `q`, the second left endpoint
`L(s)` moves right and the right endpoint `R(s)` moves left.  Hence
`Z(s)=R(s)-L(s)` decreases from infinity to zero.  Differentiation gives

\[
 L'(s)=1/g(L(s))>0,
 \qquad
 R'(s)=-1/f(R(s))<0,
\]

and therefore

\[
 Z'(s)=-(1/g+1/f)<0.
\]

Its decreasing inverse `C(t)` has

\[
 C'(t)=-{gf\over g+f}<0.                         \tag{2.2}
\]

Thus `-C'<f(R)`.  Since `R>b` and the imported theorem makes `u'`
strictly decreasing to the right of `b`,

\[
 -C'(t)<u'(R)<u'(b).                             \tag{2.3}
\]

This verifies the crucial derivative orientation.  No inequality was
reversed by using a decreasing inverse.

### 2.3 Endpoint ordering at `t<b`

Because the original gap `z(v)` increases with `v`, a gap `t<b` has a
lower level than the gap `b`: its left endpoint is closer to `c` and its
right endpoint is also closer to `c`.  In particular

\[
 \ell(u(t))>e:=\ell(u(b))>113/200.               \tag{2.4}
\]

On `[113/200,c]`, `K''>0`.  A direct bound is

\[
 Q'(A-x)>7/5,
 \qquad
 Q'(A+x)>-4/5,
\]

so `K''(x)>3/5`.  Hence `-K'` decreases on that interval and

\[
 -K'(\ell(u(t)))<-K'(113/200)<23/100.            \tag{2.5}
\]

The right slope is globally below `4/25` after `c`.  These are exactly
the two inputs used in the parallel-slope bound.

## 3. Exact rational Gaussian replay

Use

\[
 {4431\over5000}<A<{8863\over10000}
\]

and the degree-20 rational exponential enclosure

\[
 E_{20}(x)<e^x<
 E_{20}(x)+{x^{21}\over21!}{1\over1-x/22},
 \qquad0\le x\le4.                               \tag{3.1}
\]

All arithmetic below is over exact rational numbers.  Outward rounding to
the displayed decimal rationals gives:

| expression | certified rational interval |
|---|---:|
| `K(9/50)` | `(718/10000,720/10000)` |
| `K(69/100)` | `(-457/10000,-455/10000)` |
| `K(87/100)` | `(-456/10000,-454/10000)` |
| `K(57/100)` | `(-249/10000,-247/10000)` |
| `K(207/200)` | `(-250/10000,-249/10000)` |
| `K(9/25)` | `(302/10000,304/10000)` |
| `K(121/200)` | `(-3219/100000,-3209/100000)` |
| `K(121/125)` | `(-3213/100000,-3211/100000)` |
| `K'(9/50)` | `(-174/1000,-173/1000)` |
| `K'(113/200)` | `(-227/1000,-226/1000)` |
| `K''(9/25)` | `(-216/1000,-214/1000)` |
| `4Ae^{-pi}` | `(0,154/1000)` |

Every inequality used in the theorem follows with room:

\[
\begin{gathered}
 K(9/50)>71/1000,
 \quad -K'(9/50)>17/100,\\
 K(69/100),K(87/100)>-23/500,\\
 K(57/100),K(207/200)>-1/40,\\
 K(9/25)<31/1000,\\
 K(121/200),K(121/125)<-4/125,\\
 -K'(113/200)<23/100,
 \quad K''(9/25)<-1/5,
 \quad4Ae^{-pi}<4/25.
\end{gathered}                                    \tag{3.2}
\]

The exponential-tail inequality in (3.1) is valid because after the
`x^21/21!` term all successive ratios are at most `x/22<1`.

## 4. Interval proof of `K''<0`

Let

\[
 F(x)=-Q''(x)=4x(3-2x^2)e^{-x^2}.
\]

On `[0,sqrt(3/2)]`,

\[
 \operatorname{sgn}F'(x)
 =\operatorname{sgn}(4x^4-12x^2+3).
\]

At the smallest possible left argument,

\[
 x_0={4431\over5000}-{9\over25}={2631\over5000},
\]

the polynomial equals

\[
 -{2495762090079\over156250000000000}<0.
\]

It remains negative until `sqrt(3/2)`.  Thus `F` decreases throughout the
relevant positive part.  If `A+t<=sqrt(3/2)`, then

\[
 K'''(t)=F(A-t)-F(A+t)>0.
\]

If `A+t>sqrt(3/2)`, then `Q''(A+t)>0` and

\[
 K'''(t)=F(A-t)+Q''(A+t)>0.
\]

Hence `K''` is increasing on `[0,9/25]`.  The exact endpoint enclosure in
Section 3 gives

\[
 K''(t)\le K''(9/25)<-1/5<0,                    \tag{4.1}
\]

which authenticates the monotonicity of `-K'` used on `[9/50,a]`.

## 5. Slope arithmetic replay

For `0<t<b`, let `alpha` and `beta` be the right and left original branch
slopes.  Equations (2.5) and (3.2) give

\[
 \alpha<4/25,
 \qquad
 \beta<23/100.
\]

Thus

\[
 u'(t)={\alpha\beta\over\alpha+\beta}
 \le{\alpha+\beta\over4}<39/400.                \tag{5.1}
\]

At `t=b`, `alpha<1/10` is not inferred from `alpha<4/25`; it is imported
explicitly from equation (2.4) of the residual-job density theorem.  With
`beta<23/100`, monotonicity of the parallel sum gives

\[
 u'(b)<{(1/10)(23/100)\over1/10+23/100}
 ={23\over330}<7/100.                            \tag{5.2}
\]

For `9/50<=t<=a<9/25`, (4.1) and the derivative row of (3.2) imply

\[
 -K'(t)\ge-K'(9/50)>17/100.
\]

Subtracting (5.1) gives

\[
 g(t)>29/400>7/100>u'(b)>-C'(t),                \tag{5.3}
\]

so `(R^2K)'<0` on the asserted interval.

## 6. Endpoint and uniqueness audit

The level brackets give, in the correct directions,

\[
 H(9/50)>1/40>q,
 \qquad
 H(9/25)<0,
\]

so `a<9/25`.  On `[0,9/50]`, `H` decreases while `C<=C(0)=q`; hence

\[
 H-C\ge H(9/50)-q>0.
\]

On `[9/50,a]`, Section 5 proves strict decrease, and at `a`,

\[
 H_+(a)-C(a)=-C(a)<0.
\]

There is exactly one zero.  Beyond `a`, `H_+=0` and `C>0`, so the kernel
stays strictly negative.  This completes the independent logical replay.

## 7. Scope

The audit certifies only:

\[
 \mathcal R^2K
 \text{ has positive-prefix/negative-tail sign order.}
\]

It also certifies the immediate corollary

\[
 \int_0^\infty t(\mathcal R^2K)(t)\,dt<0
\]

by the previously proved sign-order moment lemma.  It does **not** prove
that `R^2K` is one-well, that the same slope estimates regenerate, or that
all signed moments remain nonpositive.
