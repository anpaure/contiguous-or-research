# A loose forest of q2-neutral clean C6s closes the graphic turn-section gate

**Date:** 2026-08-05  
**Method:** exact component and omission accounting; no computation or search  
**Status:** unconditional implication.  It converts the remaining global
q2-Pascal graphic condition into a rooted loose-forest problem in the
component hypergraph of the common-deletion clean-C6 atlas.

## 1. Factor, section, and connector atlas

Let `F` be a spanning two-factor in a Johnson graph, and let `S` be a
one-occurrence q1 section which is q2-complete.  For a factor cycle `C`, put

\[
 o_C=|E(C)\setminus S|.
\tag{1.1}
\]

Call `C` **hit** when `o_C>0` and **unhit** when `o_C=0`.

A **selected q2-neutral clean C6** is a clean Boolean-diamond trade whose
three old q1 occurrences belong to `S`, whose three new occurrences carry
the same q1 labels, and whose selected q2-turn multiset is unchanged.  By
the common-deletion classification, in the nondegenerate common-core normal
form this is equivalent to one common deleted core coordinate at the three
unchanged companion turns.

Project every available selected q2-neutral clean `C6` to the set of factor
cycles containing its three old edges.  Retain only connectors whose old
edges lie on three distinct cycles.  This gives a three-uniform component
multihypergraph `H`.

## 2. One connector adds omission counts

### Lemma 2.1

Suppose one selected q2-neutral clean `C6` uses old edges on three distinct
factor cycles `C_0,C_1,C_2`.  After the switch:

1. the three cycles merge into one cycle `C'`;
2. the transported section remains one-occurrence and q2-complete; and
3. its omission count is

