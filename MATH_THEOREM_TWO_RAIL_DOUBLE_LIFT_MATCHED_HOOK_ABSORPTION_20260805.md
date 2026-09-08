# Two parent rails absorb every matched hook pair without a contour order

**Date:** 2026-08-05  
**Method:** directed cut-path topology and local q1/q2 composition; no
search  
**Status:** unconditional topology theorem.  Its hook application is
conditional only on a matching of the child angle graph and on choosing the
two stated halo-disjoint literal lifts, one on each existing parent rail.

## 1. Four-cycle double lift

Let

\[
                         R_0,R_1,U,V
\tag{1.1}

be four distinct directed factor cycles.  Choose two disjoint directed
edges on each of `U,V`, denoted `A_U,B_U,A_V,B_V`, and one edge `A_0` on
`R_0`, one edge `B_1` on `R_1`.

Perform a clean C6 on

\[
                         (A_0,A_U,A_V)
\tag{1.2}

and a second clean C6 on

\[
                         (B_1,B_U,B_V).
\tag{1.3}

The two C6 orientations may be chosen independently.

### Theorem 1.1 (four-cycle two-rail absorption)

After both switches, the union of the four old cycles consists of exactly
two directed cycles.  Each new cycle contains a nonempty path fragment of
both `U` and `V`.  Hence both fresh child cycles are split across the two
output rails.

### Proof

Apply (1.2) first.  It is a genuine `1+1+1` C6 and merges `R_0,U,V` into
one directed cycle `M`; `R_1` remains separate.

The two cuts `B_U,B_V` lie on `M`, while `B_1` lies on `R_1`.  Thus the
second C6 has cut distribution `2+1`.  Cutting `M` at `B_U,B_V` produces
two nonempty directed paths: one contains the `U` fragment between its two
cuts and the complementary `V` fragment, and the other contains the
opposite `U,V` fragments.  Cutting `R_1` produces one directed path.

A three-cycle reconnection of two paths from one old cycle and one path
from another old cycle always closes exactly two directed cycles: one of
the two `M` paths is concatenated with the `R_1` path, and the other closes
through the remaining reconnection.  Reversing the C6 orientation exchanges
which path receives `R_1` but not the count.  Both `M` paths contain
material from `U` and `V`, proving the final assertion.  `square`

The same count also follows from the cut-permutation parity theorem: a C6
is even, so the even component count cannot become one, while the explicit
two-path decomposition rules out four.

### Corollary 1.2 (palette-transparent absorption)

If both switches are selected common-pivot q2-neutral clean C6s and their
protected halos are disjoint, the operation preserves lower q1, immediate
upper q1, and selected q2 exactly while propagating exactly two rails.

The C6s need not use the same original promoted-parent torus and need not
have a common marked-port order.  Their third shores need only lie on the
two different current parent rails.

## 2. Hook matching lift

Let `G_(q,b)` be the adjacent-unit-transfer graph of hook tori at one action
level.  Suppose `M` is any matching in this graph.  Every matched edge
`UV` has one selected q1/q2-neutral leaf-plucking C6 and, for sufficiently
large dimension, two vertex-disjoint ground rotations on the same component
triple.

Assume inductively that its promoted parent block has two rails `R_0,R_1`
and that the marked parent occurrence of one lift lies on each rail, with
the complete q2 halos disjoint.  Then Theorem 1.1 absorbs `U,V` and leaves
two rails, each containing material from both children.

### Theorem 2.1 (matched hook absorption)

Under the stated literal occurrence/halo premise, every matched child pair
can be absorbed independently into the two parent rails, in any order,
without increasing the number of rails and without using a global
third-shore contour permutation.

### Proof

Matching edges have child-disjoint endpoints.  Before processing `UV`, its
two child cycles are fresh.  Apply Corollary 1.2 with the current two parent
rails.  The output again has two rails and contains both fresh children on
both rails, so it has the same interface for later hook levels.  Induction
over the matching edges proves the claim.  `square`

## 3. Consequence for the global hook gate

The cool-lex directed-port problem is not mandatory if the full hook angle
graph has a matching with bounded deficiency.  More precisely, if every
`G_(2h-1,b)` has a matching leaving at most `C` prescribed hook tori, and
the two-lift halo premise above is available, then all matched tori enter
the inherited two-rail block.  Only the `C` unmatched tori at each required
regenerative boundary remain for a named-spine or sidecar argument.

The exact new combinatorial target is therefore

\[
 \boxed{\operatorname{def}_{\rm match}(G_{2h-1,b})=O(1),}
\tag{3.1}

preferably zero for even order and one for odd order.

The theorem does not prove (3.1), nor that an arbitrary marked promoted
parent has one halo-disjoint lift on each current rail.  It proves that,
once those two inputs hold, neither marked-reflection conjugacy nor a
monotone physical `gamma` is needed for topology or q1/q2.

No all-depth source, arbitrary-upper, residence, common-cap, or all-`k`
claim is included.
