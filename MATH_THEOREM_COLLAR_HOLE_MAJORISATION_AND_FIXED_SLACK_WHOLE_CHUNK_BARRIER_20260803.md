# Collar-hole majorization and the fixed-slack whole-chunk barrier

**Date:** 2026-08-03  
**Status:** unconditional rank-incidence min--max theorem and sharp
obstruction. No computation is used. The obstruction applies to the
parity-block residual chunks kept whole; it does not rule out a globally
rechainized lower ideal.

## 0. Outcome

Continue from
MATH_THEOREM_CROSS_SCD_CAPACITATED_ATTACHMENT_UNIT_BARRIER_AND_TOP_CAP_20260803.md.
That theorem attaches every residual chunk to a distinct rank-\((r-1)\)
cap at depth \(d+1\), but leaves collar ranks
\[
                         r-a,\ldots,r-2.
\]

The remaining collar cannot be placed on the current whole-chunk,
remainder-preserving face with any fixed additive slack.

The reason is stronger than bottom-containment failure. Let \(X\) be any
\(A\) owner rows, and let
\[
 n_j=\binom{2r}{r-j}-b_{r-j},
 \qquad
 H_j=W-n_j
\tag{0.1}
\]
be respectively the nonboundary target count and hole count at collar
distance \(j\). Every exact collar assignment forces at least
\[
 \boxed{
 L(A)=\sum_{j=1}^{a}(A-H_j)_+}
\tag{0.2}
\]
collar targets into the rows \(X\), regardless of containment or
chainization.

The residual construction has
\[
 A\ge(\gamma-o(1))W,
 \qquad
 \gamma=e^{-(7/8+\sqrt\pi)^2}>0,
\tag{0.3}
\]
full length-\(d\) chunks after the \(O(r)\) boundary deletion. For this
value of \(A\),
\[
                         L(A)=\Omega(\sqrt r\,W).
\tag{0.4}
\]

At total depth \(d+C\), unmodified full chunks have only \(AC\) collar
capacity. Thus every fixed \(C\), and even every \(C=o(\sqrt r)\), fails
the rank-incidence majorization before literal bottom containment is
tested.

More sharply, in the remainder-preserving model, if \(e_i\) residual
targets are exported from full chunk \(i\) while every original chunk keeps
one distinct designated row containing its entire unexported remainder,
then
\[
 \boxed{
 \sum_{i\in X}e_i\ge L(A)-AC
 =\Omega(\sqrt r\,W).}
\tag{0.5}
\]

Consequently the \(d+1\) top-cap bridge is exact but cannot be completed
within this remainder-preserving repair model by an \(O(W)\) collection of
one-cell fixes. The parity-block residual bank must undergo a bulk
\(\Omega(\sqrt r\,W)\) rechainization, or it must be replaced by a
construction whose loads are correlated with the collar holes from the
outset.

## 1. Exact rank-incidence capacity theorem

Let \(a\) collar ranks be represented by columns, let \(n_j\) be the
number of named targets in column \(j\), and let
\(c_1,\ldots,c_W\in\mathbb Z_{\ge0}\) be the available collar capacities
of the owner rows. Ignore containment and ask only for a zero--one
incidence matrix
\[
 y\in\{0,1\}^{W\times a},
 \qquad
 \sum_i y_{ij}=n_j,
 \qquad
 \sum_j y_{ij}\le c_i.
\tag{1.1}
\]

### Theorem 1.1 (Gale--flow criterion)

The matrix (1.1) exists if and only if, for every column family
\(J\subseteq[a]\),
\[
 \sum_{j\in J}n_j
 \le
 \sum_{i=1}^{W}\min\{c_i,|J|\}.
\tag{1.2}
\]

Equivalently, after sorting
\[
 c_1\le c_2\le\cdots\le c_W,
\]
one has total capacity
\[
 \sum_i c_i\ge\sum_jn_j
\tag{1.3}
\]
and, for every \(1\le x\le W\),
\[
 \sum_{i=1}^{x}c_i
 \ge
 \sum_{j=1}^{a}\bigl(n_j-(W-x)\bigr)_+.
\tag{1.4}
\]

### Proof

