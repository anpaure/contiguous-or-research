# Adjacent necklaces: every smaller-gap move has an odd circulation blossom

**Date:** 2026-08-05  
**Method:** a literal chip circulation around the odd coordinate cycle; no
computation  
**Status:** unconditional local lift.  It supplies the cross-base
interaction missing from the exit-only full-merge fibres.  Simultaneous
collision-free packing of many such blossoms is not proved here.

## 1. The local shifted-cut move

Let `q>=3` be odd and let

\[
                    x\in\mathbb Z_{\ge0}^{\mathbb Z_q}.
\]

Suppose, at three consecutive coordinates `c,c+1,c+2`, that

\[
                         (x_c,x_{c+1},x_{c+2})=(2,0,1).       \tag{1.1}
\]

Put

\[
 y=x-e_c+2e_{c+1}-e_{c+2},
 \qquad
 w=x-e_c+e_{c+1}.                                    \tag{1.2}
\]

Locally,

\[
              x:(2,0,1),\qquad
              w:(1,1,1),\qquad
              y:(1,2,0).                              \tag{1.3}
\]

Thus `x-w-y` is the two-edge route which moves a shifted-quiet cut one
coordinate to the right.

When `x` belongs to the all-one full-merge fibre, `x` has a selected cut at
`c`.  If replacing that cut by `c+1` remains admissible, then the resulting
critical state is exactly `y`.

## 2. The counter-circulation path

Define

\[
 v_0=x,
 \qquad
 v_t=x-e_c+e_{c-t}quad(1\le t\le q-1),               \tag{2.1}
\]

with indices modulo `q`.  Since `c-(q-1)=c+1`,

\[
                             v_{q-1}=w.               \tag{2.2}
\]

### Lemma 2.1 (literal simple path)

The sequence

\[
                    v_0-v_1-\cdots-v_{q-1}            \tag{2.3}
\]

is a simple path of legal adjacent unit transfers.

#### Proof

The first move sends one of the two chips at `c` to `c-1`.  At every later
step, the travelling chip is sent from `c-t+1` to `c-t`.  Its current
coordinate contains its original nonnegative load plus the travelling
chip, so every transfer is legal.  Formula (2.1) shows that the positive
anomaly occupies a different coordinate at every internal step, while the
negative anomaly remains at `c`.  Hence the vertices are distinct.
\(\square\)

There is also the direct edge `v_0 v_(q-1)=xw`, obtained by moving one chip
from `c` to `c+1`.

### Theorem 2.2 (odd circulation blossom)

The vertices

\[
                   v_0,v_1,\ldots,v_{q-1}             \tag{2.4}
\]

span a literal cycle of length `q`.  It is odd.  The vertex `y` is joined
to the cycle vertex `w=v_(q-1)` by the literal edge `wy`.

The resulting blossom-plus-tail graph has a perfect matching.

#### Proof

Lemma 2.1 supplies `q-1` consecutive cycle edges and `xw` closes the
cycle.  Oddness is exactly the hypothesis that `q` is odd.  The edge `wy`
moves the unit at `c+2` into `c+1`, as displayed in (1.3).

Match `w` to `y`.  Deleting `w` from the odd cycle leaves the even path

\[
                     v_0-v_1-\cdots-v_{q-2},
\]

which is perfectly matched by

\[
             v_0v_1,\ v_2v_3,\ldots,\ v_{q-3}v_{q-2}.
\]

Together with `wy`, these edges cover every vertex. \(\square\)

The direct route `x-w-y` has even length, while the counter-circulation
route `x-v_1-...-w-y` has odd length `q`.  Their parity difference is the
precise blossom resource absent from the exit-only bipartite fibre.

## 3. Identification with the smaller gap graph

Let an all-one full-merge cut set have cyclically ordered centres

\[
                     \cdots,p,c,n,\cdots
\]

and cyclic gaps

\[
                     g_-=c-p,\qquad g_+=n-c.
\]

Assume `c+1` is still admissible, equivalently `g_+>=4`.  Moving the cut
from `c` to `c+1` changes

\[
                   (g_-,g_+)\longmapsto(g_-+1,g_+-1). \tag{3.1}
\]

After subtracting the mandatory gap three,

\[
                   e_i=g_i-3,
\]

equation (3.1) is exactly one adjacent unit transfer

\[
                   (e_-,e_+)\longmapsto(e_-+1,e_+-1) \tag{3.2}
\]

in the smaller weak-composition necklace graph

\[
                           G_{k,q-3k}.                \tag{3.3}
\]

### Corollary 3.1 (odd blossom lift of every horizontal edge)

Every literal adjacent edge of the smaller gap graph (3.3) lifts, before
rotation quotienting, to a blossom-plus-tail subgraph of the ambient
`q`-coordinate adjacent-composition graph.  Both critical endpoints of the
smaller edge occur as the two tail endpoints `x` and `y`, and the lift has
a perfect matching.

