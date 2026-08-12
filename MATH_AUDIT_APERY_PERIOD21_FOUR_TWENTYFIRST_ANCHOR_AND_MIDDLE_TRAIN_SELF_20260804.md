# Self-audit: period-twenty-one anchor and middle-train reduction

**Date:** 2026-08-04  
**Audited theorem:**  
`MATH_THEOREM_APERY_PERIOD21_FOUR_TWENTYFIRST_ANCHOR_AND_MIDDLE_TRAIN_REDUCTION_20260804.md`  
**Verdict:** **PASS / GO in the stated `u<=8` scope.**  The anchor
certificate, middle-floor certificate, ray/middle ledgers, and residual
`u=9` scalar replay exactly.  No computation or search is used.

## 1. Four-twenty-first anchor arithmetic

At `4/21`, the first two derivative ratios are bounded by `81/100` and
`11/100`, and all later ratios have geometric quotient below `1/30`.
Their total is

\[
{81\over100}+{11/100\over1-1/30}
={2679\over2900}<1.
\]

The logarithmic derivative of every ratio is negative on
`[4/21,1/2]`, so this signs the derivative on the whole interval rather
than only at the anchor.  The anchor pair price therefore uses a proved
monotonicity interval; it does not infer monotonicity from a single value.

At `u=4/21`, the first four adverse exponents are exactly

\[
{289\pi\over1764},\quad
{625\pi\over1764},\quad
{529\pi\over441},\quad
{4489\pi\over1764}.
\]

Multiplication by `22/7` gives the four rational upper exponents in the
theorem.  The `U_24` tail majorant is valid because every one is below
twenty-five.  The four certified Gaussian lower bounds sum to

\[
{2987\over5000}+{41\over125}+{23\over1000}
+{33\over100000}
={94873\over100000}.
\]

Therefore

\[
f(4/21)<{5127\over100000}={25635\over500000}.
\]

The target threshold exceeds it by

\[
{25747-25635\over500000}={112\over500000}.
\]

This is exactly the `u=5` final margin after all other prices.

## 2. Middle-floor arithmetic

At `10/21`, the four displayed adverse exponentials plus the tail are
bounded above by

\[
{1613\over2000}+{181\over1000}+{82\over10000}
+{1\over10000}+{1\over1000000}.
\]

Over denominator one million this is

\[
806500+181000+8200+100+1=995801.
\]

Thus

\[
f(10/21)>{4199\over1000000}>{1\over250}.
\]

For `t<=10/21`, either `t<=1/5`, where `f(t)>L>1/250`, or
`1/5<=t<=10/21`, where monotone decrease gives
`f(t)>=f(10/21)>1/250`.  The uniform middle floor is valid.

## 3. Period-twenty-one ledgers

Over denominator `500000`, the anchored `u=5` numerator is

\[
132072-80925-25635-25250-150=112.
\]

Each new quarter pair changes it by

\[
L-Q=22012-22580=-568.
\]

For `u=6,7,8`, prefix averaging puts the first middle residue below
`8/21,9/21,10/21`, respectively.  Adding the certified `2000` middle
credit gives

\[
112-568+2000=1544,
\]

\[
112-1136+2000=976,
\]

\[
112-1704+2000=408.
\]

At `u=3`, the numerator is `7023`.  At `u=4`,

\[
5L-3G-V-5\varepsilon
=110060-80925-25635-125=3375.
\]

All rows through `u=8` are positive.

## 4. Residual row and scope

At `u=9`, four quarter increments give

\[
112-4(568)=-2160.
\]

There is exactly one middle residue, `r=11`.  Hence the remaining
sufficient scalar is

\[
f(s_{11}/A)+\mathcal C>{2160\over500000}={27\over6250}.
\]

No uniform location bound supplies this, because only
`s_11/A<=1/2` is known and `f(1/2)<1/40000`.  The theorem correctly
stops at `u=8` and makes no period-twenty-one complete-closure claim.

**Final audit verdict:** **PASS / GO in the stated scope.**
