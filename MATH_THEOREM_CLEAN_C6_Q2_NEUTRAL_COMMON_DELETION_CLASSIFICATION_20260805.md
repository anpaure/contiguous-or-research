# Exact q2-neutrality criterion for a clean Boolean-diamond C6

**Date:** 2026-08-05  
**Method:** pure set algebra; no computation or search  
**Status:** unconditional local classification.  In a clean common-core
`C6` whose six relevant q1 occurrences coexist in a one-occurrence section,
q2-multiset transparency is equivalent to one common deleted core
coordinate at the three unchanged companion turns.

## 1. Clean-C6 normal form

Let `K` have size `m-2`, and choose pairwise distinct labels

\[
 a_0,a_1,a_2,c\notin K.
\]

Read subscripts modulo three and put

\[
 R_i=K+a_i,
 \qquad
 P_i=K+a_i+a_{i+1},
 \qquad
 Q_i=K+a_i+c.
\tag{1.1}
\]

The old and new Johnson shores are

\[
 E_i=P_iQ_i,
 \qquad
 E_i'=P_iQ_{i+1}.
\tag{1.2}
\]

Their q1 rows are respectively

\[
 P_i\cap Q_i=R_i,
 \qquad
 P_i\cap Q_{i+1}=R_{i+1},
\tag{1.3}
\]

and their upper colours agree edgewise:

\[
 P_i\cup Q_i=P_i\cup Q_{i+1}
 =K+a_i+a_{i+1}+c.
\tag{1.4}
\]

Assume that all three old occurrences `E_i` belong to a one-occurrence q1
section.  At `P_i`, let `L_i` be the q1 row of the unchanged other selected
factor edge.  Assume also

\[
 L_i\notin\{R_i,R_{i+1}\}.
\tag{1.5}
\]

The first exclusion is forced by the old one-occurrence section and the
second by the transported new one-occurrence section.

## 2. Companion rows have one deleted core coordinate

Both q1 rows incident at a rank-`m` owner are rank-`(m-1)` subsets of that
owner.  Hence there is a unique `d_i in P_i` such that

\[
                         L_i=P_i-d_i.
\tag{2.1}
\]

Condition (1.5) excludes `d_i=a_(i+1)` and `d_i=a_i`, respectively.
Therefore

\[
 d_i\in K,
 \qquad
 L_i=(K-d_i)+a_i+a_{i+1}.
\tag{2.2}
\]

The old q2 turn at `P_i` is

\[
 D_i=R_i\cap L_i=(K-d_i)+a_i,
\tag{2.3}
\]

while after transporting the row `R_(i+1)` across the clean `C6`, the new
turn is

\[
 D_i'=R_{i+1}\cap L_i=(K-d_i)+a_{i+1}.
\tag{2.4}
\]

At every `Q_i`, the new incident clean-C6 edge is `P_(i-1)Q_i`, whose row
is still `R_i`.  Thus q2 turns at all `Q_i` are pointwise unchanged.

## 3. Classification theorem

### Theorem 3.1 (common-deletion criterion)

Under the hypotheses above, the clean `C6` preserves the multiset of all
selected q2 turns if and only if

\[
                         d_0=d_1=d_2.
\tag{3.1}
\]

When (3.1) holds, writing the common coordinate as `d`, the three affected
q2 turns rotate cyclically:

\[
 (K-d+a_0,\ K-d+a_1,\ K-d+a_2)
 \longmapsto
 (K-d+a_1,\ K-d+a_2,\ K-d+a_0).
\tag{3.2}
\]

#### Proof

Sufficiency is immediate from (2.3)--(2.4): if all `d_i=d`, then

\[
                         D_i'=D_{i+1}.
\]

For necessity, every set in (2.3)--(2.4) contains exactly one of the
active labels `a_0,a_1,a_2`, all of which lie outside `K`.  The new set
`D_i'` contains `a_(i+1)`.  In the old multiset the unique member containing
that active label is `D_(i+1)`.  Equality of the old and new multisets
therefore forces

\[
 (K-d_i)+a_{i+1}=(K-d_{i+1})+a_{i+1}.
\]

Deleting the common active label gives `K-d_i=K-d_(i+1)`, and hence
`d_i=d_(i+1)`.  Cycling `i` proves (3.1).  The turns at the `Q_i` were
already pointwise fixed, so no other q2 change exists. \(\square\)

## 4. Consequence for the PBBS graphic problem

Every q1/q2-transparent clean-C6 connector in this normal form is therefore
specified by:

1. one rank-`(m-2)` core `K`;
2. four active labels `a_0,a_1,a_2,c`; and
3. one common pivot `d in K` deleted by all three companion rows.

The remaining PBBS existence question is no longer an arbitrary q2 audit.
It is the following component-incidence problem:

> Find enough literal PBBS old shores (1.2) whose three companion rows all
> delete one common pivot `d`, and whose projected factor-component triples
> connect every completely selected component to a component containing an
> omitted q1 occurrence.

A physically compatible loose forest of such connectors preserves q1 and
q2 identically under composition.  The theorem does not assert that PBBS
supplies that loose forest, nor any q3/residence/common-cap property.

