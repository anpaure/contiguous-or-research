# The `k=16` radius-147 residence/q1 cross-pattern gate

Date: 2026-07-29  
Status: exact finite reductions and audited finite no-go.

## 1. Canonical scaffold and minimum residence distance

Let `F` be the canonical `C_15`-equivariant q1-perfect, top-biresident
physical Hamilton factor in
`scratch/k16_qfactor_q1_topresident_hamilton_20260729.json`, SHA-256

`f76ab4e5c30c3269da87788c275777a3b40deea96f4fbf892cd5c6027280a7a5`.

It contains 389 AA, 80 AB and 389 BB quotient edge orbits.  Its 3390 old
short runs collapse to 226 quotient motif rows.  The interval certificate in
`scratch/k16_qfactor_q1_topresident_hamilton_residence_motifs_20260729.audit.json`
gives 147 pairwise edge-disjoint motifs.  Hence every resident quotient
factor differs from `F` by at least 147 deleted and 147 added edge orbits.

Let the 147 packed motifs have union `P`.  Then

\[
|P|=476,
\qquad
P=(233\ {m AA})\sqcup(36\ {m AB})\sqcup(207\ {m BB}).
\]

### Lemma 1.1 (exact radius face)

If a factor has exactly 147 deletions from `F` and hits every old residence
motif of `F`, then it deletes exactly one edge from every packed motif and no
edge of `F\P`.

### Proof

The packed motifs are pairwise edge-disjoint and each requires a deletion.
Thus they require at least 147 distinct deletions.  Equality leaves one in
each packed motif and none elsewhere. ∎

This converts the minimum-distance question into a finite 147-choice
rethread, rather than an unrestricted 27,456-edge factor search.

## 2. Fixed-cross shore decomposition

Suppose exactly the 80 AB edges of `F` are selected—every one is retained and
no off-seed AB edge is added.  At a quotient vertex `v`, let
`c(v)` be its fixed cross degree.  The residual same-shore degree is

\[
r(v)=2-c(v),
\]

so it is one at a cross endpoint and two elsewhere.  The q1 rows split as
follows:

* AA supplies every upper colour without `z` and every lower colour without
  `z` not already supplied by a fixed AB edge;
* BB supplies every lower colour with `z` and every upper colour with `z`
  not already supplied by a fixed AB edge.

Thus, after a deletion set is fixed, quotient degree and q1 completion are
two independent residual f-factor problems.  Only the choice of deletions in
mixed AA/AB/BB motifs, global connectivity/voltage, and subsequently created
cross-boundary residence motifs recouple the shores.

The motif interval certificate contains a minimum transversal using no AB
edge, split as 87 AA plus 60 BB.  It proves that fixing the cross pattern does
not increase the bare residence transversal number.

## 3. The displayed same-shore transversal does not lift

For the certified 87-AA/60-BB transversal, exact endpoint exposure gives:

| shore | removals | exposed deficit nodes | deficit histogram | candidate additions | missing q1 rows | zero-candidate rows |
|---|---:|---:|---|---:|---:|---:|
| AA | 87 | 170 | `1:166, 2:4` | 1832 | 130 | 1 |
| BB | 60 | 120 | `1:120` | 887 | 92 | 8 |

The nine zero-candidate colours are

\[
\begin{aligned}
{m AA\ lower}:&\quad 0{:}2765;\\
{m BB\ lower}:&\quad 1{:}845,1{:}1433,1{:}2347;\\
{m BB\ upper}:&\quad 1{:}703,1{:}1751,1{:}1963,1{:}3739,1{:}6765.
\end{aligned}
\]

### Theorem 3.1 (fixed-transversal obstruction)

The displayed 87-AA/60-BB minimum transversal has no degree-two q1-complete
completion with the 80 AB edges fixed.

### Proof

After retaining every uncut seed edge, an added nonloop edge can be selected
only if both endpoints have positive degree deficit.  An added loop would
require deficit two at its vertex.  For each of the nine listed colours,
every off-seed same-shore provider has at least one endpoint outside the
positive-deficit set.  The sole loop among these providers, edge 27347, is
based at a deficit-zero vertex.  Hence none of the nine q1 rows can be
restored. ∎

The solver-free certificate is
`scratch/k16_residence_fixed_cross_same_shore_transversal_barrier_20260729.json`.

## 4. No fixed-cross minimum-distance completion exists

The preceding obstruction concerns one transversal.  To free all cut
choices, introduce:

