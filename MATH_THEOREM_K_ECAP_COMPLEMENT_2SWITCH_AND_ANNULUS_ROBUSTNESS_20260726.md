# The ECAP complement graph: exact reciprocal two-switches and annular robustness

Date: 2026-07-26

Method: pure mathematics only.  No computation, finite search, solver, or
web input is used.

## 0. Outcome

Put

\[
 W=\binom{2m}{m},\qquad B=C_m={W\over m+1},
\tag{0.1}
\]

\[
 q_0=\lceil a\sqrt m\rceil,\qquad
 H=\lfloor b\sqrt m\rfloor,
 \qquad 0<a<b<\infty,
\tag{0.2}
\]

and

\[
 N_q=\binom{2m}{m-q},\qquad
 K_0=\left\lfloor{N_{q_0}\over2m}\right\rfloor.
\tag{0.3}
\]

Thus

\[
 {N_{q_0}\over W}=e^{-a^2}+O_a(m^{-1/2}),\qquad
 {K_0\over B}={e^{-a^2}\over2}+o(1).
\tag{0.4}
\]

Consider the canonical anchored MSW factor and the extensive bank obtained
from (u=\lfloor\alpha m\rfloor), (0<\alpha<1/2), pairwise disjoint
reciprocal-(C_8) slots.  This note proves four structural facts about the
exact ECAP gate.

1. The canonical cut complement graph is not intrinsically bipartite.  In
   semilength three it is exactly a doubled edge disjoint from a triangle.
   In particular it is not the associahedron flip graph.
2. One reciprocal rectangle does not make eight arbitrary complement-graph
   edits.  It swaps two nonport primary tokens between two fixed-port rows,
   and hence performs one graph two-switch.  For every row set (S), its
   induced-edge count changes by at most one.
3. If (S) has the required size (K_0), the number of reciprocal slot
   incidences which can act on (S) is at most
   \[
   \boxed{
   Z_{K_0}=\left({\alpha e^{-a^2}\over16}+o(1)\right)W
          =\left({\alpha\over16}+o(1)\right)N_{q_0}.}
   \tag{0.5}
   \]
   Consequently all extensive masks together can improve the middle
   collision of a fixed (K_0)-row selection by at most
   \[
   \boxed{
      2Z_{K_0}
      =\left({\alpha\over8}+o(1)\right)N_{q_0}.}
   \tag{0.6}
   \]
   Since (alpha<1/2), this is strictly less than
   ((1/16+o(1))N_{q_0}).
4. At every protected depth, the lower occurrence histogram changes by
   half-(ell^1) action at most four times the same selected incidence
   count.  This gives one hereditary canonical robustness functional whose
   failure rigorously rules out ECAP simultaneously at the middle rank and
   all depths (q_0,\ldots,H).

The conclusion is a sharp obstruction test, not a proof of ECAP.  No
expansion or near-independent-set theorem for the canonical complement
graph is currently available, and no theorem shows that the permitted
two-switch signs align with the interval-hole signs at all depths.

## 1. The cut complement graph in token form

Let an anchored exact factor (F) have rows indexed by (D_m).  Rotate
the rooted coordinate order of row (x) to

\[
 r_x=(\infty,d_{x,1},\ldots,d_{x,m},
                 a_{x,1},\ldots,a_{x,m})
\tag{1.1}
\]

and cut out (infty).  Its (m+1) nonwrapping primary middle owners are

\[
 P_{x,j}=\{d_{x,j},\ldots,d_{x,m},
                 a_{x,1},\ldots,a_{x,j-1}\},
 \qquad 1\le j\le m+1.
\tag{1.2}
\]

They partition (\binom{[2m]}m).  The two port tokens are (P_{x,1})
and (P_{x,m+1}=P_{x,1}^c).  The remaining tokens

\[
 {cal N}_F=\{P_{x,j}:x\in D_m,\ 2\le j\le m\}
\tag{1.3}
\]

are closed under complementation.  Write (o_F(Q)) for the unique row
which owns the primary token (Q).  The cut complement multigraph is

