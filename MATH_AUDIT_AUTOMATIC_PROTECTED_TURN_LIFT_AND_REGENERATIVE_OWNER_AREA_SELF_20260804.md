# Self-audit: automatic protected-turn lift and regenerative owner area

**Date:** 2026-08-04  
**Method:** line-by-line symbolic replay; no computation or search  
**Target:**
`MATH_THEOREM_AUTOMATIC_PROTECTED_TURN_LIFT_AND_REGENERATIVE_OWNER_AREA_20260804.md`  
**Target SHA-256:**
`2f6f7ef9358ca19f853e260995e954831478e08bda2342d69e94e107ba6e0e6a`  
**Verdict:** **GO under the explicitly stated selection-stable cap
interface.**

## 1. Protected-factor occurrence lift

The selected wedge contributes exactly two protected incidences at its
lower vertex.  A two-factor has degree two there, so every completion must
use those two owners consecutively around that lower turn.  Their union is
the selected q1 value.  The existing factor-occurrence and turn-diamond
theorems then give both displayed literal containments.

Global distinctness of all selected owner values forbids two selected lower
turns from being consecutive, since consecutive lower turns share one
owner.  Distinct sources, owners and selected q1 terminals make arbitrary
one-side choices pairwise disjoint in the three-layer serialized complex.
The degree-compatible incumbent bank and `|P_*|+2p<=m-2` remain explicit;
the scalar edge count is not used to infer compatibility.

The cycle-aligned wedge theorem independently strengthens the local lift by
making the chosen owner-to-q1 edge equal to an edge of the raw Boolean
full-port linkage.

## 2. Owner-to-terminal projection

A rank-`m` set in a `2m-1` element ground set has exactly `m-1` rank-`m+1`
supersets.  Every nonexceptional terminal value in the background has an
incident owner value in the same background.  Therefore its terminal
projection lies in the union of `f` neighbourhoods of size `m-1`, proving
`g<=(m-1)f+e`.  The argument uses no path order or monotonicity and remains
valid after projecting multiple physical occurrences to one value.

For a genuine alternating owner--terminal path bank every terminal vertex
on an edge has such an owner neighbour.  Only singleton terminals or
non-Boolean remote resources enter the exception bank.

## 3. Layer-energy bad-source count

At source `i`, every inactive wedge lies in one of three priced classes:
both owner sides in `R_i`, a terminal pair in `S_i`, or a hidden pair in
`H_i`.  Hence the inactive count is at most

\[
 {r_i\choose2}+t_i.
\]

The exact simultaneous wedge-packing threshold gives badness only if this
sum is at least `T=C(m-p+1,2)`.  For every admissible split `R`, a bad source
has either `r_i>=R` or `t_i>=T-C(R-1,2)`.  Summing the two energies and
using Markov counting proves the displayed minimum over `R`.

With `R=floor(m/2)+1` and `p=O(sqrt(m))`, the second denominator is at least
`m^2/4` eventually.  Thus `I<=Am,J<=Dm^2` gives at most
`floor(2A)+floor(4D)` omitted sources.  Applying the packing theorem to the
retained smaller family is valid because its threshold is no larger than
the original `B_(p-1)` threshold.

## 4. Quantifier and privacy checks

The selection-stable activation condition is a real premise.  It requires
one fixed cap/guard/phase state and joint coexistence of the selected local
routes.  Any nonendpoint collision not implied by owner/terminal equality
must be priced in `H_i`; private tails cannot be inferred from endpoint
distinctness alone.

Accordingly the theorem does not infer typed survival from factor
serialization.  It proves that serialization creates the occurrence
objects and isolates the remaining cap condition as survival/type/private
tail acceptance.

ROA item 5 is load-bearing: a constant casualty bound per transition gives
an additive constant only when the state is regenerated, rather than when
all ancestral sidecars or footprints are accumulated.

## 5. Scope conclusion

The theorem soundly reduces the physical cap row to:

1. a selection-stable typed activation atlas;
2. linear owner projection, or directly linear owner task-energy;
3. quadratic terminal-only/hidden exceptions; and
4. nonaccumulating regeneration.

It does not prove those four statements for the current Pascal child, nor
does it close the two-coordinate product, upper, residence, topology, or
compiler rows.  No unconditional `B(k)+O(1)` claim follows from this file
alone.
