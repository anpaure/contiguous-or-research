# The residual rigid-rotation cycles have positive runs at least `m-2` and zero gaps at least `m-1`

**Date:** 2026-08-05  
**Method:** exact insertion/deletion event calculus on one residual block;
no computation or search  
**Status:** unconditional for `m>=4`.  For `m>=6`, every residual
two-soliton component of the full rigid rotation rethread is cyclically
bi-resident through the optimal deadline and therefore has a depth-`d`
cyclic antecedent.  Together with the braid residence theorem, this closes
componentwise terminal factorization for the rigid orbit.  It does not join
the component antecedents or construct the strict-lower compiler.

## 1. The residual owner block

Put

\[
                         n=2m+1,
 \qquad                  L=2m-4.
\tag{1.1}
\]

One residual block starts at `P_1(t)=B_(m-2)(t)` and ends at the next
copy `P_1(t+3)`.  Its owner sequence is

\[
\begin{split}
 B_{m-2}(t),\quad
 A_2(t-1),A_3(t-2),\ldots,A_{m-1}(t-m+2),\\
 B_1(t-m-1),B_2(t-m-2),\ldots,B_{m-2}(t+3).
\end{split}
\tag{1.2}
\]

The terminal owner in (1.2) is the initial owner of the next block.  Thus
the block has `L` directed edges, indexed by

\[
                         0\le e<L.
\tag{1.3}
\]

Edge zero is the new edge `N_1(t)`.  Edges `1,...,m-3` are the successive
`A` transitions, edge `m-2` is `A_(m-1)->B_1`, and the remaining edges are
the successive `B` transitions.

## 2. Exact event labels

Let `I_e(t)` be the coordinate inserted by edge `e`, and let `D_e(t)` be
the coordinate deleted by that edge.  All labels are read modulo `n`.

### Lemma 2.1 (block event formula)

For every residual block,

\[
 I_e(t)=
 \begin{cases}
  t-e,&0\le e\le m-2,\\
  t-e-2,&m-1\le e<L,
 \end{cases}
\tag{2.1}
\]

and

\[
 D_e(t)=
 \begin{cases}
  t+m,&e=0,\\
  t+m-e-1,&1\le e<L.
 \end{cases}
\tag{2.2}
\]

#### Proof

The new edge is

\[
 P_1(t)\longrightarrow Q_2(t)
   =P_1(t)-\{t+m\}+\{t\},
\]

which gives the exceptional entries at `e=0`.

For an `A_j` state of root `r`, the transition to `A_(j+1)` of root
`r-1` deletes `r+m-1` and inserts `r`.  The exceptional transition from
`A_(m-1)` of root `t-m+2` to `B_1` of root `t-m-1` deletes `t+1` and
inserts `t-m+2`.  These are exactly (2.1)--(2.2) through `e=m-2`.

For a `B_j` state of root `r`, the transition to `B_(j+1)` of root `r-1`
deletes `r+m+1` and inserts `r`.  Substituting
`r=t-m-j` and `e=m-2+j` gives the second branches of
(2.1)--(2.2).  \(\square\)

## 3. Positive residence

Every nonconstant positive run begins immediately after one insertion
event and ends at the next deletion event of the same coordinate.  Lemma
2.1 identifies that next event explicitly.

### Theorem 3.1 (positive-run floor)

Every cyclic positive run on every residual component has length at least

\[
                         \boxed{m-2}.
\tag{3.1}
\]

The lower bound is attained: the coordinate inserted at edge `m-2` is
deleted at edge zero of the next block, after exactly `m-2` owner steps.

#### Proof

Consider an insertion at edge `e` of the block with phase `t`.

* If `0<=e<=m-4`, then

  \[
  D_{e+m-1}(t)=t-e=I_e(t).
  \]

  The deletion occurs `m-1` steps later.

* For `e=m-3`, the formal same-block index is `L`, just beyond the block.
  No deletion occurs in the remaining part of the block, whose length is
  already `m-1`.  Hence this run has length at least `m-1`.

* For `e=m-2`,

  \[
  D_0(t+3)=t+m+3\equiv t-m+2=I_{m-2}(t)\pmod n.
  \]

  The distance to that next-block edge is

  \[
                         L-(m-2)=m-2.
  \]

