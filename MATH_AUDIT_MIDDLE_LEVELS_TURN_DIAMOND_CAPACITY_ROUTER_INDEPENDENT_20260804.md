# Independent audit: Middle-Levels turn-diamond capacity router

**Date:** 2026-08-04  
**Method:** direct symbolic rederivation only; no search, finite experiment,
or computational construction.

**Audited theorem:**
`MATH_THEOREM_MIDDLE_LEVELS_TURN_DIAMOND_CAPACITY_ROUTER_20260804.md`,
SHA256
`a7176faaf6cd44768df058423c4f492018fa0f6b256008dd0de80cf3ecf85ef7`.

## 0. Verdict

The theorem passes.  Its unconditional content is exactly a router in the
serialized owner/q1 occurrence complex.  Its common-cap application remains
conditional on occurrence activation, terminal typing, and compensation
privacy.  The two-coordinate cut obstruction and product-layer repair are
also exact.

## 1. Literal diamond identities

At turn `j`, the factor gives

\[
 U_j=L_j\cup\{a_j\},\qquad
 U_{j+1}=L_j\cup\{b_j\},\qquad a_j\ne b_j.
\]

Hence its upper q1 occurrence has value

\[
 R_j=U_j\cup U_{j+1}=L_j\cup\{a_j,b_j\}.
\]

Both displayed chains

\[
 L_j\subset U_j\subset R_j,
 \qquad
 L_j\subset U_{j+1}\subset R_j
\]

increase rank by one at each step.  They use the unique lower-turn
occurrence, one of its two owner halfports, and the occurrence-labelled
upper q1 turn.  Equal `R_j` values at different turns do not identify the
addresses `(C,j)`.

This verifies the whole local occurrence diamond.  It does not assert that
the cap treats the upper q1 interval as an unused terminal capacity.

## 2. Owner-transversal proof

For one component, choosing the minus branch at turn `j` uses owner `U_j`;
choosing the plus branch uses owner `U_(j+1)`.  Therefore either uniform
choice maps the `ell` lower turns bijectively to the `ell` owner
occurrences.  Lower sources and upper-turn sinks are already indexed by
`j`, so the resulting paths are vertex-disjoint.

For uniqueness, encode branch choices by `c_j in {0,1}`.  Owner `U_j` is
used twice exactly at a cyclic pattern

\[
                         (c_{j-1},c_j)=(1,0).
\]

A unit-capacity routing has no cyclic `1 to 0` transition.  Every
nonconstant cyclic binary word has both a `0 to 1` and a `1 to 0`
transition, so the word must be constant.  Thus the two uniform routings
are exactly all routings which use an adjacent owner and end at the claim's
own upper-turn occurrence.

Restriction of either full routing to an arbitrary claim subset remains
disjoint.  The theorem's parity criterion is deliberately for these
orientation-compatible restricted routings.  A sparse subset could admit
other mixed owner choices, but those do not realize one global factor-side
orientation and are not claimed by the theorem.

## 3. Capacity quotient

At an owner occurrence, the two formal halfports are the two incident factor
edges.  In a uniform routing exactly one is selected.  Consequently the
quotient which identifies both halfports with the owner-cell capacity has
load one, not two.

For a fixed ticket bank every ticket is mandatory, so the quotient load at
owner `U` is literally `d_H(U)`.  The condition

\[
                         d_H(U)\le c(U)
\]

is therefore necessary and sufficient for the owner gate alone.  It says
nothing about sources, terminals, or later suffix intersections, exactly as
the theorem records.

This distinguishes the new router from the former full-port suffix premise:
one claim selects one factor incidence, so the unused halfport need not be
given independent capacity.

## 4. Activation audit

Once a fixed residual cap state contains the displayed source, owner, and
turn-terminal occurrence nodes and both literal arcs, Theorem 2.1 is already
an explicit linkage.  If those nodes avoid the compensation linkage and
each turn terminal is legal, no Menger, Hall, or suffix-gammoid argument is
needed.

Conversely, factor serialization alone cannot prove any of those physical
facts.  In particular it cannot prove:

* that an owner or turn occurrence remains unused after compensation;
* that equal-valued turn occurrences retain separate capacities;
* that an upper q1 occurrence has the required terminal type; or
* that a private tail exists when the q1 occurrence is not itself a sink.

The activation corollary is therefore exact and fail-closed.

## 5. Two-coordinate boundary

With two unit demands at every lower turn, every canonical path crosses the
owner shore.  In one shared physical layer that shore has total capacity
`ell`, while demand is `2ell`.  The max-flow/min-cut upper bound is
`ell`, so simultaneous routing is impossible.  Abstractly naming two
halfports per owner does not change this cut.

If both occurrence coordinates have disjoint copies of sources, owners, and
turn terminals, applying either canonical routing independently in each
layer gives `2ell` disjoint paths.  This proves sufficiency of the stated
product split.

For a smaller prescribed two-coordinate bank, global right-disjointness
does remove the owner alias because it makes `d_H(U)<=1`.  It does not
supply the two source units, and the two canonical branches at one lower
turn still meet its one `z_j` occurrence.  Separate terminal capacities or
different typed sinks remain necessary.  Finally, marginal coordinate
linkages do not imply one common cap state; product closure remains an
independent premise.

## 6. Exact proof boundary

The net implication is

\[
\begin{array}{c}
\text{serialized Middle-Levels factor}\\
\Downarrow\\
\text{two literal turn diamonds per lower occurrence}\\
\Downarrow\quad\text{one component bit}\\
\text{capacity-faithful one-claim router in the occurrence complex}.
\end{array}
\]

The missing implication is still

\[
 \text{occurrence complex}
 \not\Longrightarrow
 \text{active typed residual common cap}.
\]

Thus the theorem is a genuine reduction of the matched-port physical gap,
not a proof of common-cap activation or the all-dimensional construction.
