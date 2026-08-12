# Slab splitters, the Beneš obstruction, and the rooted-flag gate

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Outcome

The proposed fixed-topology whole-packet Beneš/Waksman embedding does
not exist when one bare slab is required to implement each independently
programmable switch.

The legal \(Q_{R+1}\) trade is not a packet-level \(2\times2\)
straight/cross switch. It is a tensor transpose: if the old packets are
the two facets fixing an inactive slab direction \(e\), and the new
packets are the two facets fixing an old active direction \(i\), then
every old packet meets every new packet in exactly \(2^{R-1}\) owners.
Thus each new packet receives half of each old packet.

The switch state is also recorded in the physical active frame:

\[
 D\quad\longleftrightarrow\quad
 D'=(D\setminus\{i\})\cup\{e\}.
\tag{0.1}
\]

Consequently independently chosen first-layer states cannot feed a fixed
transverse second slab layer. The standard four-wire butterfly already
fails this closure test, before any target-load calculation.

There is a second independent obstruction. A floor-balanced nested
deletion/addition table need not be rooted-successor compatible. Any
cycle factor realizing rooted flags must have a bijective successor
\(S\) and obey the all-depth cocycle

\[
 S^qX=X-D_q(X)+A_q(X).
\tag{0.2}
\]

Perfect lower and upper floor balance alone does not imply even that
\(S\) is a permutation; an exact six-owner counterexample occurs at
\(m=2,H=1\).

Thus the statement

> choose arbitrary balanced nested flags first and route them through a
> recursive Beneš network of slab trades

is false twice over: the local primitive is not a Beneš switch, and the
abstract flags need not be the windows of any successor permutation.

A stronger adaptive, compound, half-packet, or state-dependent
construction is not ruled out. One clean sufficient statement is a
hereditary rooted-splitter theorem which chooses the flags, successor,
slab decisions, and final compiler packets jointly.
For coefficient one it is enough that its owner leave satisfy

\[
                         HE=o(W).
\tag{0.3}
\]

The stronger condition

\[
                         H(B_H+2)E=o(W),
 \qquad B_H=\left\lfloor\frac W{N_H}\right\rfloor,
\tag{0.4}
\]

implies CPCR. Exact slab re-resolution itself creates no owner leave.
The final component/interface cost remains

\[
                         O(HG/R)=o(W)
\tag{0.5}
\]

when \(H=o(R)\).

## 1. The exact slab as a tensor transpose

Let \(D\) be a set of \(R\) mutually disjoint physical pair-directions,
let \(e\notin D\) be disjoint from them, and fix \(i\in D\). Inside

\[
                         \mathcal S=Q_{D\cup\{e\}}
                                      \cong Q_{R+1},
\tag{1.1}
\]

write

\[
 P_a^e=\{x\in\mathcal S:x_e=a\},\qquad
 P_b^i=\{x\in\mathcal S:x_i=b\},
 \qquad a,b\in\{0,1\}.
\tag{1.2}
\]

