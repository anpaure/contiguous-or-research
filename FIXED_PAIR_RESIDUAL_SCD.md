# Fixed-pair residual SCDs and the orientation-coherence obstruction

This note develops the fixed-coordinate-pair construction suggested by the
partial pair-flip program.  It gives an exact simultaneous pairing of every
lower and upper rank via ordinary symmetric chain decompositions of residual
Boolean lattices.  It also proves that the most natural orientation-blind
assembly necessarily has linearly many tiny middle components.

The remaining target is thereby reduced to an orientation-dependent family
of residual SCDs whose central matchings form long cycles in the orientation
cubes.

## 1. Pair-state notation

Partition the `2m` ground coordinates into fixed pairs

\[
 P_i=\{a_i,b_i\},\qquad i\in[m].
\]

Every subset of the ground set has four pieces of pair data:

* `S`, the indices of split pairs (exactly one member is present);
* an orientation `eta in {0,1}^S` of those split pairs;
* `F`, the indices of full pairs;
* `E`, the indices of empty pairs.

These sets partition `[m]`, and the rank is

\[
 |S|+2|F|.                                             \tag{1.1}
\]

Fix `(S,eta)` and put

\[
 T=[m]\setminus S,\qquad n=|T|.                       \tag{1.2}
\]

A rank-`m-q` target with this split data corresponds exactly to a full-pair
set

\[
 F\in\binom{T}{(n-q)/2},                              \tag{1.3}
\]

where necessarily `n` and `q` have the same parity.  A rank-`m+q` target
with the same split data corresponds to a set of full pairs of size
`(n+q)/2`.

## 2. One residual SCD pairs all depths simultaneously

Choose a saturated symmetric chain decomposition

\[
 \mathcal D_{S,\eta}\quad\text{of}\quad 2^T.          \tag{2.1}
\]

### Theorem 1 (residual reflection theorem)

For every admissible `q` and every `F` in (1.3), the chain of
`D_(S,eta)` containing `F` contains a unique member

\[
 F^+\in\binom{T}{(n+q)/2}.                            \tag{2.2}
\]

The map

\[
 \Psi_{S,\eta,q}:F\longmapsto F^+                    \tag{2.3}
\]

is a bijection between the two indicated ranks, satisfies `F subset F^+`,
and all the maps (2.3), as `q` varies, are nested along the chains of the
same SCD.

Consequently, keeping `(S,eta)` fixed and replacing the full-pair set `F`
by `F^+` pairs every rank-`m-q` target with a unique containing
rank-`m+q` target, simultaneously for every depth.

#### Proof

A symmetric chain that contains rank `(n-q)/2` begins at some rank at most
`(n-q)/2`; its top rank is the complementary rank and is therefore at least
`(n+q)/2`.  Saturation gives a unique member of the latter rank.  Since an
SCD partitions both ranks, reflection within chains is a bijection.  The
containment and simultaneous nesting are immediate from the fact that all
members lie on the same saturated chain.  QED.

Write the segment from `F` to `F^+` as

\[
 F\subset F\cup\{i_1\}\subset\cdots\subset
 F\cup\{i_1,\ldots,i_q\}=F^+.                       \tag{2.4}
\]

In the original paired ground set, the lower and upper targets differ by
making the `q` pairs `P_(i_1),...,P_(i_q)` go from empty to full.  Choosing
one member of each at the middle and flipping those `q` orientations in the
order (2.4) gives a locally geodesic middle path whose intersection is the
lower target and whose union is the upper target.  Thus an ordinary residual
SCD supplies not only the two-sided colour pairing but the complete ordered
flag required by a depth-`q` pair-flip window.

## 3. The exact depth-one projection

Suppose `n=|T|` is odd.  At the middle of each residual chain, Theorem 1
uses an edge

\[
 F\subset F\cup\{i\},
 \qquad |F|=(n-1)/2.                                 \tag{3.1}
\]

The associated original lower and upper targets have two middle sets
between them, obtained by choosing `a_i` or `b_i` in the newly split pair.
They form a Johnson edge that flips the orientation of `P_i`.

Now fix a middle pair-type stratum:

\[
 R=\text{the split-pair indices},\qquad
 F_0=\text{the full-pair indices outside }R.          \tag{3.2}
\]

Necessarily the remaining pairs outside `R` are empty and

\[
 |F_0|=(m-|R|)/2.                                    \tag{3.3}
\]

Its middle sets form the orientation cube

\[
 Q_R=\{0,1\}^R.                                      \tag{3.4}
\]

For `i in R`, put `S=R\setminus{i}`.  The edge of `Q_R` in coordinate `i`
and with other orientations `eta` is selected exactly when the central
matching of `D_(S,eta)` contains

