# Zero-defect PBBS absorption: exact palette recycling, run sealing, and the real obstruction

Date: 2026-07-31  
Status: proved reduction and obstruction lemmas; the all-
\(k\) zero-defect existence assertion remains open

Throughout let

\[
 k=2m+1,\qquad r=m+1,\qquad
 W=\binom{k}{r},\qquad d=d(k),
\]

and let

\[
 \Delta(k)=dW+\binom{d+1}{2}-(2^{2m}-1)
\]

be the exact deadline slack.  Let \(F\) be a lower-q1-exact Johnson
2-factor on \(\binom{[k]}r\), in particular the balanced PBBS
two-extension factor or an alternating-circuit transform of it.

The purpose of this note is exact equality, not an additive constant.  Every
deleted lower colour must be recycled or installed in an existing boundary
cell, every upper target must retain or gain a witness, and the deadline and
common-cap ledgers must have zero residual defect.

## 1. The Catalan-third slack heuristic is false

The finite data suggested

\[
                         \Delta(2m+1)>\operatorname{Cat}_m/3.
\tag{1.1}
\]

It is not an all-dimensional inequality.  The exact instance

\[
 m=225669,\qquad k=451339,\qquad d=421
\]

satisfies

\[
                         3\Delta(k)<\operatorname{Cat}_m,
\]

more precisely

\[
 \left\lfloor10^{12}\frac{\Delta(k)}{\operatorname{Cat}_m}\right\rfloor
 =62419986187.
\]

This is an integer calculation using

\[
 W=\binom{451339}{225669},\qquad
 \operatorname{Cat}_m=W/451339,
\]

not a floating-point extrapolation.  The compact exact audit records bit
lengths and SHA256 digests of the three large integers:

    scratch/audit_slack_catalan_third_counterexample_20260731.py
      SHA256 f0ba582b1334b6d91593e0b0ca357ef47c93012f7718be1f66fdfcd4e4c10795
    scratch/slack_catalan_third_counterexample_20260731.audit.json
      SHA256 55393a2f1c446c96b9b71e1446014d0b35471b306e37e7ff6ca91b354cdb8fd0
      payload e1c9761dd08129c7158ef070c5f1f322efcdd382a505478da21717da0c043b02

Thus a general proof cannot pay one unit of scalar slack for each member of
a \(\operatorname{Cat}_m/3\)-sized component family.  Component opening has
to be palette-neutral, and its run cost must be sealed or charged to the
*actual* deadline functional rather than to this empirical inequality.

## 2. Destination-colour recycling

Cut any number of edges of \(F\).  Orient the resulting fragments.  For
each fragment \(P_j\), write

* \(h_j\) for its first owner and \(t_j\) for its last owner;
* \(C_j\) for the colour of the deleted source edge immediately preceding
  \(h_j\) in the chosen source orientation.

Then \(C_j\subset h_j\), \(|C_j|=r-1\), and all \(C_j\)'s are distinct.
Define the destination-colour digraph \(D\) on the fragments by

\[
                      i\longrightarrow j
             \quad\Longleftrightarrow\quad C_j\subset t_i.
\tag{2.1}
\]

### Lemma 2.1 (self-recycling seam)

If \(i\ne j\) and \(i\to j\) in \(D\), then \(t_i h_j\) is a Johnson
edge and

\[
                         t_i\cap h_j=C_j.
\tag{2.2}
\]

Consequently, a directed Hamilton path

\[
                 j_1\longrightarrow j_2\longrightarrow\cdots
                 \longrightarrow j_b
\tag{2.3}
\]

gives a braid whose seam colours are exactly

\[
                         \{C_{j_2},\ldots,C_{j_b}\}.
\]

Relative to the original exact lower palette, the final internal palette
therefore contains every colour exactly once except \(C_{j_1}\), with no
excess colour.

#### Proof

Both \(t_i\) and \(h_j\) are rank-\(r\) supersets of the rank-\((r-1)\)
set \(C_j\).  They are distinct because different fragments have disjoint
owner sets.  Hence they are the two sets \(C_j+x\) and \(C_j+y\), with
\(x\ne y\), proving (2.2).  The seam entering \(P_j\) consequently restores
the deleted colour assigned to that destination.  Every noninitial fragment
has one predecessor in (2.3), so all deleted colours except the initial one
return once.  Distinct destinations have distinct deleted colours. \(\square\)

