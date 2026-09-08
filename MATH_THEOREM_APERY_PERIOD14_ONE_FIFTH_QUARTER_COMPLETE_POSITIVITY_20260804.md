# Period fourteen: one-fifth/quarter ray ledger and complete positivity

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical theorem.  It proves that every
honest exact-first-carry cyclic Apéry clock of period fourteen has strictly
positive formal Bellman functional.  No computation or search is used.
The maximal `u=6` chamber has certified margin `1761/125000`.  The theorem
does not address threshold overshoot, later first crossing, or finite
physical shoulders.

Put

\[
 A={\sqrt\pi\over2},\qquad
 f(x)=F_A(Ax),\qquad C=F_A(0),\qquad g(x)=\rho(Ax).
\tag{0.1}
\]

## 1. Compact constants

The endpoint certificates and the strict-maximum critical-point theorem
give

\[
 \boxed{f(x)>L:={5503\over125000}
 \qquad(0\le x\le1/4).}
\tag{1.1}
\]

Indeed, `C>L`, while

\[
 f(1/4)>{44739\over1000000}>{5503\over125000},
\]

and an interior minimum would be an interior critical point rather than a
strict maximum.

Retain

\[
 f(x)<G:={1079\over20000}quad(0\le x\le1/2),
\tag{1.2}
\]

\[
 f(1/5)<U:={101\over2000},
 \qquad f'(x)<0\quad(1/5\le x\le1/2),
\tag{1.3}
\]

\[
 f(x)<Q:={1129\over25000}quad(1/4\le x<1/2),
\tag{1.4}
\]

and

\[
 |g(x)|<\varepsilon:={1\over20000},
 \qquad g(x)>0\quad(1/4\le x\le1/2).
\tag{1.5}
\]

## 2. Period-fourteen geometry

Let

\[
 0=s_0<s_1<\cdots<s_{13}<P,
 \qquad P+s_1=A,
\tag{2.1}
\]

be honest, and put `alpha=s_1/A`.  Define

\[
 X_i={s_{i+1}\over A},
 \qquad
 Y_i={A-s_{14-i}\over A},
 \qquad1\le i\le u.
\tag{2.2}
\]

Then `0<X_i<=Y_i<1/2`.  Ray disjointness gives

\[
 u+1<14-u,
 \qquad\hbox{so}\qquad u\le6.
\tag{2.3}
\]

Terminal-suffix maximality gives

\[
 Y_i\ge\alpha+{i\over14}(1-\alpha)>{i\over14}.
\tag{2.4}
\]

Consequently

\[
 \boxed{
 Y_3>{3\over14}>{1\over5},
 \qquad
 Y_i>{i\over14}\ge{2\over7}>{1\over4}
 \quad(i\ge4).}
\tag{2.5}
\]

The exact endpoint identity is

\[
\boxed{
\begin{aligned}
 E(s)={}&C+g(\alpha)
 +\sum_{i=1}^{u}
 \bigl(f(X_i)-f(Y_i)+g(Y_i)\bigr)\\
 &+\sum_{r=u+2}^{13-u}f(s_r/A),
\end{aligned}}
\tag{2.6}
\]

with `Phi(W)>=E(s)`.  The middle residue sets are

\[
\begin{array}{c|c}
u&\text{middle residues}\\ \hline
3&5,6,7,8,9,10\\
4&6,7,8,9\\
5&7,8\\
6&\varnothing.
\end{array}
\tag{2.7}
\]

Every displayed middle train is strictly positive.

## 3. Uniform ray ledger

The same two-case arguments yield the following three pair prices:

\[
 f(X)-f(Y)+g(Y)>L-G-\varepsilon
 \qquad(0<X\le Y<1/2),
\tag{3.1}
\]

\[
 f(X)-f(Y)+g(Y)>L-U-\varepsilon
 \qquad(Y>1/5),
\tag{3.2}
\]

and

\[
 f(X)-f(Y)+g(Y)>L-Q
 \qquad(Y>1/4).
\tag{3.3}
\]

