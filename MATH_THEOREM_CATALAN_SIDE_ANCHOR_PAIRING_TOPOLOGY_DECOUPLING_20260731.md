# Catalan side-anchor pairings decouple the collar topology

Date: 2026-07-31  
Status: complete abstract topology theorem.  The initially proposed
universal prescribed-pair side theorem is false; the corrected gate is a
joint existential choice from the two physically realizable pairing
families.

## 0. Verdict

In the exact two-coordinate recursion, suppose the synchronized common basis
`Q` has already been chosen.  The inherited-port theorem makes the central
trace a subforest of the child.  Each punctured diagonal side is required to
be a linear forest, and every seam anchor must have side degree at most one.

The remaining global acyclicity condition can be separated from the side
incidence problem.

If each side forest has **no anchor-free component**, then its component
partition consists of exactly

```text
Cat_n double-anchor paths and (C-2 Cat_n) single-anchor paths.       (0.1)
```

Thus it induces an ordinary matching of order `Cat_n` on its `C` seam
labels.  For every left-side matching of this order, one can choose a
right-side matching of the same order so that, together with the fixed
central child segments, the contracted seam graph is a forest.  The proof
is a greedy matching argument and uses only `C>2 Cat_n`.

Consequently, the abstract topology can be completed after one shore is
fixed.  The tempting sufficient all-`n` physical theorem would be:

> realize prescribed Catalan-size pairings of the seam anchors by
> punctured saturating side forests, with every other anchor in a singleton
> component and no anchor-free component.

Under that theorem the two shores could be chosen sequentially and global
acyclicity would be automatic.  However, the theorem is false: every
realized double-anchor pairing obeys the metric budget

```text
sum d_J(anchor pair) <= P,
```

whereas for every `n>=3` there are Catalan-size requested pairings whose
cost exceeds `P`.  See
`MATH_THEOREM_CATALAN_SIDE_PAIRING_METRIC_OBSTRUCTION_AND_CORRECTED_GATE_20260731.md`.
Thus Theorem 3.1 remains useful only inside a joint construction that chooses
physically realizable pairings on both shores.

## 1. Exact component charge

Use the constants of the child parameter `n`:

\[
 M=\binom{2n}n,\quad N=\binom{2n}{n-1},\quad
 P=\binom{2n}{n-2},\quad K=\operatorname{Cat}_n,
 \quad C=M-P.
\]

A diagonal side forest has `N` physical vertices and `P` edges, hence

\[
                         H=N-P=C-K                         \tag{1.1}
\]

components.  It has `C` seam anchors.

### Lemma 1.1 (signed anchor charge)

Assume every seam anchor has side degree at most one.  Let `c_j` be the
number of side components containing exactly `j` anchors.  Then `c_j=0`
for `j>2` and

\[
                         c_2-c_0=K.                       \tag{1.2}
\]

In particular, if `c_0=0`, then

\[
                         c_2=K,\qquad c_1=C-2K.           \tag{1.3}
\]

### Proof

Every component is a path.  A vertex of side degree at most one can occur
only as a path endpoint (or as an isolated vertex), so a component contains
at most two anchors.  Counting components and anchors gives

\[
 c_0+c_1+c_2=H,\qquad c_1+2c_2=C.
\]

Subtract and use `C-H=K`.  If `c_0=0`, solve the two equations. `square`

The Catalan excess in (1.2) is forced; it is not a statistic of a special
finite certificate.

## 2. The central child relation is a partial matching

Orient every child component as a path and remove the edge set `Q`.  Give
the left seam of `q` the label `q^-` and the right seam the label `q^+`.

### Lemma 2.1

After contracting the components of `F-Q`, the nontrivial central
attachment relation is a partial matching between the left labels
`Q^-` and right labels `Q^+`.

### Proof

Along one oriented child path, a component of `F-Q` is a consecutive
segment.  Its left boundary, when present, is the head side of the removed
edge immediately preceding the segment; its right boundary, when present,
is the tail side of the removed edge immediately following it.  Thus the
segment contains at most one right-seam and at most one left-seam endpoint.
Contracting every segment therefore pairs at most one label of each shore.
Different segments are disjoint. `square`

Call this partial matching `P_0`.

## 3. Abstract topology completion

The identity

\[
 {C\over K}=4-{6\over n+2}>2                           \tag{3.1}
\]

holds for every `n>=2`.