This removes the apparent three-resource Latin constraint: in this
restricted but natural normal form, choosing distinct destination heads
already makes the recycled colours distinct.

### Lemma 2.3 (full-fragment quotient)

Cut every factor edge, so every fragment is one middle owner.  Orient every
source factor cycle and assign each deleted colour to the singleton head
following it.  After deleting the resulting loops, the destination-colour
digraph is \((r-1)\)-regular in both directions and strongly connected.
Moreover, it has a directed Hamilton cycle if and only if the assigned
colour-to-head perfect matching extends to a Hamilton cycle of the middle-
levels incidence graph.

#### Proof

Every rank-\((r-1)\) colour lies in exactly
\(k-r+1=r\) middle owners.  One is its assigned head and gives a loop; the
other \(r-1\) give incoming arcs.  Every middle owner contains exactly
\(r\) colours, exactly one of which is assigned to that owner, so deleting
loops also leaves outdegree \(r-1\).

The full incidence graph is connected.  Contracting the assigned perfect
matching produces the underlying undirected destination graph; removing
the contracted loops does not remove any edge between distinct contracted
vertices.  Hence that underlying graph is connected.  Equal indegree and
outdegree at every vertex then make the directed graph strongly connected.

Finally, a destination arc is precisely a nonmatching incidence followed by
the assigned matching incidence into its head.  Alternating a directed
Hamilton cycle with those matching edges gives a middle-levels Hamilton
cycle containing the assigned matching, and contraction gives the converse.
\(\square\)

Thus even the lower-only full-fragment problem is not ordinary connectivity:
it is the perfect-matching extension problem for the middle-levels graph.
The lemma supplies regularity and strong connectivity unconditionally, but
neither property alone forces Hamiltonicity.

### Lemma 2.2 (the remaining root colour is halo-compatible)

Suppose the braid is a flat depth-\(d\) carrier and let \(T_0=h_{j_1}\).
The missing colour \(C_{j_1}\) may be placed in the leftmost source cell
without changing \(D^dA=T\), provided the other left-halo cells initially
take their maximal erosion values.

#### Proof

The first retained adjacency, whether internal to the first fragment or the
first seam after a singleton fragment, has a colour \(R\ne C_{j_1}\).
Both are facets of \(T_0\), so \(C_{j_1}\cup R=T_0\).  The maximal erosion
has \(P_0=T_0\) and \(P_1=R\).  Replacing \(P_0\) by \(C_{j_1}\) preserves
the first full-window union, and position zero belongs to no other full
window. \(\square\)

The lemma is individual derivative compatibility.  A full compiler must
retain this pin simultaneously with all other lower targets.

## 3. Why the primitive merge is a hexagon, not a 2-switch

### Lemma 3.1 (no off-diagonal recycling 2-switch)

Two distinct arcs \(i\to a\), \(j\to b\) of (2.1) cannot be replaced by
both cross arcs \(i\to b\), \(j\to a\) when the two tails are distinct and
\(C_a\ne C_b\).

#### Proof

The two cross conditions would make each rank-\(r\) tail contain both
rank-\((r-1)\) sets \(C_a,C_b\).  If their union has rank greater than
\(r\), no such tail exists.  If it has rank \(r\), the only possible tail
is \(C_a\cup C_b\), forcing \(t_i=t_j\). \(\square\)

### Lemma 3.2 (the first nontrivial switch is the incidence hexagon)

Suppose three old destination assignments are replaced by the opposite
cyclic assignment and all six corresponding arcs satisfy (2.1), with three
distinct tails.  Then there are a rank-\((r-2)\) set \(S\) and distinct
\(a,b,c\notin S\) such that the deleted colours are

\[
                 S+a,\qquad S+b,\qquad S+c,
\]

and the three tails are

\[
                 S+a+b,\qquad S+b+c,\qquad S+c+a.
\]

Thus the move is exactly an alternating incidence hexagon.

#### Proof

