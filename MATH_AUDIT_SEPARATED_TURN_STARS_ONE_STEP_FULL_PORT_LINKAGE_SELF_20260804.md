# Self-audit: separated-turn one-step full-port linkage

**Date:** 2026-08-04  
**Method:** symbolic proof audit only; no computation or search  
**Target:** `MATH_THEOREM_SEPARATED_TURN_STARS_ONE_STEP_FULL_PORT_LINKAGE_20260804.md`

## Verdict

The proof is internally complete under its stated hypotheses.  The result
is a value-level Boolean-incidence linkage and its typed-occurrence
corollary remains explicitly conditional on materialization and deletion
pricing.

## Checks

1. If two rank-`m-1` sources have exchange distance `d`, their union has
   rank `m-1+d`.  A common rank-`m` owner forces `d<=1`; a common
   rank-`m+1` terminal forces `d<=2`, and at `d=2` that terminal is the
   unique union.  Thus pairwise distance at least two gives disjoint owner
   stars and at most one common terminal per source pair.
2. At induction step `i`, at most one selected terminal from each earlier
   source can lie in the current terminal cloud.  Hence at most `i-1`
   edges are deleted from the current `K_m`.
3. The residual minimum degree is at least `m-i`.  Under
   `i<=p<=floor(m/2)` this is at least `m/2`; with `m>=3`, Dirac applies.
4. Orienting a Hamilton cycle assigns each of the `m` owner coordinates to
   its outgoing cycle edge.  Different vertices have different outgoing
   edges, so this is an injection into terminals and every terminal contains
   its assigned owner.
5. Owner-star disjointness and induction-level terminal avoidance make all
   `pm` one-edge paths vertex-disjoint.
6. Deleting a unit-capacity bank can hit at most one of these paths per
   deleted vertex.  Retaining every unhit path proves the exact corank bound
   `K<=h_F<=|F|`; no matroid-contraction assumption is used.
7. The final wedge conclusion uses only the full-set corank hypothesis of
   the frozen near-full owner-gammoid theorem and stays in its valid range
   `p<=m-1`.

## Scope exclusions

The theorem does not prove pairwise source separation in the regenerative
carrier, physical occurrence injectivity, terminal typing, survival of
source/prefix resources, or bounded deletion cost.  It proves the raw
full-port linkage once those separated literal sources and Boolean layers
are present.
