# Global owner packing for the \(H\)-wide \(Q_8\) controller, and the exact target covariance gate

Date: 2026-07-26

Method: pure mathematics only.

## 0. Outcome

The owner-support problem for the \(H\)-wide \(Q_8\) controller has a
positive solution.  The exponentially sparse declared carrier in the
local theorem is not the right object to repeat.  Instead, take one
controlled macrocycle, choose its total dimension \(D\) to be a power of
two, and translate it by the kernel of a syndrome map for its actual
doubled-permutation word.  Those translates partition \(Q_D\) exactly.
Every translate is a physical coordinate conjugate of the complete
controller/carousel template, so the owner splice, literal compiler,
homogeneous collars, and phase colouring all remain valid.

Choose

\[
 \sqrt m\ll H=o(m),\qquad
 r=2n=O(H),\qquad
 D=2^s,\quad {m\over8}<D\le {m\over4},              \tag{0.1}
\]

and

\[
                         L={D-r-8\over8}.            \tag{0.2}
\]

For all sufficiently large \(m\), \(L\) is a positive integer and
\(L=\Theta(m)\).  Embedding the syndrome factors in the exact
rank-twisted/log-block status cells gives controlled macrocycles on

\[
                         G=W-o(W/H)                 \tag{0.3}
\]

middle owners.  There are no cross-packet seams.  The within-macro
controller-created literal collision ledger is

\[
 \sum_{q\le H}(E_q^-+E_q^+)
 \le {32H\over D}G=o(W).                            \tag{0.4}
\]

Thus the global owner packing and the within-macro homogeneous seam
accounting are proved.

The requested aggregate literal target conclusion does **not** follow.
The exact remaining obstruction is a grouped cross-macrocycle overlap
functional.  Order all depth-\(q\), sign-\(\pm\) target occurrences as
\(\tau_1,\ldots,\tau_{G_q^\pm}\), macro by macro, and put

\[
 {\cal R}_q^\pm
 =\sum_{a=1}^{G_q^\pm}
   {\bf1}\{\tau_a\in\{\tau_1,\ldots,\tau_{a-1}\}\}. \tag{0.5}
\]

If \(N_q^\pm\) is the target-layer size and \(M_q^\pm\) is the number of
missing targets, then

\[
 \boxed{M_q^\pm=N_q^\pm-G_q^\pm+{\cal R}_q^\pm.}    \tag{0.6}
\]

The local theorem controls only the seam part of \({\cal R}_q^\pm\).
It does not control inherited payload repeats or repeats whose first
occurrence lies in another macrocycle.  Rank-twisted first marginals and
complete conjugate averages do not control these terms either.  In the
central fixed-allocation slice with one addition in each of \(q\) blocks,
the exact capacity ratio is

\[
 \left({d/2\over d/2+1}\right)^q
 =\exp\!\left(-(2+o(1)){q\over d}\right).            \tag{0.7}
\]

At \(q=A\sqrt m\) and \(d=\Theta(\log m)\), this tends to zero.  This is
a decorated allocation deficit rather than a raw-target cut, and proves
that cross-allocation negative covariance is genuinely necessary.

The final verdict is therefore sharp: the full owner-disjoint controlled
carrier theorem is true, with leave \(o(W/H)\), but aggregate target loss
\(o(W)\) remains exactly the integral grouped Hall/covariance problem
recorded in (0.5)--(0.7).

## 1. Parameters and physical coordinate ledger

Use the certified controller on \(Q_r\) from the \(H\)-wide local theorem.
It is obtained from

\[
                         n=4\cdot2^t,\qquad r=2n,    \tag{1.1}
\]

where \(n\) is least with \(n\ge2(H+1)\).  Hence

\[
              4(H+1)\le r<8(H+1),\qquad r=O(H).     \tag{1.2}
\]

Let \(D\) be the largest power of two not exceeding \(m/4\).  Then

\[
                         {m\over8}<D\le {m\over4}.  \tag{1.3}
\]

