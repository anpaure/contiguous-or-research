# Final independent GO audit: period twenty-three complete positivity

**Date:** 2026-08-04  
**Audited successor:**
`MATH_THEOREM_APERY_PERIOD23_FOUR_AND_SIX_TWENTYTHIRDS_COMPLETE_POSITIVITY_20260804.md`  
**Audited successor SHA-256:**
`2f8078d67c08ec37529351d57defe0e73a67779550dec31456806bcaa5c1c46f`  
**Requested predecessor SHA-256:**
`e2cca779d75c925dcca20792ac71d1d7916c4216ae4acee661d35b4f944b5c09`  
**Verdict:** **PASS / GO in the exact stated scope.**  The predecessor's
mathematics passes; the successor changes only three malformed TeX
separators (`qquad`/`quad`).  All rational exponential comparisons,
monotonicity intervals, theta/base counts, and the maximal `u=10` ledger
replay exactly.  No search or sampled computation is used.

## 1. Derivative ratios and monotonicity

At `x=4/23`, the adverse compact derivative is `h(19/23)`.  The first
two positive ratios are exactly

\[
 {h(27/23)\over h(19/23)}
 ={27\over19}e^{-4\pi/23},
\]

and

\[
 {h(50/23)\over h(19/23)}
 ={50\over19}e^{-93\pi/92}.
\]

The rational lower exponents obtained from `pi>333/106` are

\[
 {4\pi\over23}>{666\over1219},
 \qquad
 {93\pi\over92}>{30969\over9752}.
\]

The displayed degree-four and degree-six positive Taylor sums give

\[
 e^{666/1219}>{2700\over1577},
 \qquad
 e^{30969/9752}>{1250\over57},
\]

so the ratio prices `83/100` and `3/25` have the correct strict
directions.

The first successor ratio is

\[
 {h(73/23)\over h(50/23)}
 ={73\over50}e^{-123\pi/92}.
\]

Since

\[
 {123\pi\over92}>{40959\over9752},
 \qquad
 e^{40959/9752}>{219\over5},
\]

it is `<1/30`; every later successor ratio is smaller.  Thus the complete
positive/adverse ratio is

\[
 {83\over100}+{3/25\over1-1/30}
 ={2767\over2900}<1.
\]

For the first compact ratio,

\[
 {d\over dx}\log R_1(x)
 ={2\over1-x^2}-\pi
 \le {8\over3}-\pi<0
\]

on the complete interval `[4/23,1/2]`.  Every later positive/adverse
ratio has logarithmic derivative at most

\[
                         {5\over2}-{3\pi\over2}<0.
\]

Hence the endpoint comparison propagates and `f'<0` on exactly the
claimed interval.

## 2. Four-twenty-thirds value anchor

The four adverse exponents are exactly

\[
 {361\pi\over2116},\quad
 {729\pi\over2116},\quad
 {625\pi\over529},\quad
 {5329\pi\over2116}.
\]

Using `pi<355/113`, their rational upper exponents are

\[
 {128155\over239108},\quad
 {258795\over239108},\quad
 {221875\over59777},\quad
 {1891795\over239108}.
\]

Each is below 25, so the `U_24` denominator is positive.  Direct rational
cross multiplication gives the four lower Gaussian bounds

\[
 {58509\over100000},\quad
 {33879\over100000},\quad
 {61\over2500},\quad
 {9\over25000}.
\]

Over denominator `100000`, their numerator sum is

\[
                         58509+33879+2440+36=94864.
\]

Therefore

\[
                         f(4/23)<{5136\over100000}={321\over6250}.
\]

## 3. Six-twenty-thirds value anchor

The four adverse exponents are

\[
 {289\pi\over2116},\quad
 {841\pi\over2116},\quad
 {676\pi\over529},\quad
 {5625\pi\over2116},
\]

with rational upper exponents

\[
 {102595\over239108},\quad
 {298555\over239108},\quad
 {239980\over59777},\quad
 {1996875\over239108}.
\]

The exact `U_24` comparisons yield lower Gaussian numerators

\[
                         65108,\quad28687,\quad1803,\quad23
\]

over `100000`.  Their sum is `95621`, so

\[
 f(6/23)<{4379\over100000},
 \qquad
 L-V_6={234\over1000000}.
\]

All exponent substitutions use upper bounds when lower Gaussian bounds
are required; no direction is reversed.

## 4. Short chambers and base/theta ledger

The short ledgers reconstruct as

\[
\begin{array}{c|c}
u&500000\,E_{\rm low}\\ \hline
1&2L-G-2\varepsilon=16999,\\
2&3L-2G-3\varepsilon=12011,\\
3&4L-3G-4\varepsilon=7023,\\
4&5L-3G-V_4-5\varepsilon=3330.
\end{array}
\]

The `u=0` base is `L-epsilon>0`.  Through pair five, the six possible
adverse theta terms are all charged once, giving

\[
\begin{aligned}
 B_{23}
 &=6L-3G-V_4-U-6\varepsilon\\
 &={132072-80925-25680-25250-150\over500000}\\
 &={67\over500000}>0.
\end{aligned}
\]

From pair six onward, `Y_6>6/23>1/4`, so every new theta term is positive
and no further theta debit is needed.

## 5. Ordered-ray exhaustion and the `u=10` row

Ray disjointness gives `u<=10`.

* If `X_6>=1/4`, orderedness keeps every later left endpoint in the
  decreasing quarter band, so all later pairs are positive.
* If `X_6<1/4`, then `Y_6>6/23` and the monotone anchor gives pair-six
  credit `234/1000000`.
* If also `X_7<1/4`, then `Y_7>7/23>2/7` and the authenticated
  two-sevenths anchor gives credit `3194/1000000`.
* Every later unresolved pair costs at most
  `Q-L=1136/1000000`; after pair seven there are at most the three pairs
  `8,9,10`.

The maximal negative ledger is therefore exactly

\[
 {134+234+3194-3(1136)\over1000000}
 ={154\over1000000}={77\over500000}>0.
\]

Every smaller `u` deletes at least one adverse generic price.  This
exhausts all chambers `0<=u<=10`.  For reflected overlap depth at most
two, the separately frozen depth theorem already closes every `u<=139`,
so its invocation is also valid.

## 6. Scope

The audited conclusion is exactly strict positivity for honest
exact-first-carry formal period-23 cyclic Apéry clocks.  Overshoot,
later-first-crossing clocks, finite physical shoulders, arbitrary-grid
Bellman positivity, and OR-word constructions remain outside scope.

