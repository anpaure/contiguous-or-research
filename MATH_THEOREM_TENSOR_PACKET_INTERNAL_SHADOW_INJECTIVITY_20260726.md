# Exact internal shadow injectivity of the tensor associator packets

Date: 2026-07-26

Method: pure mathematics only.

## 0. Result

Let \(\mathcal V\subseteq\binom{[8]}4\) be the 24-state local
associator support and let

\[
 \mathcal V=\dot\bigcup_{j=1}^6K_j^0
            =\dot\bigcup_{j=1}^6K_j^1
\tag{0.1}
\]

be its two resolutions into oriented physical \(Q_2\)'s.  For every
\(r\) such that \(h=2r\) is a power of two, every resolution vector
\(\varepsilon\in\{0,1\}^r\) partitions \(\mathcal V^r\) into
\(6^r\) copies of \(Q_h\).

Inside each copy use the recursive maximum-isometric-cycle factor of
\(Q_h\), with the two directions belonging to the same local 8-block
placed as sibling leaves at the bottom of the recursive binary coordinate
tree.  Orient its bottom \(Q_2\)'s according to (0.1).

Then, simultaneously for every \(1\le q\le r\), the maps

\[
 x\longmapsto\bigcap_{s=0}^{q}F^s(x),
 \qquad
 x\longmapsto\bigcup_{s=0}^{q}F^s(x)
\tag{0.2}
\]

are injective on the whole packet \(\mathcal V^r\), not merely inside
one cube cell.  In particular, all collision mass of the canonical global
tensor construction comes from pairs of *different packets*.

This closes two of the three fine gates left in the first tensor-packet
audit:

1. the required directions really do occur consecutively in physical
   isometric cycles; and
2. distinct cells of one packet never create the same signed shadow
   through depth \(r\).

The remaining gate is the outer collision problem between canonical
packets.

## 1. The local one-step maps

Use the notation of the bounded associator.  On the original shore,

\[
 \mathscr R^0=
 \{Q_0\cup Y:Y\in\mathcal Y\}
 \dot\cup\{ab\cup Q_R,cd\cup Q_R\},
\tag{1.1}
\]

and on the recoupled shore,

\[
 \mathscr R^1=
 \{Q_1\cup Y:Y\in\mathcal Y\}
 \dot\cup\{ac\cup Q_R,bd\cup Q_R\}.
\tag{1.2}
\]

Orient every displayed square as in the local associator theorem.  If
\(f_\eta(x)\) is the successor of \(x\) in its unique square on shore
\(\eta\), put

\[
 \ell_\eta(x)=x\cap f_\eta(x),\qquad
 u_\eta(x)=x\cup f_\eta(x).
\tag{1.3}
\]

### Lemma 1.1 (local signed injectivity)

For each \(\eta\in\{0,1\}\), both \(\ell_\eta\) and \(u_\eta\) are
injective on \(\mathcal V\).

#### Proof

On shore zero, the four squares \(Q_0\cup Y\) give the 16 lower
targets

\[
 \{s\}\cup Y,\qquad
 s\in\{a,b,c,d\},\quad Y\in\mathcal Y.
\tag{1.4}
\]

They are all distinct.  The two reservoir squares give the eight lower
targets

\[
 ab\cup\{z\},\quad cd\cup\{z\},
 \qquad z\in\{u,v,w,x\},
\tag{1.5}
\]

again all distinct.  A target in (1.4) has one special and two reservoir
coordinates, whereas a target in (1.5) has two special and one reservoir
coordinate, so the two lists are disjoint.  Thus the 24 directed starts
have 24 different lower targets.

The same argument on shore one replaces the four-cycle local list by
\(Q_1\) and the two fixed special pairs by \(ac,bd\).  It again gives
16 targets with local profile \((1,2)\) and eight with profile \((2,1)\),
all distinct.

