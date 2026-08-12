# Self-audit: rooted pull transversal and fixed-matching obstruction

**Date:** 2026-08-04  
**Verdict:** author self-audit **GO**, pending independent review.  No
computation, search, or solver output is used.

Audited theorem:
`MATH_THEOREM_COMMON_CORE_ROOTED_PULL_TRANSVERSAL_AND_FIXED_MATCHING_OBSTRUCTION_20260804.md`.

## 1. Rooted pull identity

A maximal forest of the transparent pull host contracts exactly one host
component at a time and cannot connect distinct host components.  Since all
pulls avoid the protected bank, a contracted factor component contains a
hinge exactly when its host component contained an original hinge-bearing
factor component.  Therefore the number of residual hinge-free factor cycles
is exactly the number of rootless transparent-host components.  This proves
both directions of Theorem 1.1 inside the stated fixed-host/tree-compatible
scope.

The cut criterion is exact: a rootless host component gives a nonempty
root-free set with empty cut, while any such set is a union of rootless host
components.  Adding a universal root vertex joins all rooted components and
leaves precisely the rootless ones separate, giving graphic rank
`|C|-q_0`.

For a root-free set `X`, the surviving cut size is exactly
`|delta_H(X)|-b_D(X)`.  The sum of per-occurrence cut loads is only a union
bound and is presented as a stronger sufficient condition, not an equality.
If both endpoints of every deleted host edge are roots, every proper
transparent-host component sees a deleted boundary edge whose endpoint
inside that component is a root; the whole-host case uses nonemptiness of
the root bank.

Distinct transparent-host components require distinct root vertices, giving
the root-capacity inequality.  In the two-stage statement, every final
component either inherits a background-stage root or has a newly deleted
ring edge on its boundary; two-sided shielding supplies a root in the latter
case.  The Hall statement is explicitly conditioned on absence of further
cross-role conflicts and covers only placement among the background host
components.

## 2. Hypergraph scope

The Berge-forest statement explicitly assumes a rooted spanning Berge forest,
tree compatibility, and a leaf order in which each circuit contracts its
listed components without damaging the protected bank.  Mere connectivity of
the circuit-incidence graph is explicitly not promoted to this property:
overlapping hyperedges can revisit an already contracted component and split
it.  Under the stated assumption, induction from the root is exact.

## 3. Fixed matching

Alternating the two perfect matchings turns each factor circuit into a cycle
of the successor permutation.  Exact root support of the bank is essential:
both factor incidences at each root lie in the bank and every selected bank
edge is root-incident.  Hence deleting the hinge bank breaks exactly the
factor circuits which meet a root.  On the nonroot vertices, a selected
permutation subgraph has indegree and outdegree at most one, so graphic
dependence is equivalent to a directed cycle.

The head-swap rule is the standard multiplication of a permutation by a
transposition on its values.  Its merge/split sign depends on the incumbent
cycle placement, so local circuit abundance alone is not a descent theorem.

## 4. Abstract obstruction

For any loopless digraph `Q`, the bipartite graph with fixed identity
matching and edge `x u_y` for each arc `x to y` has successor graph exactly
`Q`.  A second perfect matching is a cycle cover.  With one root, every cycle
meeting that root means there is exactly one cycle, so the desired object is
a directed Hamilton cycle.  This is a faithful structural embedding; the
argument does not rely on a complexity-theoretic conclusion.

## 5. Ring caveat

The theorem closes only component coverage.  It explicitly does not infer
that the current ring's one fixed cyclic head shift fuses a factor when
several hinges lie on one component.  That induced permutation is a separate
ordering row unless an all-pairs completed hinge bank is available.

A ring root bank is every extension of one `(m-2)`-core except one.  If one
core lies in every component's lower shadow, representatives chosen in
different components are automatically distinct; with at most `m`
components, one of the `m+1` extension labels remains available as the
omitted label.  This proves both directions of the panchromatic-core
criterion.  The shadow condition is a direct union bound on the missing-core
events.

For the dense benchmark, deleting all unmarked labels from a rooted
permutation and reinserting them as ordered lists gives exactly
`h(W-1)!` permutations.  Only marked labels can be fixed; the union bound on
their fixed-point subfamilies yields the stated derangement lower bound.
Using `binom(2m-1,m-2)/W=(m-1)/(m+1)` gives the expectations.  This benchmark
is explicitly not transferred to the sparse Middle-Levels successor graph.

The two-hexagon obstruction uses `(m-2)`-cores meeting in `m-4` coordinates
and six fresh labels, so it fits in `2m-1` coordinates for `m>=7`.  Its
twelve-edge degree-two protected bank falls under the small extension theorem
for `m>=14`.  Cross-shore lower intersections have size `m-4`, whereas two
common-core ring roots intersect in `m-2`; hence no ring can hit both forced
cycle components.  This proves only that arbitrary factor-first placement
fails, not that a jointly chosen factor/ring is impossible.

## 6. Remaining assertion

The sole topology assertion left by this note is the rooted transparent-pull
cut family: every nonempty set of hinge-free factor components has a
protected-reservoir-transparent pull leaving it.  Protected Ore factor
extension does not prove this family: it controls incidence-graph cuts, not
the factor-component pull quotient.  The bridge example is correctly scoped
to the canonical static host and shows why a load bound without root
placement is insufficient.