Both \(D\) and \(r\) are divisible by eight.  Since \(r=o(m)\), for all
sufficiently large \(m\),

\[
                         D>r+8,\qquad
                         L={D-r-8\over8}\in\mathbb N,\qquad
                         L\ge H.                    \tag{1.4}
\]

Inside one physical \(Q_D\) packet, split the active axes disjointly as

\[
 [D]=R\mathbin{\dot\cup}B
        \mathbin{\dot\cup}P_0\mathbin{\dot\cup}\cdots
        \mathbin{\dot\cup}P_7,                      \tag{1.5}
\]

where

\[
 |R|=r,\qquad |B|=8,\qquad |P_t|=L.                 \tag{1.6}
\]

These are respectively the controller, carousel, and eight payload
blocks.  Every active axis is a split physical pair in a rank-twisted
status cell.  Toggling it swaps the chosen endpoint of that pair and is
therefore one Johnson exchange preserving middle rank.

The local-rank vector, zero/full pair statuses, unused split orientations,
residual coordinates, and exterior tag pairs are frozen.  They locate the
packet but contribute no active owner dimension.  Hence (1.5) is the
complete active-support ledger; no controller, carousel, payload, or tag
coordinate has been counted twice.

## 2. Linear-dimensional rank-twisted owner packets

The published rank-twisted owner theorem was stated for \(r=o(m)\), but
its same proof gives the linear dimension (1.3).

Let the logarithmic macroblock half-size be

\[
                         d=\Theta(\log m),           \tag{2.1}
\]

chosen divisible by four, and let
\(N=db=m+O(d)\) be the number of matched physical pairs outside
the residual coordinates.  Fix a local-rank vector.  For its induced
matching, the number \(S\) of split pairs under an unconditioned uniform
subset has law

\[
                         S\sim{\rm Bin}(N,1/2).      \tag{2.2}
\]

Because \(D\le m/4\), a Chernoff bound gives

\[
                         \Pr(S<D)\le e^{-c m}        \tag{2.3}
\]

for an absolute \(c>0\).  There are

\[
 (2d+1)^b
 =\exp\!\left(O\!\left({m\log d\over d}\right)\right)
 =\exp(o(m))                                        \tag{2.4}
\]

local-rank vectors, and the residual-coordinate factor is \(2^{O(d)}\).
The same union bound as in the rank-twisted theorem therefore gives

\[
 \#\{X\in {[2m]\choose m}:S(X)<D\}
 \le 2^{2m}e^{-cm+o(m)}
 =W e^{-cm+o(m)}
 =o(W/H).                                           \tag{2.5}
\]

Every good cell is a \(Q_S\) with \(S\ge D\).  Choose \(D\) of its axes
and freeze every orientation of the remaining \(S-D\) axes.  This
partitions the cell into physical \(Q_D\)'s.  We have proved:

### Lemma 2.1 (linear rank-twisted packet tiling)

There is an owner-disjoint family of physical \(Q_D\) packets covering
\(W-o(W/H)\) middle owners.  All their active axes cross the two halves
of logarithmic macroblocks.

The upper bound \(D<m/2\) is essential for this argument: the typical
status-cell dimension is \((1/2+o(1))m\).  The choice (1.3) leaves a fixed
Chernoff margin.

## 3. A syndrome factor for the actual macro word

We record the exact translation theorem because it is the step which
turns the sparse local carrier into a full owner factor.

### Lemma 3.1 (arbitrary-order doubled-permutation factor)

Let \(D=2^s\), and let

\[
                         \Pi=(\pi_1,\ldots,\pi_D)    \tag{3.1}
\]

be any permutation of the directions of \(Q_D\).  The cycle with word
\(\Pi\Pi\) has a translation-kernel factor

\[
                         Q_D=\dot\bigcup_{k\in K}(C_\Pi+k),       \tag{3.2}
\]

where

\[
                         |K|={2^D\over2D}.           \tag{3.3}
\]

All cycles in (3.2) have one common phase colouring and one common
direction word.

