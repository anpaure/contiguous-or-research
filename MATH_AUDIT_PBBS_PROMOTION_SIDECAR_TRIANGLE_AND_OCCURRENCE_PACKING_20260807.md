# Audit of PBBS sidecar-cycle cancellation and the exact triangle occurrence-packing gate

**Date:** 2026-08-07  
**Audited source:**
`MATH_THEOREM_PBBS_PROMOTION_SIDECAR_CYCLE_CANCELLATION_20260807.md`  
**Verdict:** PASS for named target coverage and the directed-triangle
specialization.  Important scope: cycle cancellation does not preserve a
globally simple lower-(q1) *edge-colour palette*—every cycle vertex appears
on two owner edges.  It cancels the missing literal-target debt by supplying
each sidecar name at another native source occurrence.  Three unsplit
triangle hinges can share the same abstract rail core, but their flag
endpoints obey a sharp directed-distance condition; a standalone triangle
cannot be compressed below (3d/2) cyclic positions.  The remaining exact
gate is the coordinatewise interval cover-free condition stated below.

## 1. Audit of one arc and cycle cancellation

For an arc (i\to j),

\[
 Q_j=(Q_i-\{u_i\})\cup\{b_i(j)\}.
\]

With (C_i=Q_i\setminus U_i) and
(B_i=C_i\cup\{b_i(j)\}), one has

\[
 M_i\cup B_i=Q_j,
 \qquad
 U_i\cup C_i=Q_i,
 \qquad
 T_i=U_i\cup B_i=Q_i\cup Q_j.
\]

The three owners are therefore

\[
 Q_i+b_i^-,qquad Q_i\cup Q_j,qquad Q_j+v_i,
\]

and their lower colours are (Q_i,Q_j).  The native shared source cells
are (U_i,Q_j), so exactly (Q_i) is exported and exactly (Q_j) is
supplied literally.  For a permutation (\pi),

\[
 \{Q_i:i\in J\}=\{Q_{\pi(i)}:i\in J\}
\]

as named multisets.  Theorem 3.1 is correct.

If the union colours (Q_i\cup Q_{\pi(i)}) are distinct, the middle
owners are distinct.  This condition says nothing about the two outer
owners; the source note correctly leaves their completion open.

### Palette-scope correction

In a cycle bank, every (Q_i) occurs twice as a set-theoretic lower owner
edge colour:

1. as the predecessor colour of hinge (i); and
2. as the successor colour of hinge (\pi^{-1}(i)).

Thus cycle cancellation proves that every sidecar *target name* has a
literal source witness.  It does not give an injective lower-(q1) edge
palette.  Any theorem requiring a q1-rainbow owner factor must either use
palette slack, omit one of the two edge roles from that factor, or add a
separate palette trade.

## 2. Directed triangle specialization

Let (R) have rank (m-2), and choose distinct labels (x,y,z\notin R).
Put

\[
 Q_x=R+x,qquad Q_y=R+y,qquad Q_z=R+z.
\tag{2.1}
\]

Choose flags with

\[
 u_x=x,quad u_y=y,quad u_z=z,
\]

and

\[
 M_x,M_y,M_z\subseteq R,qquad |M_i|=m-d-2.
\tag{2.2}
\]

Then

\[
 Q_x-x=R\subset Q_y,quad
 Q_y-y=R\subset Q_z,quad
 Q_z-z=R\subset Q_x.
\]

Hence

\[
 x\to y\to z\to x
\tag{2.3}
\]

is a directed flagged-coatom triangle.  Its entering labels are
(y,z,x), and its middle owners are

\[
 R+x+y,qquad R+y+z,qquad R+z+x,
\tag{2.4}
\]

which are pairwise distinct.  The triangle therefore satisfies every
claim of Corollary 3.2.

## 3. Common-core compatibility of the three local collars

The owner-level cores can be synchronized.  Suppose there is a set

\[
 A\subseteq M_x\cap M_y\cap M_z,qquad |A|=d-1.
\tag{3.1}
\]

Write

\[
 K_i=M_i\setminus A,qquad C_i=R\setminus M_i.
\]

Then every unsplit residence collar has the same core

\[
 \boxed{G=K_i\cup C_i=R\setminus A.}
\tag{3.2}
\]

Thus there is no owner-rank or permanent-core obstruction to placing all
three hinges in one (G)-rail.  For large parameters (3.1) is easy to
arrange: it suffices to choose the three (d)-set complements (C_i) so
that (R\setminus(C_x\cup C_y\cup C_z)) has size at least (d-1).

This is only owner-level compatibility.  The three saturated suffix flags
still impose occurrence constraints on one source chronology.

## 4. A forced support position

Let hinge (i\to j) have flag endpoint (e_i).  Its literal table contains

\[
 Z_{e_i,d-1}=M_i
\tag{4.1}
\]

and

\[
 Z_{e_i+1,d}=Q_j=M_i\cup C_i\cup\{u_j\}.
\tag{4.2}
\]

