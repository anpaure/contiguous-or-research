# The eight-owner cross-sector \(Q_2\) associator: exact audit, heat matrix, and tensor capacity

Date: 2026-07-26

Method: pure mathematics only.

## 0. Verdict

The proposed eight-owner packet is valid.  It is smaller and cleaner than
the rank-four \(Q_3\) packet if local \(Q_2\)-cells are permitted.

Let

\[
 P=\{a,b,c,d\},\qquad R=\{u,v\},\qquad
 \Omega=\{\{p,r\}:p\in P, r\in R\}.                 \tag{0.1}
\]

Thus \(|\Omega|=8\).  Every perfect matching \(M\) of \(K_P\) gives an
exact partition

\[
 \mathcal R_M=\{E\star R:E\in M\}                    \tag{0.2}
\]

into two literal \(Q_2\)-cells.  Here

\[
                    E\star R=\{\{e,r\}:e\in E,r\in R\}.
\]

Both cells carry each of the labelled lower targets \(\{u\}\) and
\(\{v\}\).  Hence either target has two simultaneous vertex-disjoint
carriers in one exact owner partition.

For two different matchings, the ownership overlap is a connected
two-versus-two associator with self Gram \(4I_2\) and cross Gram
\(2J_2\).  After removing the common reservoir factor two, this is
exactly

\[
                              2I_2\longleftrightarrow J_2.          \tag{0.3}
\]

Its normalized heat operator is \(J_2/2\): it preserves constants and
kills the antisymmetric cell mode exactly.

Tensoring \(r\) packets gives \(2^r\) cells \(Q_{2r}\).  A target
touching \(q\) blocks has exactly \(2^q\) carrier cells.  With one cyclic
direction order per cell, the same exact capacity law as for the larger
\(Q_3\) packet holds:

\[
 1-(1-p_{r,q})^{2^q}\le \rho_{r,q}
 \le \min\{1,2^qp_{r,q}\},
 \qquad p_{r,q}={r-q+1\over\binom rq}.                \tag{0.4}
\]

Thus the packet gives a real factor \(2^q\) gain but still leaves an
exponential consecutive-window obstruction, for example

\[
 \rho_{2q,q}\le
 {2^q(q+1)\over\binom{2q}q}
 =\Theta(q^{3/2}2^{-q}).                              \tag{0.5}
\]

The packet is minimal among two-carrier packets made of literal
\(Q_2\)-cells: two cells are necessary and each has four owners.  It is
not minimal if \(Q_1\)-cells are allowed; two disjoint edges already give
a four-owner packet.  Under the original rank-four/\(Q_3\) restriction,
the sixteen-owner packet in
`MATH_THEOREM_CROSS_SECTOR_TWO_CARRIER_PACKET_20260726.md` is minimal.

Already for one block, the two \(Q_2\)-cells themselves are two
isometric \(C_4\)'s.  Hence the eight-owner construction is also a literal
exact cycle packet, not merely a face packet.  After tensoring and, when
necessary, adjoining spectator axes to reach power-of-two dimension, all
\(2^q\) carrier paths of any one prescribed target can simultaneously be
completed to isometric long cycles in an exact owner factor.

## 1. The three exact resolutions

The three perfect matchings of \(K_4\) are

\[
\begin{aligned}
 M_0&=\{ab,cd\},\\
 M_1&=\{ac,bd\},\\
 M_2&=\{ad,bc\}.
\end{aligned}                                                        \tag{1.1}
\]

For every edge \(E=\{x,y\}\), the four owners

\[
                         xu,xv,yu,yv                              \tag{1.2}
\]

form a literal \(Q_2\) with active directions \(E\) and \(R\).  The
two edges of a perfect matching partition \(P\), so their two cells are
disjoint and cover all eight owners in \(\Omega\).  This proves (0.2).

Fix \(r\in R\).  In the cell \(E\star R\), the edge obtained by fixing
the reservoir orientation to \(r\) is

\[
                          \{\{x,r\},\{y,r\}\},                    \tag{1.3}
\]