Thus the smaller layers identified in the full-merge theorem are not only
set-theoretic.  Their horizontal adjacency has an explicit ambient
interacting realization.

## 4. Schur-complement interpretation

Suppose the internal vertices of the odd cycle are eliminated by a skew
Gaussian or discrete-Morse step while `x` and `y` are retained as critical
ports.  The direct and counter-circulation routes have opposite parity.
Their union is an odd blossom, so the effective critical relation is not
constrained by the bipartition of the first-order exit-toggle graph.

This explains how an interacting skew operator can evade the two earlier
obstructions:

1. the free Fourier current cancels opposite one-particle momenta; and
2. the exit-only full-merge fibre has shore imbalance two at `q=15`.

The circulation blossom uses a configuration-dependent long route.  It is
not a quadratic one-particle hopping specialization.

## 5. Quotient and packing boundary

The construction is rotation-equivariant at the level of pointed data
`(x,c)`: rotating both the state and the selected cut rotates the whole
blossom.  There is an exact collision classification within one cut level.

For a `k`-cut state `x=x_S`, call

\[
                         h(x,c)=x_{S\setminus\{c\}}  \tag{5.1}
\]

the **hub** of the horizontal edge which shifts `c` to `c+1`.  It is the
state `w` in (1.2), viewed as the `(k-1)`-cut segmentation obtained by
fully merging that cut.

### Lemma 5.1 (fixed-level interior injectivity)

Fix `k`.  For all pointed movable cuts `(x_S,c)` with `|S|=k`, the
nonhub circulation vertices

\[
                    x_S-e_c+e_r,
                    \qquad r\ne c,c+1,               \tag{5.2}
\]

are injective in the pointed data `(S,c,r)`.  They are also disjoint from
every critical cut state and every hub state.

The same assertion holds modulo rotation: two nonhub vertices lie in the
same necklace orbit only when their pointed data lie in the same rotation
orbit.

#### Proof

In a cut state, every zero is preceded by a terminal two.  In (5.2), the
zero at `c+1` remains, while its predecessor has changed from two to one.
No other zero has predecessor one: it either retains predecessor two, is
filled by the travelling chip, or has its predecessor raised from two to
three.  Hence the nonhub state recovers `c` as the unique coordinate
immediately preceding a zero by a one.

After `c` is known, suppose

