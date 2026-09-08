# Final cross-audit: period-twenty-six sharp-depth reduction

**Date:** 2026-08-04  
**Method:** independent symbolic replay of the three new Gaussian anchors,
the sharpened overlap-depth estimate, the complete ordered chamber tree,
and both residual slack identities.  No search, solver, sampled
computation, or numerical optimization was used.

**Audited theorem:**
`MATH_THEOREM_APERY_PERIOD26_SHARP_DEPTH_AND_TWO_RESIDUAL_THRESHOLD_CHAMBERS_20260804.md`,
SHA256
`15777eb5978671af4ce685f9760fc1c2a1cef25e424cafe7deda8bc004cdee2f`.

## 0. Verdict and lineage

**FINAL GO as a reduction theorem.**  The theorem proves complete
positivity for `H<=4` and for every ordered chamber outside the two stated
residual chambers.  It does not prove either residual scalar credit and
does not claim complete period-twenty-six positivity.

The earlier SHA
`999d47fdcf57cb9a89edc738cf75178f61fd442cd1beb73ced5435c7c3c8bc58`
is excluded lineage: its mathematics was unchanged, but it did not display
the twelve finite `U_24` comparisons and did not bind the promoted floor,
terminal-suffix, and theta-sign sources separately.  The audited successor
repairs both proof-audit omissions.

## 1. Monotonicity from `2/13`

At `x=2/13`, direct differentiation of the compact train gives

\[
R_1={15\over11}e^{-2\pi/13},
\qquad
R_2={28\over11}e^{-51\pi/52}.
\]

The first positive-tail successor ratio is

\[
{41\over28}e^{-69\pi/52}.
\]

The stated positive Taylor estimates imply respectively
`17/20`, `3/25`, and `1/30`.  Hence the total positive/adverse ratio is

\[
{17\over20}+{3/25\over1-1/30}
={113\over116}<1.
\]

For the first ratio,

\[
{d\over dx}\log R_1(x)={2\over1-x^2}-\pi
\le {8\over3}-\pi<0.
\]

Every later positive/adverse ratio has logarithmic derivative at most
`5/2-3pi/2<0`.  Thus all ratios decrease on `[2/13,1/2]`, and the
monotonicity direction used throughout the chamber proof is valid.

## 2. Exact Gaussian certificate audit

For `0<z<25`, the displayed `U_24(z)` is a strict upper bound on `e^z`:
after degree 23, successive tail ratios are at most `z/25<1`.  Since
`pi<355/113`, each exponent `a*pi` is strictly below the rational argument
`a(355/113)` shown in the theorem.  Therefore

\[
U_{24}(a355/113)<{1\over r}
\quad\Longrightarrow\quad
e^{-a\pi}>r.
\]

All twelve displayed rational arguments are the exact products:

\[
\begin{array}{c|cccc}
x&\multicolumn{4}{c}{a(355/113)}\\ \hline
2/13&42955/76388&79875/76388&69580/19097&596755/76388\\
5/26&156555/305552&341155/305552&1153395/305552&2445595/305552\\
3/13&8875/19097&22720/19097&298555/76388&156555/19097.
\end{array}
\]

Expanding `U_24`, multiplying by the positive target numerator, and
clearing the positive factorial and rational denominators verifies the
twelve strict comparisons in (1.7a), (1.8a), and (1.9a).  Their resulting
lower Gaussian numerator sums are

\[
56980+35140+2610+40=94770,
\]

\[
59905+32740+2290+33=94968,
\]

and

\[
62828+30428+2007+27=95290.
\]

Consequently

\[
f(2/13)<{523\over10000},
\qquad
f(5/26)<{5032\over100000}<{63\over1250},
\qquad
f(3/13)<{471\over10000}.
\]

The reciprocal directions and every denominator are correct.  The last
anchor is the tightest of the three, but its inequality is still strict.

## 3. Global-price overlap closure

The exact reflected decomposition is

\[
E(s)=C+g(\alpha)+T+\mathcal M,
\qquad
T=\sum_i\bigl(f(X_i)-f(Y_i)\bigr),
\qquad
\mathcal M\ge0.
\]

