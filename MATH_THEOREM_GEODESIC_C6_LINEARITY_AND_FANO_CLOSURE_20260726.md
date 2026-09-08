# Geodesic (C_6) linearity, the terminal-(Y) obstruction, and the Fano closure

Date: 2026-07-26

Method: pure mathematics.  The note concerns literal Johnson-geodesic
router packets; no asymptotic, probabilistic, or solver input is used.

## 0. Outcome

There is a statewise obstruction stronger than the previously recorded
``no immediate repetition'' statement.

> **Linearity law.**  Along globally Johnson-geodesic paths, two physical
> strands which meet in one nonidentity common-core (C_6) star router can
> never meet together in another such router at a later time.

Thus the supports of all internal (C_6) routers, written on the physical
strands which traverse them, form a *linear* (3)-uniform hypergraph:
two router triples intersect in at most one strand.  The law is independent
of the amount of unused storage.  It rules out direct inverse pairs, the
threefold repeated-cycle relation, and the four-strand tetrahedral relation
as literal monotone packets.

For the paired packet already constructed, the first possible same-star
successor fails even before this law is invoked: its three upper vertices
are exactly the terminal (Z_i)'s already used by the packet.

There is nevertheless an abstract identity compatible with linearity.  The
seven lines of the Fano plane admit orientations and an order whose seven
(3)-cycles multiply to the identity.  Every strand participates exactly
three times.  Hence rank three remains the first plausible storage rank,
but the correct candidate is a seven-router Fano packet, not the
three-router tetrahedral packet.  This note proves the algebraic closure;
constructing its literal monotone (X/Y) atlas remains open.

## 1. A monotonicity invariant for one path

Let

\[
 X_0-X_0^+-X_1-X_1^+-\cdots-X_ell
\]

be a path in the adjacent Boolean layers, where the lower states have a
common size and every two-step move is one Johnson exchange.  Suppose the
path is a Johnson geodesic from its first lower state to its last lower
state.  Then every coordinate is of exactly one of the following types:

1. it belongs to every lower state;
2. it is deleted once and never appears again;
3. it is inserted once and is never deleted.

Indeed, if a coordinate is deleted and later reinserted, or inserted and
later deleted, the two exchanges involving it do not contribute to the
endpoint symmetric difference.  The number of exchanges then strictly
exceeds the Johnson distance of the endpoints.

We use this elementary fact in the form

\[
 \boxed{\text{deleted original coordinates stay absent, and inserted
 coordinates stay present.}}                                      \tag{1.1}
\]

## 2. Permanent separation created by a star router

Consider a nonidentity star-to-star (C_6) router on three physical paths
(P_0,P_1,P_2).  At its input boundary the lower states have the form

\[
                         K\cup\{a_0\},\quad
                         K\cup\{a_1\},\quad
                         K\cup\{a_2\},                              \tag{2.1}
\]

where the (a_i)'s are distinct.  At the output boundary they have the
form

\[
                         K'\cup\{a_{\pi(0)}\},\quad
                         K'\cup\{a_{\pi(1)}\},\quad
                         K'\cup\{a_{\pi(2)}\},                      \tag{2.2}
\]

where (pi) is one of the two (3)-cycles.  Consequently, on the path
which enters with (a_i), the coordinate (a_i) is deleted and the
different coordinate (a_{pi(i)}) is inserted.

### Theorem 2.1 (pair-repeat no-go)

Assume the three complete paths containing the router are Johnson
geodesics.  No pair among (P_0,P_1,P_2) can occur together in a later
nonidentity common-core star router.

#### Proof

Fix (i), and put (j=\pi^{-1}(i)).  During the displayed router,
(P_i) deletes (a_i), while (P_j) inserts (a_i).  By (1.1), at
every later lower state

\[
                         a_i\notin P_i,qquad a_i\in P_j.            \tag{2.3}
\]

Suppose (P_i,P_j) occur in a later common-core star.  Any two lower
states in that star differ only in their two active petals.  Relation
(2.3) leaves three possibilities for the role of (a_i).

* It cannot lie in the common core, because (P_i) omits it.
* It cannot be the active petal of (P_i), because (P_i) omits it.
* If it is the active petal of (P_j), the later star-to-star router
  deletes it from (P_j).  But (P_j) inserted (a_i) in the first
  router, contradicting (1.1).

All possibilities are impossible.  Thus (P_i,P_j) cannot meet in a
later router.  A (3)-cycle transfers one of its three petals across each
unordered pair, so the argument covers all three pairs. (square)

### Corollary 2.2 (linear support hypergraph)

Let ({\cal T}) be the family of physical-strand triples supporting all
nonidentity common-core (C_6)'s in a monotone packet.  Then

