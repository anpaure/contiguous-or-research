# Factor-first common-core reservoirs: canonical pull-phase cover and the local wedge obstruction

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical sufficient embedding theorem for
one fixed tree-compatible pull system, followed by a sharp obstruction to
deriving its key hypothesis from exact trace/common-core structure alone.
It does not rule out a factor chosen jointly with the reservoir, a
noncanonical pull system, or longer alternating circuits.

No computation, search, or solver output is used.

## 0. Static canonical setup

Let `F_0` be a spanning Middle-Levels two-factor and let `H` be a connected
labelled pull host on `Comp(F_0)`.  For `e in E(H)`, let `Z_e` be an
alternating circuit with old and new phases

\[
 O_e\subseteq F_0,
 \qquad N_e\cap F_0=\varnothing.
\tag{0.1}
\]

Assume the standard canonical properties:

1. the complete circuit edge sets `Z_e` are pairwise edge-disjoint; and
2. every graphic forest `A subseteq E(H)` is tree-compatible: switching the
   circuits in `A` gives a spanning two-factor `F_A` whose component
   partition is obtained by contracting `A`.

The canonical GMN factor and its labelled pull family have these properties.

Let `P` be an occurrence-labelled protected path forest, such as the
common-core clipped-resident witness reservoir together with its hinge ring.

## 1. Exact pull-phase cover theorem

### Definition 1.1 (canonical phase cover)

A labelled set `A subseteq E(H)` is a **phase cover** for `P` when:

1. `A` is a graphic forest;
2. every edge of `P` lies in the switched factor

   \[
   F_A=(F_0\setminus\bigcup_{a\in A}O_a)
          \cup\bigcup_{a\in A}N_a;
   \tag{1.1}
   \]

3. every protected edge which belongs to `F_0` is absent from `O_a` for
   every `a in A`.

Condition 3 is redundant given the literal set containment in condition 2,
but records the occurrence direction needed in a certificate.

For a phase cover `A`, define the forbidden residual labels

\[
 B_P(A)=\{e\in E(H)\setminus A:O_e\cap(P\cap F_0)\ne\varnothing\}.
\tag{1.2}
\]

Pairwise circuit edge-disjointness means that no residual pull can delete a
protected edge introduced in `N_a`, `a in A`.

### Theorem 1.2 (factor-first protected Hamilton extension)

Suppose `A` is a phase cover for `P` and

\[
 \boxed{(H-B_P(A))/A\text{ is connected}.}
\tag{1.3}
\]

Then a canonical pull spanning tree produces a Hamilton cycle containing
every edge of `P`.

#### Proof

Since `A` is a forest, contract it.  Condition (1.3) supplies a spanning tree
of the quotient using labels outside `B_P(A)`.  Lift that tree and adjoin
`A`; graphic basis extension gives a spanning tree

\[
 A\subseteq T\subseteq H-B_P(A).
\]

Tree compatibility says that switching every pull in `T` turns `F_0` into
one spanning cycle.

An edge of `P cap F_0` is not deleted by a label in `A` because `A` is a
phase cover, and it is not deleted by a label in `T-A` because those labels
avoid `B_P(A)`.  An edge of `P-F_0` belongs to `N_a` for some `a in A` by
(1.1).  Pairwise circuit edge-disjointness prevents every other pull from
touching it.  Hence all protected edges survive in the final Hamilton cycle.
\(\square\)

This theorem is stronger than first extending `P` to an arbitrary
two-factor: it gives an occurrence-level certificate inside one known pull
system.

### Theorem 1.3 (rooted path-cover relaxation)

Keep a phase cover `A`, but drop connectedness in (1.3).  Let

\[
 \overline H=(H-B_P(A))/A.
\]

If every component of `overline H` contains a contracted factor component
carrying a common-core ring hinge, then a maximal forest of `overline H`,
together with `A`, produces a protected factor every component of which
contains a ring hinge.  Equivalently, the final factor has forest complement
relative to the hinge bank.

#### Proof

Choose a spanning tree in every component of `overline H` and lift it with
`A`.  Tree compatibility contracts exactly those host components.  The
phase-cover argument in Theorem 1.2 preserves `P`, so the resulting factor
component associated with one component of `overline H` contains the union
of its old hinge occurrences.  The root hypothesis makes every such union
nonempty.  Apply the exact rooted-pull/forest-complement identity. \(\square\)

Thus a factor-first proof has two independent rows:

1. literal phase cover of the structured path bank; and
2. connected, or merely ring-rooted, residual pull quotient.

## 2. The local canonical wedge aperture

At a lower vertex `L` of `F_0`, its two selected owner incidences determine
one unordered **factor wedge**.  A pull circuit **touches** `L` when its old
phase contains one of those two incidences.

### Lemma 2.1 (four-state aperture)

At most two canonical pull labels touch one fixed lower vertex `L`.
Consequently, as `A` ranges over every graphic forest in `H`, the factor
wedge at `L` takes at most four values.

#### Proof

