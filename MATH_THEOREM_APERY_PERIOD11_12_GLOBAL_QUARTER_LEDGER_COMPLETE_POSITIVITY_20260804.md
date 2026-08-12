# Periods eleven and twelve: global/quarter ray ledgers and complete positivity

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical theorem.  It proves that every
honest exact-first-carry cyclic Apéry clock of period eleven or twelve has
strictly positive formal Bellman functional.  The proof uses the
terminal-suffix cutoff, the sharpened global compact bound already proved
inside the period-ten argument, and the earlier exact quarter value.  No
computation or search is used.  It does not address periods at least
thirteen, threshold overshoot, later first crossing, or finite physical
shoulders.

Put

\[
 A={\sqrt\pi\over2},\qquad
 F_A(w)=\sum_{q\ge0}K(qA+w),\qquad
 f(x)=F_A(Ax),
\tag{0.1}
\]

and

\[
                         C=F_A(0),\qquad
                         g(x)=\rho(Ax).
\]

## 1. Two compact constants

The period-ten proof actually establishes the stronger global estimate

\[
 \boxed{
 f(x)<G:={1079\over20000}
 \qquad(0\le x\le1/2).}
\tag{1.1}
\]

Indeed, its Jacobi-completion argument gives \(f(x)<1079/20000\) on
\([0,1/5]\), while its monotonicity and one-fifth anchor give

\[
 f(x)\le f(1/5)<{101\over2000}
                    <{1079\over20000}
\]

on \([1/5,1/2]\).

The exact quarter audit supplies the sharper value

\[
 \boxed{
 f(1/4)<Q:={1129\over25000}.}
\tag{1.2}
\]

Together with monotone decrease on \([1/4,1/2]\),

\[
                         f(y)<Q
 \qquad(1/4\le y<1/2).
\tag{1.3}
\]

We also retain

\[
 C>m_0:={57\over1400},
\qquad
 f(x)>m_0\quad(0\le x\le1/4),
\tag{1.4}
\]

and

\[
 |g(x)|<\varepsilon:={1\over20000},
\qquad
 g(x)>0\quad(1/4\le x\le1/2).
\tag{1.5}
\]

## 2. A uniform terminal cutoff

Let an honest exact-first-carry table have period \(h\in\{11,12\}\):

\[
 0=s_0<s_1<\cdots<s_{h-1}<P,
 \qquad
 P+s_1=A.
\tag{2.1}
\]

Put

\[
 a=s_1,\qquad \alpha={a\over A}.
\]

For the reflected rays define

\[
 X_i={s_{i+1}\over A},
 \qquad
 Y_i={A-s_{h-i}\over A},
 \qquad 1\le i\le u.
\tag{2.2}
\]

Then \(0<X_i\le Y_i<1/2\).  Terminal-suffix maximality gives

\[
                         Y_i>{i\over h}.
\tag{2.3}
\]

For both \(h=11\) and \(h=12\),

\[
                         \boxed{Y_i>{1\over4}
                         \qquad(i\ge3).}
\tag{2.4}
\]

For \(h=11\), this follows from \(3/11>1/4\).  For \(h=12\),
equation (2.3) is strict and gives \(Y_3>3/12=1/4\).

## 3. Two ray prices

### Lemma 3.1 (global pair)

Every reflected pair satisfies

\[
 \boxed{
 f(X)-f(Y)+g(Y)>m_0-G-\varepsilon.}
\tag{3.1}
\]

#### Proof

If \(X<1/4\), use (1.1), (1.4), and the absolute theta bound.
If \(X\ge1/4\), then \(X\le Y<1/2\), so quarter-interval decrease makes
the compact difference nonnegative and \(g(Y)>0\).  This is stronger than
(3.1). \(\square\)

### Lemma 3.2 (quarter pair)

If \(Y>1/4\), then

\[
 \boxed{
 f(X)-f(Y)+g(Y)>m_0-Q.}
\tag{3.2}
\]

#### Proof

If \(X<1/4\), equations (1.3)--(1.5) give (3.2).  If \(X\ge1/4\),
monotone decrease makes the compact difference nonnegative, while
\(g(Y)>0\). \(\square\)

Thus the first two pairs may always be priced by (3.1), and every later
pair is priced by (3.2) because of (2.4).

## 4. Exhaustive chamber lists and middle terms

The disjoint-ray inequality

\[
                         u+1<h-u
\]

gives

\[
\begin{array}{c|c|c}
h&u_{\max}&\text{new chambers after }H\le2\\ \hline
11&4&(u,H)=(3,3),(4,3),(4,4)\\
12&5&(u,H)=(3,3),(4,3),(4,4),
        (5,3),(5,4),(5,5).
\end{array}
\tag{4.1}
\]

The exact endpoint identity is

