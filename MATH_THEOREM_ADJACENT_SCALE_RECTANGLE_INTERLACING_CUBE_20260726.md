# Adjacent MSW rectangle scales admit a full-capacity interlaced cube

Date: 2026-07-26

Method: pure mathematics only.

This note completes the physical compatibility gate left in
`MATH_THEOREM_MSW_ADJACENT_SCALE_CAPACITY_INTERLACING_20260726.md`.
The two adjacent rectangle catalogues do not commute in full: there is one
universal nested critical pair, and its simultaneous toggle is not even a
Johnson path.  However, the cross-scale conflict graph is a matching.
Deleting the conflicting quarter of the larger-scale catalogue leaves an
exact Boolean cube whose cardinality still strictly exceeds the worst
Catalan demand.

Put

\[
 M_r=H_{m,r+1}C_{r-1},
 \qquad
 M_{r+1}=H_{m,r+2}C_r,
\tag{0.1}
\]

where (C_j=\operatorname {Cat}_j).  Let ({\cal E}_r) and
({\cal E}_{r+1}) be the certified elementary rectangle catalogues at
the two scales.  Define

\[
 \widetilde {\cal E}_{r+1}
 =\{(C,S)\in{\cal E}_{r+1}:S\notin10D_{r-1}\}.
\tag{0.2}
\]

Then

\[
 \boxed{{\cal E}_r\ \dot\cup\ \widetilde {\cal E}_{r+1}}
\tag{0.3}
\]

is a literal exact-factor Boolean cube, and its number of bits is

\[
 \boxed{
 \widetilde M_r
 =M_r+H_{m,r+2}(C_r-C_{r-1}).}
\tag{0.4}
\]

If (r) is minimal with (C_r\ge4p), then, throughout the range of the
adjacent-scale capacity theorem,

\[
 \boxed{\widetilde M_r>{D_r\over4}.}
\tag{0.5}
\]

Thus the cardinality (L=\lfloor(D_r-c_H)/4\rfloor) can be chosen from
one actual joint exact cube.  Cross-scale physical compatibility costs no
asymptotic or constant-capacity obstruction.

## 1. The two elementary rectangles

At scale (r), a switch lives in an aligned node of semilength (r+1).
For (R\in D_{r-1}), its two local rows are

\[
                         A_R=1100R,
 \qquad                  B_R=1010R,
\tag{1.1}
\]

and it exchanges their phase-one states.  Suppressing the common
spectator set, the relevant traces are

\[
\begin{array}{c|ccc}
A_R&12Q_R&14Q_R&34Q_R\\
B_R&13Q_R&23Q_R&24Q_R.
\end{array}
\tag{1.2}
\]

At scale (r+1), the same rule is applied in a node of semilength
(r+2), with parameter (S\in D_r):

\[
                         A'_S=1100S,
 \qquad                  B'_S=1010S.
\tag{1.3}
\]

Every individual switch preserves the complete local (X)- and
(Y)-ownership ledgers.

## 2. Complete classification of adjacent-scale overlaps

### Theorem 2.1 (unique nested critical pair)

A scale-(r) switch and a scale-(r+1) switch share a row in nested
contexts if and only if, for a unique (R\in D_{r-1}), the larger
parameter is

\[
                         S=10R,
\tag{2.1}
\]

and the common row is

\[
                         B'_{10R}=10B_R=101010R.
\tag{2.2}
\]

Every switch occurs in at most one such pair.  Consequently the
cross-scale conflict graph is a matching.

#### Proof

Two distinct recursion nodes in one ordered binary tree are either
disjoint or nested.  Since their sizes are (r+1) and (r+2), a nested
size-(r+1) node must be an immediate child of the size-(r+2) node,
and the other child must be empty.

Parse the two larger fillings as binary trees.  The word (1100S) has
left subtree of size one and right subtree of size (r); it has no child
of size (r+1).  The word (1010S), on the other hand, has empty left
subtree and right-child word

\[
                         10S,
\]

of semilength (r+1).  Therefore a shared smaller switch must occur in
this right child.

For that child to be one of the two scale-(r) switch rows, one needs

\[
                         10S=1100R
 \quad\hbox{or}\quad   10S=1010R.
\]

The first equality is impossible from the first two bits.  The second is
equivalent to (S=10R), and gives (2.2).  Conversely these words plainly
give the claimed overlap.

A tree node has a unique parent, and the right child in (2.2) is unique.
Thus neither switch can occur in two conflict pairs.  The conflict graph
is a matching.  (square)

### Proposition 2.2 (the critical pair genuinely does not commute)

The simultaneous phasewise toggle of the pair in Theorem 2.1 is not a
legal path replacement.

#### Proof

Delete the common suffix (R) and all exterior spectators.  The common
row is the (D_3) root (101010), whose canonical local trace is

\[
                         135-235-245-246.
\tag{2.3}
\]

The larger rectangle changes its phase-one state from (235) to (145).
The nested smaller rectangle changes its phase-two state from (245) to
(236).  Applying both substitutions would therefore require the
consecutive middle states

\[
                         145\longrightarrow236.
\tag{2.4}
\]

