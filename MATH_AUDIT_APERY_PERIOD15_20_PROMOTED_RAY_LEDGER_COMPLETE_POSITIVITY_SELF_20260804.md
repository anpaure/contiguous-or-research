# Self-audit: periods fifteen through twenty promoted-ray closure

**Date:** 2026-08-04  
**Audited theorem:**  
`MATH_THEOREM_APERY_PERIOD15_20_PROMOTED_RAY_LEDGER_COMPLETE_POSITIVITY_20260804.md`  
**Verdict:** **PASS / GO.**  The forced anchors, maximal ray counts,
piecewise ledgers, worst margin, and first period-twenty-one scalar break
all replay exactly.  No computation or search is used.

## 1. Maximal rays and forced anchors

From `2u<h-1`,

\[
u_{\max}(15),\ldots,u_{\max}(20)=6,7,7,8,8,9.
\]

The first index forced past a fraction `c` is `ceil(ch)`, because the
terminal estimate is strict.  Therefore:

\[
\begin{array}{c|cccccc}
h&15&16&17&18&19&20\\ \hline
\text{first }Y_i>1/5&3&4&4&4&4&4\\
\text{first }Y_i>1/4&4&4&5&5&5&5.
\end{array}
\]

This agrees with the theorem's three regimes.

## 2. Common rational ledger

Over denominator `500000`,

\[
L=22012,\qquad G=26975,\qquad U=25250,\qquad Q=22580,
\qquad\varepsilon=25.
\]

Hence one added quarter pair changes the numerator by

\[
L-Q=22012-22580=-568.
\]

### Period fifteen

At `u=3`,

\[
4L-2G-U-4\varepsilon
=88048-53950-25250-100=8748.
\]

At `u=6`, subtract three quarter increments:

\[
8748-3\cdot568=7044,
\]

giving `1761/125000`.

### Period sixteen

At `u=3`,

\[
4L-3G-4\varepsilon
=88048-80925-100=7023.
\]

At `u=7`, subtract four quarter increments:

\[
7023-4\cdot568=4751,
\]

giving `4751/500000`.

### Periods seventeen through twenty

At `u=4`,

\[
5L-3G-U-5\varepsilon
=110060-80925-25250-125=3760.
\]

Thus the maximal numerators are

\[
\begin{array}{c|c}
h&\text{numerator over }500000\\ \hline
17&3760-3(568)=2056\\
18&3760-4(568)=1488\\
19&3760-4(568)=1488\\
20&3760-5(568)=920.
\end{array}
\]

They reduce respectively to

\[
{257\over62500},\quad
{93\over31250},\quad
{93\over31250},\quad
{23\over12500}.
\]

The smallest is the last and is positive.

## 3. Theta and chamber accounting

In the period-fifteen regime, only `g(alpha),g(Y_1),g(Y_2),g(Y_3)` can
be adverse: four charges.  Period sixteen has the same four charges.
For periods seventeen through twenty, pair four is after one fifth but
before the quarter, so `g(Y_4)` may also be adverse: five charges.

If `H>=3`, then `u>=3`, and the ledgers above cover every allowed `u`.
If `H<=2`, the uniform worst scalar is

\[
720+(9+1)=730<860.
\]

No chamber is omitted.

## 4. Period-twenty-one frontier

At `h=21`, the first one-fifth and quarter indices are five and six.
At `u=5`, the present numerator is

\[
6L-4G-U-6\varepsilon
=132072-107900-25250-150=-1228,
\]

or `-307/125000`.

Replacing the fourth global upper price `G` by an anchor price `V`
requires

\[
V<6L-3G-U-6\varepsilon.
\]

The right side is

\[
{132072-80925-25250-150\over500000}
={25747\over500000}.
\]

This is an exact sufficient scalar gate, not a claim that period twenty-one
is negative.

**Final audit verdict:** **PASS / GO.**
