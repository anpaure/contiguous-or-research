# Diagonal q1 rows give a literal two-factor router

**Date:** 2026-08-03  
**Status:** unconditional occurrence-level theorem for one cyclic flat
q1-exact row, followed by the exact terminal-socket interface.  No finite
search is used.  The theorem does not assert that the selected middle-owner
cells remain unused supplier sinks after the common cap and compensation
linkage have been fixed.

## 0. Result

Let `2<=d<W`, let indices be in `Z_W`, and let

\[
                 A_0,A_1,\ldots,A_{W-1}\ne\varnothing                 \tag{0.1}
\]

be literal source letters.  Suppose

\[
 T_i=\bigcup_{h=i}^{i+d}A_h\in{[k]\choose r}                       \tag{0.2}
\]

runs once through the complete rank-`r` layer, and suppose the last proper
prefixes

\[
 P_i=\bigcup_{h=i+1}^{i+d}A_h                                      \tag{0.3}
\]

satisfy the **q1-exactness** equations

\[
 P_i=T_i\cap T_{i+1}\in{[k]\choose r-1}                            \tag{0.4}
\]

and run once through the complete rank-`(r-1)` layer.  Necessarily the two
central layers have equal size, as in `k=2r-1`.

Give every interval in (0.2)--(0.3) its physical occurrence address.  Then
the two literal extensions

\[
 \begin{aligned}
 R_i^- &: P_i\xrightarrow{\ A_i\ }T_i,\\
 R_i^+ &: P_i\xrightarrow{\ A_{i+d+1}\ }T_{i+1}
 \end{aligned}                                                     \tag{0.5}
\]

form an occurrence-labelled spanning two-factor between the `P`-ports and
the `T`-terminal types.  Both semantic equations are literal:

\[
                  P_i\cup A_i=T_i,
 \qquad           P_i\cup A_{i+d+1}=T_{i+1}.                       \tag{0.6}
\]

Moreover:

1. the complete left phase `{R_i^-}` is a pairwise resource-disjoint full
   port linkage to the `W` distinct `T_i` sockets;
2. the complete right phase `{R_i^+}` is another such linkage;
3. if both incidences are retained as a degree-two path catalogue and the
   priced resources are ports, boundary-letter occurrences, and terminal
   sockets, every priced resource has raw multiplicity exactly two.
   Consequently uniform path weight `1/2` has zero overload.

Thus a q1-exact literal diagonal row closes the **occurrence map, semantic
compatibility, and capacity packing** of its own chronological Middle-Levels
two-factor.  It does not require a generic suffix-expansion theorem.

The remaining cap interface is exact.  If, after deleting the compensation
linkage and transported background, every addressed owner occurrence `T_i`
has one distinct unused compatible unit terminal socket attached by a
private arc, then the complete physical port bank has suffix rank `W`.
More generally, an injection from owner occurrences to compatible unused
sockets with pairwise private attachments is sufficient.

Conversely, on the **native-owner-only face** in which the only admitted
terminal for `R_i^\pm` is the central occurrence `T_i`, reserving/deleting
all `T_i` owner capacities leaves suffix rank zero.  Hence the diagonal
geometry does not itself manufacture unused terminal capacity.  One socket
per routed owner (or a separate compatible terminal matching) is the exact
smallest additional resource for this literal lift.

## 1. Physical addresses and the chronological two-factor

The port occurrence is the interval

\[
                         p_i=[i+1,i+d]_W,                           \tag{1.1}
\]

with value `P_i`.  The owner occurrence is

\[
                         o_i=[i,i+d]_W,                             \tag{1.2}
\]

with value `T_i`.  Equal values at different addresses would remain
different physical resources; under (0.2)--(0.4), however, both value
families are already injective.

The lower bound `d>=2` keeps the length-`d` port cells distinct from the
length-one boundary-letter cells in the literal capacity ledger.  At
`d=1`, `p_i` is the same physical cell as `a_(i+1)`; treating those two
names as independent would be an unsound alias split.  The semantic
identities below still hold at `d=1`, but the disjointness and overload
claims then require a separate coalesced-capacity audit and are not asserted
here.

Let `F` be the bipartite graph with port shore `{p_i}` and owner shore
`{o_i}`, and edges

\[
                         p_io_i,qquad p_io_{i+1}.                  \tag{1.3}
\]

Every port has degree two.  Every owner `o_i` is incident with `p_i` and
`p_(i-1)`, so every owner also has degree two.  On semantic values, (0.4)
gives

\[
                 P_i\subset T_i,
 \qquad          P_i\subset T_{i+1},                              \tag{1.4}
\]

and the rank difference is one.  Since both shores enumerate their full
central layers, `F` is a spanning two-factor of `ML(2r-1)`.

