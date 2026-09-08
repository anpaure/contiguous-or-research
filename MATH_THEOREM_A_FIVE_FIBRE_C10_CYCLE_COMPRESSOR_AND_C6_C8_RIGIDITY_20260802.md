# Five-fibre C10 cycle compressor and C6/C8 rigidity

**Date:** 2026-08-02  
**Status:** exact local theorem.  It gives one literal palette-neutral
topology compressor for the Dong--Mao five-coordinate bank.  It does not
construct the remaining central bank, a global common basis, residence,
upper shadows, or a compiler.

## 0. Result

The saturated nontrivial `B_5` fibre has exactly one nonidentity
lower/upper-palette-preserving interval replacement.  It replaces all five
diamonds and its old/new Johnson matchings form one alternating `C10`.
Consequently there is no exact `C6` or `C8` replacement in one frozen
fibre.  The complementary fibre has the same classification, while the
size-one fibres are rigid.

Two adjacent core fibres and one fixed vertical connector bank turn this
local `C10` into a genuine topology actuator.  Before the switch their
two-bank Johnson union is five disjoint `C4` cycles; after switching one
fibre it is one `C20`.  Every lower and upper colour, every middle vertex,
and both bank matching constraints are unchanged.  Thus the move compresses
five cycle components to the unique unavoidable cycle of a closed saturated
two-matching block.

This is the missing third interval-replacement mechanism on the frozen
five-fibre face.  It is not a complete cycle absorber: a nonempty union of
two perfect matchings is 2-regular, so no internal move can make this closed
block a forest.  One opening or exterior attachment remains necessary.

## 1. Saturated `B_5` diamonds are regular tournaments

Let `K=Z_5`.  Consider a five-diamond packing across ranks `1,2,3` of
`B_5` which uses all five singleton lower endpoints.  Five disjoint
diamonds consume ten rank-two middle sets, hence every two-set exactly once.

For distinct `i,j in K`, orient

\[
                 i\longrightarrow j
\quad\Longleftrightarrow\quad
 \{i,j\}\text{ is used by the diamond with lower endpoint }\{i\}.
                                                               \tag{1.1}
\]

Exactly one orientation is chosen on every pair, and every vertex has
outdegree two.  Thus (1.1) is a regular tournament.  Conversely, a regular
tournament `T` gives the packing

\[
 [\{i\},\,\{i\}\cup N_T^+(i)]\qquad(i\in K).          \tag{1.2}
\]

Its middle vertices are all ten pairs.  Its upper triples are distinct:
equality of the triples belonging to `i` and `j` would require both
`i->j` and `j->i`.

Every regular tournament on five vertices is cyclic.  Indeed, take a
directed Hamilton cycle.  It contributes one incoming and one outgoing arc
at every vertex; the five remaining chords must do the same and hence form
the complementary directed five-cycle.  After relabelling,

\[
             N^+(i)=\{i+1,i+2\}.                    \tag{1.3}
\]

Write

\[
 U_i=\{i,i+1,i+2\},\quad
 p_i=\{i,i+1\},\quad d_i=\{i,i+2\}.                 \tag{1.4}
\]

The first phase is the matching

\[
                  E^+=\{p_i d_i:i\in Z_5\}.         \tag{1.5}
\]

## 2. Fixed-palette classification

### Theorem 2.1 (unique mate and the primitive `C10`)

There are exactly two five-diamond packings whose lower palette is all
singletons and whose upper palette is `{U_i:i in Z_5}`.  Their Johnson
matchings are

\[
 E^+=\{p_i d_i:i\in Z_5\},\qquad
 E^-=\{p_i d_{i-1}:i\in Z_5\}.                      \tag{2.1}
\]

They differ on all five intervals, and `E^+ union E^-` is one alternating
`C10`.  In particular, no nonidentity palette-neutral replacement changes
only three or four intervals.

#### Proof

Assign lower endpoint `i` to one of the upper triples containing it.  Write
that triple as `U_(i+x_i)`, where

\[
                        x_i\in\{0,-1,-2\}.           \tag{2.2}
\]

The middle pair `{i,i+1}` must occur exactly once.  It occurs in the
interval at `i` exactly when `x_i != -2`, and in the interval at `i+1`
exactly when `x_(i+1) != 0`.  Therefore

\[
 1_{x_i\ne-2}+1_{x_{i+1}\ne0}=1                    \tag{2.3}
\]

for every cyclic index `i`.  If one `x_i` is zero, (2.3) propagates zero
around the cycle.  If none is zero, the value `-1` would force the next
value to be zero, so all values are `-2`.  These are precisely the two
phases in (2.1).

