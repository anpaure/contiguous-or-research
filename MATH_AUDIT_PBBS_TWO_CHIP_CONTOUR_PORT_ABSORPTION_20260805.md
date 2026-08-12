# Audit of two-chip contour-port absorption

**Date:** 2026-08-05  
**Audited theorem:**
`MATH_THEOREM_PBBS_TWO_CHIP_CONTOUR_PORT_ABSORPTION_20260805.md`  
**Method:** independent distance, permutation, and packing audit; no search  
**Verdict:** **RETRACTED.**  The earlier PASS audit checked the undirected
port order and the abstract contour permutation separately, but did not
check their orientation coupling or the action-angle velocity converting
vacancy position into directed PBBS time.  It must not be used to support
Theorem 5.1.

## 0. Retraction reason

The rooted realizations at `+d` and `-d` exchange the two child shores.
Thus a mixed sign pattern chosen only to realize a desired parent cyclic
order need not give one coherent C6 orientation across the path.  For
`E=4`, the coherent sign pattern yields the inverse of the previously used
path contour under the geometric slot order.  In addition, that geometric
order equals physical PBBS order only after multiplication by the exact
hook velocity unit, which the old audit did not compute.  The claimed
identity `gamma=beta alpha` is therefore unproved.

## 1. Angle and port rows

For two chips on an odd `q=2h-1` cycle, shorter distance takes every value
`0,...,h-1` once.  Adjacent transfer changes it by one; the outward move at
the last value is a quotient loop.  The simple graph is therefore the
claimed path with `E=h-1` edges.

Deleting the moving chip leaves the unique one-chip base.  The two possible
root cuts are reflected, so after double-zero promotion their marked cuts
have relative positions `+d,-d`, up to a common origin.  This uses the mark;
the unmarked promoted necklace is the same at every edge.

## 2. Contour row

At path vertex `C_i`, the two incident edge labels are `(i,i+1)`.  The
products over even and odd internal vertices are exactly the displayed
`alpha,beta`.  Direct multiplication gives

\[
 1\mapsto2\mapsto4\mapsto6\mapsto\cdots
 \mapsto(\text{largest odd})\mapsto\cdots\mapsto3\mapsto1.
\]

Choosing positive ports for label one and the even labels, and negative
ports for the remaining odd labels, puts them around the parent in this
same cyclic order.  There is no hidden reflection: reversing all connector
orientations simultaneously replaces every permutation by its inverse and
leaves the cycle count unchanged.

## 3. Reconnection row

The plane-tree contour `beta alpha` is one cycle.  A path fragment crosses
the three C6 shores once before returning to its original shore, so the
third return map is `gamma beta alpha`.  With `gamma=beta alpha=pi`, this
is `pi^2`, which has `gcd(E,2)` cycles.  This verifies both parity cases.

## 4. Physical packing row

Distinct marked parent ports are distinct rooted shape positions.  A q2
protected halo contains only a bounded number of predecessor/successor
shape positions.  Therefore only a bounded number of the selected parent
ports can have overlapping shape projections.  Child components form a
path and have incidence degree at most two.  The support-conflict graph is
thus bounded-degree.

For each conflict edge, free ground rotation excludes at most `B^2`
relative phases.  Greedy list coloring from `2m+1` phases works once `m`
exceeds an absolute constant.  Ground rotation changes coordinate phase,
not the marked shape position, so it does not disturb the contour order.

## 5. Scope check

The proof begins with the one-chip parent and all two-chip children as
separate original PBBS components.  It does not justify applying the same
family after the rigid and named-hook switches have already cut those
components.  The theorem explicitly excludes that splice and all post-q2
compiler gates.
