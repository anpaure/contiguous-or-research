# Independent audit: common-core rooted pull transversal and fixed-matching obstruction

**Date:** 2026-08-04  
**Verdict:** **GO**, with the hypergraph theorem read in its explicitly
stated tree-compatible sense.  No computation, search, or solver output is
used.

Audited theorem:
`MATH_THEOREM_COMMON_CORE_ROOTED_PULL_TRANSVERSAL_AND_FIXED_MATCHING_OBSTRUCTION_20260804.md`,
SHA-256
`5cc02e3ce3fd07a2fd3d7656893a72ef4c4395076dafc19c0769c6834b30668a`.

Author self-audit:
`MATH_AUDIT_COMMON_CORE_ROOTED_PULL_TRANSVERSAL_AND_FIXED_MATCHING_OBSTRUCTION_SELF_20260804.md`,
SHA-256
`f7b6290a236b7df414aa41386d2a9835255bd0253c9157c003f6c0ac1898dabe`.

## 1. Rooted pull closure

The identity

\[
 c_S(F_T)=q_0(F,S,H_D)
\]

is exact in the declared fixed-host scope.  A spanning forest of each
transparent-host component contracts exactly the old factor components in
that host component.  Since every switched circuit avoids the complete
protected bank, its resulting factor component contains an `S` occurrence
if and only if one of its constituent old components did.  Distinct host
components cannot be joined by any switch from the fixed host.  Therefore a
rootless host component is also a genuine converse obstruction, not merely
an obstruction to the displayed maximal-forest construction.

Deleting `S` from a two-factor leaves one cyclic component for every factor
cycle disjoint from `S` and only paths from every factor cycle meeting `S`.
Thus the use of the forest-complement/cycle-transversal identity is exact.

The root-free cut criterion is equivalent to absence of a rootless host
component.  The augmented-root rank formula follows from the fact that all
rooted host components and `omega` form one component, while every rootless
host component remains separate.  The protected-cut identity subtracts
exactly the forbidden host edges; the per-occurrence expression is correctly
used only as a union-bound sufficient condition.

Two-sided shielding is valid: every proper component created by deleting
host edges has a deleted boundary edge, whose endpoint inside the component
is a root.  The exceptional case in which no deleted edge leaves a final
component means that it is the whole background host component, so it
contains its background-stage selected root.  This also supplies the precise
justification for the two-stage statement.  The numerical root-capacity
bound and the conditional Hall placement row are correct; the latter is
properly scoped to occurrence choices having no additional cross-role
conflicts.

## 2. Hypergraph/Berge statement

Theorem 2.1 is valid with the meanings already stated in the theorem:

1. every Berge-tree component is based at an old factor component containing
   an `S` occurrence;
2. every new circuit meets the previously absorbed part in exactly one
   current factor component and introduces at least one new component; and
3. the selected circuit family is dynamically tree-compatible, so its
   circuits remain applicable in the chosen order and perform contraction,
   not a split, after earlier contractions.

Under these hypotheses, induction on the rooted incidence tree is exact.
The bare existence of a connected circuit-support hypergraph would not be
enough, and the theorem expressly does not make that promotion.  Thus no
correction is needed, but future citations should retain the words
"rooted" and "tree-compatible"; a Berge-cover condition alone is not the
proved statement.

## 3. Fixed-perfect-matching normal form

Every bipartite two-factor decomposes into two disjoint perfect matchings.
After fixing `M_0`, the second matching defines the permutation

\[
 \pi(x)=\mu_0(M_1(x)),
\]

and one factor circuit is exactly one cycle of `pi`, with each successor arc
subdivided by its upper endpoint.  The exact root-support assumptions on `S`
ensure that deleting `S` breaks precisely the cycles meeting `R`.

The graphic reformulation is also exact.  On nonroots, selected successor
arcs have indegree and outdegree at most one.  Hence an undirected graphic
circuit is a directed permutation cycle; a directed two-cycle is correctly
interpreted as two parallel edges in the underlying multigraph.  Loops do
not arise because successor edges belonging to `M_0` were removed.

