# Local nonintegrality and exact cover cuts for the \(q\)-cell compiler

**Date:** 2026-08-03  
**Status:** unconditional non-TU minor on every suitable literal cell,
exact binary projection by interval-cover cuts, integral
protected-signature/nested-shell faces, and a literal local odd-cycle gap
conditional only on embedding the displayed Johnson segment in the global
carrier.  No computation is used.

## 0. Outcome

The exact mixed-integer compiler uses assignment variables \(y_{S,c}\) and
literal occurrence variables \(z_{x,h}\).  Its bare linear relaxation is
not totally unimodular.  The smallest obstruction is already local to one
cell:

\[
 \begin{pmatrix}
 1&1&0\\
 1&0&1\\
 0&1&1
 \end{pmatrix},
 \qquad \det=-2.                                      \tag{0.1}
\]

The columns are \(z_{x,h},y_{S_1,c},y_{S_2,c}\).  The first two rows say
that assigning either target, both of which omit \(x\), forbids \(x\) at
position \(h\in I_c\).  The last row is the cell capacity.  Thus

\[
 z_{x,h}=y_{S_1,c}=y_{S_2,c}=\frac12                 \tag{0.2}
\]

is admitted by the pairwise relaxation, although every integral point obeys
the missing clique inequality

\[
 z_{x,h}+y_{S_1,c}+y_{S_2,c}\le1.                    \tag{0.3}
\]

This counterexample is compatible with a fixed target rank: take two
distinct same-rank aperture-compatible targets which both omit one optional
coordinate of the cell.  It therefore survives every rank-only
specialization.

After eliminating the \(z\)'s **for binary assignments**, the exact
projection has a clean description.  Besides target and cell capacities,
it has precisely two kinds of cover cuts:

* negative assigned cell intervals may not cover one owner-supplier
  interval;
* conditional on assigning a positive target to a cell, negative assigned
  cell intervals may not cover that target-coordinate aperture.

These inequalities are necessary and sufficient on zero-one assignments.
They are the polyhedral form of the exact interval-closure theorem.

Two useful integral faces remain.

1. Once a protected occurrence system \(Z_x\) is fixed, compatible
   target-cell edges form an ordinary bipartite matching graph.
2. On nested cells and nested targets, private erosion-shell points realize
   the whole chain.  Order-preserving assignment is a unit-capacity grid
   flow.

Consequently, an all-\(k\) proof should not seek a nonexistent TU theorem
for the bare model.  It should construct a protected signature whose
matching deficiency is \(O(1)\), decompose almost all targets into protected
nested-shell faces, or control the exact interval-cover clutter.

## 1. The local triangle minor

Fix one cell \(c\), one position \(h\in I_c\), and one coordinate

\[
                         x\in E_h\setminus K_c.        \tag{1.1}
\]

Let \(S_1,S_2\) be two distinct targets of the same rank satisfying

\[
 K_c\subseteq S_a\subseteq E_c,\qquad x\notin S_a
 \quad(a=1,2).                                        \tag{1.2}
\]

Thus both assignment edges \((S_1,c)\) and \((S_2,c)\) exist.  The exact
mixed-integer system contains

\[
\begin{aligned}
 z_{x,h}+y_{S_1,c}&\le1,\\
 z_{x,h}+y_{S_2,c}&\le1,\\
 y_{S_1,c}+y_{S_2,c}&\le1.                            \tag{1.3}
\end{aligned}
\]

### Theorem 1.1 (smallest non-TU face)

The coefficient matrix of (1.3), on columns
\((z_{x,h},y_{S_1,c},y_{S_2,c})\), has determinant \(-2\).  Hence the bare
mixed assignment matrix is not totally unimodular whenever (1.1)--(1.2)
occur.

The point (0.2) satisfies (1.3) but is outside the integer hull, because
every zero-one solution satisfies (0.3).

#### Proof

The matrix is (0.1), and direct expansion gives

\[
 1(0-1)-1(1-0)=-2.                                    \tag{1.4}
\]

For a zero-one point, either \(z_{x,h}=1\), forcing both assignment
variables to zero, or \(z_{x,h}=0\), when cell capacity permits at most one
assignment variable to equal one.  This proves (0.3).  At the half point,
the left side of (0.3) is \(3/2\). \(\square\)

