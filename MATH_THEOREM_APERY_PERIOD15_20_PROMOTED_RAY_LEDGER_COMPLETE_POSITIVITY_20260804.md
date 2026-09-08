# Periods fifteen through twenty: promoted ray ledgers and complete positivity

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical theorem.  It proves that every
honest exact-first-carry cyclic Apéry clock of every period
`15<=h<=20` has strictly positive formal Bellman functional.  No
computation or search is used.  The worst certified margin is
`23/12500`, at `(h,u)=(20,9)`.  The same decoupled ledger first ceases to
be positive at period twenty-one, in the `u=5` chamber; this is recorded
as a scalar frontier, not as a nonpositivity claim.

Put

\[
 A={\sqrt\pi\over2},\qquad
 f(x)=F_A(Ax),\qquad C=F_A(0),\qquad g(x)=\rho(Ax).
\tag{0.1}
\]

## 1. Uniform analytic prices

The compact endpoint certificates and the strict-maximum classification
give

\[
 \boxed{f(x)>L:={5503\over125000}
 \qquad(0\le x\le1/4).}
\tag{1.1}
\]

We retain

\[
 f(x)<G:={1079\over20000}\qquad(0\le x\le1/2),
\tag{1.2}
\]

\[
 f(1/5)<U:={101\over2000},
 \qquad f'(x)<0\quad(1/5\le x\le1/2),
\tag{1.3}
\]

\[
 f(x)<Q:={1129\over25000}\qquad(1/4\le x<1/2),
\tag{1.4}
\]

and

\[
 |g(x)|<\varepsilon:={1\over20000},
 \qquad g(x)>0\quad(1/4\le x\le1/2).
\tag{1.5}
\]

For `0<X<=Y<1/2`, the usual two-case argument gives the three prices

\[
 \mathcal P_G:=L-G-\varepsilon,
\tag{1.6}
\]

\[
 \mathcal P_U:=L-U-\varepsilon
 \qquad(Y>1/5),
\tag{1.7}
\]

and

\[
 \mathcal P_Q:=L-Q
 \qquad(Y>1/4).
\tag{1.8}
\]

Indeed, below the named anchor use the lower floor `L` and the
corresponding upper bound.  At or beyond the anchor, monotone decrease
makes `f(X)-f(Y)` nonnegative.  The quarter price needs no adverse theta
allowance because `g(Y)>0` there.

For arithmetic, put every constant over denominator `500000`:

\[
 L={22012\over500000},\quad
 G={26975\over500000},\quad
 U={25250\over500000},
\tag{1.9}
\]

\[
 Q={22580\over500000},\quad
 \varepsilon={25\over500000}.
\tag{1.10}
\]

The incremental cost of one additional quarter pair is

\[
 L-Q=-{568\over500000}.
\tag{1.11}
\]

## 2. General finite-period geometry

Let

\[
 0=s_0<s_1<\cdots<s_{h-1}<P,
 \qquad P+s_1=A,
\tag{2.1}
\]

be honest, where `15<=h<=20`.  Put `alpha=s_1/A` and

\[
 X_i={s_{i+1}\over A},
 \qquad
 Y_i={A-s_{h-i}\over A},
 \qquad1\le i\le u.
\tag{2.2}
\]

Then `0<X_i<=Y_i<1/2`, and

\[
 u+1<h-u,
 \qquad
 u\le u_{\max}(h):=\left\lfloor{h-2\over2}\right\rfloor.
\tag{2.3}
\]

Terminal-suffix maximality gives

\[
 Y_i\ge\alpha+{i\over h}(1-\alpha)>{i\over h}.
\tag{2.4}
\]

The exact reflected identity is

\[
\boxed{
\begin{aligned}
 E(s)={}&C+g(\alpha)
 +\sum_{i=1}^{u}
 \bigl(f(X_i)-f(Y_i)+g(Y_i)\bigr)\\
 &+\sum_{r=u+2}^{h-u-1}f(s_r/A),
\end{aligned}}
\tag{2.5}
\]

with `Phi(W)>=E(s)`.  Every middle term is strictly positive and will be
discarded only after (2.5).

The relevant forced anchors and maximal ray counts are

\[
\begin{array}{c|c|c|c}
h&u_{\max}&\text{first guaranteed }Y_i>1/5
 &\text{first guaranteed }Y_i>1/4\\ \hline
15&6&i=3&i=4\\
16&7&i=4&i=4\\
17&7&i=4&i=5\\
18&8&i=4&i=5\\
19&8&i=4&i=5\\
20&9&i=4&i=5.
\end{array}
\tag{2.6}
\]

All entries follow directly from (2.4), including equality at `i/h=1/5`
or `1/4`, because the inequality in (2.4) is strict.

## 3. Period fifteen

For `h=15`, price pairs one and two by `P_G`, pair three by `P_U`, and
all later pairs by `P_Q`.  Together with `g(alpha)`, exactly four adverse
theta allowances remain.  Hence, for `u>=3`,

\[
 E(s)>(u+1)L-2G-U-(u-3)Q-4\varepsilon.
\tag{3.1}
\]

The right side decreases with `u` by (1.11), so its minimum occurs at
`u=6`.  There

\[
\begin{aligned}
 E(s)&>7L-2G-U-3Q-4\varepsilon\\
 &={7044\over500000}
 ={1761\over125000}>0.
\end{aligned}
\tag{3.2}
\]

## 4. Period sixteen