#### Proof

Let \(U=\mathbb F_2^s\), and let

\[
                         u_0,u_1,\ldots,u_{D-1}      \tag{3.4}
\]

be any enumeration of \(U\) with \(u_0=0\).  Put

\[
                         \Sigma=U\oplus\langle v\rangle.          \tag{3.5}
\]

Define a linear syndrome map
\(\phi:\mathbb F_2^D\to\Sigma\) by

\[
 \begin{aligned}
 \phi(e_{\pi_j})&=u_j+u_{j-1} &&(1\le j<D),\\
 \phi(e_{\pi_D})&=v+u_{D-1}.&
 \end{aligned}                                      \tag{3.6}
\]

If \(p_j=e_{\pi_1}+\cdots+e_{\pi_j}\), then the first-half prefix
syndromes are

\[
                         \phi(p_j)=u_j\quad(0\le j<D),            \tag{3.7}
\]

and \(\phi(p_D)=v\).  The second-half prefix syndromes are
\(v+u_j\).  Thus the \(2D\) vertices of \(C_\Pi\) meet every syndrome
fibre exactly once.

Let \(K=\ker\phi\).  If two translates \(C_\Pi+k\) and \(C_\Pi+k'\)
meet, then two vertices of \(C_\Pi\) have the same syndrome; hence they
are equal and \(k=k'\).  The translates are disjoint.  Their total size is

\[
 |K|\,2D=2^{D-(s+1)}2D=2^D,                         \tag{3.8}
\]

so they partition \(Q_D\).  Giving \(p_j+k\) phase \(j\bmod2D\) is
well-defined and common to all translates.  \(\square\)

## 4. Installing the controlled \(Q_8\) macro in the syndrome factor

Choose one cycle \(C\) of the exact phasewise \(Q_8\) splice and one cycle
\(Y\) of the certified controller.  Write the controller first-half word
as

\[
                         \kappa=BA,\qquad |A|=|B|\ge H.           \tag{4.1}
\]

Choose ordered payload paths \(\rho_t\) on \(P_t\), and put

\[
 \Sigma_0=w_0,\rho_0,w_1,\rho_1,\ldots,w_7,\rho_7,
 \qquad
 \Pi=B\,\Sigma_0\,A.                                \tag{4.2}
\]

The local controller theorem proves that \(\Pi\) is a permutation of all
\(D\) active directions and that the seed word \(\Pi\Pi\) is an
owner-valid controlled isometric \(C_{2D}\).

Apply Lemma 3.1 to this **actual** order \(\Pi\).  It remains to justify
that every kernel translate is still a legal controlled macro, not merely
an abstract cube cycle.

For \(k\in\mathbb F_2^D\), translation by \(k\) in the orientation cube
is physically the coordinate permutation which swaps the two endpoints
of every active pair \(e\) with \(k_e=1\).  Call it \(\sigma_k\).  It is
an automorphism of the Boolean inclusion graph and of the Johnson middle
layer.  Apply \(\sigma_k\) simultaneously to

1. the selected phasewise \(Q_8\) factor and all its \(X/Y\) rows;
2. the selected controller factor and its literal trace decoder;
3. the payload paths and their homogeneous collar frames; and
4. the mixed-boundary frame identifications.

This sends the seed macro to \(C_\Pi+k\).  Every owner equation and every
inclusion edge is conjugated to the corresponding valid equation or edge.
In particular, the identities

\[
                         \Xi_t^-=\Xi_{t+1}^+         \tag{4.3}
\]

survive exactly, and the controller trace at both turnarounds is the
conjugate of the certified trace.  Lemma 3.1 gives one common phase index
on all translates, so the context-array decoder remains phase-compatible.

Different translates may use different conjugates of the child factors.
This is harmless: their complete owner supports are disjoint by (3.2),
and no local row is shared between two macros.  No assertion that the
untranslated sparse declared carriers tile their Cartesian product is
being made.

We conclude:

### Theorem 4.1 (full controlled macro-factor)

Every physical \(Q_D\) packet in Lemma 2.1 has an exact factor into
\(2^D/(2D)\) owner-disjoint controlled \(Q_8\)-carousel macrocycles.
Every macro has the \(H\)-wide controller at both turnarounds, eight
homogeneous payload collars in each half, and the same global phase
colouring.

Taking these factors independently in all rank-twisted packets proves the
owner assertion (0.3).  Since cycles never cross packet boundaries, there
are no inter-packet or inter-cell seams.

## 5. Seam and compiler-conjugate ledger

Let \(M\) be the total number of selected macrocycles.  Apart from the
\(o(W/H)\) owner leave,

\[
                         G=2DM=W-o(W/H).             \tag{5.1}
\]

The local \(H\)-wide theorem gives, for every seed macro,

\[
 \sum_{q\le H}(E_q^-+E_q^+)\le64H.                 \tag{5.2}
\]

All within-macro target equalities and inequalities in that proof are
invariant under the physical conjugations \(\sigma_k\).  Summing (5.2)
over all macros,

\[
 \sum_{q\le H}(E_q^-+E_q^+)
 \le64HM={32H\over D}G=o(W),                        \tag{5.3}
\]

because \(H/D\to0\).  Frozen exterior tags merely duplicate the same
within-macro identity on disjoint owner packets and add no geometric seam.

Equation (5.3) charges only collisions created by the controller and
carousel interfaces.  As in the local theorem, any inherited collision
inside a long payload segment must be zero by the payload construction or
charged separately.  Moreover, the four frozen tag pairs in the local
proof distinguish its sixteen original \(Q_8\) base cycles; they do not
give distinct tags to the exponentially many syndrome-kernel translates.
Thus (5.3) is not a bound on seam-window collisions between different
kernel translates.  Those are part of the exact packet and global
overlap ledgers below.  This distinction is essential in the target
audit.

## 6. Exact literal-target overlap identity

Before introducing the global overlap functional, one can compute the
within-packet incidence of the actual syndrome factor exactly.

Fix a packet and a cyclic \(q\)-window support

\[
 J_j=\{\pi_{j+1},\ldots,\pi_{j+q}\},\qquad 0\le j<D, \tag{6.1}
\]

with indices modulo \(D\), and put

\[
 V_j=\phi(\mathbb F_2^{J_j}),\qquad h_j=\dim V_j.    \tag{6.2}
\]

A lower target produced at this phase contains no endpoint of the active
pairs in \(J_j\), and contains the selected endpoint of every active pair
outside \(J_j\).  Thus it is exactly a \(J_j\)-face label, determined by
the outside orientation.  The possible outside orientations at the first
occurrence of this window form one coset of

\[
 P_j=\operatorname{pr}_{[D]\setminus J_j}K.          \tag{6.3}
\]

Rank-nullity gives

\[
 \begin{aligned}
 |K\cap\mathbb F_2^{J_j}|&=2^{q-h_j},\\
 |P_j|&={|K|\over|K\cap\mathbb F_2^{J_j}|}
       =2^{D-(s+1)-q+h_j}.                           \tag{6.4}
 \end{aligned}
\]

The antipodal occurrence, \(D\) phases later, shifts the outside
orientation by \({\bf1}_{[D]\setminus J_j}\).  Its coset is the same as
the first one exactly when

\[
 \phi({\bf1}_{[D]\setminus J_j})\in V_j.
\]

Since \(\phi({\bf1}_{[D]})=v\) and
\(\phi({\bf1}_{J_j})\in V_j\), this is equivalent to \(v\in V_j\).
Define

\[
 c_j=
 \begin{cases}
 1,&v\in V_j,\\
 2,&v\notin V_j.
 \end{cases}                                        \tag{6.5}
\]

The two occurrences therefore cover exactly \(c_j|P_j|\) distinct
lower targets of active empty-pair type \(J_j\).  If \(c_j=1\), each is
hit \(2^{q-h_j+1}\) times; if \(c_j=2\), each is hit
\(2^{q-h_j}\) times.  The same statement holds for upper targets after
replacing empty active pairs by full active pairs.

Because \(q<D\), the \(D\) cyclic supports \(J_j\) are distinct.  Hence
targets belonging to different \(j\)'s have different active
empty/full-pair types and cannot coincide inside this packet.  The exact
number of repeated lower occurrences in the packet is consequently

\[
 {\cal R}^{\rm packet}_{P,q}
 =2^D-\sum_{j=0}^{D-1}
 c_j\,2^{D-(s+1)-q+h_j}.                            \tag{6.6}
\]

This is the physical Walsh/Gram ledger of the syndrome translates.  It
contains no probabilistic approximation.  It also identifies the
remaining design freedom precisely: one must choose the syndrome
enumeration and the physical order so that the sliding images \(V_j\)
make (6.6) compatible with the forced global overload, while coordinating
the resulting target cosets between different rank-twisted packets.

Fix a sign and depth \(q\).  Every covered owner contributes one target
occurrence.  Order these occurrences macro by macro as

\[
                         \tau_1,\ldots,\tau_{G_q^\pm}.            \tag{6.7}
\]

The \(o(W/H)\) owner leave gives

\[
                         G_q^\pm=W-o(W/H)            \tag{6.8}
\]

for each \(q\); summing the lost occurrences over \(q\le H\) costs
\(o(W)\).

For a literal target \(T\), put

\[
                         \ell_T=|\{a:\tau_a=T\}|.    \tag{6.9}
\]

Define the repeat count

\[
 {\cal R}_q^\pm
 =\sum_T(\ell_T-1)_+
 =\sum_{a=1}^{G_q^\pm}
   {\bf1}\{\tau_a\in\{\tau_1,\ldots,\tau_{a-1}\}\}. \tag{6.10}
\]

If \(N_q^\pm\) is the number of targets and
\(M_q^\pm=|\{T:\ell_T=0\}|\), then

\[
 \begin{aligned}
 G_q^\pm
 &=|\{T:\ell_T>0\}|+\sum_T(\ell_T-1)_+\\
 &=N_q^\pm-M_q^\pm+{\cal R}_q^\pm.
 \end{aligned}                                      \tag{6.11}
\]

This proves (0.6).  Therefore

\[
 \boxed{
 \sum_{q\le H,\,\pm}M_q^\pm=o(W)
 \iff
 \sum_{q\le H,\,\pm}
 \left({\cal R}_q^\pm-(G_q^\pm-N_q^\pm)\right)=o(W).}             \tag{6.12}
\]

The repeat count has three disjoint sources, classified by the first
earlier occurrence of the same target:

1. controller/carousel seam repeats inside the same macro, bounded in
   aggregate by (5.3);
2. inherited payload repeats inside the same macro, not covered by
   (5.3); and
3. repeats whose first occurrence is in an earlier macro, the genuine
   cross-macrocycle covariance.

The global owner factor proves no estimate for items 2 and 3.  In
particular, the fact that every conjugate occurs with a correct aggregate
first marginal determines \(G_q^\pm\), but not \({\cal R}_q^\pm\).

## 7. The grouped Hall/covariance obstruction

The remaining choice can be stated without ambiguity.  Let \({\cal P}\)
be the owner-disjoint rank-twisted \(Q_D\) packets.  For \(P\in{\cal P}\),
let \(\Omega_P\) be a permitted library of physical direction bijections,
syndrome seeds, and compiler conjugates.  Every
\(\omega\in\Omega_P\) gives a complete owner factor of \(P\).  Put

\[
 a_{P,\omega}^{q,\pm}(T)
 =\hbox{number of depth-\(q\), sign-\(\pm\) occurrences of \(T\)
        in that factor}.                            \tag{7.1}
\]

Coefficient one asks for variables

\[
 x_{P,\omega}\in\{0,1\},\qquad
 \sum_{\omega\in\Omega_P}x_{P,\omega}=1             \tag{7.2}
\]

whose induced target loads have total zero set \(o(W)\) over all
\(q\le H\).  This is a grouped integral coverage problem: ownership is
already exact for every column, but one whole column must be selected in
each packet.

Even the fractional Hall condition is a union, not a marginal, condition.
For exact fractional coverage of a protected target family \({\cal A}\),
the separating-hyperplane test is

\[
 \sum_{P\in{\cal P}}\max_{\omega\in\Omega_P}
       \sum_{T\in{\cal A}}y_T
          a_{P,\omega}^{q,\pm}(T)
 \ \ge\ \sum_{T\in{\cal A}}y_T                     \tag{7.3}
\]

for every choice \(y_T\ge0\).  This is necessary and sufficient for the
image of the product of the packet simplices to meet the target-covering
orthant.

There is an equally exact reserve version.  If at most \(R\) targets may
be omitted fractionally, let

\[
 {\cal Z}_R=\{z\in[0,1]^{\cal A}:\sum_Tz_T\le R\},
 \qquad
 \rho_R(y)=\max_{z\in{\cal Z}_R}\sum_Ty_Tz_T.        \tag{7.4}
\]

Thus \(\rho_R(y)\) is the sum of the \(R\) largest weights, with the last
one taken fractionally when \(R\) is not integral.  The exact fractional
near-Hall condition is

\[
 \sum_{P\in{\cal P}}\max_{\omega\in\Omega_P}
       \sum_{T\in{\cal A}}y_Ta_{P,\omega}^{q,\pm}(T)
       +\rho_R(y)
 \ge\sum_{T\in{\cal A}}y_T                         \tag{7.5}
\]

for all \(y\ge0\).  Passing (7.5) still would not by itself round (7.2)
integrally at the required simultaneous accuracy.

Two exact earlier audits show why no current theorem verifies (7.3), or
its reserve form (7.5).

First, frozen selector data are recoverable from literal targets.
Conditional on one selector value, a target sees one selected column,
not the average over a complete conjugate batch.  Thus complete batching
proves first marginals but not the grouped union in (7.3).

At the present linear packet dimension there is also no room to realize
the complete affine batch inside one status cell.  Its number of columns
is at least \(D!\), so

\[
                         \log_2(D!)=\Theta(m\log m), \tag{7.6}
\]

whereas a \(Q_S\) status cell has only \(S=O(m)\) selector and active
bits in total.  The owner theorem avoids this entropy cost by choosing
one conjugate independently in each already disjoint \(Q_D\) packet.
That is enough for ownership, but it supplies no literal-target averaging
within a frozen packet group.

Second, take the fixed allocation with \(\ell_j=1\) on \(q\) blocks and
zero elsewhere, and take the exact central statuses
\(e_j=d/4,u_j=d/2\) on those blocks.  Its source/target compatibility
ratio is exactly

\[
 R_{\boldsymbol\ell}
 =\left({d/2\over d/2+1}\right)^q,\qquad
 \log R_{\boldsymbol\ell}
 =-(2+o(1)){q\over d}.                              \tag{7.7}
\]

At \(q=A\sqrt m\), \(d=\Theta(\log m)\), this tends to zero.  For the
indicator weight of that decorated central slice, one frozen allocation
fails the Hall test by a \(1-o(1)\) fraction.  This is not by itself a raw
target cut, because one raw target occurs in many allocation decorations.
Rank twisting can repair it only if source neighborhoods from different
allocations and frames have enough **new union**, not merely enough summed
size.  If
\(N_\alpha({\cal A})\) is the compatible source set in allocation
\(\alpha\), the missing estimate is

\[
 \left|\bigcup_\alpha N_\alpha({\cal A})\right|
 \ge|{\cal A}|-o(W),                                \tag{7.8}
\]

coupled to one common integral choice (7.2) at every depth.  Existing
compatibility polynomials calculate each \(|N_\alpha({\cal A})|\); they do
not calculate or bound the overlaps which decide (7.8).

Equivalently, (6.12) says that the selected columns must create negative
cross-packet covariance of order \(W\) relative to diffuse selection.  In
the Poisson regime, independent columns with mean target load
\(\lambda=\Theta(1)\) leave
\(e^{-\lambda}N_q^\pm=\Theta(W)\) targets uncovered at a fixed central
depth.  Marginal symmetrization alone cannot remove that zero class.

## 8. Final theorem and exact residual

### Theorem 8.1 (global controlled-owner factor)

Let \(\sqrt m\ll H=o(m)\).  With \(r,D,L\) chosen by
(1.1)--(1.4), there exists an owner-disjoint family of physical
isometric \(C_{2D}\) macrocycles in the middle layer such that:

1. the owner leave is \(o(W/H)\);
2. every cycle is an affine physical conjugate of the \(H\)-wide
   controlled \(Q_8\) carousel macro;
3. controller, carousel, payload, and frozen tag supports have the exact
   disjoint ledger (1.5)--(1.6);
4. all cycles retain the certified common phase colouring, literal
   controller decoder, and homogeneous frame identities;
5. no seam is introduced between rank-twisted packets or macrocycles; and
6. the aggregate **within-macro** collision contribution created by the
   controlled seams is \(o(W)\), quantitatively at most
   \((32H/D)G\); cross-macro repeats are governed by (6.6) and (6.10).

#### Proof

Lemma 2.1 supplies the \(Q_D\) owner packets.  Lemma 3.1 factors every
packet by kernel translates of the actual macro word.  Section 4 proves
that every translate is an owner-valid physical conjugate of the complete
local template.  Equation (5.3) proves the seam estimate.  \(\square\)

### Exact unresolved statement

The stronger claim

\[
                 \sum_{q\le H,\,\pm}M_q^\pm=o(W)    \tag{8.1}
\]

is neither proved nor implied by Theorem 8.1.  By (6.12), its exact
remaining integral discrepancy is

\[
 \sum_{q\le H,\,\pm}
 \left({\cal R}_q^\pm-(G_q^\pm-N_q^\pm)\right),     \tag{8.2}
\]

after subtracting the already controlled seam part and separately
accounting for inherited payload repeats.  The fixed-stratum deficit
(7.7) proves that a one-frame or one-allocation choice cannot close this
quantity.  A coefficient-one completion must prove the grouped
cross-allocation union/covariance estimate (7.3)--(7.8), with one integral
column per owner packet and simultaneous accuracy \(o(W)\) over all
depths.

This is the explicit obstruction left by the global audit; it is not an
owner-support, coordinate-budget, phase, or seam obstruction.

## 9. Subsequent closure of the common-order target gate

The follow-up note

\[
\texttt{MATH\_OBSTRUCTION\_COMMON\_ORDER\_SYNDROME\_GAUSSIAN\_REPEAT\_20260726.md}
\]

closes (8.1) negatively for the particular syndrome-kernel factors proved
here.  In one \(Q_D\) packet, a common doubled-permutation order has only
\(D\) depth-\(q\) interval supports, each exposing at most \(2^{D-q}\)
literal targets.  Consequently all packets together cover at most
\((D/2^q)G=o(W)\) targets when \(q=A\sqrt m\), and the missing target
mass is at least \((e^{-A^2}-o(1))W\).

Thus the grouped Hall problem in Sections 7--8 is not merely unproved for
the common-order construction: it fails.  Any surviving replacement must
use exponentially many direction-order supports inside each exact
\(Q_D\) owner factor.

The later parity-complete diverse-order packet factor supplies precisely
that local support diversity at a smaller scale \(H\ll R\ll m\).  It is
not subject to this common-order failure; its remaining discrepancy is
cross-packet only, as recorded in
\(\texttt{MATH\_AUDIT\_DIVERSE\_ORDER\_COMPILER\_CROSS\_PACKET\_COVARIANCE\_20260726.md}\).