They are disjoint three-sets, rather than Johnson neighbours.  Adjoining
the same spectator set to both does not change their symmetric
difference.  Hence the doubly toggled row is not a path.  In particular,
the union of the two full catalogues is not a Boolean cube.  (square)

The local obstruction is the standard nested Tamari critical pair.  Its
five-shape completion is the rooted (D_3) pentagon packet, but that
larger packet is not needed for the capacity theorem below: the matching
structure allows a cheaper deletion.

## 3. The interlaced family is an exact Boolean cube

### Theorem 3.1 (cross-scale interlacing)

Every subset of

\[
                         {\cal E}_r\dot\cup
                         \widetilde {\cal E}_{r+1}
\tag{3.1}
\]

can be toggled simultaneously, and the result is an exact middle factor
with the complete (X/Y) ownership ledgers.  Hence (3.1) is a Boolean
cube of dimension (0.4).

#### Proof

At one fixed scale, simultaneous exactness is Theorem 15.1 of the
plateau audit: equal-size nodes cannot nest, and switches in distinct
nodes have disjoint affected slabs.

Consider switches at the two different scales.  If their recursion nodes
are disjoint, their coordinate blocks and chronological slabs are
disjoint.  Even when the two switches occur in the same global row, the
changed phase of each lies one step after the start of its own block; two
disjoint blocks of sizes at least (r+1\ge3) therefore have disjoint
changed states and disjoint adjacent edges.  Their local ledger
permutations commute.

If the nodes are nested and share a row, Theorem 2.1 says that the larger
parameter has the form (S=10R).  All such larger switches were deleted
in (0.2).  Thus no selected cross-scale pair has overlapping affected
slabs.  The individual local (X/Y) multiset equalities consequently add
without interference.  Arbitrary subfamilies are exact, proving the cube
claim.

There are (H_{m,r+2}) larger parent contexts.  In each, exactly
(C_{r-1}) of the (C_r) parameters have the form (10R).  This proves
(0.4).  (square)

## 4. Exact capacity after deleting the conflicts

Let

\[
 k=m-r-1,
 \qquad
 \rho_{m,r}
 ={(k+1)(r+1)\over4(2k+1)(2r-1)},
\tag{4.1}
\]

and recall

\[
 \sigma_{m,r}={M_{r+1}\over M_r}
 ={k(2r-1)\over(2k-1)(r+1)}.
\tag{4.2}
\]

The exact Catalan quotient is

\[
 q_r={C_{r-1}\over C_r}
 ={r+1\over2(2r-1)}.
\tag{4.3}
\]

Therefore

\[
 \frac{\widetilde M_r}{M_r}
 =1+\sigma_{m,r}(1-q_r)
 =1+{3k(r-1)\over2(2k-1)(r+1)}.
\tag{4.4}
\]

Minimality of (r) with (C_r\ge4p) gives

\[
 {D_r\over4M_r}
 <{7\over64\rho_{m,r}}.
\tag{4.5}
\]

### Lemma 4.1 (the retained cube beats worst overshoot)

For every (k\ge1) and (r\ge2),

\[
 \boxed{
 1+{3k(r-1)\over2(2k-1)(r+1)}
 >{7\over64\rho_{m,r}}.}
\tag{4.6}
\]

#### Proof

After clearing the positive denominators, (4.6) is equivalent to

\[
\begin{aligned}
 &8(k+1)(7kr+k-2r-2)\\
 &\hspace{25mm}>7(4k^2-1)(2r-1).
\end{aligned}
\tag{4.7}
\]

The left side minus the right side is

\[
                         36k^2+40kr-8k-2r-23.
\tag{4.8}
\]

For (k\ge1), this is at least (5+38r>0).  (square)

Combining (4.4)--(4.6) proves

\[
                         \widetilde M_r>{D_r\over4},
\]

which is (0.5).

## 5. Consequence for the tuned critical window

Assume (c_H<D_r) and put

\[
                         L=\left\lfloor{D_r-c_H\over4}\right\rfloor.
\tag{5.1}
\]

Equation (0.5) gives (L\le\widetilde M_r).  Choose any (L) bits of
the exact cube (3.1).  Then, for every (q\in[r,H]), the scalar capacity
ledger from the adjacent-scale theorem gives

\[
 K_{q,p}(F_{MSW})-(W-N_q)\ge4L.
\tag{5.2}
\]

Thus the former statement “an arbitrary subcatalogue can be tuned by
cardinality” can be strengthened to:

\[
 \boxed{
 \text{the tuned subcatalogue may be chosen inside one literal
 full-ownership exact Boolean cube}.}
\tag{5.3}
\]

This resolves the cross-scale commutation gate.  It does not orient the
four-arm vectors against the current nonlinear cap tail; the weighted
four-arm drain theorem remains logically later.

## 6. Exact boundary

The full adjacent-scale union has a genuine noncommuting obstruction, so
an unrestricted product theorem is false.  The obstruction is completely
classified and forms a matching.  Removing the larger endpoint of every
conflict retains more switches than the worst Catalan overshoot can
require.  Therefore no associahedral completion is needed for scalar
capacity or exact ownership: a pruned Boolean cube already suffices.

The next unresolved statement is not physical interlacing but selection:
orient a sufficiently large subfamily of the retained four-arm vectors so
that their negative arms drain the current overload without the positive
arms refilling it.
