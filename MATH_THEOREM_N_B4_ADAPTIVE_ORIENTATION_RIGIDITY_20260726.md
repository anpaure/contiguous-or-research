# Adaptive orientations of the three \(B_4\) seeds: maximal label alternation but no genuine frame change inside a separable packet

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Exact conclusion

Work in the middle layer of \(2m\) coordinates and put

\[
 W=\binom{2m}{m}.
 \tag{0.0}
\]

Let

\[
 M_0=12\mid34,\qquad
 M_1=13\mid24,\qquad
 M_2=14\mid23
 \tag{0.1}
\]

be the three perfect matchings of \(B=\{1,2,3,4\}\), and put

\[
 \mathcal A_c=\binom B2\setminus M_c.
 \tag{0.2}
\]

The three physical \(B_4\) seeds may be oriented as

\[
 \begin{aligned}
 C_0&=(13,14,24,23),\\
 C_1&=(14,12,23,34),\\
 C_2&=(12,13,34,24).
 \end{aligned}
 \tag{0.3}
\]

There are two different meanings of “frame change,” and they have
different answers.

1. **Frozen-context seed-label alternation is possible.**  One can
   construct a canonical first-eligible packet partition with
   exponentially small leave, assign two distinct seed labels to the two
   root children of the recursive \(Q_h\)-factor, and orient them by a
   packet-frozen context.  Every resulting \(C_{2h}\) has a seed and
   orientation label change at all \(2h\) cyclic transition boundaries.
   Both signed shadow maps remain injective inside every packet through
   every \(q\le r=h/2\).

2. **Genuine ambient-pairing changes are impossible in this grammar.**
   If one seed is fixed in each disjoint four-block, the union of its two
   matching directions over all blocks is one ambient perfect matching
   \(P\), and every edge of every packet strip is a \(P\)-pair flip.
   Hence the genuine frame-change count of every strip is exactly zero.
   Changing seed labels between disjoint blocks does not alter this fact.

Moreover, a direct attempt to change seed at one common local owner is
forbidden already by two-sided depth two.  The incoming and outgoing swap
pairs meet in one coordinate.  If that coordinate is selected at the
middle owner, it is inserted and immediately deleted, and the lower
three-state intersection has rank \(m-1\).  If it is unselected, it is
deleted and immediately reinserted, and the upper union has rank \(m+1\).
The required ranks are \(m-2\) and \(m+2\).  No orientation choice changes
this dichotomy.

Consequently:

\[
 \boxed{\text{Within separable isometric \(B_4\) tensor packets,
 genuine frame changes per strip \(=0\).}}
 \tag{0.4}
\]

Thus the requested

\[
 \Omega\!\left(\frac h{\sqrt m}\right)
 \tag{0.5}
\]

genuine changes cannot be obtained by merely choosing or orienting seed
fibres inside one unchanged isometric tensor packet.

This is an obstruction to the direct adjacent-deletion/orientation
grammar, not to all mixed-frame constructions.  The exact surviving
escape is an \(H\)-separated nonlocal re-pairing: leave the old packet,
use exterior or multi-block coordinates, and give two transitions which
reuse a coordinate edge-index gap at least \(H\), equivalently at least
\(H-1\) intervening transitions.  No such
exact owner-preserving splice is supplied by the three \(B_4\) seeds
alone.

## 1. Local geometry of the three seeds

Each \(\mathcal A_c\) is the orientation square of the matching \(M_c\).
The successive transitions of \(C_c\) alternately swap the two pairs of
\(M_c\).  Every lower edge intersection is a different singleton, and
every upper edge union is a different triple.

For distinct \(c,d,e\in\{0,1,2\}\),

\[
 \boxed{
 \mathcal A_c\cap\mathcal A_d=M_e,\qquad
 |\mathcal A_c\cap\mathcal A_d|=2,\qquad
 \mathcal A_0\cap\mathcal A_1\cap\mathcal A_2=\varnothing.}
 \tag{1.1}
\]

The two common owners in (1.1) are disjoint two-sets, hence antipodal in
\(J(4,2)\).  In particular, distinct seeds share no physical edge.
Since each seed has four edges and \(J(4,2)\) has twelve edges, the three
seed edge sets partition \(E(J(4,2))\).