The old shore is \(\{P_0^e,P_1^e\}\); its packets have active frame
\(D\). The traded shore is \(\{P_0^i,P_1^i\}\); its packets have active
frame \(D'\) from (0.1).

### Theorem 1.1 (splitter intersection matrix)

Both shores partition exactly the same \(2^{R+1}\) owners, and

\[
 \boxed{|P_a^e\cap P_b^i|=2^{R-1}
        \quad(a,b\in\{0,1\}).}
\tag{1.3}
\]

Moreover, among the coordinate-facet resolutions of \(\mathcal S\), the
only resolution whose two packets have active frame \(D\) is the
original \(e\)-resolution.

#### Proof

The intersection in (1.3) fixes the two distinct coordinates \(e\) and
\(i\) of \(Q_{R+1}\), leaving \(R-1\) free coordinates. It therefore has
size \(2^{R-1}\).

Resolving \(\mathcal S\) by fixing a coordinate \(j\in D\cup\{e\}\)
leaves active frame \((D\cup\{e\})\setminus\{j\}\). This equals \(D\)
only for \(j=e\). \(\square\)

Normalize the old/new intersection counts by the packet size \(2^R\).
The slab trade has matrix

\[
                         \frac12
 \begin{pmatrix}1&1\\1&1\end{pmatrix}.
\tag{1.4}
\]

After relabelling ports, a genuine straight or cross switch has one of

\[
 \begin{pmatrix}1&0\\0&1\end{pmatrix},
 \qquad
 \begin{pmatrix}0&1\\1&0\end{pmatrix}.
\tag{1.5}
\]

No port relabelling or compiler conjugate changes (1.3). Thus a slab
trade does not transport either old packet intact to one output. It
interchanges the roles of the packet bit \(x_e\) and the internal bit
\(x_i\).

Equivalently, the four \((R-1)\)-cubes

\[
                         Q_{ab}=\{x_e=a,x_i=b\}
\]

are paired by rows on the old shore and by columns on the new shore.
The primitive is an associator on four half-packets, not a switch on two
packet wires.

## 2. Failure of fixed-layer Beneš closure

A physical \(Q_{R+1}\) slab joining two packet facets requires, at a
minimum, that the two packets have the same active frame; they then differ
only in the frozen value of the new slab direction. Equality of active
frames is necessary, though not sufficient, because all other frozen
coordinates and the local-rank frame must also match.

Take two opposite facets of a fresh spectator direction \(f\). In each
facet place the same \(e\leftrightarrow i\) slab gadget. Let
\(\sigma_b\in\{0,1\}\) be the state in the \(f=b\) facet, with state
zero meaning the old \(e\)-resolution and state one the traded
\(i\)-resolution.

### Theorem 2.1 (two-layer state compatibility)

Outputs from the two \(f\)-facets can be paired as opposite facets of a
fixed second-layer slab across \(f\) only if

\[
                         \boxed{\sigma_0=\sigma_1.}
\tag{2.1}
\]

#### Proof

The output frame in facet \(b\) is \(D\) when \(\sigma_b=0\), and
\(D'\) when \(\sigma_b=1\). A second \(f\)-slab requires equal frames,
so (2.1) is necessary. \(\square\)

A Beneš or Waksman network assumes that every first-layer switch is
independently programmable and that its outputs enter one fixed next
pairing pattern, regardless of those settings. Theorem 2.1 contradicts
that closure assumption in the first four-wire butterfly. The direct
recursive interpretation of bare slab trades as \(2\times2\) switches
is therefore refuted.

The conclusion is deliberately limited. A state-dependent next-layer
topology, or a new compound mixed-frame associator on four or more
packets, might evade (2.1). Such a device is not supplied by recursive
application of the two-packet slab lemma.

There is one exact positive network, but it is synchronized basis
exchange rather than rearrangeability.

### Theorem 2.2 (synchronized parallel-foliation exchange)

Let \(Q_S\) be partitioned into the parallel \(Q_R\)-fibres with common
active set \(D\subseteq[S]\). For \(i\in D\) and
\(e\in[S]\setminus D\), all fibres can be re-resolved, in one
owner-disjoint slab layer, into the parallel \(Q_R\)-fibres with common
active set

\[
                         D'=(D\setminus\{i\})\cup\{e\}.
\tag{2.2}
\]

The layer contains exactly

\[
                         2^{S-R-1}
\tag{2.3}
\]

slabs, creates no owner leave, and has a common output frame. Hence any
two parallel \(R\)-coordinate foliations of \(Q_S\) are connected by at
most \(R\) synchronized slab layers.

#### Proof

For each frozen word on
\([S]\setminus(D\cup\{e\})\), the union of the two old fibres with
\(x_e=0,1\) is one \(Q_{D\cup\{e\}}\). These slabs are pairwise
owner-disjoint and exhaust \(Q_S\). Resolve every one by fixing \(i\).
The resulting packets are indexed by the old exterior word and the
new frozen bit \(x_i\), so collectively they are exactly the parallel
fibres with active set \(D'\). The number of exterior words is (2.3).

For arbitrary \(D,D^\ast\in\binom{[S]}R\), biject
\(D\setminus D^\ast\) with \(D^\ast\setminus D\) and perform one
exchange for each pair. There are at most \(R\) pairs. \(\square\)

Theorem 2.2 is the synchronized fixed-frame analogue of a switching
layer provided by the present primitive. If one insists that the output
remain a single parallel foliation of the same parent cube, every slab
in this synchronized construction takes the same frame-changing state.
It can move a common support basis, but this construction cannot make
independent routing decisions for different packet wires. This does not
exclude adaptive regrouping, compound or half-packet associators, or an
extra-coordinate encoding of the switch state.

In the rank-twisted atlas, Theorem 2.2 applies automatically inside one
parent product cube when \(e\) is an unused split matching axis. For a
genuinely cross-parent nonmatching direction \(e\), one additionally
needs an owner-spanning matching of compatible parent facets. The local
cross-parent slab theorem does not supply that abundance, so (2.3) must
not be quoted for cross-parent layers without a separate matching proof.

## 3. Coordinate-subcube invariant

There is a broader geometric restriction behind Theorems 1.1 and 2.1.

### Lemma 3.1 (subcube closure)

Starting from a packetization into literal coordinate \(Q_R\)'s, every
packet produced by any legal sequence of \(Q_{R+1}\) re-resolutions is
again a literal coordinate \(Q_R\).

#### Proof

This holds initially. A legal trade replaces two opposite coordinate
facets of one coordinate \(Q_{R+1}\) by two opposite facets in another
coordinate direction. The new facets are coordinate \(Q_R\)'s. Induct
over the trades. \(\square\)

Hence a final packet cannot be an arbitrary \(2^R\)-set of owners, as
would result from an arbitrary permutation of owner wires. Every final
packet must be an affine coordinate subcube in the available physical
pair geometry.

For a rooted flag table, let \(\mathscr D_H(X)\) be the set of physical
swap directions demanded through depth \(H\) at owner \(X\). A necessary
support condition for a final packet \(P\) is

\[
 \boxed{
 \bigcup_{X\in P}\mathscr D_H(X)\subseteq A(P),
 \qquad
 \left|\bigcup_{X\in P}\mathscr D_H(X)\right|\le R,}
\tag{3.1}
\]

where \(A(P)\) is the packet's active frame. The full prefix table must
also be an allowed affine/context conjugate of the diverse compiler.
Condition (3.1) alone is not sufficient.

Every legal direction remains a cross-half physical pair inside one
macroblock. Thus any prescribed deletion/addition pair outside this
direction class is another immediate incompatibility. Abstract Pascal
flow balance does not enforce either this legality or (3.1).

## 4. Rooted successor cocycles

For every middle owner \(X\), let

\[
\begin{aligned}
 D_1(X)&\subset D_2(X)\subset\cdots\subset D_H(X)\subseteq X,\\
 A_1(X)&\subset A_2(X)\subset\cdots\subset A_H(X)\subseteq X^c,
\end{aligned}
\tag{4.1}
\]

with \(|D_q(X)|=|A_q(X)|=q\). The corresponding lower and upper targets
are \(X-D_q(X)\) and \(X+A_q(X)\).

### Theorem 4.1 (necessary successor-cocycle law)

If the rooted flags in (4.1) are the signed windows of one directed
return-free cycle factor, then

\[
                         S(X)=X-D_1(X)+A_1(X)
\tag{4.2}
\]

is a permutation of the middle owner set and, for every \(q<H\),

\[
\begin{aligned}
 D_q(SX)&=D_{q+1}(X)\setminus D_1(X),\\
 A_q(SX)&=A_{q+1}(X)\setminus A_1(X).
\end{aligned}
\tag{4.3}
\]

Equivalently,

\[
                         S^qX=X-D_q(X)+A_q(X)
 \qquad(1\le q\le H).
\tag{4.4}
\]

#### Proof

The directed successor of a cycle factor is bijective, giving the first
claim. Along a return-free geodesic, the depth-\((q+1)\) deletion list
rooted at \(X\) is the first deletion followed by the depth-\(q\) list
rooted at \(SX\). Removing the first item gives the first identity in
(4.3); the addition identity is identical. Iteration gives (4.4).
\(\square\)

These are cross-owner constraints. The totally unimodular Pascal
deletion flow gives nested paths at each root, but it does not impose
(4.2)--(4.3).

Slab trades preserve each physical owner. A rooted flag cannot be moved
to another owner as an abstract token: its lower targets must remain
subsets of its root and its upper targets supersets of that same root.
Therefore no switching network can repair a nonbijective map (4.2)
while keeping a preselected rooted flag table fixed.

## 5. A smallest balanced table with no successor factor

Take \(m=2,H=1\) on ground set \([4]\). There are six middle owners.
Prescribe lower target \(T\), upper target \(U\), and induced successor
\(S=T\cup(U\setminus X)\) as follows:

\[
\begin{array}{c|c|c|c}
X&T&U&S\\ \hline
12&1&124&14\\
13&1&134&14\\
14&4&134&34\\
23&2&123&12\\
24&2&234&23\\
34&3&234&23
\end{array}
\tag{5.1}
\]

### Proposition 5.1

Every rank-one and rank-three target in (5.1) has floor/ceiling-balanced
load, but no cycle factor realizes the table.

#### Proof

The lower loads on \(1,2,3,4\) are \(2,2,1,1\). The upper loads on
\(123,124,134,234\) are \(1,1,2,2\). Since

\[
                         \frac{\binom42}{\binom41}=\frac32,
\]

both are exactly at their floor/ceiling quotas.

The successor values are

\[
                         14,14,34,12,23,23.
\]

Thus \(14\) and \(23\) have indegree two, while \(13\) and \(24\) have
indegree zero. The map is not a permutation, contradicting Theorem 4.1.
\(\square\)

This example is independent of packet geometry. It proves that exact
balanced nested flags are not, by themselves, routable compiler demand.
A positive construction must choose a successor-compatible balanced
flow from the outset, or repair the flags before fixing their roots.

## 6. Conditional rooted embedding theorem

The preceding obstructions identify a precise positive target.

### Hypothesis HRS (hereditary rooted-splitter embedding)

There exist:

1. floor/ceiling-balanced lower and upper rooted flags on all \(W\)
   middle owners through depth \(H\);
2. a successor permutation satisfying (4.3);
3. a legal sequence of owner-preserving slab re-resolutions; and
4. a final diverse-compiler factor on a retained owner set
   \(\mathcal G\), \(|\mathcal G|=G=W-E\),

such that the final compiler flags at every \(X\in\mathcal G\) equal the
restriction of the prescribed rooted table.

The final packets must be literal \(Q_R\)'s, and every packet table must
be one allowed whole-compiler table, not merely satisfy (3.1).

### Theorem 6.1 (HRS implies CPCR with an exact leave bound)

Assume HRS and \(E<N_q\) for every \(q\le H\). Put

\[
 B_q=\left\lfloor\frac W{N_q}\right\rfloor,\qquad
 c_q=\left\lfloor\frac G{N_q}\right\rfloor.
\tag{6.1}
\]

Then

\[
 \boxed{
 \Phi_m
 \le 2H(B_H+2)E.}
\tag{6.2}
\]

In particular, (0.4) implies CPCR.

#### Proof

Fix one sign and depth. Let \(b_T\in\{B_q,B_q+1\}\) be the full-table
load at target \(T\), let \(r_T\) be the number of omitted rooted flags
ending at \(T\), and put \(L_T=b_T-r_T\). Then

\[
                         \sum_Tr_T=E,\qquad
                         0\le r_T\le B_q+1.
\tag{6.3}
\]

Since \(G=W-E\) and \(E<N_q\),

\[
                         c_q\in\{B_q,B_q-1\}.
\tag{6.4}
\]

If \(c_q=B_q\), then

\[
\begin{aligned}
 b_T=B_q&:\quad
 (L_T-c_q)(L_T-c_q-1)=r_T(r_T+1),\\
 b_T=B_q+1&:\quad
 (L_T-c_q)(L_T-c_q-1)=r_T(r_T-1).
\end{aligned}
\]

Their sum is at most \((B_q+2)E\).

If \(c_q=B_q-1\), then targets with \(b_T=B_q\) contribute
\(r_T(r_T-1)\). Targets with \(b_T=B_q+1\) contribute
\((r_T-1)(r_T-2)\). For \(r_T\ge1\), either contribution is at most
\(B_qr_T\). A high target with \(r_T=0\) contributes two. The number of
high targets in the full table is the residue

\[
                         W-B_qN_q.
\]

The floor can drop only when this residue is \(<E\), so all zero-removal
high targets together contribute at most \(2E\). Hence the signed
depth-\(q\) energy is at most \((B_q+2)E\).

The sequence \(B_q\) is nondecreasing in \(q\). Sum over both signs and
all \(q\le H\) to obtain (6.2). \(\square\)

### Corollary 6.2 (the weaker coefficient-one leave bound)

Under HRS, the total number of missing signed targets through depth
\(H\) is at most

\[
                         2HE.
\tag{6.7}
\]

Consequently \(HE=o(W)\), together with the final interface estimate
(0.5), implies the coefficient-one central target theorem without the
quadratic CPCR conclusion.

#### Proof

Fix one sign and depth. Every target has full-table load at least one.
If it is missing after restriction to \(\mathcal G\), at least one of
its full-table occurrences belongs to an omitted owner. Charge the
missing target to one such occurrence. Distinct missing targets use
distinct occurrences, while the \(E\) omitted owners contribute exactly
one occurrence each at the fixed sign and depth. Thus there are at most
\(E\) missing targets per signed depth. Sum over the \(2H\) choices.
\(\square\)

For the rank-twisted packet leave

\[
                         E\le2^{m+o(m)}
\tag{6.5}
\]

and any \(H=o(m)\),

\[
 B_H\le\frac W{N_H}
       =\exp\!\left(O(H^2/m)+o(1)\right)=\exp(o(m)).
\tag{6.6}
\]

Thus the right side of (6.2) is \(2^{m+o(m)}=o(W)\). A successful HRS
construction on the existing retained owner set would therefore prove
CPCR with ample room.

## 7. Leave, switch count, and interfaces

Let \(s=2^R\) and \(P=G/s\) be the number of final packets.

### Exact owner ledger

Every slab re-resolution replaces two \(Q_R\)'s by two \(Q_R\)'s on the
same \(Q_{R+1}\). Therefore:

* owner leave created by any legal sequence of trades: \(0\);
* packet count after every trade: \(P\);
* final compiler component count: \(G/(2R)\).

The only owner leave is the initial packetization leave plus any
additional quarantine imposed because a desired network stage is not
geometrically available.

If a full packet layer existed, it would contain

\[
                         \frac{P}{2}
                         =\frac{G}{2^{R+1}}
\tag{7.1}
\]

owner-disjoint slabs. A standard Beneš network on \(P=2^\ell\) wires
would have

\[
                         2\ell-1
                         =2\log_2P-1
\tag{7.2}
\]

layers and \((P/2)(2\ell-1)\) switches. These are hypothetical counts
only: Theorems 1.1 and 2.1 invalidate the packet-wire interpretation.

### Final interface ledger

Install the diverse compiler only after all offline re-resolutions.
There are \(G/(2R)\) final cycles. Linearizing each by an \(O(H)\)
prefix costs

\[
                         O\left(\frac{HG}{R}\right)=o(W)
\tag{7.3}
\]

when \(H=o(R)\). Intermediate switch states are not serialized into the
contiguous-OR word and create no interface charge.

Serializing \(t\) complete factor states would already use
\(\Omega(tG)\) owner symbols and is incompatible with coefficient one.
Thus a switching network, if it exists, is an offline design algorithm,
not a word concatenation.

### Absolute derivative warning

For one slab, the \(L^1\) variation of the target-occurrence vector is
at most \(4s\) at each signed depth; repeated labels can only decrease
this value. A complete layer has \(P/2\) slabs, so its total
triangle-bound occurrence variation over both signs and all \(q\le H\)
is at most

\[
                         4HG.
\tag{7.4}
\]

For \(t\) layers this becomes \(4tHG\), far larger than \(W\) at
Beneš depth \(t=\Theta(m)\). Therefore no proof may pay the stages by
absolute derivative. Only the final common load, with genuine
cancellation, is relevant.

### Additional network leave

If unavailable or incompatible stages force an additional owner
quarantine \(E_{\rm net}\), the strong HRS-to-CPCR estimate requires

\[
                         H(B_H+2)E_{\rm net}=o(W).
\tag{7.5}
\]

For missing-target control alone, the weaker condition

\[
                         HE_{\rm net}=o(W)
\tag{7.6}
\]

suffices. If \(t=\Theta(m)\) stages each discard owners permanently, the
sum of their discarded masses must obey (7.6) for coefficient one, or
(7.5) for CPCR. Uniform per-stage budgets are respectively
\(o(W/(tH))\) and \(o(W/(tH(B_H+2)))\).

## 8. Exact boundary

Proved:

1. the slab intersection matrix (1.3), showing that the primitive is a
   balanced splitter rather than a straight/cross switch;
2. failure of fixed transverse-layer closure under independent upstream
   states;
3. the synchronized parallel-foliation exchange theorem;
4. coordinate-subcube closure of every legal sequence;
5. the necessary rooted successor permutation and all-depth cocycle;
6. the smallest perfectly balanced non-successor table;
7. the exact conditional CPCR bound (6.2); and
8. the weaker coefficient-one missing bound (6.7); and
9. zero slab leave and the final interface ledger (7.1)--(7.6).

Not proved:

1. an adaptive compound mixed-frame associator;
2. existence of a successor-compatible balanced nested table on all
   owners;
3. a hereditary splitter network grouping that table into allowed
   diverse-compiler packets;
4. abundance of the necessary slab geometries through all adaptive
   scales; or
5. CPCR and coefficient one.

The fixed-topology model with one independently programmable bare slab
per whole-packet switch is closed. Adaptive, state-dependent, compound,
and half-packet networks remain open. HRS is one sufficient positive
lemma for coefficient one with leave \(E=o(W/H)\); the stronger leave
\(E=o(W/(H(B_H+2)))\) yields CPCR. HRS is not claimed necessary: it is
strictly stronger than abstract rearrangeability and co-designs
chronology, packet geometry, and the balanced target quotas.
