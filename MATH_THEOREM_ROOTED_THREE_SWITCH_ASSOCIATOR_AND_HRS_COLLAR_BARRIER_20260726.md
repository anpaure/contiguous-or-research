# A rooted three-switch half-packet associator and the HRS collar barrier

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Outcome

There is a smallest two-generation adaptive mixed-frame compound in which
a transverse trade consumes outputs of two precursor trades, the original
active special direction is eliminated, and two different terminal
special directions survive.  It consists of three primitive slab trades
(two commuting trades in the first parallel layer and one trade in the
second layer).  On four initial packets its normalized owner-transfer
matrix is

\[
 {1\over2}
 \begin{pmatrix}
 1&1&0&0\\
 0&0&1&1\\
 1&0&1&0\\
 0&1&0&1
 \end{pmatrix}.
\tag{0.1}
\]

Thus the compound is not a four-wire permutation.  It is the incidence
operator of a four-cycle on the old packet labels: every output contains
one half of each of two old packets, and every old packet supplies one
half to each of two outputs.

The compound nevertheless has an exact rooted factor lift.  By assigning
the audited twisted-twin compiler contexts on its three switch edges, all
three trades preserve directed ordered half-paths and produce exact
isometric \(C_{2R}\)-factors.  Hence the successor is a permutation at
every stage and its nested lower and upper flags obey the rooted cocycle
exactly.  The third trade reuses a subset of the seams introduced by the
first layer.  Relative to the initial successor, the final successor
differs only at the tails of the original active direction.  Therefore,
on compound owner mass \(P\), the number of changed rooted depth-\(q\)
targets is exactly

\[
                         {qP\over R}
\tag{0.2}
\]

for each sign and every \(q<R\).  Three switches cost the same final
chronology collar as one effective direction replacement, rather than
three times as much.

This positive local construction does not rescue transport of a fixed
balanced nested table.  There are two increasingly strong reasons.  If
one temporarily ignores the requirement that the retained owners form an
exact factor, verbatim preservation through depth \(H<R\) forces the
root collar

\[
                         E\ge {HT\over R}
\tag{0.3}
\]

on any endpoint-reframed owner region of mass \(T\).  But exact factor
closure is stronger.  Equality of the two depth-one signed flags forces
the final successor to equal the prescribed successor at every retained
owner.  The retained set is therefore a union of entire old successor
cycles.  Since every affected old compiler cycle contains an \(a\)-edge
which no final \(a\)-frozen packet can realize, no affected cycle can be
retained.  Thus exact HRS actually forces

\[
                         \boxed{E\ge T,\qquad HE\ge HT.}
\tag{0.4}
\]

Consequently \(HE=o(W)\) permits endpoint reframing on only
\(T=o(W/H)\) old-cycle mass.  In particular it excludes every
positive-density use, independently of the relation between \(H\) and
\(R\).

Thus half-packet associators close the local factor/cocycle gate and
permit seam recycling, but they cannot route a preselected balanced HRS
table on more than \(o(W/H)\) owner mass with the required \(HE=o(W)\)
leave.
The only surviving uses are to co-design a new final balanced table, to
make the endpoint frame return with cancelling ordered-port holonomy, or
to act on only \(o(W/H)\) old-cycle mass.

## 1. The three-switch coordinate compound

Let \(K\) be a set of \(R-1\) common active directions, and let
\(a,b,c\) be three further, mutually disjoint physical pair directions.
Work in

\[
                         Q_{K\cup\{a,b,c\}}\cong Q_{R+2}.
\tag{1.1}
\]

Initially use the four packets

\[
 I_{uv}=\{x_b=u,\ x_c=v\},
 \qquad (u,v)\in\{0,1\}^2,
\tag{1.2}
\]

each with active frame \(K\cup\{a\}\) and size \(2^R\).

Perform the following three primitive trades.

1. In the \(c=0\) slab, replace the \(b\)-resolution by the
   \(a\)-resolution.  Equivalently the active special direction changes
   from \(a\) to \(b\).
