# Direct proof audit: long-wrap outer periods and compact theta core

**Date:** 2026-08-04  
**Verdict:** **GO as a reduction.**  The two outer-period closures, the
convex endpoint arguments, and the normalized residual system replay
symbolically.  This is an author-side direct audit, not an independent
audit and not a sign certificate for the final theta core.

## 1. Origin derivative

At `x=0`, the `q=0` positive term cancels `h(1)`, leaving exactly

\[
 T_\rho(0)=\sum_{q\ge1}h(1+q\rho)-h(1-\rho).
\]

The first/low ratio is (1.3).  On `[1/2,3/5]` its logarithmic derivative
is negative.  On `[3/5,4/5]` that derivative is increasing, so its
maximum is at an endpoint.  The successive-term bounds are uniform and
the geometric factors `8/5` and `4/3` are in the correct direction.
Thus no positive tail term is omitted from Lemma 1.1.

## 2. Lower-period closure

For `rho<=3/5`, the upper endpoint is `a=P/3`.  Both shift derivatives
there lie in the authenticated density-tie wedge.  Since `Q_P'` is
strictly convex and negative at both endpoints, it is negative everywhere.

For `3/5<=rho<=4/5`, the upper endpoint is `(A-P)/2`.  Strict convexity
of `F_P'`, together with negativity at `0` and `A-P`, makes `F_P'`
negative on the entire shift interval.  The formula for

\[
 U(\rho)=F_P'(A-P)/(2A)
\]

is exact.  Its derivative (3.5) includes all weighted tail terms, and the
rational bounds give `U'>1/4`; since `U(4/5)<0`, the endpoint sign holds
throughout the interval.  Hence `Q_P` decreases to the already-signed
threshold face.

## 3. Upper-period closure

For `r=1-rho<=1/12`, the compact difference `D(x)` is bounded below by
`-x`, the first shifted positive term by `h(2)`, and the remaining adverse
term by `r-x`.  Every omitted `q>=2` term is positive.  Thus

\[
 T_\rho(x)>2e^{-\pi}-r>0.
\]

Both arguments `a/A` and `2a/A` lie in `[0,r]`, so `Q_P'>0` and its
minimum is the arithmetic boundary `a=0`.

## 4. Residual curve

The surviving band and KKT equations are literal normalizations of the
frozen system.  Equation (5.4) retains the weights `q` from period
differentiation.  For fixed `rho`, strict convexity leaves at most one
local-minimum root `x_*`, so (5.6) is genuinely one-dimensional.  No
claim is made for its sign.

