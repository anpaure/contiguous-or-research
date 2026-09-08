# Self-audit: forced pull phases and the exact last-ring basis criterion

**Date:** 2026-08-04  
**Method:** line-by-line symbolic audit; no computation, search, or solver  
**Audited file:**
`MATH_THEOREM_FORCED_PULL_PHASE_LAST_RING_BASIS_AND_CONJUGATION_NOGO_20260804.md`  
**Verdict:** `SUPERSEDED_BY_INDEPENDENT_AUDIT`.  The physical/tree core is
correct, but this self-audit missed one exact scope omission in the original
typed-cap paragraph: validity of `A_D` alone did not ensure that the final
ring pull `g` preserved the fixed common typed state.  The theorem has now
been corrected to require joint validity of all
`J_D=A_D\cup\{g\}`.  Cite
`MATH_AUDIT_FORCED_PULL_PHASE_LAST_RING_BASIS_AND_CONJUGATION_NOGO_INDEPENDENT_20260804.md`
for the authoritative audit.

## 1. Forced-phase normal form

The complete pull supports are assumed pairwise edge-disjoint.  Therefore
an edge outside the base factor belongs to at most one new phase.  Every
selected factor containing the protected bank must select that unique label.
This proves that `A_D` is forced.

A protected base-factor edge survives a selected pull family exactly when it
belongs to none of the selected old phases.  No removed protected edge can
be reinstalled by another label, again by complete-support disjointness.
These two observations prove both directions of Theorem 1.1.  The revised
minimality wording is conditional on accessibility and phase consistency;
it does not call an inconsistent forced set a phase cover.

## 2. Last-pull graphic criterion

If a spanning tree contains `J_D`, then `J_D` is a forest.  After contracting
it, the remaining tree edges span the quotient and avoid `B_D`.  Conversely,
a spanning tree of the connected quotient lifts with `J_D` to a spanning
tree of the original multigraph.  Parallel edges and loops after contraction
do not affect this standard graphic-basis argument.

Deleting the distinguished tree edge `g` leaves a spanning forest with
exactly two components.  Tree compatibility therefore gives exactly two
factor cycles, not merely at most two.  Restoring `g` gives the full spanning
tree and hence one Hamilton cycle.  Pairwise support disjointness and
`D cap Z_g=emptyset` make the local phase change exactly `O_g -> N_g` while
preserving `D`.

The converse is deliberately scoped to a realization obtained from this
same static pull system with `g` as one edge of the selected spanning tree.
It makes no necessity claim for arbitrary alternating circuits or arbitrary
Middle-Levels Hamilton cycles.

## 3. Reservoir and cap scope

The common bank `D` may contain the unchanged ring stubs and private upper
witness paths.  The three changed seam edges are not put in `D`; they are
exactly the phase-specific sets `O_g,N_g`.  Thus the disjointness assumption
does not accidentally exclude the ring.

The theorem supplies physical factor containment only.  Arbitrary-width
upper transport still uses the independent damage-cone theorem and its
ambient pre-toggle upper-completeness hypothesis.  Section 4 treats a typed
cap state only after that state and all its routes have been fixed; it does
not infer occurrence equality, capacity, or cap linkage from Boolean mask
equality.

## 4. Finite-conjugate obstruction

For each fixed conjugated pull system, the local canonical aperture theorem
gives at most four accessible wedges at one lower vertex.  A union over `s`
systems therefore gives at most `4s`, without assuming their accessible
sets are disjoint.

A lower rank-`(m-1)` vertex has exactly `m` owner neighbours and hence
`binom(m,2)` wedges.  Given an omitted wedge `I+x,I+y`, choose

\[
 B=I-\{a\},\qquad b=x,
\]

and make `y` the predecessor of active label `a`.  Then the distinguished
three-ring hinge is literally

\[
 I+x\; -\; I\; -\; I+y.
\]

A third active label exists for `m>=3`; a nonempty depth-`d` partition of
`B` exists for `d<=m-2`.  Hence inaccessible wedge implies inaccessible
ring.  The independent reservoir is constructed after fixing this hinge and
does not change it.

For all synchronous cyclic rotations, `s<=2m-1`.  The arithmetic threshold
is exact:

\[
 \binom m2>4(2m-1)
 \iff m^2-17m+8>0,
\]

which holds for every integer `m>=17`.

## 5. Exact retained frontier

The theorem does not show that the current clipped reservoir is accessible
in the canonical phase union, that its forced labels are a forest, or that
the residual quotient is connected.  It proves that these are the complete
static-host physical rows and that synchronous rotation cannot supply a
universal shortcut.  The typed one-state cap coexistence remains outside the
physical theorem.
