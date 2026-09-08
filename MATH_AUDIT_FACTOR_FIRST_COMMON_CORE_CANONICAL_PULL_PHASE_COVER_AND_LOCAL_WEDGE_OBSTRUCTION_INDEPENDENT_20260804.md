# Independent audit: factor-first canonical phase cover and local wedge obstruction

**Date:** 2026-08-04  
**Verdict:** **GO** at the hashes below.  No computation, search, or solver
output is used.

Audited theorem:
`MATH_THEOREM_FACTOR_FIRST_COMMON_CORE_CANONICAL_PULL_PHASE_COVER_AND_LOCAL_WEDGE_OBSTRUCTION_20260804.md`,
SHA-256
`ae2a051514ca3cc8d16a17cdc8e5cb2a70468511f4148e65b4bd601dc8194079`.

Author self-audit:
`MATH_AUDIT_FACTOR_FIRST_COMMON_CORE_CANONICAL_PULL_PHASE_COVER_AND_LOCAL_WEDGE_OBSTRUCTION_SELF_20260804.md`,
SHA-256
`b5d67f9da20dd1685bd807794596e355b32b2a723c82a7cfa4d6718f316d570b`.

The earlier draft's finite-versus-asymptotic reservoir quantifier has been
corrected in the audited theorem.

## 1. Phase-cover basis extension and survival

Let `A` be the declared graphic phase cover.  Connectivity of

\[
 (H-B_P(A))/A
\]

is exactly the graphic basis-extension condition: a spanning tree of the
quotient lifts to a set whose union with `A` is a spanning tree of `H` and
uses no label in `B_P(A)`.  The canonical tree-compatibility hypothesis then
turns that pull tree into one factor cycle.

The protected-edge survival argument separates all possible cases:

* a protected edge in `F_0` is not removed by `A`, by the phase-cover
  condition, and is not removed later because every later selected label
  avoids `B_P(A)`;
* a protected edge outside `F_0` must occur in `N_a` for some `a in A`, by
  the literal formula for `F_A`;
* pairwise disjointness of the complete circuit edge sets prevents every
  other selected pull from either deleting or colliding with that introduced
  edge.

Thus Theorem 1.2 proves literal containment of the whole occurrence-labelled
bank, not merely preservation of its value set.

For Theorem 1.3, quotient vertices after contracting `A` are precisely the
factor components of `F_A`.  A maximal forest inside each residual quotient
component contracts exactly that component and no other.  The phase-cover
argument still preserves every hinge occurrence, so the stipulated root in
each quotient component gives exactly one hinge-bearing final factor
component.  The rooted cycle-transversal identity then gives the claimed
forest complement.  No unproved connectivity inference is used.

## 2. Four-state local wedge aperture

At a lower vertex `L`, an alternating pull circuit which changes the local
wedge contains one old and one new incidence at `L`; in particular it uses
one of the two `F_0` incidences at `L`.  Complete canonical pull circuits are
edge-disjoint, so each of those two old incidences belongs to at most one
pull label.  Hence at most two labels can affect the wedge.

For any selected graphic forest, all other pull labels leave the two local
incidences unchanged.  The local state is therefore determined by a subset
of at most two labels and has at most four values.  Possible graphic
dependence or coincident output wedges only decreases this number.  The
argument concerns the full fixed canonical pull family, not one previously
chosen pull tree.

## 3. Arbitrary common-ring wedge realization

Fix an `(m-1)`-set `I` and distinct external labels `x,y`.  Removing any
`a in I` gives an `(m-2)`-core `B`.  The complement of `B` consists of
`m+1` labels: the common label `b=x` and exactly `m` cyclic ring labels,
including `a` and `y`.  Making `y` the predecessor of `a` gives the hinge
owners

\[
 B+a+b=I+x,
 \qquad
 B+a+y=I+y.
\]