\[
 V(G_F)=D_m,\qquad
 E(G_F)=\bigl\{\{o_F(Q),o_F(Q^c)\}:
                   \{Q,Q^c\}\subset{cal N}_F\bigr\}.
\tag{1.4}
\]

Each complementary pair is taken once.  The graph is loopless and
((m-1))-regular, with parallel edges retained.  For every (S\subseteq
D_m),

\[
 C_0(S,F)=2e_{G_F}(S).
\tag{1.5}
\]

The token form (1.4), rather than abstract regularity, is what makes the
reciprocal switch calculation exact.

## 2. The canonical graph is not bipartite

The first nontrivial case already rules out a universal bipartition
invariant.

### Proposition 2.1 (the exact canonical graph at (m=3))

For the canonical MSW factor at semilength three, (G_F) is the disjoint
union of a doubled (K_2) and a simple (K_3).

#### Proof

The five Dyck roots, their deletion and insertion lists, and their two
nonport primary tokens are as follows:

\[
\begin{array}{c|c|c|c}
x&(d_1,d_2,d_3)&(a_1,a_2,a_3)&(P_{x,2},P_{x,3})\\ \hline
111000&(2,3,1)&(6,4,5)&(136,146)\\
110100&(4,2,1)&(6,5,3)&(126,156)\\
110010&(2,1,5)&(4,3,6)&(145,345)\\
101100&(1,4,3)&(2,6,5)&(234,236)\\
101010&(1,3,5)&(2,4,6)&(235,245).
\end{array}
\tag{2.1}
\]

For example, these lists follow directly from the MSW recursion

\[
 \rho(1u0v)=
 (|u|+2,\ |u|+2-\rho(\mu u),\ 1,
                       |u|+2+\rho(v)),
\tag{2.2}
\]

by taking the even entries of (\rho) as the deletion list and the odd
entries as the insertion list.  The complementary pairs in (2.1) are

\[
 136\leftrightarrow245,\qquad
 146\leftrightarrow235,\qquad
 126\leftrightarrow345,
\tag{2.3}
\]

\[
 156\leftrightarrow234,\qquad
 145\leftrightarrow236.
\tag{2.4}
\]

Thus (111000) and (101010) are joined twice, while
(110100,110010,101100) form a triangle.  These are all five graph
edges, as required by (|E|=(m-1)C_m/2=5). \(\square\)

This is only a structural counterexample.  It is not an asymptotic
expansion theorem and does not by itself obstruct a density
(e^{-a^2}/2) shore.

## 3. A reciprocal rectangle is exactly one graph two-switch

### Lemma 3.1 (primary-token swap)

In one ambient reciprocal-(C_8) rectangle, identify the two old and new
rows by their fixed ports.  There are two nonport primary tokens (Q,R)
such that

* the old rows (x,y) own (Q,R), respectively;
* the new rows (x,y) own (R,Q), respectively; and
* every other primary token has the same row owner before and after the
  trade.

#### Proof

In the base rectangle the old and new traces are

\[
\begin{array}{c|ccc@{\qquad}ccc}
 &\multicolumn{3}{c}{\rm old}&\multicolumn{3}{c}{\rm new}\\
1100&12&14&34&12&23&34\\
1010&13&23&24&13&14&24.
\end{array}
\tag{3.1}
\]

Thus the two middle primary tokens are exchanged and all four ports are
fixed.  An aligned ambient context adjoins one fixed spectator state and
applies one injective coordinate relabelling to every displayed state.
It therefore preserves the statement literally.  Outside the aligned
three-state slab the two ambient paths are unchanged. \(\square\)

### Theorem 3.2 (exact induced-edge switch formula)