\[
                         o_{C'}=o_{C_0}+o_{C_1}+o_{C_2}.
\tag{2.1}
\]

In particular, `C'` is hit if and only if at least one input cycle is hit.

#### Proof

Cutting one directed edge in each of three distinct cycles leaves three
directed paths.  The cyclic clean-C6 reconnection concatenates them into one
cycle.  The q1 and q2 assertions are the definition of a selected
q2-neutral connector.

All three removed old edges were selected, and all three replacement edges
are selected.  No other occurrence changes section status.  Hence every
omission on the three input cycles survives on the output cycle and no new
omission is created or consumed.  This proves (2.1). \(\square\)

## 3. Rooted loose trees

A finite three-uniform hypergraph `T` is a **loose tree** when its incidence
bipartite graph is a tree.  Equivalently, starting from one vertex, its
hyperedges can be attached one at a time, each new edge meeting the previous
union in exactly one vertex and introducing two new vertices.  Thus

\[
                         |V(T)|=2|E(T)|+1.
\tag{3.1}
\]

Call such a tree **hit-rooted** when at least one of its vertices represents
an initially hit factor cycle.

Assume that the physical clean-C6 supports assigned to the hyperedges are
pairwise vertex-disjoint.  This ensures that a switch never deletes or
changes an edge required by another connector.

### Lemma 3.1 (serial realization of a loose tree)

The connectors of a physically disjoint loose tree can be applied in an
order in which every connector meets three distinct current factor cycles.
Their total effect merges all initial cycles indexed by `V(T)` into one
cycle.

#### Proof

Root the incidence tree at any cycle vertex.  Process it recursively from
the leaves toward the root.  At a connector node, its two child branches
have already each been merged into the cycle containing their attachment
vertex, while its parent branch has not yet crossed that connector.  The
three old edges therefore lie on three distinct current cycles.  Lemma 2.1
merges them.

Pairwise disjoint physical support guarantees that the remaining old shores
are still present.  Induction over the connector nodes proves that the final
block is one cycle. \(\square\)

## 4. Graphic completion theorem

### Theorem 4.1 (q2-neutral loose-forest completion)

Suppose the component set of `F` is partitioned into vertex sets of
physically supported loose trees in `H`, and every such tree is hit-rooted.
Then the corresponding clean-C6 switches produce a new spanning two-factor
`F'` and transported section `S'` such that:

1. `S'` contains exactly one occurrence of every q1 colour;
2. `S'` is q2-complete; and
3. every factor cycle of `F'` is hit by `E(F')\setminus S'`.

Consequently `F',S'` satisfy all three hypotheses of the q2 Pascal
two-factor lift.

#### Proof

Apply Lemma 3.1 independently in every loose-tree block.  Exact q1 and q2
preservation compose because the physical supports are disjoint.  Lemma
2.1 shows that the unique output cycle of a tree has omission count equal
to the sum of its input omission counts.  Hit-rootedness makes that sum
positive.  Therefore every output cycle is hit.  The q2 Pascal lift now
applies verbatim. \(\square\)

### Corollary 4.2 (bounded residual-cycle form)

Suppose instead that the factor cycles are partitioned into `b` physically
supported loose-tree blocks, without requiring every block to be hit-rooted.
After the switches there is exactly one output factor cycle per block, the
q1 section remains q2-complete, and at most `b` output cycles are unhit.

In particular, a uniform bound `b<=b_0` reduces the exact graphic failure
to at most `b_0` named cycle punctures.  Any bounded-defect Pascal lift or
guarded cycle-sidecar theorem which pays a constant charge per named
puncture then contributes only an absolute additive constant.

#### Proof

Lemma 3.1 gives one output cycle per loose tree.  Lemma 2.1 makes its
omission count the sum over the input block.  A positive sum gives a hit
cycle and a zero sum gives one unhit cycle, so there is at most one unhit
output per block.  The q1/q2 argument is unchanged. \(\square\)

## 5. Exact remaining PBBS statement

For the max-height PBBS section, define the **common-pivot connector
hypergraph** by retaining precisely the literal clean `C6`s classified by
the common-deletion theorem and projecting them to PBBS factor components.
The remaining graphic theorem is now:

> The PBBS common-pivot connector hypergraph contains a physically
> vertex-disjoint loose forest whose components are all rooted at cycles
> already containing a max-height omission and whose vertex set contains
> every completely selected PBBS cycle.

The explicit rigid-soliton clean `C6` proves that this connector atlas is
nonempty, but its two non-rigid old edges lie on one common, also-unhit
two-soliton cycle.  It is therefore a repeated-vertex hyperedge and is not
itself an edge of the retained three-component hypergraph.  A new
three-component common-pivot connector, or a compound simulating one, is
still required.

There is a particularly sharp two-switch target.  The explicit first
switch cuts the two-soliton component into two directed paths

\[
 \Pi_{12}:Q_1\leadsto P_2,
 \qquad
 \Pi_{21}:Q_2\leadsto P_1,
\tag{5.1}
\]

and produces two unhit output cycles: one contains the opened
single-soliton path together with `Pi_(12)`, and the other is `Pi_(21)`
closed by `P_1Q_2`.

### Corollary 5.1 (exact two-C6 escape criterion)

Assume that, disjointly from the first gadget, a second selected q2-neutral
clean `C6` has:

1. one old edge in the interior of `Pi_(12)`;
2. one old edge in the interior of `Pi_(21)`; and
3. one old edge on a factor cycle having positive omission count.

Then applying the first and second switches produces one hit cycle in place
of the two forced input cycles and the donor cycle, while preserving q1 and
q2 exactly.

#### Proof

After the first switch, the three old edges of the second connector lie on
three distinct current cycles by construction.  Lemma 2.1 merges them, and
its output omission count is the sum of the two zeros and the positive donor
count.  Thus the output cycle is hit.  Both switches are q2-neutral and have
disjoint support, so their q1/q2 identities compose. \(\square\)

This reduces the first nontrivial PBBS compound search to one literal
**straddling common-pivot connector** across the two explicit two-soliton
arcs and any hit donor component.

No q3, residence, arbitrary-upper, or common-cap assertion is part of this
theorem.
