# Gate C: an explicit one-to-two product-atom absorber

**Status (2026-08-22).**  Everything in this note is proved.  For every
odd `b=2h+1>=7` it constructs three genuine all-split product atoms
`E_0,E_1,E_2` and a structured packet `P` of `b^2` middle vertices such
that

\[
                   E_0\mathbin{\dot\cup}E_2
                   =E_1\mathbin{\dot\cup}P.             \tag{0.1}
\]

Consequently, if a matching contains `E_1` and leaves `P` uncovered, the
single atom `E_1` can be replaced by the two disjoint atoms `E_0,E_2`,
covering the whole packet and increasing the matching by one atom.  The
packet has exactly the coordinate residues required of `b^2` additional
covered vertices.  Taking the gadget together with its complement gives a
complement-symmetric, prime-residue-safe two-to-four absorber.

This is not yet a Gate-C near-factor.  The remaining global problem is now
sharply stated: arrange a preliminary matching so that it contains many
trigger atoms `E_1` and its leave is a disjoint union, up to `o(W)`, of the
corresponding packets `P`.  No independent-survival assertion is made.

## 1. A local deck identity

Let

\[
                       b=2h+1,\qquad h\ge3,
\]

and label a `b`-set by

\[
                        A=\{0,1,\ldots,2h\}.
\]

For a cyclic order `alpha` on `A`, write

\[
 \mathcal D(\alpha)=
 \{I_\alpha(i,h):i\in\mathbb Z_b\}                    \tag{1.1}
\]

for its deck of cyclic `h`-intervals.  Put

\[
 w=h-1,\qquad u=2h-1,\qquad v=2h,                     \tag{1.2}
\]

and define three cyclic orders

\[
\begin{aligned}
 \alpha_0&=(0,1,\ldots,2h),\\
 \alpha_1&=(0,1,\ldots,2h-2,v,u),\\
 \alpha_2&=(u,h-2,h-3,\ldots,0,
                 h,h+1,\ldots,2h-2,v,w).
\end{aligned}                                         \tag{1.3}
\]

Thus `alpha_1` is obtained from `alpha_0` by swapping its last two
entries.  Write

\[
                    \mathcal D_i=\mathcal D(\alpha_i)
                    \quad(i=0,1,2).                   \tag{1.4}
\]

### Lemma 1.1 (the adjacent-swap fringe)

Let

\[
 L=\{0,1,\ldots,h-2\},\qquad
 M=\{h,h+1,\ldots,2h-2\},                             \tag{1.5}
\]

and put

\[
 A_*=L\cup\{v\},\quad B_*=M\cup\{u\},\quad
 X=L\cup\{u\},\quad Y=M\cup\{v\}.                  \tag{1.6}
\]

Then

\[
 \mathcal D_0-\mathcal D_1=\{A_*,B_*\},
 \qquad
 \mathcal D_1-\mathcal D_0=\{X,Y\}.                 \tag{1.7}
\]

#### Proof

A cyclic `h`-interval is unchanged as a set by the transposition of the
adjacent entries `u,v` unless it contains exactly one of those two
positions.  There are exactly two such intervals, one across each boundary
between the transposed positions and the rest of the cycle.  Reading those
two intervals before and after the swap gives precisely the four sets in
(1.6).  \(\square\)

### Lemma 1.2 (a disjoint deck containing the new fringe)

The deck `mathcal D_2` contains `X,Y` and is disjoint from `mathcal D_0`.
Consequently

\[
                         \mathcal D_1
                         \subseteq\mathcal D_0\cup\mathcal D_2.   \tag{1.8}
\]

#### Proof

In `alpha_2`, its first `h` entries form `X` and its next `h` entries form
`Y`, so both belong to `mathcal D_2`.  It remains to prove disjointness.

The starts of the cyclic `h`-windows of `alpha_2` give the following
complete list.  Besides `X` and `Y`, a start `a` positions into the first
block, where `1<=a<=h-1`, gives

\[
 C_a=\{0,\ldots,h-a-1\}\cup\{h,\ldots,h+a-1\}.       \tag{1.9}
\]

This has two nonempty components in the natural cyclic order `alpha_0`.
A start `a` positions into the second block gives, for `2<=a<=h-1`,