Every touching pull uses one of the two `F_0`-edges incident with `L`.
Canonical pull circuits are edge-disjoint, so each of those two edges belongs
to at most one pull.  Hence at most two pull labels affect the local wedge.

For a fixed forest `A`, the local state depends only on which of those at
most two labels lie in `A`.  There are at most `2^2=4` subsets.  Some subsets
may be graphically dependent or may produce the same wedge, which only lowers
the number. \(\square\)

This is a property of the full static pull family, not merely of one chosen
spanning tree.

## 3. The common-core ring has full wedge aperture

Work in `ML_m`.  Fix any lower vertex

\[
 I\in{[2m-1]\choose m-1}.
\]

Its `m` owner neighbours are `I+x`, `x notin I`, so it supports
`binom(m,2)` possible wedges.

### Lemma 3.1 (arbitrary wedge realized by a full-size ring)

Assume `m>=3` and `d<=m-2`.  For every unordered pair

\[
 \{x,y\}\subseteq[2m-1]\setminus I
\]

there is a full-size common-history hinge ring whose hinge at `I` has owner
pair `I+x,I+y`.

#### Proof

Choose any `a in I` and put

\[
 B=I\setminus\{a\}.
\]

Set the ring label `b=x`, let `a` be one cyclic external label, and make
`y` its predecessor in the cyclic order.  The complement of `B` has
`m+1` elements: `b` and exactly `m` ring labels, so the remaining labels can
be placed arbitrarily around the cycle.  Partition `B` into `d` nonempty
history letters.

At the distinguished hinge, the two owners are

\[
 B\cup\{a,b\}=I+x,
 \qquad
 B\cup\{a,y\}=I+y.
\]

All other owner and palette identities are those of the cyclic
common-history ring. \(\square\)

For sufficiently large `m`, with `1<=d=O(sqrt(m))`, the full
clipped-resident witness reservoir can then be built over this ring.  The top
paths contain the ring hinges as their first edges; every private target has
its exact external-trace path; and the symmetric spreading and high-tail
packing theorems apply for the chosen `B,b` and cyclic order.

## 4. Exact common-label scarcity and the predecessor-cycle gate

The local aperture bound can be sharpened globally.  For an arbitrary
two-factor `F`, let `w_F(L)` be the unordered pair of coordinates added by
the two factor owners above a lower vertex `L`.

For `B in binom([2m-1],m-2)` and `b notin B`, put

\[
 s_F(B,b)=
 |\{a\notin B\cup\{b\}:b\in w_F(B\cup\{a\})\}|.
\tag{4.1}
\]

### Theorem 4.1 (exact common-label average)

For every spanning two-factor `F`,

\[
 \boxed{
  \sum_{B}\sum_{b\notin B}s_F(B,b)
  =2(m-1)W,
 }
\tag{4.2}
\]

where `W=binom(2m-1,m-1)`.  Since

\[
 {2m-1\choose m-2}(m+1)=(m-1)W,
\tag{4.3}
\]

the average value of `s_F(B,b)` is exactly two.

In particular, at most a `2/m` fraction of the pairs `(B,b)` can satisfy
`s_F(B,b)=m`, the first necessary row for a full-size ring.

#### Proof

Count triples `(B,b,a)` appearing on the left.  A lower vertex `L` has
exactly `m-1` representations `L=B union {a}`, one for each `a in L`.
For each representation, exactly the two coordinates in `w_F(L)` are
eligible values of `b`.  Thus every one of the `W` lower vertices contributes
`2(m-1)` triples, proving (4.2).  Formula (4.3) is the adjacent-binomial
ratio.  The fraction bound follows from `s_F<=m` and Markov's inequality.
\(\square\)

For a fixed canonical pull family, let `mathcal W(L)` be the set of wedges
accessible at `L` as the selected graphic pull forest varies.  Lemma 2.1
gives `|mathcal W(L)|<=4`.  Define `s_mathcalW(B,b)` by replacing
`b in w_F(...)` in (4.1) with membership in at least one wedge of
`mathcal W(...)`.

### Corollary 4.2 (accessible common-label scarcity)

