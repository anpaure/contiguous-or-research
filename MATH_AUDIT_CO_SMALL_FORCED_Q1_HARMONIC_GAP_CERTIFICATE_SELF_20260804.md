# Self-audit: co-small forced-q1 harmonic gap certificate

**Date:** 2026-08-04  
**Audited theorem:**
`MATH_THEOREM_CO_SMALL_FORCED_Q1_HARMONIC_GAP_CERTIFICATE_20260804.md`

No computation or search is used.

## 1. Base-bank cases

At `B=emptyset`, `b_U=0`.  The full-owner indicator in the exact gap
formula fires exactly at `g_U=0`; the unprotected almost-full indicator
fires exactly at `g_U=1`.  This gives (1.1).  Since every summand is
nonnegative, its vanishing is exactly the pair of implications (1.2).

## 2. Owner-wise charging

At a full optional gap, `b_U=g_U`, the charge

\[
 \sum_{x\in B\cap N(U)}{c_U\over g_U}=c_U
\]

is exact.  At an unprotected almost-full gap, `c_U=2` and
`b_U=g_U-1`.  The base condition excludes `g_U=1`, and for `g_U>=2`,

\[
 {2(g_U-1)\over g_U}\ge1.
\]

These are the only two terms in `Omega`; therefore summing and reversing
the incidence order proves (2.2).  No owner is charged twice for one
simultaneous state, since full and almost-full indicators are mutually
exclusive.

## 3. Mean-two identity

Every owner has exactly `g_U` facets outside `Z`.  Its contribution after
reversing the harmonic sum is `c_U` when `g_U>0`.  When `g_U=0`, the base
condition forces `c_U=0`, so no term is missing.

The total residual owner capacity is

\[
 \sum_Uc_U=2|\mathcal U|-|E(P)|.
\]

Because the shores have equal size and the incidence-lift lower bank has
`2|Z|=|E(P)|`, this is exactly `2|mathcal L-Z|`.  Hence the average is two.
Pointwise upper bound two is therefore equivalent to equality everywhere,
as stated.

## 4. Scope

The theorem supplies a sufficient fractional charging certificate; it
does not claim the pointwise harmonic condition for the current
constant-spread reservoir.  Its exact-mean result shows why ordinary
average spread cannot establish that condition.

## 5. Mechanical checks

At freeze time, display-math delimiter balance is zero, no hidden control
byte is present, and `git diff --check` reports no whitespace errors.