Every tail contains the two colours assigned to it before and after the
switch, so the three colours are pairwise adjacent in the Johnson graph on
rank-\((r-1)\) sets.  Such a triangle is either a star with a common
rank-\((r-2)\) core, or a top consisting of three facets of one rank-\(r\)
set.  In the top case every pairwise union is that same rank-\(r\) set,
contradicting distinct tails.  The star case gives the displayed six
vertices. \(\square\)

Hence palette-neutral component collapse must use transversal hexagons or
longer alternating circuits.  A proof based on ordinary alternating
2-switches cannot work in this incidence geometry.

### Corollary 3.3 (protected-collapse induction)

The original successor relation of the cut source cycles is a
self-recycling directed cycle cover in \(D\).  Toggling a destination-colour
hexagon whose three selected arcs lie in three different cover cycles merges
those cycles into one and preserves every lower colour.  Therefore, if a
protected transversal hexagon remains available whenever the current cover
has at least three cycles, iteration reaches one cycle when the initial
count is odd and two cycles when it is even.

#### Proof

The deleted edge immediately before each fragment head joins that head to
the tail of its original predecessor, so every original successor is an arc
of (2.1) carrying the destination's colour.  Lemma 3.2 identifies a
three-arc reassignment with the incidence hexagon.  Cutting one selected arc
from each of three directed cycles and inserting the opposite three arcs
concatenates their three paths into one cycle, decreasing the count by two.
Repeat. \(\square\)

The word “protected” is load-bearing: the corollary is unconditional for
the lower palette and conditional only on retaining the upper/run/compiler
decorations at each chosen endpoint.

## 4. Exact extension of a protected partial bank

Let \(G=(\mathcal L,\mathcal M;E)\) be the consecutive-level incidence
graph and let \(P\subseteq E\) be prescribed protected incidences with
\(\deg_P(v)\le2\).  For \(A\subseteq\mathcal L\) and
\(B\subseteq\mathcal M\), put

\[
 \Gamma(A,B)=e_G(A,\mathcal M\setminus B)-2(|A|-|B|).
\tag{4.1}
\]

### Theorem 4.1 (oriented Hall rectangle)

The partial bank \(P\) extends to a spanning degree-two factor if and only
if, for every \(A\subseteq\mathcal L\), \(B\subseteq\mathcal M\),

\[
                       e_P(\mathcal L\setminus A,B)
                       \le \Gamma(A,B).
\tag{4.2}
\]

#### Proof

Give every vertex residual demand \(b(v)=2-\deg_P(v)\) and seek a
bipartite \(b\)-matching in \(G-P\).  The total demands on the two shores
are equal.  The max-flow cut condition is

\[
 b(A)\le e_{G-P}(A,\mathcal M\setminus B)+b(B).
\]

Expanding the three residual terms and cancelling the incidences of \(P\)
inside \(A\times B\) gives exactly (4.2). \(\square\)

Thus every failure of the degree-two completion stage has one explicit
oriented Hall rectangle.  Connectivity and the protected upper/run labels
remain additional requirements.

## 5. Cutting short runs and sealing their fragments

For a cyclic positive coordinate run \(R\), let \(\overline E(R)\) be its
closed edge span: the edge entering the run, its internal edges, and the edge
leaving it.

### Lemma 5.1 (short-run transversal)

If a cut set meets \(\overline E(R)\) for every cyclic positive run of
length at most \(d\), then every positive run of length at most \(d\) in an
individual opened fragment touches a fragment boundary.

#### Proof

An internal run in a fragment is an unchanged cyclic run whose entering,
internal, and leaving edges were all retained.  This is excluded for every
short cyclic run by the hitting assumption. \(\square\)

For an oriented fragment and coordinate \(x\), record its positive prefix
and suffix lengths, capped at \(d+1\).  Call a seam **\(d\)-sealed** if,
for every coordinate with a positive boundary piece, the suffix/prefix block
completed or joined at that seam has total length at least \(d+1\).  This is
a local sufficient condition; the exact run monoid permits additional safe
seams through all-one fragments.

### Lemma 5.2 (zero deadline particles)