The intervals in (4.1)--(4.2) have the same left endpoint; (4.2) adds only
the new physical position (e_i+1).  Since (u_j\notin M_i), its source
support is forced:

\[
 \boxed{u_j\in A_{e_i+1}.}
\tag{4.3}
\]

On the other hand, the next flag minimum (M_j) omits its distinguished
label (u_j).  If its flag endpoint is (e_j), then

\[
 u_j\notin A_p
 \qquad(e_j-d+2\le p\le e_j).
\tag{4.4}
\]

### Theorem 4.1 (directed endpoint-distance obstruction)

For every arc (i\to j) in a simultaneously realized sidecar cycle,

\[
 \boxed{
 e_i+1\notin[e_j-d+2,e_j]_{\rm cyc}.}
\tag{4.5}
\]

Equivalently, for distinct endpoints, the forward cyclic distance satisfies

\[
 \boxed{\delta(e_i,e_j)\ge d.}
\tag{4.6}
\]

#### Proof

Equation (4.3) requires (u_j) at (e_i+1), whereas (4.4) forbids it
throughout the penultimate interval of flag (j).  This proves (4.5),
which is exactly (4.6).  \(\square\)

In particular consecutive or distance-two concatenation of triangle
hinges is impossible for (d\ge3), even if their outer owners are made
equal.  This obstruction uses only the saturated suffix values, not the
canonical source-letter presentation.

### Corollary 4.2 (sharp triangle span lower bound)

If the three triangle endpoints lie on a cyclic source of length (L),
then

\[
 \boxed{L\ge\left\lceil\frac{3d}{2}\right\rceil.}
\tag{4.7}
\]

#### Proof

Let the three forward distances along the directed triangle be
(\delta_x,\delta_y,\delta_z).  Their sum is (wL), where the winding
number (w) is (1) or (2).  Theorem 4.1 gives

\[
 3d\le\delta_x+\delta_y+\delta_z=wL\le2L.
\]

This is (4.7).  \(\square\)

Hence a standalone three-hinge collar cannot have (O(1)) total length as
(d\to\infty).  This does not imply an additive (\Theta(d)) cost for
every triangle in a large shared chronology: the cyclic spans of different
triangles may overlap.

## 5. The distance schedule itself has ample global room

For a large endpoint cycle of length (g), the directed-distance row is
not a scalar obstruction to a sparse triangle bank.  If (3h) flag
endpoints are needed and (3h+3d\le g), choose three disjoint blocks of
(h) endpoints near (0,\lfloor g/3\rfloor,lfloor2g/3\rfloor), and pair
equal block indices in the directed order.  After harmless rounding, all
three directed distances are at least (d).

In the PBBS regime (H/g) tends to a tiny positive constant and
(d=o(g)), so this placement condition holds with a huge margin.  The
remaining obstruction is not endpoint count; it is simultaneous source
support and protected-owner compatibility.

## 6. Exact remaining occurrence-packing condition

Fix proposed flag endpoints and all required hinge/owner/q1/upper
intervals.  For a coordinate (c), let

* (\mathcal I_c^+) be the required intervals whose target contains (c);
* (\mathcal I_c^-) be the required intervals whose target omits (c);
* (P_c) be the set of physical positions allowed by its owner envelope
  and protected state.

### Theorem 6.1 (coordinatewise cover-free equivalence)

There is a source support for every coordinate realizing all prescribed
interval unions if and only if

\[
 \boxed{
 I\cap P_c\not\subseteq
 \bigcup_{J\in\mathcal I_c^-}J
 \quad
 (c\text{ a coordinate},\ I\in\mathcal I_c^+).}
\tag{6.1}
\]

Equivalently, every positive interval contains an allowed position which
belongs to no negative interval.

#### Proof

Any support for (c) must lie in (P_c), avoid every negative interval,
and hit every positive interval, proving necessity.  Under (6.1), choose
one point from each positive interval in

\[
 (I\cap P_c)\setminus\bigcup_{J\in\mathcal I_c^-}J.
\]

The union of the chosen points is an allowed support which hits exactly the
required positive intervals and avoids every negative interval.  The
coordinate choices are independent.  \(\square\)

After (6.1), the remaining checks are:

1. every selected length-(D) owner value has rank (m), is distinct,
   and consecutive values are Johnson neighbours;
2. the induced owner incidence words meet the run/gap residence floor;
3. the literal native successor cells (Q_j) remain pairwise usable; and
4. all upper/common-cap tickets survive.

If the common-core (G)-rail representation (3.2) is imposed, Items 1--2
are automatic once the cyclic toggle windows are simple and every toggle
run/gap has length at least (D).  Thus the sharp joint triangle target is:

\[
 \boxed{
 \text{choose endpoint triangles satisfying (4.6), a common-core rail,
 and the cover-free cuts (6.1).}}
\tag{6.2}

This is the exact occurrence-level packing condition left after named
sidecar cancellation.  Neither the cycle-cover algebra nor the individual
residence collars proves it.
