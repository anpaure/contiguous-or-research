# Independent audit: collar-hole majorization and the fixed-slack barrier

**Date:** 2026-08-03  
**Audited theorem:**  
MATH_THEOREM_COLLAR_HOLE_MAJORISATION_AND_FIXED_SLACK_WHOLE_CHUNK_BARRIER_20260803.md  
**Audited theorem SHA256:**  
bb145cf2bbd92d7fed51151fdbc2c5d908e35dc5bc20e056451701711a3659ef

**Verdict:** PASS after expanding the conjugate Gale proof and tightening
the conclusion to the whole-chunk, remainder-preserving repair model. No
computation is used.

## 1. Gale flow criterion

Use a network with source-to-column capacities \(n_j\), unit
column-to-row capacities, and row-to-sink capacities \(c_i\). An integral
flow of value \(\sum_jn_j\) is exactly a zero--one incidence matrix with
the required column sums and row upper bounds.

For a column family \(J\), its entries can use at most
\(\min(c_i,|J|)\) units at row \(i\). Max-flow/min-cut therefore gives
exactly

\[
 \sum_{j\in J}n_j\le\sum_{i=1}^W\min(c_i,|J|)
 \qquad(J\subseteq[a]).
\tag{1.1}
\]

This is both necessary and sufficient.

## 2. Conjugate form

Sort \(c_1\le\cdots\le c_W\). Assume

\[
 \sum_{i=1}^x c_i
 \ge\sum_{j=1}^a(n_j-(W-x))_+
 \qquad(1\le x\le W).
\tag{2.1}
\]

For a fixed \(J\), put \(q=|J|\), and let \(x\) be the number of capacities
strictly below \(q\). Then

\[
 \sum_i\min(c_i,q)=\sum_{i\le x}c_i+q(W-x).
\]

Since

\[
 n_j\le(n_j-(W-x))_++(W-x),
\]

summing over \(J\), enlarging the positive-part sum to all columns, and
using (2.1) proves (1.1).

Conversely, fix \(x\) and set

\[
 J_x=\{j:n_j>W-x\},\qquad q=|J_x|.
\]

Criterion (1.1) gives

\[
 \sum_{j\in J_x}n_j
 \le\sum_i\min(c_i,q)
 \le\sum_{i\le x}c_i+q(W-x).
\]

After subtracting \(q(W-x)\), this is (2.1). At \(x=W\), it is the total
capacity inequality. Thus the Gale and conjugate formulations in Theorem
1.1 are exactly equivalent, not merely one-way necessary conditions.

## 3. Forced load on any distinguished rows

Fix any \(X\) of \(A\) rows. Column \(j\) can put at most \(W-A\) entries
outside \(X\), so every assignment puts at least

\[
 (n_j-(W-A))_+=(A-H_j)_+
\]

entries inside \(X\), where \(H_j=W-n_j\). Summing columns gives

\[
 L(A)=\sum_{j=1}^a(A-H_j)_+.
\tag{3.1}
\]

This lower bound is independent of containment, owner choice, or collar
chainization. It is sharp one column at a time: maximize placements outside
\(X\), then put the remainder inside. As correctly stated in the theorem,
this projected sharpness does not impose simultaneous row capacities or
named-target nesting.

## 4. Hole estimate

For distance \(j\) below the middle,

\[
 p_{r-j}=\prod_{t=0}^{j-1}{r-t\over r+t+1}
 =\prod_{t=0}^{j-1}
 \left(1-{2t+1\over r+t+1}\right).
\]

The elementary product union bound gives

\[
 1-p_{r-j}
 \le\sum_{t=0}^{j-1}{2t+1\over r}
 ={j^2\over r}.
\tag{4.1}
\]

Since

\[
 H_j=W-\left(\binom{2r}{r-j}-b_{r-j}\right)
 =W(1-p_{r-j})+b_{r-j},
\]

and \(b_{r-j}\le B_\partial\), one obtains

