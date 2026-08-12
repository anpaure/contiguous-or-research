# Private coherent trees make forced Hall and router resilience automatic

Date: 2026-07-31  
Status: exact all-dimension conditional theorem; proves two recursive closure
rules and sharp counterexamples; no uniform private coherent-tree supply
claim

## 0. Verdict

Two of the three rows in the coherent transparent-gluing target have exact
private recursive certificates.

1. **Matching closure.**  Forced coherent ports extend through the residual
   gap--Hall matching whenever every private forced block has zero matching
   flux under one base perfect matching.
2. **Router closure.**  Router resilience is preserved under a tree sum of
   resilient blocks when every interblock bridge owns a vertex-disjoint
   private route.

Hence a coherent component tree becomes an accepted transparent gluing tree
if its forced gap/colour triples are matching-closed and its occurrence
transfers are privately routed.  The missing all-`m` statement is supply of
that joint private state, not another gluing-order theorem.

## 1. Forced edges in a bipartite perfect matching

Let `Gamma=(G,C;E)` be a balanced bipartite graph with a perfect matching
`M`, and let `F` be a matching of edges which are required in the final
perfect matching.

### Theorem 1.1 (alternating-cycle criterion)

There is a perfect matching `M'` containing `F` if and only if there is a
vertex-disjoint family of `M`-alternating cycles such that

* every edge of `F-M` occurs on a non-`M` half; and
* no edge of `F cap M` occurs on an `M` half.

#### Proof

If `M'` exists, `M triangle M'` is a vertex-disjoint union of alternating
even cycles.  Every forced edge not already in `M` lies on the `M'` half of
one cycle, while a forced edge in `M` is retained and therefore lies on no
cycle's deleted half.

Conversely, flip `M` on all the displayed cycles.  Vertex disjointness keeps
the result a perfect matching, the first condition inserts every missing
forced edge, and the second deletes no already forced edge.  \(\square\)

### Corollary 1.2 (zero-flux private blocks)

Partition the forced matching into vertex-disjoint blocks

\[
                      F=\bigsqcup_t F_t,\qquad
                      F_t:G_t\longrightarrow C_t,     \tag{1.1}
\]

where `G_t subseteq G` and `C_t subseteq C`.  If

\[
                         M(G_t)=C_t                   \tag{1.2}
\]

for every `t`, then `F` extends to a perfect matching.

Indeed, `M` restricted to `G_t union C_t` and `F_t` are two perfect
matchings of the same balanced vertex block.  Their symmetric difference is
a union of alternating cycles.  The blocks are vertex-disjoint, so all
cycles may be flipped simultaneously.

For one coherent incidence hexagon, take the three forced `B`-position gaps
as `G_t` and its three forced lower colours as `C_t`.  Condition (1.2) says
that the old matching has no net endpoint leaving that private triple.  It
is strictly weaker than requiring three singleton sockets.

### Minimal flux obstruction

Let the base matching be `g_i-c_i`, `i=1,...,4`, and force

\[
                 g_1c_2,\quad g_2c_3,\quad g_3c_4.   \tag{1.3}
\]

The forced edges are disjoint, and each neighbourhood may be realized by
the interval lists `(c1,c2),(c2,c3),(c3,c4),(c4)`.  But `M union F` contains
the open alternating path

\[
 c_1-g_1-c_2-g_2-c_3-g_3-c_4-g_4,                   \tag{1.4}
\]

not a cycle.  Deleting the forced vertices leaves `g_4,c_1` unmatched with
no edge.  Thus disjoint triples and interval-convex support alone do not
imply Hall; zero flux or an explicit endpoint router is necessary.

## 2. Router-resilient tree sums

For `i=1,...,h`, let `(K_i,N_i)` be a prepared catalogue block with disjoint
component set and disjoint router bank.  Suppose

\[
               c((K_i)_{Y_i})\le |Y_i|+1             \tag{2.1}
\]

for every deletion set `Y_i subseteq V(N_i)`.