2. Do the same in the disjoint \(c=1\) slab.
3. Among the resulting packets with \(a=0\), use their two opposite
   \(c\)-facets as one slab and replace active direction \(b\) by \(c\).

The first two trades are owner-disjoint and form one parallel layer.  The
third is a second layer.  If primitive trades rather than parallel depth
are counted, the compound has size three.

Its final packets are

\[
\begin{aligned}
 J_0&=\{x_a=0,x_b=0\},&
 J_1&=\{x_a=0,x_b=1\},\\
 L_0&=\{x_a=1,x_c=0\},&
 L_1&=\{x_a=1,x_c=1\}.
\end{aligned}
\tag{1.3}
\]

The packets \(J_0,J_1\) have active frame \(K\cup\{c\}\), while
\(L_0,L_1\) have active frame \(K\cup\{b\}\).  This is a genuinely
mixed terminal frame state.

### Theorem 1.1 (exact owner-transfer matrix)

Order the initial packets as

\[
                         I_{00},I_{01},I_{10},I_{11}
\]

and the final packets as

\[
                         J_0,J_1,L_0,L_1.
\]

After division by the packet size \(2^R\), their intersection matrix is
exactly (0.1).

#### Proof

For example, \(J_0\) fixes \(a=0,b=0\) and leaves \(c\) free.  It meets
each of \(I_{00},I_{01}\) in the \((R-1)\)-cube obtained by fixing
\(a=0\), and is disjoint from \(I_{10},I_{11}\).  This is the first row
of (0.1).  The other three rows follow identically from (1.3).  Every
nonzero intersection has size \(2^{R-1}\).  \(\square\)

The matrix in (0.1) is one half the vertex-edge incidence matrix of the
cycle

\[
                         00-01-11-10-00.
\tag{1.4}
\]

In particular it has four nonintegral rows and is not a relabelled
permutation matrix.

### Corollary 1.2 (checkerboard packet mode is erased)

The matrix in (0.1) has rank three and

\[
 \ker M=\operatorname {span}\{(1,-1,-1,1)\}.
\tag{1.5}
\]

Thus packet marginals after the compound cannot distinguish the
checkerboard difference between the two diagonals of the old packet
square.  The exact owner histories retain that information, but it is
absent from the four final packet totals.

#### Proof

The displayed vector is killed by every row.  The first, second, and
third rows are linearly independent, while the fourth equals the first
plus the second minus the third.  \(\square\)

### Proposition 1.3 (minimality)

Starting from the parallel \(a\)-edge matching of the special cube
\(Q_{\{a,b,c\}}\), any coordinate-square-flip state which has no
\(a\)-edge and uses both of the other special directions requires at least
three primitive square flips.  Up to cube symmetries, the three-flip
construction above is the unique minimal dependency pattern.

#### Proof

The first flip removes exactly two of the four \(a\)-edges and replaces
them by two parallel edges in one new direction, say \(b\).  The two
remaining \(a\)-edges are the opposite edges of the other parallel
\(ab\)-face.  Before any third flip, the only nonreversing square flip
which can remove both of them is the flip of that face; after it the
matching is the all-\(b\) matching.  Thus two flips can eliminate \(a\)
only by producing a parallel matching.  A third flip is necessary to
introduce direction \(c\), and the construction above shows it is
sufficient.  These incidences also give uniqueness up to cube
symmetries.  \(\square\)

### Proposition 1.4 (the fourth bare trade destroys the mixed state)

From the terminal matching (1.3), the only nonreversing special-coordinate
square flips are:

1. flip the \(bc\)-face at \(a=0\), undoing the third trade and producing
   the all-\(b\) parallel matching; or
2. flip the \(bc\)-face at \(a=1\), producing the all-\(c\) parallel
   matching.

Hence a fourth bare trade which restores one common active frame collapses
the adaptive mixed state to an ordinary synchronized frame exchange.

#### Proof