For upper targets, the first lists have local profile \((3,2)\), while
the reservoir-square lists have profile \((2,3)\).  Within each list the
oriented square has four different edge unions.  Hence the upper maps are
injective on both shores as well. \(\square\)

## 2. The recursive cube factor respects local blocks

Fix one cell

\[
 K=K_{j_1}^{\varepsilon_1}\square\cdots\square
   K_{j_r}^{\varepsilon_r}\cong Q_{2r}.
\tag{2.1}
\]

Regard the two directions of \(K_{j_i}^{\varepsilon_i}\) as one sibling
pair in the bottom level of a binary coordinate tree on the \(2r\)
directions.  Apply the recursive factor from
`MATH_THEOREM_RECURSIVE_ISOMETRIC_CUBE_2_FACTOR_20260726.md`.
Every component has direction word \(\pi\pi\), hence is a physical
isometric \(C_{4r}\).

The dyadic-balance law for that factor says that a cyclic block \(D\) of
\(q\) consecutive directions meets every bottom sibling pair in

\[
 |D\cap P_i|\in
 \left\{\left\lfloor\frac qr\right\rfloor,
             \left\lceil\frac qr\right\rceil\right\}.
\tag{2.2}
\]

Therefore, for \(q\le r\),

\[
                         |D\cap P_i|\in\{0,1\}.
\tag{2.3}
\]

In words, a shallow window advances any one local associator square by
at most one edge.

The word “advances” requires an orientation check which is not contained
in (2.3) alone.

### Lemma 2.1 (bottom orientations are preserved)

Choose the forward orientation in every product-torus step of the
recursive construction, and do not use the optional parent reversals.
Then the successive visits of a recursive cycle to any bottom sibling
pair traverse its local \(Q_2=C_4\) in the prescribed orientation from
(0.1).  In particular, if a shallow window meets local block \(i\) once,
its two local endpoint states are

\[
                         x_i,\ f_{\varepsilon_i}(x_i),
\tag{2.4}
\]

in that order.

#### Proof

At the bottom of the recursion this is the chosen orientation of the
physical square.  In the product-torus construction (2.5) of the
recursive-factor theorem, every child cycle moves only *forward* in each
of its two parent cycles.  Its direction word is a shuffle of cyclic
rotations of the two parent direction words; a shuffle changes the times
at which a parent is visited but not the order of those visits.  Induction
up the binary coordinate tree therefore preserves the cyclic order of
the four states in every bottom square. \(\square\)

Allowing a reversal of a parent is harmless only if the orientations of
all bottom squares below that parent are reversed simultaneously in the
definition of \(\ell_\eta,u_\eta\).  The forward-only convention avoids
that bookkeeping.

## 3. Packet-wide injectivity

Let \(x=(x_1,\ldots,x_r)\in\mathcal V^r\).  Its unique cell in (2.1)
and its unique recursive cycle determine a successor map \(F\) on the
whole packet.  For a \(q\)-window write

\[
 D(x,q)=\{i:\text{the window uses one direction in local block }i\}.
\tag{3.1}
\]

By (2.3), no local block occurs twice.  Lemma 2.1 identifies its unique
local move with the successor used in Lemma 1.1.  Consequently the physical lower
shadow factors blockwise as

\[
 \left(\bigcap_{s=0}^{q}F^s(x)\right)\cap B_i
 =
 \begin{cases}
   x_i,&i\notin D(x,q),\\
   \ell_{\varepsilon_i}(x_i),&i\in D(x,q),
 \end{cases}
\tag{3.2}
\]

and the upper shadow has the analogous formula with \(u_{\varepsilon_i}\).

### Theorem 3.1 (exact internal two-sided rainbow property)

For every fixed packet resolution \(\varepsilon\) and every
\(1\le q\le r\), the lower and upper maps in (0.2) are injective on
\(\mathcal V^r\).

#### Proof

