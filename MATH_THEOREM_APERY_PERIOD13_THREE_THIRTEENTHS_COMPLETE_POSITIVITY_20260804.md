# Period thirteen: the three-thirteenths ray and complete positivity

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical theorem.  It proves that every
honest exact-first-carry cyclic Apéry clock of period thirteen has strictly
positive formal Bellman functional.  No computation or search is used.
The proof promotes a previously certified compact endpoint lower bound,
uses the forced location `Y_3>3/13>1/5`, and closes the formerly critical
`u=5` chamber with rational margin `1903/125000`.  It does not address
threshold overshoot, later first crossing, or finite physical shoulders.

Put

\[
 A={\sqrt\pi\over2},\qquad
 F_A(w)=\sum_{q\ge0}K(qA+w),\qquad
 f(x)=F_A(Ax),
\tag{0.1}
\]

and

\[
 C=F_A(0),\qquad g(x)=\rho(Ax).
\tag{0.2}
\]

## 1. A promoted pre-quarter floor

The authenticated compact estimates are

\[
 C>{5503\over125000},
 \qquad
 f(1/4)>{44739\over1000000}.
\tag{1.1}
\]

Every interior critical point of `f` on `[0,1/4]` is a strict maximum.
Therefore the minimum of `f` on that interval occurs at an endpoint.
Since

\[
 {44739\over1000000}>{5503\over125000},
\]

we obtain the strengthened floor

\[
 \boxed{
 f(x)>L:={5503\over125000}
 \qquad(0\le x\le1/4).}
\tag{1.2}
\]

This is the only new analytic observation needed below.  It uses the
certified endpoint bounds from the compact-Gaussian theorem and the
already-proved one-mode critical-point classification.  In particular,
it does not use the later six-slot theorem whose frozen statement has an
endpoint-strictness correction pending.

Retain also the proved estimates

\[
 f(x)<G:={1079\over20000}
 \qquad(0\le x\le1/2),
\tag{1.3}
\]

\[
 f(1/5)<U:={101\over2000},
 \qquad
 f'(x)<0\quad(1/5\le x\le1/2),
\tag{1.4}
\]

\[
 f(x)<Q:={1129\over25000}
 \qquad(1/4\le x<1/2),
\tag{1.5}
\]

and

\[
 |g(x)|<\varepsilon:={1\over20000},
 \qquad
 g(x)>0\quad(1/4\le x\le1/2).
\tag{1.6}
\]

## 2. Period-thirteen ray geometry

Let

\[
 0=s_0<s_1<\cdots<s_{12}<P,
 \qquad P+s_1=A,
\tag{2.1}
\]

be an honest exact-first-carry period-thirteen table.  Put

\[
 a=s_1,\qquad \alpha={a\over A}.
\tag{2.2}
\]

For the two reflected rays write

\[
 X_i={s_{i+1}\over A},
 \qquad
 Y_i={A-s_{13-i}\over A},
 \qquad1\le i\le u.
\tag{2.3}
\]

Then

\[
 0<X_i\le Y_i<1/2.
\tag{2.4}
\]

Disjointness gives

\[
 u+1<13-u,
 \qquad\hbox{hence}\qquad u\le5.
\tag{2.5}
\]

Terminal-suffix maximality gives the exact lower envelope

\[
 Y_i\ge\alpha+{i\over13}(1-\alpha)>{i\over13}.
\tag{2.6}
\]

In particular,

\[
 \boxed{
 Y_3>{3\over13}>{1\over5},
 \qquad
 Y_4>{4\over13}>{1\over4},
 \qquad
 Y_5>{5\over13}>{1\over4}.}
\tag{2.7}
\]

The exact reflected-ray identity is

\[
\boxed{
\begin{aligned}
 E(s)={}&C+g(\alpha)
 +\sum_{i=1}^{u}
 \bigl(f(X_i)-f(Y_i)+g(Y_i)\bigr)\\
 &+\sum_{r=u+2}^{12-u}f(s_r/A),
\end{aligned}}
\tag{2.8}
\]

and the exact-first-carry comparison gives

\[
 \Phi(W)\ge E(s).
\tag{2.9}
\]

The middle trains in (2.8) are strictly positive.  Their exact residue
sets are

\[
\begin{array}{c|c}
u&\text{middle residues}\\ \hline
3&5,6,7,8,9\\
4&6,7,8\\
5&7.
\end{array}
\tag{2.10}
\]

Thus the critical `u=5` chamber still contains one positive middle train,
but the proof below is strong enough to discard it.

## 3. Three exact pair prices

### Lemma 3.1 (global pair)

For every `0<X<=Y<1/2`,

\[
 \boxed{
 f(X)-f(Y)+g(Y)>L-G-\varepsilon.}
\tag{3.1}
\]

#### Proof

If `X<1/4`, use (1.2), (1.3), and the absolute theta bound.  If
`X>=1/4`, then `X<=Y`, monotone decrease on `[1/4,1/2]` makes the compact
difference nonnegative, and `g(Y)>0`.  This is stronger than (3.1).
\(\square\)

### Lemma 3.2 (three-thirteenths pair)

If `Y>3/13`, then

\[
 \boxed{
 f(X)-f(Y)+g(Y)>L-U-\varepsilon.}
\tag{3.2}
\]

