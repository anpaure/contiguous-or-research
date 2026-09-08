# Self-audit: canonical phase cover and local wedge obstruction

**Date:** 2026-08-04  
**Verdict:** author self-audit **GO**, pending independent review.  No
computation, search, or solver output is used.

Audited theorem:
`MATH_THEOREM_FACTOR_FIRST_COMMON_CORE_CANONICAL_PULL_PHASE_COVER_AND_LOCAL_WEDGE_OBSTRUCTION_20260804.md`.

## 1. Phase-cover extension

Contracting a prescribed graphic pull forest and taking a spanning tree in
the residual quotient is ordinary graphic basis extension.  A protected
base edge survives because every later selected label avoids its unique
old-phase pull.  A protected new-phase edge survives because canonical pull
circuits are edge-disjoint.  Tree compatibility then gives one Hamilton
cycle.  The rooted relaxation applies the same argument componentwise and
uses the already frozen rootless-component identity.

The theorem is intentionally limited to a static canonical family.  It does
not treat dynamically generated pull occurrences.

## 2. Four-state local aperture

A touching canonical pull must remove one of the two base-factor edges at
the lower vertex.  Edge-disjointness allows at most one pull per edge and
therefore at most two relevant labels.  The local state is determined by
their selected subset, giving at most four wedges.  Tree compatibility is
needed only to know that every selected graphic forest is a factor; the
cardinality upper bound remains valid if some subsets are unavailable.

## 3. Ring realization

For a prescribed lower root `I` and wedge labels `x,y`, removing any
`a in I` gives the `(m-2)`-core `B`.  Taking `b=x` and making `y` the cyclic
predecessor of `a` produces owners `I+x,I+y`.  There are exactly `m+1`
labels outside `B`, so the full-size ring uses all of them with the required
`b`/ring split.  The history partition exists under `d<=m-2`.

## 4. Obstruction scope

For the common-label average, each lower vertex has `m-1` decompositions
`L=B+a` and exactly two factor-wedge labels available as `b`, giving
`2(m-1)W` triples.  The number of `(B,b)` pairs is `(m-1)W`, so the average
is exactly two.  With at most four accessible wedges, their coordinate union
has size at most eight, proving the accessible average bound.  A full ring
requires support `m`.

Once common `B,b` are fixed, the other wedge coordinate at every root is
forced in a fixed factor.  These coordinates are precisely the predecessor
map of a ring; the ring exists exactly when they form one directed cycle.
For pull menus, global consistency of the arc labels is explicitly retained
as a separate graphic-forest condition.

## 5. Fixed-host obstruction scope

For `m>=4`, `binom(m,2)>4`; choose an inaccessible wedge.  Since both of its
incidence edges belong to the ring bank, no forest-switched canonical factor
can contain the ring.  This finite obstruction requires `d<=m-2`.  The hybrid
path and random spread constructions are parametrized by the chosen common
core/order, so for sufficiently large `m` with `1<=d=O(sqrt(m))` they can be
applied after fixing this ring to obtain the full clipped-resident reservoir.

This proves failure of universal embedding into a **fixed** canonical
factor/pull family.  It does not rule out choosing that family jointly with
the ring, using noncanonical or longer circuits, or replacing witnesses by
an equivalent transparent bank.
