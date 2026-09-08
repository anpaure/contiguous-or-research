# Anchored reserve packing in the central resident rail hypergraph

**Date:** 2026-08-13  
**Status:** unconditional quantitative packing lemma.  It gives a
`Theta(k^{3/2})` supply of mutually owner-disjoint, individually anchored
central rails in the target regime.  It does not turn an arbitrary nibble
leave into complete reserved fibres and is not a cover-down theorem.

## 1. Setup

Put

\[
 q=d+1,\qquad r=2q+1,
\]

and let `H_cent` be the parameterized central rail hypergraph on

\[
 \mathcal V={ [k]\choose R}.
\]

Thus an edge is the owner support of a period-`r` cyclic `q`-window rail,
with parallel orientations retained.  Write `D` for its exact vertex
degree and `Delta_2` for its maximum pair codegree.  In the central
regime already proved,

\[
 {\Delta_2\over D}={2\over R(k-R)}.                 \tag{1.1}
\]

Every edge is a literal closed biresident pure rail with a simple proper
interval deck.

## 2. Avoidance through one prescribed owner

### Lemma 2.1

Fix an owner `A` and a forbidden owner set
`Z subseteq V\setminus{A}`.  If

\[
 |Z|\Delta_2<D,                                     \tag{2.1}
\]

then some central rail contains `A` and avoids `Z`.

#### Proof

There are exactly `D` parameterized rails through `A`.  For each
`B in Z`, at most `Delta_2` of them also contain `B`.  Hence the union of
all rails blocked by at least one member of `Z` has size at most
`|Z|Delta_2<D`.  One rail through `A` remains.  `square`

This elementary union bound is robust: no independence or asymptotic
matching theorem is being invoked.

## 3. Simultaneous anchored reserve

### Theorem 3.1 (anchored reserve packing)

Let

\[
 \mathcal A=\{A_1,\ldots,A_g\}\subseteq\mathcal V
\]

be distinct prescribed owners, and let
`F subseteq V\setminus mathcal A` be an
additional forbidden set.  If

\[
 |F|+gr < {D\over\Delta_2}={R(k-R)\over2},          \tag{3.1}
\]

then there are pairwise owner-disjoint central rails

\[
 E_1,\ldots,E_g
\]

such that

\[
 A_i\in E_i,\qquad E_i\cap F=\varnothing,
 \qquad E_i\cap\mathcal A=\{A_i\}.                 \tag{3.2}
\]

#### Proof

Choose the rails successively.  Before choosing `E_i`, forbid

\[
 Z_i=F\cup(\mathcal A\setminus\{A_i\})
       \cup\bigcup_{j<i}E_j.
\]

The prescribed anchors are distinct, and earlier rails contain no later
anchor by the inductive condition.  Therefore `A_i notin Z_i`, while

\[
 |Z_i|\le |F|+(g-1)+(i-1)(r-1)<|F|+gr.             \tag{3.3}
\]

Condition (3.1) and Lemma 2.1 supply a rail `E_i` through `A_i` avoiding
`Z_i`.  It avoids `F`, every other anchor, and all earlier rails.  This
maintains the induction and proves (3.2).  `square`

### Corollary 3.2 (target scale)

With no initial forbidden set, any

\[
 g < {R(k-R)\over2(2q+1)}                           \tag{3.4}
\]

prescribed distinct anchors admit mutually disjoint anchored rails.  In
the target regime

\[
 R,k-R=\Theta(k),\qquad q=\Theta(\sqrt k),
\]

the right side is `Theta(k^{3/2})`.

Thus the central rail geometry supplies enough fresh owner-disjoint
closed rails to host `O(k^{3/2})` individually anchored local reserve or
halo requests, provided one request consumes one central rail and its
other tickets can be instantiated independently.

## 4. Exact boundary for whole-rail cover-down

The theorem packs **central rail supports**.  It does not establish the
stronger facts required by the complementary-fibre whole-rail absorber:

1. a graph-absorber block may contain many correlated rails and owners,
   not one freely chosen central edge;
2. compulsory socket, cap, phase, and history tickets can create
   conflicts not represented in `H_cent`;
3. a bulk matching must leave either all or none of every reserved
   period-`2q` fibre; and
4. an arbitrary small leave need not be a union of those fibres.

Accordingly (3.4) proves the **reserve-capacity** part for individually
anchored central rails.  The remaining positive-semigroup gate is a
reserve-aware transversal cover-down which coordinates the bulk matching
with whole residual fibre blocks.  Pair-codegree avoidance alone does not
provide that correlation.