### 1.1 The whole local owner switch is inseparable

Complete the central seed to the middle-owner partition

\[
 \Pi_c=\{\mathcal A_c\}\cup\{\{x\}:x\in M_c\}.
 \tag{1.2}
\]

Thus \(\Pi_c\) consists of one four-owner central SCD component and the two
omitted middle owners as singleton SCD components.  This is owner
bookkeeping, not by itself a literal factor into nontrivial \(C_4\)'s.
For \(c\ne d\), the
simple ownership-interaction graph between \(\Pi_c\) and \(\Pi_d\) has:

* the central edge \(\mathcal A_c-\mathcal A_d\), supported by the two
  common owners; and
* four singleton leaves, two incident to each central vertex.

It is a six-vertex tree.  Therefore the standard component-switch
equations force the entire six-owner fibre to change shore at once.
There is no proper owner-preserving local seed switch.

Equivalently, group the six middle owners into the three matching pairs.
The seed-incidence matrix is

\[
 B=
 \begin{pmatrix}
 0&1&1\\
 1&0&1\\
 1&1&0
 \end{pmatrix},
 \qquad \det B=2.
 \tag{1.3}
\]

Exact coverage by whole seeds would require \(Bz=\mathbf1\), whose unique
solution is

\[
 z_0=z_1=z_2=\frac12.
 \tag{1.4}
\]

Thus the symmetric three-seed average is fractional and has no integral
one-block realization.

The obstruction tensors exactly.  Group a local owner by the unique
matching \(M_{\rho_i}\) which contains it.  A product seed
\(\theta\in\{0,1,2\}^r\) contains a product owner of class
\(\rho\in\{0,1,2\}^r\) exactly when

\[
 \theta_i\ne\rho_i\qquad(1\le i\le r).
 \tag{1.5}
\]

Hence the whole-product incidence matrix is \(B^{\otimes r}\).  An exact
cover of the raw \(6^r\)-owner Cartesian carrier by whole product seeds
would require

\[
 B^{\otimes r}z=\mathbf1.
 \tag{1.6}
\]

Since \(B\) is invertible and \(B^{-1}\mathbf1=\frac12\mathbf1\), the
unique solution is

\[
 z_\theta=2^{-r}\qquad
 (\theta\in\{0,1,2\}^r).
 \tag{1.7}
\]

There is therefore no integral exact cover by whole raw product seeds for
any \(r\ge1\).  This statement does not cover a larger reservoir
completion or the sequential context-dependent repacketization in
Section 5.

## 2. Statewise orientation rigidity

Fix one seed

\[
 C=(v_0,v_1,v_2,v_3)
 \tag{2.1}
\]

with indices modulo four.  At state \(v_i\), suppose a rule chooses either
the forward neighbour \(v_{i+1}\) or the reverse neighbour \(v_{i-1}\).
Encode this choice by \(\sigma_i\in\{+,-\}\).

### Lemma 2.1 (orientation must be fibre-constant)

The lower map

\[
 v_i\longmapsto v_i\cap v_{i+\sigma_i}
 \tag{2.2}
\]

is injective if and only if all four signs \(\sigma_i\) are equal.  The
same equivalence holds for the upper-union map.

#### Proof

If \(\sigma_i=+\) and \(\sigma_{i+1}=-\), then both starts choose the
same undirected edge \(v_iv_{i+1}\).  They therefore have the same
intersection and the same union.  Every nonconstant cyclic sign word has
at least one \(+\)-to-\(-\) boundary, so either signed map fails
injectivity.

If all signs are \(+\), every cycle edge is used once, and the four
singleton intersections and four triple unions are distinct.  The same
holds when all signs are \(-\). \(\square\)

Thus orientation may depend on packet-frozen exterior context, but not
on the varying owner within one four-state seed fibre.

### Lemma 2.2 (classification of four-owner signed-rainbow fibres)

Let \(U\subseteq\binom B2\), \(|U|=4\), and let \(f:U\to U\) be a
fixed-point-free physical Johnson successor whose directed components use
all four owners.  If