\[
 F_0\subset F_0\cup\{i\}.                            \tag{3.5}
\]

This is the exact coupling between residual SCDs and the projected middle
graph.

### Every prescribed central perfect matching extends to an SCD

The phrase “choose a residual SCD” imposes no hidden restriction at depth
one.

### Theorem 2 (central-matching extension theorem)

Let `T` have odd size `n=2h+1`.  Every perfect matching in the inclusion
graph

\[
 \binom Th\longleftrightarrow\binom T{h+1}            \tag{3.6}
\]

is the central matching of some saturated SCD of `2^T`.

#### Proof

Start with the prescribed matching as a symmetric chain decomposition of the
two central levels.  Inductively suppose that the band from ranks
`h-s+1` through `h+s` has been decomposed into symmetric chains.  These
chains give a bijection between their lower and upper endpoints.

Glue each paired endpoint into one middle vertex `y`.  Add the next outer
levels

\[
 X=\binom T{h-s},\qquad Z=\binom T{h+s+1}.             \tag{3.7}
\]

The resulting three-level poset has `|X|=|Z|<|Y|`.  Every `x in X` is
comparable with `h+s+1` vertices of `Y`, and every `z in Z` is comparable
with the same number; every `y` has `h-s+1` neighbours on each side.

For completeness, construct its SCD via an auxiliary bipartite graph.  Take
copies `Y_1,Y_2`, put `U=X dotcup Y_1` and `V=Z dotcup Y_2`, join `x` to
`y_2` and `z` to `y_1` when comparable, and join the two copies of every
`y`.  Give comparison edges weight `1/(h+s+1)` and identity edges weight
`1-|X|/|Y|`.  All row and column sums are one.  The support of this doubly
stochastic matrix has a perfect matching.  An identity edge leaves the old
band chain unchanged; a pair of comparison edges extends one old chain at
both ends.  Hence the perfect matching extends the band decomposition by one
rank on each side.

Iterating to the boundary gives a saturated SCD containing the originally
prescribed central matching.  QED.

This is the extension mechanism used in Griggs' three-level argument and in
the recursive count of Boolean SCDs.  Its significance here is concrete:
the orientation-dependent central matchings may be designed first for their
middle-graph behaviour, and only afterwards extended to full residual SCDs.
The higher-depth shift conditions still constrain those extensions, but
depth one does not.

## 4. Orientation-blind residual SCDs force tiny components

Call the construction orientation-blind if, for each split index set `S`,
the chosen residual SCD does not depend on `eta`:

\[
 \mathcal D_{S,\eta}=\mathcal D_S.                   \tag{4.1}
\]

### Theorem 3 (coordinate-subcube obstruction)

Under (4.1), for every middle pair-type stratum `(R,F_0)` there is a fixed
set `A(R,F_0) subset R` such that its selected projected graph is exactly

\[
 \bigcup_{i\in A(R,F_0)} M_i,                        \tag{4.2}
\]

where `M_i` is the complete coordinate-`i` matching of `Q_R`.

Hence the graph is regular of degree `|A(R,F_0)|`.  If it has maximum degree
at most two, then:

* `|A|=0`: all vertices are isolated;
* `|A|=1`: it is a perfect matching;
* `|A|=2`: it is a disjoint union of `2^(|R|-2)` four-cycles.

#### Proof

Condition (3.5) depends on `(R,F_0,i)` but, under (4.1), not on the
orientation of any pair in `R`.  Thus either every coordinate-`i` edge of
`Q_R` is selected or none is, proving (4.2).  The component classification
is the elementary Cartesian-product structure of the cube restricted to
zero, one, or two coordinate directions.  QED.

### Corollary 4 (linear component cost)

An orientation-blind residual construction whose selected graph has degree
two on `1-o(1)` of the `W=binomial(2m,m)` middle vertices has `Omega(W)`
components.  Turning those components into one row requires `Omega(W)`
edge changes or seams.

#### Proof

Every degree-two stratum component has four vertices, so the degree-two
vertices alone contribute `(1-o(1))W/4` components.  Joining `c` disjoint
cycles into `o(W)` paths or cycles changes at least `c-o(W)=Omega(W)` edges.
QED.

Thus the positive residual-reflection theorem does not by itself give a
near-width OR row.  The SCD choice must depend essentially on the orientations
of the already-split pairs.  This is not a cosmetic source of randomness:
without it, the component count is asymptotically fatal.

## 5. There is no pair-type counting obstruction

Although orientation-blind assembly fails geometrically, the number of
available colour edges in a typical pair-type stratum is asymptotically
exactly what a two-factor needs.

Let `s=|R|`.  The number of middle vertices in all strata with `s` split
pairs is

