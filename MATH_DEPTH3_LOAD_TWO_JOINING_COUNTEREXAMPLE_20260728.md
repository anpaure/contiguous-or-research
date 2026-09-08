# A load-two counterexample to support-preserving transition joining

Date: 2026-07-28

Status: unconditional finite counterexample with a compact machine-readable
certificate and independent verifier.  It refutes only the proposed
universal implication

\[
  \min_S d_S\ge2
  \quad\Longrightarrow\quad
  \text{the transition components can be joined without a hole}.
\]

It does **not** refute the frozen `k=15` table, whose component/label
incidence may satisfy a stronger cut condition.

## 1. Statement

There is a connected loopless Johnson multigraph on rank-four subsets of
`[12]` with a safe local transition system, two end stubs, and the following
properties.

1. Its transition graph consists of one path and three cycles.
2. Every rank-two transition label has multiplicity at least two.
3. No re-pairing of the same edge copies can make the transition graph
   connected while retaining every rank-two label.

Thus pointwise redundancy two is not a sufficient support theorem for the
cross-switch mechanism of
`MATH_DEPTH_THREE_TRANSITION_SYSTEM_AND_COMMON_ORDER_GATE_20260728.md`.

## 2. The three-label obstruction

Put

\[
 p=\{0,1\},\qquad q=\{2,3\},\qquad r=\{4,5\},
\]

and define the rank-four owner types

\[
 A=p\cup q,\qquad B=p\cup r,\qquad C=q\cup r.
\]

Four safe closed Johnson walks `C1,C2,C3,C4` have owner intersections

\[
 C_1\cap C_2=\{A\},\quad
 C_2\cap C_3=\{B\},\quad
 C_3\cap C_4=\{C\},
\]

and no other cross-intersections.  Their two transition labels at the three
contacts are

\[
 (p,q)\text{ at }A,\qquad
 (p,r)\text{ at }B,\qquad
 (q,r)\text{ at }C.                                      \tag{2.1}
\]

At a rank-four owner, a transition label is the complement of the omitted
coordinate pair.  Since the two labels in each pair in (2.1) are disjoint,
the two corresponding omitted pairs are also disjoint.  The original local
pairing leaves the macro cut disconnected.  Either cross-pairing connects
the two sides but replaces both displayed labels by mixed labels, retaining
neither one.

The macro contact graph is the path

\[
 C_1-A-C_2-B-C_3-C-C_4.                                  \tag{2.2}
\]

Consequently every connected final transition system must cross-pair at all
three owners.  It then removes both copies of `p`, both copies of `q`, and
both copies of `r`.

## 3. Completing every other label without opening another route

The raw four-cycle core already gives each of `p,q,r` exactly twice.  To
make the scalar hypothesis literally complete, attach 30 additional safe
closed Johnson walks to `C1` at the common owner

\[
 H=\{0,1,3,8\}.
\]

Every attached walk has transition label `{1,3}` at `H`.  Identical omitted
pair types can be cross-paired at `H`, so all 30 walks merge into `C1`
without changing any label.  Whenever two walks in this enlarged first
macro component share any other owner, their transition labels there are
also identical.  None meets `C2,C3,C4` at an owner.  Hence internal
re-pairing cannot create a new macro route or replenish `p,q,r`.

The 34 displayed walks together use 217 owner types and give every rank-two
subset of `[12]` load at least two.  Exactly three owner types carry more
than one omitted-pair type: `A,B,C`.  At every other owner, arbitrary safe
re-pairing merely permutes copies of one type and cannot change a label.
After merging the gadgets at `H`, delete one remaining `{1,3}` pairing edge.
This supplies the two global end stubs and turns the enlarged `C1` into the
unique path component; the minimum label load is still two.

Now (2.2) remains the entire macro contact graph.  There are three possible
local pairings at each bridge owner: the original pairing and two crossing
pairings.  Exhausting the `3^3=27` final bridge states gives eight connected
states and zero connected states with complete support.  In every connected
state the final loads of `p,q,r` are all zero.

## 4. Consequence for the proof architecture

The proposed load-two lemma must be replaced by a cut-aware condition.  One
exact necessary condition is:

> for every cut of the transition components, the labels whose last
> protected occurrences are forced to cross that cut must admit a choice of
> local switches with nonzero residual load.

Equivalently, one needs a labelled component-joining tree plus a protected
occurrence transversal; pointwise multiplicity alone forgets how the two
copies are distributed across macro bridges.  This is the same distinction
as ordinary degree conditions versus Hall cuts in the earlier compiler
analysis.

The certificate and verifier are:

```text
scratch/depth3_load2_joining_counterexample.json
scratch/verify_depth3_load2_joining_counterexample.py
```

The verifier checks every Johnson adjacency, every safe triple, all owner
intersections, the complete 217-owner pair-type census, complete rank-two
support after opening the path, the three critical loads, and all 27
bridge-pairing states.  Since only `A,B,C` have multiple pair types, this
enumeration covers the whole fixed-end local-pairing fibre, not merely the
greedy `c-1` switch sequences.