No two-by-two zero-one minor has determinant of absolute value greater than
one, so this three-variable triangle is the smallest possible zero-one TU
obstruction.

### Corollary 1.2 (the first missing clique cuts)

For every cell \(c\), coordinate \(x\), and position \(h\in I_c\), the
following inequality is valid for all integral compiler states:

\[
 z_{x,h}
 +\sum_{\substack{S:(S,c)\text{ is allowed}\\x\notin S}}y_{S,c}
 \le1.                                                \tag{1.5}
\]

It is the maximal-clique inequality joining one occurrence variable to all
negative alternatives of one cell.  The pairwise inequalities in the bare
formulation do not imply it fractionally.

### A full-assignment fractional extension

If each \(S_a\) has any private alternative cell \(c_a\), the local half
point extends to the target equalities by setting

\[
 y_{S_a,c}=y_{S_a,c_a}=\frac12.                       \tag{1.6}
\]

Choose the private-cell occurrence variables inside their individual
apertures and use protected exterior owner suppliers.  This gives a
feasible fractional compiler state violating (1.5).  An integral compiler
may still exist; the point is that the LP contains a point outside its
integer hull.

The aperture hypotheses are modest and carrier-literal.  Unlike a
three-overlapping-cell construction, they do not ask one target to cross
incompatible mandatory collars: both targets use the same shared cell.

## 2. Fixed integral assignments have integral occurrence realizations

The nonintegrality comes from mixing assignment alternatives, not from the
occurrence block alone.

### Theorem 2.1 (integral \(z\)-fibre)

Fix an integral target-to-cell assignment \(y\).  If the relaxed
occurrence constraints have a feasible \(z\in[0,1]\), then they have a
zero-one feasible solution.

#### Proof

For each coordinate \(x\), let

\[
 F_x=R_x\cap\bigcup_{\substack{c\text{ selected}\\x\notin S_c}}I_c,
 \qquad U_x=R_x\setminus F_x.                         \tag{2.1}
\]

Every feasible fractional occurrence vector vanishes on \(F_x\).  A
positive-cell or owner inequality with right side one can therefore be
feasible only if its interval meets \(U_x\).  Set

\[
                         z^*_{x,h}={\bf1}_{\{h\in U_x\}}.        \tag{2.2}
\]

Every negative constraint remains valid, while every positive-cell and
owner interval is hit integrally.  Mandatory footprint positions cannot be
forbidden by an aperture-compatible assignment, so source letters remain
nonempty. \(\square\)

Thus the exact obstruction after choosing \(y\) is combinatorial interval
coverage.  No denominator remains in the occurrence variables.

## 3. Exact binary projection: the cover-cut clutter

Let \({\cal E}\) be the allowed target-cell edges.  For an edge
\(e=(S,c)\), write \(y_e=y_{S,c}\) and \(I_e=I_c\).

Fix a coordinate \(x\).  A **negative edge** is one with \(x\notin S\).
For an owner occurrence \(x\in T_i\), let

\[
                         B_{x,i}=[i,i+d]_W\cap R_x.   \tag{3.1}
\]

For a positive edge \(e_0=(S_0,c_0)\), \(x\in S_0\), let

\[
                         P_{x,e_0}=I_{c_0}\cap R_x.   \tag{3.2}
\]

Both are nonempty intervals in the appropriate erosion-run lift.

### Theorem 3.1 (exact owner cover cuts)

For every family \(Q\) of negative edges satisfying

\[
                         B_{x,i}\subseteq
                         \bigcup_{e\in Q}I_e,          \tag{3.3}
\]

the inequality

\[
                         \sum_{e\in Q}y_e\le |Q|-1    \tag{3.4}
\]

is valid.

### Theorem 3.2 (exact conditional positive cover cuts)

For every positive edge \(e_0\) and every family \(Q\) of negative edges
satisfying

\[
                         P_{x,e_0}\subseteq
                         \bigcup_{e\in Q}I_e,          \tag{3.5}
\]

the inequality

\[
                         y_{e_0}+\sum_{e\in Q}y_e\le |Q|        \tag{3.6}
\]

is valid.

### Theorem 3.3 (zero-one sufficiency)

A zero-one assignment \(y\) extends to a literal factor if and only if it
satisfies

* the target and cell capacity constraints;
* every owner cover cut (3.4);
* every conditional positive cover cut (3.6).

#### Proof