\[
 x_S-e_c+e_r=x_T-e_c+e_{r'},
 \qquad |S|=|T|=k.                                  \tag{5.3}
\]

Then `x_T-x_S=e_r-e_(r')`.  Write

\[
 x_S={\bf1}+\sum_{j\in S}(e_j-e_{j+1}),
 \qquad
 a_j={\bf1}_T(j)-{\bf1}_S(j).                       \tag{5.4}
\]

Comparing coordinates in

\[
 \sum_j a_j(e_j-e_{j+1})=e_r-e_{r'}                \tag{5.5}
\]

shows that the cyclic sequence `(a_j)` is constant except for one upward
and one downward jump.  Hence its nonzero support, after possibly changing
all signs, is one cyclic interval on which every coefficient is one.
If that interval had length at least two, either `S` or `T` would contain
two adjacent cuts, contrary to admissibility.  Thus a nonzero interval has
length one, which changes the cut cardinality by one.  Since `|S|=|T|`,
the interval must be empty.  Therefore `S=T` and then `r=r'`.

Every critical or hub state has all zeroes preceded by two, whereas (5.2)
has the distinguished zero preceded by one.  This proves disjointness.
All characterizations are rotation-equivariant, giving the orbit version.
\(\square\)

The fixed-level hypothesis is sharp.  A travelling chip may fill the zero
of an extra cut and thereby identify an interior state coming from the
next cut level.  Horizontal layers must therefore be packed one level at
a time, or assigned disjoint phase banks.

For each selected simple quotient edge, choose one rotation orbit of its
pointed cut-shift occurrences.  Call this occurrence-labelled matching of
horizontal smaller-gap edges **hub-rainbow** when no two chosen occurrences
have the same `(k-1)`-cut hub orbit.

### Theorem 5.2 (hub-rainbow blossom packing)

Every hub-rainbow matching in the necklace graph `G_(k,q-3k)` lifts to a
vertex-disjoint family of perfectly matchable circulation
blossom-plus-tail gadgets in the ambient adjacent-necklace graph.

#### Proof

Matching disjointness separates the critical tail endpoints.  The
hub-rainbow condition separates the hub vertices.  Lemma 5.1 separates all
remaining circulation vertices, both literally and after taking rotation
orbits.  Theorem 2.2 perfectly matches each gadget.  Their union is
therefore a matching-disjoint bank. \(\square\)

Consequently the unresolved packing problem is not arbitrary orbit
collision.  It is the explicit rainbow problem

\[
 \boxed{
 \text{pair the residual same-shore monomers by horizontal edges whose
 deleted-cut hubs are distinct.}}                    \tag{5.6}
\]

There can be several horizontal edges over one hub, so an arbitrary
matching of the smaller graph need not be hub-rainbow.  Therefore the
following stronger statement is still **not** asserted:

> an arbitrary matching of the smaller graph lifts to a vertex-disjoint
> matching bank of circulation blossoms in the simple necklace quotient.

That is now the exact remaining rainbow theorem.  Any one of the
following would suffice:

1. a hub-rainbow horizontal bank pairing the residual monomers left by the
   vertical exit toggles;
2. a serial alternating-path theorem showing that overlapping blossoms can
   be applied without increasing the monomer count; or
3. a protected-minor argument for the union of their interior matching
   blocks.

## 6. The q=15 obstruction is closed by two blossoms

The full-merge theorem found shore imbalance two in the all-one fibre at
`q=15`.  The circulation lift repairs that exact example.

Write the ten three-cut gap necklaces of mass six as

\[
\begin{array}{llll}
A_0=(6,0,0),&A_1=(5,1,0),&\bar A_1=(5,0,1),\\
A_2=(4,2,0),&\bar A_2=(4,0,2),&A_3=(4,1,1),\\
A_4=(3,3,0),&A_5=(3,2,1),&\bar A_5=(3,1,2),
&A_6=(2,2,2).
\end{array}                                          \tag{6.1}
\]

The five two-cut necklaces are

\[
                    B_j=[9-j,j],\qquad0\le j\le4,    \tag{6.2}
\]

and the five four-cut necklaces are

\[
\begin{aligned}
C_0&=(3,0,0,0),&C_1&=(2,1,0,0),&C_2&=(2,0,1,0),\\
C_3&=(2,0,0,1),&C_4&=(1,1,1,0).
\end{aligned}                                       \tag{6.3}
\]

Let `R` and `Z` denote the unique one-cut and five-cut vertices.

Choose the two horizontal edges

\[
                         A_0A_1,qquad A_6A_5.        \tag{6.4}
\]

They are literal adjacent gap transfers

\[
             (6,0,0)\leftrightarrow(5,1,0),
 \qquad
             (2,2,2)\leftrightarrow(3,2,1).          \tag{6.5}
\]

Their deleted-cut hubs are respectively

\[
                              B_0=[9,0],
 \qquad                       B_2=[7,2],              \tag{6.6}
\]

so they are hub-rainbow.  Lift them by Theorem 5.2 and use the perfect
matching inside each blossom-plus-tail.

Match all remaining critical vertices vertically by

\[
\begin{array}{llll}
R-B_1,& Z-C_0,\\
B_3-A_4,&B_4-A_3,\\
C_1-\bar A_2,&C_2-A_2,&C_3-\bar A_5,&C_4-\bar A_1.
\end{array}                                          \tag{6.7}
\]

Every edge in (6.7) deletes one cut.  In gap coordinates, deletion replaces
two adjacent parts `u,v` by `u+v+3`.  This directly verifies all eight
incidences.  For example,

\[
 (2,1,0,0)\longmapsto(2,4,0)\sim(4,0,2)=\bar A_2,
\]

and

\[
 (2,0,0,1)\longmapsto(2,3,1)\sim(3,1,2)=\bar A_5.
\]

### Theorem 6.1 (exact q=15 critical closure)

The `q=15` all-one full-merge critical fibre, together with the interiors
of the two circulation blossoms (6.4), has a perfect matching.  The two
blossoms are vertex-disjoint, and every remaining critical vertex occurs
in exactly one edge of (6.7).

#### Proof

The horizontal edges have disjoint endpoints and distinct hubs, so
Theorem 5.2 makes their lifted gadgets vertex-disjoint and perfectly
matchable.  They consume

\[
                A_0,A_1,A_5,A_6,B_0,B_2.            \tag{6.8}
\]

The eight edges in (6.7) use every other vertex in (6.1)--(6.3), together
with `R,Z`, exactly once.  They are disjoint from the nonhub blossom
interiors by Lemma 5.1. \(\square\)

This theorem is a calibration, not the general rainbow induction.  It
shows that the first exact parity obstruction to exit-only matching is
repaired by precisely the cross-base interacting term developed here.
It also assumes that the two circulation interiors have not already been
committed by an earlier ambient matching stage.

## 7. Scope

Proved:

1. an explicit odd cycle through every movable all-one cut;
2. a perfectly matchable blossom-plus-tail joining the two shifted
   critical states;
3. exact identification of the shift with an adjacent move in
   `G_(k,q-3k)`;
4. exact fixed-level collision classification and hub-rainbow packing; and
5. exact closure of the first deficiency-two fibre at `q=15`.

Not proved:

1. existence of the required hub-rainbow residual-monomer bank;
2. global near-perfect matching of all shifted-quiet critical necklaces;
3. protected radial sockets; or
4. any universal-word upper bound.