\[
 \boxed{
  \sum_{B,b}s_{\mathcal W}(B,b)
  \le8(m-1)W.
 }
\tag{4.4}

Hence the average accessible common-label support is at most eight, and at
most an `8/m` fraction of `(B,b)` pairs can even pass the common-label row
`s_mathcalW(B,b)=m`.

#### Proof

For each representation `L=B+a`, the union of the at most four accessible
wedges contains at most eight possible common labels `b`.  Repeat the count
in Theorem 4.1. \(\square\)

The remaining ring row has an exact finite form.

### Theorem 4.3 (predecessor-cycle criterion)

Fix `(B,b)` with `s_F(B,b)=m`, and put

\[
 E=[2m-1]\setminus(B\cup\{b\}).
\]

For `a in E`, write

\[
 w_F(B+a)=\{b,p(a)\}.
\tag{4.5}

Then the complete full-size hinge ring with core `B` and common label `b`
is contained in `F` if and only if the directed edges

\[
 p(a)\longrightarrow a\qquad(a\in E)
\tag{4.6}

form one directed Hamilton cycle on `E`.

#### Proof

In a cyclic ring, the second label at hinge `a` is exactly the predecessor
of `a` in the cyclic order.  Thus containment of all hinges says precisely
that `p(a)` is that predecessor for every `a`.  Such a cyclic order exists
exactly when (4.6) is one directed cycle through all labels. \(\square\)

For a pull-switchable factor, each `a` instead has a menu of at most four
predecessor arcs, labelled by the local pull choices which realize them.  A
ring phase cover is therefore exactly a directed Hamilton cycle in this
`m`-vertex predecessor digraph whose arc labels admit one globally consistent
graphic pull forest.  This is a much smaller joint-selection problem than
the full owner layer, but Corollary 4.2 shows it is a rare high-codegree face,
not a consequence of average local aperture.

## 5. Sharp failure of a fixed canonical factor/pull system

### Theorem 5.1 (fixed-host universal embedding is impossible)

Let `m>=4`, assume `d<=m-2`, and fix any canonical base factor `F_0` and its
static edge-disjoint pull family.  There exists a full-size common-history
ring which has no phase cover in this pull family.

For sufficiently large `m`, with `1<=d=O(sqrt(m))`, that ring may moreover be
coinstantiated with a clipped-resident exact-trace witness reservoir, and the
resulting protected reservoir still has no phase cover in this pull family.

#### Proof

Fix any lower vertex `I`.  By Lemma 2.1, all factors obtainable by switching
graphic forests of the fixed pull host expose at most four wedges at `I`.
But

\[
 {m\choose2}>4
 \qquad(m>=4).
\]

Choose an unexposed pair `\{x,y\}` and build the common-history ring from
Lemma 3.1.  Its protected bank contains both incidence edges of the wedge
`I+x-I-I+y`.  No forest-switched factor `F_A` contains that wedge, so no
`A` satisfies the phase-cover condition `P subseteq F_A`.

The remaining witness paths can be chosen by the frozen hybrid and spread
constructions without changing this literal hinge.  Hence the failure occurs
inside the exact-trace/common-core structured class. \(\square\)

### Corollary 5.2

No theorem of the form

> every exact-trace/common-core reservoir embeds into one fixed canonical
> factor after canonical pull-tree switches

is possible.  A successful factor-first proof must do at least one of:

1. choose the base factor/pull host jointly with the ring wedge data;
2. enlarge the static move family beyond the canonical edge-disjoint pulls;
3. use longer alternating circuits which increase the local wedge aperture;
   or
4. weaken literal containment to a proved transparent replacement of the
   witness bank.

This does not refute any of those four routes.

## 6. Exact constructive target

Theorem 1.2 isolates the strongest factor-first target which survives the
obstruction:

> **Joint canonical phase-cover lemma.**  Choose the common-core ring and
> exact-trace reservoir together with a canonical base factor so that the
> protected paths admit a graphic pull-phase cover `A` and the residual
> quotient `(H-B_P(A))/A` is connected.

For the weaker `m`-rooted path-cover goal, replace connectedness by the
rooted-component condition of Theorem 1.3.  The local aperture theorem shows
that the quantifier order is essential: the factor cannot be frozen before
the ring wedge choices.

## 7. Scope and dependencies

The phase-cover theorem is an exact sufficient construction, not an
existence proof for the current reservoir.  The obstruction is against one
fixed canonical base/pull family only; it is not a no-go for adaptive factors
or arbitrary Middle-Levels Hamilton cycles.

| role | file | SHA-256 |
|---|---|---|
| canonical pull edge-disjointness and forest extension | `MATH_THEOREM_R_CANONICAL_MUTZE_PULL_COATOM_AND_RESIDENT_COLLAR_EMBEDDING_20260801.md` | see frozen source |
| local pull degree and star-bridge obstruction | `MATH_THEOREM_ORDERED_PORTAL_DIRECT_PULL_ZERO_DENSITY_AND_STAR_BRIDGE_20260801.md` | see frozen source |
| common-history ring and short-deck invariance | `MATH_THEOREM_CYCLIC_COMMON_HISTORY_HINGE_RING_AND_SHORT_DECK_INVARIANCE_20260804.md` | `96b9f8717c138dfac7df2a4d1c439392de1a3313c9e57114d2e1cd6f145b90ba` |
| clipped-resident exact-trace reservoir | `MATH_THEOREM_COMMON_CORE_HYBRID_CLIPPED_RESIDENT_WITNESS_RESERVOIR_20260804.md` | `f9cd82ff39c3fb6979bd2c70e92223af6f7bb171d4ede422a023b7d2c6809314` |
| rooted pull/forest-complement theorem | `MATH_THEOREM_COMMON_CORE_ROOTED_PULL_TRANSVERSAL_AND_FIXED_MATCHING_OBSTRUCTION_20260804.md` | `5cc02e3ce3fd07a2fd3d7656893a72ef4c4395076dafc19c0769c6834b30668a` |