Thus every one of the `binom(m,2)` wedges at `I` occurs in a full-size ring.
The history partition exists in the ring theorem's parameter range
`1 <= d <= m-2`.  Here and below the lower bound `d>=1` is inherited from
the cited common-history-ring setup.

The compatibility statement with the hybrid/spread reservoir is also
correctly scoped after revision.  With

\[
 K=B\cup\{b\},
 \qquad
 E=[2m-1]\setminus K,
\]

the chosen cyclic order is exactly an allowed relabelling of the reservoir
construction; its top paths contain these ring hinges as first edges, and
the private paths can be packed without changing them.  This full-reservoir
conclusion is used only for sufficiently large `m` with
`1 <= d=O(sqrt(m))`, which is the proved range of the hybrid theorem.

## 4. Exact common-label average and scarcity

For each lower vertex `L`, there are exactly `m-1` decompositions
`L=B+a`.  For each such decomposition, the eligible common labels `b` are
exactly the two coordinate labels in the factor wedge `w_F(L)`.  Therefore
each of the `W` lower vertices contributes `2(m-1)` triples `(B,b,a)`, giving

\[
 \sum_{B,b}s_F(B,b)=2(m-1)W.
\]

Also

\[
 {2m-1\choose m-2}(m+1)=(m-1)W,
\]

so the average is exactly two.  Since `0<=s_F(B,b)<=m`, Markov's inequality
gives the stated `2/m` upper fraction for full support.

For a fixed canonical pull family, at most four accessible wedges at `L`
contain at most eight distinct external coordinate labels in total.  The
same decomposition count therefore gives

\[
 \sum_{B,b}s_{\mathcal W}(B,b)\le8(m-1)W,
\]

and the `8/m` fraction bound follows.  This is only a necessary local-support
row and is not promoted to a globally consistent pull selection.

## 5. Predecessor-cycle criterion

If `s_F(B,b)=m`, then for every

\[
 a\in E=[2m-1]\setminus(B\cup\{b\})
\]

the wedge at `B+a` has the unique form `{b,p(a)}`, with
`p(a) in E\setminus\{a\}`.  A full common-core ring with common label `b`
is contained in `F` exactly when `p(a)` is the predecessor of `a` for every
`a`.  This is equivalent to the arcs `p(a)->a` forming one directed cycle
through all of `E`; if they fail injectivity or split into several cycles,
no single cyclic order realizes all hinges.

In the pull-switchable version, each local predecessor arc must be decorated
by the local subset of touching pull labels which realizes it.  Requiring
one globally consistent graphic pull forest is therefore an essential extra
condition and is retained explicitly.  Local arc menus alone do not prove a
ring phase cover.

## 6. Fixed-host obstruction and its exact scope

For `m>=4`,

\[
 {m\choose2}>4.
\]

At any fixed lower vertex, choose a wedge absent from all four or fewer
states reachable by graphic forests in the fixed canonical host.  The ring
construction places that exact wedge in its protected bank.  Since no
forest-switched factor contains both of its incidence edges, no canonical
phase cover of the ring exists.

This finite ring obstruction is valid in the common-history parameter range
`1<=d<=m-2`.  The stronger statement coinstantiating all clipped-resident
exact-trace witness paths is now, correctly, asserted only for sufficiently
large `m` with `d=O(sqrt(m))`.  The hybrid theorem is equivariant in the
chosen core, common label, and cyclic order, so the additional paths do not
remove the already inaccessible hinge.

The result is solely a no-go for embedding every reservoir into one **fixed
canonical** base factor and static edge-disjoint pull family.  It says
nothing against a jointly selected base factor, a noncanonical or dynamic
pull host, longer alternating circuits, or a proved transparent replacement
of the literal bank.

## 7. Final verdict

All phase-cover, rooted-quotient, wedge-aperture, common-label counting, and
predecessor-cycle claims are correct at the audited hashes.  The earlier
quantifier defect in the full-reservoir obstruction has been repaired.
The independent verdict is **GO**.
