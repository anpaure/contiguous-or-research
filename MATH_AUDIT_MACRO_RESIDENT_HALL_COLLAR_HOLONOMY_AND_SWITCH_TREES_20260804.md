# Independent proof audit: macro-resident Hall, collar holonomy, and switch trees

**Date:** 2026-08-04  
**Audited file:**
`MATH_THEOREM_MACRO_RESIDENT_HALL_COLLAR_HOLONOMY_AND_SWITCH_TREES_20260804.md`

## 1. Macro-block off-by-one audit

A block with `ell` internal transition edges has its incoming and outgoing
connector edges separated by `ell+1` transition slots.  Therefore
`ell>=L-1` is exactly enough to ensure that two connector edges are never at
distance less than `L`.  Under this hypothesis, a short pair of transitions
is either internal to one block or crosses exactly one seam.  The local seam
word in Theorem 2.1 contains every such cross-seam pair.

The perfect-matching correspondence is exact: one connector leaves every
block and, because right endpoints are matched once, one enters every block.
The resulting permutation of vertex-disjoint paths is a spanning directed
cycle factor.  Conversely every such concatenation gives the matching.
Regular bipartite macro-incidence therefore proves the correct Hall row.

## 2. Dense corollary audit

The frozen corollary takes degrees after self-connectors are discarded.
This loopless convention is necessary: two isolated vertices carrying only
self-loops would otherwise satisfy the numerical degree row at `n=2` but
have no Hamilton two-cycle.

In the loopless seam digraph, minimum in- and out-degree at least `n/2`
forces strong connectivity.  A
source and a sink strongly connected component in a nontrivial condensation
would be disjoint and each have at least `n/2+1` vertices.  The total degree
of every vertex is at least `n`, so the Ghouila-Houri theorem applies and
gives a directed Hamilton cycle of blocks.  The macro theorem then gives one
resident owner cycle.

## 3. Balanced-collar phase audit

At each end, the ages are the permutation `1,...,L-1`.  Equal endpoint
support and old residence give `theta_initial(x)+theta_terminal(x)>=L` for
every supported direction.  The sum of the left sides is `L(L-1)`, equal to
the sum of the lower bounds, so every inequality is equality.  This proves
the complement law.

Across a seam, the inequalities

\[
       L-\theta_i(x)+\theta_j(\phi_{ij}(x))\ge L
\]

sum to equality for the same reason.  Hence all are equalities and the seam
transports the complete age phase.  Propagating a phase around a base cycle
returns consistently exactly when the transport product has a fixed point.
Under a coboundary representation `tau_ij=g_j g_i^{-1}`, every cyclic product
telescopes to the identity.  No unspoken commutativity is used.

## 4. Switch-tree audit

A two-edge directed switch between distinct directed cycles merges them.
For any processed proper subset of a tree's edges, the endpoints of an
unprocessed tree edge are in different components; otherwise the processed
edges already contain a tree path between them.  Thus `s-1` switches leave
one component.

The global-separation definition is stronger than pairwise disjointness and
is the needed one.  It ensures that a short final transition interval meets
at most one new seam.  Old residence or the corresponding local seam check
then handles every possible short repetition.  This proof would be false if
one assumed only that each switch was safe in isolation; the theorem does
not make that mistake.

## 5. Regularity obstruction audit

The two-owner multigraph has degree `a` on all four bipartite owner copies.
Every perfect matching projects to the same antiparallel pair.  The two
selected physical transition supports coincide, so the cyclic distance-one
constraint fails for `L>=2`.  Parallel edges correctly represent distinct
frame occurrences and do not change the physical support.

The example proves insufficiency of regularity as an abstract implication.
It is not asserted to be an induced subinstance of the complete
all-perfect-pairings host.

## 6. Scope verdict

**PASS.**  The note proves three exact, useful statements:

1. Hall is necessary and sufficient after residence is packaged into
   sufficiently long literal path blocks;
2. balanced critical collars carry a phase whose only global obstruction is
   cycle holonomy; and
3. a globally separated tree of safe switches Hamiltonizes a resident
   factor.

It correctly does **not** prove:

* that the all-perfect-pairings occurrence factor admits a resident block
  partition;
* regularity or even Hall for the literal macro connector graph;
* flat collar transport in the actual pair-cell host;
* a seam-free exact cover of the good cells; or
* any upper-palette, component-compiler, or lower-compiler statement.

The exact residence frontier is therefore a lifted one: construct macro
blocks and prove macro Hall plus collar holonomy, or construct a resident
factor and a separated complementary-age switch tree.