* a removal bit for every same-shore seed edge in `P`;
* an addition bit for every nonloop off-seed same-shore edge joining two of
  the 572 potentially exposed vertices;
* one-deletion equality on each of the 147 packed motifs;
* all 226 original motif-hit rows;
* at each vertex, added incidence equals removed incidence; and
* every nonconstant lower and upper q1 provider row.

There are 440 removable same-shore edges and 10266 possible replacements,
split as 5758 AA and 4508 BB.  Exactly 729 q1 rows remain nonconstant, and
none is empty before the endpoint/degree equations are imposed.

### Theorem 4.1 (fixed-cross radius-147 no-go)

There is no loopless quotient degree-two, lower-q1-complete and
upper-q1-complete factor which

1. selects exactly the same 80 AB edges as `F` and no other AB edge;
2. deletes exactly 147 edges of `F`; and
3. hits all 226 old residence motifs of `F`.

In particular, there is no resident Hamilton factor on this fixed cross
pattern at radius 147.

### Proof

Lemma 1.1 makes the 147 packed equalities exact and fixes every seed edge
outside `P`.  With the AB edges fixed, per-vertex equality of added and
removed same-shore incidence is equivalent to final quotient degree two.
The provider rows are the literal q1 conditions.  Thus the stated finite
system is necessary and sufficient for the three displayed conditions.

The exact CP-SAT instance has 10707 variables and, after deliberately
removing every top-residence row, 1961 constraints.  It returns `INFEASIBLE`
after 178725 branches and 5399 conflicts.  The audited artifact is
`scratch/k16_residence_fixed_cross_joint_radius147_degree_q1_nogo_20260729.json`,
with internal payload SHA-256

`153d8bb6f5d61d24c903412dca46f03d36187361429d42a80eae4b5e2f3d3cf5`.

The logical equivalence of the model rows was independently audited. ∎

Quotient loops were excluded.  This loses no connected Hamilton target: a
selected quotient loop consumes both degree incidences at its vertex and is
therefore a separate quotient component.

## 5. Sharp consequence and next gate

### Corollary 5.1

Every radius-147 resident Hamilton rethread of `F`, if one exists, changes
the selected AB edge set.  Equivalently, any rethread selecting exactly the
same 80 AB edges has radius at least 148.  Merely retaining those 80 edges is
not enough: a rethread may retain them and add new AB edges.

The exact alternatives are now sharply separated:

1. solve the variable-cross radius-147 f-factor face; or
2. retain the cross pattern and move to radius greater than 147.

Neither alternative is resolved by Theorem 4.1.  Connectivity, unit voltage,
and newly created residence motifs must still be imposed after any positive
degree/q1 completion.

### Lemma 5.2 (cross-count arithmetic)

Let a radius-147 rethread remove `(r_A,r_X,r_B)` AA, AB and BB edges and add
`(a_A,a_X,a_B)`.  Then

\[
a_X\equiv r_X\pmod 2,
\qquad
a_A-r_A=a_B-r_B={r_X-a_X\over2}. \tag{5.1}
\]

Consequently its final sector counts are

\[
\left(389+s,\ 80-2s,\ 389+s\right),
\qquad s={r_X-a_X\over2}. \tag{5.2}
\]

### Proof

Sum final degree over the 429 A-shore quotient vertices and separately over
the 429 B-shore vertices.  These give

\[
2(389-r_A+a_A)+(80-r_X+a_X)=858
\]

and the same equation with `A` replaced by `B`.  Rearrangement gives (5.1)
and (5.2). ∎

The packed motifs have types

\[
55\ {m AA},\quad56\ {m BB},\quad18\ ({\rm AA/AB}),
\quad18\ ({\rm AA/AB/BB}).
\]

If exactly `k` AB edges are removed, then necessarily

\[
73-\min(18,k)\le r_A\le91-k,
\qquad r_B=147-k-r_A. \tag{5.3}
\]

Thus the variable-cross gate decomposes first by the pair `(r_X,a_X)`, with
matching parity.  The fixed-cross theorem closes only the cell
`(r_X,a_X)=(0,0)`.  It does **not** close the whole `r_X=0` stratum, because
even `a_X>0` changes the cross pattern while retaining all old AB edges.

## 6. Reproducibility boundary

The reductions and literal witness audits are solver-independent.  The final
finite infeasibility assertion uses CP-SAT's exact `INFEASIBLE` result; no
separate DRAT-style proof log is currently archived.  Therefore the theorem
is an audited finite exact-model no-go, not a standalone hand enumeration of
all assignments.