Suppose a lower target \(T\) is given.  In a selected 8-block its local
rank is four if that block was untouched and three if it was touched.
Thus \(T\) itself identifies \(D(x,q)\).  In an untouched block it gives
\(x_i\) literally.  In a touched block, Lemma 1.1 recovers the unique
\(x_i\) from \(\ell_{\varepsilon_i}(x_i)\).  Hence every coordinate
\(x_i\), and therefore the global start \(x\), is recovered from \(T\).

For an upper target the local ranks are four and five.  The same argument
uses the inverse of \(u_{\varepsilon_i}\).  Thus both maps are injective.
\(\square\)

Notice that the target also recovers the product cell: once every
\(x_i\) is known, its unique member of the shore partition (0.1) is
known.  Hence Theorem 3.1 rules out collisions between different cells,
not only between different cycles in one cell.

## 4. Canonical global packets and the exact remaining ledger

Use the first-\(r\)-eligible-block partition from
`MATH_THEOREM_TENSORIZED_PAIR_FRAME_PACKETS_20260726.md`.  Let
\(E=e^{-\Omega(m)}W\) be its middle leave, and let \(A=W-E\) be the
number of starts contained in packets.  Choose one resolution and the
recursive factor independently in every packet.

For a signed depth \(q\le r\), let \(n_q^\pm(S)\) be the number of packet
starts producing the physical target \(S\), and put

\[
 M_q^\pm=|\{S:n_q^\pm(S)=0\}|,qquad
 C_q^\pm=\sum_S(n_q^\pm(S)-1)_+.
\tag{4.1}
\]

Every start produces one target, so

\[
 \boxed{M_q^\pm=N_q-A+C_q^\pm.}
\tag{4.2}
\]

Theorem 3.1 implies that one packet contributes at most one occurrence to
each target.  Thus its pair energy has the exact outer form

\[
 P_q^\pm
 =\sum_{\{\mathscr P,\mathscr P'\}}
   |\operatorname{Im}\Sigma_{q,\mathscr P}^\pm
     \cap
     \operatorname{Im}\Sigma_{q,\mathscr P'}^\pm|,
\tag{4.3}
\]

where the sum is over different packets only.  There are no diagonal or
same-packet terms.

Consequently the exact remaining tensor theorem is the outer assertion

\[
 \sum_{q\le H}\sum_{\pm}
 \left[C_q^\pm-(A-N_q)_+\right]=o(W),
 \qquad
 \sqrt m\ll H=o(r),
\tag{4.4}
\]

or any stronger pair-energy/Hall condition implying it.  Indeed, (4.2),
the exponentially small middle leave, the \(O(HW/r)\) cycle collar, and
the factor-blind product-SCD tail then give a literal word of length
\(W+o(W)\).

Equation (4.4) is now purely an *outer packet-collision* problem.  Local
direction order, cellwise Hamming faces, and intra-packet collisions have
been eliminated exactly.

The first-\(r\) convention does not solve this outer problem by itself.
There is an explicit collision already at \(r=2,q=1\): take blocks
\(A<B<C\), put the same local lower edge-decoration in \(A,B\), and a
common eligible middle state in \(C\).  Completing \(A\) gives canonical
packet \(\{A,C\}\), while completing \(B\) gives \(\{B,C\}\); the two
forward local edges have the same global lower target.  Replacing
intersections by unions gives the upper collision.  The full labelled
example and a collision-graph guard bound are recorded in
MATH_AUDIT_Z4_TENSOR_SUCCESSOR_AND_PACKET_COLLISIONS_20260726.md.

## 5. Boundary

Proved here:

* local lower and upper one-step injectivity on both associator shores;
* at most one changed direction per local block for every \(q\le r\);
* exact packet-wide signed shadow injectivity through depth \(r\);
* the cross-packet-only collision formula (4.3); and
* the precise outer collision ledger (4.4) sufficient for coefficient one.

Not proved here:

* a choice of packet resolutions making (4.4) hold;
* an outer matching/frame design which changes the canonical packets; or
* a cross-packet Hall or discrepancy theorem.

The tensor lane has therefore been reduced from three fine gates to one.