\[
                         |T\cap T'|\le1
             \qquad(T\ne T'\in{\cal T}).                             \tag{2.4}
\]

In particular, increasing the number of unused port coordinates cannot
make any of the following abstract relations physically monotone:

* a router followed by its inverse on the same three strands;
* three repetitions of one (3)-cycle;
* the tetrahedral closure on triples
  ({a,b,c},{a,d,b},{a,c,d}).

Each list repeats a pair of physical strands.  The obstruction is not a
storage *count*; it is the permanent membership discrepancy (2.3).

## 3. Exact failure of the immediate successor to the paired packet

Retain the notation of
`MATH_THEOREM_PAIRED_C6_STAR_TO_STAR_PACKET_20260726.md`:

\[
 B_i=C\cup\{v,k',a_i\},\qquad
 Z_i=C\cup\{v,k',a_i,a_{i+1}\}.                     \tag{3.1}
\]

The output family ({B_0,B_1,B_2}) is a common-core star.  Its unique
incidence (C_6) is

\[
 B_0-Z_0-B_1-Z_1-B_2-Z_2-B_0.                         \tag{3.2}
\]

Indeed, the upper vertex joining (B_i) and (B_{i+1}) must be their
union, and

\[
                         B_i\cup B_{i+1}=Z_i.                          \tag{3.3}
\]

But the (Z_i)'s are exactly the terminal upper shore already used by
the paired packet.  Hence an immediate third (C_6) has complete ledger

\[
 \mathcal X_{m third}=\{B_0,B_1,B_2\},\qquad
 \mathcal Y_{m third}=\{Z_0,Z_1,Z_2\},                              \tag{3.4}
\]

and its (Y)-shore is not fresh:

\[
 \mathcal Y_{m third}=\mathcal Y_{m terminal}.                    \tag{3.5}
\]

Therefore it is not a vertex-disjoint incidence packet at all.  This is
stronger than the earlier observation that it would delete an inserted
petal and cease to be geodesic.

## 4. A linear identity: the Fano seven-router closure

The linearity law does not force abstract monodromy to be trivial.  On
the point set ({0,1,2,3,4,5,6}), take the seven Fano lines

\[
 012, 034, 056, 135, 146, 236, 245.                            \tag{4.1}
\]

With the usual right-to-left convention for composing permutations,

\[
 \boxed{
 (135)^{-1}(245)(236)(034)(146)(056)(012)=1.}                        \tag{4.2}
\]

Every two supports in (4.2) intersect in exactly one point and every
point belongs to exactly three supports.

### Proof of (4.2)

Apply the factors from right to left.  The seven point trajectories are

\[
\begin{array}{c|cccccccc}
 &0&1&2&3&4&5&6&7\\ \hline
0&0&1&1&4&0&0&0&0\\
1&1&2&2&2&2&3&3&1\\
2&2&0&5&5&5&5&2&2\\
3&3&3&3&3&4&4&5&3\\
4&4&4&4&6&6&2&4&4\\
5&5&5&6&1&1&1&1&5\\
6&6&6&0&0&3&6&6&6.
\end{array}                                                          \tag{4.3}
\]

The columns correspond respectively to

\[
 (012), (056), (146), (034), (236), (245), (135)^{-1}.         \tag{4.4}
\]

The last column equals the first, proving (4.2).  The incidence claims
are the defining (2)-((7,3,1)) property of the Fano plane and can also
be read directly from (4.1). (square)

The *physical* strand triples encountered in this order are

\[
 012, 256, 045, 036, 146, 234, 135,                            \tag{4.5}
\]

again the seven lines of a Fano plane.  Thus (4.2) respects Corollary 2.2
even after the distinction between fixed positions and moving physical
paths is made.

## 5. Storage consequence and exact remaining packet problem

In (4.5), every physical strand participates in exactly three routers.
Since a globally geodesic star-to-star router permanently deletes at
least one old active petal on each participating path, any literal
realization of the Fano closure needs at least three independently
available old petal coordinates per path.  In this precise participation
sense,

\[
                         \boxed{\text{Fano storage rank}\ge3.}        \tag{5.1}
\]

The Fano relation attains the corresponding *abstract* participation
bound: no strand is used more than three times.  It therefore replaces
the tetrahedral relation as the first candidate for a rank-three
norm-closing successor.

What remains is not group theory.  One must exhibit lower and upper
states for all seven routers such that

1. every router has a fresh (X/Y) shore;
2. the seven paths have equal length;
3. each path deletes only coordinates from its initial state and inserts
   only coordinates outside its initial state;
4. the boundary monodromy is (4.2), hence the identity;
5. the literal (X/Y) multisets are identical in the two global settings.

No such atlas is asserted here.  The pair-repeat obstruction proves that
the earlier two- and three-router closure candidates cannot be repaired by
adding storage; (4.2) is the smallest explicit candidate presently known
which survives that statewise test.