whose lower intersection is the labelled singleton \(\{r\}\).  Each
resolution has two cells, hence two disjoint carrier edges for \(\{r\}\).
Their physical directions are the two edges of its matching.  Across the
three resolutions, the carrier directions are all six edges of \(K_4\),
each exactly once.

## 2. Genuine cross-sector transport

Place \(a,b\) in one coordinate macroblock and \(c,d\) in a second one;
keep \(u,v\) in a reservoir class.  Then the two cells of \(M_0\) are
profile-pure: the \(ab\)-cell always chooses its nonreservoir coordinate
from the first macroblock, and the \(cd\)-cell always chooses it from the
second.

Every cell of \(M_1\) or \(M_2\), by contrast, has one endpoint from each
nonreservoir macroblock in its first active pair.  Its carrier edge for
\(\{u\}\), and likewise for \(\{v\}\), joins the two source profiles.
Thus the changed shore is genuinely cross-sector at the carrier itself.

For a fixed target \(\{u\}\), its four middle extensions in this packet
are

\[
                         au,bu,cu,du.                              \tag{2.1}
\]

Every matching resolution uses all four of them, paired into two carrier
edges.  Therefore this even extension star has no analogue of the
one-in-five leave in the rank-four \(Q_3\) packet.  The parallel matching
realizes two within-sector pairs, while either crossed matching realizes
two between-sector pairs.  Averaging the three resolutions is exactly
uniform on all six possible extension pairs and exactly uniform on the
four extension owners.

## 3. Exact overlap and the heat operator

Take two different perfect matchings \(M,N\).  An edge of \(M\) meets an
edge of \(N\) in exactly one vertex of \(P\).  Therefore every left cell
meets every right cell in

\[
                        \{p\}\star R,                              \tag{3.1}
\]

a two-owner \(Q_1\).  The ownership-overlap graph is consequently
\(K_{2,2}=C_4\), and is connected.

Let rows and columns index the two cells on the two shores.  The cell
indicator Gram matrices are

\[
                     G_{MM}=4I_2,
                     \qquad G_{MN}=2J_2.                           \tag{3.2}
\]

The factor two is the common reservoir size.  Dividing by it gives
\(2I_2\) and \(J_2\), proving (0.3).  Conditional averaging from a
left-cell function \((f_0,f_1)\) to the right shore is

\[
             (f_0,f_1)\longmapsto
             \left({f_0+f_1\over2},{f_0+f_1\over2}\right),         \tag{3.3}
\]

so the normalized matrix is \(H=J_2/2\).  Its eigenvalues are

\[
                  H(1,1)=(1,1),qquad H(1,-1)=0.                  \tag{3.4}
\]

This is exact annihilation, not merely a spectral gap.

For \(r\) blocks, the shore cells are indexed by \(\{0,1\}^r\), and

\[
 G_{MM}^{(r)}=4^rI_{2^r},qquad
 G_{MN}^{(r)}=2^rJ_{2^r},qquad
 H^{(r)}={1\over2^r}J_{2^r}.                        \tag{3.5}
\]

Hence every pair of opposite-shore product cells meets, always in
exactly \(2^r\) owners; the overlap graph is the single connected
\(K_{2^r,2^r}\).  The normalized heat operator kills every nonconstant
Walsh mode in one step.

The qualification is structural: because the overlap has one component,
an ownership-component switch chooses the whole shore at once.  The rank
one heat matrix does not supply \(2^r\) independently switchable pieces.

## 4. Tensor carrier and order counts

Fix one of the three resolutions in every block.  Its tensor product is
an exact partition

\[
                         \Omega^r
  =\mathop{\dot\bigcup}_{2^r\ {m cells}}Q_{2r}.                   \tag{4.1}
\]

For \(I\in\binom{[r]}q\), prescribe the local target \(\{u_i\}\) in
blocks \(i\in I\) and an arbitrary owner of \(\Omega_j\) in every
untouched block.  The resulting target family has cardinality

\[
                         \binom rq8^{r-q}.                          \tag{4.2}
\]

An untouched owner fixes its unique local cell.  In a touched block,
both cells carry \(\{u_i\}\).  Thus every target has exactly \(2^q\)
carrier product cells and \(2^q\) distinct physical \(q\)-matchings.