In the second phase, the interval at `i` has upper endpoint `U_(i-2)` and
middle vertices `p_(i-1),d_(i-2)`, which reindexes to the second matching
in (2.1).  The alternating trace

\[
 p_0,d_0,p_1,d_1,\ldots,p_4,d_4,p_0               \tag{2.4}
\]

is the whole symmetric difference.  Hence it is one `C10`, and all five
intervals change.  QED.

Complementation proves the identical statement for the saturated rank
`2,3,4` fibre.  At ranks `0,1,2` or `3,4,5`, fixing the one lower and one
upper endpoint fixes the unique interval, so those fibres admit no move.

### Corollary 2.2 (no primitive two-fibre `C6/C8` in the frozen face)

If every replacement interval retains its fixed `H`-intersection, then
preservation of the named lower and upper palettes separates fibre by
fibre.  Therefore every primitive nonzero circuit is one of the `C10`
circuits in Theorem 2.1 or its complement.  A simultaneous move in two
fibres is their disjoint direct sum and is not primitive.  In particular,
there is no frozen-fibre `C6` or `C8` circuit.

This statement is deliberately scoped to the fibre-preserving face.
Allowing an interval itself to change its `H`-intersection leaves that face
and is not ruled out.

## 3. A literal two-fibre cycle compressor

The topology mechanism is the following elementary matching lemma.

### Lemma 3.0 (two-copy alternating-cycle compressor)

Let `M_0,M_1` be perfect matchings on a `2t`-element set `S`, and suppose
`M_0 union M_1` is one alternating `C_(2t)`.  Take copies `S_a,S_b` and
let `V={s_a s_b:s in S}` be the vertical matching.  Then

\[
 (M_0^a\cup M_0^b)\cup V=tC_4,
 \qquad
 (M_1^a\cup M_0^b)\cup V=C_{4t}.                    \tag{3.0}
\]

#### Proof

In the first union, the two copies of each edge of `M_0` and its two
vertical edges form a `C4`, independently for all `t` edges.  In the second,
contracting every vertical edge gives `M_0 union M_1=C_(2t)`.  Lifting the
alternating cycle uses its `M_1` edges in the `a`-copy and its `M_0` edges
in the `b`-copy, with one vertical edge between successive horizontal
edges.  It is therefore one cycle of length `4t`.  QED.

Lemma 3.0 is purely graphic.  The point of the construction below is that
all three matchings are literal Boolean interval banks and `M_0,M_1` have
identical named outer palettes.

Assume `m>=4`.  Choose pairwise disjoint data

\[
 |C|=m-3,\qquad a,b\notin C,\qquad
 K=Z_5,\qquad K\cap(C\cup\{a,b\})=\varnothing.       \tag{3.1}
\]

There are enough ground points because the displayed support has size
`m+4 <= 2m`.

Put `P_a=C+a` and `P_b=C+b`.  In each of the two adjacent fibres, lift the
phases (2.1):

\[
 \mathcal Q_x^\pm
 =\{[P_x+i,\,P_x+U_{\sigma_\pm(i)}]:i\in Z_5\},
 \quad x\in\{a,b\},                                  \tag{3.2}
\]

where `sigma_+(i)=i` and `sigma_-(i)=i-2`.  Each phase has the same five
lower colours and the same five upper colours.

Define the fixed vertical bank

\[
 \mathcal R
 =\{[C+X,\,C+\{a,b\}+X]:X\in {K\choose2}\}.        \tag{3.3}
\]

Its two middle vertices are `C+a+X` and `C+b+X`.  Distinct `X` give
pairwise disjoint intervals, so `R` is a ten-diamond bank.  Its lower and
upper palettes are disjoint from those in (3.2), distinguished respectively
by containing neither and both of `a,b`; the palettes in (3.2) contain
exactly one.

### Theorem 3.1 (five cycles compress to one)

Both

\[
 \mathcal Q_{old}=\mathcal Q_a^+\cup\mathcal Q_b^+,
 \qquad
 \mathcal Q_{new}=\mathcal Q_a^-\cup\mathcal Q_b^+   \tag{3.4}
\]

are ten-diamond banks with identical lower and upper palettes.  Relative to
the fixed bank `R`, their physical middle-level unions satisfy

\[
 \mathcal Q_{old}\cup\mathcal R=5C_4,
 \qquad
 \mathcal Q_{new}\cup\mathcal R=C_{20}.             \tag{3.5}
\]