Let `J` be a tree on the blocks.  For every bridge `a=ij` of `J`, add one
component edge joining a vertex of `K_i` to a vertex of `K_j`, and give its
label one source-to-sink router path `P_a`.  Assume the paths `P_a` are
pairwise vertex-disjoint and avoid every block router bank.

### Theorem 2.1 (private tree-sum closure)

The union catalogue satisfies

\[
                         c(K_Y)\le |Y|+1              \tag{2.2}
\]

for every router deletion set `Y`.

#### Proof

Write `Y_i=Y cap V(N_i)` and let

\[
                   D=\{a:Y\cap V(P_a)\ne\varnothing\}.
\]

The surviving graph contains every `(K_i)_(Y_i)` and every bridge of
`J-D`.  Joining the surviving block pieces across those bridges gives

\[
\begin{aligned}
 c(K_Y)
 &\le \sum_i c((K_i)_{Y_i})-\bigl((h-1)-|D|\bigr)\\
 &\le \sum_i(|Y_i|+1)-(h-1)+|D|\\
 &=1+\sum_i|Y_i|+|D|.
\end{aligned}                                         \tag{2.3}
\]

The bridge paths are pairwise disjoint and avoid the block banks, so every
failed bridge in `D` can be charged injectively to a distinct vertex of
`Y` outside all `Y_i`.  Therefore

\[
                   \sum_i|Y_i|+|D|\le |Y|,
\]

and (2.2) follows.  \(\square\)

The theorem includes rooted leaf insertion, one-sums, and tree-indexed ear
extensions.  Extra catalogue labels are harmless because they can only join
surviving components further.

### Laminar-cut corollary

A weaker certificate replaces literal disjoint paths by a laminar charging
family.  Associate router vertices with a laminar family of component sets.
If, after deleting `Y`, every nonempty atom of the generated laminar
partition induces a connected subgraph of `K_Y`, then the family has at most
`|Y|+1` atoms and (2.2) follows.  In particular, it suffices to fix a rooted
backbone tree and charge every failed backbone edge injectively to a deleted
resource assigned to that edge.

This is the precise useful meaning of tree-contiguous routing.  Merely
placing components in a tree order does not prove resilience.

## 3. Sharp router cautions

1. On a three-component path, if both bridge sources must traverse one
   router vertex `v`, deleting `v` kills both bridges and leaves three
   components, violating `3<=2`.
2. Singleton deletion tests are insufficient.  On the four-component path
   with edges `e1,e2,e3`, let `e1` route only through `x`, `e2` only through
   `y`, and `e3` have one route through either `x` or `y`.  Deleting either
   singleton leaves two components, but deleting `{x,y}` kills every edge
   and leaves four components, violating `4<=3`.

The second example is minimal for a two-router synergy failure.  It shows
that “one exposed component per deleted router” must be a global charging
or laminar-backbone theorem, not a collection of singleton checks.

## 4. Coherent-tree implication and scope

Suppose a component-spanning coherent-hex tree has one joint upper
transversal and base gap matching `M`.  Assume collectively the full
prepared `H0`--`H5` cube, including component-faithful Boolean
superposition and prefix reachability redundancy.  If

* every forced upper port belongs to that transversal and the forced upper
  colours are distinct;
* the forced lower ports occupy distinct transversal gaps and have distinct
  lower colours;
* its forced gap/colour triples are pairwise disjoint and satisfy (1.2);
* its private gap attachments satisfy the leaf-forest condition;
* its occurrence transfers have the private tree-sum or laminar certificate
  of Section 2; and
* a physical trace breaker is protected,

then all forced ports install simultaneously, router resilience holds, and
the ordered fixed-decoration theorem makes every ordering of the tree an
accepted transparent gluing list.

The standard `m=4` triple `{18,20,24}` and repaired `m=5` triples
`{82,84,88}`, `{50,52,56}` lie on this zero-flux face: their old relevant
gaps are singleton matched sockets.  The all-`m` existence of such matching-
closed blocks and private occurrence routes remains open.  Colour privacy
alone does not imply occurrence-router privacy.
