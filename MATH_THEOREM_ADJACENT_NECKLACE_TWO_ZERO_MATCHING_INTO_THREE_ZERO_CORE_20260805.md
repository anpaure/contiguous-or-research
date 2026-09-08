# Odd-slot adjacent necklaces: the two-zero stratum matches into the three-zero core

**Date:** 2026-08-05  
**Method:** canonical short-gap rooting, a product parity involution, and a
tagged adjacent-zero receiver; no computation  
**Status:** unconditional for odd `q>=5`.  Combined with the unique-zero
theorem, it saturates every shell vertex having one or two zero coordinates.
The remaining obstruction is confined to an explicit codimension-at-least-
three core.

## 1. Canonical rooting of two zeros

Put `q=2h+1>=5`.  A necklace with exactly two zero coordinates has two
directed positive gap lengths whose sum is

\[
                         q-2=2h-1.
\]

They cannot be equal.  Root at the zero followed by the shorter gap.  This
gives the unique representation

\[
 X=[0,a_1,\ldots,a_\ell,0,b_1,\ldots,b_r],
 \qquad 0\le\ell<r,
 \qquad \ell+r=2h-1,                                \tag{1.1}
\]

with every displayed `a_i,b_i` positive.  Exactly one of `ell,r` is odd.
Call that positive block `O=(o_1,...,o_(2u+1))` and the other block
`E=(e_1,...,e_(2v))`; either block may be empty only when it is `E`.

In `O`, leave `o_1` unpaired and form the adjacent ordered pairs

\[
                         (o_2,o_3),(o_4,o_5),\ldots,
                         (o_{2u},o_{2u+1}).           \tag{1.2}
\]

In `E`, form

\[
                         (e_1,e_2),(e_3,e_4),\ldots,
                         (e_{2v-1},e_{2v}).           \tag{1.3}
\]

There are `h-1>=1` pairs in total.  Order them deterministically, first by
their parent block in (1.1) and then from left to right.

## 2. Product parity involution

For an ordered positive pair `(c,d)`, put `u=c-1,v=d-1`.  Call it quiet
when `u` is even and `v=0`.  At the first nonquiet pair make the transfer

\[
 (c,d)\longmapsto
 \begin{cases}
  (c-1,d+1),&u\text{ odd},\\
  (c+1,d-1),&u\text{ even and }v>0.
 \end{cases}                                         \tag{2.1}
\]

### Lemma 2.1

Equation (2.1) is a fixed-point-free adjacent-transfer involution on all
two-zero vertices having a nonquiet pair.  It preserves the two zero
coordinates and hence the canonical root (1.1).

#### Proof

Exactly as in the unique-zero theorem, the two branches interchange

\[
                         (u\text{ odd},v\ge0)
 \quad\longleftrightarrow\quad
                         (u\text{ even},v>0).
\]

Earlier pairs stay quiet.  The donor is at least two, so all positive
coordinates stay positive and the zero pattern is unchanged.  `square`

The residual vertices have:

* arbitrary positive unpaired coordinate `o_1`;
* every ordered pair equal to `(2z+1,1)` for some `z>=0`.

## 3. Tagged injection into three zeros

Choose a designated residual pair as follows.

* If the odd block has length at least three, use its last pair
  `(o_(2u),o_(2u+1))`.
* If the odd block has length one, use the last pair of the even block.

The designated pair is the final pair immediately before one of the two
old zeros.  On a residual vertex it has form `(2z+1,1)`.  Move its second
coordinate into its first:

\[
                         (2z+1,1,0)
 \longmapsto
                         (2z+2,0,0),                 \tag{3.1}
\]

where the final displayed zero is the old zero ending that positive block.
This is one legal adjacent transfer and creates exactly one new zero.

### Lemma 3.1 (receiver injectivity)

The map in (3.1) is injective on residual two-zero necklaces.  Its image
has exactly three zeros and is disjoint from the two-zero receiver family
used by the unique-zero theorem.