#### Proof

Since `3/13>1/5`, first suppose `X<1/5`.  Then (1.2) gives
`f(X)>L`, while (1.4) and `Y>3/13` give

\[
 f(Y)<f(3/13)<f(1/5)<U.
\]

The absolute theta bound proves (3.2).  If `X>=1/5`, monotone decrease
on `[1/5,1/2]` gives `f(X)>=f(Y)`; the absolute theta bound is again
strictly stronger than (3.2), because `L-U<0`. \(\square\)

### Lemma 3.3 (quarter pair)

If `Y>1/4`, then

\[
 \boxed{
 f(X)-f(Y)+g(Y)>L-Q.}
\tag{3.3}
\]

#### Proof

If `X<1/4`, use (1.2), (1.5), and `g(Y)>0`.  If `X>=1/4`, monotone
decrease makes the compact difference nonnegative and theta is positive.
\(\square\)

## 4. Complete rational ledger

For every chamber with `u>=3`, price pairs one and two by Lemma 3.1,
pair three by Lemma 3.2, and all later pairs by Lemma 3.3.  Also
`g(alpha)>-epsilon`.  The only possible negative theta charges are thus
`g(alpha),g(Y_1),g(Y_2),g(Y_3)`, exactly four charges.  Discarding the
strictly positive middle trains gives

\[
 \boxed{
 E(s)>
 (u+1)L-2G-U-(u-3)Q-4\varepsilon.}
\tag{4.1}
\]

With common denominator `500000`,

\[
 L={22012\over500000},\quad
 2G={53950\over500000},\quad
 U={25250\over500000},\quad
 Q={22580\over500000},\quad
 4\varepsilon={100\over500000}.
\tag{4.2}
\]

For `u=3`,

\[
 E(s)>{88048-53950-25250-100\over500000}
 ={2187\over125000}>0.
\tag{4.3}
\]

For `u=4`,

\[
 E(s)>{110060-53950-25250-22580-100\over500000}
 ={409\over25000}>0.
\tag{4.4}
\]

For `u=5`,

\[
 \boxed{
 E(s)>{132072-53950-25250-45160-100\over500000}
 ={1903\over125000}>0.}
\tag{4.5}
\]

This is the critical period-thirteen margin.  It uses the
`3/13` location and does not spend the surviving middle train.

## 5. Complete period-thirteen closure

### Theorem 5.1

Every honest exact-first-carry period-thirteen cyclic Apéry clock satisfies

\[
 \boxed{\Phi(W)>0.}
\tag{5.1}
\]

#### Proof

The overlap depth obeys `H<=u`.  If `H<=2`, then `u<=5` and the scalar
in the reflected-depth theorem satisfies

\[
 360H+\tau\le720+(u+1)\le726<860.
\]

That theorem gives strict positivity.

It remains to take `H>=3`.  Then `u>=3`, while (2.5) gives `u<=5`.
Equations (4.3)--(4.5) therefore exhaust every possible value of `u`,
independently of whether `H` is three, four, or five.  Finally use
`Phi(W)>=E(s)`. \(\square\)

## 6. Scope and frozen dependencies

This theorem closes the complete honest exact-first-carry formal branch at
period thirteen.  It does not address overshoot, later first crossing, the
finite physical shoulder, or arbitrary Bellman clocks.

| role | file | SHA-256 |
|---|---|---|
| prefix minimum, ray identity, and depth theorem | `MATH_THEOREM_APERY_MULTIDEFECT_PREFIX_MINIMUM_AND_REFLECTED_RAY_DEPTH_REDUCTION_20260804.md` | `28c714f8eae3ae56c22a1c7c643f583e73b891e1abf2f66e4e866d831b7eb21e` |
| terminal-suffix envelope | `MATH_LEMMA_APERY_TERMINAL_SUFFIX_MAXIMUM_AND_QUARTER_CUTOFF_20260804.md` | `6ef133e15f8635db9a91fb837ef2df65fadedc6a52ff923b0b5895f215324639` |
| global, one-fifth, and quarter upper bounds | `MATH_THEOREM_APERY_PERIOD11_12_GLOBAL_QUARTER_LEDGER_COMPLETE_POSITIVITY_20260804.md` | `fb9139813f93d8e5450b8ab3cee0238c289cd573222d0d05fd6174040fdbe601` |
| one-mode critical-point classification | `MATH_THEOREM_COMPLEMENTARY_PAIR_TRAIN_AND_H4_INERT_SCALAR_REDUCTION_20260804.md` | `fc8b2dee92dd3bb9afab390c8507db51fec05c6ca4e9d46ac4948c7422d042a7` |
| sharpened compact endpoint bounds | `MATH_THEOREM_H4_INERT_COMPACT_GAUSSIAN_GATE_CLOSURE_20260804.md` | `f88e8ac246d0533f018b7d713cfc6f09e14872d2f2026e7e29b3bc40f3a6062b` |
| theta sign and absolute bound | `MATH_LEMMA_THETA_HALF_INTERVAL_MONOTONICITY_AND_HALF_ROOT_SUMS_20260804.md` | `f974aeda114df4c933a396c06de51596bccd2fea18066412d45f7a18df62a0e3` |