If the cuts satisfy Lemma 5.1 and every seam of a linear braid is
\(d\)-sealed, then the final chronology has no internal positive run of
length at most \(d\).  Consequently its exact terminal-start deadline debt
is zero.

#### Proof

Every internal final run is either wholly internal to one fragment, which is
long by Lemma 5.1, or uses a fragment boundary.  In the second case the seam
at which it is joined or completed certifies length at least \(d+1\).
Boundary-truncated runs at the two ends are free.  Therefore all latest
short-run frontiers vanish, and the exact debt formula gives zero. \(\square\)

More generally, the sealed condition may be replaced by the exact composed
run-monoid replay and the inequality

\[
                 \min_{\alpha}{\mathsf R}^{\alpha}_d(T)\le\Delta(k).
\tag{5.1}
\]

Unlike a component-count charge, (5.1) is the actual deadline-particle
condition.

There is also an exact cut-only formulation of the tension with upper
protection.  Let \(\mathscr R_d\) be the hypergraph of closed edge spans of
all cyclic short runs, and for an upper target \(Z\) let \(\mathscr W(Z)\)
be the hypergraph of edge spans of all its old cyclic witnesses.  Before
using any seam restoration, a cut set \(K\) simultaneously removes every
cyclic short run and preserves every upper target if and only if

\[
 K\in\operatorname{Tr}(\mathscr R_d)
 \quad\hbox{and}\quad
 K\notin\operatorname{Tr}(\mathscr W(Z))
       \quad\text{for every upper }Z.
\tag{5.2}
\]

Here \(\operatorname{Tr}(\mathscr H)\) denotes the family of sets meeting
every edge of the hypergraph \(\mathscr H\).

Indeed the first statement is exactly Lemma 5.1, while the second says that
some witness span of \(Z\) avoids all cuts.  Thus failure of (5.2) is a
literal red--blue transversal obstruction, not a shortage of scalar slack.
Suffix--prefix seam service enlarges the blue witness family by the exact
gain formula and is the only way around such an obstruction without changing
the factor.

As a crude but sometimes useful corollary, if \(|K|=b\) and every upper
target has \(b+1\) pairwise edge-disjoint old witness spans, then the second
half of (5.2) holds automatically: \(b\) edges cannot meet all members of
that reserve.  The PBBS theorem currently supplies support, not this much
edge-disjoint multiplicity, so this is a sufficient calibration rather than
the missing all-\(k\) result.

## 6. A shallow maximal-erosion identity

Let a flat chronology \(T_0,\ldots,T_{W-1}\) have every internal positive
coordinate run of length at least \(d+1\), and let

\[
 P_p=\bigcap_{\max(0,p-d)\le t\le\min(p,W-1)}T_t,
 \qquad0\le p<W+d
\tag{6.1}
\]

be its maximal erosion.

### Lemma 6.1 (protected intersections compile canonically through depth d)

If \(0\le q\le d\) and

\[
                         R=\bigcap_{t=i}^{i+q}T_t,
\tag{6.2}
\]

then

\[
                         \boxed{
 R=\bigcup_{p=i+q}^{i+d}P_p.}
\tag{6.3}
\]

#### Proof

Every physical position \(p\in[i+q,i+d]\) belongs to all source windows
indexed by \(i,\ldots,i+q\).  Hence \(P_p\subseteq R\).

Fix \(x\in R\), and let \([a,b]\) be the positive run of \(x\) containing
\([i,i+q]\).  For an internal run, the positions at which the maximal
erosion may contain \(x\) form \([a+d,b]\).  This interval meets
\([i+q,i+d]\), because \(a\le i\) and \(b\ge i+q\).  If the run touches a
carrier boundary, the corresponding safe interval is clipped outward and
the same intersection conclusion is immediate.  Thus every \(x\in R\)
appears in at least one term on the right of (6.3). \(\square\)

This gives canonical candidate intervals for all protected lower decks down
to rank \(r-d\), including every retained or recycled q1 colour.  It does
not by itself prove that shrinking the maximal erosion to install deeper
targets preserves all these candidates simultaneously; that is the exact
common-cap coupling.

## 7. Zero-defect absorption theorem

### Theorem 7.1