* If `m-1<=e<L`, put `e'=e-m+3`.  Then

  \[
  2\le e'\le m-2,
  \qquad
  D_{e'}(t+3)=I_e(t),
  \]

  and the distance is

  \[
                         L-e+e'=m-1.
  \]

Within one block all deleted coordinates are distinct.  In the cross-block
cases the displayed deletion is the first equal deletion in the next
block; the piecewise formulas exclude an earlier equality.  Thus these are
the actual next deletions, proving (3.1).  A coordinate constant on an
entire component, if present, has the full component period as its run and
is harmless.  \(\square\)

## 4. Zero-gap residence

The dual event calculation is nearly as rigid.

### Theorem 4.1 (zero-gap floor)

Every cyclic zero gap on every residual component has length at least

\[
                         \boxed{m-1}.
\tag{4.1}
\]

#### Proof

Start with a deletion at edge `e`.

* For `e=0`, the next equal insertion is `I_(m-1)(t)`, at distance
  `m-1`.
* For `1<=e<=m-5`, the next equal insertion is `I_(e+m)(t)`, at distance
  `m`.
* For `max{1,m-4}<=e<=L-2`, put `e'=e-m+4`.  Then the next equal insertion
  is `I_(e')(t+3)`, at distance

  \[
                         L-e+e'=m.
  \]
* At `e=L-1`, neither the remainder of the current block nor the next
  block before its corresponding solution contains an equal insertion, so
  the gap is longer than the preceding lower bounds.

The equalities follow by direct substitution in (2.1)--(2.2).  Distinctness
of the insertion labels within the relevant block pieces makes the listed
events the first possible insertions.  This proves (4.1).  \(\square\)

## 5. Comparison with the optimal deadline

For `k=2m+1`, put

\[
 W_m={2m+1\choose m},
 \qquad
 \Lambda_m=\sum_{s=1}^{m}{2m+1\choose s}=4^m-1.
\tag{5.1}
\]

The optimal deadline is the least `d` satisfying

\[
                         dW_m+{d+1\choose2}\ge\Lambda_m.
\tag{5.2}
\]

### Lemma 5.1

For every `m>=6`,

\[
                         d(2m+1)\le m-3.
\tag{5.3}
\]

#### Proof

At `m=6`,

\[
                         3{13\choose6}=5148>4096.
\]

Moreover, with

\[
                         a_m={(m-3)W_m\over4^m},
\]

one has

\[
 {a_{m+1}\over a_m}
 ={(m-2)(2m+3)\over2(m-3)(m+2)}
 =1+{m+6\over2(m-3)(m+2)}>1.
\tag{5.4}
\]

Thus

\[
                         (m-3)W_m>4^m>\Lambda_m
\]

for every `m>=6`, so `m-3` is admissible in (5.2).  \(\square\)

### Corollary 5.2 (residual componentwise factorization)

For every `m>=6`, every residual component is cyclically bi-resident
through the optimal deadline:

\[
 \text{positive runs}\ge m-2\ge d+1,
 \qquad
 \text{zero gaps}\ge m-1\ge d+1.
\tag{5.5}
\]

Hence the maximal-antecedent criterion gives a cyclic nonempty source word
on every residual component whose depth-`d` derivative is exactly that
component's owner chronology.

The exceptional values `m=4,5` are already among the independently solved
finite dimensions.  This theorem is intended for the uniform construction,
so no claim that the rigid residual factor itself handles those two cases
is needed.

## 6. Consequence and remaining interface

The terminal rigid orbit now has componentwise antecedents everywhere:

1. the alternating braid component by its exact run/gap theorem; and
2. every residual two-soliton component by Corollary 5.2.

Together with the complete target-support theorem and the owner-path SDR
theorem, the remaining source-side problem is no longer residence or
factorability of an individual component.  It is the joint interface:

* join the component antecedents with bounded total history charge, or
  perform a zero-position owner rethread before factorization;
* choose one fresh strict-lower short-cell matching on the final source
  chronology; and
* route that matching through the typed shared cap.

Bounded component count alone does not solve the first item: two unrelated
order-`d` histories can have overlap zero and cost `d` to concatenate.

## 7. Dependencies

The residual block order is proved in

`MATH_THEOREM_PBBS_RIGID_C6_SERIAL_ROTATION_ORBIT_TOPOLOGY_NOGO_20260805.md`.

The braid comparison is

`MATH_THEOREM_PBBS_RIGID_ROTATION_BRAID_EXACT_BIRESIDENCE_20260805.md`.

The exact antecedent/run criterion is in

`MATH_THEOREM_AD_FAILCLOSED_FLAT_SOURCE_COMPILER_PIPELINE_20260802.md`.