\[
 D_a=\{h-a+1,\ldots,h-1\}\cup\{h+a,\ldots,2h\},     \tag{1.10}
\]

again with two nonempty natural cyclic components.  For `a=1`, the window
is

\[
 D_1=\{w,v\}\cup\{h+1,\ldots,2h-2\},                \tag{1.11}
\]

which omits `u` between `2h-2` and `v` and is not a natural interval.  The
window starting at the final entry `w` is

\[
                         \{1,2,\ldots,h-1,u\},         \tag{1.12}
\]

also disconnected in the natural cycle.  Finally, `X` and `Y` themselves
are obtained from the natural intervals `A_*` and `B_*` by exchanging
`u,v`, so neither is in `mathcal D_0`.  Thus no member of `mathcal D_2`
belongs to `mathcal D_0`.

Equation (1.8) now follows from Lemma 1.1 and the inclusion
`{X,Y} subset mathcal D_2`.  \(\square\)

Define the residual local packet

\[
 \mathcal R=(\mathcal D_0\mathbin{\dot\cup}\mathcal D_2)
                         -\mathcal D_1.                \tag{1.13}
\]

The dot is justified by Lemma 1.2.  Equations (1.8) and (1.13) give the
exact disjoint identity

\[
 \boxed{
 \mathcal D_0\mathbin{\dot\cup}\mathcal D_2
 =\mathcal D_1\mathbin{\dot\cup}\mathcal R,
 \qquad |\mathcal R|=b.}                              \tag{1.14}
\]

### Lemma 1.3 (the residual packet is regular but is not a wreath deck)

Every coordinate of `A` belongs to exactly `h` members of `mathcal R`.
For `h>=3`, there is no cyclic order `gamma` on `A` such that
`mathcal R=mathcal D(gamma)`.

#### Proof

Every coordinate belongs to exactly `h` members of every cyclic
`h`-interval deck.  Taking coordinate degrees in (1.14) therefore gives

\[
                         2h=h+\deg_{\mathcal R}(x),
\]

and proves regularity.

For the second assertion, recall the elementary pair census of a cyclic
`h`-deck on `2h+1` labels: two labels at cyclic distance `d<=h` belong
together to exactly `h-d` deck members.  In particular, every label has
exactly two partners of pair-codegree `h-1`, namely its two cyclic
neighbours.

We show that `u` has only one such partner in `mathcal R`.  Lemmas 1.1--1.2
give

\[
 \mathcal R=\{A_*,B_*\}\mathbin{\dot\cup}
               (\mathcal D_2-\{X,Y\}).                \tag{1.15}
\]

In `alpha_2`, the two cyclic neighbours of `u` are `w` and `h-2`.
The set `X` contains `u,h-2` but not `w`; the set `B_*` contains `u` but
neither `w` nor `h-2`; and `A_*,Y` do not contain `u`.  Hence the
`mathcal R`-codegrees of `(u,w)` and `(u,h-2)` are respectively `h-1` and
`h-2`.

The only labels at cyclic distance two from `u` in `alpha_2` are `v` and
`h-3`.  The first receives no added incidence from `B_*`, while the second
lies in the removed set `X`.  Their residual codegrees are at most `h-2`.
Every other label has `mathcal D_2`-codegree at most `h-3`, and (1.15) can
add at most one, so its residual codegree is also at most `h-2`.  Thus `w`
is the unique partner of `u` with codegree `h-1`, which is impossible in a
cyclic deck.  \(\square\)

The non-wreath conclusion matters: from `b=7` onward the packet in (1.14)
is not merely a fourth atom hidden under different notation.  For `b=5`,
the analogous residual happens to be a cyclic deck and the identity
degenerates to an ordinary two-by-two wreath trade.

## 2. Lifting the identity to product atoms

Let `B` be a `b`-set disjoint from `A`, fix any cyclic order `beta` on it,
and write

\[
 \mathcal Y=\{I_\beta(j,h+1):j\in\mathbb Z_b\}.        \tag{2.1}
\]

For families `mathcal X subseteq binom(A,h)` and
`mathcal Z subseteq binom(B,h+1)`, use the Cartesian-union notation

