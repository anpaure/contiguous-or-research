# Independent-style audit: smooth binomial configuration dual and ceiling prices

**Date:** 2026-08-04
**Audited file:** `MATH_THEOREM_SMOOTH_BINOMIAL_CONFIGURATION_DUAL_AND_CEILING_PRICE_CLASSES_20260804.md`
**Verdict:** PASS for the stated reduction and price classes.  The file does not prove the all-price configuration inequality.

## 1. Covering semantics

The physical configuration constraint is total selected capacity at least
the job length.  Under this convention the dynamic-programming closure is
monotone and subadditive.  The idempotent replacement
`theta_u -> psi_theta(u)` is valid: every new part can be expanded into an
old optimal cover, and every old cover remains available.  This explicitly
excludes the nonmonotone residue examples created by an equality-only coin
equation.

The converse is claimed only on `ell<=d`, where the one-part cover exists;
it is not overclaimed for arbitrary `ell>d`.

## 2. Discrete tails

From `n_ell=H_(t-ell)`,

\[
 \sum_{\ell\ge q}n_\ell=\sum_{b\le t-q}H_b=C_{t-q}.
\]

From `m_u=H_(t+u)+1`,

\[
 \sum_{u\ge q}m_u=W-C_{t+q-1}+d-q+1.
\]

Thus the signed-tail summation-by-parts formula is correct.  The sole
punctured-empty-set correction changes one job length by one and is within
the declared `O(psi(t))` bound.

## 3. Gaussian kernel

The limiting job tail is `exp(-(A+y)^2)`.  The limiting socket tail is
`1-exp(-(A-y)^2)` on `0<=y<=A` and zero afterward.  Their difference is
exactly (3.1).  Its integral is zero because both measures have first
moment

\[
 \int_A^\infty e^{-z^2}\,dz
 =A-\int_0^A e^{-z^2}\,dz.
\]

For the crossing proof, the logarithmic derivative of
`2 exp(-A^2-y^2) cosh(2Ay)` is correct.  Strict concavity of
`A tanh(2Ay)-y`, together with its endpoint signs, gives one maximum of
the Gaussian sum.  Since the sum starts below one and ends above one, its
crossing of one is unique.  Weighting this single-crossing zero-area kernel
by a decreasing concave derivative proves the stated concave-price order.

## 4. Ceiling calculation

For `a=A/q`, tail-summing `ceil(X/a)` gives

\[
 D_q=q-e^{-A^2}-\sum_{j\ge1}e^{-(ja)^2}.
\]

Poisson summation gives

\[
 \sum_{j\ge1}e^{-(ja)^2}
 =q\left(1+2\sum_{m\ge1}e^{-4\pi q^2m^2}\right)-{1\over2},
\]

and hence the displayed formula (4.2).  Its positivity is uniform for
`q>=1`: the correction is largest at `q=1` and exponentially smaller than
`1/2-exp(-pi/4)`.  For a completely elementary separation, use
`pi/4>3/4` and the exponential series to get
`1/2-exp(-pi/4)>0.02`, while

\[
 {2e^{-4\pi}\over1-e^{-12\pi}}<0.001.
\]

The discrete passage is legitimate because the ceiling cost is bounded by
a constant times `1+x` after Gaussian scaling; Gaussian tails give uniform
integrability.  Rounding `a_r` and the one puncture are `o(W)` against the
strict `D_q W` margin.

## 5. Scope

The proved price cone contains the linear volume ray, every globally
concave profile, every fixed reciprocal ceiling ray, and fixed
nonnegative combinations of them.  It does not establish that these are
all extreme rays of the finite covering/subadditive cone.  In particular,
mixed efficient denominations can create fixed macroscopic or changing
renewal patterns not covered by the theorem.  Those patterns are correctly
retained as the remaining fractional configuration gate.
