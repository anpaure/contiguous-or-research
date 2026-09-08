# Rank-twisted cross-parent \(Q_{R+1}\) slab trades

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, solver, or web
input is used.

## 0. Result

The \(Q_{R+1}\) two-resolution trade can recouple **different**
rank-twisted parent product cells.  It is not confined to two parallel
fibres of one parent \(Q_S\).

There is a particularly clean rank-preserving construction.  In one
macroblock, choose a cross-half pair \(e=\{u,v\}\) which is not an edge of
the rank-\(k\) matching \(M_k\).  The two \(e\)-facets of a physical
\(Q_{R+1}\) then have the same local rank and the same rank-dependent
frame, but their status labels lie in two different cells.  Replacing the
\(e\)-resolution by the resolution along one common active direction is
an exact two-packet-versus-two-packet owner trade.  Its new packets cross
the old parent-cell boundary, remain literal coordinate-disjoint
\(Q_R\)'s, and therefore accept the diverse-order compiler without
modification.

There is also a minimality invariant:

> At a fixed local rank and fixed matching frame, one Johnson swap either
> changes only the orientation inside one single-status edge and leaves
> the parent status label unchanged, or changes exactly two status
> coordinates.  It can never change exactly one status coordinate.

Thus the parent label is not an invariant of slab trades, but
rank-preserving cross-parent recoupling has status Hamming distance at
least two.  The construction below attains two.

For one traded slab, write \(s=2^R\) and
\(g_R=2^R/R\).  At signed depth \(q\le H<R\), the exact target derivative
is a balanced vector

\[
 \Delta_q^\pm
   =\mathbf1_{\mathcal I_{\rm new,q}^\pm}
      -\mathbf1_{\mathcal I_{\rm old,q}^\pm},
 \qquad
 \sum_T\Delta_q^\pm(T)=0,
\]

with

\[
 \|\Delta_q^\pm\|_1\le4s,\qquad
 \sum_T(\Delta_q^\pm(T))_+
   =\sum_T(-\Delta_q^\pm(T))_+\le2s.               \tag{0.1}
\]

Its exact depth-\(q\) direction-support marginal is

\[
 2qg_R(e_e-e_i),                                   \tag{0.2}
\]

where \(e\) is activated and the old active direction \(i\) is frozen.
At \(q=1\), (0.2) is the previously audited literal direction step
\(2g_R(e_e-e_i)\).

Equation (0.1) is the universal literal bound.  It is not \(o(s)\), and
the construction alone gives no all-depth cancellation theorem.
Therefore the local trade positively breaks the parent-cell barrier, but
an abundance/routing theorem aligning these derivatives is still needed.

## 1. Parent-cell labels

Fix a macroblock

\[
                         B=A\mathbin{\dot\cup}C,
 \qquad |A|=|C|=d.
\]

At local rank \(k\), let \(M_k\) be the prescribed perfect matching from
\(A\) to \(C\).  For \(X\in\binom Bk\), define its status vector

\[
 \rho_k(X)=\bigl(|X\cap f|\bigr)_{f\in M_k}
             \in\{0,1,2\}^{M_k}.                  \tag{1.1}
\]

Equivalently, put

\[
 \begin{aligned}
 Z_k(X)&=\{f\in M_k:|X\cap f|=0\},\\
 S_k(X)&=\{f\in M_k:|X\cap f|=1\},\\
 V_k(X)&=\{f\in M_k:|X\cap f|=2\}.
 \end{aligned}                                     \tag{1.2}
\]

The local parent cell labelled by

\[
                         (k;Z,S,V)                 \tag{1.3}
\]

consists of all choices of one endpoint on every edge in \(S\), with
the edges in \(Z\) empty and those in \(V\) full.  It is a physical
\(Q_{|S|}\).

A global rank-twisted parent product cell has label

\[
 \Lambda=
 \bigl((k_j;Z_j,S_j,V_j)\bigr)_{j=1}^{b}
 \quad\text{together with the residual-coordinate pins}.       \tag{1.4}
\]

Inside it, a \(Q_R\)-fibre additionally specifies:

1. a selected \(R\)-subset \(D\subseteq\bigsqcup_jS_j\) of active
   matching edges; and
2. one frozen endpoint on every edge of
   \((\bigsqcup_jS_j)\setminus D\).

This separates the **parent status label** from the **spectator
orientation label**.  Sibling fibres share (1.4) and differ only in the
second item.  The trade below changes (1.4).

## 2. Minimal parent-label change

### Lemma 2.1 (two-coordinate status law)

Fix \(k\) and \(M_k\).  Let

\[
                         Y=X-\{u\}+\{v\}
\]

be Johnson neighbours in \(\binom Bk\).

1. If \(u,v\) lie on the same matching edge, then
   \(\rho_k(Y)=\rho_k(X)\).  Only its orientation bit changes.
2. If \(u\) and \(v\) lie on distinct matching edges \(f,g\), then all
   status coordinates except \(f,g\) agree, and

   \[
      \rho_k(Y)_f=\rho_k(X)_f-1,\qquad
      \rho_k(Y)_g=\rho_k(X)_g+1.                  \tag{2.1}
   \]

In particular, a rank-preserving Johnson move cannot change exactly one
parent status coordinate.

#### Proof

Only the matching edges containing the removed and added coordinates can
change.  If these are the same edge, its cardinality stays one.  If they
are distinct, one cardinality falls by one and the other rises by one.
Equation (2.1) follows.  The coordinate sum

\[
                         \sum_{f\in M_k}\rho_k(X)_f=k
\]

also gives the one-coordinate impossibility directly. \(\square\)

The rank dependence of the atlas does not strengthen this to a
parent-label invariant.  A move within one macroblock preserves \(k\), so
both shores use the same \(M_k\), and the second branch of Lemma 2.1 is
available.

## 3. Explicit cross-parent slab

Choose two distinct matching edges

\[
                         f=\{u,u^\ast\},\qquad
                         g=\{v,v^\ast\}
                         \quad\text{in }M_k,         \tag{3.1}
\]

where \(u\in A\), \(v\in C\), and \(g\ne f\).  Then

\[
                         e=\{u,v\}                  \tag{3.2}
\]

is a cross-half pair but is not an edge of \(M_k\).

Choose \(R\) further mutually disjoint physical matching edges

\[
                         D=\{d_1,\ldots,d_R\}        \tag{3.3}
\]

from the global rank-twisted frames, avoiding
\(f\cup g\).  They may lie in this and other macroblocks.  Freeze all
remaining ground coordinates so that:

* \(u^\ast\) and \(v^\ast\) are absent;
* the two choices \(u\in X,v\notin X\) and
  \(u\notin X,v\in X\) have the same local rank \(k\); and
* the total owner rank is the global middle rank.

In the literal notation for orientation cubes, this gives one slab

\[
                         \mathcal S
   =\mathcal Q(F,E;D\cup\{e\})\cong Q_{R+1}.         \tag{3.4}
\]

Its \(e\)-resolution is

\[
 \begin{aligned}
 P_u&=\mathcal Q(F\cup\{u\},E\cup\{v\};D),\\
 P_v&=\mathcal Q(F\cup\{v\},E\cup\{u\};D).
 \end{aligned}                                     \tag{3.5}
\]

For every owner of \(P_u\), the two special frame statuses are

\[
                         (\rho(f),\rho(g))=(1,0),
\]

while for every owner of \(P_v\) they are

\[
                         (\rho(f),\rho(g))=(0,1).   \tag{3.6}
\]

All other parent status coordinates agree.  Hence \(P_u\) and \(P_v\)
are \(Q_R\)-fibres of two different rank-twisted parent product cells.
They are not sibling fibres of one \(Q_S\).

The construction is nonvacuous in the cyclic atlas

\[
 M_k=\{a_i c_{i+k}:i\in\mathbb Z_d\},
\]

because every current matching has \(d(d-1)\) other cross-half pairs
\(\{a_i,c_j\}\) available for (3.2).

### Theorem 3.1 (exact cross-parent slab trade)

For any \(i\in D\), replace the \(e\)-resolution (3.5) by the
\(i\)-resolution