In each product cell there is one carrier axis per block and one
reservoir axis per block.  A cyclic order exposes at most \(r-q+1\)
all-carrier length-\(q\) intervals.  For each such touched set, the cell
carries \(4^{r-q}\) targets, one for every untouched cell vertex.  Hence
the number reached is at most

\[
                          2^r(r-q+1)4^{r-q}.                         \tag{4.3}
\]

Dividing (4.3) by (4.2) gives the upper half of (0.4).

For the lower half, independently put the \(r\) carrier axes of each
cell in one uniformly random run.  A fixed \(q\)-set is an interval with
probability \(p_{r,q}=(r-q+1)/\binom rq\).  A target has \(2^q\)
independently ordered carrier cells, so it is reached with probability
\(1-(1-p_{r,q})^{2^q}\).  Averaging proves that some deterministic order
assignment reaches at least this fraction.

## 5. Minimality boundary

Two simultaneous carriers require at least two disjoint cells.  A literal
\(Q_2\) has four owners.  Therefore every two-carrier \(Q_2\) packet has
at least eight owners, and (0.1)--(0.2) attains this bound.

For a nonempty singleton target, one carrier direction consumes two
coordinates outside the target, and two disjoint carrier directions
consume four.  Five total coordinates still do not suffice.  Indeed, let
the target be \(\{u\}\), let the two carrier pairs be disjoint pairs
\(P,Q\), and suppose \(\{u\}\cup P\cup Q\) is the whole ground set.  A
rank-two \(Q_2\)-cell has no fixed core.  The second active pair in the
\(P\)-carrier cell must therefore be \(\{u,q\}\) for some \(q\in Q\),
and the second active pair in the \(Q\)-carrier cell must be
\(\{u,p\}\) for some \(p\in P\).  The middle owner \(\{p,q\}\) then
lies in both cells.  Thus the cells cannot be disjoint.

The six-coordinate construction (0.1) is therefore ground-set minimal as
well: its second active pair is the common reservoir pair \(R=\{u,v\}\),
and disjointness follows from the disjoint carrier pairs.

If no reservoir direction is required, take any target core \(T\) and
four outside coordinates \(a,b,c,d\).  The two \(Q_1\)-edges with
directions \(ab\) and \(cd\) form a four-owner two-carrier packet, and
the other perfect matchings of \(K_4\) give trades on the same support.
Thus “eight owners is smallest” is correct only with the explicit
\(Q_2\)-cell requirement.  Likewise, the sixteen-owner theorem for the
original local architecture is minimal only with the rank-four
\(Q_3\)-cell requirement.

## 6. Exact cycle completion

For one block, each cell \(E\star R\) is itself the isometric cycle

\[
                  eu,fu,fv,ev,eu\qquad(E=\{e,f\}),                 \tag{6.1}
\]

with doubled transition word \(E,R,E,R\).  The two cells of one matching
therefore give an exact two-\(C_4\) owner factor of \(\Omega\), and both
cycles contain the carrier edge for \(\{u\}\) (and also for \(\{v\}\)).

For the tensor packet, append \(d\) spectator axes so that

\[
                             h=2r+d                                \tag{6.2}
\]

is a power of two.  Its owner support is partitioned into \(2^r\)
disjoint \(Q_h\)-cells.  Fix one target touching \(q\) blocks.  In every
one of its \(2^q\) carrier cells, its forced directions form a geodesic
path.  Order those directions first, extend them to a permutation of all
\(h\) axes, and double the permutation.  This gives an isometric
\(C_{2h}\) containing the prescribed path.

Every isometric \(C_{2h}\) in a power-of-two cube belongs to a vertex
resolution class: translate and permute coordinates in the standard
resolvable cube construction so that its base cycle is the prescribed
one.  Choose that class independently in each carrier cell and an
arbitrary class in every other cell.  Since the cells are disjoint, the
union is an exact owner factor in which all \(2^q\) carriers of the fixed
target occur on distinct long cycles.

This choice is target-adaptive.  Simultaneously serving the whole target
family with one class/order per cell is constrained by (0.4); the cycle
completion does not erase that global order count.
