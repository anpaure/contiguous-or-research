# Aligned double-C6 ears and the exact hook-matching reduction

**Date:** 2026-08-05  
**Method:** cut-path permutation calculus; no search  
**Status:** unconditional as a topology theorem.  Its hook consequence is
conditional on both explicitly stated premises: a near-perfect sibling
matching and global separation of every selected constant q2 halo (with
named-spine ports reserved).  It claims neither premise and no post-q2
compiler gate.

## 1. The aligned double-ear lemma

Let a directed two-factor contain three distinct cycles

\[
                         C_0,C_1,C_2.
\]

For each `i` choose two directed edges `A_i,B_i` on `C_i`, with all six
supports disjoint.  At both triples perform the same clean cyclic
reconnection

\[
 \operatorname{tail}(A_i)\longmapsto\operatorname{head}(A_{i+1}),
 \qquad
 \operatorname{tail}(B_i)\longmapsto\operatorname{head}(B_{i+1}),
 \tag{1.1}
\]

where indices are modulo three.

### Theorem 1.1 (aligned double ear)

After the two reconnections, the union of `C_0,C_1,C_2` is one directed
cycle.

#### Proof

Cut `A_i` and `B_i`.  Let `X_i` be the directed path from
`head(A_i)` to `tail(B_i)`, and let `Y_i` be the complementary directed
path from `head(B_i)` to `tail(A_i)`.

Starting at `head(A_i)`, the new successor structure follows

\[
 X_i,quad
 \operatorname{tail}(B_i)\to\operatorname{head}(B_{i+1}),
 \quad Y_{i+1},quad
 \operatorname{tail}(A_{i+1})\to\operatorname{head}(A_{i+2}).
 \tag{1.2}
\]

Thus one passage through an `X`-path and a `Y`-path advances the index by
two modulo three.  Since two generates `Z_3`, the resulting orbit visits

\[
 X_0,X_1,X_2,Y_0,Y_1,Y_2
\]

exactly once.  These six paths partition the three old cycles, so the new
factor has exactly one cycle.  `square`

The same proof works with the inverse cyclic reconnection at both triples.
Using opposite orientations at the two triples would instead close three
separate path pairs; the word *aligned* means that the orientations agree.

### Corollary 1.2 (palette-transparent double ear)

If both triples are selected common-pivot clean C6 moves with disjoint
q2 halos, then the double ear:

1. merges the three cycles to one;
2. preserves the selected q1 multiset exactly;
3. preserves every immediate upper colour edgewise;
4. preserves the selected q2 multiset exactly.

This follows by Theorem 1.1 and by composing the two disjoint local
q1/q2 identities.

## 2. Loose hyperstars need no parent-degree bound

Let `z` be one factor cycle, and let

\[
                         \{u_j,v_j\},\qquad j\in J,
\]

be pairwise disjoint pairs of other factor cycles.  Suppose for every `j`
there are two disjoint aligned common-pivot C6 lifts on the component
triple

\[
                         \{z,u_j,v_j\}.
\]

### Theorem 2.1 (double-ear hyperstar)

All cycles `z,u_j,v_j` can be merged to one while preserving q1 and q2
exactly.

#### Proof

Order `J` arbitrarily.  Before the first double ear, its three component
cycles are distinct, so Corollary 1.2 merges them.  Inductively, the
already processed material is one cycle containing `z`, whereas `u_j`
and `v_j` are two fresh cycles because the child pairs are disjoint.
Corollary 1.2 again applies to these three distinct cycles.  `square`

In particular, an arbitrarily large number of ears may share the parent
component `z`.  What must be bounded and made disjoint are the *marked
physical ports and their constant halos*, not the degree of the unmarked
parent component.

## 3. Exact hook-angle incidence

For the hook action `(h,1^b)`, put

\[
                         q=2h-1.
\]

Its action-angle tori are cyclic weak-composition necklaces

\[
 \mathcal N_{q,b}
 =\{(x_0,\ldots,x_{q-1})\in\mathbb Z_{\ge0}^q:\sum x_i=b\}/C_q.
 \tag{3.1}
\]

Let `y` have mass `b-1`.  Root it at the cut between slots `j` and
`j+1`.  The leaf-plucking C6 has component triple

\[
 \boxed{
 \bigl\{[y+e_j],\ [y+e_{j+1}],\ [\iota_j(y)]\bigr\},
 }
 \tag{3.2}
\]

where the promoted parent angle satisfies

