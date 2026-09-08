# Independent audit: full reflected slope and all-grid affine closure

**Date:** 2026-08-04  
**Method:** pure symbolic replay; no finite enumeration, numerical search,
remote computation, or solver.  
**Verdict:** **PASS** for the current theorem bytes.

## 1. Frozen object

The audited theorem is

`MATH_THEOREM_REFLECTED_COMPACT_SLOPE_FULL_HALF_INTERVAL_AND_ALL_GRID_AFFINE_CLOSURE_20260804.md`

with SHA-256

`2c37dfcd8d05231cd3cd60e4babe3cf1c22b54e869f716665c08511d3fcf4c2f`.

Relative to the submitted hash
`d451d46facec8a0e32c8da8784a9a2ed94c46c217f89444706e5ed9a473cec73`,
the only correction is the typographical replacement of `le` by `\le` in
the theta estimate.  No mathematical statement changed.

## 2. Independent replay of the reflected half interval

Put

\[
 h(x)=xe^{-\pi x^2/4},\qquad
 D(u)=h(1+u)-h(1-u),\qquad
 R(u)=D(1-u)-D(u).
\]

The four central terms in the bilateral theta sum give exactly

\[
 S(u)=-R(u)+T(u),\qquad
 T(u)=\sum_{k\ge2}\{h(k+u)-h(k+1-u)\}.
\]

For `1/3<u<1/2`, write `delta=1-2u`.  Since `h` decreases on
`[2,infinity)`, every summand of `T` is positive.  The first is the
integral of `-h'` over `[2+u,3-u]`, an interval of length `delta` contained
in `[7/3,8/3]`.  Direct differentiation gives

\[
 h''(x)={\pi x\over2}e^{-\pi x^2/4}
             \left({\pi x^2\over2}-3\right)>0
 \quad(7/3\le x\le8/3),
\]

so `-h'` decreases there and

\[
 T(u)\ge-\delta h'(8/3).
\]

The rational estimates in the theorem replay exactly:

\[
 -h'(8/3)=e^{-16\pi/9}(32\pi/9-1)>1/40.
\]

Indeed `32pi/9-1>29/3`, `16pi/9<28/5`, and

\[
 e^{28/5}< (11/4)^5(5/4)^3<1160/3.
\]

Poisson summation gives

\[
 S(u)=16\sum_{m\ge1}m e^{-4\pi m^2}\sin(2\pi m u).
\]

As `u=(1-delta)/2`, its sine is
`(-1)^{m+1} sin(pi m delta)`.  Hence

\[
 |S(u)|\le16\pi\delta\sum_{m\ge1}m^2e^{-4\pi m^2}.
\]

With `r=e^{-12}<10^{-5}`,

\[
 \sum_{m\ge1}m^2e^{-4\pi m^2}
 <\sum_{m\ge1}m^2r^m
 ={r(1+r)\over(1-r)^3}<1/90000.
\]

Since `16pi<51`, this yields `|S(u)|<delta/1000`.  Therefore

\[
 R(u)=T(u)-S(u)
 >\delta(1/40-1/1000)>0.
\]

Together with the frozen `0<=u<=1/3` result, this proves
`D(1-u)>D(u)` for the full `0<=u<1/2`; at `u=1/2` the arguments are
identical, so equality is literal.  No endpoint or sign reversal is
missing.

## 3. Independent replay of the affine derivative

For `n>=3`, set `h=n-1`.  Solving the affine endpoint equations gives

\[
 p=1-t,\qquad a={1-2t\over h-1},\qquad 0<t<1/n,
\]

and normalized shifts

\[
 s_0=0,\qquad s_r=t+(r-1)a\quad(1\le r<h).
\]

For `m=qh+r`, their slopes are

\[
 -q\quad(r=0),\qquad
 -q+\ell_j,quad
 \ell_j=1-{2j\over h-1},\quad j=r-1.
\]

The derivative partition in the theorem is exhaustive:

* the compact shift `t` pairs with `p=1-t`, with slopes `+1,-1`;
* for `1<=j<h-1-j<=h-2`, the compact shifts
  `t+ja` and `t+(h-1-j)a` sum to one and have slopes
  `ell_j,-ell_j`;
* the possible central compact shift is exactly `1/2` and stationary;
* at `q=1`, `p+t=1` is stationary, while every `r>=2` term has argument
  `1+(r-1)a>1` and negative slope;
* every `q>=2` term has argument greater than one and strictly negative
  slope.

The reflected theorem makes each nonstationary compact pair negative.
On the Gaussian tail `K'>0`, so all remaining nonstationary terms are
negative.  The first compact pair is always present, including `n=3`,
so the total derivative is strictly negative.  Gaussian decay supplies a
uniform summable derivative majorant on every closed subinterval of
`(0,1/n]`.

At the closure point `t=1/n`,

\[
 p=(n-1)/n,\qquad s_r=r/n,
\]

and `q(n-1)+r` runs bijectively through the nonnegative integers.  Thus
the train is exactly `C(A/n)>0`.  Strict decrease therefore gives

\[
 \Phi_n(t)>\Phi_n(1/n)>0\qquad(0<t<1/n).
\]

The limiting point corresponds to `beta=0`; using it as a comparison
endpoint does not enlarge the asserted open affine parameter family.

## 4. Scope

The proof is uniform over every integer `n>=3` and closes the complete
one-parameter affine setup-cost family.  It does not prove positivity of
arbitrary Bellman tables, any non-affine efficiency branch, or an
all-dimensional OR-word upper bound.

