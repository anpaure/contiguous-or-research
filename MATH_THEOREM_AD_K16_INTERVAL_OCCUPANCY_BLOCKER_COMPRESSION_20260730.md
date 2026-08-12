# K16 exact interval-occupancy/blocker compression

Date: 2026-07-30  
Lane: AD  
Status: proved exact CNF reduction for all three fixed-gap profiles; no SAT
or UNSAT verdict

## 1. Input theorem

Use the authenticated fixed-gap data and the 57-target repair family \(R\)
from

~~~text
MATH_THEOREM_AD_K16_CHART_INTERSECTION_ELIMINATION_AND_ANCHOR_PRUNING_20260730.md
SHA-256 2f52bc0bbcbc61d7ac0d22113bceb951d46610c0c526c0482160da6785f5a156
~~~

For each \(T\in R\), it is necessary and sufficient to choose one local
interval \(I_T\) in one collar such that active targets have nonempty
intersection at every used cell and every bit in
\(T\setminus b_T(I_T)\) has a durable point in \(I_T\).

The direct selector encoding uses one variable for each of 57 times 65,
61, or 66 target/interval pairs. The present theorem eliminates all those
selectors.

## 2. Occupancy variables and one-run constraints

Fix one of the three width profiles

\[
 (4,9,4),\qquad(5,8,4),\qquad(5,9,3).
\]

Let \(P=P_1\dot\cup P_2\dot\cup P_3\) be its 17 editable positions. For
every \(T\in R\) and \(p\in P\), introduce an occupancy bit \(o_{T,p}\).
For every target and block introduce \(g_{T,j}\), and impose:

1. \(\bigvee_{p\in P}o_{T,p}\);
2. \(o_{T,p}\Longrightarrow g_{T,j}\) for \(p\in P_j\); and
3. pairwise at-most-one clauses on \(g_{T,1},g_{T,2},g_{T,3}\).

Thus some block is used and no two blocks are used. No at-least-one row on
the \(g\)-variables is needed.

Within a block write its occupancies as \(a_0,\ldots,a_{w-1}\). Its possible
run-start events are

\[
 s_0=a_0,\qquad s_i=\neg a_{i-1}\wedge a_i\quad(1\le i<w).
\]

For every \(0\le i<j<w\) with \(j\ge i+2\), forbid \(s_i\wedge s_j\).
Explicitly, the clause is

\[
\begin{cases}
 \neg a_0\vee a_{j-1}\vee\neg a_j,&i=0,\\
 a_{i-1}\vee\neg a_i\vee a_{j-1}\vee\neg a_j,&i>0.
\end{cases}                                             \tag{2.1}
\]

Adjacent start events are already logically inconsistent and need no
clause. There are exactly \(\binom{w-1}{2}\) rows in (2.1).

### Lemma 2.1 (exact support normal form)

Constraints 1--3 and (2.1) make the support
\(\{p:o_{T,p}=1\}\) one nonempty interval in exactly one block.

#### Proof

Constraint 1 makes the support nonempty. Occupancy-to-block implications
and block at-most-one put it in one block. Two distinct runs have two start
events. Nonadjacent starts are forbidden by (2.1), while adjacent starts
cannot simultaneously hold because one requires their common occupancy bit
to be zero and the other requires it to be one. Hence there is at most one
run. Conversely every one-run support satisfies all the clauses.
\(\square\)

## 3. Exact interval signatures

For an interval \(I=[f,\ell]\) within a block, define

\[
 \Sigma_I=
 o_{T,f}\wedge o_{T,\ell}\wedge
 \begin{cases}\neg o_{T,f-1},&f>0,\end{cases}\wedge
 \begin{cases}\neg o_{T,\ell+1},&\ell+1<w.\end{cases}    \tag{3.1}
\]

Duplicate endpoint literals are omitted when \(f=\ell\).

### Lemma 3.1 (unique true interval signature)

Under Lemma 2.1, \(\Sigma_I\) is true for exactly one local interval \(I\),
namely the support of \(o_T\).

#### Proof

The support interval makes its two endpoints true and its immediate exterior
neighbors false. Conversely, if (3.1) holds, one-run contiguity fills every
cell between the endpoints, while either exterior neighbor prevents the run
from extending. At a block boundary there is no exterior cell to check.
No other block is active. \(\square\)

