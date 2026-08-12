# Rank-twisted macroblock packet tiling

Date: 2026-07-26

## 0. Result

The Gaussian Hall theorem for a fixed quartet decomposition forces a
successful (Q_r)-packet factor to contain many axes crossing those
quartets.  This note gives an exact owner tiling meeting that crossing-axis
toll with maximal slack.

Partition almost all coordinates into blocks

\[
                         B_j=A_j\mathbin{\dot\cup}C_j,
 \qquad |A_j|=|C_j|=d,                              \tag{0.1}
\]

where (d=\Theta(\log m)).  At local rank (k), use a perfect matching
(M_{j,k}) between (A_j) and (C_j), with the matching twisted as a
function of (k).  The status cells of (M_{j,k}) partition the local
rank-(k) layer into physical cubes.  Tensor all local cells, and split
every product cube of dimension at least (r) into parallel (Q_r)'s.

### Theorem 0.1 (dense-cross owner near-factor)

Let (d\to\infty), (d=m^{o(1)}), and

\[
                         r=o(m),\qquad
 {m\over d}\log d=o(m).                            \tag{0.2}
\]

For example one may take (d=\lceil10\log_2m\rceil) and
(r=m^{3/5+o(1)}).  There is an owner-disjoint family of physical
(Q_r) packets in (\binom{[2m]}m) whose leave satisfies

\[
                         L\le2^{m+o(m)}=o(W/H)      \tag{0.3}
\]

for every (H\le m), where (W=\binom{2m}m).  Every active packet axis
joins the two halves of one macroblock.  Hence, relative to any base
partition refining those halves, every packet has

\[
                              s(P)=r                \tag{0.4}
\]

physically crossing axes.  In particular every nonempty depth-(q)
window contains exactly (q) such axes and the occurrence toll
(s=\Omega(r/q)) is satisfied with room.

The construction is not one fixed global-frame status factor.  Choosing

