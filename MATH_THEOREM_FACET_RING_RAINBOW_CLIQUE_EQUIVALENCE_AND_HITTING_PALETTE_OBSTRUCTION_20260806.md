# Facet rings are rainbow Hamilton cycles in clique blocks

## Status

This note gives the exact second-stage formulation for an integral
all-high facet-ring factor.  After partitioning the owner shore into facet
blocks, choosing the cyclic source order in each block is exactly choosing
a Hamilton cycle in a clique; immediate-lower exactness is exactly global
rainbowness of those clique cycles.

The ambient edge-colouring is proper, and the average root-colour
multiplicity is `(L-1)/2`.  Those two facts, even together with maximum
colour multiplicity `O(L)`, do **not** imply a rainbow clique-Hamilton
factor.  An explicit hitting-palette obstruction is given below.  Thus the
remaining positive theorem must use the Boolean incidence geometry or an
all-cut palette condition, not only properness and multiplicity.

## 1. Facet blocks

Put

\[
                         n=2r-1,qquad L=d+2.                \tag{1.1}
\]

A facet block is specified by

\[
                         K\subset H\subset[n],
 \qquad |H|=r+1,\quad |H-K|=L.                              \tag{1.2}
\]

Write `F=H-K`.  Its owner set is

\[
                         B(H,K)=\{H-\{f\}:f\in F\}.         \tag{1.3}
\]

It has `L` rank-`r` owners.  Let `G_B` be the complete graph on those
owners.  Colour the edge between `H-f` and `H-g` by

\[
                              \kappa_B(fg)=H-\{f,g\}.        \tag{1.4}
\]

The colour is a rank-`r-1` immediate-lower root.

Let `mathcal B` be an owner-disjoint family of blocks and let

\[
                              G=\bigsqcup_{B\in\mathcal B}G_B. \tag{1.5}
\]

### Lemma 1.1 (proper root colouring)

The colouring (1.4) is injective inside each clique.  Across the disjoint
block family, every colour class is a matching.

#### Proof

Inside one block, `H-{f,g}` recovers the missing unordered pair `{f,g}`.
Across different blocks, two edges of the same colour cannot share an
owner: an owner belongs to only one block.  \(\square\)

## 2. Exact ring--Hamilton equivalence

Choose a cyclic order

\[
                         f_0,f_1,\ldots,f_{L-1}             \tag{2.1}
\]

of `F` and use the cyclic source word

\[
                         A_t=K\cup\{f_t\}.                   \tag{2.2}
\]

Because the owner width is `L-1=d+1`, its owner at phase `t` is the facet
of `H` missing the unique private phase outside that window.  Consecutive
owners are therefore consecutive vertices of the Hamilton cycle induced by
(2.1), and their root is (1.4).

### Theorem 2.1 (rainbow clique-factor equivalence)

Let `mathcal B` partition a set `U` of owners.  The following data are
equivalent.

1. For every `B in mathcal B`, a literal all-high source ring on `B`.
2. For every clique `G_B`, a Hamilton cycle `C_B`.

Under this equivalence, all immediate-lower roots in the ring family are
distinct exactly when

\[
                         \bigcup_{B\in\mathcal B}E(C_B)      \tag{2.3}
\]

is rainbow in the colouring (1.4).

If `U` is the full owner shore, then a rainbow selection is automatically
root-exact: it uses every rank-`r-1` root exactly once.

#### Proof

Equation (2.2) proves the bijection between cyclic private-label orders and
clique Hamilton cycles.  Their transition roots are exactly their edge
colours, proving the rainbow equivalence.

For a full owner partition, the selected cycles contain

\[
                    \sum_B|B|=\binom{2r-1}{r}               \tag{2.4}
\]

edges.  The rank-`r-1` shore has the same cardinality.  A rainbow family of
that size therefore uses the whole root shore.  \(\square\)

This theorem is parity-free.  Odd `L` prevents a partition of the ring into
disjoint shift-two two-owner macros, but it does not prevent the literal
one-step cyclic source ring (2.2).

## 3. Exact colour multiplicity ledger

Let `m_Q` be the number of clique edges of colour `Q` in (1.5).

### Proposition 3.1 (average and maximum multiplicity)