For `h=16`, the first three pairs are global and every later pair is
already past the quarter.  Thus

\[
 E(s)>(u+1)L-3G-(u-3)Q-4\varepsilon
 \qquad(u\ge3).
\tag{4.1}
\]

At the maximal `u=7`,

\[
\begin{aligned}
 E(s)&>8L-3G-4Q-4\varepsilon\\
 &={176096-80925-90320-100\over500000}\\
 &={4751\over500000}>0.
\end{aligned}
\tag{4.2}
\]

## 5. Periods seventeen through twenty

For `17<=h<=20`, the first three pairs are global, pair four is past
one fifth, and every pair from five onward is past the quarter.  For
`u>=4`,

\[
 E(s)>(u+1)L-3G-U-(u-4)Q-5\varepsilon.
\tag{5.1}
\]

The `u=3` chamber is independently positive from

\[
 E(s)>4L-3G-4\varepsilon={7023\over500000}>0.
\tag{5.2}
\]

At `u=4`, the numerator in (5.1) is

\[
 5L-3G-U-5\varepsilon
 ={3760\over500000}.
\tag{5.3}
\]

Every later quarter pair subtracts exactly `568/500000`.  Therefore the
maximal chambers have margins

\[
\begin{array}{c|c|c}
h&u_{\max}&\text{strict lower margin}\\ \hline
17&7&(3760-3\cdot568)/500000=257/62500\\
18&8&(3760-4\cdot568)/500000=93/31250\\
19&8&(3760-4\cdot568)/500000=93/31250\\
20&9&(3760-5\cdot568)/500000=23/12500.
\end{array}
\tag{5.4}
\]

Every entry is positive.  The last one is the smallest margin in the
entire range `15<=h<=20`.

## 6. Complete closure and the first scalar break

### Theorem 6.1

For every integer `15<=h<=20`, every honest exact-first-carry period-`h`
cyclic Apéry clock satisfies

\[
 \boxed{\Phi(W)>0.}
\tag{6.1}
\]

#### Proof

If `H<=2`, then throughout this range `u<=9`, so

\[
 360H+\tau\le720+(u+1)\le730<860.
\]

The prior reflected-depth theorem applies.  If `H>=3`, then `u>=3`.
Sections 3--5 exhaust every possible `u<=u_max(h)` and give a positive
margin.  Finally `Phi(W)>=E(s)`. \(\square\)

The same decoupled ledger has its first nonpositive row at period
twenty-one.  There

\[
 u_{\max}=9,
 \qquad
 Y_4>{4\over21},\qquad {4\over21}<{1\over5},
 \qquad
 Y_5>{5\over21}>{1\over5},
 \qquad
 Y_6>{2\over7}>{1\over4}.
\tag{6.2}
\]

Already at `u=5`, four global pairs, one one-fifth pair, and six theta
allowances give only

\[
 6L-4G-U-6\varepsilon
 =-{1228\over500000}
 =-{307\over125000}.
\tag{6.3}
\]

Thus the present independent-pair method breaks first at `(h,u)=(21,5)`.
This is not a counterexample.  If pair four were instead priced by an
anchor bound `f(Y_4)<V` valid from `4/21`, that first row would close
provided

\[
 \boxed{V<{25747\over500000}.}
\tag{6.4}
\]

Indeed, (6.4) is exactly

\[
 V<6L-3G-U-6\varepsilon.
\]

Alternatively, an equal credit may come from the nine positive middle
trains or from overlap/theta correlation.  No such credit is asserted
here.

## 7. Scope and frozen dependencies

| role | file | SHA-256 |
|---|---|---|
| prefix minimum, ray identity, and depth theorem | `MATH_THEOREM_APERY_MULTIDEFECT_PREFIX_MINIMUM_AND_REFLECTED_RAY_DEPTH_REDUCTION_20260804.md` | `28c714f8eae3ae56c22a1c7c643f583e73b891e1abf2f66e4e866d831b7eb21e` |
| terminal-suffix envelope | `MATH_LEMMA_APERY_TERMINAL_SUFFIX_MAXIMUM_AND_QUARTER_CUTOFF_20260804.md` | `6ef133e15f8635db9a91fb837ef2df65fadedc6a52ff923b0b5895f215324639` |
| global, one-fifth, and quarter upper bounds | `MATH_THEOREM_APERY_PERIOD11_12_GLOBAL_QUARTER_LEDGER_COMPLETE_POSITIVITY_20260804.md` | `fb9139813f93d8e5450b8ab3cee0238c289cd573222d0d05fd6174040fdbe601` |
| one-mode critical-point classification | `MATH_THEOREM_COMPLEMENTARY_PAIR_TRAIN_AND_H4_INERT_SCALAR_REDUCTION_20260804.md` | `fc8b2dee92dd3bb9afab390c8507db51fec05c6ca4e9d46ac4948c7422d042a7` |
| compact endpoint bounds | `MATH_THEOREM_H4_INERT_COMPACT_GAUSSIAN_GATE_CLOSURE_20260804.md` | `f88e8ac246d0533f018b7d713cfc6f09e14872d2f2026e7e29b3bc40f3a6062b` |
| theta sign and absolute bound | `MATH_LEMMA_THETA_HALF_INTERVAL_MONOTONICITY_AND_HALF_ROOT_SUMS_20260804.md` | `f974aeda114df4c933a396c06de51596bccd2fea18066412d45f7a18df62a0e3` |