In the contracted special cube, at \(a=0\), the matching consists of the two opposite \(c\)-edges of
the unique \(bc\)-face.  At \(a=1\), it consists of the two opposite
\(b\)-edges of the other \(bc\)-face.  These are the only pairs of
parallel matching edges spanning a coordinate square.  Flipping the first
pair yields all \(b\)-edges; flipping the second yields all \(c\)-edges.

Equivalently at the full packet-frame level, one fourth trade changes
only one of the two equal-frame pairs and leaves the other pair untouched.
To match the untouched frame \(K\cup\{b\}\), a trade on the
\(K\cup\{c\}\) pair must insert \(b\) and remove \(c\); removing a
core direction would leave \(c\) active and fail equality.  The symmetric
argument applies to the other pair.  Thus allowing a core direction in
the fourth slab creates no additional one-step common-frame closure.
\(\square\)

## 2. Exact rooted lift by twisted-twin contexts

We recall and prove the local statement needed for self-containment.
Let two old packets be the opposite \(e\)-facets of a
\(Q_{R+1}\)-slab and have common active frame \(D\), with \(i\in D\).
Let \(\tau_j\) toggle orientation coordinate \(j\).

### Lemma 2.1 (twisted-twin directed splice)

Let \(F_0\) be any canonically oriented isometric \(C_{2R}\)-factor on
the \(e=0\) packet, and put

\[
                         F_1=\tau_e\tau_iF_0
\tag{2.1}
\]

on the \(e=1\) packet.  Delete the \(i\)-edges and retain every other
directed edge.  The half-paths glue with \(e\)-edges to exact canonically
oriented isometric \(C_{2R}\)-factors on the two packets which freeze
\(i\).  Every cycle direction word is obtained by replacing \(i\) with
\(e\).

#### Proof

Phase one old cycle immediately after an \(i\)-edge.  Its doubled word is

\[
                         w,i,w,i
\]

for a permutation word \(w\) on \(D\setminus\{i\}\).  If one directed
\(i\)-facet path has record \((u,v;w)\), the companion path in the other
\(i\)-facet has record \((v+i,u+i;w)\).  Translation by \(i\), followed
by translation by \(e\), gives on the opposite old packet the record

\[
                         (v+e,u+e;w).
\]

The two retained paths therefore join as

\[
 u\mathrel{\mathop{\longrightarrow}^{w}}v
 \longrightarrow v+e
 \mathrel{\mathop{\longrightarrow}^{w}}u+e
 \longrightarrow u.
\]

Its direction word is \(w,e,w,e\), so it is an isometric
\(C_{2R}\).  The path pairing is bijective in each frozen \(i\)-facet,
and hence the resulting cycles partition all owners.  \(\square\)

The construction is reversible, and its two output factors again have
the twisted relation \(\tau_i\tau_e\).  This follows either from the
displayed paths or by applying \(\tau_i\tau_e\) to each glued cycle.

### Theorem 2.2 (rooted lift of the three-switch compound)

The three coordinate trades of Section 1 admit compiler contexts for
which every primitive trade is a directed twisted-twin splice.  Hence
every intermediate and final state is an exact isometric cycle factor,
and all its owner-rooted flags satisfy the successor cocycle.

#### Proof

It is convenient to choose contexts backwards.  Choose an arbitrary
factor \(G\) on the intermediate packet \(a=0,c=0\), active on
\(K\cup\{b\}\).  On its \(c=1\) twin install

\[
                         \tau_c\tau_bG.
\tag{2.2}
\]

Lemma 2.1 makes the third, \(b\mapsto c\), trade legal.  For each fixed
value of \(c\), put on the \(a=1\) intermediate packet the translate

\[
                         \tau_a\tau_b
\tag{2.3}
\]

of the chosen \(a=0\) factor.  Thus the two intermediate shores at that
value of \(c\) are twisted twins for the reversible
\(a\leftrightarrow b\) splice.  Inverting Lemma 2.1 supplies exact old
factors on \(I_{0c},I_{1c}\).  The two inversions are owner-disjoint.
This constructs all four initial contexts and validates the three trades.

