# Self-audit: period-26 residual middle-anchor collapse

**Date:** 2026-08-04  
**Target:**
`MATH_THEOREM_APERY_PERIOD26_RESIDUAL_MIDDLE_ANCHOR_AND_HIGH_DEPTH_COLLAPSE_20260804.md`  
**Target SHA256:**
`497e59d075f6af97fb64d2f5a62e6843e97bced41b837ca14159e9fb60e448c1`  
**Verdict:** **SELF-AUDIT GO as a reduction theorem.**  This is not an
independent audit and makes no complete period-26 claim.

## 1. Middle anchor

At `x=6/13`, the four displayed exponents are exactly those of
`1-x,1+x,2+x,3+x`.  Using the lower rational value `333/106` for `pi`,
the positive Taylor comparisons give the upper Gaussian prices

\[
{797\over1000},\qquad {47\over250},\qquad
{1\over100},\qquad {1\over10000}.
\]

The next exponent is already larger than `280053/17914>15`; the first
tail term and its geometric successor ratio give total tail less than
`1/10000`.  Therefore

\[
f(6/13)>1-.797-.188-.01-.0001-.0001
=.0048={3\over625}>{1\over250}.
\]

The frozen critical-point theorem says every interior critical point on
`[0,1/2]` is a strict maximum.  Since `C>1/250`, the minimum on
`[0,6/13]` is larger than `1/250`.

## 2. Forced middle position

Prefix averaging gives

\[
{s_r\over A}\le {r(1-\alpha)\over26}<{r\over26}.
\]

For `6<=u<=10`, the first middle index is `r=u+2`, so `8<=r<=12` and

\[
{s_r\over A}<{12\over26}={6\over13}.
\]

Thus the literal middle train contributes more than `1/250=4000/10^6`.
Subtracting the two authenticated debts gives respectively

\[
4000-1882=2118,
\qquad
4000-1648=2352,
\]

both strictly positive.  Hence both residual chambers close through depth
ten.

## 3. Depth-eleven rail

At `u=11`, the middle indices are exactly 13 and 14.  Minimum-gap spacing
gives `s_14-s_13>=alpha A`, while depth gives `s_14<=A/2`; hence

\[
{s_{13}\over A}\le {1\over2}-\alpha.
\]

Both residual chambers have `X_6>=7alpha` and `X_6<2/13`, so
`alpha<2/91` and `1/2-alpha>1/3`.  Decrease from the proved compact
threshold and the one-third anchor give

\[
f(1/2-\alpha)<f(1/3)<L<C.
\]

The strict-maximum classification therefore places the two relevant
interval minima at `1/2-alpha` and `1/2`, proving the stated central-rail
lower bound.  No positive constant is asserted as `alpha` tends to zero.

## 4. Scope

The result leaves only `u=11,12`, `H>=5`, and chambers `R_6,R_7`.
At `u=11` it retains the exact two-point central rail; at `u=12` the
middle train is empty.  All five dependency hashes match the cited files.
