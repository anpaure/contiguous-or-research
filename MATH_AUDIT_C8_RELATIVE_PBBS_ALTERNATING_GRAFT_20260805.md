# Audit of the relative common-history `C8` graft reduction

**Date:** 2026-08-05  
**Method:** independent symbolic replay; no computation or search  
**Audited theorem:**
`MATH_THEOREM_C8_RELATIVE_PBBS_ALTERNATING_GRAFT_AND_UPPER_BACKUP_20260805.md`  
**Audited theorem SHA-256:**
`d1831c53ea7c226c1c160fcfcd5582e815b79966d1050c2b98e8914934e12cde`  
**Corrected reduction SHA-256:**
`6c0629400a199744d5d5ff88ebd811152f289b578cc016d57bf7b4452419a13e`

## 0. Verdict

**PASS at stated scope.**  The theorem proves an exact normal form for a
colour-compatible local graft relative to a fixed PBBS two-factor and a
pointwise stabilizer backup for isolated-collar upper casualties.  It does
not prove existence of the required `O(d)` return systems, simultaneous
backup packing, exterior upper preservation, or a common cap.

The earlier identification of the screen `C8` with the cyclic
capacity-two receiver sector is correctly withdrawn.  The two graphs have
different edge relations.

## 1. Active hinge replay

With

\[
 L_i=B+b+a_i,\quad I_i=B+a_i,\quad R_i=B+a_{i-1}+a_i,
\]

both `I_i subset L_i` and `I_i subset R_i` hold.  Also
`I_i subset R_(i+1)`.  Thus the old and new right banks really are
incidence matchings on the same four facets and four heads.  Following old
and new edges alternately subtracts one from the index, hence produces one
`C8`, not two `C4`s.

The displayed intersection and union identities are literal.  Therefore
the toggle preserves owner degree, facet degree, the lower facet value at
each role, and the multiset of four upper hinge values.

## 2. Receiver no-go replay

In the cyclic adjacent-token graph, `A_i={b,a_i}` to
`D_i={a_(i-1),a_i}` moves the token at `b` to `a_(i-1)`.  All four old
edges would require four different neighbours of `b`; a cycle gives only
two.  Hence Johnson adjacency cannot be replaced by receiver adjacency.

Necklace quotienting alone is insufficient because the literal packet
uses one common core and one common ordered history.  Independently
rotating endpoint representatives changes those data.  A pointed lift is
therefore a genuine additional premise.

## 3. Exchange-digraph replay

Orient nonmatching incidence edges from the lower shore to the owner shore
and matching edges back.  After contracting matching edges, every
alternating cycle becomes a directed cycle.  Conversely every directed
cycle expands uniquely to an alternating cycle.  A family of directed
cycles is a cycle cover on its switched contracted vertices exactly when
the toggled incidence set is again a perfect matching.

The forced new collar edges are a partial directed injection because each
colour class of the protected collar is a matching.  Forced retained old
edges occupy both endpoints of their matching-pair unit, so excluding those
units from the switched set is necessary and sufficient.  This verifies
Lemma 2.1.

Applying the argument to both colours gives two perfect matchings.  Their
edge-disjointness is separately load-bearing: without it, their union is a
degree-two multigraph with a doubled incidence, not the required simple
factor.  The theorem includes this row.

The equivalence is deliberately restricted to colour-compatible grafts.
A factor rethread whose alternating phase flips along an untouched
component is outside the stated normal form unless its colouring is first
made compatible.

Adding zero-cost diagonal fixed points to the exchange assignment graph
is exact: a perfect assignment is a directed cycle cover, and its nonloop
cost counts precisely the switched contracted vertices.  Thus the
one-colour minimum-support problem is an ordinary min-cost bipartite
matching.  The theorem does not claim that two such optima respect their
shared physical-edge capacities.

The cyclic packing lemma uses only disjoint phase intervals.  It is valid
under its explicit phase-convexity premise and does not establish that a
template has that premise or reaches named PBBS components.

The imported natural-PBBS no-`C8` theorem excludes a directed four-cycle
in the unchanged PBBS exchange graph.  It therefore rules out the direct
four-slot/one-colour installation, but not a larger return system which
first changes the host matching.  The theorem states exactly this scope.

## 4. Rooted return replay

The old next-role map `(0 2)(1 3)` records two old components.  The head
cycle is `(0 1 2 3)`.  Applying the old continuation first and the new head
assignment second gives

\[
 (0\ 1\ 2\ 3)(0\ 2)(1\ 3)=(0\ 3\ 2\ 1),
\]

one cycle.  Degree/matching extension does not determine which remote port
is met next, so the rooted return row cannot be dropped.

For the adaptive phase theorem, each protected open collar path already
puts its opposite role pair in one factor component.  Hence the two paths
are either on one component, in which case the old phase is sufficient, or
on two components, in which case the return is the displayed double
transposition and the toggle fuses them.  This proves Theorem 3.2 without
assuming a rooted selector.  If the statement requires the toggle itself
to merge two named bodies, their pre-toggle distinctness remains a real
premise.

## 5. Stabilizer replay

If a path witnesses upper value `Z`, every owner and intervening lower
facet on that path is contained in `Z`.  Under a uniform permutation of
`Z`, a fixed rank-`s` vertex is uniform among the `binom(|Z|,s)` such
vertices.  The union bound gives exactly inequality (5.1).

For an isolated collar, both the witness path and forbidden active bank
have `O(d)` vertices.  At casualty rank at least `r+2`, the two orbit
denominators are at least `binom(r+2,2)` and `binom(r+2,3)`.  With
`d^2=Theta(r)`, the collision probability tends to zero.  Thus the
pointwise backup corollary is valid.

Nothing in this calculation couples different targets.  Up to `O(d^2)`
separately chosen paths can have `O(d^3)` total length and need not extend
to one factor.  The theorem correctly declines that conclusion.

## 6. Exact open statement

The owner/q1 graft is reduced, not solved.  Its remaining statement is:

1. extend both collar colour classes by directed return cycles on `O(d)`
   PBBS matching-pair units;
2. keep the reconstructed matchings edge-disjoint; and
3. attach the two protected open paths to the two named PBBS bodies.

Pair-connectivity then removes the independent rooted-selector row.  Only
when the switch itself, rather than adaptive phase choice, must perform the
merge is pre-toggle body separation additionally required.

Even a proof of these three rows would leave grafted exterior upper
intervals and the typed common cap open.  The isolated `O(d^2)` casualty
bound cannot be applied to those exterior intervals.
