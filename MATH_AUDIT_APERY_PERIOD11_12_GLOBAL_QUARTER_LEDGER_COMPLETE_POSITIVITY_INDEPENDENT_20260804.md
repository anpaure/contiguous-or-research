# Independent audit: period-eleven/twelve global-quarter closure

**Date:** 2026-08-04  
**Audited theorem:**  
MATH_THEOREM_APERY_PERIOD11_12_GLOBAL_QUARTER_LEDGER_COMPLETE_POSITIVITY_20260804.md  
**Audited SHA-256:**  
fb9139813f93d8e5450b8ab3cee0238c289cd573222d0d05fd6174040fdbe601  
**Verdict:** **GO.**  The promoted compact constants, terminal cutoff,
chamber exhaustion, middle-term counts, theta pricing, and all three
rational margins are exact.  No computation or search is used.

## 1. Promoted train constants

The period-ten theorem proves, before weakening its displayed global
constant, that

\[
 f(x)<{1079\over20000}
 \qquad(0\le x\le1/5).
\]

On the complementary interval it proves monotone decrease and

\[
 f(x)\le f(1/5)<{101\over2000}
 ={1010\over20000}<{1079\over20000}.
\]

Thus the promoted global bound

\[
                         f(x)<G:={1079\over20000}
\tag{1.1}
\]

is a literal consequence of the frozen period-ten proof, not a new
assumption.

The exact quarter certificate in the H4 compact-Gaussian theorem is

\[
                         f(1/4)<Q:={1129\over25000}.
\tag{1.2}
\]

Because \(f\) decreases on \([1/4,1/2]\), equation (1.2) applies to every
post-quarter reflected endpoint.

The remaining constants are

\[
 m_0={57\over1400},\qquad
 \varepsilon={1\over20000},
\]

with \(C>m_0\), \(f(x)>m_0\) for \(x\le1/4\),
\(|g(x)|<\varepsilon\), and \(g(x)>0\) for \(x\ge1/4\).

## 2. Terminal cutoff

For period \(h\), terminal-suffix maximality gives

\[
 Y_i\ge{a+iP/h\over P+a}.
\]

Subtracting \(i/h\) yields the exact strict excess

\[
 {a+iP/h\over P+a}-{i\over h}
 ={(h-i)a\over h(P+a)}>0.
\tag{2.1}
\]

Therefore \(Y_i>i/h\).  At both periods under audit,

\[
\begin{aligned}
h=11:&\qquad Y_i>1/4\quad(i\ge3),\\
h=12:&\qquad Y_3>3/12=1/4,
                 \quad Y_i>1/4\quad(i\ge3).
\end{aligned}
\tag{2.2}
\]

Thus exactly the first two reflected pairs may lie before the quarter;
every later pair has positive theta and the sharp quarter compact bound.

## 3. Pair estimates

For any \(0<X\le Y<1/2\):

* if \(X<1/4\), equations (1.1) and the compact lower bound give

  \[
  f(X)-f(Y)+g(Y)>m_0-G-\varepsilon;
  \]

* if \(X\ge1/4\), compact monotonicity and positive theta give a
  nonnegative value.

Hence the global pair price is

\[
                         m_0-G-\varepsilon.
\tag{3.1}
\]

If \(Y>1/4\), then either \(X<1/4\), in which case

\[
 f(X)-f(Y)+g(Y)>m_0-Q,
\]

or \(X\ge1/4\), in which case the pair is nonnegative.  Thus every
post-quarter pair costs at most

\[
                         m_0-Q.
\tag{3.2}
\]

The first two pairs are safely priced by (3.1).  Equation (2.2) prices
all remaining pairs by (3.2).  Finally \(g(\alpha)>-\varepsilon\).
Therefore exactly three possible theta losses are included.

## 4. Chamber exhaustion

The disjoint-ray inequality is \(u+1<h-u\).

For \(h=11\), it gives \(u\le4\).  After \(H\le2\), the exhaustive list is

\[
                         (3,3),(4,3),(4,4).
\]

For \(h=12\), it gives \(u\le5\).  The exhaustive list is

\[
 (3,3),(4,3),(4,4),(5,3),(5,4),(5,5).
\]

The middle-residue count is \(h-2u-2\).  Direct substitution gives

\[
\begin{array}{c|c|c}
h&u&\text{middle residues}\\ \hline
11&3&5,6,7\\
11&4&6\\
12&3&5,6,7,8\\
12&4&6,7\\
12&5&\varnothing.
\end{array}
\]

All displayed middle terms are strictly positive.  The theorem preserves
them in the exact endpoint identity and discards them only when taking the
uniform lower bound.

## 5. Rational ledgers

For every new chamber,

\[
 E(s)>(u+1)m_0-2G-(u-2)Q-3\varepsilon.
\tag{5.1}
\]

Use denominator \(700000\).  The common entries are

\[
\begin{aligned}
m_0&={28500\over700000},\\
2G&={75530\over700000},\\
Q&={31612\over700000},\\
3\varepsilon&={105\over700000}.
\end{aligned}
\]

For \(u=3\),

\[
 4m_0-2G-Q-3\varepsilon
 ={114000-75530-31612-105\over700000}
 ={6753\over700000}>0.
\]

For \(u=4\),

\[
 5m_0-2G-2Q-3\varepsilon
 ={142500-75530-63224-105\over700000}
 ={3641\over700000}>0.
\]

For \(u=5\),

\[
 6m_0-2G-3Q-3\varepsilon
 ={171000-75530-94836-105\over700000}
 ={529\over700000}>0.
\]

All arithmetic in the theorem is correct.

## 6. Prior-depth branch and scope

For \(H\le2\), periods eleven and twelve have \(u\le5\), so
\(\tau\le u+1\le6\).  Hence

\[
                         360H+\tau\le726<860,
\]

and the frozen reflected-depth theorem applies.

Combining that branch with the exhaustive positive ledgers proves every
honest exact-first-carry formal clock positive at periods eleven and
twelve.

Threshold overshoot, later first crossing, finite physical shoulders, and
periods at least thirteen remain outside scope.

**Audit verdict:** **PASS.**
