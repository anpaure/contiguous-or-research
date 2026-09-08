# Self-audit: GMM tight enumeration versus double-turn fusion

**Date:** 2026-08-05  
**Audited note:**
`MATH_AUDIT_GMM_TIGHT_ENUMERATION_DOUBLE_TURN_FUSION_AND_BALANCED_CUT_20260805.md`

## 1. Parameter audit

For a `(2r-1)`-set,

\[
 W={2r-1\choose r}={2r-1\choose r-1},
\]

\[
 U={2r-1\choose r+1}
   ={r-1\over r+1}W,
\]

so

\[
 W-U={2W\over r+1}
 ={1\over r+1}{2r\choose r}=\operatorname {Cat}_r.
\]

All owner, edge, deletion, and component counts in the note use these
identities consistently.

## 2. Primary-source quantifier audit

The GMM source defines saturating cycles and tight enumerations separately
and says that every consecutive-level interval has both.  Its proof of the
corollary invokes separate earlier theorems for the two objects.  Nothing in
the statement identifies their cyclic order on a shared level.

Gregor--Mütze Theorem 15 applies separately at `k=r-1` and `k=r`.  At
`k=r-1` the shores are balanced, so the output is a Middle Levels Hamilton
cycle.  At `k=r` the output contains rank-`(r+1)` vertices and `Cat_r`
same-rank distance-two steps.  Calling the latter an `ML(2r-1)` Hamilton
cycle would be a type error.  The scope conclusion in the audited note is
therefore correct.

## 3. Projection audit

In the upper tight enumeration, every rank-`(r+1)` vertex is flanked by two
distinct rank-`r` facets, because the smaller partition has no same-shore
step.  Suppression produces one Johnson edge with that upper vertex as its
union.  Every direct step is also a Johnson edge because the construction's
length-two steps remain in rank `r`.  Hence the suppressed graph is indeed
a Hamilton cycle and its union map is surjective.

Deleting all direct steps leaves exactly the subdivided edges, one per
rank-`(r+1)` vertex.  The remainder is spanning, acyclic, has `U` edges,
and therefore has `W-U=Cat_r` components.  No lower injectivity follows.

## 4. Hand-example audit

The complements of the ten triples in (3.3) are, in order,

\[
 12,23,13,14,24,25,35,34,45,15,
\]

which is an Euler circuit of `K_5`: consecutive pairs share, cyclically,

\[
 2,3,1,4,2,5,3,4,5,1.
\]

Thus consecutive triples are Johnson adjacent and their unions are the
five rank-four sets, each twice.  Inserting one occurrence of each rank-four
set and leaving the other five turns direct gives exactly ten rank-three
vertices, five rank-four vertices, ten cross steps, and five length-two
steps.  Since the bipartition difference is `10-5=5`, this enumeration is
tight.  The repeated intersection `45` is literal.  The example correctly
refutes only automatic implication, not existence of another fused cycle.

## 5. Conditional deletion and path-cover audit

For a surjective upper map, deleting all but one occurrence per colour
removes

\[
 \sum_R(\mu(R)-1)=W-U=Cat_r
\]

edges.  The original lower colours are bijective because they are the
lower vertices of the Middle Levels Hamilton cycle.  Hence retained lower
colours are injective.  A cycle minus `Cat_r` edges is a spanning forest
with exactly `Cat_r` components, including the possibility of isolated
owners.

Lifting each retained edge inserts one distinct lower vertex.  A path with
`t` upper owners has `t-1` inserted lower vertices, so every component has
shore imbalance one and endpoints on the upper shore.  There are `Cat_r`
omitted lower vertices and `2 Cat_r` endpoint roles.  A completion assigns
two roles at distinct owner vertices to each omitted lower vertex.  An
isolated owner contributes two roles at the same vertex, which must be used
by two different bridges.  Degree two plus connectedness is exactly
Hamiltonicity; after contracting the paths this is one cycle.
The converse in the note is therefore exact.

## 6. Duality audit

Complementation on a `(2r-1)`-set swaps ranks `r` and `r-1`, swaps ranks
`r+1` and `r-2`, and sends a union to the complement of the corresponding
intersection.  It is an automorphism of the Middle Levels graph.  The
upper- and lower-turn existence statements and their balanced path-cover
forms are therefore genuinely equivalent.

## 7. Final verdict

\[
 \boxed{\text{PASS: the note's negative source-scope verdict and all
 conditional reductions are proof-safe.}}
\]

The all-`r` double-turn existence theorem remains open; the audited note
does not claim otherwise.
