# Run-transparent pair-cell squares and the exceptional-port gate

**Date:** 2026-08-04  
**Status:** unconditional local splice theorems, an exact correction to the
cross-stratum splice claim, and an exact abstract port-supply theorem.  This
note does **not** claim a spanning resident Johnson cycle, palette
surjectivity, or an upper/lower compiler.

## 1. Transition spacing

For a Johnson edge `XY`, put

\[
        \partial(XY)=X\mathbin\triangle Y.
\]

Thus `|partial(XY)|=2`.  A cyclic Johnson ordering is `L`-resident exactly
when, for every physical coordinate `z`, any two edges whose transition
supports contain `z` have cyclic edge-distance at least `L`.

Partition `[2r]` into pairs

\[
        P_i=\{i^0,i^1\}\qquad(1\le i\le r).
\]

A pair cell is specified by disjoint sets `(D,E,S)` with

\[
 |D|=|E|=t,\qquad |S|=m=r-2t.
\]

Pairs in `D,E,S` are respectively double, empty, and singleton.  The cell
is a cube `Q_m`; a cube transition in direction `i in S` changes both
physical coordinates of `P_i`.

## 2. The twisted same-stratum square

Take distinct pair indices `p,q`.  Let

\[
 \mathcal A=(D,E,S),\qquad p\in D,\ q\in S,
\]

and transfer the double status from `p` to `q`:

\[
 \mathcal B=((D-\{p\})\cup\{q\},E,(S-\{q\})\cup\{p\}).       \tag{2.1}
\]

The two cells have the same dimension `m`.  Write

\[
 P_p=\{p^0,p^1\},\qquad P_q=\{q^0,q^1\}.
\]

Fix an orientation of every pair in `S-{q}`.  The four owners

\[
\begin{aligned}
 x_0&:\quad P_p\text{ double},\ q^0\text{ selected},\\
 x_1&:\quad P_p\text{ double},\ q^1\text{ selected},\\
 y_0&:\quad p^0\text{ selected},\ P_q\text{ double},\\
 y_1&:\quad p^1\text{ selected},\ P_q\text{ double}
\end{aligned}                                                     \tag{2.2}
\]

form the twisted square

\[
              x_0-x_1-y_1-y_0-x_0.                              \tag{2.3}
\]

The horizontal edge in `A` has cube direction `q`; the horizontal edge in
`B` has cube direction `p`.  The two cross edges have supports

\[
 \partial(x_0y_0)=\{p^1,q^1\},\qquad
 \partial(x_1y_1)=\{p^0,q^0\}.                                  \tag{2.4}
\]

The use of opposite physical members in (2.4) is the decisive feature.

### Theorem 2.1 (one run-transparent twisted switch)

Let `G=(g_0,...,g_{N-1})` be a cyclic Hamilton Gray code of `Q_m`, and let
its transition word be

\[
        \gamma_0,\ldots,\gamma_{N-1}.
\]

Assume equal transition directions have cyclic separation at least `rho`,
where

\[
                         \rho\ge L+1.                            \tag{2.5}
\]

Choose an index `a` and call `gamma_a=*`.  Embed one copy of `G` in
`A`, sending `*` to pair `q`, and a second copy in `B`, sending `*` to
pair `p`.  Send every other abstract direction to the same physical pair
in `S-{q}` on the two sides.  Complement the `*` bit in the second copy
and translate the remaining cube bits so that the four cut endpoints are
exactly (2.2).

Delete `x_0x_1` and `y_0y_1`, and insert `x_0y_0` and `x_1y_1`.  The result
is one Hamilton cycle on the union of the two cells, and its minimum
physical-coordinate transition separation is at least

\[
                         \rho-1\ge L.                            \tag{2.6}
\]

#### Proof

Let

\[
 w=\gamma_{a+1}\gamma_{a+2}\cdots\gamma_{a-1}                 \tag{2.7}
\]

with cyclic indices.  Orient the two opened cube cycles so that the new
cycle is

\[
 x_0,y_0,\ G_B[g_{a+1}\leadsto g_a],\ y_1,x_1,
 G_A[g_{a+1}\leadsto g_a],x_0.                                  \tag{2.8}
\]