\[
 X\longmapsto X\cap f(X)
 \tag{2.3}
\]

is injective, then \(U=\mathcal A_c\) for a unique \(c\), and \(f\) is
one of the two orientations of \(C_c\).  Its upper-union map is then
automatically injective.

#### Proof

As a permutation of four points, \(f\) is either a four-cycle or a union
of two directed two-cycles.  A two-cycle uses one undirected Johnson edge
from both endpoints and immediately repeats its intersection, so
injectivity excludes that case.

Write the directed four-cycle as \(X_0,X_1,X_2,X_3\), and put

\[
 \ell_i=X_i\cap X_{i+1}.
 \tag{2.4}
\]

Injectivity makes the four \(\ell_i\)'s the four different coordinates
of \(B\).  Since \(X_i\) is a two-set containing the two intersections
with its incident edges,

\[
 X_i=\{\ell_{i-1},\ell_i\}.
 \tag{2.5}
\]

Thus \(U\) consists of the four adjacent pairs in the cyclic coordinate
order \(\ell_0,\ell_1,\ell_2,\ell_3\).  The two omitted pairs are its
opposite pairs, one perfect matching \(M_c\), so \(U=\mathcal A_c\).
The transition exchanges alternate between the two pairs of \(M_c\).
The four unions omit four different coordinates and are therefore
injective. \(\square\)

In particular, a six-owner local fibre cannot be depth-one signed
injective using one occurrence per owner: there are six starts but only
four singleton lower labels and four triple upper labels.

## 3. Exact two-sided run criterion

Let

\[
 X_0,X_1,\ldots,X_q
 \tag{3.1}
\]

be a Johnson path, and write its transitions as

\[
 X_i=X_{i-1}-d_i+a_i,
 \qquad
 d_i\in X_{i-1},\quad a_i\notin X_{i-1}.
 \tag{3.2}
\]

### Lemma 3.1 (distinct-endpoint criterion)

The two equalities

\[
 \left|\bigcap_{i=0}^qX_i\right|=m-q,
 \qquad
 \left|\bigcup_{i=0}^qX_i\right|=m+q
 \tag{3.3}
\]

hold simultaneously if and only if

\[
 d_1,\ldots,d_q,a_1,\ldots,a_q
 \tag{3.4}
\]

are \(2q\) distinct coordinates.

#### Proof

Every state lies in

\[
 X_0\cup\{a_1,\ldots,a_q\},
 \tag{3.5}
\]

and every inserted coordinate occurs in some state, so the union in
(3.3) equals the right side of (3.5).  Its size is \(m+q\) exactly when
the \(a_i\)'s are distinct and all lie outside \(X_0\).

Likewise, an initial coordinate belongs to every state precisely when it
is never deleted.  Hence

\[
 \bigcap_{i=0}^qX_i
 =X_0\setminus\{d_1,\ldots,d_q\}.
 \tag{3.6}
\]

Its size is \(m-q\) exactly when the \(d_i\)'s are distinct and all
belong to \(X_0\).  These two conditions make the deletion and insertion
sets disjoint, proving necessity and sufficiency. \(\square\)

### Theorem 3.2 (direct seed turns violate depth two)