If the blocks cover `|U|` owners, then

\[
                 \sum_Qm_Q={|U|(L-1)\over2}.                \tag{3.1}
\]

For a full owner partition, the average over all roots is exactly

\[
                              {L-1\over2}.                   \tag{3.2}
\]

Every individual root satisfies

\[
                              m_Q\le\left\lfloor{r\over2}\right\rfloor. \tag{3.3}
\]

#### Proof

There are `|U|/L` cliques and `binom(L,2)` edges per clique, proving (3.1).
The two central shores have the same size, giving (3.2).

Every edge of colour `Q` joins two distinct owners `Q+x,Q+y`, with
`x,y notin Q`.  By Lemma 1.1 these edges form a matching on the `r` possible
extensions of `Q`, proving (3.3).  \(\square\)

If one could choose the owner-block partition so that every `m_Q` were
close to `(L-1)/2`, the remaining problem would be a highly regular rainbow
Hamilton selection.  The next theorem shows that regular-looking local
parameters alone are not enough.

## 4. Proper bounded multiplicity is insufficient

### Theorem 4.1 (hitting-palette obstruction)

For every `L>=4`, there is a properly edge-coloured disjoint union of

\[
                              B=L-1                          \tag{4.1}
\]

copies of `K_L` with exactly `BL` colours such that:

1. every colour occurs between one and `B` times;
2. the average colour multiplicity is exactly `(L-1)/2`;
3. every colour class is a matching; but
4. there is no globally rainbow choice of one Hamilton cycle from each
   clique.

#### Proof

Let `S` be a common palette of `L-2` colours.  In every clique choose a
vertex `v` and one incident edge `e_0`.  Colour the other `L-2` edges at
`v` bijectively by `S`.  All colours within a clique are distinct.  Across
different cliques their edges are vertex-disjoint, so every colour class is
a matching.

After deleting the `S`-coloured edges, `v` has degree one.  Hence the
remaining graph has no Hamilton cycle.  Every Hamilton cycle in every
clique must therefore use at least one colour of `S`.  There are `B=L-1`
cliques but only `L-2` colours in `S`; a globally rainbow choice is
impossible.

It remains only to colour the other edge occurrences.  There are

\[
 R=BL-(L-2)                                                 \tag{4.2}
\]

remaining available colours and

\[
 M=\binom L2-(L-2)                                         \tag{4.3}
\]

remaining edges in each clique.  Since `M<=R`, choose in every clique an
`M`-subset of the `R` colours and use it injectively.  The subsets may be
chosen so that their union is all `R` colours.  Indeed, partition the `R`
colours into `B` parts and assign one part to each clique; every part has
size at most `ceil(R/B)<=L<=M`.  Extend each part arbitrarily to an
`M`-subset of the palette.  No colour is used twice inside one clique, and
every remaining colour is used between one and `B` times.

The total number of edge occurrences is `B binom(L,2)`, while the number of
colours is `BL`; their ratio is `(L-1)/2`.  This proves all four items.
\(\square\)

The obstruction is an all-cut defect: the small palette `S` meets every
Hamilton cycle in too many components.  It survives properness, bounded
multiplicity, the correct average, and complete local Hamiltonicity.

## 5. The sharpened positive target

For a Boolean facet-block partition, define for a palette `S` of roots

\[
 \tau_B(S)=\min\{|E(C)\cap\kappa^{-1}(S)|:
                         C\text{ a Hamilton cycle of }G_B\}. \tag{5.1}
\]

Every globally rainbow clique-Hamilton factor necessarily satisfies

\[
                         \sum_{B\in\mathcal B}\tau_B(S)le|S|
                         \qquad\text{for every }S.           \tag{5.2}
\]

Theorem 4.1 violates (5.2).  Thus a credible integral theorem must prove
the Boolean all-cut inequality (5.2), together with an augmentation or
absorption statement showing its sufficiency in this structured colour
system.  Average multiplicity and a proper colouring are only marginal
data and cannot replace that row.

Even after a rainbow cycle is selected in every clique, the packet cycles
must still be fused at the source-state level.  Theorem 2.1 isolates the
owner/`q1` selection cleanly; it does not assert that final fusion.
