# Final cross-audit: period-24 one-sixth and five-twenty-fourths positivity

**Date:** 2026-08-04  
**Method:** independent symbolic replay of the derivative-ratio proof, both
new Gaussian anchors, every short- and far-ray ledger, the tight branch, and
the final formal-scope reduction.  No search, solver, sampled computation, or
numerical optimization was used.

**Audited theorem:**
`MATH_THEOREM_APERY_PERIOD24_ONE_SIXTH_AND_FIVE_TWENTYFOURTHS_COMPLETE_POSITIVITY_20260804.md`,
SHA256
`0c3e35f6880f0903cbe44bfed543dcdc65be4f4dea8c8032b6b57b0a7713d5ec`.

## 0. Verdict

**FINAL GO.**  The two pre-quarter anchors, monotonicity from `1/6`, the
period-24 ray geometry, all ordered branches, and the strict
`108/1000000` bottleneck are correct.  The four declared dependencies match
their frozen hashes and support exactly the inherited claims used here.  The
conclusion is correctly restricted to honest exact-first-carry formal cyclic
Apéry clocks.

## 1. Monotonicity audit

For `0<=x<=1/2`, differentiation of the literal train compares the adverse
term `h(1-x)` with the positive terms `h(m+x)`, where

\[
                         h(t)=t e^{-\pi t^2/4}.
\]

At `x=1/6`, the first two ratios are exactly

\[
 {h(7/6)\over h(5/6)}={7\over5}e^{-\pi/6},
 \qquad
 {h(13/6)\over h(5/6)}={13\over5}e^{-\pi}.
\]

The stated positive Taylor lower bounds give respectively `21/25` and
`3/25`.  The ratio from `h(13/6)` to `h(19/6)` is

\[
                         {19\over13}e^{-4\pi/3}<{1\over30}.
\]

For later successive terms the ratio decreases, since

\[
 {d\over dt}\log\left({t+1\over t}e^{-\pi(2t+1)/4}\right)
 =-{1\over t(t+1)}-\frac\pi2<0.
\]

Hence the total positive/adverse ratio is strictly below

\[
 {21\over25}+{3/25\over1-1/30}
 ={609+90\over725}={699\over725}<1.
\]

For the first individual ratio the logarithmic derivative on
`[1/6,1/2]` is at most `8/3-pi<0`.  For every later ratio it is at most
`5/2-3pi/2<0`.  Thus every ratio decreases after the anchor, proving

\[
                         f'(x)<0\qquad(1/6\le x\le1/2).
\]

No unproved monotonicity is used below this anchor.

## 2. One-sixth anchor

At `x=1/6`, the first four adverse exponents are exactly

\[
 {25\pi\over144},\quad {49\pi\over144},\quad
 {169\pi\over144},\quad {361\pi\over144}.
\]

All four rational arguments in the displayed `U_24` ledger are obtained by
substituting `pi<355/113`; all lie in `(0,25)`, so the geometric-tail
majorant defining `U_24` applies.  Expanding over positive denominators gives
the four strict Gaussian lower bounds

\[
 {57959\over100000},\quad {34334\over100000},\quad
 {2504\over100000},\quad {37\over100000}.
\]

Their sum is

\[
 57959+34334+2504+37=94834,
\]

and dropping all later adverse terms is strict.  Therefore

\[
 f(1/6)<1-{94834\over100000}
 ={5166\over100000}={2583\over50000}=V_4.
\]

## 3. Five-twenty-fourths anchor

At `x=5/24`, the first four adverse exponents are exactly

\[
 {361\pi\over2304},\quad {841\pi\over2304},\quad
 {2809\pi\over2304},\quad {5929\pi\over2304}.
\]

Again the `355/113` substitutions in the theorem are exact and below 25.
The finite positive-denominator `U_24` comparisons give lower bounds

\[
 {61125\over100000},\quad {31766\over100000},\quad
 {2170\over100000},\quad {30\over100000}.
\]

Their numerator sum is

\[
 61125+31766+2170+30=95091.
\]

Consequently

\[
 f(5/24)<1-{95091\over100000}
 ={4909\over100000}=V_5.
\]

The reciprocal directions are correct in both anchors: an upper bound on
`e^z` yields a strict lower bound on `e^{-z}`.

## 4. Ray geometry and base ledger

Ray disjointness is `u+1<24-u`, hence `u<=11`.  Terminal-suffix
maximality gives the strict cutoff

\[
                         Y_i>{i\over24}.
\]

Thus

\[
 Y_4>1/6,\qquad Y_5>5/24,\qquad Y_6>1/4,
 \qquad Y_7>7/24>2/7,\qquad Y_8>1/3.
\]

