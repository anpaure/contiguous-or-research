# Common-template all-depth exchanges: a frozen global-order state and the missing nonneutral braid

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Outcome

Put

\[
 V=[2m],\qquad M=m+H,\qquad
 \mathcal A_H=\binom V{m-H},\qquad N_H=|\mathcal A_H|,
 \qquad W=\binom{2m}m,
\]

where (H=o(m)) and

\[
                         H^2/m=\log m+o(1).
\]

Fix one directed cyclic order \(\Pi\) of \(V\).
For every promotion root (A\in\mathcal A_H), put (U_A=A^c) and
select the literal frame

\[
                         \pi_A=\Pi|_{U_A}.
\tag{0.1}
\]

This gives one complete promotion ring at every root, hence exactly
(N_H=\Theta(W/m)) physical rings (or (N_H) repaired paths after one
cut per ring).  Nevertheless:

1. **Cycle exchanges are unavailable.**  No nontrivial common-core
   triangle or directed-cycle exchange is applicable to the selected
   table.
2. **Every higher cube is unavailable.**  No nontrivial checkerboard
   (2^d)-corner exchange from the all-depth higher-placeholder theorem
   is applicable, for any (2\le d\le m-H).
3. **The middle support is negligible.**  A middle target (D) occurs
   in some selected deck if and only if the cyclic (0/1) word of (D)
   in \(\Pi\) contains a run of at least (H) ones.  Consequently the
   number of covered middle targets is at most
   
   \[
       2m\binom{2m-H}{m-H}
       \le 2m,2^{-H}W=o(W).
   \tag{0.2}
   \]
4. The triangle/cycle and higher-cube moves preserve every scheduled
   physical target load.  Therefore every state reachable from (0.1)
   by these moves has the same (W-o(W)) middle holes.  In fact (0.1)
   is an isolated vertex of their nonnegative move graph.

Thus the audited common-template exchanges are not a global lag-(H)
compiler and do not turn the MSW owner-star lift into one.  The owner-star
lift supplies an incidence-wise frame witness for every (A\subset D),
whereas the exchanges are kernel moves between frame tables which are
already legal.  They neither select the first legal table from those
incidence witnesses nor change its target loads.

This is a statewise availability obstruction beyond component colouring.
It does not rule out a specially constructed balanced table, nor an
enlarged move library containing load-changing moving-hole or collision-
paying moves.  It proves that a positive theorem must contain a genuinely
nonneutral global selection/splicing step; the common-template identities
alone cannot provide it.

## 1. The global-order frame table

For a directed cyclic order \(\Pi\) and (U\subseteq V), write
\(\Pi|_U\) for the induced directed cyclic order after deleting
(V\setminus U).  For every (A\in\mathcal A_H), (0.1) is therefore a
literal cyclic frame on its (M)-top (U_A).  Its middle deck is

\[
 \mathcal D(A,\pi_A)
 =\{A\cup J:J\text{ is a cyclic (H)-interval of }\Pi|_{U_A}\}.
\tag{1.1}
\]

Any common deleted phase and any nested phase-to-depth schedule may be
attached rootwise.  All later nonavailability assertions concern the
underlying cyclic orders and are therefore independent of that schedule.

## 2. No common-core directed cycle is present

Fix an ((M-2))-set (C), two placeholder positions (P,Q) in a
common cyclic positional word on (C\cup\{P,Q\}), and an outside label
set (Z).  The fixed-core cycle sector has tops

\[
                         C\cup\{u,v\},\qquad \{u,v\}\in\binom Z2,
\tag{2.1}
\]

and orients (u\to v) when the selected frame puts (u) at (P) and
(v) at (Q).

### Theorem 2.1 (transitive-tournament obstruction)

Among the global-order frames (0.1), every physically present
fixed-core tournament is transitive.  Hence it contains no directed
cycle, and no triangle or longer cycle reversal is applicable.

#### Proof

Choose (c\in C) and cut all cyclic words immediately after (c).
The common positional template now linearly orders (P,Q).  Suppose
first that (P) precedes (Q).  If the frame on
(C\cup\{u,v\}) specializes the template as (u\) at (P), (v) at
(Q), then in the restriction of \(\Pi\), cut at the same (c), the
label (u) precedes (v).  Thus every tournament edge points forward
in one fixed linear order, namely the order induced by \(\Pi\) on (Z).
It is transitive.  If (Q) precedes (P), every edge points backward
in that same order, again giving a transitive tournament.  A transitive
tournament contains no directed cycle. \(\square\)