On every common singleton pair, the transition word in (2.8) is `ww`.
Deleting one distinguished position from a cyclic word can shorten the
distance between two consecutive retained occurrences by at most one.
Every cube direction occurs at least twice in a Hamilton cycle, so no
consecutive retained occurrences span more than one full period.  Hence
every common direction has separation at least `rho-1` in `ww`.

For pair `p`, the distinguished internal `p`-edge of the second cube was
deleted.  The two seams toggle different physical members `p^0,p^1`.
The nearest retained internal `p`-transition to either seam is at distance
at least `rho-1` (and, with the natural edge-slot convention, at least
`rho`), by the old run condition.  Pair `p` is constant in the
first cube.  The identical argument, with the two cubes interchanged,
handles `q`.  All other double or empty pairs are constant.  This proves
(2.6).  The ordinary square switch merges two disjoint cycles into one,
proving the topology claim. \(\square\)

### Corollary 2.2 (a matching of cells costs no residence)

In a fixed singleton-dimension stratum, take any matching in the cell graph
whose edges are double-status transfers (2.1), or their empty-status
complements.  Put coherently relabelled copies of the same `rho`-run cube
cycle in the two cells of every matched edge and perform Theorem 2.1.
The switches are vertex-disjoint, so they compose.  The resulting factor
has one resident cycle for every unmatched cell and one resident cycle for
every matched pair, all with run at least `rho-1`.

This is a genuine component reduction, but only by a cell matching.  It is
not a spanning-tree theorem: a cell used at several ports needs a common
phase/collar certificate, which is not supplied by Theorem 2.1.

## 3. Cross-stratum squares need collars

Now let

\[
 \mathcal C=(D,E,S),\qquad p\in D,\ q\in E,
\]

and let

\[
 \mathcal C^+=(D-\{p\},E-\{q\},S\cup\{p,q\}).                  \tag{3.1}
\]

Their dimensions are `m` and `m+2`.  If a cube edge of `C` and a cube
edge of `C+` use the same common direction `s in S` and agree on all common
orientations, their endpoints again form a Cartesian square.  However,
the two cross edges now use the **same** removed member of `P_p` and the
same added member of `P_q`.  Moreover `p,q` are active directions inside
the larger cube.  Therefore long opened arcs alone do not prove residence.

For an endpoint of an opened cube path, let its `(L-1)`-collar be the set
of pair directions used on the first `L-1` retained edges going inward
from that endpoint.

### Theorem 3.1 (correct cross-stratum collar criterion)

The square switch between `C` and `C+` is `L`-resident provided that:

1. both old cube cycles are `L`-resident;
2. both opened arcs have at least `L` edges;
3. neither `p` nor `q` occurs in either endpoint collar of the larger
   opened cube;
4. at each of the two new seams, the two inward collar sets on its two
   sides are disjoint after the common directions `S` are physically
   identified.

#### Proof

The seam coordinates lie in `P_p union P_q`.  These pairs are constant on
the small side, and condition 3 keeps their first possible large-side
transition at distance at least `L`.  Their two seam occurrences are
separated through either opened arc by condition 2.

Every coordinate belonging to a common singleton pair is unchanged by a
seam.  A new short run could therefore arise only from one occurrence in
the left collar and one in the right collar.  Condition 4 excludes exactly
that event.  Internal runs are protected by condition 1, and all other
pairs are constant. \(\square\)

The criterion is sufficient, not claimed necessary.

### Corollary 3.2 (a crude high-stratum existence range)

Suppose both dimensions admit cube Hamilton cycles of run at least `L`,
and

\[
                             m\ge4L.                              \tag{3.2}
\]

Then any one cell adjacency (3.1) admits a relabelling, translation, and
cut for which Theorem 3.1 applies.

#### Proof

Each endpoint collar contains at most `L-1` distinct directions.  In the
larger cube choose the physical labels `p,q` among two abstract directions
outside the union of its two collars; (3.2) leaves ample room.  Reserve the
common cut direction `s`, which is absent from all four collars by the old
run condition.

The union of the two large-side collar sets has size at most `2L-2`.
The complement of the union of the two small-side collar sets, after
reserving `s`, has size at least

\[
             m-(2L-2)-1\ge2L-1.
\]

Map the former union injectively into the latter complement and extend to
a bijection of all common directions.  This simultaneously makes the two
cross-seam collar pairs disjoint.  Cube translation then aligns the common
endpoint orientations, while the two local pair gauges align the cross
edges.  Conditions 1--4 follow. \(\square\)

