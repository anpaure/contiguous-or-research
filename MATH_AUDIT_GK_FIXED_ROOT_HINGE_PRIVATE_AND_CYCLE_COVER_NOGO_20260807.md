# Audit: canonical closing-step GK private/cycle-cover obstruction

**Date:** 2026-08-07  
**Audited theorem:**
`MATH_THEOREM_GK_FIXED_ROOT_HINGE_PRIVATE_AND_CYCLE_COVER_NOGO_20260807.md`  
**Verdict:** **GO for the canonical first-upstep, closing-step subfamily.**

The endpoint substitutions show that an oriented root edge `U -> V`
claims exactly the opposite fixed facet `X_V` and its private auxiliary
resource `Z_e`.  Therefore strict disjointness from the full `X` bank is
impossible.

Under the relaxed controlled-overlap interpretation, choosing one edge per
root gives outdegree one.  Distinct opposite facets give indegree at most
one, while distinct `a_e` or `Z_e` forbids selecting both orientations of
one edge.  Hence the selector is exactly an oriented cycle cover, or an
undirected spanning 2-factor of the bipartite root graph.

For the mountain word `1^m0^m`, the only four-record decomposition
`1A1B0C0D` has `A=C=D=empty` and `B=1^{m-2}0^{m-2}`.  Thus its root-graph
degree is one, excluding a spanning 2-factor.

The full GK catalogue allows any of the `m-1` downsteps in the mountain's
child subtree, so the mountain has full-catalogue degree `m-1`; the
degree-one statement is only about `R_m`.  This audit does not extend the
no-go to that full catalogue, other distinguished upsteps, rotated SCD
matchings, or non-GK first matchings.