Build the flow network
\[
 \text{source}\longrightarrow\text{column }j
 \longrightarrow\text{row }i
 \longrightarrow\text{sink}
\]
with capacities \(n_j,1,c_i\), respectively. Integral max flow is exactly
(1.1). The max-flow min-cut inequalities, after minimizing over the row
side of a cut, are (1.2). This is the usual bipartite degree-sequence or
Gale criterion.

For (1.4), fix a set \(X\) of \(x\) rows. Column \(j\) can place at most
\(W-x\) of its targets outside \(X\), so it forces
\[
                         (n_j-(W-x))_+
\]
targets into \(X\). The smallest total capacity among \(x\) rows is
\(\sum_{i\le x}c_i\), proving necessity.

For completeness, the equivalence with (1.2) is exact. Assume (1.4), fix
\(J\subseteq[a]\), and put \(q=|J|\). Let \(x\) be the number of sorted
capacities strictly below \(q\). Then
\[
 \sum_i\min\{c_i,q\}=\sum_{i\le x}c_i+q(W-x).
\]
For each \(j\),
\[
 n_j\le(n_j-(W-x))_++(W-x).
\]
Summing this over \(J\), enlarging the positive-part sum to all columns,
and applying (1.4) proves (1.2).

Conversely, fix \(x\) and let
\[
 J_x=\{j:n_j>W-x\},\qquad q=|J_x|.
\]
By (1.2),
\[
 \sum_{j\in J_x}n_j
 \le\sum_i\min\{c_i,q\}
 \le\sum_{i\le x}c_i+q(W-x).
\]
Subtracting \(q(W-x)\) gives (1.4). At \(x=W\), (1.4) is exactly the total
capacity row (1.3). Thus the two forms are equivalent.
\(\square\)

The theorem concerns only rank incidences. An ownerwise collar flag must
additionally make its selected named targets nested. Therefore failure of
(1.4) is a fortiori a failure of every literal collar attachment.

## 2. Forced load on a distinguished row family

For any fixed \(X\subseteq[W]\) of size \(A\), column \(j\) can place at
most \(W-A\) targets outside \(X\). Hence every exact assignment satisfies
\[
 \sum_{i\in X}y_{ij}
 \ge n_j-(W-A)
 =A-H_j
\]
when the right side is positive.

### Corollary 2.1 (exact forced-collar formula)

Every \(A\)-row family carries at least the quantity \(L(A)\) in (0.2).
At the rank-incidence level this bound is sharp column by column.

### Proof

Sum the preceding inequalities over the collar ranks. For sharpness with
only the row family \(X\) prescribed, place
\(\min\{n_j,W-A\}\) entries of column \(j\) outside \(X\) and the rest
inside. Columns are independent at this projected level. \(\square\)

The sharpness assertion does not impose row capacities simultaneously and
does not claim nested named flags; it identifies the exact amount which no
later structure can avoid.

## 3. Central collar holes are too sparse

For \(1\le j<r\),
\[
 p_{r-j}
 =\frac{\binom{2r}{r-j}}{\binom{2r}{r}}
 =\prod_{t=0}^{j-1}\frac{r-t}{r+t+1}.
\tag{3.1}
\]

### Lemma 3.1 (elementary hole bound)

\[
                         1-p_{r-j}\le\frac{j^2}{r}.
\tag{3.2}
\]

### Proof

Write the \(t\)-th factor in (3.1) as
\[
 1-\frac{2t+1}{r+t+1}.
\]
For numbers \(z_t\in[0,1]\),
\[
 1-\prod_t(1-z_t)\le\sum_tz_t.
\]
Since \(r+t+1\ge r\),
\[
 1-p_{r-j}
 \le\sum_{t=0}^{j-1}\frac{2t+1}{r}
 =\frac{j^2}{r}.
\]
\(\square\)

Let the total boundary size be \(B_\partial=O(r)\), as in the optimal
triangular ledger. Equation (0.1) and Lemma 3.1 give
\[
 H_j\le\frac{j^2}{r}W+B_\partial.
\tag{3.3}
\]

## 4. Positive-density full chunks force macroscopic collar load

