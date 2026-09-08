# Period twenty-one: the two-sevenths far-ray dichotomy and complete positivity

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical theorem.  It proves that every
honest exact-first-carry cyclic Apéry clock of period twenty-one has
strictly positive formal Bellman functional.  The formerly residual
`u=9` chamber has exact rational margin `1/100000`.  No computation or
search is used.  The proof uses an ordered-ray dichotomy; it does not
incorrectly assign a positive anchor price to a pair whose left endpoint
already lies past the quarter.

Put

\[
 A={\sqrt\pi\over2},\qquad
 f(x)=F_A(Ax),\qquad C=F_A(0),\qquad g(x)=\rho(Ax).
\tag{0.1}
\]

Retain

\[
 L={5503\over125000},\qquad
 Q={1129\over25000},
\tag{0.2}
\]

with `f(x)>L` on `[0,1/4]`, `f(x)<Q` on `[1/4,1/2)`, strict decrease
of `f` on `[1/5,1/2]`, and positivity of `g` on `[1/4,1/2]`.

The preceding period-twenty-one reduction proves every chamber with
`u<=8`.  In the sole residual `u=9` chamber it proves the exact base
ledger

\[
 E(s)>{112\over500000}
 +\sum_{i=6}^{9}
 \bigl(f(X_i)-f(Y_i)+g(Y_i)\bigr)
 +\sum_{r=11}^{11}f(s_r/A),
\tag{0.3}
\]

where the first term is the complete contribution through pair five.
Also

\[
 0<X_6<X_7<X_8<X_9<1/2,
 \qquad X_i\le Y_i,
 \qquad Y_6>{6\over21}={2\over7}.
\tag{0.4}
\]

## 1. A rational two-sevenths bound

For `0<x<25`, define

\[
 U_{24}(x)=\sum_{j=0}^{23}{x^j\over j!}
 +{x^{24}\over24!\,(1-x/25)}.
\tag{1.1}
\]

Then `e^x<U_24(x)`.

### Lemma 1.1

\[
 \boxed{f(2/7)<V_6:={4083\over100000}.}
\tag{1.2}
\]

#### Proof

The literal train gives

\[
\begin{aligned}
f(2/7)<1
&-e^{-25\pi/196}
-e^{-81\pi/196}\\
&-e^{-64\pi/49}
-e^{-529\pi/196}.
\end{aligned}
\tag{1.3}
\]

Using `pi<22/7`, the four exponents are smaller than

\[
 {275\over686},\qquad
 {891\over686},\qquad
 {1408\over343},\qquad
 {5819\over686}.
\tag{1.4}
\]

Direct rational substitution in (1.1) gives

\[
\begin{aligned}
U_{24}(275/686)&<{25000\over16743},\\
U_{24}(891/686)&<{1250\over341},\\
U_{24}(1408/343)&<{20000\over329},\\
U_{24}(5819/686)&<5000.
\end{aligned}
\tag{1.5}
\]

All denominators are positive, and each displayed comparison is an
integer cross multiplication after clearing `24!`, `25`, and the listed
rational denominators.  Hence

\[
 e^{-25\pi/196}>{16743\over25000},\qquad
 e^{-81\pi/196}>{341\over1250},
\tag{1.6}
\]

\[
 e^{-64\pi/49}>{329\over20000},\qquad
 e^{-529\pi/196}>{1\over5000}.
\tag{1.7}
\]

Their sum is

\[
 {66972+27280+1645+20\over100000}
 ={95917\over100000}.
\]

Substitution in (1.3) gives

\[
 f(2/7)<1-{95917\over100000}
 ={4083\over100000}.
\]
\(\square\)

The anchor improvement over the generic quarter upper price is

\[
 Q-V_6
 ={4516-4083\over100000}
 ={433\over100000}.
\tag{1.8}
\]

This exceeds the residual four-quarter deficit

\[
 {27\over6250}={432\over100000}
\tag{1.9}
\]

by exactly `1/100000`.

## 2. The ordered far-ray dichotomy

### Lemma 2.1

In the residual `u=9` chamber, the total of pairs six through nine is
strictly larger than