The conclusion applies to every possible (C), positional word, and
outside set (Z); it is not tied to a preselected template sector.

## 3. No nontrivial higher-placeholder cube is present

Consider a putative (d)-cube with common ((M-d))-set (C), disjoint
pairs

\[
                         \{a_{j,0},a_{j,1}\},\qquad 1\le j\le d,
\]

and corners

\[
 U_\epsilon=C\cup\{a_{j,\epsilon_j}:1\le j\le d\}.
\tag{3.1}
\]

The higher-cube exchange requires one common positional word and two
placeholder permutations \(\sigma,\tau\), with the selected frames equal
to the \(\sigma\)-specializations on one parity of the cube and the
\(\tau\)-specializations on the other parity.

### Theorem 3.1 (four-corner order contradiction)

If all selected frames are the global restrictions \(\Pi|_{U_\epsilon}\),
then the preceding checkerboard realization is possible only when
\(\sigma=\tau\).  Thus every applicable higher-cube exchange is trivial.

#### Proof

The critical range gives

\[
                         |C|=M-d\ge2H>0.
\]

Choose (c\in C) and cut every cyclic word immediately after (c).
Suppose \(\sigma\ne\tau\).  Two placeholder indices (r,s) then have
opposite relative order in the two permutations.  After interchanging
their names if necessary, (r) precedes (s) in \(\sigma\), while
(s) precedes (r) in \(\tau\).

Freeze all cube bits except \(\epsilon_r,\epsilon_s\).  If the frozen
parity is even, the four selected global restrictions force, in the
linear order induced by \(\Pi\),

\[
 a_{r,0}<a_{s,0}<a_{r,1}<a_{s,1}<a_{r,0}.
\tag{3.2}
\]

Indeed the four inequalities, in order, come from corners
((0,0),(1,0),(1,1),(0,1)): the even corners use \(\sigma\), and the
odd corners use \(\tau\).  Formula (3.2) is impossible in a linear
order.  If the frozen parity is odd, the roles of \(\sigma,\tau\) are
reversed and the same cyclic chain of strict inequalities results with
all directions reversed.  Hence \(\sigma=\tau\), in which case the
putative exchange has identical shores and is trivial. \(\square\)

This proof uses only one two-dimensional face of the cube.  Enlarging
the cube dimension therefore supplies no escape from the obstruction.

## 4. Exact census of the middle targets seen by one global order

Fix (D\in\binom Vm).  Traverse \(\Pi\), and between consecutive
elements of (D^c) let

\[
                         g_1,\ldots,g_m
\tag{4.1}
\]

be the numbers of elements of (D) in the corresponding open cyclic
gaps.  Thus (g_i\ge0) and \(\sum_i g_i=m\).

### Theorem 4.1 (provider count in a global-order table)

The exact number of compatible roots (A\in\binom D{m-H}) for which
the selected frame \(\Pi|_{A^c}\) contains (D) is

\[
 \boxed{
 r_\Pi(D)=\sum_{i=1}^m\binom{g_i}{H}.}
\tag{4.2}
\]

In particular (D) is covered if and only if its cyclic indicator word
in \(\Pi\) has a run of at least (H) ones.

#### Proof

For (A\subset D), put (J=D\setminus A), so (|J|=H) and