Thus a five-interval `C10` replacement reduces the cycle/component count
from five to one while preserving every named outer colour and every
middle capacity.

#### Proof

The bank and palette assertions follow from Theorem 2.1 and the disjoint
`a`- and `b`-fibres.  The vertical intervals (3.3) match the two physical
copies of each rank-two set `X`.

When both copies use `E^+`, every edge `p_i d_i` and its two vertical mates
form one `C4`; the five edges give five disjoint cycles.

After switching only the `a`-copy, start at its vertex `p_i`.  The four-step
trace is

\[
 p_i^a\;--\;d_{i-1}^a\;--\;d_{i-1}^b
       \;--\;p_{i-1}^b\;--\;p_{i-1}^a.             \tag{3.6}
\]

It advances the index by `-1`.  Five repetitions visit all twenty middle
vertices before returning, proving the second identity in (3.5).  QED.

### Proposition 3.2 (sharp residual cycle)

No palette-preserving operation confined to this closed saturated
two-bank block can produce a forest.  Each bank is a perfect matching on
the same twenty middle vertices, so their union is 2-regular and therefore
contains a cycle.  The `C20` in (3.5) attains the minimum possible number,
one.

Hence Theorem 3.1 is a cycle **compressor**, not the final opening theorem.
An exterior attachment, a protected edge replacement, or one controlled
palette defect is necessary to turn the last cycle into a path.

### Corollary 3.3 (one-ticket opening normal form)

Delete any one vertical connector edge `e in R` from the switched union in
(3.5).  The result is a spanning `P20`.  Deleting the same edge before the
switch leaves one `P4` and four intact `C4` cycles.  Equivalently, the
`C10` move raises the graphic rank on these twenty vertices from `15` to
`19`, and concentrates all remaining cycle debt at one opening ticket.

The deletion by itself loses the lower and upper colour of `e`.  Therefore
Corollary 3.3 is an exact interface for one exterior replacement, not an
exact-palette forest assertion.

## 4. Common-base interpretation and exact scope

For a diamond `I=[L,L+{x,y}]`, put

\[
 r(I)=e_L^{\rm low}+e_{L+\{x,y\}}^{\rm up}
      +e_{L+x}^{\rm mid}+e_{L+y}^{\rm mid}.          \tag{4.1}
\]

The circuit identity is literally

\[
 \sum_{i\in Z_5}r([P_a+i,P_a+U_{i-2}])
 -\sum_{i\in Z_5}r([P_a+i,P_a+U_i])=0.              \tag{4.2}
\]

The lower terms agree termwise, the upper terms agree after the cyclic
reindexing `i -> i-2`, and both middle sums are the incidence vector of all
ten rank-two sets in the `a`-fibre.  Thus (4.2) is an exact integer resource
circuit, not a degree average.

There is also a common **local directed** inventory.  Orient both phases in
(2.1) from `p_i` to their `d`-endpoint.  In either phase the tail palette is
exactly `{p_i:i in Z_5}` and the head palette exactly
`{d_i:i in Z_5}`.  Thus the circuit can preserve directed middle resources
before it is joined to the vertical bank.  A globally coherent orientation
of the resulting `C4/C20` components may reverse one copy, however, so this
local fact is not yet a fixed-history or fixed-address theorem.

Consequently the signed lower, upper, and undirected middle-incidence vector
of `Q_new-Q_old` is zero.  It is a legitimate nonrectangular five-role mode
for the central common-base/absorber master.  Relative to the fixed vertical
bank, its graphic change is

\[
        \Delta(\text{cycle components})=1-5=-4.      \tag{4.3}
\]

It therefore removes four units of graphic component debt in the literal
two-fibre socket of Theorem 3.1.

What is not automatic is equally important.

1. The circuit does not itself supply the missing one-quarter central bank.
2. The closed socket retains one unavoidable cycle.
3. No literal predecessor/successor state, reset address, residence history,
   upper-shadow guard, or common compiler is assigned here.
4. The theorem does not claim that every alternating cycle in a global
   two-bank union contains such a socket.
5. The circuit's effect on any Smith/parity character depends on the
   eventual literal state decoration and is not inferred from its odd
   five-interval support.

Thus the exact next supply question is Boolean-specific: plant enough
vertex-disjoint copies of (3.1)--(3.3), with one exterior opening ticket per
connected block, while retaining the Cartesian/Hoffman or common-base rows
of the fixed-core state theorem.

## 5. A positive-density disjoint socket bank

