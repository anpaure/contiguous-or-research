# Audit of the Catalan private-hinge packing theorem

**Date:** 2026-08-07  
**Audited source:**
`MATH_THEOREM_CATALAN_PRIVATE_HINGE_BANK_AND_LINEAR_RESIDUAL_DEGREE_20260807.md`  
**Method:** exact catalogue, resource-load, greedy, and residual-degree
audit; no search  
**Verdict:** `GO`.

## 1. Literal hinge

For `U`, `u,b in U`, and `x,y outside U` as in the source, all four labels
are distinct outside the rank-`(m-2)` core `a`.  The displayed path has
rank sequence

\[
 (m-1),m,(m-1),m,(m-1),
\]

and both suppressed edges have intersection `a`.  Its central facet
`X=a+b` lies in the omitted colour `U=a+b+u`.  Thus either edge can be
assigned to `U`, while its mate preserves `a` after deletion.

## 2. Catalogue and load counts

For fixed `U`, ordered choices give

\[
 m(m-1)m(m-1)=g=m^2(m-1)^2.
\]

For a fixed rank-`m` resource, each of the three roles has exactly `g`
preimages.  For a fixed rank-`(m-1)` resource, each role has

\[
 h=(m+1)(m-1)m(m-1)=m(m+1)(m-1)^2
\]

preimages.  For a fixed core `a`, ordered `u,b` and ordered `x,y` give

\[
 \ell=(m+2)(m+1)m(m-1).
\]

Therefore one selected packet conflicts with at most
`9g+9h+ell=D_m g` catalogue members.  Duplicate orientation is harmless:
both orientations share resources and are removed together.

Direct rational comparison gives `D_m<m+1` first at `m=19` and for every
larger `m`.  Hence a maximal resource matching has more than
`W/(m+1)=Cat_m` members.  Theorem 3.1 is correct.

## 3. Degree-control rule

After `t` omitted colours have been chosen there are exactly `mt`
omitted-colour/facet incidences.  If the allowed omission load is
`m+1-delta`, at most

\[
 {mt\over m+1-\delta}
\]

facets are saturated.  Each has exactly `delta` not-yet-selected
supersets, so the number of newly forbidden omitted colours is at most
`delta mt/(m+1-delta)`.  Multiplying by `g` and adding the resource-conflict
loss gives precisely condition (4.2).  At termination every residual facet
degree is at least `delta`.

For fixed `alpha<1/2`, the normalized saturation loss is
`(alpha/(1-alpha)+o(1))m`, strictly below the available coefficient `m`.
For `delta=2`, direct substitution verifies the asserted threshold
`m>=21`.

## 4. Protected loss

Every fixed rank-labelled resource occurs in at most `4g` candidates.
After forbidding `p` such resources, selecting `C` hinges requires

\[
 Wg-4pg>CD_mg,
\]

or

\[
 m+1-{4p\over C}>D_m.
\]

Thus a global polynomial-size protected bank is negligible because
`C=Cat_m` is exponential.  The loss is not `4p` in the normalized
inequality.  The source now displays this normalization explicitly.

## 5. Sublinear exposure and contraction

The sublinear-exposure sampling is also sound.  In a private catalogue
matching, a fixed facet sees at most its `m+1` distinct rank-`m` supersets,
and a fixed rank-`m` set sees at most its `m` distinct facets.  A gadget
contributes at most three relevant resources.  Sampling `C` gadgets from a
matching of size at least `W/(2D_m)` gives inclusion ratio at most
`2D_m/(m+1)`.  Reaching load `24m/log m` requires at least
`8m/log m` relevant gadgets, so the hypergeometric union bound is
`exp(-(8+o(1))m)` per test.  This beats the fewer than `2^(2m+1)` tests.
Thus both exposure bounds are indeed `o(m)`.

The contraction ledger is exact: removing `3C` protected lower resources
and replacing each hinge by one supervertex gives

\[
 (mC-3C)+C=(m-2)C,
\]

while removing the omitted and two visited upper resources gives

\[
 (m+1)C-3C=(m-2)C.
\]

Expansion/contraction preserves a Hamilton cycle containing every forced
path.  Parallel endpoint roles at the one common upper neighbour cannot be
used as an isolated two-cycle inside a spanning Hamilton cycle.

## 6. Host scope

Resource privacy supplies distinct omitted colours, visited upper colours,
incidence vertices, and hinge intersection colours.  If one Hamilton cycle
contains these incidence paths and covers every intersection colour, one
edge from each hinge is a literal common-basis deletion: its endpoint maps
to the corresponding omitted colour and its mate retains the deleted
edge's intersection colour.

The theorem correctly does not infer such a Hamilton extension from linear
minimum degree.  It also makes no exterior-forest, residence, deeper-shadow,
or compiler claim.