\[
                         A^c=D^c\cup J.

The set (D=A\cup J) occurs in the selected deck rooted at (A) if
and only if (J) is consecutive in \(\Pi|_{D^c\cup J}\).  Every label
of (D^c) remains in that restriction.  Therefore (J) is consecutive
if and only if all of its labels lie in one open gap between consecutive
labels of (D^c).  The (i)-th gap supplies exactly
\(\binom{g_i}{H}\) choices, and different gaps supply disjoint choices.
This proves (4.2) and its last assertion. \(\square\)

### Corollary 4.2 (negligible support)

The number of middle targets covered by the whole table is at most the
quantity in (0.2).

#### Proof

If (D) is covered, some cyclic block of (H) consecutive coordinates
of \(\Pi\) lies in (D).  There are (2m) possible starts.  For one
fixed block, the number of (m)-sets containing it is
\(\binom{2m-H}{m-H}\).  The union bound gives the first inequality in
(0.2).  Moreover

\[
 \frac{\binom{2m-H}{m-H}}{\binom{2m}m}
 =\frac{(m)_H}{(2m)_H}
 =\prod_{j=0}^{H-1}\frac{m-j}{2m-j}
 \le2^{-H}.
\]

Since (H\to\infty) faster than \(\log m\) in the critical regime,
the last expression in (0.2) is (o(W)). \(\square\)

Deleting one phase from every ring can only reduce this covered support.

## 5. The load-fibre invariant and the MSW interface

Let \(\mathsf A\) be the literal frame-column matrix whose rows are the
top markers and all scheduled physical lower, middle, and upper targets.
Every audited common-template triangle, directed-cycle, quartet, and
higher-cube exchange is an integer vector

\[
                         z\in\ker_{\mathbb Z}\mathsf A.
\tag{5.1}
\]

Therefore a sequence of such exchanges preserves \(\mathsf A x\)
exactly.  In particular it preserves the complete middle load vector,
its support, and every hole and collision multiplicity.  Theorems 2.1
and 3.1 say more for the state (0.1): no first nonzero move is available.

The exact MSW owner-star theorem gives, for every incidence (A\subset D),
an individually legal witness frame

\[
                         \Phi(A,D)=\pi_D|_{A^c}
\tag{5.2}
\]

containing (D).  This is a relation on root--target incidences, not a
selection of one common frame at each root.  In particular, at a fixed
root the witnesses \(\Phi(A,D)\) generally vary with (D).  A kernel
move such as (5.1) acts only after one has a nonnegative integral table
of complete legal frame columns.  It cannot turn the incidence relation
(5.2) into such a table, and once a table is chosen it cannot alter the
target load which must be balanced.

The global-order state makes this logical separation literal.  For each
of its (W-o(W)) missing targets, (5.2) supplies a witness at every
compatible root, but no sequence of the common-template exchanges can
insert even one of those targets: doing so would change the invariant
middle load vector.

## 6. Cut recycling

The state (0.1) already consists of exactly (N_H=\Theta(W/m)) rings,
or the same number of one-cut repaired paths.  Corollary 4.2 shows that
this optimal component count is compatible with (W-o(W)) middle holes.
Thus the component ledger and the target-load ledger are independent;
the all-depth kernel exchanges do not trade one for the other.

For comparison, the exact unchanged-row bound in the MSW interface says
that one ambient row contributes at most (H+1) consecutive owner phases
to one fixed promotion top.  Covering (W-o(W)) owner phases by unchanged
provenance pieces therefore uses at least

\[
                         (1-o(1))\frac{W}{H+1}
\tag{6.1}
\]

pieces.  Reducing these to (O(N_H)=O(W/m)) physical components requires

\[
                         \Theta(W/H)
\tag{6.2}
\]

actual cross-row splices.  The common-template exchange identities
replace already completed rings by already completed rings.  They give
no equality of MSW transition endpoints and hence no one of the splices
counted in (6.2).  Interpreting their algebraic cancellation as cut
recycling would therefore be circular: completion of the rings is a
hypothesis of the move, not its conclusion.

## 7. Precise boundary

Proved here:

1. a literal one-frame-per-root state with exactly (N_H) rings;
2. exact nonavailability of every common-template directed-cycle move;
3. exact nonavailability of every nontrivial higher-placeholder cube;
4. the exact provider formula (4.2) and the (2m2^{-H}W) support bound;
5. invariance of all holes and collisions under the audited all-depth
   exchange library; and
6. the distinction between \(\Theta(W/H)\) MSW provenance splices and
   (O(N_H)) final components.

Not proved:

1. nonexistence of a balanced promotion-frame table;
2. nonconnectivity after adding genuinely load-changing moving-hole or
   collision-paying primitives;
3. a lower bound against an adaptive construction which chooses a good
   initial legal table rather than starting from (0.1); or
4. coefficient one.

The exact missing positive primitive is consequently stronger than a
kernel/holonomy exchange.  It must simultaneously (i) select one common
lag-(H) order per root from the MSW incidence witnesses, (ii) change
the physical target load toward a squarefree near-cover, and (iii)
realize the \(\Theta(W/H)\) cross-row endpoint splices while leaving only
(O(N_H)) final components.  None of the audited triangle/cycle,
quartet, or higher-cube identities supplies any of these three steps by
itself.