If all edges of \(Q\) in (3.3) were selected, their negative intervals
would cover the complete owner supplier interval, so that owner could not
be supplied.  This proves (3.4).  If \(e_0\) and every edge of \(Q\) in
(3.5) were selected, the positive cell aperture of \(e_0\) would be covered
by negative intervals, proving (3.6).

Conversely, suppose a zero-one assignment has no literal extension.  The
simultaneous interval-closure theorem gives either a covered owner interval
or a covered positive aperture.  The selected negative intervals contain a
finite inclusion-minimal subfamily \(Q\) covering that required interval.
In the owner case the assignment violates (3.4); in the positive case it
selects \(e_0\) and violates (3.6). \(\square\)

It suffices to include inclusion-minimal interval-cover chains \(Q\).
Their members can be ordered by increasing left and right endpoints, with
successive intervals overlapping or touching.  Hence separation of a
violated cut is a one-dimensional interval-cover sweep once \(y\) is
integral.

Theorems 3.1--3.3 are an exact projection statement for binary assignments.
They do **not** assert that the relaxation containing all cover cuts is
integral.  In general it is a set-packing polytope of an interval-cover
clutter intersected with the two matching partitions.

### Theorem 3.4 (an odd cover cycle survives every exact cover cut)

On any carrier containing the segment below, the cover-cut relaxation is
not integral.  Its three-edge fixed-rank face has fractional optimum
\(3/2\) and integral optimum one.

#### Construction

Take \(d=3\) and three cells

\[
 I_1=[1,3],\qquad I_2=[2,4],\qquad I_3=[3,5].         \tag{3.7}
\]

Here is a literal Johnson realization of all apertures.  Take four
persistent coordinates

\[
                         H=\{x_{12},x_{13},x_{23},p\}
                                                               \tag{3.8}
\]

and eleven fresh coordinates \(u_{-2},u_{-1},\ldots,u_8\).  On this
15-coordinate ground set, use the local rank-eight owner segment

\[
                         T_i=H\cup\{u_i,u_{i+1},u_{i+2},u_{i+3}\}
                         \qquad(-2\le i\le5).          \tag{3.9}
\]

Then

\[
 \alpha_i=u_i,\qquad\beta_i=u_{i+4},\qquad
 E_h=H\cup\{u_h\}\quad(1\le h\le5).                  \tag{3.10}
\]

In particular the one-position mandatory footprint at \(h\) is just
\(\{u_h\}\).  Define the three rank-four targets

\[
\begin{aligned}
 S_1&=\{u_1,u_2,u_3,x_{23}\},\\
 S_2&=\{u_2,u_3,u_4,x_{13}\},\\
 S_3&=\{u_3,u_4,u_5,x_{12}\}.                         \tag{3.11}
\end{aligned}
\]

Thus \(e_i=(S_i,c_i)\) is individually aperture-compatible, all three
targets have the same rank, and the active-coordinate table is

\[
\begin{array}{c|ccc}
 &S_1&S_2&S_3\\ \hline
x_{12}&0&0&1\\
x_{13}&0&1&0\\
x_{23}&1&0&0.
\end{array}                                             \tag{3.12}
\]

The fourth persistent coordinate \(p\) is omitted by all three targets; it
only adds the same owner-cover conflicts and causes no positive-cell
obligation.  The moving coordinates \(u_h\) have their unique protected
erosion occurrences exactly where their mandatory collars require them.

Restrict to the polyhedral face on which every assignment variable other
than \(y_{e_1},y_{e_2},y_{e_3}\) is zero.  Nonnegativity makes this a genuine
face; hence a fractional point outside the integer hull of this face is also
outside the integer hull of the full formulation.

Use the owner supplier intervals

\[
 B_{12}=B_{13}=[1,4],\qquad B_{23}=[2,5].             \tag{3.13}
\]

These are legitimate un-clipped depth-three supplier intervals inside the
long runs.

#### Integral optimum

Selecting \(e_1,e_2\) makes \(I_1\cup I_2\) a negative cover of \(B_{12}\).
Selecting \(e_1,e_3\) makes \(I_1\cup I_3\) a negative cover of \(B_{13}\).
Selecting \(e_2,e_3\) makes \(I_2\cup I_3\) a negative cover of \(B_{23}\).
Thus no two edges can be selected, and the integral optimum is one.

#### Fractional optimum