\[
          1D_h(y)0=D_{h+1}(0,y,0).
 \tag{3.3}
\]

Equivalently, `iota_j` inserts a marked consecutive `00` slot-pair at the
chosen cut.  Deleting that marked pair recovers `(y,j)`.  Hence different
angle edges have different **marked parent ports**, even when forgetting
the mark identifies their promoted parent tori.

The literal leaf-plucking theorem proves that (3.2) is a selected
q1/q2-neutral clean C6.  Its rotation theorem gives two vertex-disjoint
six-owner lifts on the same component triple for all `m>=18`.  Give both
lifts the canonical orientation.  They therefore form an aligned
**topological** double ear.  Exact composition of their q2 identities also
requires their companion halos to be disjoint; this is part of hypothesis
4.1(2), not a consequence of the six-owner rotation count.

## 4. Reduction to a sibling matching

Let `G_(q,b)` be the graph on `N_(q,b)` in which

\[
                    [y+e_j]\sim[y+e_{j+1}].
 \tag{4.1}
\]

For each action profile `(h,1^b)`, choose a matching `M_(h,b)` in this
graph.  Attach to every matched edge its marked promoted parent from
(3.2).

### Theorem 4.1 (hook matching reduction)

Assume the following two statements.

1. For every `(h,b)` in the hook range, `M_(h,b)` covers every hook torus
   except at most one named torus `H_(h,b)`.
2. The two lifts of every matched edge can be chosen so that all six-owner
   supports and their constant q2 halos are globally disjoint, except for
   sharing the intended *component vertex*.  In particular, marked parent
   ports are distinct on a repeated parent torus, and ports used when the
   same torus appears at the adjacent hook level or on the named spine are
   also reserved separately.

Then all unnamed hook tori can be absorbed into their promoted parents by
q1/q2-exact double ears.  The resulting connector hypergraph is a union of
loose hyperstars: distinct ears incident with one promoted parent intersect
only in that unmarked parent vertex.  If the named tori and the promoted
parent roots are joined by the already-proved one-or-two-rail named hook
spine, the complete hook sector has only the spine's bounded component
defect.

#### Proof

The child pairs of a matching are disjoint.  Group matched edges by their
unmarked promoted parent torus.  Within each group, Theorem 2.1 merges the
parent and every paired child into one cycle.  Marked-port injectivity and
hypothesis 2 make all local identities simultaneously literal.  Different
groups share no child torus.

Order hook levels by increasing `b`, **before** installing the named
spine.  Every promoted parent of level `b` lies at level `b-1`, so it is
already contained in a unique one-cycle block rooted at one of the named
lower-level tori.  Each matched level-`b` child pair is fresh.  Its aligned
double ear therefore acts on that parent block and two fresh cycles, and
Theorem 1.1 leaves one cycle again.  Induction over `b` produces one
one-cycle descendant block for each unmatched named root.  Finally apply
the proved named-spine construction to those named roots; it leaves one or
two rails.  The only uncovered child in each profile is thus precisely the
interface retained for the named spine.  `square`

This theorem explains why the large parent degree forced already at
`b=2` is harmless.  There the unique one-chip promoted parent supports a
linear child graph; alternating marked ports give the required hyperstar.

## 5. Exact remaining hook theorem

After the all-angle leaf-plucking and double-ear results, the unresolved
hook topology is the following purely finite-family statement.

> **Near-perfect cyclic-composition matching.**  For odd `q=2h-1`, the
> adjacent-unit-transfer graph `G_(q,b)` has a matching covering every
> cyclic weak composition of mass `b` except at most one prescribed named
> necklace; furthermore its matched edges admit mutually halo-disjoint
> marked `00` parent ports.

For `b=1` there is one named vertex and nothing to match.  For `b=2`, the
child graph is the path on cyclic two-chip distances and alternating edges
give the optimum matching.  The statement for general `b` is not proved
here.

## 6. Scope

Proved:

1. two aligned clean C6 copies on three cycles are a one-cycle ear;
2. an arbitrary loose hyperstar of such double ears is one-cycle and
   q1/q2 exact;
3. the hook packing problem reduces exactly to near-perfect matchings in
   `G_(2h-1,b)` plus marked-port halo separation.

Not proved:

1. the general near-perfect matching;
2. the simultaneous halo-separation estimate;
3. non-hook angle packing;
4. q3, residence, arbitrary upper witnesses, or common-cap regeneration;
5. `nu(k)<=B(k)+O(1)`.