\[
                 M_{j,k}=\{a_{j,i}c_{j,i+k\pmod d}:i\in\mathbb Z_d\}
\tag{0.5}

makes the frame depend on the local owner rank; as (k) varies, the
local frame union is the complete bipartite graph (K_{d,d}).

The theorem proves owner packing and dense physical frame motion.  It
does not prove the simultaneous colored target condition.  Its exact
remaining gate is the Hall/floor-energy calculation for the rank-twisted
status atlas.

The independent audit
`MATH_AUDIT_RANK_TWISTED_MACROBLOCK_COMPATIBILITY_KERNEL_20260726.md`
verifies the owner partition and leave.  To make (0.4) refer to the fixed
quartet decomposition in the full-internal Hall theorem, choose (d) as a
multiple of four and make every half (A_j,C_j) a union of old quartets.
It also derives the exact compatibility kernel.  The selected-tiling Hall
ratio is not yet determined because the deterministic (r)-axis selector and
the physical-to-compiler direction bijection are unspecified; those choices
must be included in any colored theorem.

## 1. Local rank-twisted cells

Fix one block (B=A\dot\cup C) with

\[
 A=\{a_i:i\in\mathbb Z_d\},\qquad
 C=\{c_i:i\in\mathbb Z_d\}.                        \tag{1.1}
\]

For (0\le k\le2d), let (M_k) be any perfect matching from (A) to
(C); (0.5) is the concrete choice used below.  For a local (k)-set
(X\subseteq B), record, on every edge of (M_k), whether (X) contains
zero, one, or two endpoints.  Fixing all zero/two statuses and leaving the
one-endpoint statuses free gives a physical orientation cube.  Toggling a
free edge preserves local rank, so the whole cell remains inside the
rank-(k) layer.

Distinct status vectors are disjoint and every (k)-set has one status
vector.  Thus these cells partition (\binom Bk).  Taking their union over
all (k) partitions (2^B).  The dependence of (M_k) on (k) is legal
because different local ranks are disjoint and no cube move changes (k).

For the cyclic choice (0.5), the union of the local frames is (K_{d,d}):
for every (i,j), the edge (a_ic_j) occurs when
(k\equiv j-i\pmod d).  Thus the local atlas has no single completed
matching frame common to all rank layers.

## 2. Global product cells

Partition all but at most (2d-1) coordinates into

\[
                         b=\left\lfloor{m\over d}\right\rfloor
\tag{2.1}

blocks of the form (0.1).  Freeze the residual coordinates exactly.
Tensor the local rank-twisted status partitions.  A product cell is a
physical (Q_S), where (S) is the total number of flexible matched
pairs over all blocks.  Its local rank vector and its total global rank
are fixed.  Hence the product cells restrict to a partition of the middle
layer.

If (S\ge r), choose a deterministic (r)-subset of its axes.  Freezing
the other (S-r) orientations in all possible ways partitions the cell
into parallel physical (Q_r)'s.  Applying this in every such middle
cell gives an exact owner matching on the good cells.

Every selected axis is an edge of some (M_{j,k}), hence has one endpoint
in (A_j) and the other in (C_j).  This proves (0.4).

## 3. Exponentially small low-dimension leave

The only uncovered owners lie in product cells with (S<r).  We bound
all subsets with this property before conditioning on the middle rank.

Fix a complete local-rank vector

\[
                         \mathbf k=(k_1,\ldots,k_b).              \tag{3.1}
\]

It fixes one perfect matching (M_{j,k_j}) in every macroblock, hence one
global matching on the (2db) nonresidual coordinates.  Under a uniform
unconditioned subset, the number of flexible pairs for this fixed matching
has distribution

\[
                         S\sim\operatorname{Bin}(db,1/2).       \tag{3.2}
\]

Indeed a pair is flexible in two of its four endpoint states, independently
over matching edges.  Since (db=m+O(d)) and (r=o(m)),

\[
 \Pr(S<r)=2^{-m+o(m)}.                              \tag{3.3}
\]

The number of possible vectors (3.1) is at most

\[
                         (2d+1)^b
   =\exp\!\left(O\!\left({m\log d\over d}\right)\right)
   =2^{o(m)}.                                       \tag{3.4}
\]

For a vector (mathbf k), the subsets actually inducing that vector are
a subset of the full sample space used in (3.2), so a union bound over
(3.4), followed by the subexponential (2^{O(d)}) residual-coordinate
factor, gives

\[
 \#\{X\subseteq[2m]:S(X)<r\}
                         \le2^{m+o(m)}.             \tag{3.5}
\]

Restricting to rank (m) can only decrease this count.  Since

\[
                         W=\binom{2m}m=2^{2m-o(m)},               \tag{3.6}
\]

equations (3.5)--(3.6) prove (0.3).

## 4. Compiler installation

Every selected owner block is a literal physical (Q_r).  Install the
proved cell-factor-blind compiler, with any desired bijection between its
abstract directions and the selected physical axes.  The same packet
factor then supplies simultaneous return-free traces through every
depth (q\le H=o(r)).  The owner leave remains (0.3), and every compiler
window uses (q) axes crossing macroblock halves.

There is no seam or concatenation loss because each packet is compiled as
a complete cyclic factor.

## 5. What remains

The construction removes two owner-side obstacles:

1. a growing packet rank does not require a random hypergraph matching;
2. the crossing-axis toll from the complete quartet Hall theorem is met
   maximally rather than by accumulating one-axis trades.

It does not yet prove target coverage.  A lower target (T) can use an
axis in a macroblock only when, at source local rank (k), one edge of
(M_k) has both endpoints absent from (T).  Since (k) itself depends
on how many additions are assigned to the block, the compatibility graph
is a rank-twisted, multiblock allocation problem.  The exact next tasks
are:

* sum the exact profile ratios below over overlapping allocation fibres at
  (q=A\sqrt m) without double-counting source owners;
* test Hall for every profile cut of the selected-axis graph, not only
  potential reachability; and
* choose one common compiler labeling whose aggregate lower/upper holes
  are (o(W)).

For a target block of rank (t) receiving (a) additions, put (k=t+a), and
let (z,s,v) be its empty/single/double status counts in (M_k).  The exact
local lower source/target ratio is

\[
                         2^a{\binom za\over\binom{s+a}a}.        \tag{5.1}
\]

For an upper target of rank (u), statuses are taken in (M_{u-a}) and the
corresponding ratio is

\[
                         2^a{\binom va\over\binom{s+a}a}.        \tag{5.2}
\]

These ratios must be summed over allocation vectors with overlaps
controlled.  A single allocation fibre is not a Hall neighbourhood.

The complete raw lower compatibility count is recorded in
`MATH_AUDIT_RANK_TWISTED_MACROBLOCK_PACKET_TILING_20260726.md`.  If a
target has restrictions (T_j), local sizes (t_j), and receives
(\ell_j) additions in block (j), then

\[
 \ell_j\le e_{t_j+\ell_j}(T_j),\qquad
 e_s(Y)=\#\{\text{edges of }M_s\text{ empty in }Y\},             \tag{5.3}
\]

and

\[
 C_q^-(T)=2^q\sum_{\sum_j\ell_j=q}
        \prod_j\binom{e_{t_j+\ell_j}(T_j)}{\ell_j}.              \tag{5.4}
\]

The upper formula replaces empty-edge counts by full-edge counts in
(M_{u_j-\ell_j}).  Equations (5.3)--(5.4) precede the selected-axis and
installed-compiler restrictions, but make the remaining Hall calculation
fully explicit.

The independent-rank-permutation attack
MATH_ATTACK_RANK_TWISTED_ALLOCATION_OVERLAP_HALL_GATE_20260726.md
proves that the union over one-hit allocations removes every admissible
positive-density Gaussian macro/half/carrier profile cut in the maximal
atlas.  It does not prove Hall for block-labelled subfamilies inside one
profile cell.  It also proves that the unspecified deterministic
\(r\)-axis selector cannot be left arbitrary: a legal localized selector
has an explicit \(\Omega(W)\) lower and upper Hall cut, independent of the
compiler.  Thus a dispersed selector and the grouped compiler dual are
additional required hypotheses.

The follow-up
MATH_THEOREM_TRANSVERSAL_AXIS_SELECTOR_AND_COMPILER_HALL_GATE_20260726.md
constructs such a dispersed selector at the direction level.  It replaces
the parallel split of every dimension-typical \(Q_S\)-cell by a product
of \(r\) direction-spread edge matchings.  This is an exact nonparallel
\(Q_r\)-partition and satisfies, for both signed compiler traces,
\[
 \nu_q(D\subseteq E)\le(1+o(1))
       \left({|E|\over S-o(S)}\right)^q.
\]
Hence the localized-\(E\) obstruction is removed.  The remaining theorem
is still the arbitrary block-labelled selected-axis/configuration Hall
dual; the transversal design proves it only for the Gaussian profile and
exterior-cylinder weight classes.

The macroblock-fullness invariant is negligible when (d>C\log m): the
expected number of full macroblocks in a central random set is

\[
                    O\!\left({m\over d}2^{-2d}\right)=o(1).     \tag{5.5}
\]

This observation removes the particular fixed-quartet Hall cut but is not
a proof that no different rank-twisted capacity cut survives.

## 6. Audited boundary

Proved:

* an exact rank-dependent mixed-frame partition of every macroblock;
* an owner-disjoint (Q_r)-packet near-factor with exponentially small
  leave;
* (s(P)=r) cross-half axes in every selected packet; and
* compatibility with the common all-depth local compiler.

Open:

* the rank-twisted Gaussian Hall theorem;
* simultaneous lower/upper quota balancing; and
* the final implication to `CPM`.

Thus the final obstruction has moved from owner packing and sparse frame
motion to one explicit target-capacity calculation for a deterministic
dense mixed-frame atlas.
