# The canonical closing-step GK hinge subfamily has no full private or cycle-cover bank

**Date:** 2026-08-07  
**Status:** unconditional obstruction for the four-record subfamily with
the first upstep distinguished and `x` equal to the closing downstep of
`b`.  It does **not** obstruct the full GK catalogue, which permits every
downstep inside the `b`-subtree.

## 1. Edge form of every canonical closing-step root hinge

Use the root-rotation edge

\[
 L=1A1B0C0D,
 \qquad
 R=1A0B1C0D                                      \tag{1.1}
\]

with common rank-`(m-2)` word `a` and displayed record positions
`alpha<beta<gamma<delta`.  Put

\[
 X_L=a+\beta,qquad X_R=a+\gamma,qquad Z_e=a+\delta.
\]

The explicit GK-compatible hinge at `L` claims the two rank-`(m-1)`
resources

\[
                         \{X_R,Z_e\},                 \tag{1.2}
\]

whereas the hinge at `R` claims

\[
                         \{X_L,Z_e\}.                 \tag{1.3}
\]

Thus every root hinge claims the fixed root facet of its opposite endpoint.

## Corollary 1.1 (strict privacy no-go)

No hinge from this canonical closing-step family is disjoint from the
full fixed facet bank

\[
                         \mathcal X=\{X_U:U\in D_m\}.
\]

In particular, the strict private-bank conditions (4.1)--(4.3) in the
singleton-root hinge theorem have no solution inside this subfamily.

This is not an accidental collision: the two endpoint hinges on one edge
combine into the exact alternating `C_6` proved in the root-rotation note.

## 2. Controlled overlap is an oriented cycle cover

Relax strict privacy by allowing the intended claims of the fixed `X`
bank.  Choose one incident root-rotation edge for every root and orient it
away from that root.  Require:

1. all claimed opposite-root facets are distinct;
2. all auxiliary resources `Z_e` are distinct;
3. all intersection colours `a_e` are distinct.

The maps `e -> a_e` and `e -> Z_e` are injective.  Hence conditions 2--3
say exactly that no underlying edge is selected in both orientations.
Condition 1 says that every root has indegree at most one.  Since every root
has outdegree exactly one, the selected arcs form a vertex-disjoint union of
directed cycles, each of length at least four.

Conversely, every such oriented cycle cover satisfies the three resource
conditions.  We have therefore proved:

## Theorem 2.1 (cycle-cover equivalence)

The controlled-overlap three-resource transversal for the canonical
closing-step hinge
family exists if and only if `R_m` has a spanning oriented cycle cover with
no directed two-cycle.  Equivalently, because `R_m` is bipartite, it exists
if and only if `R_m` has a spanning 2-factor.

## 3. The mountain obstruction

Let

\[
                              M_m=1^m0^m.
\]

Its first primitive component is the whole word.  Relative to the fixed
first upstep, the only eligible second opener in (1.1) is the second bit:
the plane tree is a chain, so the outer root has one child and there is no
later top-level component.  Therefore

\[
                              \deg_{R_m}(M_m)=1.        \tag{3.1}
\]

A graph with a degree-one vertex has no spanning 2-factor.  Combining
(3.1) with Theorem 2.1 gives:

## Corollary 3.1 (all-`m` fixed-root no-go)

For every `m>=2`, the canonical fixed-first-upstep, closing-step GK
subfamily has neither a strict private bank nor a controlled-overlap
oriented cycle-cover bank covering all Dyck roots.

For odd `m=2s+1` there is the additional global obstruction that the two
inversion-parity shores differ by `Cat_s`; the mountain obstruction shows
that balancing the shores at even `m` is still not sufficient.

## 4. Exact escape routes

Any successful SCD-based root construction must use at least one of:

1. the full fixed-upstep catalogue, using nonclosing downsteps `x` inside
   the `b`-subtree;
2. a second distinguished-upstep phase, giving the mountain and the parity
   surplus further neighbours;
3. higher incidence circuits whose overlap is not encoded by a 2-factor of
   `R_m`;
4. a different first perfect matching or omission basis.

Thus the canonical closing-step family remains a useful local `C_6`
supply, but it cannot by itself be the all-root integral selector.