\[
 \mathcal X\boxtimes\mathcal Z
 =\{X\cup Z:X\in\mathcal X,\ Z\in\mathcal Z\}.       \tag{2.2}
\]

Intersection with `A,B` recovers the two factors, so the map in (2.2) is
injective and respects disjoint unions in either factor.

Put

\[
 E_i=\mathcal D_i\boxtimes\mathcal Y\quad(i=0,1,2),
 \qquad
 P=\mathcal R\boxtimes\mathcal Y.                    \tag{2.3}
\]

Each `E_i` is a genuine all-split product atom of size `b^2`, while `P` is
a packet of `b^2` distinct middle vertices.

### Theorem 2.1 (one-to-two product-atom absorber)

The atoms `E_0,E_2` are disjoint, the packet `P` is disjoint from `E_1`,
and

\[
 \boxed{
                  E_0\mathbin{\dot\cup}E_2
                  =E_1\mathbin{\dot\cup}P.}           \tag{2.4}
\]

Hence, if an atom matching `mathcal M` contains `E_1` and no vertex of
`P`, then

\[
            (\mathcal M-\{E_1\})\cup\{E_0,E_2\}       \tag{2.5}
\]

is an atom matching which covers every vertex formerly covered by
`mathcal M` and also all `b^2` vertices of `P`.

#### Proof

Apply the injective Cartesian lift (2.2) to the disjoint local identity
(1.14).  This gives every disjointness assertion and (2.4).  In (2.5), the
new atoms have union `E_1 dotcup P`; both pieces are disjoint from all
unchanged atoms by the hypotheses.  \(\square\)

This theorem is monotone: the switch releases no previously covered
vertex.  It increases the number of atoms by one and decreases the leave by
exactly `b^2` vertices.

## 3. Lattice and complement compatibility

### Proposition 3.1 (the packet has the exact atom residue profile)

For every `a in A` and `z in B`,

\[
 \deg_P(a)=bh,
 \qquad
 \deg_P(z)=b(h+1).                                    \tag{3.1}
\]

In particular every coordinate degree in `P` is divisible by `b`.

#### Proof

Lemma 1.3 gives `deg_mathcal R(a)=h`, and every member of `mathcal R` can
be paired with all `b` members of `mathcal Y`.  Conversely every coordinate
of `B` lies in `h+1` members of `mathcal Y`, each paired with all `b`
members of `mathcal R`.  This proves (3.1).  \(\square\)

Thus the absorber does not fight the coordinate congruence obstruction: it
absorbs exactly one atom-sized lattice packet.

For a family `mathcal F subseteq binom(A union B,b)`, write

\[
 \overline{\mathcal F}
 =\{(A\cup B)-S:S\in\mathcal F\}.                    \tag{3.2}
\]

The complement of a product atom is again a product atom, with the two
blocks exchanged and both local interval decks complemented.  Every member
of `E_i` has `h` points in `A`, while every member of `overline{E_i}` has
`h+1` points in `A`; hence these families are disjoint.  The same holds for
`P,overline P`.

### Corollary 3.2 (complement-symmetric two-to-four absorber)

The two matchings

\[
 \{E_1,\overline{E_1}\}
 \quad\hbox{and}\quad
 \{E_0,E_2,\overline{E_0},\overline{E_2}\}            \tag{3.3}
\]

satisfy the disjoint identity

\[
 E_0\dot\cup E_2\dot\cup\overline{E_0}\dot\cup
 \overline{E_2}
 =E_1\dot\cup\overline{E_1}\dot\cup
   P\dot\cup\overline P.                             \tag{3.4}
\]

Therefore a complement-closed leave containing
`P dotcup overline P` can be reduced by `2b^2` vertices without breaking
complement symmetry.  This is compatible with the prime-`b` requirement
that a two-vertex terminal leave, if reached, consist of a complementary
pair.

## 4. The remaining coordinated-packing condition

Call a collection of absorber placements **compatible** if all domains

\[
                         E_1\mathbin{\dot\cup}P        \tag{4.1}
\]

are pairwise disjoint.  Theorem 2.1 immediately gives the following exact
reduction.

### Corollary 4.1 (packet-reservoir reduction)

