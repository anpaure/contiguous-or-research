# Self-audit: period-twenty-five sharp-price threshold-ray closure

**Date:** 2026-08-04  
**Target:**
`MATH_THEOREM_APERY_PERIOD25_SHARP_GLOBAL_PRICE_AND_THRESHOLD_RAY_COMPLETE_POSITIVITY_20260804.md`  
**Target SHA256:**
`61265fdf0e355aae0c6c786f9725ee639a427a1efb866fa21191ccb7b575653a`  
**Verdict:** **SELF-AUDIT GO.** This is not an independent audit.

## 0. Rejected lineage and exact repair

The drafts with SHA256 prefixes `1c1acead` and `ac693301` are rejected
lineage.  The latter incorrectly asserted `7/25>2/7`.  In fact

\[
{7\over25}<{2\over7},
\qquad
{7\over25}>{6\over23}.
\]

The authoritative successor uses the frozen six-twenty-thirds anchor at
pair seven.  Its credit is

\[
L-{4379\over100000}={234\over1000000}>0.
\]

Pair eight still legitimately uses the two-sevenths anchor, because
`8/25>2/7`.  This repair leaves the shortest displayed margin unchanged.

## 1. Sharpened global price

The critical-point test is in the correct direction: at
`t_0=589/5000`, equation (1.4) makes the unique critical point satisfy
`t_*<t_0`.  The critical envelope is increasing on this interval.  The
quantity

\[
z_0={115524693\over10600000000}

\]

is exactly `(333/106)t_0^2/4`, so the lower bound on `pi` and
`e^{-z}<1-z+z^2/2` give the stated strict upper envelope.  The final
global-price comparison reduces to

\[
{53\over24750}<{43\over20000},
\]

because

\[
53\cdot20000=1060000<1064250=43\cdot24750.
\]

Therefore

\[
{10511\over10000}-1+{53\over24750}+{1\over20000}
<{533\over10000}.
\]

On `[1/5,1/2]`, the frozen one-fifth value
`f(1/5)<101/2000<533/10000` and the frozen monotonicity theorem supply
the complementary interval.

## 2. Monotonicity from four twenty-fifths

At `x=4/25`, the first two positive/adverse ratios and first successor
ratio are exactly

\[
{29\over21}e^{-4\pi/25},\qquad
{18\over7}e^{-99\pi/100},\qquad
{79\over54}e^{-133\pi/100}.
\]

The displayed rational prices give

\[
{17\over20}+{3/25\over1-1/30}
={17\over20}+{18\over145}
={113\over116}<1.
\]

Every ratio has the required negative logarithmic derivative on
`[4/25,1/2]`.  Thus the proof uses monotonicity only inside its proved
interval.

## 3. Literal anchors

The four lower Gaussian numerators at `4/25` sum to

\[
57454+34754+2561+39=94808,
\]

giving `f(4/25)<5192/100000=649/12500`.

At `1/5`, they sum to

\[
60491+32271+2233+32=95027,
\]

giving `f(1/5)<4973/100000`.

At `6/25`, after expressing the first two values over denominator
`100000`, they sum to

\[
63530+29890+1943+26=95389,
\]

giving `f(6/25)<4611/100000`.

Every `U_24` argument is below 25.  The reciprocal direction is correct:
an upper bound on `e^z` yields the strict lower bound on `e^{-z}` used in
each adverse Gaussian ledger.

## 4. Base and short rays

The first-five base is exactly

\[
264144-159900-51920-49730-300=2294
\]

over denominator one million.  The shorter-ray lower numerators are

\[
43974,\quad34648,\quad25322,\quad15996,\quad8050,\quad2294,
\]

for `u=0,1,2,3,4,5`, respectively, and hence are all positive.

Ray disjointness is `u+1<25-u`, so `u<=11`.  Terminal maximality gives
`Y_i>i/25`.

## 5. Ordered-ray ledger after the repair

If `X_6>=4/25`, the only remaining allowance is one `epsilon`, leaving
`2244/1000000`.

If `X_6<4/25`, pair six costs

\[
L-V_6-\varepsilon=-{2136\over1000000}.
\]

Crossing at pair seven therefore leaves the true displayed bottleneck

\[
{2294-2136\over1000000}={158\over1000000}>0.
\]

If pair seven also stays below the threshold, then

\[
Y_7>{7\over25}>{6\over23}
\]

and the corrected credit is `234/1000000`.  If pair eight stays below,
then `Y_8>8/25>2/7` gives `3194/1000000`.  If pair nine stays below,
then `Y_9>9/25>1/3` gives `2009/375000`.  At most two generic quarter
costs remain.  On denominator three million the fully un-crossed ledger
is

\[
3(2294-2136+234+3194-2\cdot1136)+16072
=20014>0.
\]

All earlier terminations are stronger, so `158/1000000` remains the
minimum displayed margin.

## 6. Dependencies and scope

All five dependency hashes in the theorem match the current files.  They
are used only for the one-fifth Jacobi/monotonicity facts, the
six-twenty-thirds, two-sevenths, and one-third anchors, and the reflected
depth reduction.  The theorem is restricted to honest exact-first-carry
formal cyclic Apéry clocks and makes no physical-word claim.
