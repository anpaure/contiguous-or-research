# Why a two-sided SCD path forest does not yield an MTF tour

This note audits a tempting global route for the universal contiguous-OR
problem.  In dimension `2m`, an SCD gives one Johnson edge for every
non-singleton chain; the edges have all rank-`(m-1)` intersections and all
rank-`(m+1)` unions exactly once.  It is natural to try to choose the SCD so
that these edges form only `Cat_m` paths and then traverse each path by
move-to-front (MTF) updates.

The first part of that proposal remains an interesting pure design question.
The second part is impossible for a reason that applies to **every** SCD (and,
in fact, to every disjoint saturated chain cover with the same central
diamonds).  An edge of the central projection is almost never a one-step MTF
transition between the two chains at its ends.  Only an edge entering a
singleton middle chain, or one involving the unique chain with empty minimum,
can escape the obstruction.

Throughout,

\[
 W=\binom{2m}{m},\qquad
 C=\binom{2m}{m-1},\qquad
 K=W-C=\operatorname{Cat}_m=\frac{W}{m+1}.
\tag{0.1}
\]

## 1. Theorem ledger

### Inherited and proved

1. A saturated chain
   \[
   B\subset B+e_1\subset\cdots\subset B+e_1+\cdots+e_h
   \]
   is exposed by an ordered-partition state exactly when that state consists
   of a partition of `B`, followed by the singleton blocks
   `e_1,...,e_h`, followed by an arbitrary partition of the complement of the
   chain top.
2. For a target chain `D` with nonempty minimum `A`, there is a one-step MTF
   transition from some state exposing `C` to some state exposing `D` if and
   only if `C-A` and `D-A` are cross-nested.  That is, every member of one
   quotient chain is comparable with every member of the other.
3. Every SCD of `B_(2m)` induces `C` Johnson edges on the middle layer.  Their
   meets are all `(m-1)`-sets once and their joins are all `(m+1)`-sets once.
   Each non-singleton chain owns one edge; the `K` singleton middle chains own
   none.

### New and proved here

1. **Central-square transition barrier.**  Let a chain `C` own the central
   diamond
   \[
       S\subset T=S+a\subset U=S+a+b,
   \]
   and let the alternate middle set `T'=S+b` lie in a disjoint saturated
   chain `D`.

   * The reverse transition `D -> C` is impossible whenever the minimum of
     `C` is nonempty.
   * The forward transition `C -> D` is impossible whenever the minimum of
     `D` is nonempty and `D` has a successor above `T'`.

2. In an SCD, the only targets not covered by the forward statement are the
   `K` singleton middle chains and the unique chain whose minimum is empty.
   The reverse statement has only the latter exception.
3. Consequently, in **any** vertex-disjoint directed path system made from
   central-projection edges, at most `K+1` edges can also be one-step MTF
   transitions (allowing either direction on each path).
4. Even if an SCD with a central projection that is a linear forest with
   exactly `K` components exists, at least
   \[
                        W-2K-1
   \tag{0.2}
   \]
   of its `C=W-K` internal path adjacencies are not one-step MTF transitions.
   Thus the forest cannot be turned into an MTF tour by only `O(K)` seam
   repairs.  It requires `Theta(W)` genuinely new state-aware adjacencies.

### Still open

1. Whether some SCD has an induced two-sided rainbow linear forest with
   exactly `K` components.
2. Whether an unrelated, state-aware selection of cross-chain MTF arcs gives
   an `o(W)`-component transversal path cover.
3. Whether a two-sided rainbow path factor can be extended through deeper
   shadows by a method not based on exposing its owner chains consecutively.

The new theorem does not lower the global upper bound on `nu(2m)`.  It rules
out one proposed way of obtaining `nu(2m)=(1+o(1))W`.

## 2. The central-square transition barrier

The statement is slightly more general than an SCD statement.

### Theorem 1

Let `C,D` be two disjoint saturated chains in `B_(2m)`.  Suppose `C` contains

\[
 S\subset T=S\cup\{a\}\subset U=S\cup\{a,b\},
 \qquad |S|=m-1,
\tag{2.1}
\]

and `D` contains the alternate middle set

\[
                         T'=S\cup\{b\}.
\tag{2.2}
\]

Then the following hold.

1. If the minimum `B` of `C` is nonempty, there is no one-step MTF transition
   from any state exposing `D` to any state exposing `C`.
2. Suppose the minimum `A` of `D` is nonempty and `D` contains a cover
   `V` of `T'`, so `T' subset V` and `|V|=m+1`.  Then there is no one-step MTF
   transition from any state exposing `C` to any state exposing `D`.

#### Proof of the reverse direction

Since `B` is the minimum of `C` and `S` is a member of `C`,

\[
                              B\subseteq S.
\tag{2.3}
\]

If `D -> C` were a one-step MTF transition, the quotient-chain criterion for
the nonempty target minimum `B` would make `D-B` and `C-B` cross-nested.
In particular, their respective members

\[
 T'-B=(S-B)+b,
 \qquad
 T-B=(S-B)+a
\tag{2.4}
\]

