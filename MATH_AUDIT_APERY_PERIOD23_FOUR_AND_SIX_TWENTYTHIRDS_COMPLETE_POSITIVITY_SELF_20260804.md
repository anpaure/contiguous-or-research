# Self-audit: period twenty-three anchor closure

**Date:** 2026-08-04  
**Target:**
`MATH_THEOREM_APERY_PERIOD23_FOUR_AND_SIX_TWENTYTHIRDS_COMPLETE_POSITIVITY_20260804.md`  
**Target SHA256:**
`2f8078d67c08ec37529351d57defe0e73a67779550dec31456806bcaa5c1c46f`  
**Verdict:** **SELF-AUDIT GO.**  This is not an independent audit.

## 1. Derivative ledger

At `x=4/23`, the first two positive/adverse ratios are exactly

\[
{27\over19}e^{-4\pi/23},\qquad
{50\over19}e^{-93\pi/92}.
\]

The displayed rational Taylor comparisons price them by `83/100` and
`3/25`.  The first successor ratio is

\[
{73\over50}e^{-123\pi/92}<{1\over30},
\]

and all later successor ratios are smaller.  Therefore the complete ratio
is below

\[
{83\over100}+{3\over25}{30\over29}
={2767\over2900}<1.
\]

The logarithmic derivatives of every individual ratio are negative from
`4/23` onward, so `f'<0` on the entire required half interval.

## 2. Endpoint anchors

At `4/23`, the four lower Gaussian numerators over `100000` are

\[
58509,\quad33879,\quad2440,\quad36,
\]

whose sum is `94864`.  Hence

\[
f(4/23)<{5136\over100000}={321\over6250}.
\]

At `6/23`, the four lower Gaussian numerators over `100000` are

\[
65108,\quad28687,\quad1803,\quad23,
\]

whose sum is `95621`.  Hence

\[
f(6/23)<{4379\over100000}.
\]

All exponent directions use the upper bound `pi<355/113`; all denominators
in `U_24` are positive because every rational exponent is below 25.

## 3. Base and far-ray arithmetic

Over denominator `500000`, the first-five-pair base is

\[
6L-3G-V_4-U-6\varepsilon
=132072-80925-25680-25250-150=67.
\]

The new sixth-pair credit over denominator one million is

\[
L-V_6=44024-43790=234.
\]

The seventh-pair two-sevenths credit is `3194`, and every remaining
quarter pair costs at worst `1136`.  Thus the maximal `u=10` ledger is

\[
134+234+3194-3(1136)=154>0.
\]

The ordered cases never charge a positive anchor price after the relevant
left endpoint crosses the quarter.

## 4. Exhaustion and scope

Ray disjointness gives `u<=10`.  The short ledgers through `u=4`, the
positive `u=5` base, and the nested cases for `u=6,...,10` exhaust the
ray geometry.  Depth at most two is already covered by the general depth
theorem.  The result remains formal and exact-first-carry only.