Set

\[
                         y_{e_1}=y_{e_2}=y_{e_3}=\frac12.       \tag{3.14}
\]

For \(x_{12}\), take \(z_1=z_4=1/2\) and use a protected positive
occurrence at position five.  For \(x_{13}\), take
\(z_1=z_2=z_4=1/2\).
For \(x_{23}\), take \(z_2=z_5=1/2\) and a protected positive occurrence
at position one.  Put \(z_{p,h}=1/2\) for \(1\le h\le5\).  For a moving
coordinate \(u_h\), put \(z_{u_h,h}=1\); every selected cell containing
position \(h\) also contains \(u_h\) in its target by (3.11).  Extend every
coordinate by its maximal allowed exterior erosion occurrences.

Every negative inequality has the form \(z_h+1/2\le1\).  Each owner interval
in (3.13) has \(z\)-mass at least one, and every selected positive cell has
\(z\)-mass at least \(1/2\).  Hence (3.14) extends to the bare LP.

The exact owner cover cuts on this face are

\[
 y_{e_1}+y_{e_2}\le1,\qquad
 y_{e_1}+y_{e_3}\le1,\qquad
 y_{e_2}+y_{e_3}\le1.                                \tag{3.15}
\]

Any conditional positive-aperture cover cut has at least these edges plus
its positive edge and is also satisfied by (3.14).  Therefore the point
survives **all** cuts from Theorems 3.1--3.2 and has objective \(3/2\).

The missing integer-hull inequality is the odd-cycle cut

\[
                         y_{e_1}+y_{e_2}+y_{e_3}\le1. \tag{3.16}
\]

This proves that exact local cover cuts characterize zero-one feasibility
but do not make their linear relaxation integral. \(\square\)

The construction is a literal depth-three Johnson segment.  It is local:
the theorem applies to any complete carrier containing this segment, and
does not assert here that a prescribed segment extends to a complete-layer
Hamilton carrier.  It does not require one target to be legal on overlapping
cells.

### Theorem 3.5 (perfect binary-cover faces are integral)

Restrict to a face on which every inclusion-minimal owner or conditional
positive cover obstruction has two assignment edges.  Form the conflict
graph \(G_{\rm cov}\) whose vertices are the remaining assignment edges,
joining two vertices when

* they use the same target or the same cell; or
* selecting them together is one of the two-edge cover obstructions.

Then zero-one realizable assignments are exactly the stable sets of
\(G_{\rm cov}\).  If \(G_{\rm cov}\) is perfect, its stable-set polytope is
described by the nonnegativity constraints and all clique inequalities.
Consequently maximum-cardinality compilation on this face has an integral
LP.

#### Proof

Target and cell capacities are precisely conflict edges inside their
respective cliques.  Under the rank-two obstruction hypothesis, Theorem
3.3 adds no forbidden set larger than a pair.  Hence a zero-one assignment
is realizable exactly when it is a stable set.

For a perfect graph, the stable-set polytope is cut out by nonnegativity and
clique inequalities.  Applying that theorem to \(G_{\rm cov}\) proves
integrality. \(\square\)

Thus bipartite, interval, and chordal conflict faces are tractable after
their maximal clique cuts are installed.  The triangle in Theorem 3.4 is
itself perfect; its missing maximal-clique inequality is exactly (3.16).
The genuine next obstruction is therefore either a nonperfect cover graph
(an odd hole or antihole) or a minimal cover hyperedge of size at least
three.

## 4. The fixed protected-signature face is TU

Fix occurrence sets

\[
                         Z_x\subseteq R_x              \tag{4.1}
\]

which contain all mandatory footprint positions and hit every owner
supplier interval.  They define the exact cell signature

\[
                         V_Z(c)=\{x:I_c\cap Z_x\ne\varnothing\}.
                                                               \tag{4.2}
\]

Retain only edges

\[
 {\cal E}_Z=\{(S,c):K_c\subseteq S\subseteq E_c,\ S=V_Z(c)\}.   \tag{4.3}
\]

### Theorem 4.1 (protected-signature matching)

Every matching in \({\cal E}_Z\) is simultaneously realizable by the one
fixed factor

\[
                         A_h=\{x:h\in Z_x\}.           \tag{4.4}
\]

The target-to-cell polytope on \({\cal E}_Z\) is the bipartite matching
polytope and is integral.

