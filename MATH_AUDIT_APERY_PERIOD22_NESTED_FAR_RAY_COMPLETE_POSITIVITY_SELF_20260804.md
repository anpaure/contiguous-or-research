# Self-audit: period-twenty-two nested far-ray closure

**Date:** 2026-08-04  
**Audited theorem:**  
`MATH_THEOREM_APERY_PERIOD22_NESTED_FAR_RAY_COMPLETE_POSITIVITY_20260804.md`  
**Verdict:** **PASS / GO.**  The rational anchors, base ledger, nested
ordered-ray cases, maximal `u=10` margin, and first period-twenty-three
frontier replay exactly.  No computation or search is used.

## 1. Anchor ledgers

At `2/11`, the four Gaussian lower certificates sum to

\[
{11819\over20000}+{3337\over10000}
+{237\over10000}+{7\over20000}
={94870\over100000}.
\]

Thus `f(2/11)<513/10000`.  The derivative ratio at the anchor is below

\[
{83\over100}+{11/100\over1-1/30}
={2737\over2900}<1,
\]

and each ratio decreases afterward, so the required monotonicity interval
is valid.

At `3/11`, the adverse lower sum is

\[
{3299\over5000}+{7\over25}+{43\over2500}+{1\over5000}
={9572\over10000},
\]

so `f(3/11)<107/2500`.

The two far credits over denominator one million are

\[
L-V_6=44024-42800=1224,
\qquad
L-V_7=44024-40830=3194.
\]

## 2. Base arithmetic

The first five pairs at period twenty-two cost three global prices, one
`2/11` price, one one-fifth price, and six theta allowances.  Over
denominator `500000`,

\[
6L-3G-V_4-U-6\varepsilon
=132072-80925-25650-25250-150=97.
\]

Thus `B_22=97/500000=194/1000000`.

## 3. Ordered cases

If `X_6>=1/4`, all later pairs are positive.  If `X_6<1/4`, pair six
earns `1224/1000000`.  If then `X_7>=1/4`, all still later pairs are
positive.  If `X_7<1/4`, pair seven earns `3194/1000000` and at most
three quarter-priced pairs remain.

The maximal adverse case is therefore

\[
194+1224+3194-3(1136)=1204,
\]

or `301/250000`, strictly positive.  No branch applies a positive anchor
price after its left endpoint has crossed the quarter.

## 4. Exhaustion and next break

Ray disjointness gives `u<=10`.  The nested cases cover all
`5<=u<=10`; the earlier `u=3,4` rows are already positive.  The `H<=2`
scalar is at most `731<860`.

At period twenty-three, the current anchor set no longer reaches pair
four because `4/23<2/11`.  The first `u=5` ledger is

\[
6L-4G-U-6\varepsilon=-{307\over125000}.
\]

Replacing its fourth global price requires exactly

\[
f(4/23)<{25747\over500000}.
\]

This is a sufficient method gate, not a negative-clock claim.

**Final audit verdict:** **PASS / GO.**
