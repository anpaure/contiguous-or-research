# Self-audit: rooted path-cover coefficient, ordered Hall, and pull parity

**Date:** 2026-08-04  
**Audited file:**
`MATH_THEOREM_ROOTED_PATH_COVER_COEFFICIENT_ORDERED_HALL_AND_PULL_PARITY_20260804.md`  
**Method:** line-by-line mathematical audit; no computation, search, or solver  
**Verdict:** **SELF-GO**, with the full-versus-pruned successor distinction in
Theorem 6.1 retained exactly as written.

## 1. Rooted path-cover bijection

Deleting the outgoing arc at every root from a permutation cycle which
meets the roots cuts that cycle into directed paths.  The surviving tails
are exactly the nonroots, their heads remain distinct, and their unused
heads are exactly the images of the roots.  Conversely, an acyclic selected
arc set with one outgoing arc at every nonroot and distinct heads has
`N-|R|` edges.  Hence it has `|R|` path components; only roots can be sinks,
so each component ends at exactly one root.  A root-to-unused-head matching
restores indegree and outdegree one everywhere.  Every restored cycle uses
a root-tail arc.  The correspondence is therefore bijective, including
cycles containing more than one root.

## 2. Ordered Hall

Every directed forest admits a total topological order with `head < tail`
on each arc.  Conversely, a matching consisting only of strictly decreasing
arcs is acyclic.  The two bipartite sides in the residual matching have the
same cardinality `N-|R|`, and the closure sides have cardinality `|R|`, so
ordinary Hall saturation is perfection in both cases.  Forced nonroot arcs
correctly impose order relations; forced root arcs correctly reserve their
heads in the missing-head set.  No claim is made that one common order is
already supplied by the current Middle-Levels factor.

## 3. Matrix-tree coefficient

The out-Laplacian principal minor is the directed rooted-forest polynomial:
every nonroot has exactly one outgoing arc and every component is directed
toward one deleted root.  Weighting an arc `x->y` by `z_y` records head
multiplicity.  The full squarefree coefficient in the product with the
root matching polynomial forces:

1. no repeated forest head;
2. no head shared by forest and closure matching;
3. every head used exactly once.

The total degrees are `N-|R|` and `|R|`, so there is no missing degree case.
The directed matrix-tree expansion has nonnegative coefficients; the
determinant notation introduces no cancellation into the combinatorial
coefficient.  Tail classes separate the forest and closure arc variables,
so the forced-edge differentiation statement is multilinear and exact.

## 4. Three matroids and the exchange warning

A common base of the two partition matroids is exactly a directed cycle
cover.  Removing root-tail arcs leaves indegree and outdegree at most one.
In that class, an underlying graphic circuit is necessarily a directed
cycle; opposite directed arcs are correctly parallel in the graphic
multigraph.  Thus rooted graphic independence is exact.

The displayed sets

\[
 I=\{1\to2,2\to3\},\qquad
 J=\{4\to2,2\to5,1\to3\}
\]

are both tail/head matchings and forests, while each member of `J-I`
violates a tail or head capacity when added to `I`.  This proves only that
the natural common-independent family is not a matroid.  The theorem
correctly does not claim impossibility of every lifted representation.

## 5. Alternating-circuit parity

Rotating `t` selected heads is left multiplication by one `t`-cycle.  A
`t`-cycle is a product of `t-1` transpositions, each of which changes the
cycle count by `+1` or `-1`; hence both the bound and parity are exact.
Points in distinct incumbent cycles are spliced into one cycle.  Therefore
a second-matching `C_6` has even component-rank change and cannot perform a
binary merger, whereas a `C_8` can have rank one at permutation level.  It
is the first circuit length not ruled out by girth and parity in the
Middle-Levels incidence graph because that graph has no `C_4`; this
firstness is not asserted for a general bipartite host.  The explicit
`(1 2)(3 4)` example verifies existence of the latter incidence pattern.

If the old and new coherent-hex factors shared one perfect-matching
coordinate, all six changed edges would lie in the complementary matching,
contradicting the odd `2 -> 1` component change.  The recolouring conclusion
is therefore valid.

## 6. Common-core acyclicity no-go

The theorem uses the **full** successor digraph.  If its nonroot induced
subgraph were acyclic, a source `y` would make the matched upper vertex
`u_y` degree one after deleting the root pairs.  A common-core root family
has the form `K+a` with `|K|=m-2`; any upper `m`-set contains at most two of
these roots.  Its residual degree is consequently at least `m-2>=2` for
`m>=4`, contradiction.

This does not survive arbitrary additional forbidden-edge deletion and is
not presented as doing so.  It rules out only the shortcut in which the
root geometry alone makes the whole unpruned matching fibre safe.  It does
not obstruct a specially selected rooted second matching.

## 7. Scope verdict

The note proves an exact terminal formulation and two structural boundaries:

* topology after fixing one matching is a rooted linear-path-cover plus
  closure problem, equivalently the positive coefficient or ordered Hall;
* a one-coordinate `C_6` cannot be the binary pull used by the coherent
  construction, and the whole successor host cannot be made root-acyclic by
  the common-core ring alone.

It does not prove the positive coefficient for the core-pinned protected
reservoir, phase accessibility in the canonical pull orbit, global
residence, upper completeness, or the common cap.  **SELF-GO within this
scope.**
