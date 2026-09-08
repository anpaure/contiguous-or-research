# Cross-audit: periods fifteen through twenty promoted ray ledgers

**Date:** 2026-08-04  
**Method:** independent symbolic and rational audit only; no search, numerical
experiment, or computational construction.

**Audited theorem:**
`MATH_THEOREM_APERY_PERIOD15_20_PROMOTED_RAY_LEDGER_COMPLETE_POSITIVITY_20260804.md`,
SHA256
`876c12340cad4755c5c0e571525fdf48456fe1c31bc934894d9e451abf4f0e3b`.

## 0. Verdict

**GO.**  Every threshold-table row, theta allowance, chamber range, and
rational margin is correct.  The worst certified margin on `15<=h<=20` is
indeed `23/12500` at `(h,u)=(20,9)`.  The period-twenty-one method-break
row and the replacement-anchor scalar are also exact.  No theorem repair is
needed.

## 1. Constants and incremental price

On denominator `500000`, the promoted constants are

\[
 L={22012\over500000},\quad
 G={26975\over500000},\quad
 U={25250\over500000},
\]

\[
 Q={22580\over500000},\quad
 \varepsilon={25\over500000}.
\]

Thus adding a quarter-priced pair changes a ledger by

\[
                         L-Q=-{568\over500000}.
\tag{1.1}
\]

The promoted floor itself is the already audited endpoint argument:
`f(0)>L`, `f(1/4)>L`, and every interior critical point on the interval is
a strict maximum.  The three pair prices use their anchors in the correct
directions:

* global: `L-G-epsilon`;
* one fifth: `L-U-epsilon` when `Y>1/5`;
* quarter: `L-Q` when `Y>1/4`, with positive theta and no `epsilon` cost.

## 2. Exact threshold table

Ray disjointness gives

\[
 u+1<h-u
 \quad\Longleftrightarrow\quad
 2u<h-1,
\]

so

\[
                         u_{\max}(h)=\left\lfloor{h-2\over2}\right\rfloor.
\tag{2.1}
\]

The terminal envelope is strict:

\[
 Y_i>{i\over h}.
\]

Therefore the first guaranteed one-fifth index is `ceil(h/5)`, and the
first guaranteed quarter index is `ceil(h/4)`.  Equality of `i/h` with an
anchor is sufficient because the displayed envelope is strict.  This gives

\[
\begin{array}{c|c|c|c}
h&u_{\max}&\min\{i:Y_i>1/5\}&\min\{i:Y_i>1/4\}\\ \hline
15&6&3&4\\
16&7&4&4\\
17&7&4&5\\
18&8&4&5\\
19&8&4&5\\
20&9&4&5.
\end{array}
\tag{2.2}
\]

Every row of the theorem's threshold table is therefore exact.

## 3. Period fifteen ledger

Pairs one and two are global, pair three is one-fifth, and every later pair
is quarter-priced.  Including `g(alpha)`, the adverse theta count is

\[
                         2+1+1=4.
\]

Hence

\[
 E(s)>(u+1)L-2G-U-(u-3)Q-4\varepsilon.
\]

By (1.1) this decreases with `u`, so the worst row is `u=6`.  Its numerator
is

\[
 7(22012)-2(26975)-25250-3(22580)-4(25)=7044,
\]

and

\[
                         {7044\over500000}={1761\over125000}>0.
\]

## 4. Period sixteen ledger

The first three pairs are global.  Pair four and every later pair are
already beyond the quarter.  The only adverse theta terms are the three
global pair terms and `g(alpha)`, again four.  Thus

\[
 E(s)>(u+1)L-3G-(u-3)Q-4\varepsilon.
\]

The decrement is again (1.1), so `u=7` is worst.  Its numerator is

\[
 8(22012)-3(26975)-4(22580)-4(25)
 =176096-80925-90320-100=4751>0.
\]

## 5. Periods seventeen through twenty

