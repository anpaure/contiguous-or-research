# Independent audit: rooted path-cover coefficient, ordered Hall, and pull parity

**Date:** 2026-08-04  
**Audited theorem:**
`MATH_THEOREM_ROOTED_PATH_COVER_COEFFICIENT_ORDERED_HALL_AND_PULL_PARITY_20260804.md`  
**Audited theorem SHA-256:**
`8b0f13778888218e1c35a2ff2d9f361690ea3174b960672cd06c960b3d0975db`  
**Method:** independent line-by-line pure-mathematical replay; no search,
solver, or finite computation  
**Verdict:** **INDEPENDENT-GO after one scope correction.**  The theorem is
proof-safe at its stated scope.  During the audit, the `C_8` “first local
actuator” sentence was restricted to the Middle-Levels girth/parity
boundary; without that restriction it is false for a general bipartite
host containing an alternating `C_4`.

## 1. Fixed-matching contraction

For the fixed perfect matching `M_0`, every disjoint second perfect
matching selects exactly one successor arc at every tail and exactly one at
every head.  It is therefore exactly a permutation cycle cover of `Q`.
Conversely, a cycle cover of the loopless successor graph selects a second
perfect matching disjoint from `M_0`.  The permutation cycles and the
components of `M_0 union M_1` agree, with each directed successor step
representing two bipartite factor edges.

Thus the hinge condition “every factor component meets `R`” is exactly the
rooted-cycle-cover condition used throughout the note.

## 2. Rooted path-cover bijection

Delete the outgoing arc of every root from a rooted cycle cover.  Tails of
the remaining arcs are exactly `L-R`, their heads remain distinct, and no
directed cycle survives because each old cycle was cut at at least one
root.  The unused heads are exactly `pi(R)`, and the deleted arcs are a
root-to-unused-head bijection.

Conversely, let `F` have one outgoing arc at every nonroot, no root tail,
distinct heads, and no directed cycle.  Its indegree and outdegree are at
most one.  In this degree class, an undirected cycle would necessarily be a
directed cycle, so `F` is an undirected forest with `N-|R|` edges and hence
`|R|` path components.  Only roots can be terminal vertices.  There are
exactly `|R|` roots, so every component ends at exactly one root.  Matching
all root tails onto the `|R|` unused heads restores indegree and outdegree
one everywhere, and every restored cycle contains a root-tail arc.

The two operations are inverse even when one original cycle contains more
than one root.  Theorem 1.1 is exact.

## 3. Ordered-Hall equivalence

Every acyclic `F` admits a total topological order in which each head
precedes its tail.  Its arcs are then a perfect matching

\[
        L-R\longrightarrow L-S,
        \qquad S=L\setminus h(F),
\]

inside the descending-arc graph.  The deleted root arcs give the independent
perfect matching `R -> S`.

In the reverse direction, strict descent makes the nonroot matching
acyclic.  Its tail set is `L-R` and head set is `L-S`, so it has exactly the
linear-forest data required by Theorem 1.1.  Both bipartite sides have the
same cardinality, hence Hall saturation is perfection.  Forced nonroot
arcs impose order inequalities and reserve their tails/heads; forced root
arcs reserve heads in `S`.  Repeated tails, repeated heads, or a forced
nonroot directed cycle are correctly immediate obstructions.

No hidden subtour condition remains after `S` and the order are fixed.

## 4. Directed matrix-tree orientation and coefficient

The row out-Laplacian in (3.1), with roots deleted, has the correct
orientation: its principal minor is the generating polynomial for spanning
directed forests in which every nonroot has one outgoing arc and every path
terminates in `R`.  For example, an arc directed from a nonroot toward a
root contributes to the diagonal minor, while the reverse root-tail arc
does not.  This agrees with the path orientation in Theorem 1.1.

An arc `x -> y` has weight `z_y`, so the exponent of `z_y` is the forest
indegree of `y`.  The directed matrix-tree forest expansion has coefficient
`+1` for each rooted forest.  Consequently, although the object is written
as a determinant, its relevant combinatorial expansion has nonnegative
integral coefficients and no cancellation.

The forest polynomial has degree `N-|R|` in the head variables and the root
closure polynomial has degree `|R|`.  Extracting
`prod_(v in L) z_v` therefore forces simultaneously:

1. every forest head has multiplicity at most one;
2. every closure head has multiplicity one within its injection;
3. the two head sets are disjoint; and
4. together they use all `N` heads.

Thus every contributing product is exactly one rooted linear forest and
its complementary root-closure matching.  The bijection of Theorem 1.1
shows that the coefficient counts rooted cycle covers once each.