\[
 \min\left\{
 (L-V_6)+3(L-Q),\ 0
 \right\}.
\tag{2.1}
\]

More precisely:

1. if `X_6<1/4`, pair six is larger than `L-V_6`, while each of pairs
   seven through nine is larger than `L-Q`;
2. if `X_6>=1/4`, every pair from six through nine is strictly positive.

#### Proof

Suppose first that `X_6<1/4`.  Then `f(X_6)>L`.  Since
`Y_6>2/7>1/5` and `f` decreases from one fifth,

\[
 f(Y_6)<f(2/7)<V_6.
\]

Also `g(Y_6)>0`.  Therefore pair six is larger than `L-V_6`.
For each later pair, either its left endpoint remains before the quarter,
in which case the lower floor and quarter upper bound give `L-Q`, or it
lies after the quarter, in which case monotone decrease and positive theta
give a nonnegative value, stronger than `L-Q<0`.

Now suppose `X_6>=1/4`.  The early ray is strictly increasing, so
`X_i>=X_6>=1/4` for every `i>=6`.  Since `X_i<=Y_i<1/2`, quarter-band
decrease gives `f(X_i)>=f(Y_i)`, and `g(Y_i)>0`.  Every far pair is
therefore strictly positive. \(\square\)

The dichotomy is essential.  The positive price `L-V_6` is not asserted
in the second case; instead, orderedness makes all four far pairs free.

## 3. Complete period-twenty-one closure

### Theorem 3.1

Every honest exact-first-carry period-twenty-one cyclic Apéry clock
satisfies

\[
 \boxed{\Phi(W)>0.}
\tag{3.1}
\]

#### Proof

All `u<=8` chambers are positive by the preceding reduction.  It remains
to take `u=9`.

If `X_6>=1/4`, Lemma 2.1 makes every far pair positive.  The base margin
`112/500000` in (0.3) and the positive middle train finish the proof.

If `X_6<1/4`, use the first branch of Lemma 2.1.  Over denominator one
million,

\[
 {112\over500000}={224\over1000000},
\]

\[
 L-V_6={44024-40830\over1000000}
 ={3194\over1000000},
\]

and

\[
 3(L-Q)=3{(44024-45160)\over1000000}
 =-{3408\over1000000}.
\]

Therefore

\[
 E(s)>{224+3194-3408\over1000000}
 ={1\over100000}>0,
\tag{3.2}
\]

even after discarding the remaining positive middle train.  Finally
`Phi(W)>=E(s)`. \(\square\)

## 4. Scope and frozen dependencies

This theorem closes the complete honest exact-first-carry formal branch at
period twenty-one.  It does not address threshold overshoot, later first
crossing, finite physical shoulders, or arbitrary Bellman clocks.

| role | file | SHA-256 |
|---|---|---|
| period-twenty-one anchor/base reduction | `MATH_THEOREM_APERY_PERIOD21_FOUR_TWENTYFIRST_ANCHOR_AND_MIDDLE_TRAIN_REDUCTION_20260804.md` | `4f31625b65431320566e5372e027af3863366aa9482844cf98e220d723fecf45` |
| prefix minimum and reflected identity | `MATH_THEOREM_APERY_MULTIDEFECT_PREFIX_MINIMUM_AND_REFLECTED_RAY_DEPTH_REDUCTION_20260804.md` | `28c714f8eae3ae56c22a1c7c643f583e73b891e1abf2f66e4e866d831b7eb21e` |
| compact monotonicity and endpoint bounds | `MATH_THEOREM_APERY_PERIOD11_12_GLOBAL_QUARTER_LEDGER_COMPLETE_POSITIVITY_20260804.md` | `fb9139813f93d8e5450b8ab3cee0238c289cd573222d0d05fd6174040fdbe601` |
| theta positivity | `MATH_LEMMA_THETA_HALF_INTERVAL_MONOTONICITY_AND_HALF_ROOT_SUMS_20260804.md` | `f974aeda114df4c933a396c06de51596bccd2fea18066412d45f7a18df62a0e3` |
