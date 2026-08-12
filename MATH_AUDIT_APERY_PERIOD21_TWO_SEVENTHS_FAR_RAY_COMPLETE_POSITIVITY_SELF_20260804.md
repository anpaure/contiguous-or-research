# Self-audit: period-twenty-one two-sevenths complete closure

**Date:** 2026-08-04  
**Audited theorem:**  
`MATH_THEOREM_APERY_PERIOD21_TWO_SEVENTHS_FAR_RAY_COMPLETE_POSITIVITY_20260804.md`  
**Verdict:** **PASS / GO.**  The rational `2/7` anchor, ordered-ray
dichotomy, and final `1/100000` margin replay exactly.  No computation or
search is used.

## 1. Gaussian certificate

At `2/7`, the first four adverse exponents are

\[
{25\pi\over196},\quad
{81\pi\over196},\quad
{64\pi\over49},\quad
{529\pi\over196}.
\]

Multiplying by `22/7` gives exactly

\[
{275\over686},\quad
{891\over686},\quad
{1408\over343},\quad
{5819\over686}.
\]

The `U_24` rational upper certificates invert to the lower Gaussian
bounds

\[
{16743\over25000},\quad
{341\over1250},\quad
{329\over20000},\quad
{1\over5000}.
\]

Over denominator `100000`, their numerator sum is

\[
66972+27280+1645+20=95917.
\]

Thus

\[
f(2/7)<{4083\over100000}.
\]

The quarter improvement is

\[
{1129\over25000}-{4083\over100000}
={433\over100000},
\]

which exceeds `27/6250=432/100000` by `1/100000`.

## 2. Logical dichotomy

If `X_6<1/4`, then `f(X_6)>L`; since `Y_6>2/7` and `f` decreases from
`1/5`, `f(Y_6)<V_6`.  Positive theta yields the price `L-V_6`.
Pairs seven through nine each have the safe quarter price `L-Q`.

If `X_6>=1/4`, orderedness gives `X_i>=1/4` for all `i>=6`.
Quarter decrease and positive theta make every one of those pairs
strictly positive.  The audit therefore does not apply the positive
anchor price outside its valid branch.

## 3. Final arithmetic

The base-through-pair-five margin is

\[
{112\over500000}={224\over1000000}.
\]

In the anchor branch,

\[
L-V_6={44024-40830\over1000000}
={3194\over1000000},
\]

while three generic quarter pairs cost

\[
3(L-Q)=3(44024-45160)/1000000
=-{3408\over1000000}.
\]

The final numerator is

\[
224+3194-3408=10,
\]

so

\[
E(s)>{10\over1000000}={1\over100000}>0.
\]

In the post-quarter branch, all four far pairs and the middle train are
positive on top of the base margin.  Both branches close.

**Final audit verdict:** **PASS / GO.**