\[
 V_s=\binom ms 2^s
       \binom{m-s}{(m-s)/2}.                         \tag{5.1}
\]

The number of rank-`m-1` colours whose paired middle edge lands in those
strata is

\[
 E_s=\binom m{s-1}2^{s-1}
       \binom{m-s+1}{(m-s)/2}.                       \tag{5.2}
\]

Therefore the forced average degree is

\[
 \bar d_s=\frac{2E_s}{V_s}
          =\frac{2s}{m-s+2}.                         \tag{5.3}
\]

The pair statistic `s` of a uniform middle set is concentrated at
`m/2+O(sqrt(m))`.  In that range

\[
 \bar d_s=2+O(m^{-1/2}).                             \tag{5.4}
\]

Summing the absolute edge surplus or deficit relative to degree two over all
typical strata is `o(W)`, and the atypical strata themselves contain `o(W)`
vertices.  Thus neither rank capacity nor the fixed pair-type distribution
prevents a near two-factor.  The obstruction in Theorem 3 is specifically
the lack of orientation coherence.

## 6. Exact all-depth assembly condition

Before imposing the longer flags, the orientation-dependent depth-one
assembly can in fact be done asymptotically.  This is a useful positive
counterpoint to Theorem 3.

### Theorem 5 (fixed-pair near-linearization at depth one)

There is a spanning linear forest on the middle layer with `W-o(W)` edges
such that

* every edge flips the two members of one fixed pair `P_i`;
* its lower intersection colours are distinct;
* its upper union colours are distinct; and
* it has `o(W)` components.

Consequently its selected colour pairs are partial central matchings in the
residual incidence graphs, missing only `o(W)` lower and upper targets in
total.

#### Proof

Use two clones of every middle set.  Make a 4-uniform hypergraph whose other
two vertex classes are the rank-`m-1` and rank-`m+1` masks.  For every lower
mask `L` and every empty fixed pair `P_i`, put `U=L union P_i`; the two
intermediate middle masks are `X=L union {a_i}` and
`Y=L union {b_i}`.  Add the four clone lifts

\[
 \{L,U,X^a,Y^b\},\qquad a,b\in\{0,1\}.              \tag{6.1}
\]

A hypergraph matching projects to a middle graph of maximum degree two and
is rainbow in both colour systems.

Restrict to pair-type strata with

\[
 |s-m/2|\le m^{2/3},                                 \tag{6.2}
\]

using split count `s` for the middle masks and `s-1` for the colour masks.
Standard concentration shows that only `o(W)` vertices are discarded.
For an edge in such a stratum the exact degrees are

\[
 d(L)=d(U)=2(m-s+2),
 \qquad d(X^a)=d(Y^b)=2s.                            \tag{6.3}
\]

Thus all degrees are `(1+o(1))m`.  The maximum pair codegree is at most
four: a lower--upper pair has four clone lifts, a colour--middle-clone pair
has at most two, and two fixed middle clones determine at most one edge.

The Pippenger--Frankl--Rodl almost-perfect matching theorem therefore gives
a matching of size `W-o(W)`.  To control components, forbid projected cycles
of every fixed length at most `g`.  A fixed lifted edge lies in
`O_g(m^(j-2))` projected `j`-cycles, and fixing `l` lifted edges leaves
`O_g(m^(j-l-1))` completions.  These are exactly the power-saving conflict
degree bounds used in the cloned-hypergraph proof in
`ASYMPTOTIC_MATCHING.md`; the Delcourt--Postle conflict-free matching theorem
applies because the base degree is `Theta(m)` and the pair codegree is
constant.  Hence, for each fixed `g`, the projected matching may be chosen
with no cycle of length at most `g`.

Let `g` tend to infinity by the standard diagonal argument and delete one
edge from every remaining cycle.  Only `o(W)` edges are lost.  The result is
a forest on `W` vertices with `W-o(W)` edges, hence exactly `o(W)`
components.  Every edge still has the three asserted fixed-pair/rainbow
properties.  QED.

This theorem proves that the pair geometry itself can be assembled into
long orientation-dependent paths; Theorem 3 pinpoints why a single SCD per
unoriented split set cannot realize them.

It also gives an `o(W)`-defect radius-preserving normal form at depth one.
List the forest paths, partition their concatenated vertex lists into the
forced radius-class sizes

\[
 \binom{2m}{m-d}-\binom{2m}{m-d-1},                 \tag{6.4}
\]

and cut whenever a path or a radius class ends.  There are only `o(W)+m`
cuts.  Away from those cuts, the projected transition is a fixed-pair edge,
the assigned radius is constant, and both adjacent colours are unique.
What remains open is to replace the cut defects coherently and to impose the
longer residual-chain words below.