Suppose two consecutive transitions through a middle owner \(X\), both
supported on the same physical four-block \(B\), use swap pairs
\(p\in M_c\) and \(p'\in M_d\), where \(c\ne d\).  Then
exactly one of the two equalities

\[
 |\text{three-state intersection}|=m-2,\qquad
 |\text{three-state union}|=m+2
 \tag{3.7}
\]

fails.

#### Proof

Every edge of one perfect matching of \(K_4\) meets every edge of a
different perfect matching in exactly one coordinate.  Write the two
neighbours of \(X\) as

\[
 X-a+b,\qquad X-a'+b',
 \tag{3.8}
\]

where \(a,a'\in X\) and \(b,b'\notin X\).  The unique coordinate in
\(p\cap p'\) is either selected at \(X\), giving \(a=a'\), or unselected,
giving \(b=b'\).

In the first case the intersection is

\[
 (X-a+b)\cap X\cap(X-a+b')
 =X-\{a\},
 \tag{3.9}
\]

of rank \(m-1\), while \(b\ne b'\) and the union has rank \(m+2\).
In the second case the union has rank \(m+1\), while the intersection has
rank \(m-2\). \(\square\)

Reversing either seed only chooses a different edge of its matching and
does not affect the proof.

### Corollary 3.3 (\(H\)-separation is necessary)

If every consecutive window through \(q\le H\) obeys (3.3), then any two
transitions whose swap pairs share a coordinate have cyclic edge-index
distance at least \(H\).

#### Proof

Two transitions at forward index distance \(\Delta\) lie together in a
window of \(\Delta+1\) transitions.  Lemma 3.1 forbids this when
\(\Delta+1\le H\).  Hence \(\Delta\ge H\). \(\square\)

Thus a genuine re-pairing may exist only with edge-index gap at least
\(H\), or at least \(H-1\) intervening transitions in which the reused
coordinates do not move.

## 4. The fixed-frame invariant of every tensor packet

The invariant is intrinsic to physical isometric cube packets, not an
artifact of the displayed seed coordinates.

### Lemma 4.1 (unique pair frame of a Johnson cube)

Let \(Q_d\) be embedded isometrically in one Johnson layer, and let \(X\)
be one cube vertex.  Write its \(d\) cube neighbours as

\[
 X-a_i+b_i,\qquad 1\le i\le d.
 \tag{4.0a}
\]

Then all \(a_i\)'s are distinct, all \(b_i\)'s are distinct, and every
cube vertex indexed by \(I\subseteq[d]\) is

\[
 X-\{a_i:i\in I\}+\{b_i:i\in I\}.
 \tag{4.0b}
\]

Consequently the \(d\) active pairs \(\{a_i,b_i\}\) are disjoint and
extend to one ambient perfect matching.

#### Proof

Two different cube neighbours of \(X\) have cube distance two.  If their
deleted coordinates agreed, or their inserted coordinates agreed, their
Johnson distance would be one.  Hence the two endpoint lists are
separately injective.

For \(i\ne j\), the square vertex opposite \(X\) must be the unique common
Johnson neighbour at Johnson distance two from \(X\) of
\(X-a_i+b_i\) and \(X-a_j+b_j\), namely

\[
 X-\{a_i,a_j\}+\{b_i,b_j\}.
\]

Induction over cube faces gives (4.0b).  Move legality at \(X\) puts every
\(a_i\) in \(X\) and every \(b_i\) outside \(X\), so the active pairs are
mutually disjoint. \(\square\)

Fix a seed vector

\[
 \theta=(\theta_1,\ldots,\theta_r)\in\{0,1,2\}^r
 \tag{4.1}
\]

and arbitrary packet-frozen orientation signs.  The corresponding packet
has owner support

\[
 \mathcal P_\theta
 =\mathcal A_{\theta_1}\times\cdots\times
  \mathcal A_{\theta_r}\cong Q_{2r}.
 \tag{4.2}
\]

Put

\[
 P_\theta=\bigcup_{j=1}^rM_{\theta_j},
 \tag{4.3}
\]

and complete it arbitrarily to a perfect matching on the frozen exterior
coordinates.  Every physical edge of every recursive-factor strip in
\(\mathcal P_\theta\) flips one of the pairs in (4.3).  Therefore all
strip edges are internal to the one ambient frame \(P_\theta\).

To make this invariant quantitative, for a strip \(C\) with swap pairs
\(p_s\), define

\[
 \operatorname{exc}(C)
 =\min_{P\text{ a perfect matching}}
 \#\{s:p_s\notin P\}.
 \tag{4.4}
\]

Then every separable \(B_4\) packet strip satisfies

\[
 \boxed{\operatorname{exc}(C)=0.}
 \tag{4.5}
\]

This remains true if \(\theta\) and all orientation signs are arbitrary
functions of packet-frozen exterior context.

The usual recursive-factor recovery theorem is fully compatible with
this invariant.  If \(q\le r\), dyadic balance touches each local
four-block at most once.  Its local trace has rank two when untouched and
rank one or three when touched.  The target identifies the touched blocks,
and Lemma 2.1 inverts their singleton or triple labels.  Thus both signed
maps are injective inside the packet.  What fails is genuine frame
variation, not packetwise trace recovery.

## 5. A maximal but cosmetic context-dependent orientation rule

For completeness, the three seeds do permit a legal rule with the
largest possible number of *seed-label* and orientation-label changes.
This construction identifies exactly why label alternation is weaker than
ambient-frame change.

Reserve two anchor coordinates and partition the remaining coordinates
into ordered four-blocks, leaving at most two further coordinates frozen.
Fix maps

\[
 \kappa:2^{\mathrm{anchor}}\to\mathbb Z_3,
 \qquad
 \varepsilon:2^{\mathrm{anchor}}\to\{+,-\}.
 \tag{5.1}
\]

Choose \(\kappa\) surjectively; the fourth anchor state may be assigned
arbitrarily.

Let \(r\ge2\) be a power of two, \(h=2r\), and \(r\le m/16\).  For a middle
owner \(X\), freeze its anchor and scan the four-blocks sequentially.
At packet position \(j\), request the seed

\[
 \theta_j(X)=
 \begin{cases}
 \kappa(X),&1\le j\le r/2,\\
 \kappa(X)+1\pmod3,&r/2<j\le r.
 \end{cases}
 \tag{5.2}
\]

Select the first unused block whose restriction lies in
\(\mathcal A_{\theta_j(X)}\), then continue the scan.  Retain \(X\) if
all \(r\) positions are selected.  Freeze the anchor, all skipped blocks,
and the exterior, and vary every selected block through its requested
four-state support.

### Proposition 5.1 (exact retained owner partition)

The retained owners partition into disjoint packets of the form (4.2),
and the omitted middle mass is \(e^{-\Omega(m)}W\).

#### Proof

The anchor is frozen, so \(\kappa,\varepsilon\), and the requested seed
word remain fixed throughout a packet.  Inductively, every skipped block
still fails the current request and every selected block remains in its
requested support.  Hence the selected index sequence is stable, proving
disjointness and exact ownership on the retained set.

Under independent fair coordinate bits, every fresh four-block passes
every requested seed with probability \(4/16=1/4\).  There are
\((1+o(1))m/2\) blocks and only \(r\le m/16\) successes are required.
A Chernoff lower-tail bound gives \(e^{-\Omega(m)}\) failure probability.
Conditioning on total rank \(m\) costs only \(O(\sqrt m)\), which is
absorbed by the exponential. \(\square\)

Place the first \(r/2\) local blocks below the left root child of the
recursive coordinate tree and the remaining \(r/2\) below the right root
child.  Orient every left local square by
\(C_{\kappa}^{\varepsilon}\) and every right local square by
\(C_{\kappa+1}^{-\varepsilon}\).  Use only forward parent moves.

### Proposition 5.2 (maximal label alternation and exact trace recovery)

Every recursive \(C_{2h}\) component has exactly \(2h\) cyclic
seed-label changes and \(2h\) cyclic orientation-label changes.  Both
signed depth-\(q\) maps are injective inside its packet for every
\(q\le r\).

#### Proof

At the root of the recursive product-torus factor, transitions alternate
between the left and right child cycles.  Their labels are respectively
\((\kappa,\varepsilon)\) and
\((\kappa+1,-\varepsilon)\), so every cyclic transition boundary changes
both labels.  The cycle has \(2h\) transitions.

Packetwise injectivity is the recovery argument following (4.5):
bottom sibling balance touches a block at most once, and every oriented
seed has bijective singleton and triple edge-label maps. \(\square\)

Nevertheless every such component lies in \(P_\theta\), so (4.5) still
holds.  Proposition 5.2 therefore does **not** meet the genuine
frame-change requirement (0.5).  It is a useful guard against counting
decorative seed or orientation labels as physical re-pairings.

## 6. Common-core capacity of a variable seed catalogue

For two seed vectors \(\theta,\phi\in\{0,1,2\}^r\) at Hamming distance
\(d\), equation (1.1) gives

\[
 \boxed{
 |\mathcal P_\theta\cap\mathcal P_\phi|
 =4^{r-d}2^d
 =4^r2^{-d}.}
 \tag{6.1}
\]

If one coordinate is allowed to take all three seed values, the common
owner core is empty.  If \(L\) coordinates are genuinely variable
between two seed values, the common-core fraction is at most

\[
 2^{-L}.
 \tag{6.2}
\]

Thus a same-owner catalogue with

\[
 L\ge\gamma\frac h{\sqrt m}
 \tag{6.3}
\]

variable local frames retains at most

\[
 \exp\!\left(
 -\gamma(\log2)\frac h{\sqrt m}
 \right)
 \tag{6.4}
\]

of one packet's owners.  This is not a no-go for a new integral
repacketization; it proves that such a construction cannot be obtained by
declaring the different seed products to be states of one unchanged
packet.

## 7. Proved boundary and exact replacement

The following are proved.

* A statewise forward/reverse rule on one seed is signed-injective at
  depth one only when the orientation is constant on its four owners.
* Every four-owner signed-rainbow physical fibre is one of the three
  seed squares with one fixed local matching.
* A direct turn between two seeds at a common owner violates one signed
  depth-two rank exactly.
* Every product of frozen \(B_4\) seed fibres is contained in one ambient
  perfect matching and has genuine frame-change count zero.
* Frozen-context seed and orientation labels can alternate maximally
  while preserving packetwise injectivity, but this alternation is not a
  physical re-pairing.
* A same-owner seed catalogue loses a factor two of common support at
  every genuinely variable block.

The obstruction covers the direct/separable \(B_4\) packet grammar.  It
does not cover the following replacement statement.

It also does not contradict the eight-coordinate, 24-owner pair-frame
carrier: that carrier adds reservoir coordinates and has several exact
whole-owner \(Q_2\) resolutions.  Its safe transitions can use disjoint
special and reservoir pairs, so it is not the raw four-coordinate common
fibre treated by Theorem 3.2.

> **\(H\)-separated exterior re-pairing — UNPROVED.**  Construct an exact
> owner-disjoint strip factor which uses a nonlocal associator or
> exterior-moving splice to change the partner of a coordinate, places
> any two transitions sharing a coordinate at cyclic distance at least
> \(H\), makes \(\Omega(h/\sqrt m)\) such changes per strip, and preserves
> packetwise lower and upper shadow injectivity through every \(q\le H\).

Corollary 3.3 proves that the \(H\)-separation clause is necessary.  Since
a \(2h\)-cycle has room for only \(O(h/H)\) mutually \(H\)-separated
re-pairing sites on one reuse channel, the desired scale
\(h/\sqrt m\) is exactly critical when \(H=\Theta(\sqrt m)\).

The separation condition does not itself forbid the critical construction.
For example, start from a set \(X_0\) satisfying
\(X_0\cap\{1,2,3,4,5\}=\{1,3,5\}\), and use the chronological
swap pairs

\[
 12,\qquad34,\qquad15
 \tag{7.1}
\]

with orientations \(1\to2\), \(3\to4\), and \(5\to1\).  Each consecutive
two-transition window has four distinct endpoints, so it has the exact
two signed ranks.  Yet the first and third pairs meet, so the three pairs
do not lie in one perfect matching.  This is a genuine re-pairing buffered
by one intervening transition, exactly at separation \(H=2\).  It lies
outside one separable \(B_4\) packet and confirms that the unproved
replacement above is a real logical escape.

No coefficient-one conclusion is claimed.

## 8. Independent audit

The decisive step was independently checked at three levels.

1. Distinct one-factors of \(K_4\) have no common edge and every edge of
   one meets every edge of the other once.  At a common owner the shared
   coordinate is either selected in both swaps or absent in both swaps,
   giving exactly one insert--delete or delete--reinsert event.
2. The union/intersection criterion in Lemma 3.1 checks all cross-time
   possibilities, including delete--reinsert and insert--delete patterns;
   it is not merely a same-step distinctness assertion.
3. Varying seed labels between disjoint blocks was checked against the
   ambient matching (4.3).  Such label changes are fixed-frame moves and
   cannot be counted toward (0.5).

The obstruction is exact for \(H\ge2\); the surviving \(H\)-separated
theorem is explicitly marked unproved.