#### Proof

If the two old zeros were nonconsecutive, the image has a unique adjacent
zero pair: the new zero followed by the old terminal zero.  If the old
zeros were consecutive, the image has a unique run of three zeros.  In
either case the first zero of the unique nontrivial zero run is preceded by
the even positive coordinate `2z+2>=2`; it is the newly created zero.

Restore that zero to one and subtract one from its predecessor.  This
recovers the residual source, including its canonical two-zero root.  Thus
the map is injective.  The old receiver family has exactly two zeros,
whereas the present images have exactly three, so the two families are
disjoint.  `square`

## 4. Compatibility with the consumed two-zero family

The unique-zero theorem already consumes the two-zero vertices

\[
 [0,2z_1+2,0,2z_2+1,1,\ldots,2z_h+1,1].             \tag{4.1}
\]

In the canonical representation (1.1), their short gap has length one.
That one coordinate is the unpaired member of the odd block, and every
coordinate pair on the even block is `(2z+1,1)`.  Hence every vertex in
(4.1) is residual for Lemma 2.1.

Consequently, removing the already consumed family (4.1):

1. deletes no endpoint of an involution edge from Lemma 2.1;
2. merely deletes some sources from the injective map of Lemma 3.1;
3. leaves the restricted receiver map injective.

This is the quantifier needed to compose the two codimension stages.

## 5. Protecting the radial socket in the only overlap case

For `q>5`, the radial socket

\[
                         D_s=[0^{q-2},1,s-1]
\]

has at least four zeros and cannot lie in the three-zero receiver family.
For `q=5`, one generic receiver equals `D_s` exactly when `s` is odd; its
source is

\[
                         [0,0,1,s-2,1].              \tag{5.1}
\]

Reroute this single source by moving its middle singleton to the right:

\[
 [0,0,1,s-2,1]
 \longmapsto
 [0,0,0,s-1,1].                                     \tag{5.2}
\]

The new receiver is not `D_s=[0,0,0,1,s-1]`.  It is also outside the
generic receiver image: its unique three-zero run is preceded by a
singleton, whereas every generic run is preceded by an even value at least
two.  Thus (5.2) preserves injectivity and reserves `D_s`.  The concentrated
socket `C_s` has four zeros and was never used.

## 6. Two-stage saturation theorem

### Theorem 6.1

For every odd `q>=5` and every shell mass `s`, there is a matching in
`\partial\mathcal N_{q,s}` which saturates every vertex having exactly one
or exactly two zero coordinates.  It also saturates explicit, pairwise distinct
receiver families with respectively two and three zeros.

The matching may be chosen to contain the protected radial edges
`A_sB_s` and `C_sD_s` whenever those sockets are nonterminal.

#### Proof

Use the complete unique-zero matching from the preceding theorem.  On the
remaining exactly-two-zero vertices, use Lemma 2.1 and then the restricted
receiver injection of Lemma 3.1.  Section 4 proves disjointness from the
first-stage receivers.  Section 5 reserves `D_s`; `C_s` is automatically
reserved.  Add `C_sD_s`, while `A_sB_s` is already an edge of the
unique-zero involution.  All listed edge families are vertex-disjoint.
`square`

Therefore any remaining Tutte obstruction lies in the induced family

\[
 \boxed{
 \text{at least three zero coordinates, after deleting the explicit
 three-zero receiver image.}
 }                                                       \tag{6.1}
\]

## 7. Scope

Proved:

1. complete saturation of the exactly-two-zero stratum left after the
   unique-zero stage;
2. an explicit injective adjacent edge into the three-zero core;
3. compatibility with both radial protected edges.

Not proved:

1. iteration through arbitrary zero codimension;
2. parity-optimal matching of the residual at-least-three-zero core;
3. PBBS halo separation or the full adjacent-necklace theorem;
4. any `nu(k)<=B(k)+O(1)` conclusion.
