# Audit: odd circulation blossom lift

**Date:** 2026-08-05  
**Audited theorem:**
`MATH_THEOREM_ADJACENT_NECKLACE_ODD_CIRCULATION_BLOSSOM_LIFT_20260805.md`
  
**Method:** direct vector-difference and parity audit; no search  
**Verdict:** PASS.  The local lift and the fixed-level hub-rainbow packing
criterion are exact; existence of the required rainbow residual bank remains
open.

## 1. Path legality

For

\[
 v_t=x-e_c+e_{c-t},
\]

the transition `v_(t-1)->v_t` moves the travelling unit from `c-t+1` to
`c-t`.  At `t=1` the donor is `c`, whose load is two.  Subsequently the
donor holds the travelling unit in addition to its original load.  Thus no
step attempts to subtract from zero.

Distinct `t` give distinct positive-anomaly coordinates, so the labelled
path is simple.  At `t=q-1`, the anomaly is at `c+1`, giving the displayed
state `(1,1,1)`.

## 2. Cycle and tail parity

The long route has `q-1` edges.  The direct `x-w` edge closes a `q`-cycle,
which is odd.  The tail `w-y` is legal because the third local coordinate
is one.  Deleting `w` leaves `q-1` cycle vertices, an even path, so the
listed matching plus `wy` is exact.

## 3. Smaller-gap dictionary

Moving centre `c` to `c+1` increases its preceding cyclic gap by one and
decreases its following gap by one.  The following gap must initially be
at least four so that all post-move gaps remain at least three.  Subtracting
three from every gap gives exactly one adjacent weak-composition transfer.

No reflection or long transposition is introduced.

## 4. Fixed-level collision audit

For a nonhub circulation vertex, the removed cut leaves a zero preceded by
one.  Every other surviving zero is preceded by two or three, so this
locates the removed centre uniquely.

After the centre is fixed, equality of two interiors at the same cut
cardinality makes the difference of their cut incidence vectors a single
root `e_r-e_(r')`.  The cyclic discrete derivative identity says the
difference of the two cut indicators is constant on one cyclic interval.
An interval of length at least two would put adjacent cuts in one of the
two admissible cut sets; an interval of length one changes cardinality.
Thus equal cardinality forces equal cut data and equal travelling
coordinate.

The recovery is intrinsic and commutes with rotation.  Distinct endpoint
orbits, distinct hub orbits, and fixed-level injectivity therefore imply
vertex-disjoint quotient gadgets exactly as stated.

## 5. Quotient scope

The labelled vertices in one blossom are distinct.  The theorem proves
orbit-disjointness for a fixed cut level under the hub-rainbow hypothesis.
It does not prove that the vertical-toggle residual monomers admit enough
horizontal edges satisfying that extra colour constraint, nor does it
compose banks from different cut levels without separate phases.

## 6. q=15 calibration audit

The two horizontal edges use four distinct three-cut vertices.  Coarsening
their moved boundaries gives the distinct hubs `[9,0]` and `[7,2]`.

After removing those six critical vertices, the remaining incidence list
is checked by the coarsening rule

\[
                         (u,v)\mapsto u+v+3.
\]

The one-cut vertex expands to every `B_j`, and the five-cut zero vector
coarsens to `C_0`.  The two `B-A` and four `C-A` incidences in the theorem
give pairwise distinct endpoints and exhaust all remaining named types.
Thus eight vertical edges cover sixteen vertices, while the two disjoint
blossoms cover the other six critical vertices plus their private
interiors.

This verifies the calibration conditional only on those interiors being
free from earlier ambient stages, exactly as stated.

## 7. Verdict

All local formulas and matching edges check.  The construction genuinely
supplies an odd interacting resource absent from the free current and the
exit-only toggle graph:

\[
 \boxed{\text{every smaller-gap edge has a literal odd circulation
 blossom lift, and hub-rainbow edge banks lift disjointly.}}
\]
