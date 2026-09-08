# Final independent GO audit of the monotone anchor-grid ray ledger

**Date:** 2026-08-04  
**Audited source:**
`MATH_LEMMA_APERY_MONOTONE_ANCHOR_GRID_RAY_LEDGER_20260804.md`  
**Audited SHA256:**
`2f83517aee645bfacb1b50b8b462cbe0436b5055b0d4c3b5ead05ef598ab2f3f`

## Verdict

**PASS / GO in the exact stated scope.**  The successor repairs the positive
anchor-price error identified in the fail-closed audit, repairs the
below-quarter proof sentence, and removes the unstated monotonicity
assumption on the numerical anchor bounds.  The finite-grid ledger and the
priced-majorant all-period sufficient condition now follow exactly from
the displayed hypotheses.

This is a reduction theorem only.  It does not itself establish the
uniform quadrature inequality, all-period positivity, physical shoulder
control, integral carrier rounding, common-cap compilation, or an OR-word
upper bound.

## 1. One-pair lemma

Let

\[
P(X,Y)=f(X)-f(Y)+g(Y),\qquad 0<X\le Y<1/2.
\]

### 1.1 Anchor below the quarter

Assume `t_j<1/4` and `Y>t_j`.

If `X<t_j`, the floor, anchor upper bound, monotonicity, and theta bound
give

\[
P(X,Y)>L-V_j-\varepsilon.
\]

If `X>=t_j`, monotonicity gives `f(X)-f(Y)>=0`, and
`g(Y)>-epsilon`.  Since

\[
f(t_j)>L,\qquad f(t_j)<V_j,
\]

we have `L-V_j-epsilon<-epsilon`, hence again

\[
P(X,Y)>-\varepsilon>L-V_j-\varepsilon.
\]

This proves the first clipped price in (1.1).  The successor explicitly
contains this missing argument.

### 1.2 Anchor at or above the quarter

Assume `t_j>=1/4` and `Y>t_j`.

If `X<1/4`, then `f(X)>L`, `f(Y)<V_j`, and `g(Y)>0`, so
`P(X,Y)>L-V_j`.  If `X>=1/4`, quarter-band decrease gives
`f(X)-f(Y)>=0`, and positive theta gives `P(X,Y)>0`.  Therefore

\[
P(X,Y)>\min\{0,L-V_j\}.
\]

This correctly clips the positive raw `2/7` price.  In particular, the
invalid inference exposed by the prior audit can no longer occur.

### 1.3 Global anchor

If `X<1/4`, the global upper bound and adverse-theta allowance give
`P(X,Y)>L-V_*-epsilon`.  If `X>=1/4`, quarter monotonicity and positive
theta give `P(X,Y)>0`.  Thus (1.2) is exact.

## 2. Strict endpoint eligibility

Terminal-suffix maximality gives

\[
Y_i>{i\over h}.
\]

Every anchor with `t_j<=i/h` is consequently legal, including equality at
the grid point.  The successor permits any eligible anchor and chooses one
with largest clipped price, equivalently a smallest theta-priced upper
bound.  No monotonicity of the sequence `V_j` is assumed or needed.

## 3. Finite-grid summation

The endpoint comparison is

\[
E(s)=C+g(\alpha)+\sum_iP(X_i,Y_i)+\sum_r f(s_r/A),
\qquad \Phi(W)\ge E(s).
\]

Using `C>L`, `g(alpha)>-epsilon`, and the independently valid clipped
price for each pair yields

\[
E(s)>L-\varepsilon+\sum_i p_i+\sum_r f(s_r/A).
\]

The retained middle train is positive in the authenticated Apéry setting.
Therefore a strictly positive ray-only ledger is sufficient, and any
retained middle or overlap/theta credit can only strengthen it.

The source now correctly separates the period-twenty-one ordered-ray
improvement from the unconditional grid.  The raw positive `2/7` credit is
used only when `X_6<1/4`; when `X_6>=1/4`, orderedness puts the later pairs
in the decreasing quarter interval and supplies positivity instead.

## 4. Priced majorant

For a grid point `t`, every anchor `t_j<=t` is eligible for a pair with
`Y>t`.  Its theta-priced upper value is

\[
b_j=V_j+\varepsilon\mathbf 1_{t_j<1/4},
\]

while the global value is `V_*+epsilon`.  Hence the best clipped price is

\[
\min\{0,L-B(t)\},
\]

where `B(t)` is exactly (4.1).  The anchor grid is finite, so the displayed
infimum is attained; no limiting strictness issue arises.

Substitution at `t=i/h` proves that

\[
L-\varepsilon+
\sum_{i=1}^{u}\min\{0,L-B(i/h)\}>0
\]

is a sufficient ray-only all-period criterion.  The same statement with
retained positive middle and overlap-depth credits is also sufficient.
The lemma does not claim that this uniform discrete/Riemann-sum inequality
has already been established.

## 5. Scope discipline

The final paragraph confines the result to honest exact-first-carry formal
cyclic Apéry clocks.  It expressly excludes overshoot, later first
crossing, finite physical shoulders, integral carrier rounding, common-cap
compilation, and an OR-word upper bound.  No broader conclusion is licensed
by this audit.

## Final disposition

The successor SHA above is proof-safe and may be promoted in its stated
scope.  The earlier SHA
`8b696e0a2ec971924fb24b6b3cb7498ce4c8ba1164e3f7f21eef21ea9a256d07`
remains fail-closed lineage because it assigned the un-clipped positive
`2/7` price to every above-quarter pair.