\[
 H_j\le {j^2\over r}W+B_\partial.
\tag{4.2}
\]

For the optimal triangular boundary, \(B_\partial=O(r)=o(W)\).

## 5. Positive-density full chunks

The audited predecessor theorem supplies, after boundary deletion,

\[
 A\ge(\gamma-o(1))W,\qquad
 \gamma=e^{-(7/8+\sqrt\pi)^2}>0.
\]

Hence \(A\ge\gamma W/2\) eventually. Put

\[
 J_0=\left\lfloor\sqrt{\gamma r/8}\right\rfloor.
\]

Because \(\gamma<1\), \(J_0<a=\lceil7\sqrt r/8\rceil\) eventually. For
\(j\le J_0\), (4.2) gives

\[
 H_j\le{\gamma\over8}W+B_\partial
 \le{\gamma\over4}W
\]

for large \(r\). Therefore

\[
 (A-H_j)_+\ge{\gamma\over4}W
\]

on all these collar ranks, and

\[
 L(A)\ge{\gamma\over4}W
 \left\lfloor\sqrt{\gamma r/8}\right\rfloor
 =\Omega(\sqrt r\,W).
\tag{5.1}
\]

The constants and floor do not affect the order.

## 6. Fixed-slack whole-chunk barrier

If the \(A\) full length-\(d\) chunks remain unchanged on distinct owner
rows at total depth \(d+C\), those rows have at most \(C\) collar slots
each. Their aggregate collar capacity is at most \(AC\), whereas Section 3
forces \(L(A)\). Thus

\[
 AC\ge L(A)
\tag{6.1}
\]

is necessary. Since \(A\le W\) and \(L(A)=\Omega(\sqrt r\,W)\), (6.1)
fails for every \(C=o(\sqrt r)\), in particular every fixed \(C\).

This is a rank-incidence obstruction and therefore remains valid before
testing bottom containment or literal nesting.

## 7. Export lower bound and its exact scope

In the remainder-preserving model, original chunk \(i\) retains a
designated distinct row and keeps its entire unexported remainder there.
After exporting \(e_i\) targets, that row has residual load \(d-e_i\) and
collar capacity at most \(C+e_i\). The \(A\) designated rows therefore
have total collar capacity at most

\[
 AC+\sum_{i=1}^A e_i.
\]

The forced-load formula applies to this fixed \(A\)-row family, yielding

\[
 \sum_{i=1}^A e_i\ge L(A)-AC.
\tag{7.1}
\]

For \(C=o(\sqrt r)\), the right side is
\(\Omega(\sqrt r\,W)\).

The exported targets may be placed elsewhere and are not counted as
omissions. If an original chunk is dissolved completely and its designated
row is dropped, the fixed-\(A\)-row premise no longer applies; that is a
global rechainization outside formula (7.1). The theorem now states this
boundary explicitly and does not promote (7.1) to an unrestricted lower
bound on all constructions.

## 8. Relation to the top-cap bridge

At \(C=1\), the preceding bound is still
\(\Omega(\sqrt r\,W)\). Thus the exact residual-to-rank-\((r-1)\) cap
matching does not leave enough capacity on full residual rows for the
remaining collar under remainder preservation.

This does not invalidate that bridge: it exactly covers the residual bank
plus the top collar rank. It says that completing ranks
\(r-a,\ldots,r-2\) needs a bulk correlated rechainization, a different
initial load distribution, or another construction outside the fixed
whole-chunk face.

## 9. Scope repairs

The theorem was patched so that:

1. all row capacities are explicitly nonnegative integers;
2. sufficiency of the conjugate Gale inequalities is proved directly;
3. the outcome and \(d+1\) consequence explicitly say
   remainder-preserving face;
4. the export formula requires one distinct designated row per original
   chunk;
5. dropping those rows through complete global dissolution is expressly
   outside the exact formula.

Within this scope, the majorization, hole, full-chunk, and export bounds
are proof-safe.