### Exact compatibility beyond depth one

Let

\[
 X_0,X_1,\ldots
\]

be a projected middle orbit inside one fixed pair-type stratum `(R,F_0)`,
and let `i_t in R` be the pair whose orientation is flipped from `X_t` to
`X_(t+1)`.  Suppose the orbit is assigned radius `d` and every `d`
consecutive flip indices are distinct.  Put

\[
 D_t=\{i_t,i_{t+1},\ldots,i_{t+d-1}\},
 \quad S_t=R\setminus D_t,                           \tag{6.1}
\]

and let `eta_t` be the common orientation of the pairs in `S_t` throughout
that window.  The residual ground set is

\[
 T_t=[m]\setminus S_t=([m]\setminus R)\mathbin{\dot\cup}D_t. \tag{6.2}
\]

### Proposition 6 (local flag compatibility)

The radius-`d` chain flag at `X_t` agrees with the projected window if and
only if the residual SCD `D_(S_t,eta_t)` contains the saturated segment

\[
 F_0
 \subset F_0\cup\{i_t\}
 \subset F_0\cup\{i_t,i_{t+1}\}
 \subset\cdots\subset F_0\cup D_t.                  \tag{6.3}
\]

#### Proof

The intersection of the `d+1` middle vertices in the window makes precisely
the pairs `D_t` empty; the union makes precisely those pairs full.  The
successive lower/upper labels are the flipped pair indices in chronological
order.  Theorem 1 gives exactly these endpoints and this order if and only if
(6.3) is the corresponding residual-chain segment.  QED.

Proposition 6 exposes the full recursive coupling.  Consecutive projected
windows use different residual sets `T_t` and different oriented split cores
`(S_t,eta_t)`, while their prescribed chain-label words overlap in `d-1`
positions.  Merely choosing an SCD independently for every residual cube
does not enforce those overlaps.

## 7. The sharpened successor theorem

The fixed-pair route is reduced to the following concrete target.

> **Orientation-coherent residual-SCD theorem.**  Choose an SCD
> `D_(S,eta)` of every residual Boolean lattice `B_([m]\S)` so that:
>
> 1. the central edges (3.5) form, outside `o(W)` vertices, long
>    radius-preserving cycles in every orientation cube, with only `o(W)`
>    cycles in total;
> 2. radii can be assigned with the exact SCD radius counts; and
> 3. every resulting sliding label word satisfies the residual-chain
>    condition (6.3) at all certified depths.

Condition 1 is already impossible without `eta`-dependence by Theorem 3.
Conditions 2--3 are the higher-depth coherence absent from an arbitrary
collection of cube Hamilton cycles.

A useful intermediate target is depth one: arrange the central perfect
matchings of the residual SCDs so that each typical orientation cube is one
Hamilton cycle (or `o(2^s)` cycles).  The number of pair-type strata is
exponentially smaller than `W`, so one long cycle per typical stratum would
automatically give `o(W)` total components.  Proposition 6 then states
exactly what additional structure is required to lift that depth-one object
to all ranks.

## 8. Global limitation of one fixed coordinate pairing

Even a solution of the orientation-coherent theorem for shallow depths would
not by itself reach the literal-tail depth
`Theta(sqrt(m log m))`.  The reason is a pair-type capacity obstruction,
independent of SCD choices.

For a rank-`m-q` lower target having `f` full pairs, `f+q` empty pairs, and
the remaining pairs split, the number of such targets is

\[
 T_{f,q}=
 \frac{m!}{f!(f+q)!(m-2f-q)!},2^{m-2f-q}.           \tag{8.1}
\]

Every witnessing fixed-pair window must start in a middle stratum having
`f` full pairs, `f` empty pairs, and `m-2f` split pairs.  The total number of
physical starts of that type is only

\[
 V_f=\frac{m!}{f!f!(m-2f)!},2^{m-2f}.               \tag{8.2}
\]

Thus at least

\[
 \sum_f(T_{f,q}-V_f)_+                               \tag{8.3}
\]

lower targets are missed by every construction confined to this one
coordinate pairing.  As proved in `CUBE_SHADOW_TILING.md`, when

\[
 q/\sqrt m\longrightarrow\infty,                     \tag{8.4}
\]

the quantity (8.3) is `(1-o(1)) binomial(2m,m-q)`.

Therefore residual SCDs solve the exact **pairing** of lower and upper target
types, but cannot create absent physical starts.  At the depth needed to
make literal tails negligible, a successful construction must mix many
different coordinate pairings (or leave the fixed-pair architecture).  The
positive depth-one theorem and the orientation-coherence reduction should be
viewed as local modules for that multi-pairing reservoir, not as a complete
single-pairing solution.