Here pairs one through three are global, pair four is one-fifth, and pairs
from five onward are quarter-priced.  The adverse theta count is

\[
                         3+1+1=5,
\]

where the final one is `g(alpha)`.  Therefore, for `u>=4`,

\[
 E(s)>(u+1)L-3G-U-(u-4)Q-5\varepsilon.
\tag{5.1}
\]

The separate `u=3` row has three global pairs plus `g(alpha)` and equals

\[
 4L-3G-4\varepsilon
 ={88048-80925-100\over500000}
 ={7023\over500000}>0.
\]

At `u=4`, equation (5.1) has numerator

\[
                         5(22012)-80925-25250-125=3760.
\tag{5.2}
\]

Each later pair subtracts `568`.  At the maximal chambers this gives

\[
\begin{array}{c|c|c|c}
h&u_{\max}&\text{numerator over }500000&\text{reduced margin}\\ \hline
17&7&3760-3(568)=2056&257/62500\\
18&8&3760-4(568)=1488&93/31250\\
19&8&3760-4(568)=1488&93/31250\\
20&9&3760-5(568)=920&23/12500.
\end{array}
\tag{5.3}
\]

All rows are positive, and `920/500000` is the smallest displayed margin
in the full period range.

## 6. `H/u` exhaustion

Always `H<=u`.  If `H<=2`, then throughout `15<=h<=20`,

\[
 \tau\le u+1\le10,
 \qquad
 360H+\tau\le720+10=730<860.
\]

The reflected-depth theorem closes every such chamber, including all cases
with `u<3`.

If `H>=3`, then `u>=3`.  Period fifteen is covered for every `3<=u<=6`,
period sixteen for every `3<=u<=7`, and periods seventeen through twenty by
the separate `u=3` row plus (5.1) through the corresponding maxima in
(5.3).  No integer `u` chamber remains.

The positive middle trains are discarded only after the exact ray identity,
so their omission cannot weaken any lower bound incorrectly.  Finally
`Phi(W)>=E(s)` transfers each strict margin.

## 7. Exact period-twenty-one method break

For `h=21`,

\[
                         u_{\max}=\left\lfloor{19\over2}\right\rfloor=9.
\]

The strict envelope gives

\[
 Y_4>{4\over21}<{1\over5},\qquad
 Y_5>{5\over21}>{1\over5},\qquad
 Y_6>{6\over21}={2\over7}>{1\over4}.
\]

The first two inequalities intentionally say that `Y_4` is guaranteed only
past `4/21`, not past one fifth.  At `u=5`, the decoupled method must price
four pairs globally and only pair five at one fifth.  Together with
`g(alpha)`, this spends six theta allowances:

\[
 6L-4G-U-6\varepsilon
 ={132072-107900-25250-150\over500000}
 =-{1228\over500000}
 =-{307\over125000}.
\tag{7.1}
\]

The preceding rows at `u=3,4` remain positive, so this is the first
nonpositive row of this decoupled ledger, not a counterexample clock.

If pair four has a uniform upper bound `f(Y_4)<V` from the `4/21` anchor,
then its replacement price is `L-V-epsilon`.  The `u=5` ledger becomes

\[
                         6L-3G-U-V-6\varepsilon,
\]

which is positive exactly when

\[
 \boxed{
 V<6L-3G-U-6\varepsilon
 ={25747\over500000}.}
\tag{7.2}
\]

This condition needs only a uniform upper bound for `Y>=4/21`: if
`X<1/4`, use the promoted floor and that bound; if `X>=1/4`, quarter
decrease and positive theta are stronger.  No unproved monotonicity from
`4/21` to `1/5` is being assumed.

For `(h,u)=(21,5)`, the middle range is

\[
                         7\le r\le15,
\]

containing exactly nine strictly positive trains.  The theorem correctly
records them only as a possible future correlated credit and does not spend
them in (7.1).

Thus period twenty-one is the exact scalar frontier of the present
independent-pair ledger, while the honest exact-first-carry positivity
question itself remains open there.