In the displayed chronological addresses it is in fact the alternating
cycle

\[
 o_0,p_0,o_1,p_1,\ldots,o_{W-1},p_{W-1},o_0.                       \tag{1.5}
\]

This assertion is about occurrence addresses.  Even if the same abstract
two-factor is later presented with another ordering, (1.5) retains the
literal chronology needed below.

## 2. Exact literal extension identities

### Theorem 2.1 (two boundary extensions)

Equations (0.6) hold for every `i`.

### Proof

By definitions (0.2)--(0.3),

\[
 A_i\cup P_i
 =\bigcup_{h=i}^{i+d}A_h
 =T_i.                                                            \tag{2.1}
\]

Similarly,

\[
 P_i\cup A_{i+d+1}
 =\bigcup_{h=i+1}^{i+d+1}A_h
 =T_{i+1}.                                                        \tag{2.2}
\]

All indices are cyclic, so these identities also cover the displayed
`W-1|0` boundary.  No residence, Johnson-transition, or endpoint-symbol
inference is being substituted for the equations: they are literal unions
of the addressed intervals. `square`

The q1 condition (0.4) is load-bearing.  Flat equal-rank owners alone do
not imply it.  For example at `d=2`, one may have

\[
 T_0=\{1,2,3\},\qquad T_1=\{1,2,4\},
 \qquad \bigcup_{h=1}^{2}A_h=\{1\},                               \tag{2.3}
\]

with the persistent coordinate `2` supplied only by both boundary letters.
Then the overlap cell has rank one rather than rank two.  Accordingly this
theorem applies either to a full-erosion q1 row or to a separately pinned
q1-exact factor; q1-exactness is not inferred from flatness.

## 3. Capacity ledger

Make the following finite resources explicit.

* Every port occurrence `p_i` has capacity one.
* Every boundary-letter occurrence `a_h` at source position `h` has
  capacity one if source positions are priced by the physical model.
* Every terminal socket `tau_i` attached to `o_i` has capacity one.
* Route-specific transport arcs have infinite capacity and retain the
  route's occurrence and semantic state.

The two routes in (0.5) are read as

\[
 p_i\longrightarrow a_i\longrightarrow\tau_i,
 \qquad
 p_i\longrightarrow a_{i+d+1}\longrightarrow\tau_{i+1}.          \tag{3.1}
\]

If a shared source resource is represented by an ordinary node-split arc,
the surrounding state expansion must forbid an illegal cross-route switch,
or all terminal sockets in that block must be genuinely interchangeable.
The theorem never forgets this semantic-state condition.  The two explicit
phases below avoid the issue entirely because they never share a source
resource.

### Theorem 3.1 (two literal full linkages)

Each of

\[
                         {\cal R}^- =\{R_i^-:i\in Z_W\},
 \qquad                  {\cal R}^+ =\{R_i^+:i\in Z_W\}           \tag{3.2}
\]

is a pairwise resource-disjoint linkage of every port to every terminal
socket.

### Proof

In the minus phase, the routes use respectively the distinct triples

\[
                         (p_i,a_i,\tau_i).                          \tag{3.3}
\]

All three coordinates of these triples are injective in `i`.  In the plus
phase they use

\[
                         (p_i,a_{i+d+1},\tau_{i+1}).                \tag{3.4}
\]

Translation by `d+1` and by `1` are permutations of `Z_W`, so these three
coordinates are again injective.  Route-specific transport arcs are
private.  Equations (2.1)--(2.2) prove the terminal semantics. `square`

Thus, after compatible sockets are exported, no max-flow rounding is
actually needed: either phase is an explicit full suffix router.  Every
sub-bank of ports inherits the corresponding restricted linkage.

### Corollary 3.2 (zero raw overload of the two-factor catalogue)

If both routes at every port are retained, every finite resource in the
above ledger has raw multiplicity exactly two.  Uniform weight `1/2`
therefore gives a capacity-feasible endpoint-balanced flow of value `W`.

### Proof

Port `p_i` lies on its two displayed routes.  Socket `tau_i` terminates
`R_i^-` and `R_(i-1)^+`.  Source occurrence `a_h` lies on `R_h^-` and
`R_(h-d-1)^+`.  Hence every multiplicity is two.  Dividing by two gives
load one at every unit resource. `square`

This is a zero-**overload** statement, not an endpoint-star statement:
the two routes sharing `a_h` generally have neither a common port nor a
common terminal.  The explicit phases in Theorem 3.1 are the clean literal
certificate when terminal identities are not interchangeable.

## 4. The exact terminal-socket interface

Let the fixed post-compensation child contain a unit terminal bank `S`.
Suppose there is an injection

