# Audit: joint fan/endpoint selector and linear-loss obstruction

**Date:** 2026-08-05  
**Audited theorem:**
`MATH_THEOREM_JOINT_FAN_ENDPOINT_THREE_MATROID_GATE_AND_LINEAR_LOSS_OBSTRUCTION_20260805.md`  
**Method:** independent matroid and literal-cube replay; no computation  
**Verdict:** PASS with fixed active anchors.  The obstruction rules out
post-hoc bounded repair, not a correlated choice of the parent factor.

## 1. Selector replay

Choosing exactly one candidate from every fan is a base of the partition
matroid `P`.  Endpoint SDR on one diagonal shore is independence in its
transversal/bicircular matroid.  Hence complete selection is exactly a
cardinality-`|F|` member of `P cap M_A cap M_B`.

If every `P`-independent set is already `M_A`-independent, the `M_A` row is
redundant.  Edmonds' two-matroid formula applied to `P,M_B` gives

\[
 \nu=\min_X(r_P(X)+r_B(E\setminus X)).
\]

The displayed fan-private sufficient condition really implies the premise:
a `P`-independent set uses at most one candidate per fan, and endpoint sets
from different fans are disjoint.

## 2. Why three pairwise tests do not compose

For two two-choice fan blocks, let `A` forbid equal labels and `B` forbid
unequal labels.  An unequal choice satisfies `P cap M_A`; an equal choice
satisfies `P cap M_B`; and two choices from one fan can satisfy
`M_A cap M_B`.  But no one-per-fan choice satisfies all three.  A mandatory
base edge plus candidate parallel edges realizes each capacity-one conflict
inside a bicircular matroid.  Thus the abstract warning is exact.

## 3. Growing literal sector replay

There are `8h+1` coordinate pairs, each of mass three, so

\[
 \ell=2(8h+1)=16h+2,
 \qquad
 R=3(8h+1)=24h+3.
\]

The coordinate length is even and the mass is odd.  Every variable move is
`12 <-> 21`, and deleting its cut leaves residue five, so all parent
endpoints remain critical.

Each block of eight direction bits supplies four group directions.  The
two displayed `C_4`s use all four once at their common zero vertex.  Across
blocks the direction sets are disjoint, so all `2h` cycles may share that
one `B` endpoint without reusing a receiver-square boundary edge.  Away
from the zero vertex the cycles are disjoint.

Consequently

\[
 e_B=4(2h)=8h,
 \qquad
 v_B=1+3(2h)=6h+1.
\]

Every `A` endpoint belongs to only one selected face: two faces in one
block intersect only at displayed `B` vertices, and faces from different
blocks have their unique noncross group in different direction blocks.
Thus the `A` graph is a matching.

A superincreasing background prevents rotational or deleted-hub
coalescence.  One private active split block per square gives a fixed
three-petal fan with exactly the displayed passive pair.  Those active
endpoints use cuts absent from all passive endpoints and can be made
pairwise distinct.

The connected `B` bouquet has bicircular rank

\[
                         \min(8h,6h+1)=6h+1.
\]

Therefore at least `2h-1` singleton fan tasks must be omitted.  Keeping
one `C_4` intact and deleting one edge from every other `C_4` gives a
connected unicyclic spanning subgraph with `6h+1` edges, so the loss is
sharp.

## 4. Scope replay

The construction fixes the active petal at every fan.  If a global parent
selector is allowed to replace those anchors or parent edges, it may avoid
the catalogue.  Hence the correct conclusion is:

*local fan axioms do not imply an `O(1)` post-hoc receiver loss; endpoint
rank must be imposed during parent/anchor selection.*

The example has trivial stabilizer and therefore says nothing negative
about the separate theorem that invariant pseudoforests descend through
odd rotational quotients.