Suppose an initial atom matching contains the trigger `E_1` from each of
`q` compatible placements, leaves all corresponding packets uncovered, and
has total leave size `L` (including those packets).  Switching all `q`
absorbers produces a matching whose leave has size exactly

\[
                              L-qb^2.                 \tag{4.2}
\]

In particular, a Gate-C near-factor follows if one can coordinately build a
matching whose leave, apart from `o(W)` vertices, is tiled by compatible
packets and whose trigger atoms are all present.

The word *coordinately* is essential.  A packet has `b^2` vertices, so an
independently thinned residual would preserve a prescribed packet with
probability of order `x^(b^2)`.  The theorem supplies an exact absorber and
its correct algebraic interface; it does not revive the ruled-out
independent-residual nibble.

## 5. The packet orbit and an unconditional absorber atlas

Let `k=b^2`, fix one placement of Theorem 2.1, and retain permutation
labels in the full symmetric-group orbits

\[
 \mathfrak P=\{gP:g\in\operatorname{Sym}(A\cup B)\},
 \qquad
 \mathfrak D=\{g(E_1\dot\cup P):g\in\operatorname{Sym}(A\cup B)\}.
                                                               \tag{5.1}
\]

Thus members of `mathfrak P` have size `k`, while members of `mathfrak D`
have size `2k`.  Repeated labelled copies are allowed in the incidence
counts, exactly as for the all-split atom hypergraph.

### Proposition 5.1 (no fractional packet-orbit obstruction)

The labelled packet-orbit hypergraph is regular.  Uniform weight on its
labelled packets is a fractional perfect matching of total weight `W/k`,
where

\[
                         W={2b\choose b}.              \tag{5.2}
\]

#### Proof

The symmetric group is transitive on the middle layer and preserves the
labelled orbit, so every middle vertex has one common packet degree
`D_P`.  Double-counting incidences gives

\[
                   |\mathfrak P|k=WD_P.
\]

Weight `1/D_P` on every labelled packet covers each vertex fractionally
once and has total weight `|mathfrak P|/D_P=W/k`.  \(\square\)

This is only a fractional statement.  In particular it does not say that
an arbitrary leave can be tiled by packets.

### Theorem 5.2 (an unconditional disjoint binary atlas)

There is a compatible collection of absorber placements of cardinality

\[
                         q\ge {W\over4k^2}.             \tag{5.3}
\]

Its `q` packets are pairwise disjoint and contain at least

\[
                         qk\ge {W\over4k}
                             ={W\over4b^2}              \tag{5.4}
\]

vertices.  Starting with all `q` triggers, every one of the `2^q` subunions
of these packets can be absorbed independently.

#### Proof

Choose a maximal pairwise-disjoint subfamily of the labelled domain orbit
`mathfrak D`, and let its size be `q`.  If `N=|mathfrak D|` and `D_D` is
the common domain degree, then

\[
                         2kN=WD_D.                     \tag{5.5}
\]

Maximality says that every labelled domain meets the union `U` of the
chosen domains.  Counting a domain once for every possible intersection
vertex gives

\[
 N\le |U|D_D=(2kq)D_D.
\]

Substitution from (5.5) yields `q>=W/(4k^2)`.  The chosen domains are
disjoint, so their trigger atoms and packets form compatible placements.
For any index subset, use the two-atom state on those domains and the
one-atom trigger state on all other domains.  The domains are disjoint, so
these choices form a matching and absorb exactly the selected packet
subunion.  \(\square\)

Theorem 5.2 is a genuine but deliberately modest capacity guarantee.  It
provides a structured reservoir of size `Omega(W/b^2)`; it does not prove
that every residue-compatible set of that size, let alone every `o(W)`
set, is representable by its packets.

Applying the same argument to the complement-doubled domains in Corollary
3.2 gives a complement-symmetric atlas with at least

\[
                         {W\over16k^2}                 \tag{5.6}
\]

binary switches and complement-closed packet capacity at least `W/(8k)`.

There is also an exact linear-span restriction on every one-block packet
atlas.  Let `J` be the coordinate-versus-local-vertex incidence map

\[
 J:\mathbb Q^{\binom Ah}\longrightarrow\mathbb Q^A,
 \qquad
 (Jz)_a=\sum_{S\ni a}z_S.                             \tag{5.7}
\]