The static resource-disjoint planting part has an unconditional answer.
Return to the fixed split `[2m]=H dotcup K` with `|K|=5`, and put

\[
                  h=|H|=2m-5,\qquad r=m-2.          \tag{5.1}
\]

Every edge `{P,Q}` of `J(H,r)` has

\[
 C=P\cap Q,\quad P=C+a,\quad Q=C+b,quad D=P\cup Q. \tag{5.2}
\]

It therefore carries exactly the compressor (3.1)--(3.3).  Call this its
**socket**.

### Theorem 5.1 (exact socket-conflict criterion)

Two such sockets are disjoint in every named lower, upper, and middle
resource if and only if their Johnson edges

1. share no endpoint `P` or `Q`;
2. have different intersection colours `C`; and
3. have different union colours `D`.

#### Proof

The horizontal fibres of a socket use every middle resource `P+X` and
`Q+X`, every horizontal lower resource `P+i,Q+i`, and their corresponding
upper resources.  Hence a shared endpoint core is exactly a collision in
these banks.  The vertical bank uses every lower resource `C+X` and every
upper resource `D+X`, so equality of `C` or `D` is exactly a vertical
collision.  Resources from horizontal and vertical rows cannot collide:
their `H`-intersection sizes are respectively `r`, `r-1`, and `r+1`.
These are all resources in the construction.  QED.

### Corollary 5.2 (unconditional positive-density supply)

There is a pairwise resource-disjoint socket family of size at least

\[
 \left\lceil
 {\binom{2m-5}{m-2}(m-2)(m-3)
  \over 2(3m^2-14m+13)}
 \right\rceil
 =\left({1\over6}+o(1)\right)\binom{2m-5}{m-2}.     \tag{5.3}
\]

#### Proof

The Johnson graph in (5.1) has degree

\[
                         \Delta=(m-2)(m-3)           \tag{5.4}
\]

and `binom(h,r) Delta/2` edges.  For one edge, at most

\[
 2(\Delta-1)
 +\left(\binom{m-2}{2}-1\right)
 +\left(\binom{m-1}{2}-1\right)                    \tag{5.5}
\]

other edges conflict with it: the three terms respectively charge a shared
endpoint, intersection, or union.  Greedy independent-set selection in
this conflict graph therefore retains at least the number in (5.3), since
one plus (5.5) is `3m^2-14m+13`.  Theorem 5.1 converts that independent set
to disjoint sockets.  QED.

Corollary 5.2 proves static actuator abundance, not circuit completeness in
an incumbent factor.  Acceptance still requires the incumbent alternating
components to meet the sockets in a useful phase, as well as literal
history/reset and exterior-opening tickets.

### Corollary 5.3 (circuit-complete planted subatlas)

Let `S` be any resource-disjoint socket family of size `s`.  Keep every
vertical bank fixed, and independently choose the `+` or `-` phase in each
of the two horizontal fibres of every socket.  Then:

1. all `4^s` configurations have exactly the same named lower, upper, and
   middle incidence vector;
2. their exchange graph under the primitive `C10` moves is the
   `2s`-dimensional hypercube, and hence connected;
3. in each socket, equal horizontal phases give `5C4`, while unequal phases
   give `C20`.

Thus the primitive `C10` circuits are circuit-complete on this planted
static subatlas, and choosing unequal phases minimizes its internal cycle
debt to exactly `s`.  That residual debt is sharp for the **disjoint closed
socket** model by Proposition 3.2.  Cross-socket or exterior openings are
still required to obtain a forest, and Corollary 5.3 makes no claim that an
arbitrary incumbent factor belongs to this subatlas.

#### Proof

Theorem 2.1 makes each phase bit resource-neutral and supplies its primitive
`C10`; Theorem 5.1 makes distinct sockets resource-disjoint.  Therefore the
phase choices commute, giving the asserted hypercube.  Lemma 3.0 gives the
two topology states in each coordinate pair.  Proposition 3.2 gives the
per-socket lower bound.  QED.

## 6. Exact regression

The lightweight verifier

```text
scratch/a_five_fibre_c10_cycle_compressor_20260802/
  audit_a_five_fibre_c10_cycle_compressor_20260802.py
```

enumerates all `2^10` tournaments and checks:

* 24 saturated `B_5` packings;
* 12 fixed-upper-palette classes, each of size two;
* every nonidentity mate changes five intervals and has one `C10`
  symmetric difference; and
* the literal two-fibre identities `5C4 -> C20`, with unchanged outer
  palettes.

The enumeration is an audit only; Theorems 2.1 and 3.1 are proved above.