\[
 \mathcal R_i=
 \bigl\{\{x_i=0\}\cong
          Q_{(D\setminus\{i\})\cup\{e\}},
        \{x_i=1\}\cong
          Q_{(D\setminus\{i\})\cup\{e\}}\bigr\}.     \tag{3.7}
\]

Then:

1. the two old and the two new packets have exactly the same owner union,
   namely \(\mathcal S\);
2. the new packets cross the boundary between the two parent labels in
   (3.6);
3. every new packet is a literal coordinate-disjoint \(Q_R\);
4. every active axis remains a cross-half macroblock pair; and
5. the diverse-order \(Q_R\)-compiler can be installed independently and
   exactly in both new packets.

#### Proof

Both (3.5) and (3.7) are opposite-facet resolutions of the same
\(Q_{R+1}\), proving exact owner preservation.  In (3.7), the coordinate
\(e\) is active, so each new packet contains owners from both status
labels (3.6).  The axes in \(D\setminus\{i\}\) are mutually disjoint and
avoid \(u,v\), so adjoining \(e\) leaves a matching of \(R\) physical
swap pairs.  Every edge in \(D\) joins the two halves of its macroblock by
construction, and so does \(e\).  Finally, the compiler theorem requires
only \(R\) coordinate-disjoint physical swap pairs.  It is blind to
whether those pairs came from one rank-twisted parent cell. \(\square\)

### Atlas compatibility

For this move to occur inside a previously fixed packet tiling, the
selector must choose the same common active set \(D\) in the two parent
cells and freeze \(f\) respectively \(g\) as in (3.6).  The theorem is a
local exact trade once such a pair is present.  It does not prove that a
positive density of the deterministic atlas fibres can be paired this
way.  That is an abundance/matching problem over parent labels.

## 4. Compiler preservation

Each shore of the trade consists of two complete physical \(Q_R\)'s.
Installing the certified diverse-order compiler gives an exact factor
into \(C_{2R}\)'s on either shore.  For every sign and
\(1\le q\le H<R/4\), each constituent packet has a literal injective
trace image of size

\[
                              s=2^R.                \tag{4.1}
\]

The two packets in one resolution also have disjoint images.  On the old
shore they have opposite frozen endpoints on \(e\), which is inactive in
both packets and hence remains visible in every lower and upper target.
On the new shore the same statement holds for the frozen direction
\(i\).  Therefore the aggregate image of either resolution is a set,
not a multiset, of size

\[
                              2s=2^{R+1}.            \tag{4.2}
\]

No owner leave, within-packet repeat, sibling-packet repeat, or compiler
completion error is created by the trade.

As elsewhere, use one canonical compiler orientation on all components;
arbitrary componentwise mixtures of forward and reverse orientations are
not needed.

## 5. Exact literal target derivative

For a signed depth \(c=(\pm,q)\), let

\[
 \Gamma_{e,c}
   =\mathbf1_{\mathcal I_{e,c}},\qquad
 \Gamma_{i,c}
   =\mathbf1_{\mathcal I_{i,c}}                  \tag{5.1}
\]

be the aggregate image indicators of the old and new resolutions.  By
(4.2),

\[
                         \sum_T\Gamma_{e,c}(T)
  =\sum_T\Gamma_{i,c}(T)=2s.                       \tag{5.2}
\]

Define

\[
                         \Delta_c=\Gamma_{i,c}-\Gamma_{e,c}.
                                                               \tag{5.3}
\]

Then, exactly,

\[
 \Delta_c(T)\in\{-1,0,1\},\qquad
 \sum_T\Delta_c(T)=0,                              \tag{5.4}
\]

and

\[
 \begin{aligned}
 \|\Delta_c\|_1
   &=|\mathcal I_{i,c}\triangle\mathcal I_{e,c}|
     \le4s,\\
 \sum_T(\Delta_c(T))_+
   &=|\mathcal I_{i,c}\setminus\mathcal I_{e,c}|
     =|\mathcal I_{e,c}\setminus\mathcal I_{i,c}|
     \le2s.
 \end{aligned}                                     \tag{5.5}
\]

These bounds hold for arbitrary certified compiler conjugates on the four
packets.