The full-chunk theorem gives, after boundary deletion,
\[
 A\ge(\gamma-o(1))W.
\]
For all sufficiently large \(r\), take
\[
                         A\ge\frac{\gamma}{2}W.
\tag{4.1}
\]

Put
\[
 J_0=\left\lfloor\sqrt{\frac{\gamma r}{8}}\right\rfloor.
\tag{4.2}
\]
Since \(J_0<a\) for all sufficiently large \(r\), these are collar ranks.
For every \(1\le j\le J_0\), (3.3) and
\(B_\partial=o(W)\) give
\[
                         H_j\le\frac{\gamma}{4}W.
\tag{4.3}
\]
Therefore
\[
 (A-H_j)_+\ge\frac{\gamma}{4}W
\]
throughout this interval.

### Theorem 4.1 (fixed-slack whole-chunk obstruction)

\[
 L(A)\ge
 \frac{\gamma}{4}W
 \left\lfloor\sqrt{\frac{\gamma r}{8}}\right\rfloor
 =\Omega(\sqrt r\,W).
\tag{4.4}
\]

If the \(A\) full chunks are retained unchanged at total depth \(d+C\),
then necessarily
\[
 AC\ge L(A).
\tag{4.5}
\]
Consequently (4.5) fails for every \(C=o(\sqrt r)\), including every
absolute constant.

### Proof

Equation (4.4) is the contribution of the first \(J_0\) summands in
(0.2). A full chunk already has \(d\) marked targets, so at depth \(d+C\)
its owner row has collar capacity at most \(C\). The total collar capacity
of the \(A\) distinguished rows is at most \(AC\). Corollary 2.1 forces
the lower bound \(L(A)\), proving (4.5) and the conclusion. \(\square\)

This argument permits arbitrary noncontiguous collar rank patterns. It
does not assume one SCD, saturated collar chains, bottom containment, or
any particular owner assignment.

## 5. Exact target-migration lower bound

Suppose each original full chunk \(i\) retains one designated, distinct
owner row after exporting \(e_i\) of its residual targets, and its entire
unexported remainder stays together on that row. This is the
**remainder-preserving repair model**. Its residual load becomes
\(d-e_i\), so at total depth \(d+C\) its collar capacity is at most
\(C+e_i\). If a chunk is dissolved completely and no designated row is
retained, that operation is a global rechainization and lies outside this
exact formula.

### Theorem 5.1 (bulk splice lower bound)

Every attachment in this remainder-preserving repair model satisfies
\[
 \sum_{i=1}^{A}e_i
 \ge L(A)-AC.
\tag{5.1}
\]

For \(C=o(\sqrt r)\),
\[
                         \sum_i e_i=\Omega(\sqrt r\,W).
\tag{5.2}
\]

### Proof

The total collar capacity on the distinguished rows is at most
\[
 AC+\sum_i e_i.
\]
Corollary 2.1 says it must be at least \(L(A)\), giving (5.1). Combine
with Theorem 4.1 to obtain (5.2). \(\square\)

The exported targets may be reinserted elsewhere; the theorem does not
count them as omissions. A completely global rechainization which dissolves
the original chunks or drops their designated rows is outside the formal
premise. The theorem proves that the current residual decomposition cannot
be repaired by a bounded number of local exports while retaining one
remainder row per original chunk.

## 6. Consequence for the \(d+1\) top-cap bridge

At \(C=1\), Theorem 5.1 gives
\[
                         \sum_i e_i=\Omega(\sqrt r\,W).
\]
Thus the exact top-cap matching remains valuable—it correlates every
residual chunk with one literal cap and owner—but within the
remainder-preserving face the remaining collar ranks cannot be inserted
without a macroscopic rechainization of the residual bank.

The next viable lower construction must therefore do one of the following.

1. Build the residual and collar flags jointly so long residual rows are
   assigned a positive density of collar holes at every central rank.
2. Replace the length-\(d\) parity blocks by a load distribution already
   antitone to the collar incidence profile.
3. Use a global cross-SCD exchange which migrates
   \(\Omega(\sqrt r\,W)\) target incidences while preserving exact named
   coverage.

The obstruction is confined to the present whole-chunk face. It is not a
lower bound against a different \(B(k)+O(1)\) construction.