Swapping two selected heads composes the permutation on the left by their
transposition.  The standard merge/split rule therefore proves Corollary
3.2.  The analogous longer alternating circuit changes the permutation by a
cycle on the affected heads, so its component effect genuinely depends on
the incumbent cycle incidence.

## 4. Hamiltonicity obstruction

The construction from a loopless digraph `Q` is faithful.  The identity
matching supplies `M_0`, every arc `x -> y` supplies the edge `x u_y`, and a
disjoint second perfect matching is exactly a directed cycle cover of `Q`.
With one root, requiring every cycle to meet that root forces the cover to
have one cycle, i.e. to be Hamiltonian.  A digraph consisting, for example,
of two disjoint directed cycles shows directly that ordinary factor
extendability can hold while rooted completion fails.  No complexity
assumption is needed.

## 5. Common-core ring criterion

The panchromatic-core criterion is exact.  Necessity follows because the
`m` ring roots can hit at most `m` components and their common `(m-2)`-core
lies in every hit component's lower shadow.  Conversely, choose one
extension of a common core in each component.  Extensions chosen in distinct
components have distinct external labels, because otherwise they would be
the same lower vertex.  With at most `m` chosen labels among the `m+1`
labels outside the core, one unused label can be omitted and the resulting
punctured star contains all representatives.

The shadow-expansion corollary is the direct strict union bound on the events
that a uniformly chosen core misses a component.

## 6. Uniform-permutation and derangement counts

For a fixed marked set of size `h`, deletion of all unmarked labels from a
cycle-hit permutation leaves an arbitrary permutation of the marked labels.
Reinsertion as `h` ordered possibly empty lists gives

\[
 h!\,(W-h)!{W-1\choose h-1}=h(W-1)!,
\]

so the exact probability is `h/W`.

In a cycle-hit permutation, only a marked label can be fixed.  Fixing one
marked label leaves `(h-1)(W-2)!` cycle-hit permutations, so the stated union
bound leaves `h(W-h)(W-2)!` derangements.  Division by `!W <= W!` yields the
claimed lower bound.  Finally,

\[
 {\binom{2m-1}{m-2}\over \binom{2m-1}{m-1}}
 ={m-1\over m+1},
\]

which gives both expectations.  The theorem correctly presents this only as
a dense benchmark, not as a distributional theorem for the sparse protected
Middle-Levels successor graph.

## 7. Two-hexagon Middle-Levels obstruction

Let `H_0,H_1` be `(m-2)`-cores meeting in `m-4` coordinates.  Their union has
size `m`; two disjoint fresh triples therefore fit in the `2m-1` coordinate
set for `m >= 7`.  The two corresponding incidence hexagons are
vertex-disjoint, have twelve total edges, and their union has maximum degree
two.  For `m >= 14`, the repository's small protected-factor theorem applies
because `12 <= m-2`.  It does not require the protected bank to be acyclic.
All vertices on either prescribed hexagon are already saturated, so each
hexagon remains a separate component of every extending two-factor.

Every lower vertex on different prescribed hexagons intersects in exactly
`m-4` coordinates.  Two distinct roots in a common-core ring intersect in
their common `(m-2)`-core and are therefore Johnson adjacent.  Hence one ring
cannot place roots in both distinguished components.  This proves exactly
the claimed factor-first obstruction and no stronger joint-selection
impossibility.

## 8. Final scope verdict

The theorem is proof-safe as written.  It closes the topology row only
conditionally on a rooted transparent pull host (or a fixed matching with a
rooted cycle cover).  It does not derive that host from protected Ore
extension, does not show that the current cyclic ring's fixed head shift is
one cycle after arbitrary placement, and does not close the common cap.

The independent verdict is therefore **GO** for the theorem at the hashes
listed above.