\[
                         \theta:\{o_i\}\hookrightarrow S           \tag{4.1}
\]

such that:

1. the fixed residual state admits the addressed minus routes
   `p_i -> a_i -> o_i` (or, uniformly, the addressed plus routes) as legal
   canonical full-block routes, with no hidden route resource omitted from
   the capacity ledger;
2. `theta(o_i)` accepts the semantic type `T_i` (or belongs to a genuinely
   interchangeable complete type shared by all `T_i`);
3. the attachment from `o_i` to `theta(o_i)` is private and uses no
   compensation/background capacity;
4. the socket, attachment, port, and boundary occurrence live in one common
   cap/guard/phase state; and
5. any additionally priced state or guard resource on (3.1) is either
   private in the chosen phase or already represented in the disjointness
   ledger.

Then take `tau_i=theta(o_i)` in Theorem 3.1.  The suffix gammoid on the
complete port set has rank `W`; concatenating any edge-private balanced
claim-to-port prefixes therefore services every claim by the exact balanced
rank-transfer theorem.

The co-located special case--one unused typed socket attached to every
owner occurrence--is the smallest transparent hypothesis.  It is weaker
than assuming a pre-existing arbitrary disjoint suffix router: the diagonal
row itself supplies and proves the entire linkage after those terminal
sockets are named.  The cardinality is sharp on this unit-sink face: a
linkage of `W` unit-capacity ports to distinct terminals requires at least
`W` units of terminal capacity by the terminal cut.

### Proposition 4.1 (reserved-owner counterface)

Restrict the admitted suffix system to the routes (0.5), and suppose their
only possible terminals are the native owner occurrence capacities `o_i`.
If all `o_i` are deleted because the central owner matching has reserved
them, then the residual suffix rank of the complete port set is zero.

### Proof

Every admitted route in (0.5) ends at one of the deleted vertices.  Hence
there is no port-to-terminal path, even for a singleton port. `square`

This proposition is deliberately scoped to the native diagonal lift.  It
does not assert that the full common-cap network has rank zero: remote
duplicate owner occurrences, alternating background recourse, or a
different supplier type may provide other terminals.  It proves exactly
that q1 geometry alone cannot be cited as an unused-sink theorem.

## 5. Linear rows and boundary charge

The architecture-free normalization theorem extracts linear diagonal
blocks rather than one cyclic row.  On a block with owners

\[
                         T_0,\ldots,T_{n-1}                         \tag{5.1}
\]

and q1-exact overlaps `P_0,...,P_(n-2)`, the same proof gives the literal
path

\[
             T_0,P_0,T_1,P_1,\ldots,P_{n-2},T_{n-1}.               \tag{5.2}
\]

The minus routes link every `P_i` to `T_i`; the plus routes link every
`P_i` to `T_(i+1)`.  Thus either phase links all `n-1` ports to distinct
owner sockets, leaving exactly one endpoint owner socket unused.  Across
`b` disjoint diagonal blocks, the only cardinality mismatch is exactly `b`
owner sockets.

This gives a useful bounded-piece corollary but not an automatic global
router.  The exact diagonal decomposition may have `O(d)` blocks, and the
architecture-free theorem does not prove q1-exactness on them.  Its
macroscopic extraction has `O_C(1/eta)` blocks only after discarding
`eta W+o(W)` owners, far too many for an additive bound.  Therefore the
present lemma closes the literal lift **once a q1-exact diagonal row is
constructed**; it does not turn the necessary architecture-free
normalization into an upper construction.

## 6. Exact scope

The theorem proves all of the following for a cyclic q1-exact flat row:

* an explicit injection from every abstract rank-`(r-1)` port value to one
  physical q1 interval occurrence;
* an explicit injection from every abstract rank-`r` terminal value to one
  physical owner occurrence;
* two semantically correct literal routes for every factor port;
* a spanning occurrence-labelled degree-two Middle-Levels factor;
* two explicit pairwise-disjoint full routing phases; and
* zero normalized raw overload for the union of both phases.

It does **not** prove:

* q1-exactness from flatness or from the architecture-free density theorem;
* that an independently selected protected Middle-Levels two-factor equals
  this chronological q1 factor;
* that the central owner occurrence is an unused post-compensation sink;
* common-cap product closure between two occurrence coordinates;
* transported phase 1, upper coverage, deeper lower compilation, topology,
  or regeneration; or
* `nu(k)<=B(k)+O(1)`.

The exact positive bridge is therefore smaller than the former arbitrary
suffix-router premise:

\[
 \boxed{
 \text{q1-exact literal diagonal row}
 +\text{ one compatible unused socket per routed owner}
 \Longrightarrow
 \text{an exact h=2 literal suffix router}.}
\]
