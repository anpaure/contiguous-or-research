# The exact two-point alternative behind the Gaussian PBBS packing gate

Date: 2026-07-26

Method: pure mathematics only.

## 0. Statement

Let \(\tau\) be the PBBS quotient permutation on the \(B=\operatorname
{Cat}_r\) Dyck roots.  Fix \(H=\lceil A\sqrt r\rceil\), discard quotient
cycles of length at most \(H+1\), and let \(E_H\) be the remaining roots
which start an eligible omitted-label return.  Put

\[
 R_H=|E_H|,
\qquad
 \mathcal C_H=
 \sum_{t=1}^{H+1}|E_H\cap\tau^{-t}E_H|.
\tag{0.1}
\]

Then the quotient residence packing number satisfies

\[
 \boxed{
 \overline\nu_H
 \ge {R_H^2\over R_H+2\mathcal C_H}.}
\tag{0.2}
\]

Consequently, if along any subsequence

\[
 R_H\ge c_A{B\over H}
 \quad\hbox{and}\quad
 \mathcal C_H=O_A(R_H),
\tag{0.3}
\]

then

\[
 \overline\nu_H=\Omega_A(B/H),
\tag{0.4}
\]

and \((ST_A)\) is false.  Conversely, if \((ST_A)\) holds while
\(R_H\ge c_AB/H\), then necessarily

\[
 \boxed{\mathcal C_H/R_H\longrightarrow\infty.}
\tag{0.5}
\]

Thus at critical start density the missing theorem is not merely a
one-point rare-return estimate.  It is a divergent short-lag clustering
theorem for the actual PBBS return-start process.

## 1. Conflict graph

Make a graph \(G_H\) with vertex set \(E_H\).  Join two starts when their
actual quotient residence intervals share an edge.  An independent set in
\(G_H\) is exactly an edge-disjoint residence family, so

\[
 \alpha(G_H)=\overline\nu_H.
\tag{1.1}
\]

Every eligible interval uses at most \(H+1\) consecutive quotient edges.
On a retained cycle it is nonwrapping.  If two such intervals overlap,
then in one of the two cyclic orientations their starts are separated by
some \(1\le t\le H+1\).  Therefore

\[
 |E(G_H)|\le\mathcal C_H.
\tag{1.2}
\]

No independence or stationarity assumption is used here; (1.2) is just
the support geometry of two short intervals.

## 2. Turan--Cauchy bound

For any finite graph with \(R\) vertices and \(C\) edges, the greedy
degree bound followed by Cauchy--Schwarz gives

\[
 \alpha(G)
 \ge\sum_{v}{1\over d(v)+1}
 \ge {R^2\over\sum_v(d(v)+1)}
 ={R^2\over R+2C}.
\tag{2.1}
\]

Apply (2.1) to \(G_H\) and use (1.2).  This proves (0.2).  Statements
(0.3)--(0.5) are immediate.

## 3. Relation to the clustered seam

The separate result `PBBS_ST_CS_EQUIVALENCE_20260726.md` proves, after the
already established sub-Gaussian-height deletion,

\[
 \mathfrak S_H=o(B)
 \quad\Longleftrightarrow\quad
 \overline\nu_H=o(B/H).
\tag{3.1}
\]

Combining (0.5) and (3.1) gives a sharp implication boundary.  At a
critical one-point density \(R_H\asymp B/H\), both the packing route and
the clustered-staircase route can succeed only if a typical eligible PBBS
start has a number of other eligible starts within quotient distance
\(H\) that tends to infinity.  Bounded short-lag correlation is already a
rigorous obstruction to both routes.

## 4. What remains mathematical

Equation (0.2) reduces any analytic falsification of \((ST_A)\) to two
PBBS statements:

1. a lower bound \(R_H=\Omega_A(B/H)\) for genuine long-cycle starts; and
2. an upper bound \(\mathcal C_H=O_A(R_H)\).

Alternatively, a proof of \((ST_A)\) at critical start density must prove
the opposite, genuinely dynamical conclusion (0.5).  Marginal height,
deficit, Pascal-slot, and fixed-core estimates do not decide this
two-time quantity.