Let (F') be obtained from (F) by one reciprocal rectangle, with the
notation of Lemma 3.1.  Then for every (S\subseteq D_m),

\[
 \boxed{|e_{G_{F'}}(S)-e_{G_F}(S)|\le1.}
\tag{3.2}
\]

More precisely, if (R\ne Q^c), put

\[
 z=o_F(Q^c),\qquad w=o_F(R^c),
\tag{3.3}
\]

and (s_v={\bf1}_{\{v\in S\}}).  Then

\[
 \boxed{
 e_{G_{F'}}(S)-e_{G_F}(S)
       =(s_y-s_x)(s_z-s_w).}
\tag{3.4}
\]

If (R=Q^c), the complement-graph edge is unchanged and the difference
is zero.

#### Proof

Assume first that (R\ne Q^c).  The complement owners (z,w) are not
among the two token assignments changed in this rectangle.  The two old
edges are

\[
                         xz,\qquad yw,
\tag{3.5}
\]

and the two new edges are

\[
                         yz,\qquad xw.
\tag{3.6}
\]

All other labelled edges agree.  Their contributions to the induced-edge
count differ by

\[
 s_ys_z+s_xs_w-s_xs_z-s_ys_w
       =(s_y-s_x)(s_z-s_w),
\tag{3.7}
\]

which belongs to ({-1,0,1}).  If (R=Q^c), exchanging the owners of
the two ends of the same complementary pair preserves its unordered row
edge. \(\square\)

Thus a rectangle changes (e(S)) only if both its source row pair
({x,y}) and its complementary-owner pair ({z,w}) are split by
(S).  The first split condition alone gives the useful uniform bound
below.

### Corollary 3.3 (global-mask profile stability)

Let (A\subseteq[u]) be a global slot mask.  Define

\[
 I_A(S)=\sum_{x\in S}|A\cap J(x)|,
\tag{3.8}
\]

where (J(x)) is the set of reciprocal slots eligible in row (x).
Then

\[
 \boxed{
 |e_{G_{F^A}}(S)-e_{G_{F^0}}(S)|\le I_A(S).}
\tag{3.9}
\]

For (0\le K\le B), put

\[
 Z_K=\max_{\substack{S\subseteq D_m\\|S|=K}}
                         \sum_{x\in S}|J(x)|.
\tag{3.10}
\]

Then

\[
 \boxed{
 \left|min_{|S|=K}e_{G_{F^A}}(S)
       -\min_{|S|=K}e_{G_{F^0}}(S)\right|\le Z_K.}
\tag{3.11}
\]

#### Proof

Install the rectangles sequentially.  The aligned disjoint-slot theorem
ensures that every step is again the token swap of Lemma 3.1.  By Theorem
3.2, only a rectangle whose two source rows are split by (S) can change
the induced-edge count.  Such a rectangle contains exactly one selected
eligible row and therefore contributes one to (I_A(S)).  Telescoping
proves (3.9).  The bound is uniform in (S), so applying it to minimizers
on the two sides proves (3.11). \(\square\)

The estimate (uC_{m-2}) counts every installed rectangle.  Formula
(3.9) is stronger at the ECAP density because it counts only selected-row
incidences.

## 4. Exact selected-row supply at the annular density

For (x\in D_m), write

\[
                         z_x=|J(x)|.
\tag{4.1}
\]

The marked-slot Catalan census gives

\[
 {1\over B}\sum_xz_x
 =u{2C_{m-2}\over C_m}
 ={\alpha m\over8}+O_\alpha(1),
\tag{4.2}
\]

and the two-slot census gives

\[
 {1\over B}\sum_x(z_x-\bar z)^2=O_\alpha(m).
\tag{4.3}
\]

### Theorem 4.1 (effective trade supply)

At (K=K_0), equation (0.5) holds.

#### Proof

For every (K)-set (S), Cauchy--Schwarz and (4.3) give

\[
 \sum_{x\in S}z_x
 \le K\bar z+
   \sqrt{K\sum_{x\in D_m}(z_x-\bar z)^2}.
\tag{4.4}
\]

By (0.4) and (4.2), the first term at (K=K_0) is

\[
 \left({e^{-a^2}\over2}+o(1)\right)B
 \left({\alpha m\over8}+O_\alpha(1)\right)
 =\left({\alpha e^{-a^2}\over16}+o(1)\right)W.
\tag{4.5}
\]

The square-root term is \(O_{a,\alpha}(B\sqrt m)=o(W)\).  This proves the
upper bound in the first equality of (0.5).  A uniformly random
\(K_0\)-subset has expected incidence \(K_0\bar z\), so the maximum is at
least the main term in (4.5).  This gives the matching lower bound and
hence the first equality in (0.5); (0.4) gives the second. \(\square\)

There are two different supply normalizations:

\[
 uC_{m-2}
   =\left({\alpha\over16}+o(1)\right)W
   =\left({\alpha e^{a^2}\over16}+o(1)\right)N_{q_0}
\tag{4.6}
\]

is the raw number of rectangles in the complete factor bank, while

\[
 Z_{K_0}
   =\left({\alpha\over16}+o(1)\right)N_{q_0}
\tag{4.7}
\]

is the maximum number of slot incidences visible to a selected
(K_0)-row family.  It is (4.7), not (4.6), which controls selection
repair.  Equations (3.9) and (4.7) prove (0.6).

## 5. The same incidence budget controls every annular depth

For a row set (S) and global mask (A), let

\[
 \mu_q^{A,S}(T)=
   |\{(x,j):x\in S,
       \text{the start }j\text{ of }\pi_x^A
       \text{ has lower depth-}q\text{ target }T\}|
\tag{5.1}
\]

and

\[
 h_q(S,A)=N_q-|\operatorname{supp}\mu_q^{A,S}|.
\tag{5.2}
\]

For equal-mass histograms put

\[
 {\mathsf A}(\mu,\nu)={1\over2}\|\mu-\nu\|_1.
\tag{5.3}
\]

### Lemma 5.1 (selected all-depth action)

For every (1\le q<m),

\[
 \boxed{
 {\mathsf A}(\mu_q^{A,S},\mu_q^{0,S})
       \le4I_A(S),}
\tag{5.4}
\]

and consequently

\[
 \boxed{
 |h_q(S,A)-h_q(S,0)|\le4I_A(S).}
\tag{5.5}
\]

The identical statements hold for the complementary upper histograms.

#### Proof

On one eligible selected row, one reciprocal slot makes exactly one
adjacent transposition in the deletion half and one in the insertion half
of the ordinary cut order.  At any proper interval length, one adjacent
transposition changes at most two indexed window occurrences.  Thus its
half-(ell^1) action is at most two, and the two transpositions have
combined action at most four.  Sum over the selected active incidences to
obtain (5.4).

Moving one occurrence unit can change the number of zero histogram cells
by at most one.  The hole-count functional is therefore one-Lipschitz in
({\mathsf A}), proving (5.5).  Complementation is a bijection between
the lower and upper targets at antipodal starts, proving the last
statement. \(\square\)

The depth profiles are not independent: their oriented rank-(q_0)
traces determine all deeper sliding intersections.  Lemma 5.1 does not
discard that dependence; it merely gives a simultaneous necessary
capacity bound for the same mask and the same selected rows.

### Theorem 5.2 (hereditary ECAP robustness functional)

Put (Z=Z_{K_0}), and define the canonical functional

\[
 {\cal R}_{a,b,\alpha}(m)
 =\min_{\substack{S\subseteq D_m\\|S|=K_0}}
 \left\{
   (e_{G_{F^0}}(S)-Z)_+
   +\sum_{q=q_0}^{H}(h_q(S,0)-4Z)_+
 \right\}.
\tag{5.6}
\]

For every global mask (A) and every (K_0)-row set (S),

\[
\begin{aligned}
 e_{G_{F^A}}(S)+\sum_{q=q_0}^{H}h_q(S,A)
 \;&\ge
 (e_{G_{F^0}}(S)-I_A(S))_+\\
 &\quad+
 \sum_{q=q_0}^{H}(h_q(S,0)-4I_A(S))_+\\
 &\ge {\cal R}_{a,b,\alpha}(m).
\end{aligned}
\tag{5.7}
\]

Consequently

\[
 \boxed{
 \mathrm{ECAP}_{a,b}(\alpha)
       \quad\Longrightarrow\quad
 {\cal R}_{a,b,\alpha}(m)=o(W).}
\tag{5.8}
\]

#### Proof

Equations (3.9) and (5.5), together with nonnegativity of induced-edge and
hole counts, give the first inequality in (5.7).  Since
(I_A(S)\le Z), replacing (I_A(S)) by (Z) can only decrease every
positive part.  Minimizing over (S) gives the second inequality.  Under
ECAP the left side of (5.7) is (o(W)), proving (5.8). \(\square\)

This is a genuinely coupled obstruction: the minimum in (5.6) uses one
row set for the complement graph and every interval depth.  Separate
depthwise minimizers would give a weaker test and would not be a legal
packet selection.

### Corollary 5.3 (explicit necessary canonical margins)

If ECAP holds, its selected row sets (S_m) must satisfy

\[
 e_{G_{F^0}}(S_m)
 \le\left({\alpha\over16}+o(1)\right)N_{q_0}+o(W),
\tag{5.9}
\]

\[
 h_q(S_m,0)
 \le\left({\alpha\over4}+o(1)\right)N_{q_0}+o(W)
 \qquad(q_0\le q\le H),
\tag{5.10}
\]

and, more strongly,

\[
 \sum_{q=q_0}^{H}
 \left(h_q(S_m,0)-4Z_{K_0}\right)_+
 =o(W).
\tag{5.11}
\]

Thus the canonical middle collision may exceed the final (o(W)) target
by at most

\[
 \left({\alpha\over8}+o(1)\right)N_{q_0},
\tag{5.12}
\]

and the canonical hole count at any one protected depth may exceed its
final value by at most

\[
 \left({\alpha\over4}+o(1)\right)N_{q_0}.
\tag{5.13}
\]

#### Proof

Apply (3.9) and (5.5) to an ECAP witness and then use (0.5).  Summing the
positive-part lower bounds in (5.7) gives the exact-threshold statement
(5.11).  The exact \(Z_{K_0}\) is retained there because an unspecified
per-depth \(o(W)\) asymptotic error cannot be summed over a growing number
of depths. \(\square\)

For (alpha<1/2), the respective strict ceilings in (5.12)--(5.13) are
((1/16+o(1))N_{q_0}) and ((1/8+o(1))N_{q_0}).

## 6. Exact implication boundary

The following conclusions are proved.

1. The canonical cut complement graph is a genuine multigraph and need
   not be bipartite; the exact (m=3) graph contains a triangle.
2. A reciprocal rectangle is one token two-switch.  Its induced-edge
   effect is the bilinear split product (3.4), and has absolute value at
   most one.
3. At the corrected ECAP density, the effective selected-row switch supply
   is only ((\alpha/16+o(1))N_{q_0}), although the complete factor bank
   contains ((\alpha e^{a^2}/16+o(1))N_{q_0}) rectangles.
4. The same incidence budget gives at most four occurrence moves per
   protected depth and yields the coupled canonical obstruction
   (5.6)--(5.8).

The following statements are not proved.

1. There is no proved asymptotic lower or upper formula for
   \[
   \min_{|S|=K_0}e_{G_{F^0}}(S).
   \]
   Regularity alone is insufficient: a regular bipartite graph permits a
   zero-edge shore of every density below one half, while regular graphs
   with dense small components need not.
2. Satisfying the canonical margins (5.9)--(5.11) is not sufficient.
   The graph two-switch signs, the rank-(q_0) interval signs, and all
   deeper sliding-intersection signs must be realized by the same global
   slot mask.
3. The theorem concerns ECAP row sets, hence at most one selected row over
   each anchored root.  A broader packet catalogue allowing repeated use
   of one root with different local masks is not controlled by the
   (K_0)-set incidence estimate (4.4), and it no longer has the common
   complement graph (1.5).

Accordingly the extensive reciprocal bank remains a viable but unproved
constant-density annulus design.  The exact surviving positive task is now
sharper: find one (K_0)-row set whose canonical robust margins fit inside
the budgets (0.5), then prove that one global mask realizes productive
two-switch and interval signs simultaneously.  Failure of (5.8) is a
rigorous statewise obstruction closing the entire common-factor ECAP lane.
