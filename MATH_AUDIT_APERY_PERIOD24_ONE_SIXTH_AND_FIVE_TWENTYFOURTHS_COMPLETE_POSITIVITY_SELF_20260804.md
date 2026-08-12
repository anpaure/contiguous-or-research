# Self-audit: period twenty-four anchor closure

**Date:** 2026-08-04  
**Target:**
`MATH_THEOREM_APERY_PERIOD24_ONE_SIXTH_AND_FIVE_TWENTYFOURTHS_COMPLETE_POSITIVITY_20260804.md`  
**Target SHA256:**
`0c3e35f6880f0903cbe44bfed543dcdc65be4f4dea8c8032b6b57b0a7713d5ec`  
**Verdict:** **SELF-AUDIT GO.**  This is not an independent audit.

## 1. Monotonicity

At `1/6`, the first two ratios are exactly

\[
{7\over5}e^{-\pi/6},\qquad {13\over5}e^{-\pi},
\]

and the first successor ratio is

\[
{19\over13}e^{-4\pi/3}.
\]

The stated prices give the complete ratio

\[
{21\over25}+{3\over25}{30\over29}={699\over725}<1.
\]

Every individual ratio decreases afterward, proving the required
monotonicity interval.

## 2. Rational anchors

At `1/6`, the four Gaussian lower numerators over `100000` are

\[
57959,quad34334,quad2504,quad37,
\]

with sum `94834`.  Hence `f(1/6)<5166/100000=2583/50000`.

At `5/24`, the four lower numerators are

\[
61125,quad31766,quad2170,quad30,
\]

with sum `95091`.  Hence `f(5/24)<4909/100000`.

Every `U_24` argument is below 25 and uses the correct upper exponent from
`pi<355/113`.

## 3. Ordered ledger

The first-five base over denominator one million is

\[
264144-161850-51660-49090-300=1244.
\]

If pair six pays the quarter cost and pair seven has already crossed the
quarter, the remaining margin is

\[
1244-1136=108.
\]

If pair seven remains below the quarter, it earns `3194`; if pair eight
also remains below, it earns `2009/375000`.  In the maximal `u=11` branch,

\[
3732-3408+9582+16072-3(3408)=15754>0
\]

over denominator three million.  Thus `108/10^6=27/250000` is the true
smallest displayed margin.

## 4. Scope

Ray disjointness gives `u<=11`; the ordered cases exhaust it.  The theorem
is formal exact-first-carry only and makes no physical-word claim.