For completeness, in each line, if `X` lies below the named monotonicity
anchor, use the lower floor `L` and the corresponding upper bound at `Y`.
If `X` lies at or beyond the anchor, monotone decrease makes the compact
difference nonnegative.  The quarter case has positive theta; the first
two cases use its absolute bound.

Price pairs one and two by (3.1), pair three by (3.2), and all later
pairs by (3.3).  Together with `g(alpha)>-epsilon`, exactly four possible
negative theta charges are retained.  Discarding only positive middle
trains gives

\[
 \boxed{
 E(s)>(u+1)L-2G-U-(u-3)Q-4\varepsilon.}
\tag{3.4}
\]

## 4. Exact margins

Use denominator `500000`:

\[
 L={22012\over500000},\quad
 2G={53950\over500000},\quad
 U={25250\over500000},\quad
 Q={22580\over500000},\quad
 4\varepsilon={100\over500000}.
\tag{4.1}
\]

The complete ledger is

\[
\begin{array}{c|c}
u&\text{strict lower margin}\\ \hline
3&2187/125000\\
4&409/25000\\
5&1903/125000\\
6&1761/125000.
\end{array}
\tag{4.2}
\]

The new last row is

\[
\begin{aligned}
 7L-2G-U-3Q-4\varepsilon
 &={154084-53950-25250-67740-100\over500000}\\
 &={7044\over500000}
 ={1761\over125000}>0.
\end{aligned}
\tag{4.3}
\]

## 5. Complete closure

### Theorem 5.1

Every honest exact-first-carry period-fourteen cyclic Apéry clock satisfies

\[
 \boxed{\Phi(W)>0.}
\tag{5.1}
\]

#### Proof

If the overlap depth `H<=2`, then `u<=6` and

\[
 360H+\tau\le720+(u+1)\le727<860,
\]

so the reflected-depth theorem applies.  If `H>=3`, then `H<=u` and
(2.3) give `3<=u<=6`; every such value is strictly positive by (4.2).
Finally `Phi(W)>=E(s)`. \(\square\)

## 6. Scope and frozen dependencies

| role | file | SHA-256 |
|---|---|---|
| prefix minimum, ray identity, and depth theorem | `MATH_THEOREM_APERY_MULTIDEFECT_PREFIX_MINIMUM_AND_REFLECTED_RAY_DEPTH_REDUCTION_20260804.md` | `28c714f8eae3ae56c22a1c7c643f583e73b891e1abf2f66e4e866d831b7eb21e` |
| terminal-suffix envelope | `MATH_LEMMA_APERY_TERMINAL_SUFFIX_MAXIMUM_AND_QUARTER_CUTOFF_20260804.md` | `6ef133e15f8635db9a91fb837ef2df65fadedc6a52ff923b0b5895f215324639` |
| global, one-fifth, and quarter upper bounds | `MATH_THEOREM_APERY_PERIOD11_12_GLOBAL_QUARTER_LEDGER_COMPLETE_POSITIVITY_20260804.md` | `fb9139813f93d8e5450b8ab3cee0238c289cd573222d0d05fd6174040fdbe601` |
| one-mode critical-point classification | `MATH_THEOREM_COMPLEMENTARY_PAIR_TRAIN_AND_H4_INERT_SCALAR_REDUCTION_20260804.md` | `fc8b2dee92dd3bb9afab390c8507db51fec05c6ca4e9d46ac4948c7422d042a7` |
| compact endpoint bounds | `MATH_THEOREM_H4_INERT_COMPACT_GAUSSIAN_GATE_CLOSURE_20260804.md` | `f88e8ac246d0533f018b7d713cfc6f09e14872d2f2026e7e29b3bc40f3a6062b` |
| theta sign and absolute bound | `MATH_LEMMA_THETA_HALF_INTERVAL_MONOTONICITY_AND_HALF_ROOT_SUMS_20260804.md` | `f974aeda114df4c933a396c06de51596bccd2fea18066412d45f7a18df62a0e3` |