would have to be comparable.  They are distinct sets of the same size, hence
are incomparable.  This is a contradiction.

#### Proof of the forward direction

Assume that `C -> D` is possible.  Since the target minimum `A` is nonempty,
the quotient chains `C-A` and `D-A` must be cross-nested.

First, `A subseteq T'`.  If `b notin A`, then `A subseteq S` (the only element
of `T'` outside `S` is `b`).  The two quotient sets

\[
                         T-A,
                         \quad T'-A
\tag{2.5}
\]

would then be distinct and have the same size, contradicting cross-nesting.
Therefore

\[
                         b\in A.
\tag{2.6}
\]

Write `A=A_0+b`, where `A_0 subseteq S`.  Now

\[
 T'-A=S-A_0,
 \qquad
 T-A=(S-A_0)+a.
\tag{2.7}
\]

Thus `T-A` is the unique member of the common quotient chain one rank above
`T'-A`.  But `V` covers `T'`, so `V-A` is also one rank above `T'-A` in the
same common quotient chain.  A chain contains at most one set at a fixed
rank, hence

\[
                           V-A=T-A.
\tag{2.8}
\]

Adding `A` back and using (2.6) gives

\[
                           V=T\cup\{b\}=U.
\tag{2.9}
\]

This is impossible because `U` is a member of `C`, `V` is a member of `D`,
and the two chains are disjoint.  This proves the theorem.  `square`

### Remarks on the hypotheses

* No Greene--Kleitman rule, complement symmetry, or particular SCD is used.
* The proof is existential over the **entire state fibers** of both chains.
  Splitting either minimum into many recency blocks does not evade it.
* Saturation above `T'` is used only to know that `V-A` is exactly one rank
  above `T'-A`.
* The empty-minimum exception is real at the level of the quotient theorem:
  a target with empty minimum has a special forced singleton anchor.  There
  is only one such chain in a chain partition, so this exception is globally
  negligible.

## 3. Consequence for every SCD

Fix an arbitrary SCD `mathcal D` of `B_(2m)`.  Every non-singleton chain `C`
has a central segment (2.1), and owns the Johnson edge

\[
                              e_C=TT'.
\tag{3.1}
\]

The middle set `T'` belongs to a unique chain, denoted `h(C)`.  Orient `e_C`
from the middle member of `C` to the middle member of `h(C)`.

There are exactly `K` singleton chains and exactly one chain `L` whose
minimum is empty.  If `h(C)` is neither singleton nor `L`, it has a successor
above its middle set.  Theorem 1 therefore says

\[
 C\longrightarrow h(C)
 \quad\hbox{is not an MTF arc}.
\tag{3.2}
\]

The reverse use of the same edge is impossible unless `C=L`:

\[
 h(C)\longrightarrow C
 \quad\hbox{is not an MTF arc whenever }C\ne L.
\tag{3.3}
\]

### Corollary 2 (at most `K+1` usable projection edges)

Let `mathcal P` be any vertex-disjoint path system on the SCD chains using
only edges `e_C`.  Orient each path in either of its two traversal
directions.  At most `K+1` traversed edges are one-step MTF transitions.

#### Proof

A forward projection arc can only enter one of the `K` singleton chains or
the exceptional chain `L`.  A reverse projection arc can only be the edge
owned by `L`, and when traversed in reverse it also enters `L`.  Thus every
potentially compatible traversed edge has one of these `K+1` exceptional
heads.  Vertex disjointness allows at most one incoming path edge at each
head, proving the bound.  `square`

The harmless `+2` is kept to avoid case distinctions when the edge owned by
`L` also enters an exceptional head.

## 4. The hypothetical linear-forest case

Suppose the induced graph is a linear forest.  It has `W` vertices and
`C=W-K` edges, hence exactly `K` path components.  Its functional orientation
has outdegree one at every non-singleton chain and outdegree zero at every
singleton chain, so every directed component ends at a singleton chain.

There are `C` internal path edges.  By Corollary 2 at least

\[
 C-(K+1)=W-2K-1
\tag{4.1}
\]

of them fail the one-step MTF test, no matter which direction is chosen for
each component.  Since

\[
 K=\frac{W}{m+1},
\tag{4.2}
\]

the failed fraction tends to one:

\[
 \frac{W-2K-1}{C}=1-O(1/m).
\tag{4.3}
\]

In the natural functional direction (toward the singleton root), the picture
is even simpler: apart from a possible edge entering `L`, only the final edge
of each nontrivial path can work.  That final edge really is pairwise
compatible, because a singleton target with minimum `T'` is exposed by the
canonical update `T'`; there is no successor whose presence could force the
collision (2.9).  The obstruction is therefore exactly an **internal-path**
obstruction, not an artifact of an overly strong necessary test.

For `2m=14`, for example,

\[
 W=3432,\quad C=3003,\quad K=429,
\]

so at least

\[
                         3432-858-1=2573
\]

of the `3003` forest adjacencies are MTF-incompatible.

This is stronger than the earlier audit of the Greene--Kleitman forest.  The
Greene--Kleitman audit showed that its particular projection branches too
much.  Theorem 1 says that even a **perfectly linear** projection from a
different SCD would not supply the desired chain tour.