### Theorem 3.1 (one shore may be arbitrary)

Let `L,R` be disjoint sets of order `C`, and let `P_0` be any partial
matching between `L` and `R`.  Let `P_L` be **any** matching of order `K`
on `L`.  If `C>2K`, there is a matching `P_R` of order `K` on `R` such
that

\[
                         P_0\cup P_L\cup P_R            \tag{3.2}
\]

is a forest.

### Proof

The graph `G_0=P_0 union P_L` is a forest.  Indeed `P_0` and `P_L` are
matchings, and every component is an isolated vertex, one edge, or a path
of the form

```text
R - L - L - R.
```

In particular every component initially contains at most two unused
vertices of `R`.

Build `P_R` greedily.  At a given stage, join two unused `R`-vertices in
different components.  This preserves the forest.  It also preserves the
invariant that every component contains at most two unused `R`-vertices:
merging components with `r_1,r_2<=2` unused vertices consumes one from each
and leaves `r_1+r_2-2<=2`.

Before the `(j+1)`-st edge, `j<K`, the number of unused `R`-vertices is

\[
                         C-2j\ge C-2K+2>2.             \tag{3.3}

Since no component contains more than two of them, two lie in different
components.  The greedy step is therefore always possible through `j=K`.
The resulting `P_R` proves (3.2). `square`

### Corollary 3.2 (physical topology decoupling)

Assume the left and right punctured diagonal matchings lift to side forests
with seam-anchor degree at most one and no anchor-free components.  If the
left forest realizes any prescribed `K`-matching `P_L` on its double-anchor
components and the right forest realizes the matching `P_R` supplied by
Theorem 3.1, then the full five-sector physical support is a linear forest.

### Proof

By Lemma 1.1 the two side component partitions contract to `P_L` and `P_R`
plus isolated seam labels.  Lemma 2.1 supplies `P_0`.  More precisely, the
incidence part of the contracted attachment graph is the barycentric
subdivision of `P_0 union P_L union P_R`, with degree-one component vertices
adjoined at singleton anchors.  Subdivision and adjoining leaves preserve
cycle rank.  Theorem 3.1 therefore makes the contracted attachment graph
acyclic.  The side and central pieces are themselves forests, so the
contraction identity gives zero cycle rank in the uncontracted support.  All
degrees are at most two by the inherited-port and side-anchor degree
hypotheses. `square`

## 4. The corrected reduced physical theorem

The automatic common-basis theorem supplies `Q` and both diagonal
incidence bases.  The following stronger realization statement would have
finished the central Catalan recursion:

> **Prescribed-pair punctured-side theorem.**  For each shore, for the
> guaranteed diagonal basis and every requested matching of `K` disjoint
> anchor pairs, there is a saturating physical side forest whose paired
> anchors are exactly those path endpoint pairs, whose remaining anchors
> lie one per component, and which has no anchor-free component.

It is enough that the left shore realize one such matching and that the
right shore realize the greedily selected matching from Theorem 3.1; full
universality on both shores is stronger than necessary.

This theorem is false by the metric obstruction cited above.  The literal
`n=3` recursion has
`c_0=0,c_2=K` on both shores.  In the first retained `n=4` witness the left
shore also has `c_0=0,c_2=K`, while the right shore has
`c_0=1,c_2=K+1`; hence that witness passes the weaker contracted-forest test
but does not instantiate the no-empty sufficient normal form on both
shores.

The exact surviving gate is existential.  Choose `Q`, its two diagonal
representative systems, and the two anchor-capped side forests jointly so
that their induced realizable pairing families contain
`P_L,P_R` with

```text
P_0 union P_L union P_R
```

acyclic.  Equivalently, prove that the two physical pairing families meet
the graphic completion class determined by `P_0`.  This is the strict
edgewise-side/turn-forest gate, not arbitrary pairing universality.

## 5. Audit

The standard-library replay

```text
scratch/audit_catalan_side_anchor_pairing_topology_20260731.py
```

checks the binomial identities through `n=100`, reconstructs the side
component/anchor histograms of the frozen `n=3,4` integral collar witnesses,
and exhausts all partial central matchings and all left `K`-matchings for
the abstract cases `(C,K)=(5,2),(8,3)`, verifying the greedy completion and
cycle rank directly.  The finite audit is not evidence for the unproved
prescribed-pair side-realization theorem.