This explicitly covers singleton intervals, full-block intervals, and all
left/right boundary cases; no sentinel position is introduced.

## 4. Blockers and durable clauses

Introduce \(B_{p,q}\) for each of 17 cells and 16 coordinates. Impose

\[
 o_{T,p}\Longrightarrow B_{p,q}\qquad(q\notin T),       \tag{4.1}
\]

and

\[
                         \bigvee_{q=0}^{15}\neg B_{p,q} \tag{4.2}
\]

at every cell. For every target, every candidate interval \(I\), and every
\(q\in T\setminus b_T(I)\), impose

\[
             \Sigma_I\Longrightarrow\bigvee_{p\in I}\neg B_{p,q}.     \tag{4.3}
\]

Negating (3.1) makes (4.3) one ordinary CNF clause.

### Theorem 4.1 (occupancy/blocker equivalence)

Constraints 1--3, (2.1), and (4.1)--(4.3) are satisfiable if and only if
the named fixed-gap profile contains a literal universal word.

#### Proof

Given a feasible chart selection, set \(o_{T,p}=1\) exactly on its selected
interval, set the corresponding block bit, and set \(B_{p,q}=1\) exactly
when some active target at \(p\) omits \(q\). Lemma 2.1 holds, (4.2) is
nonemptiness of the active-target intersection, and (4.3) is the durable
point condition.

Conversely, Lemmas 2.1 and 3.1 recover one actual interval \(I_T\) for each
target. Whenever \(B_{p,q}=0\), implication (4.1) proves that every active
target contains \(q\). Thus (4.2) gives a nonempty intersection at every
used cell, and the unique triggered rows (4.3) give all required durable
points. Assign to each used cell the intersection of its active targets and
an arbitrary nonzero closure value to an unused cell. The chart-intersection
theorem turns every selected maximal-context form into a literal interval,
and the fixed gaps retain all other targets. \(\square\)

The \(B\)-bits may overstate blocking. This creates no false positive because
only false \(B\)-bits certify common coordinates or durable points. A decoder
must reconstruct cell values from active-target intersections.

## 5. Exact dimensions

Across the 57 repair targets,

\[
 \sum_{T\in R}(16-|T|)=448.
\]

Therefore (4.1) contributes \(17\cdot448=7616\) clauses. The common counts
are:

* 969 occupancy variables and 969 occupancy-to-block clauses;
* 171 block variables and 171 block-AMO clauses;
* 272 blocker variables and 17 common-coordinate clauses; and
* 57 target occupancy ALO clauses.

The one-run counts are

\[
\begin{array}{c|c}
(4,9,4)&57(3+28+3)=1938,\\
(5,8,4)&57(6+21+3)=1710,\\
(5,9,3)&57(6+28+1)=1995.
\end{array}
\]

The audited maximal-context ledgers give respectively 28,292, 26,442, and
28,695 durable rows. Hence every profile has exactly

\[
                         969+171+272=1412
\]

variables, and the unanchored clause counts are:

\[
\begin{array}{c|c}
(4,9,4)&57+969+171+1938+7616+28292+17=39060,\\
(5,8,4)&57+969+171+1710+7616+26442+17=36982,\\
(5,9,3)&57+969+171+1995+7616+28695+17=39520.
\end{array}                                             \tag{5.1}
\]

These dimensions are strictly smaller than the selector/blocker CNFs in
both variables and clauses.

## 6. Singleton-anchor branching

For \(H=\mathtt{0x8000}\), any chosen witness interval consists entirely of
cells equal to \(H\). It is therefore WLOG to constrain \(o_H\) to have
exactly one true position. Pairwise at-most-one over its 17 occupancies adds
136 clauses; its target ALO already supplies at-least-one. This gives the
complete anchor-any instances.

For a fixed absolute editable position \(p\), setting \(o_{H,p}=1\) and all
other \(o_{H,p'}=0\) adds 17 unit clauses and gives the exact singleton
anchor-\(p\) branch. The union of the 17 branches is complete; one branch is
only a restriction.

## 7. Scope

SAT plus fail-closed canonical decoding and full literal replay proves
\(\nu(16)=12873\). Proof-checked UNSAT of an anchor-any instance closes its
entire named fixed-gap profile. The theorem does not cover a changed fixed
gap, a moved separator, a nonlocal braid, or an unrelated length-12,873
word.
