# Transparent gluing is exactly router-resilient connectivity

Date: 2026-07-31  
Status: exact dimension-uniform reduction on the prepared private/aligned
fixed-decoration face of item 2189; no all-`m` catalogue-existence claim

## 0. Verdict

After a debt-carrying repair packet has terminated, suppose the hypotheses
`H0`--`H5` of
`MATH_THEOREM_CATALAN_ORDERED_FIXED_D_TRANSPARENT_GLUING_AFTER_ROUTER_20260731.md`
hold.  Thus every transparent collar label `t` has

* one edge `c_t` in the multigraph `K` on the current factor components;
* one source `s_t` in a fixed vertex-capacitated linkage network `N` with
  sink bank `Z`; and
* private/aligned gap effects and a redundant directed-reachability row.

For a set `Y` of router vertices, let

\[
 T_Y=\{t:s_t\text{ can reach }Z\text{ in }N-Y\},
 \qquad
 K_Y=(V(K),\{c_t:t\in T_Y\}).                         \tag{0.1}
\]

Then a fixed-decoration transparent component-spanning list exists if and
only if

\[
 \boxed{\quad c(K_Y)\le |Y|+1
        \qquad\text{for every }Y\subseteq V(N).\quad} \tag{0.2}
\]

Here isolated factor vertices count as components of `K_Y`.  Thus the full
graphic--gammoid rank family collapses to one Hall--Tutte-style statement:
deleting `y` routing resources may split the surviving transparent collar
graph into at most `y+1` pieces.

This is strictly a post-repair theorem.  It does not construct the fixed
decoration, the transparent catalogue, its private/aligned gap realization,
or the later residence/deep-shadow/compiler state.

## 1. Gammoid rank as a router deletion minimum

For a label set `S`, let `r_L(S)` be the maximum number of sources
`{s_t:t in S}` which can be linked vertex-disjointly to distinct sinks in
`Z`.  Unit source arcs may be used to model the option of discarding a
source.  Vertex-capacitated Menger then gives

\[
 \boxed{
 r_L(S)=\min_{Y\subseteq V(N)}
       \bigl(|Y|+|S\cap T_Y|\bigr).}                  \tag{1.1}
\]

Indeed, after deleting `Y`, every source in `S cap T_Y` still has a route
to the sink bank, so its unit source arc must also be cut.  Conversely, `Y`
together with those source arcs separates all of `S` from `Z`.  Minimizing
over `Y` is the vertex-capacitated max-flow/min-cut theorem.  Equivalently,
one may restrict `Y` to internal router vertices after source splitting;
this avoids double-counting a source vertex itself.

## 2. Matroidal spanning-tree criterion

Let `delta_K(Pi)` be the collar labels whose component edges cross a
partition `Pi` of `V(K)`.  A standard matroidal spanning-tree theorem gives

\[
 \boxed{
 \text{`K` has a spanning tree independent in the linkage gammoid}
 \iff
 r_L(\delta_K(\Pi))\ge |\Pi|-1
 \quad\text{for every partition }\Pi.}              \tag{2.1}
\]

For completeness, (2.1) is also an immediate specialization of Edmonds'
matroid-intersection formula.  Necessity follows because every spanning
tree has at least `|Pi|-1` edges crossing `Pi`, and every subset of a
gammoid-independent set is independent.  Sufficiency is the graphic--
gammoid common-basis theorem.

Substitute (1.1) into (2.1).  The condition becomes

\[
 |Y|+|\delta_K(\Pi)\cap T_Y|\ge |\Pi|-1
 \quad\text{for every }(Y,\Pi).                       \tag{2.2}
\]

But `delta_K(Pi) cap T_Y` is exactly the set of edges of `K_Y` crossing
`Pi`.

## 3. Partition cuts collapse to component count

### Lemma 3.1

If a graph `G` has `c(G)` connected components and `Pi` is a partition of
its vertex set into `p` nonempty blocks, then

\[
                    |\delta_G(\Pi)|\ge p-c(G).        \tag{3.1}
\]

Equality is attained by the partition into the connected components when
`p=c(G)`.

#### Proof

Inside each connected component, contract every nonempty intersection with
a block of `Pi`.  The resulting quotient is connected, hence has at least
one fewer edge than vertices.  Summing these inequalities over the
components gives (3.1).  For the component partition no edge crosses.
\(\square\)

### Theorem 3.2 (router-resilience criterion)

Under the prepared hypotheses, (2.1) is equivalent to (0.2).

#### Proof

Assume (0.2).  For fixed `Y` and a `p`-block partition `Pi`, Lemma 3.1
gives

\[
 |Y|+|\delta_{K_Y}(\Pi)|
 \ge |Y|+p-c(K_Y)
 \ge p-1,
\]

which is (2.2).

Conversely, take `Pi` to be the component partition of `K_Y`.  Then its
crossing set in `K_Y` is empty, so (2.2) gives

\[
                    |Y|\ge c(K_Y)-1.
\]

This is (0.2).  The ordered fixed-decoration theorem then turns the common
spanning tree into an executable transparent gluing list.  \(\square\)

## 4. Why ordinary connectivity is insufficient

Take three factor components and let `K` be a triangle with collar labels
`a,b,c`.  In `N`, route all three sources through one common unit-capacity
bottleneck `v` before the sink bank.  Every ordinary two-block component cut
is crossed by at least two collar edges, and `K` itself is connected.  But
for `Y={v}` no source reaches a sink, so `K_Y` has three isolated vertices:

\[
                    c(K_Y)=3>|Y|+1=2.                \tag{4.1}
\]

The linkage gammoid has rank one, so no two-edge spanning tree can be routed.
This is the smallest calibration showing that component connectivity without
router resilience does not close the transparent gluing gate.

## 5. Coherent-port transparent gluing corollary

Assume additionally that the prepared catalogue is made of pairwise
compatible coherent all-six incidence hexagons in the sense of
`MATH_THEOREM_CATALAN_COHERENT_ALLSIX_TRANSPARENT_HEX_20260731.md`.
Let `S` be a label set whose component edges form the common spanning tree
provided by (0.2).  Suppose:

1. the union of the six ports of the labels in `S` passes the forced-port
   residual gap--Hall criterion of
   `MATH_THEOREM_CATALAN_FORCED_PORT_GAP_HALL_20260731.md`;
2. the occurrence-gap effects are private/aligned as in item 2189; and
3. a physical trace breaker is protected.

Then the residual Hall matching supplies one joint decoration `D` containing
all six ports of every label in `S`.  Coherence makes every selected toggle
`D`-transparent without any further local palette test.  Condition (0.2)
provides a common graphic--gammoid spanning tree, and item 2189 makes every
ordering of that tree an executable component-spanning list preserving `D`,
leaf peeling and the protected forest face.

Consequently the genuinely constructive central supply problem on this face
has only three rows:

* enough coherent component edges;
* one joint forced-port matching extension; and
* router resilience `c(K_Y)<=|Y|+1`.

Transparency itself has disappeared as an independent constraint.  This is
a conditional central theorem, not a construction of such a catalogue.

## 6. Consequence for the all-`m` programme

The missing post-repair catalogue theorem can now be stated without an
exponential matroid-rank ledger:

> construct fixed-decoration transparent collars whose surviving component
> graph obeys `c(K_Y)<=|Y|+1` after every router deletion.

On a node-private tree-contiguous construction this is especially natural:
each deleted private router may expose at most one additional component.
Proving that structural statement would discharge the graphic--gammoid
selection and ordering layer at once.  Palette preparation, residence,
deeper shadows, primitive voltage, and the lower compiler remain separate.