The forced-edge operation is also exact.  Nonroot-tail variables occur
only in the forest factor and root-tail variables only in the closure
factor, and no selected arc is repeated inside either factor.  Hence the
product is multilinear in each arc variable; differentiating in a forced
arc variable selects precisely the monomials containing that occurrence.
Setting forbidden variables to zero and the remaining allowed variables to
one is therefore proof-safe.

## 5. Three-matroid formulation

An `N`-element common base of the tail and head partition matroids uses one
arc at every tail and one at every head, hence is exactly a cycle cover.
After root-tail arcs are deleted, indegree and outdegree are at most one.
In this degree class every underlying graphic circuit is a directed cycle;
an opposite pair is correctly represented as two parallel edges in the
underlying multigraph.  Independence in the rooted graphic direct sum is
therefore equivalent to every cycle of the cover meeting `R`.

The displayed augmentation witness is valid:

\[
 I=\{1\to2,2\to3\},\qquad
 J=\{4\to2,2\to5,1\to3\}.
\]

Both sets obey tail/head capacities and are forests, but each member of
`J-I` repeats a tail or head of `I`.  The common-independent family is not
itself a matroid.  This establishes only the failure of a direct one-matroid
shortcut, not the impossibility of a problem-specific lift, exactly as the
source states.

## 6. `C_6/C_8` parity

The head rotation sends `pi` to `sigma pi`, where `sigma` is one `t`-cycle.
Writing `sigma` as `t-1` transpositions gives

\[
 |c(\sigma\pi)-c(\pi)|\le t-1,
 \qquad
 c(\sigma\pi)-c(\pi)\equiv t-1\pmod 2,
\]

because a transposition changes permutation-cycle count by exactly one.
If the moved heads occupy distinct incumbent cycles, standard cycle
splicing merges those `t` cycles into one, attaining `-(t-1)`.

It follows that a fixed-coordinate `C_6` (`t=3`) cannot change two factor
components into one.  A `C_8` (`t=4`) is parity-compatible with a rank-one
change, and the displayed permutation multiplication verifies that abstract
incidence pattern.  The corrected source now states the necessary scope:
the Middle-Levels incidence graph has no `C_4`, so `C_8` is the first
circuit length not excluded by girth and parity there.  In an arbitrary
bipartite graph with a `C_4`, a `t=2` switch can already change the cycle
count by one.

If the coherent binary `C_6` pull preserved either perfect-matching
coordinate, all changed factor edges would lie in the complementary
coordinate and would be a fixed-coordinate `t=3` switch.  Its observed
`2 -> 1` component change contradicts the even-parity law.  The conclusion
that the coherent pull necessarily recolours both coordinates is valid.

## 7. Full-host common-core no-go

Theorem 6.1 is valid exactly for `Q^full`, before any additional protected
edge deletions.  If `Q^full[L-R]` were acyclic, choose a source `y`.  In the
residual bipartite graph obtained by deleting `R` and `M_0(R)`, every
nonmatching lower neighbour `x` of the matched owner `u_y` would give an
incoming successor arc `x -> y`.  Thus sourcehood would force `u_y` to have
only its matching neighbour and residual degree one.

Every root is `K+a` with `|K|=m-2`.  An upper `m`-set either omits part of
`K`, in which case it contains no root, or contains all of `K` and has only
two remaining positions, in which case it contains at most two roots.
Deleting `R` therefore removes at most two of the `m` lower facets of
`u_y`.  Its residual degree is at least `m-2>=2` for `m>=4`, contradiction.

Directed cycles in the residual successor graph are exactly alternating
cycles relative to the restricted `M_0`; hence the equivalent
nonuniqueness statement is correct.

This proof does **not** extend to a pruned successor host.  Additional
protected-edge deletion can reduce owner degree and can remove every
directed cycle.  The source preserves this distinction explicitly: the
result rules out only automatic acyclicity of the whole unpruned fibre and
does not rule out one correlated rooted second matching.

## 8. Final scope

The theorem proves three equivalent exact terminal formulations—rooted
path cover plus closure, ordered Hall, and positive coefficient—and one
exact three-matroid formulation.  It also proves the fixed-coordinate parity
boundary and the full-host common-core no-go.

It does not prove positivity for the current core-pinned reservoir, choose
the missing-head set/order, produce phase accessibility, preserve global
residence or arbitrary-width upper witnesses, or close the common cap.
The exact remaining fixed-host task is still a correlated selection of the
second matching.  **INDEPENDENT-GO at that scope.**