#### Proof

Equation (4.2) is exactly the union of (4.4) over the cell interval.  Owner
hitting makes (4.4) a factor.  Hence every retained assignment edge is
compatible with the same occurrence state, independently of every other
retained edge.  What remains are only the two matching partitions, whose
incidence matrix is totally unimodular. \(\square\)

### Corollary 4.2 (bounded-defect signature criterion)

If some protected occurrence system \(Z\) has a matching in
\({\cal E}_Z\) which covers all but \(C\) lower targets, the literal lower
compiler defect is at most \(C\).

This is the cleanest TU route to an additive constant: choose the physical
signature first, then use ordinary matching only as the terminal allocator.

## 5. A nested private-shell network-flow face

There is a constructive way to produce a protected signature on nested
cells.  In one linear erosion-run lift, let

\[
                         I_1\subsetneq I_2\subsetneq
                         \cdots\subsetneq I_m          \tag{5.1}
\]

and prescribe nested targets

\[
                         S_1\subseteq S_2\subseteq
                         \cdots\subseteq S_m.          \tag{5.2}
\]

Put \(I_0=\varnothing\).  For a coordinate occurring in the target chain,
let

\[
                         \tau(x)=\min\{t:x\in S_t\}.   \tag{5.3}
\]

### Theorem 5.1 (nested private-shell realization)

Assume all individual apertures.  Suppose that every coordinate appearing
in the chain has a protected shell point

\[
 p_x\in (I_{\tau(x)}\setminus I_{\tau(x)-1})\cap R_x, \tag{5.4}
\]

and every owner occurrence has a protected supplier point lying in none of
the chain cells whose target omits that coordinate.  Then all chain targets
are simultaneously realizable.

#### Proof

Place \(x\) at \(p_x\).  If \(t<\tau(x)\), then
\(I_t\subseteq I_{\tau(x)-1}\), so \(p_x\notin I_t\).  If
\(t\ge\tau(x)\), then \(I_{\tau(x)}\subseteq I_t\), so \(p_x\in I_t\).
Thus one shell occurrence gives exactly the required membership pattern

\[
                         0,\ldots,0,1,\ldots,1.        \tag{5.5}
\]

Add the protected owner suppliers and mandatory footprints.  None enters a
negative chain cell, so the protected-occurrence theorem applies. \(\square\)

The shell condition is sharp for this one-entry construction: a coordinate
which first appears at level \(t\) needs an occurrence in \(I_t\) but no
occurrence in \(I_{t-1}\).

### Integral order-preserving assignment

Suppose candidate targets form inclusion chains, candidate cells form
nested chains, and admissible assignments must preserve their orders.
Make a directed acyclic graph whose states are admissible matched pairs
\((a,b)\), meaning that target \(a\) is placed on cell \(b\).  Join
\((a,b)\) to \((a',b')\), \(a<a'\), \(b<b'\), precisely when every
coordinate introduced between targets \(a\) and \(a'\) has a protected
point in the shell \(I_{b'}\setminus I_b\), and the retained owner anchors
remain protected.  Add a source and sink with the analogous boundary
tests.

An order-preserving protected assignment is exactly a path in this DAG.
Unit-capacity path flow is integral.  Giving an arc the number of targets
skipped between its endpoint states makes shortest path compute the exact
number of omitted targets.

Separated copies compose: if every owner interval meets at most one chain
support, the product of their grid flows remains integral and their literal
factors can be superposed.  If the total number of vertical steps is
\(C\), the lower compiler defect is at most \(C\).

## 6. Consequence for the integral rotor programme

The bare mixed LP cannot round the stationary fractional rotor: it already
misses the local clique inequalities (1.5), before any long cover chain,
owner topology, or upper-shadow constraint is considered.  Fixing target
ranks does not repair this.

The exact proof-safe alternatives are now:

1. build a protected occurrence system whose signature graph has matching
   deficiency \(O(1)\);
2. decompose all but \(O(1)\) targets into separated nested-shell flow
   faces; or
3. prove bounded integral deficiency for the matching polytope strengthened
   by every minimal owner and positive-aperture cover cut.

The first two would immediately close the lower compiler up to \(O(1)\).
The third is the precise remaining polyhedral conjecture.  This note proves
neither global construction; it rules out only the unstrengthened TU
shortcut and gives exact replacement cuts.