\[
\boxed{
\begin{aligned}
 E(s)
 ={}&C+g(\alpha)
 +\sum_{i=1}^u
   \bigl(f(X_i)-f(Y_i)+g(Y_i)\bigr)\\
 &+\sum_{r=u+2}^{h-u-1}f(s_r/A),
\end{aligned}}
\tag{4.2}
\]

with \(\Phi(W)\ge E(s)\).

The number of displayed middle terms is

\[
                         h-2u-2.
\]

Explicitly:

\[
\begin{array}{c|c|c}
h&u&\text{middle residues}\\ \hline
11&3&5,6,7\\
11&4&6\\
12&3&5,6,7,8\\
12&4&6,7\\
12&5&\varnothing.
\end{array}
\tag{4.3}
\]

Every such middle train is strictly positive.  They remain explicit in
(4.2) and are discarded only at the final lower-bound step.

## 5. One ledger for every new chamber

The minimum-gap theorem gives \(P\ge ha\), so

\[
 0<\alpha={a\over P+a}\le{1\over h+1}<1/2
\]

and therefore

\[
                         g(\alpha)>-\varepsilon.
\tag{5.1}
\]

Price the first two pairs by Lemma 3.1 and all \(u-2\) remaining pairs by
Lemma 3.2.  After retaining and then discarding the positive middle terms,
(4.2) gives the uniform ledger

\[
\boxed{
 E(s)>
 (u+1)m_0-2G-(u-2)Q-3\varepsilon.}
\tag{5.2}
\]

The three theta charges are exactly \(g(\alpha),g(Y_1),g(Y_2)\).
All later theta terms are positive.

For \(u=3\), equation (5.2) gives

\[
\begin{aligned}
 E(s)
 &>{4\cdot57\over1400}
   -2{1079\over20000}
   -{1129\over25000}
   -{3\over20000}\\
 &={6753\over700000}>0.
\end{aligned}
\tag{5.3}
\]

For \(u=4\),

\[
\begin{aligned}
 E(s)
 &>{5\cdot57\over1400}
   -2{1079\over20000}
   -2{1129\over25000}
   -{3\over20000}\\
 &={3641\over700000}>0.
\end{aligned}
\tag{5.4}
\]

For \(u=5\), which occurs only at period twelve,

\[
\begin{aligned}
 E(s)
 &>{6\cdot57\over1400}
   -2{1079\over20000}
   -3{1129\over25000}
   -{3\over20000}\\
 &={529\over700000}>0.
\end{aligned}
\tag{5.5}
\]

## 6. Complete closures

### Theorem 6.1

Every honest exact-first-carry period-eleven cyclic Apéry clock satisfies

\[
                         \boxed{\Phi(W)>0.}
\tag{6.1}
\]

### Theorem 6.2

Every honest exact-first-carry period-twelve cyclic Apéry clock satisfies

\[
                         \boxed{\Phi(W)>0.}
\tag{6.2}
\]

#### Proof of both theorems

The chamber list (4.1) is exhaustive after \(H\le2\).
Equations (5.3)--(5.5) close every listed chamber.

If \(H\le2\), then \(\tau\le u+1\le6\), so

\[
                         360H+\tau\le726<860.
\]

The general reflected-ray depth theorem closes those remaining cases.
Finally \(\Phi(W)\ge E(s)\). \(\square\)

## 7. Scope and frozen dependencies

The theorem closes the complete exact-first-carry formal branches at
periods eleven and twelve.  It does not address threshold overshoot, later
first crossing, finite physical shoulders, or the corresponding
all-period problem.

| role | file | SHA-256 |
|---|---|---|
| prefix-minimum, terminal cutoff, ray identity, depth theorem | MATH_THEOREM_APERY_MULTIDEFECT_PREFIX_MINIMUM_AND_REFLECTED_RAY_DEPTH_REDUCTION_20260804.md | 28c714f8eae3ae56c22a1c7c643f583e73b891e1abf2f66e4e866d831b7eb21e |
| compact lower bounds and quarter monotonicity | MATH_THEOREM_COMPLEMENTARY_PAIR_TRAIN_AND_H4_INERT_SCALAR_REDUCTION_20260804.md | fc8b2dee92dd3bb9afab390c8507db51fec05c6ca4e9d46ac4948c7422d042a7 |
| sharp quarter value | MATH_THEOREM_H4_INERT_COMPACT_GAUSSIAN_GATE_CLOSURE_20260804.md | f88e8ac246d0533f018b7d713cfc6f09e14872d2f2026e7e29b3bc40f3a6062b |
| theta sign and absolute bound | MATH_LEMMA_THETA_HALF_INTERVAL_MONOTONICITY_AND_HALF_ROOT_SUMS_20260804.md | f974aeda114df4c933a396c06de51596bccd2fea18066412d45f7a18df62a0e3 |
| global compact proof | MATH_THEOREM_APERY_PERIOD10_H34_ONE_FIFTH_TRAIN_AND_COMPLETE_POSITIVITY_20260804.md | 1697def0ed72f30c6972a706a968a3efed68e470ebe511b813c7eedc7259095e |
