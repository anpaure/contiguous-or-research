# Audit: exact OFHT resources and the antichain-top SCD--Hamilton lift

Date: 2026-08-02  
Status: independent proof audit PASS.  This note records the exact joint
scope of the two source theorems.  It proves no literal age cycle, residence,
upper-shadow, compiler, or additive-constant conclusion.

## 1. Authenticated inputs

```text
MATH_THEOREM_OFHT_EXACT_CYCLE_HYPERGRAPH_FUNCTIONAL_HALL_AND_POINTED_FACE_20260801.md
  SHA-256 77cef7655cf0a713f75e00d4818787f0a9a74bcbf756d636118748fc6e262f95

MATH_THEOREM_ANTICHAIN_TOP_SCD_HAMILTON_OWNER_LIFT_AND_LITERAL_AGE_GATE_20260802.md
  SHA-256 dd2dc195a623e21fc9f367c02b1e4443f8d2e8493966d508cd1b92b012f7f977
```

Both hashes agree with the authoritative handoff.

## 2. Exact OFHT and fixed-table Hall scope

Fix the role types, marked positions and named target resources.  A literal
candidate consumes one role, one owner and its complete nested target
payload.  Selecting each resource exactly once and giving every selected
candidate one compatible predecessor and successor is therefore equivalent
to an exact cover by directed-cycle resource hyperedges.  This is an exact
cycle-cover formulation; it has no one-component row.

After a literal flag table is fixed, let an aligned column `a` have head
`q(a)`, owner `o(a)` and predecessor list `L(a)`.  Integral head--owner
variables `u_a` extend to distinct predecessors if and only if

\[
        \sum_{a:L(a)\cap X\ne\varnothing}u_a\ge |X|
        \qquad(X\subseteq P).                              \tag{2.1}
\]

Indeed, after `u` is fixed, the left side is exactly the neighbourhood size
of `X` in the predecessor-to-selected-column graph, so (2.1) is Hall's
theorem.  Before that functional choice the problem remains a three-partite
matching problem.  The Rado form is valid only after a functional
head--owner bijection has been fixed and the stated target-neutrality and
tail-invariance hypotheses hold.

## 3. Antichain-top static lift

Let there be `W` nested, rank-consistent role chains.  Assume:

1. every named target is globally distinct; and
2. the maxima of the nonempty chains form an antichain.

Fix an SCD of the Boolean lattice.  Distinct antichain maxima lie in distinct
SCD chains, and every such chain crosses the owner rank.  Assign those roles
to their containing chains and the empty roles bijectively to the remaining
chains.  Partition each successive set difference, including the final gap
to the owner, into the prescribed age-cell sizes.  This gives distinct
rank-`r` owners and literal **static** states realizing every prescribed
chain.

The global distinctness and antichain-maxima assumptions are load-bearing.
The phrase “static target chains” below always includes both.

## 4. Every odd central matching extends to an SCD

Put `n=2h+1` and fix any perfect matching between ranks `h` and `h+1`.
Suppose ranks

\[
                    h-t,\ldots,h+1+t
\]

have already been decomposed into symmetric saturated chains while
retaining the fixed central edges.  Let `Y` be the chains reaching both
boundary ranks, let

\[
 X={ [n]\choose h-t-1},\qquad Z={ [n]\choose h+t+2},
\]

and use the bipartite shores \(X\mathbin{\dot\cup}Y^-\) and
\(Z\mathbin{\dot\cup}Y^+\).  A new lower
vertex has `h+t+2` comparison neighbours, as does a new upper vertex.  Each
old boundary chain has `h-t` possible extensions on either side.  Give every
comparison edge weight `1/(h+t+2)` and its identity edge weight

\[
                  1-{h-t\over h+t+2}={2t+2\over h+t+2}. \tag{4.1}
\]

Every row and column sum is one.  Thus the square support has a fractional
perfect matching and hence an integral one.  An identity edge stops the old
chain; otherwise the matched lower and upper vertices extend it at both
ends.  Iteration proves that the original arbitrary central matching extends
to a full SCD.

This verifies the nonstandard load-bearing step of the new theorem.

## 5. Exact synchronized conclusion in odd dimension

For `k=2r-1`, take either parity matching `M` of any Middle Levels Hamilton
cycle and extend `M` to an SCD by Section 4.  Apply the antichain-top lift
inside that SCD.  The other parity matching `N` is unchanged.  Consequently
one obtains simultaneously:

* every prescribed static chain target exactly once;
* every rank-`r` owner exactly once, with free owner assignment;
* an SCD whose central matching is that owner matching; and
* one connected alternating Middle Levels incidence skeleton `M union N`.

This is unconditional for every `r>=2` under the hypotheses of Section 3.
It does not apply to a previously fixed SCD, owner map or flag table.  For a
fixed central matching, the exact remaining topology test is Hamiltonicity
of its directed contraction graph; regularity supplies only a cycle cover.

## 6. The exact remaining literal gate

The projected edge

\[
                         q_i-T_i-q_{i+1}
\]

does not imply that an independently built static state at owner `T_i` has
root `q_i`, nor that consecutive states satisfy

\[
              X^{i+1}_{j+1}=X^i_j\setminus X^{i+1}_0.    \tag{6.1}
\]

Thus the opposite parity matching is not yet an OFHT successor matching.
For general age types, (6.1), the role-successor row and their common
integral choice remain exact.  In the all-high sector the same gate reduces
to a resident Johnson Hamilton cycle whose consecutive-intersection decks
contain the prescribed chains.  Adjacent-union owners are then automatic
because the carrier is already a Middle Levels Hamilton cycle.

The two audited theorems do not provide a prescribed role order, fixed
target-to-owner assignment, residence outside that explicit serialization,
deep upper shadows, voltage/opening, common-cap/compiler feasibility, or any
`O(1)` bound for the contiguous-OR problem.

## 7. Facet-absorber arithmetic

The local facet absorber has `q=d+2` owners.  For a fixed rank-`r` owner,
choose the extra point of its rank-`r+1` envelope and the other `q-1`
distinguished facets.  Its exact degree is

\[
                       D=(k-r){r\choose d+1}.             \tag{7.1}
\]

Two owners have nonzero codegree only when Johnson adjacent.  Their common
envelope is then unique, and the distinguished set must contain the two
omitted points, giving

\[
                   \lambda={r-1\choose d},\qquad
                   {\lambda\over D}={d+1\over r(k-r)}.   \tag{7.2}
\]

Uniform edge weight `1/D` is an exact fractional owner cover.  Neither
(7.1) nor (7.2) proves an integral global absorber factor or simultaneous
named-target packing.

## 8. Verdict

Both source notes are proof-safe in their stated scopes.  The authoritative
rebase is therefore:

> Static antichain-top target chains, free owner exactness and one projected
> Middle Levels Hamilton topology are jointly closed in every odd dimension.
> The first nonautomatic row is literal statewise age/intersection chronology.

No stronger contiguous-OR conclusion follows.
