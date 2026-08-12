# Exact double-matching path-cover criterion for GK root-circuit contraction

**Date:** 2026-08-07  
**Status:** unconditional min-cut and fusion reduction.  The required cut
inequalities for the specific GK root graph remain open.

## 1. Abstract bipartite factor

Let `G=(P,N;E)` be bipartite, with

\[
                         |P|=p,\qquad |N|=p+d.          \tag{1.1}
\]

We seek a simple edge set `H` satisfying

\[
                         d_H(u)=2\quad(u\in P),
 \qquad                 d_H(v)\le2\quad(v\in N).       \tag{1.2}
\]

Build the network with source-to-`P` capacity two, unit capacity on each
edge of `G`, and `N`-to-sink capacity two.

## Theorem 1.1 (exact double-Hall criterion)

A factor (1.2) exists if and only if, for every `S subset P`,

\[
 \boxed{
  \sum_{v\in N(S)}\min\{2,d_S(v)\}\ge2|S|.}           \tag{1.3}
\]

### Proof

The left side is the rank of all edges leaving `S` under the unit edge
capacities and the capacity-two constraints at `N`.  Necessity is
immediate.  Conversely, (1.3) is precisely the family of source-side
min-cut inequalities in the displayed integral network.  Max-flow/min-cut
gives a value-`2p` integral flow, whose unit `P-N` edges form `H`. \(\square\)

Since a bipartite graph of maximum degree two is 2-edge-colourable, `H`
is the union of two edge-disjoint matchings, each saturating `P`.

## 2. Exact component count

Every component of `H` is a path, an even cycle, or an isolated vertex of
`N`.  Let `c(H)` be its number of cycle components.  Delete one edge from
each cycle.  The result is a spanning linear forest `F` with

\[
 |E(F)|=2p-c(H).
\]

Since `|V(G)|=2p+d`, the number of path components, counting isolated
vertices as paths of length zero, is exactly

\[
 \boxed{\operatorname {pc}(F)=d+c(H).}                 \tag{2.1}
\]

Thus the shore imbalance is the exact unavoidable path-cover term; only
the cycle count is additional.

## 3. Application to the GK root graph

For odd semilength `m=2s+1`, let `P` be the smaller inversion-parity shore
of the root-rotation graph `R_m`, and `N` the larger shore.  Then

\[
                         d=\operatorname {Cat}_s.       \tag{3.1}
\]

If (1.3) holds in `R_m`, two smaller-shore-saturating matchings give a
spanning degree-two path/cycle cover.  Breaking its cycles gives exactly
`Cat_s+c(H)` root paths.  On every nontrivial root path, the path-fusion
theorem combines the edge `C_6` circuits into one incidence cycle.  Hence
the entire `Cat_m` singleton-root bank contracts to

\[
                         \operatorname {Cat}_s+c(H)     \tag{3.2}
\]

root blocks, with isolated roots retained as singleton sidecar blocks.

Because

\[
 \operatorname {Cat}_s
 =\operatorname {Cat}_{(m-1)/2}
 =\operatorname {Cat}_m^{1/2}\,m^{-3/4+o(1)},          \tag{3.3}
\]

this is a square-root-scale contraction if `c(H)=O(Cat_s)`.

## 4. The exact missing GK lemma

The sufficient graph statement is now:

> **GK double-Hall low-cycle lemma.**  For every odd `m=2s+1`, the smaller
> inversion shore of `R_m` satisfies (1.3), and one value-`2|P|` factor can
> be chosen with at most `O(Cat_s)` cycle components.

The first clause is an ordinary integral flow theorem once the inequalities
are proved.  The second is a correlated topology condition; it does not
follow from max flow alone.

For even `m`, the shores balance but the mountain has degree one, so (1.2)
cannot hold.  The correct even analogue must prescribe two or a bounded
number of degree-one endpoints and demand degree two elsewhere.  The same
network proof gives its exact lower-quota cut criterion after those
endpoints are fixed.

## 5. Scope of a recursive use

Equation (3.2) is a component contraction, not yet an additive-constant OR
construction.  To iterate it, every residual path block must export the
same protected colour/residence/compiler interface at the smaller
semilength.  If such regeneration holds and `c(H)=O(Cat_s)`, repeated
halving of semilength reaches a bounded terminal bank after `O(log m)`
zero-positional-charge stages.  No additive conclusion is claimed without
that regeneration theorem.
