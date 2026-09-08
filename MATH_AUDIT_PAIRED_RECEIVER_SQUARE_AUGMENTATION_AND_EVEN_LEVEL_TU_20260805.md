# Audit: paired receiver-square augmentation and even-level TU reduction

**Date:** 2026-08-05  
**Audited theorem:**
`MATH_THEOREM_PAIRED_RECEIVER_SQUARE_AUGMENTATION_AND_EVEN_LEVEL_TU_20260805.md`  
**Method:** independent literal-square, matching-replacement, parity, and
counterexample replay; no computation  
**Verdict:** PASS with the theorem's fixed passive-pairing and
Hall/Tutte premises.  It is an exact reformulation, not a proof of those
cuts for every PBBS bank.

## 1. Literal square and colours

The four double expansions are indexed by `(alpha,beta) in Q_2`.
The even-parity vertices `00,11` are adjacent to both odd-parity vertices
`10,01`; these and only these are the four square edges.  Hence one job
really has two independent endpoint lists.

For an `alpha`-edge, deleting the moved `p`-cut leaves the chosen endpoint
of the `r`-petal; for a `beta`-edge, deleting the moved `r`-cut leaves the
chosen endpoint of the `p`-petal.  Thus all four receiver hub colours are
parent endpoint colours.  Removing the reset hub vertices from the lower
ordinary selector protects the entire square.  Removing occupied receiver
vertices only shrinks its two endpoint lists and preserves completeness
between the survivors.

## 2. Augmented-matching replay

In a perfect matching of the augmented graph, each private `alpha_j` and
`beta_j` chooses one distinct ordinary endpoint.  Matching capacity makes
all chosen endpoints globally distinct.  The square identity joins each
job's two endpoints by a legal receiver edge.  Replacing the two private
edges by that receiver edge produces the required prescribed pair; all
other ordinary matching edges give the completion.

The reverse replacement is literal and covers both private vertices.
When parity is odd, `omega` consumes exactly the one outgoing socket; when
parity is even, a one-socket residual is impossible by parity and no
`omega` is added.  This verifies both directions of Theorem 3.1.

## 3. Even-level parity

For even coordinate length `ell`, every adjacent transfer changes

\[
                         \sum_i i t_i\pmod2
\]

by one, including the wrap transfer.  An odd-order rotational stabilizer
uses only even shifts and hence preserves that parity.  The quotient is
therefore bipartite.  Each receiver square's `00,11` shore has one parity
and its `10,01` shore the other, so adding one private terminal to the
opposite shore preserves bipartiteness and adds one vertex to each shore
per job.

If an outgoing socket is required, the pre-`omega` shore imbalance must
be exactly one.  Placing `omega` on the smaller shore and retaining socket
candidates on the larger shore is both necessary and sufficient to keep
the augmented graph bipartite and balanced.  Hall and total unimodularity
then apply exactly.

Relative to a base perfect matching, symmetric difference with any
augmented perfect matching has job terminals as its only degree-one
vertices.  Its path components alternate and orient from the private
terminals on one shore to those on the other.  Conversely, flipping a
vertex-disjoint saturating path family gives the augmented matching.  This
verifies the one-commodity router theorem.

For a fixed ordinary shore set `U`, the remaining receiver endpoint lists
have size zero, one, or two.  Representing a two-list as an edge and a
one-list as a loop is exact: assigning jobs injectively to endpoints is an
orientation with distinct heads.  A connected component with `e` edges
and `v` vertices assigns exactly `min(e,v)` jobs (tree orientation when
`e=v-1`, cyclic orientation when `e>=v`).  Its deficiency is therefore
`(e-v)_+`.  Summing components verifies the bicircular surplus formula
and the closed two-shore cut equations.

## 4. Odd-level boundary

For odd coordinate length the capacity-one face is the odd cycle
`C_ell`, so no global shore exists.  Tutte's odd-component inequalities
are exactly equivalent to the augmented perfect matching.  The triangle's
unsigned incidence determinant is two, confirming that the even-level TU
matrix cannot be reused without blossom rows.

The `C_9` bank `01,34,67` leaves three isolated vertices, and the `C_5`
bank `01` with incoming singleton `3` leaves two.  Thus vertex-disjointness
alone does not imply the one-socket extension.  These examples are scoped
to the unrestricted capacity-token statement; the theorem does not claim
that PBBS generates those exact bad banks.

## 5. Exact remaining premise

The old two-stage language—first an edge-orbit SDR and then an extension
matching—is insufficient because distinct edge orbits may share
endpoints.  The augmented graph fixes that logical gap.

The remaining all-level assertion is exactly:

* Hall for the actual augmented graph at every even cut length; and
* Tutte for the actual augmented graph at every odd cut length,

after the special fibres, occupied receivers, two reset colour classes,
and the typed incoming/outgoing socket lists are installed.  No statement
in the audited theorem proves those inequalities automatically.