If \(B_c(T)\) is the literal load contributed by all packets outside the
slab, the exact hole derivative is

\[
 {\cal H}_c(B+\Gamma_i)-{\cal H}_c(B+\Gamma_e)
   =\sum_{T:B_c(T)=0}
        \bigl(\Gamma_{e,c}(T)-\Gamma_{i,c}(T)\bigr), \tag{5.6}
\]

so its absolute value is at most \(2s\).  Likewise the repeat derivative
is

\[
 {\cal E}_c(B+\Gamma_i)-{\cal E}_c(B+\Gamma_e)
   =\sum_{T:B_c(T)\ge1}
        \bigl(\Gamma_{i,c}(T)-\Gamma_{e,c}(T)\bigr), \tag{5.7}
\]

again of absolute value at most \(2s\).  Equations (5.6)--(5.7) add to
the fixed hole/repeat ledger because both resolutions have the same
occurrence mass.

For factorial collision energy one gets the exact weighted derivative

\[
 {\cal C}_c(B+\Gamma_i)-{\cal C}_c(B+\Gamma_e)
   =\sum_TB_c(T)\Delta_c(T).                        \tag{5.8}
\]

There is no useful load-independent improvement of (5.8) without a
bound or cancellation theorem for the background loads.

## 6. Exact direction-support derivative

Every isometric \(C_{2R}\) compiler component has a direction word
\(\pi\pi\).  For \(q<R\), each occurrence of a fixed direction belongs to
exactly \(q\) directed \(q\)-windows, and the two occurrences in one
component give disjoint sets of starts.  Since a packet has
\(s/(2R)\) components, the number of its \(q\)-windows whose support
contains one fixed active direction is

\[
             2q\,{s\over2R}={qs\over R}=qg_R.       \tag{6.1}
\]

Each resolution has two packets.  The old active set is \(D\), and the
new active set is

\[
                         (D\setminus\{i\})\cup\{e\}.
\]

Therefore the exact change in the direction-support incidence vector is

\[
 \boxed{
  2qg_R(e_e-e_i).}                                 \tag{6.2}
\]

At \(q=1\), this is the literal lower- and upper-direction marginal
\(2g_R(e_e-e_i)\).  Formula (6.2) is compiler-order independent.

It is only a projection of the literal derivative (5.3).  Matching
direction marginals does not align the target identities at higher
depths.

## 7. Quantitative boundary

One slab contains \(2^{R+1}=2s\) owners.  The universal literal bound
(5.5) permits \(O(s)\) changed targets at each signed depth.  Summed over
\(O(H)\) signed depths, this is \(O(Hs)\) per slab.  If a positive
fraction of all owners is tiled by such slabs, the resulting uncancelled
absolute derivative can be \(O(WH)\), not \(o(W)\).

The direction projection is much smaller.  If only the support incidence
were charged, summing (6.2) over \(q\le H\) gives

\[
 O\!\left(g_RH^2\right)
\]

per slab and \(O(WH^2/R)\) over owner mass \(W\).  Even that need not be
small for an arbitrary \(H=o(m)\), and it does not control literal
targets.

Thus cross-parent slabs solve an exact **reachability** problem:
parent-cell image columns can interact through owner-preserving trades.
They do not solve the target-labelled covariance problem.

## 8. Boundary of the theorem

Proved:

* an exact formal parent-label model;
* impossibility of a one-status-coordinate rank-preserving change;
* an explicit minimal two-coordinate recoupling of different parent
  cells;
* exact preservation of all middle owners;
* preservation of the dense cross-half physical-axis property;
* exact reinstallability of the diverse-order compiler;
* the literal derivative (5.3)--(5.8); and
* the exact direction-support derivative (6.2).

Not proved:

* a positive-density matching of compatible parent fibres into such
  slabs;
* simultaneous choices of the deterministic \(R\)-axis selectors making
  those slabs abundant;
* cancellation of their all-depth literal derivatives; or
* coefficient one.

The parent label is therefore **not** the invariant blocking
cross-packet covariance.  The surviving problem is abundance and
target-labelled routing, not local owner reachability.