The frozen layer-cake theorem gives

\[
T\ge-H(\sup f-C).
\]

The independently audited period-25 theorem supplies `sup f<G`, while the
promoted endpoint theorem supplies `C>L`.  The theta ray has exactly
`u+1` terms, each strictly greater than `-epsilon`.  Therefore

\[
E(s)>(H+1)L-HG-(u+1)\varepsilon.
\]

Ray disjointness gives `u<=12`.  The right-hand side decreases in both
variables, so its worst value for `H<=4` is

\[
5L-4G-13\varepsilon
={220120-213200-650\over1000000}
={6270\over1000000}>0.
\]

Thus the generic depth closure is valid and independent of the later
anchor cases.

## 4. Base ledger and chamber exhaustiveness

The first-five base is exactly

\[
6L-3G-V_4-V_5-6\varepsilon
={264144-159900-52300-50400-300\over1000000}
={1244\over1000000}.
\]

The ordered case tree is exhaustive:

1. `u<=5` is covered by this base or a stronger truncated base.
2. If `X_6>=2/13`, pair six costs at most one theta allowance and every
   later pair is positive, leaving `1194/1000000`.
3. If `X_6<2/13`, pair six costs
   
   \[
   L-V_6-\varepsilon=-{3126\over1000000}.
   \]
   
   Termination at six or crossing at seven is precisely `R_6`, with debt
   `1882/1000000`.
4. If also `X_7<2/13`, then
   
   \[
   {7\over26}>{6\over23}
   \]
   
   gives credit `234/1000000`.  Termination at seven or crossing at eight
   is precisely `R_7`, with debt `1648/1000000`.
5. If also `X_8<2/13`, then `4/13>2/7` gives credit
   `3194/1000000`, leaving `1546/1000000>0`.
6. If pair nine also remains below threshold, `9/26>1/3` gives
   `2009/375000`; charging all three possible later pairs by the generic
   quarter cost leaves
   
   \[
   3(1546)+16072-3(3408)=10486>0
   \]
   
   over denominator three million.

All threshold-crossed continuations are stronger because `f` decreases
from `2/13`, and from pair seven onward the theta terms are positive.
Therefore no chamber is omitted.  Combining this tree with Section 3
also proves that every residual table has `H>=5`.

## 5. Exact `R_6` and `R_7` slack identities

On `R_6`, the baseline is

\[
7L-(3G+V_4+V_5+V_6)-7\varepsilon
=-{1882\over1000000}.
\]

Expanding `mathcal S_6` cancels all six inserted far prices, all seven
theta allowances, and all seven inserted copies of `L`, leaving exactly

\[
C+g(\alpha)+\sum_{i=1}^{u}P_i+\mathcal M=E(s).
\]

Every term in `mathcal S_6` is nonnegative: the first six early endpoints
are pre-quarter, each far price is valid, the seven theta allowances are
valid, and any later pair has crossed the decreasing threshold and has
positive theta.

On `R_7`, the baseline is

\[
8L-(3G+V_4+V_5+V_6+4379/100000)-7\varepsilon
=-{1648\over1000000}.
\]

Here `g(Y_7)>0` because `Y_7>7/26>1/4`, so exactly seven—not eight—theta
allowances are required.  Expansion of `mathcal S_7` again yields exactly
`E(s)`, and every term is nonnegative.  Thus the two remaining sufficient
credits are precisely

\[
\mathcal S_6>{1882\over1000000},
\qquad
\mathcal S_7>{1648\over1000000}.
\]

They are not asserted by the theorem.

## 6. Dependencies and scope

All nine source hashes in the theorem match the current files.  The added
floor, terminal-suffix, and theta-sign rows support exactly the facts for
which they are cited.  The period-25 global price has its own independent
GO audit.

The proof-safe conclusion is only:

\[
\text{period 26 is positive outside }R_6\cup R_7,
\]

with the two exact scalar credit gates above inside the residual chambers.
No complete period-twenty-six, shoulder, arbitrary-period, or OR-word
claim follows.