Every state is a disjoint union of directed cycles, so its successor is a
permutation.  Defining its flags by directed iterates gives, identically,

\[
 S^qX=X-D_q(X)+A_q(X)
\]

and the shifted rooted cocycle at all available depths.  \(\square\)

There is no assertion here that the initial flags have balanced global
target loads.  The theorem closes exact ownership, factorhood, and rooted
nesting for the local compound.

## 3. Seam recycling and the exact trace effect

Let \(S_0\) and \(S_1\) be the initial and final successors in Theorem
2.2.  Choose the retained-edge implementation of Lemma 2.1 at every
trade.  Let

\[
                         Z=\{x:S_0x\ne S_1x\}.
\tag{3.1}
\]

Everything in this section compares a persistent owner-rooted table with
the retained-edge splice.  A fresh coordinate-conjugate compiler may
rewrite all flags covariantly while remaining an exact rooted factor; the
comparison below is not a lower bound on the balance of that fresh table.

### Theorem 3.1 (the third switch creates no new seam roots)

Put \(P=2^{R+2}\), the owner mass of the compound.  Then

\[
                         |Z|={P\over R}.
\tag{3.2}

More precisely, \(Z\) is exactly the set of tails of the two \(a\)-edges
on every initial \(C_{2R}\)-component.  The first two trades replace
those \(a\)-edges by \(b\)-edges.  The third trade replaces a subset of
those newly inserted \(b\)-edges by \(c\)-edges and changes no successor
outside \(Z\).

#### Proof

Lemma 2.1 retains every edge other than the removed-direction seams.  The
first two trades cover all four initial packets, so they remove every
\(a\)-edge and alter the successor exactly at its directed tail.  Each
initial component has two occurrences of \(a\).  The number of initial
components is \(P/(2R)\), giving (3.2).

Every \(b\)-edge in either intermediate factor is an edge inserted at one
of these same tails: its direction word is the old word with
\(a\) replaced by \(b\).  The third trade removes only such \(b\)-edges
and replaces them by \(c\)-edges, retaining all other successors.  No new
tail enters the difference set, while every old \(a\)-tail still has
final outgoing direction \(b\) or \(c\), never \(a\).  \(\square\)

For a sign \(\epsilon\in\{-,+\}\), write
\(T_{j,q}^{\epsilon}(x)\) for the depth-\(q\) literal target rooted at
\(x\) under \(S_j\).

### Theorem 3.2 (exact all-depth trace mismatch)

For every \(1\le q<R\) and either sign,

\[
 \boxed{
 |\{x:T_{0,q}^{\epsilon}(x)\ne
          T_{1,q}^{\epsilon}(x)\}|={qP\over R}.}
\tag{3.3}
\]

Consequently the number of changed owner-resolved signed-depth entries
through depth \(H<R\) is exactly

\[
                         {P\over R}H(H+1).
\tag{3.4}
\]

#### Proof

On an initial doubled-permutation cycle the two \(a\)-edges are separated
by \(R\) positions.  Exactly \(q\) starts have either occurrence among
their next \(q\) edges, and these two predecessor intervals are disjoint
for \(q<R\).  With \(P/(2R)\) cycles, their union has size
\(2qP/(2R)=qP/R\).

Outside this predecessor union the initial orbit does not meet \(Z\)
during its first \(q\) steps.  Theorem 3.1 and induction on the step give
the same orbit and hence the same target under \(S_0,S_1\).

Inside the union, the old window traverses physical pair direction
\(a\), while every final packet freezes that direction.  The old lower
intersection contains neither endpoint of pair \(a\), whereas the new
lower intersection contains its fixed endpoint.  The old upper union
contains both endpoints, whereas the new upper union contains only its
fixed endpoint.  Thus both signed targets differ at every counted root.
This proves (3.3).  Summing it over two signs and
\(q=1,\ldots,H\) gives (3.4).  \(\square\)

Theorem 3.2 is the exact benefit of the compound: its third switch is
chronologically free after the first effective seam has been paid.  More
generally, any sequence which repeatedly replaces only the currently
active direction occurring at the same seam tails may rotate that seam
through arbitrarily many coordinate labels without increasing \(Z\).
This is seam recycling, not packet-wire rearrangeability.

### Corollary 3.3 (owner and interface ledger)

As a fresh covariant factor trade, one compound has:

\[
\begin{array}{c|c}
\text{owner mass}&P=2^{R+2}\\
\text{owner leave}&0\\
\text{initial/final packets}&4\\
\text{initial/final }C_{2R}\text{ components}&P/(2R).
\end{array}
\tag{3.5}
\]

A disjoint bank on owner mass \(T\) therefore has exactly \(T/(2R)\)
final components.  If all trades are performed offline and only the
final factor is linearized, its usual \(O(H)\)-per-component interface
cost is

\[
                         O(HT/R)=o(T)
\tag{3.6}
\]

when \(H=o(R)\).  There is no intermediate word interface.  The
persistent-table discrepancy (3.4) is a flag-rewrite ledger, not owner
leave for the fresh covariant factor.

#### Proof

Every primitive slab trade re-resolves the same owners into packets of
the same size, so it creates no leave and preserves packet count.  Every
isometric component has \(2R\) owners.  The standard linear cut-and-copy
operation costs \(O(H)\) symbols per final component, giving (3.6).
\(\square\)

## 4. Universal HRS cycle and collar obstructions

The exact-factor requirement makes verbatim rooted transport much more
rigid than a count of changed entries suggests.  This section assumes
literal equality with the preselected two-signed rooted table on every
retained owner.  It does not apply when the final flags are freshly
chosen and only their aggregate target loads are required to be balanced.

### Lemma 4.1 (depth-one equality forces cycle invariance)

Let \(S_0\) be a successor permutation on an owner set \(\mathcal O\).
Let \(\mathcal G\subseteq\mathcal O\) carry another successor permutation
\(S_1\).  Suppose the lower and upper depth-one rooted targets under
\(S_1\) equal those under \(S_0\) at every \(x\in\mathcal G\).  Then

\[
                         S_1=S_0|_{\mathcal G}
 \quad\hbox{and}\quad
                         S_0(\mathcal G)=\mathcal G.
\tag{4.1}
\]

In particular \(\mathcal G\) is a union of complete \(S_0\)-cycles.

#### Proof

The two depth-one targets determine the deleted and inserted physical
elements, hence determine

\[
                         Sx=x-D_1(x)+A_1(x).
\]

Thus \(S_1x=S_0x\) for every \(x\in\mathcal G\).  Since \(S_1\) is a
permutation of \(\mathcal G\), this gives
\(S_0(\mathcal G)=S_1(\mathcal G)=\mathcal G\).  Invariant subsets of a
permutation are unions of its cycles.  \(\square\)

Both signs are essential in this rigidity statement.  The lower
depth-one target alone determines the deleted element but not the inserted
element, and therefore does not determine the successor.

### Theorem 4.2 (exact HRS cycle-saturation barrier)

Let \(\mathcal A\subseteq\mathcal O\) be a union of initial
isometric \(C_{2R}\)-components, of total mass \(T\), and suppose every
one of those components uses active physical direction \(a\).  Let a
final exact packet factor on retained set \(\mathcal G\) realize the
restriction of the initial two-signed rooted table.  If every final
packet meeting \(\mathcal A\) freezes \(a\), then

\[
                         \boxed{\mathcal G\cap\mathcal A=\varnothing.}
\tag{4.2}
\]

Consequently its owner leave satisfies \(E\ge T\).

#### Proof

By Lemma 4.1, \(\mathcal G\) is a union of complete initial successor
cycles.  If it met one component \(C\subseteq\mathcal A\), it would
contain all of \(C\).  The doubled-permutation word on \(C\) uses
direction \(a\) twice.  At the tail \(z\) of either such edge,
\(S_0z\) has the opposite \(a\)-orientation from \(z\).  But
\(S_1=S_0|_{\mathcal G}\), while the final packet containing \(z\)
freezes \(a\), so \(S_1z\) cannot change that orientation.  This is a
contradiction.  Thus no such \(C\) is retained.  \(\square\)

This theorem is independent of the number of compound layers, adaptive
topology, seam recycling, or the choice of final compiler.  It uses exact
middle factorhood and already the two signed depth-one flags.

For comparison, if one drops cycle closure and asks only how many roots
can keep their prescribed tower, the weaker sharp collar count remains
useful.

### Lemma 4.3 (rootwise collar without factor closure)

In the hypotheses of Theorem 4.2, suppose a second successor is defined
on all of \(\mathcal A\) and freezes \(a\) there.  Any root set on which
both signed flags agree through every depth \(q\le H<R\) omits at least

\[
                         {HT\over R}
\tag{4.3}
\]

owners.

#### Proof

Every initial component has two directed \(a\)-edge tails, separated by
\(R\), so their number over \(\mathcal A\) is \(T/R\).  Take the
\(H\) predecessors, including the tail, of each.  The resulting sets are
disjoint and have total size \(HT/R\).

For a root \(x\) in this union, consider its first encounter, before time
\(H\), with an \(a\)-tail.  If the two successor trajectories diverge
earlier, their endpoint—and therefore one of the paired rooted flags—has
already differed.  Otherwise they diverge at that encounter because the
initial successor changes \(a\) and the second one cannot.  Equality of
both flags would imply equality of the endpoint via

\[
                         S^qx=x-D_q(x)+A_q(x),
\]

a contradiction.  \(\square\)

The three-switch construction attains (4.3) exactly.  But deleting only
that collar does not leave an exact factor: Lemma 4.1 forces deletion of
the complete affected old cycles, which is why Theorem 4.2 is the correct
HRS conclusion.

### Corollary 4.4 (quantitative failure of positive-density HRS transport)

If endpoint-nontrivial compounds act on old-cycle mass \(T\), exact HRS
transport gives

\[
                         E\ge T,\qquad HE\ge HT.
\tag{4.4}
\]

Hence \(HE=o(W)\) forces

\[
                         \boxed{T=o(W/H).}
\tag{4.5}
\]

In particular no positive-density endpoint frame change can be the HRS
transport step in any regime with \(H\to\infty\).  \(\square\)

## 5. Exact boundary

Proved:

1. the smallest three-trade/two-layer, two-generation mixed-frame
   compound eliminating its source axis while retaining two terminal
   axes, together with its four-trade common-frame collapse;
2. its exact four-by-four half-packet transfer matrix;
3. a twisted-twin compiler assignment giving exact factorhood and rooted
   successor cocycles at every intermediate state;
4. seam recycling: the third trade adds no new successor-disagreement
   roots;
5. the exact depth-\(q\) two-sign trace effect and total collar; and
6. zero fresh-factor owner leave and the \(O(HT/R)\) final interface
   ledger; and
7. depth-one cycle invariance and the exact HRS saturation barrier
   \(E\ge T\), together with the sharp rootwise collar
   \(E\ge HT/R\) when factor closure is temporarily omitted.

Not proved, and not refuted:

1. a correlated family of compounds whose changed target loads cancel to
   a new balanced final table without preserving the old table ownerwise;
2. a closed-frame compound with nontrivial but quota-safe compiler
   holonomy;
3. a moving rank-twisted matching-frame realization of a dense compound
   bank; or
4. coefficient one.

The local compound escape is therefore real but quantitatively
insufficient for the persistent-table HRS strategy.  Its scalable feature is seam
recycling.  Its unavoidable rootwise cost is an \(H/R\) collar, while
exact HRS cycle closure raises the leave to the entire affected
old-cycle mass.  To proceed, balance must be co-designed with the final
successor rather than transported from an already fixed balanced nested
resolution.