Suppose an alternating-circuit transform of the PBBS balanced
two-extension factor admits a cut and fragment system with the following
properties.

1. **Exact lower recycling.**  Its destination-colour digraph has a directed
   Hamilton path, and the corresponding seams are used.
2. **Exact upper protection.**  Every target above rank \(r\) has either a
   cut-free old witness span or a suffix--prefix witness in the final braid.
3. **Exact flat deadline capacity.**  The composed chronology has no internal
   positive run of length at most \(d\).  Lemmas 5.1--5.2 are a sufficient
   local way to obtain this.
4. **Exact common cap.**  `COMP_d(T)` is feasible with the one missing root
   colour pinned in the left halo.

Then

\[
                              \boxed{\nu(k)=B(k)}.
\]

#### Proof

Lemma 2.1 leaves exactly one lower-q1 colour missing from the internal
palette, and Lemma 2.2 makes its boundary pin derivative-compatible.
Condition 3 gives the flat identity \(D^dA=T\).  Condition 4 supplies every
lower target and realizes the middle chronology.  Condition 2 and the
staircase transfer identity supply every upper target.  Hence a word of
length \(W+d=B(k)\) is universal; combine with the proved deadline lower
bound. \(\square\)

Every clause has zero residual defect.  In particular no target is appended,
so this theorem addresses the exact identity rather than \(B(k)+O(1)\).

There is an exact nonflat variant: replace clauses 3--4 by a chain-aligned
monotone start/deadline schedule whose arbitrary-start loss is at most
\(\Delta(k)\), together with a feasible staircase common cap (including the
root-colour pin).  The residence-corridor and transfer theorems then give the
same conclusion.  This is the correct formulation when deadline particles
are absorbed rather than eliminated; the scalar inequality (5.1) alone is
not a substitute for the integral common cap.

## 8. The precise remaining obstruction

The arithmetic component budget is not the obstruction: (1.1) is false,
and Lemma 2.1 shows how arbitrarily many cuts can in principle be
q1-neutral.  The irreducible combinatorial gate is the simultaneous
existence of a path in the **protected destination-colour digraph**:

* vertices are oriented fragments;
* an arc \(i\to j\) must satisfy \(C_j\subset t_i\);
* its endpoint run state must be legal for (5.1);
* its retained and gained spans must participate in a complete upper witness
  assignment; and
* the resulting chronology must pass the common cap.

Ignoring decorations, Hall's condition on tails versus destination colours
produces a self-recycling cycle cover.  Lemma 3.1 shows that two-cycle swaps
cannot merge its cycles.  The first possible palette-neutral merger is the
transversal incidence hexagon of Lemma 3.2; more generally one needs a
transversal alternating circuit.  Thus the first exact routing obstruction
is:

> a protected self-recycling cycle cover with more than two cycles for which
> every cross-cycle alternating circuit destroys a required upper witness,
> violates the exact run threshold, or enters a common-cap Hall rectangle.

This is materially sharper than “not enough slack” or “too many PBBS
components.”  It identifies the correlation theorem an all-dimensional
proof must establish: protected transversal alternating circuits must remain
available until one self-recycling path (or a two-ended equivalent) is
obtained.

At K17 the finite service matching has already passed progressively stronger
faces: all 1,838 deep holes have distinct endpoint providers; a protected,
colour-recycled assignment exists; and the remaining computation is exactly
the neutral-seam/path completion followed by the deadline/common-cap replay.
Those finite successes support the obstruction statement but are not used in
the proof of Theorem 7.1.

The local set identities in Lemmas 2.1, 3.1--3.2, and 6.1 also have a
finite exhaustive replay at \(k=5,7\) and on every binary trace of length at
most eight and depth at most three:

    scratch/audit_zero_defect_absorption_lemmas_20260731.py
      SHA256 ef4232d497a1e0281930debebad1e152ebbb1fa4984d7b5c93225f681abadc4c
    scratch/zero_defect_absorption_lemmas_20260731.audit.json
      SHA256 7c2dabac17c1c15c2291725d082e4affeb9046e7d6c728da7cd0447f8c5cb6ff
      payload 04e302469a03fe7a90b4955c8af67a298ed30dda285ff612a087c9211c2d8c15