Monotonicity from `1/6` makes both new anchors eligible.  The first three
pairs use the inherited global upper price `G`.  The base train contributes
one `L`; five pairs contribute five further copies of `L`.  The initial
theta term and five paired theta terms account for exactly six possible
adverse allowances.  Therefore

\[
\begin{aligned}
B_{24}
 &=6L-3G-V_4-V_5-6\varepsilon\\
 &={264144-161850-51660-49090-300\over1000000}\\
 &={1244\over1000000}>0.
\end{aligned}
\]

The shorter ledgers, over denominator one million, are

\[
\begin{array}{c|c}
u&\text{lower numerator}\\ \hline
0&44024-50=43974\\
1&88048-53950-100=33998\\
2&132072-107900-150=24022\\
3&176096-161850-200=14046\\
4&220120-161850-51660-250=6360\\
5&1244.
\end{array}
\]

Hence every `u<=5` chamber is indeed stronger than or equal to the stated
positive base.

## 5. Complete ordered-ray exhaustion

The early ray is increasing and satisfies `X_i<=Y_i<1/2`.  Since
`Y_i>1/4` for `i>=6`, every far theta term is positive.

If `X_6>=1/4`, then every later `X_i>=1/4`; quarter-band decrease makes
each remaining pair strictly positive.  The base `1244/1000000` closes
this branch.

Suppose `X_6<1/4`.  Pair six has the valid generic price

\[
 L-Q={44024-45160\over1000000}
 =-{1136\over1000000}.
\]

If the ray terminates at `u=6`, this already gives

\[
 B_{24}+L-Q={1244-1136\over1000000}
 ={108\over1000000}>0.
\]

If `u>=7` and `X_7>=1/4`, pair seven and every later pair are strictly
positive, so the same strict lower margin applies.

Suppose `X_7<1/4`.  Since `Y_7>2/7`, the frozen two-sevenths anchor and
the monotonicity proved above give

\[
 L-V_7={44024-40830\over1000000}
 ={3194\over1000000}.
\]

Termination at `u=7`, or `X_8>=1/4`, therefore leaves at least

\[
                         {1244-1136+3194\over1000000}
 ={3302\over1000000}.
\]

Finally suppose `X_8<1/4`.  Since `Y_8>1/3`, the frozen one-third
anchor gives

\[
 L-V_8={5503\over125000}-{29\over750}
 ={2009\over375000}={16072\over3000000}.
\]

Only pairs 9, 10, and 11 can remain.  Assigning the negative generic
quarter price to all three is valid even if one has crossed the quarter,
because a crossed pair is strictly positive and hence stronger.  The worst
ledger is therefore

\[
\begin{aligned}
E(s)&>{3732-3408+9582+16072-3(3408)\over3000000}\\
&={15754\over3000000}>0.
\end{aligned}
\]

These cases include every possible early termination.  Their smallest
uniform lower bound is exactly

\[
                         {108\over1000000}={27\over250000}.
\]

The positive anchor prices beyond the quarter are used only under the
necessary hypotheses `X_7<1/4` and `X_8<1/4`; no invalid raw post-quarter
price is assigned when the left endpoint has already crossed.

## 6. Closure and scope

The frozen reflected-depth theorem closes `H<=2` because `u<=11<140`.
For the remaining depths, the base and ordered-ray cases above exhaust all
`0<=u<=11`.  The exact endpoint comparison then gives

\[
                         \Phi(W)\ge E(s)>0.
\]

This proves strict formal Bellman positivity for honest exact-first-carry
period-24 cyclic Apéry clocks only.  It does not cover threshold overshoot,
later first crossing, finite physical shoulders, or an OR-word construction.

## 7. Frozen dependency verification

The four direct dependencies exist at exactly their declared SHA256 values:

| role | SHA256 |
|---|---|
| period-23 monotonicity and ordered template | `2f8078d67c08ec37529351d57defe0e73a67779550dec31456806bcaa5c1c46f` |
| two-sevenths far anchor | `20b87ed61065d927c25f8721586cebc42df6c15d9daf56844776ccb4e94e2bb8` |
| one-third anchor | `3259e9c0c8a3f74839f5ed1cf73646395b8bebb17ea871d1d7e95e74360e2953` |
| reflected-ray depth theorem | `28c714f8eae3ae56c22a1c7c643f583e73b891e1abf2f66e4e866d831b7eb21e` |

The audited theorem remains unchanged at SHA256
`0c3e35f6880f0903cbe44bfed543dcdc65be4f4dea8c8032b6b57b0a7713d5ec`.