### Proposition 5.3 (balanced-marginal span obstruction)

The rational orbit spans of both `mathcal R` and `mathcal Q` are contained
in

\[
 \mathcal B=
 \{z:(Jz)_a\text{ is independent of }a\in A\},        \tag{5.8}
\]

which has codimension `b-1` in `mathbb Q^(binom(A,h))`.

#### Proof

Lemma 1.3 gives

\[
 J\mathbf1_{g\mathcal R}=h\mathbf1_A
 \quad\text{for every }g\in\operatorname{Sym}(A).
\]

Likewise `mathcal Q` is the disjoint union of two cyclic decks, so
`J mathbf1_(g mathcal Q)=2h mathbf1_A`.  Linearity proves containment in
(5.8).

The map `J` has row rank `b` over the rationals.  Indeed, if coefficients
`c_a` satisfy `sum_(a in S)c_a=0` for every `h`-set `S`, comparing two
sets which differ by exchanging `a,a'` shows `c_a=c_(a')`; then any one
`h`-set forces the common value to be zero.  Requiring `Jz` to lie in the
one-dimensional constant subspace therefore imposes `b-1` independent
linear conditions.  \(\square\)

Thus even rational packet combinations cannot realize an arbitrary local
leave.  A fixed-split packet atlas must be aimed at a leave with balanced
local coordinate marginals (or be supplemented by packets from other
splits).  Proposition 5.3 is a necessary span condition, not a claim that
every balanced vector belongs to the orbit span.

## 6. Exact packet-cover and flow conditions

The absorber converts the remaining global question into a colored packet
matching problem without any probabilistic conditioning.

Let `mathcal M` be an atom matching with leave `H`.  An eligible placement
is one whose trigger `T` lies in `mathcal M` and whose packet `P_T` is a
subset of `H`.  Regard `P_T` as a `k`-edge colored by the trigger atom `T`.

### Theorem 6.1 (rainbow packet-cover criterion)

Let `mathcal Q` be a family of eligible placements such that

1. their packets are pairwise disjoint; and
2. their trigger colors are pairwise distinct.

Then all placements in `mathcal Q` can be switched simultaneously.  The
result is an atom matching whose newly covered set is exactly

\[
                         \mathop{\dot\bigcup}_{Q\in\mathcal Q}P_Q. \tag{6.1}
\]

#### Proof

Distinct triggers are members of the matching `mathcal M`, hence are
pairwise disjoint.  Every packet lies in the leave, so it is disjoint from
every trigger, including triggers belonging to other placements.  Together
with packet disjointness, the absorber domains are therefore pairwise
disjoint.  Apply Theorem 2.1 independently on every domain.  \(\square\)

There is a useful ordinary-flow specialization.  Suppose a desired part
`H_0 subseteq H` is already partitioned into candidate packets

\[
                         H_0=P_1\dot\cup\cdots\dot\cup P_s.        \tag{6.2}
\]

Make a bipartite graph with the packet blocks `P_i` on the left and the
trigger atoms of `mathcal M` on the right; join `P_i` to `T` precisely when
`(T,P_i)` is a placement of Theorem 2.1.

### Corollary 6.2 (Hall/flow reduction)

All of the fixed packet blocks in (6.2) can be absorbed simultaneously by
these placements if and only if this bipartite graph has a matching
saturating its packet side.  Equivalently, it is enough and necessary that

\[
                         |N(\mathcal X)|\ge|\mathcal X|
 \quad\text{for every packet subfamily }\mathcal X.   \tag{6.3}
\]

#### Proof

A saturating matching assigns distinct triggers to the disjoint packets,
so Theorem 6.1 applies.  Conversely, simultaneous use of these fixed packet
blocks must assign a distinct trigger to each block, which is exactly such
a bipartite matching.  The equivalence with (6.3) is the elementary Hall
criterion.  \(\square\)

Thus a complete positive Gate-C proof may target two explicit objects:

- a packet atlas which tiles the eventual structured leave; and
- a trigger-to-packet bipartite graph satisfying (6.3).