## 5. Exact framework-level length implication

Consider the restricted construction scheme that:

1. chooses one exposing state for each SCD chain;
2. lists the chains in the orders supplied by the `K` projection paths; and
3. uses a direct MTF walk between consecutive assigned states, inserting
   auxiliary update states only when a one-step transition is impossible.

A one-step-compatible adjacency costs one update.  Every incompatible
adjacency costs at least two updates and therefore at least one extra update
over the width baseline.  Equation (4.1) forces at least

\[
                           W-2K-1
\tag{5.1}
\]

extra updates inside the projection paths.  Ignoring initialization and the
joins between distinct paths, the scheme already pays asymptotically

\[
                         2W-o(W).
\tag{5.2}
\]

More exactly, the `W-K` internal forest adjacencies cost at least

\[
 (W-K)+(W-2K-1)=2W-3K-1
\tag{5.3}
\]

updates.  The `K-1` joins between path components cost at least one update
each.  Thus, before charging any nontrivial initialization cost, a continuous
walk in this prescribed chain order costs at least

\[
                           2W-2K-2
\tag{5.4}
\]

updates between assigned chain states.

This is a lower bound only for this direct chain-by-chain realization
scheme, not for `nu(2m)`.  An auxiliary state might be reorganized to expose
parts of several chains, and a wholly different state-aware tour can use
cross-chain arcs unrelated to the central projection.

The precise conclusion is:

> A two-sided rainbow SCD path forest and an MTF--SCD tour are almost
> orthogonal objects.  The former cannot be converted into the latter by
> repairing only its `K=Cat_m` component seams; asymptotically every internal
> forest edge must be replaced or globally reinterpreted.

## 6. A positive reduction that survives

Although it does not provide an MTF tour, a two-sided rainbow linear forest
still has a clean chain-cover interpretation.

### Proposition 3 (central path factor gives a width chain partition)

Let `E` be a spanning linear forest on the `m`-sets such that its `C` edge
meets are all `(m-1)`-sets once and its edge joins are all `(m+1)`-sets once.
Then the full Boolean lattice has a saturated partition into exactly `W`
chains whose central three-rank section is encoded by `E`.

#### Proof

Orient every path of `E` toward one endpoint.  For each oriented edge
`T -> T'`, make the central three-set chain

\[
             T\cap T'\ \subset\ T\ \subset\ T\cup T'.
\tag{6.1}
\]

The meet and join hypotheses make all bottom and top sets in (6.1) distinct,
and the path orientation makes all middle tails `T` distinct.  There are `C`
such chains.  The remaining `W-C=K` middle sets form singleton chains.  This
partitions ranks `m-1,m,m+1`.

For every `r<m-1`, choose an inclusion matching that saturates rank `r` into
rank `r+1`.  The union of these matchings partitions the lower half into `C`
saturated chains, one ending at each `(m-1)`-set.  Dually, inclusion matchings
partition the upper half into `C` saturated chains, one starting at each
`(m+1)`-set.  Attach these lower and upper chains to (6.1).  The `K` middle
singletons remain singleton.  The result is a saturated partition of the
entire lattice into `C+K=W` chains.  `square`

The inclusion matchings exist by the normalized matching property of the
Boolean lattice (or by restricting any standard SCD to consecutive levels).

Theorem 1 applies to this partition even though its chains need not be
symmetric.  Every non-root middle vertex owns a central triple and hence its
chain continues above the middle; exactly one lower extension contains the
empty set.  Therefore the same `K+1` compatibility bound holds.  Passing from
an SCD to this more flexible minimum chain partition does not repair the MTF
failure.

This proposition separates two questions that had been conflated:

* the linear-forest problem is a central **chain-partition design** problem;
* the MTF problem is a composable **state-transversal** problem.

Theorem 1 proves that solving the first does not supply the local arcs needed
for the second.

## 7. The exact next mathematical targets

There are now three logically distinct routes.

1. **Pure central design.**  Construct a perfect matching between the
   `(m-1)`- and `(m+1)`-layers (under containment) whose square graph on the
   middle layer is acyclic and has maximum degree two.  This is exactly the
   two-sided rainbow linear-forest problem.  It remains useful for derivative
   constructions, but not as an MTF tour by itself.
2. **State-aware SCD tour.**  Ignore the central projection when selecting
   transitions.  Work in the decorated state-fiber graph and find a
   transversal path cover with `pH=o(W)`.  The selected arcs must preserve
   target-minimum refinement; ordinary cube or Johnson adjacency is
   insufficient.
3. **Hybrid coverage.**  Use the central path factor only to cover the first
   upper and lower shadows, while a different global word handles deeper
   ranks.  Any claimed length bound must explicitly account for joining and
   factor-labeling; Proposition 3 alone gives no OR array.

The main strategic correction is therefore decisive: do not spend effort
making an SCD projection linear in the hope that this automatically solves
the move-to-front scheduling problem.  If the goal is the MTF route, the next
object must be built directly in the ordered-partition state graph.