Thus cross-stratum splicing is elementary far above the residence scale.
It is **not** established in the critical window `m=L+O(log r)` used by
the almost-spanning pair factor.

## 4. Why the smallest cells are not one-edge ears

### Lemma 4.1 (triangle pulse)

Let `U,V,W` be three distinct Johnson vertices with all three pairwise
adjacent.  In the two-edge path

\[
                             V-U-W                                \tag{4.1}
\]

some physical coordinate changes on both consecutive edges.  Hence (4.1)
has residence one.

#### Proof

Every Johnson triangle has a common `(r-1)`-set `K` and three distinct
coordinates `u,v,w`, with vertices `K+u,K+v,K+w`.  At the middle vertex
`K+u`, coordinate `u` is inserted on one incident edge and deleted on the
other. \(\square\)

An `m=0` cell is a singleton vertex.  Subdividing one edge of a neighbouring
`Q_2` cell through that vertex is exactly Lemma 4.1.  An `m=1` cell is a
single cube edge rather than a cycle; attaching either endpoint by the same
triangle operation has the same pulse.  Therefore the naive `Q_0` or
`Q_1` ear is not a resident absorption.  A longer buffer with different
transition supports is genuinely required.

## 5. Abstract exceptional-port supply is not the missing count

Let `V_m` be the owners whose singleton dimension is `m`, and put

\[
                         t={r-m\over2}.
\]

Join `V_m` to `V_{m+2}` by cross-stratum Johnson edges.  This bipartite
graph is biregular:

\[
 \deg_{V_m}=4t^2,\qquad
 \deg_{V_{m+2}}=(m+2)(m+1).                                      \tag{5.1}
\]

Indeed, upward from a lower owner one chooses a double pair, an empty pair,
the member removed from the first, and the member added to the second.
Downward from an upper owner one chooses an ordered pair of distinct
singleton pairs to collapse to double and empty.

### Proposition 5.1 (two abstract ports per exceptional owner)

If

\[
             4t^2\ge2(m+2)(m+1),                                \tag{5.2}
\]

then every owner of `V_m` can be assigned two distinct neighbours in
`V_{m+2}`, with no upper owner assigned more than once.

#### Proof

For `X subseteq V_m`, biregularity gives

\[
 |N(X)|\ge {4t^2\over(m+2)(m+1)}|X|\ge2|X|.                     \tag{5.3}
\]

Replace every lower vertex by two identical clones and apply Hall's
theorem. \(\square\)

For `m=0,1` and `L=Theta(sqrt r)`, (5.2) has enormous slack.  Thus a lack
of adjacent owner ports is not the exceptional-cell obstruction.  The two
chosen edges can still share a transition coordinate, their continuations
can still reuse it inside `L` steps, and their eventual cube endpoints can
still fail the simultaneous collar condition.  Proposition 5.1 is an
abstract port theorem, not a buffer theorem.

## 6. Exact remaining residence gate

The pair-stratified long-run factor can now be summarized as follows.

* Within every good cell, residence is proved by the long-run cube code.
* A matching of same-dimensional cells can be fused with **zero residence
  debt** by the twisted square of Theorem 2.1.
* A single cross-dimensional fusion is proved under the exact collar
  conditions of Theorem 3.1, and those conditions are automatically
  achievable in the crude range `m>=4L`.
* The smallest strata have abundant abstract upward ports, but their
  shortest ears provably create a length-one pulse.

What remains is one global statement.

> **Phase-coherent multiport buffer theorem.**  Choose cuts in the good
> cube cycles, and longer ears for every owner in the low singleton
> strata, so that (i) every cell cycle and every exceptional owner is used
> exactly once; (ii) every cross seam passes the two-sided transition-label
> collar test; and (iii) the resulting component graph has boundedly many
> components (ideally one).

Neither the exponential smallness of the low strata nor the biregular
port count proves this theorem.  It is an occurrence-labelled endpoint
matching problem with transition histories.

Finally, none of the switches above prices the immediate lower or upper
palette.  The two seam colours are explicit intersections and unions of
their endpoint owners, but their global distinctness and surjectivity must
be imposed separately.  Consequently this note advances the residence
gate only; it cannot be cited as an upper-decoration or compiler theorem.
