# Self-audit: arbitrary bounded-turn full-port linkage

**Date:** 2026-08-04  
**Method:** symbolic proof audit only; no computation or search  
**Target:** `MATH_THEOREM_BOUNDED_TURN_STARS_ONE_STEP_FULL_PORT_LINKAGE_20260804.md`

## Verdict

The Boolean-value theorem and its deletion-corank corollary are exact under
the stated hypotheses.  Physical occurrence materialization and bounded
deletion remain explicit premises.

## Checks

1. Two distinct rank-`m-1` sources at exchange distance `d` have union
   rank `m-1+d`.  This gives exactly one common owner at `d=1`, and
   terminal-cloud intersection sizes `m-1,1,0` at `d=1,2,>=3`.
2. At `d=1`, the common terminal cloud is a vertex-star in each source's
   `K_m`.  Any subset of a Hamilton cycle uses at most two of those edges.
   Thus each earlier source forbids at most two current terminal edges,
   even though the unrestricted cloud intersection has size `m-1`.
3. At stage `i`, deleting at most `2(i-1)` edges lowers minimum degree by
   at most that amount.  The hypothesis
   `i<=p<=floor((m+2)/4)` gives `m-2i+1>=m/2`, so Dirac applies.
4. Orienting the new Hamilton cycle assigns distinct outgoing edges to all
   newly seen owner ports.  Skipping a port already present in the earlier
   union cannot create a duplicate: its outgoing edge is simply unused.
5. Every selected terminal contains its assigned owner.  Old terminal
   avoidance is enforced by deletion from the current `K_m`, and the new
   terminal subset remains cycle-supported, closing the induction.
6. At termination each distinct port in the union is assigned exactly
   once and all endpoints are distinct.  The displayed one-edge paths are
   therefore pairwise vertex-disjoint.
7. A deleted unit-capacity vertex meets at most one displayed path, proving
   `K<=h_F<=|F|`.  Applying the frozen near-full theorem uses only its
   full-set corank row and remains within `p<=m-1`.  The corollary separately
   assumes the exact occurrence-faithful source prefixes, typed containment
   edges and compensation-disjoint suffix sinks required by that theorem;
   value containment is not used as a substitute for a physical edge.

## Scope exclusions

No claim is made that the current child exposes the selected rank-`m+1`
terminal occurrences or containment edges, accepts their exact types,
materializes private source-to-owner prefixes, protects all source and
prefix resources, or has deletion footprint at most `m-p`.  The theorem
proves the raw Boolean incidence linkage needed before those physical
filters.