Theorem 5.2 supplies a nontrivial disjoint atlas, but not the required
near-spanning atlas or Hall expansion.  Those are the remaining global
conditions; no atlas-coverage claim is hidden in the local absorber.

## 7. Exact audit of the one-block packet orbits

The families `mathcal R` and

\[
                         \mathcal Q=\mathcal D_0\dot\cup\mathcal D_2
                                                               \tag{7.1}
\]

have only `b` and `2b` local vertices.  Their induced
Johnson-distance-one graphs are sparse: `mathcal R` has maximum degree two,
and `mathcal Q` has maximum degree five.  It is tempting to infer an
`O(b^(-2))` orbit codegree and apply a one-block nibble.  The inference is
false because the opposite Johnson shell, distance `h`, has only `h+1`
possible neighbours.

We record the exact calculation.  Let

\[
                         \mathcal U={A\choose h},
 \qquad
 N_d={h\choose d}{h+1\choose d}.                     \tag{7.2}
\]

Thus `N_d` is the number of local `h`-sets at Johnson distance `d` from a
fixed local `h`-set.  For a family `mathcal F subseteq mathcal U`, put

\[
 m_d(\mathcal F)=
 |\{(S,T)\in\mathcal F^2:S\ne T,\ |S-T|=d\}|.         \tag{7.3}
\]

Retain all permutation labels in the `Sym(A)` orbit hypergraph of
`mathcal F`.  Let `D_F` be its vertex degree and `Lambda_(d,F)` its pair
codegree at distance `d`.

### Lemma 7.1 (orbit codegree identity)

For every `1<=d<=h`,

\[
 {\Lambda_{d,F}\over D_F}
 = {m_d(\mathcal F)/|\mathcal F|\over N_d}.            \tag{7.4}
\]

#### Proof

The symmetric group is transitive on local vertices and on ordered pairs
at each fixed Johnson distance.  Count triples consisting of a labelled
orbit member containing a fixed first vertex and a second vertex at
distance `d`.  Averaging over the possible preimages of the first vertex
inside `mathcal F` gives `m_d(mathcal F)/|mathcal F|`; counting instead by
the `N_d` possible second vertices gives
`N_d Lambda_(d,F)/D_F`.  Equating the two expressions proves (7.4).
\(\square\)

### Lemma 7.2 (the two boundary censuses)

For `h>=3`,

\[
\begin{array}{c|cc}
 &\text{unordered distance-1 pairs}&
   \text{unordered distance-}h\text{ pairs}\\ \hline
 \mathcal R&b-2&b-2\\
 \mathcal Q&2b+17&2b+3.
\end{array}                                           \tag{7.5}
\]

Moreover the distance-one maximum degrees are at most two in `mathcal R`
and at most five in `mathcal Q`.

#### Proof

Within either cyclic deck `mathcal D_0` or `mathcal D_2`, both the
distance-one graph and the distance-`h` graph are `b`-cycles: the relevant
start shifts are respectively `+-1` and `+-h` modulo `b`.

For distance `h`, there are exactly three cross pairs between
`mathcal D_0` and `mathcal D_2`.  In start-index notation `(i,j)`, with
the first index belonging to `mathcal D_0`, they are

\[
                         (0,h),\qquad(h-1,0),\qquad(h+1,1).        \tag{7.6}
\]

This follows immediately by substituting the window list
(1.9)--(1.12); every other cross pair has a common point.  The two internal
cycles contribute `2b` unordered pairs, proving the bottom-right entry of
(7.5).

For `mathcal R`, equation (1.15) removes the adjacent vertices `X,Y` from
the distance-`h` cycle of `mathcal D_2`.  The remaining path has `b-3`
edges.  The added sets `A_*,B_*` are disjoint from each other, while
neither is disjoint from any remaining `mathcal D_2` member: their
`mathcal D_0` start indices are `2h,h`, neither of which occurs as a first
coordinate in (7.6).  They therefore contribute one further edge.  This gives
`b-2`.

For completeness, direct comparison of the explicit windows gives the
following complete list of the 17 distance-one cross pairs between
`mathcal D_0` and `mathcal D_2`:

\[
\begin{aligned}
 &(0,0),(0,1),(0,2h),(1,1),(1,2h),\\
 &(h-1,h-1),(h-1,h),(h-1,h+1),\\
 &(h,h-1),(h,h),\\
 &(h+1,h),(h+1,h+1),(h+1,h+2),(h+2,h+2),\\
 &(2h-1,0),(2h,0),(2h,1).
\end{aligned}                                         \tag{7.7}
\]

No start index occurs more than three times in (7.7).  Adding the two
internal cycle neighbours proves maximum degree five and gives
`2b+17` edges in `mathcal Q`.  Finally, deleting `X,Y` from the
distance-one cycle of `mathcal D_2` and inserting `A_*,B_*`, using the same
list (7.7), leaves two paths with `b-2` total edges and maximum degree two.
This proves the remaining assertions.  \(\square\)

### Corollary 7.3 (the opposite shell blocks the proposed one-block nibble)

At distance one, the normalized orbit codegrees are indeed

\[
 {\Lambda_{1,R}\over D_R}
 ={8b-16\over b(b^2-1)},
 \qquad
 {\Lambda_{1,Q}\over D_Q}
 ={8b+68\over b(b^2-1)}.                              \tag{7.8}
\]

However, at the opposite boundary they are

\[
 {\Lambda_{h,R}\over D_R}
 ={4(b-2)\over b(b+1)},                               \tag{7.9}
\]

and

\[
 {\Lambda_{h,Q}\over D_Q}
 ={4b+6\over b(b+1)}.                                 \tag{7.10}
\]

Consequently

\[
 b{\Lambda_{h,R}\over D_R}\longrightarrow4,
 \qquad
 2b{\Lambda_{h,Q}\over D_Q}\longrightarrow8.        \tag{7.11}
\]

#### Proof

Here `N_1=h(h+1)=(b^2-1)/4`.  The first column of (7.5), followed by
(7.4), gives (7.8).  Also `N_h=h+1=(b+1)/2`.  For `mathcal R`, (7.5) gives
`m_h=2(b-2)` and `|mathcal R|=b`; substitution in (7.4) proves (7.9).
For `mathcal Q`, it gives `m_h=2(2b+3)=4b+6` and
`|mathcal Q|=2b`, proving (7.10).  Equation (7.11) is immediate.
\(\square\)

Thus bounded internal distance-one degree does **not** yield maximum
normalized codegree `O(b^(-2))`; the distance-`h` shell gives
`Theta(b^(-1))`.  Multiplying by the orbit edge sizes leaves constants four
and eight rather than `o(1)`.  The usual pure local-dependence nibble is
therefore not justified for either one-block orbit.

This does not disprove an integral near-factor of either orbit.  It does
show that such a theorem would require another coordinated argument.  In
particular, a near-factor of a fixed product slice by disjoint
`mathcal Q_i boxtimes mathcal Y_j` gadget grids is not obtained from the
distance-one bound alone; even if obtained, one fixed split slice remains a
vanishing fraction of the full middle layer.

There is small-case positive evidence which does not use a nibble: for
`b=7`, five explicitly listed permutations of `mathcal R` in the verifier
partition all `binom(7,3)=35` local triples.  Thus the residual-packet orbit
has an exact local factor in the first nondegenerate case.  This finite
factor is not promoted to an all-`b` orbit theorem, nor does it supply the
independent cyclic-deck factor on the other block needed for a product-slice
factor.

## 8. Mechanical regression

The companion script

`scratch/verify_gate_c_one_to_two_product_absorber_20260822.py`

constructs the three decks and checks, for every odd `b` from `7` through
`51`, the general identities below; it also checks the final `b=7`
certificate:

- every deck and `mathcal R` has size `b`;
- `mathcal D_0` and `mathcal D_2` are disjoint;
- `mathcal D_1 subset mathcal D_0 union mathcal D_2`;
- the two sides of (1.14) agree with multiplicity one;
- every coordinate has `mathcal R`-degree `h`; and
- `u` has exactly one `mathcal R`-partner of codegree `h-1`;
- the exact distance-one and distance-`h` edge counts in (7.5); and
- maximum distance-one degrees two and five for `mathcal R,mathcal Q`; and
- the explicit five-packet factor of `binom([7],3)`.

The script is only a regression check; Lemmas 1.1--1.3 are the proof for
all `h>=3`.
