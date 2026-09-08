# A linear-scale diverse-order mixer with fused signs and exact all-depth laminar incidence

Date: 2026-07-26

Method: pure mathematics only.

## 0. Outcome

Let

\[
                         H=H(m),\qquad H=o(m),qquad H\to\infty,
                                                                    \tag{0.1}
\]

and put

\[
 \Omega=\binom{[2m]}m,\qquad W=|\Omega|=\binom{2m}m.             \tag{0.2}
\]

At depth \(q\), write

\[
 N_q=\binom{2m}{m-q},\qquad c_q=\left\lfloor{W\over N_q}\right\rfloor
                                                                  \tag{0.2a}
\]

for the number of physical lower targets, equivalently upper targets,
and the desired base clone quota.

For a directed owner successor \(P\), use the literal window notation

\[
 L_q(X)=\bigcap_{i=0}^qP^iX,\qquad
 U_q(X)=\bigcup_{i=0}^qP^iX.                                  \tag{0.2b}
\]

The diverse-order compiler can be installed at **linear** packet scale.
Choose the largest admissible

\[
                         R=8\cdot2^t\le {m\over64}.             \tag{0.3}
\]

Then

\[
                         {m\over128}<R\le {m\over64},
 \qquad H\le {R\over4}-1                                     \tag{0.4}
\]

for all sufficiently large \(m\).

There is an explicit complement-equivariant, owner-disjoint family of
physical \(Q_R\)-packets covering

\[
 0\le W-G\le e^{-m/16}W,\qquad
                         G=W-o(W/H)                             \tag{0.5}
\]

middle owners, for all sufficiently large \(m\), with the following
properties.

1. Every packet is factored exactly by the parity-complete diverse-order
   compiler into isometric cycles \(C_{2R}\).  Hence every component has
   length

   \[
                                  2R=\Theta(m).                 \tag{0.6}
   \]

2. Every cyclic window of length at most \(H\) is a Johnson geodesic.
   For every \(q\le H\), both literal trace maps are injective on all
   owners of each packet.

3. The packet tiling uses a dense recursive mixer: in every good product
   cell, \(16R\) split axes are divided into \(R\) groups of sixteen.  An
   exact balanced perfect matching of each \(Q_{16}\) chooses one active
   physical direction per group.  Cartesian products of those edges are
   the \(Q_R\)-packets.  Thus packet axes are not supplied by bounded
   reset colours or sparse splices.

4. The complete trace map is injective not only inside a packet but over
   every entire parent product cell.  Consequently all literal repeats
   are between distinct product cells.

5. The factor is complement-equivariant.  If \(P\) is the physical owner
   successor, then

   \[
                                  P(X^c)=P(X)^c.                 \tag{0.7}
   \]

   Hence, occurrence by occurrence,

   \[
                                  U_q(X^c)=L_q(X)^c.            \tag{0.8}
   \]

   The fused signed-pair clone constraint is therefore realized exactly,
   at every protected depth, without an independent lower/upper choice.

6. Inside every product cell, the depth images are joined by canonical
   bijective shadow maps

   \[
      I_{C,1}^-\longleftarrow I_{C,2}^-\longleftarrow\cdots
                    \longleftarrow I_{C,H}^-                  \tag{0.9}
   \]

   and the dual upper maps.  Thus the physical occurrences form exact
   all-depth laminar flags.  Any reset-aware clone relabelling already
   feasible for the common run vector can be transported along these
   flags; the mixer introduces no further chronological inconsistency.

7. The number of cycles is

   \[
                                  {G\over2R}=O(W/m)=o(W/H).     \tag{0.10}
   \]

This proves the long-cycle, \(H\)-spaced, owner, complement,
and parent-cell literal-trace theorem.  It also proves that no stable
odd cut reappears at any finite \(H\le R/4-1\) **inside a packet or one
parent product cell**: an explicit integral factor and its exact laminar
flags exist there.

It does not prove global floor/ceiling quotas.  If \(I_{C,q}^\pm\) is the
literal image of one parent product cell, the only remaining energy is

\[
 \boxed{
 \mathcal E_q^\pm
   =\sum_{C<D}|I_{C,q}^\pm\cap I_{D,q}^\pm|.}                  \tag{0.11}
\]

The fused relation makes the two signs equivalent under complementation.
The first unresolved obstruction is therefore cross-cell covariance, not
a higher-memory local odd set.  Independent compiler/context choices are
known to leave \(\Omega(W)\) Gaussian holes, so a global constant-one
theorem still requires correlated cross-cell mixing.

## 1. Linear admissible scale

The parity-complete compiler is available when its physical dimension is

\[
                         R=2n,qquad n=4\cdot2^t.                \tag{1.1}
\]

Successive admissible values differ by a factor two.  Therefore the
largest one satisfying (0.3) obeys \(R>m/128\).  Since \(H=o(m)\),

\[
                         H\le {R\over4}-1                       \tag{1.2}
\]

eventually.  The compiler's literal physical recovery theorem applies
through depth

\[
                         {n\over2}-1={R\over4}-1,               \tag{1.3}
\]

so it covers every protected depth.

The old choice \(R\asymp\sqrt{mH}\) minimized packet mass.  It is not
needed for the owner theorem.  The linear choice (0.3) is what produces
components of length \(\Omega(m)\).

## 2. Complement-equivariant rank-twisted cells

Fix explicitly

\[
 d=4\left\lceil {5\over2}\log _2m\right\rceil ,
 \qquad J=\left\lfloor {m\over d}\right\rfloor ,
 \qquad n=dJ.                                                   \tag{2.0}
\]

Thus \(d=(10+o(1))\log _2m\), \(d\) is a multiple of four, and

\[
                         m-d<n\le m.                            \tag{2.0a}
\]

Partition almost all physical coordinates into macroblocks

\[
                         B_j=A_j\mathbin{\dot\cup}C_j,
                         \qquad |A_j|=|C_j|=d,                  \tag{2.1}
\]

for \(1\le j\le J\), and freeze the fewer than \(2d\) residual
coordinates cellwise.  When the fixed quartet background is retained,
choose each half as a union of \(d/4\) old quartets; this is why \(d\)
was made divisible by four.  Index both halves by \(\mathbb Z_d\).  For
\(0\le k<d\), let

\[
 M_{j,k}=\{a_{j,u}c_{j,u+k}:u\in\mathbb Z_d\};                 \tag{2.2}
\]

put \(M_{j,d}=M_{j,0}\), and for \(d<k\le2d\) put

\[
                         M_{j,k}=M_{j,2d-k}.                    \tag{2.3}
\]

This gives the required complement symmetry and the union of the local
frames is exactly \(K_{d,d}\).

Fixing the zero/singleton/full status of every matching edge partitions
the local rank layer into orientation cubes.  Complementation sends rank
\(k\) to rank \(2d-k\), swaps zero and full statuses, and flips every
singleton orientation.  Equation (2.3) therefore sends every product
cell \(C\cong Q_S\) to a product cell \(C^c\cong Q_S\) with the same
ordered set of flexible axes.

This symmetry changes none of the owner-partition proof.  Different local
ranks are disjoint, and every rank layer is still partitioned by status
vectors.

### The all-depth full-block threshold

The coordinate-union component seen by the full-block dual is one
macroblock \(B_j\), of size

\[
                         b_*=2d.
\]

Let \(X_k\) be the number of middle owners having exactly \(k\) full
complete macroblocks, let \(T_{q,k}\) be the analogous number of
rank-\((m-q)\) targets, and write

\[
 \Delta_{m,2d}(q)=\sum_{k\ge0}(T_{q,k}-X_k)_+.                  \tag{2.3a}
\]

The sharp Gaussian all-depth escape criterion is

\[
                         {2^{b_*}\over b_*}\gg m^{1/3}.         \tag{2.4}
\]

Our explicit choice has

\[
 {2^{2d}\over2d}\ge {m^{20}\over2d}\gg m^{1/3},                \tag{2.5}
\]

so it lies far above that threshold.  In fact one can verify the needed
scope directly for the whole range \(H\le m\).  In a uniform rank-\(r\)
set with \(2d\le r\le m\), a fixed complete macroblock is full with
probability

\[
 {\binom{2m-2d}{r-2d}\over\binom{2m}{r}}
 =\prod_{i=0}^{2d-1}{r-i\over2m-i}
 \le2^{-2d}.                                                   \tag{2.6}
\]

For \(r<2d\) that probability is zero, so the same upper bound holds.

There are \(J\le m/d\) complete macroblocks.  Hence the owner or target
mass having any full macroblock is at most \(J2^{-2d}\) of its layer.
For \(q\ge1\), the zero-full-block middle stratum is larger than the
corresponding rank-\((m-q)\) target stratum for all sufficiently large
\(m\), because

\[
 {W-N_q\over W}\ge {1\over m+1},
 \qquad J2^{-2d}=O(m^{-19}/d).
\]

Therefore every positive full-block profile deficit is supported on
targets with at least one full macroblock, and

\[
 \sum_{q\le H}\Delta_{m,2d}(q)
 \le H\,WJ2^{-2d}
 =o(W) \qquad(H\le m).                                        \tag{2.7}
\]

The complementary empty-block statement is identical.  Thus the block
choice is above the full all-depth threshold throughout the scope of
this note, not merely at one depth.

## 3. Exponentially small low-dimension leave

The binomial law must be used before, not after, conditioning on a
local-rank vector.  There is in fact an exact aggregate census which
removes the rank-vector union bound entirely.

For an unconditioned uniformly random subset \(X\subseteq[2m]\), put

\[
 K_j=|X\cap B_j|,\qquad
 Y_j=\#\{\text{singleton edges of }M_{j,K_j}\text{ in }X\}.    \tag{3.1}
\]

For any fixed perfect matching of one \(2d\)-coordinate block, the joint
rank/singleton enumerator is

\[
                         (1+2uz+z^2)^d.                        \tag{3.2}
\]

The coefficient of \(z^k u^s\) counts rank-\(k\) subsets with \(s\)
singleton edges and depends only on \(d,k,s\), not on which perfect
matching was used.  We may therefore use \(M_{j,k}\) separately in the
coefficient of \(z^k\); summing over \(k\) leaves the same polynomial
(3.2).  Setting \(z=1\) gives

\[
 \sum_{X_j\subseteq B_j}u^{Y_j(X_j)}
     =(2+2u)^d=2^d(1+u)^d.
\]

Thus, under the unconditioned local subset law,

\[
                         Y_j\sim\operatorname{Bin}(d,1/2).     \tag{3.3}
\]

The complete macroblocks are disjoint, so the \(Y_j\)'s are independent.
Consequently the actual adaptive product-cell dimension

\[
                         S(X)=\sum_{j=1}^JY_j
                         \sim\operatorname{Bin}(n,1/2)         \tag{3.4}
\]

exactly under the unconditioned Boolean-cube law.  No law conditional
on a fixed rank vector, and no union over rank vectors, is used.

Call a product cell good when

\[
                                  S\ge16R.                      \tag{3.5}
\]

By (0.3), \(16R\le m/4\).  For all sufficiently large \(m\), (2.0a)
gives \(n\ge7m/8\), so

\[
 {n\over2}-16R\ge {3m\over16}.
\]

Hoeffding's inequality applied to (3.4) therefore gives

\[
 \Pr(S(X)<16R)
 \le\exp\left[-{2(3m/16)^2\over n}\right]
 \le e^{-9m/128}.                                               \tag{3.6}
\]

Finally,

\[
 \Pr(|X|=m)={W\over2^{2m}}=\Theta(m^{-1/2}).                    \tag{3.7}
\]

Conditioning (3.6) on \(|X|=m\) therefore costs only
\(O(\sqrt m)=e^{o(m)}\), and yields

\[
 {1\over W}\#\{X\in\Omega:S(X)<16R\}
 \le\exp\{-(9/128-o(1))m\}
 \le e^{-m/16}                                                  \tag{3.8}
\]

for all sufficiently large \(m\).  The bad-cell set is
complement-invariant by Section 2.  Discarding it proves (0.5), now with
the explicit admissible bound \(W-G\le e^{-m/16}W\).

## 4. The balanced \(Q_{16}\) direction matcher

Index sixteen cube coordinates by \(V=\mathbb F_2^4\).  Identify \(V\)
with \(\mathbb F_{16}\), choose any
\(\alpha\in\mathbb F_{16}\setminus\{0,1\}\), and let
\(M(v)=\alpha v\).  Then both \(M\) and \(I+M\) are invertible.  For an
even word \(x\in Q_{16}\), put

\[
 \sigma(x)=\sum_{u\in V}x_u u,
 \qquad d(x)=(I+M)\sigma(x),
 \qquad f(x)=x\oplus e_{d(x)}.                                 \tag{4.1}
\]

For completeness, suppose \(f(x)=f(y)\), and put
\(a=d(x), b=d(y)\).  Then \(x\oplus y=e_a\oplus e_b\), whence

\[
 \sigma(x)\oplus\sigma(y)=a\oplus b,\qquad
 a\oplus b=(I+M)(a\oplus b).
\]

Thus \(M(a\oplus b)=0\), so \(a=b\) and then \(x=y\).  The even and odd
shores have the same size, hence \(f\) is bijective.  Moreover the
restriction of the linear syndrome map to the even shore is onto, since
the even word \(e_0\oplus e_v\) has syndrome \(v\).  Hence all syndrome
fibres have size \(2^{15}/16\).  Since \(I+M\) permutes \(V\), every
direction occurs on exactly that many even words.
Consequently:

1. \(f\) is a bijection from the even to the odd shore, hence its edges
   form a perfect matching \(\mathcal M_{16}\) of \(Q_{16}\);
2. every one of the sixteen directions occurs exactly \(2^{15}/16\)
   times.

There is a further symmetry needed here.

### Lemma 4.1 (complement-equivariance)

If \(\bar x=x\oplus\mathbf1\), then

\[
                         f(\bar x)=\overline{f(x)}.             \tag{4.2}
\]

Thus complementation permutes the matching edges and preserves their
directions.

#### Proof

Since every coordinate of \(V=\mathbb F_2^4\) occurs in exactly eight
vectors,

\[
                         \sum_{u\in V}u=0.                     \tag{4.3}
\]

Hence \(\sigma(\bar x)=\sigma(x)\), so \(d(\bar x)=d(x)\).
Equation (4.2) follows from (4.1). \(\square\)

No matching edge is fixed by complementation: that would require
\(\mathbf1=e_i\) for one coordinate \(i\).

## 5. Exact dense \(Q_R\)-packet tiling

Fix a good product cell \(C\cong Q_S\).  Take the first \(16R\) flexible
axes in the complement-invariant physical ordering and partition them
into labelled groups

\[
                         G_1\mathbin{\dot\cup}\cdots
                         \mathbin{\dot\cup}G_R,
                         \qquad |G_h|=16.                       \tag{5.1}
\]

Freeze every orientation of the remaining \(S-16R\) axes in all possible
ways.  In each group \(G_h\), install the matching
\(\mathcal M_{16}\).  For a tuple of matching edges

\[
                         e=(e_1,\ldots,e_R),
                         \qquad e_h\in\mathcal M_{16},          \tag{5.2}
\]

put

\[
                         Q(e)=e_1\times\cdots\times e_R
                                  \cong Q_R.                    \tag{5.3}
\]

### Theorem 5.1 (linear dense packet partition)

Over all frozen spectator orientations and all tuples (5.2), the packets
(5.3) partition \(Q_S\) exactly.  Every packet has one active physical
axis in every group, and a uniform packet uses each of the sixteen
directions of a fixed group with probability exactly \(1/16\).

#### Proof

Every \(\mathcal M_{16}\) partitions its group cube into edges.  Cartesian
products of parts of these \(R\) partitions, together with singleton
parts on the spectator axes, partition their full Cartesian product
\(Q_S\).  The direction statement is the exact direction census
following (4.1).  Lemma 4.1 supplies the complementary pairing.
\(\square\)

Complementation sends the packet with frozen spectator word \(z\) and
edge tuple \(e\) to the packet with word \(\bar z\) and edge tuple
\(\bar e\).  No packet is fixed, so the packet partition is paired by
complementation.

## 6. Diverse-order compiler installation

Label the \(R\) abstract compiler directions by the groups
\(G_1,\ldots,G_R\).  In a packet \(Q(e)\), identify abstract direction
\(h\) with the physical direction of \(e_h\).  Install the canonical
parity-complete diverse-order factor \(F_R\).

If \(Q(\bar e)\) is the complementary packet, choose its abstract
coordinate identification so that

\[
                         \phi_{\bar e}(x)=\phi_e(x)^c           \tag{6.1}
\]

and install the same abstract factor \(F_R\).  It follows immediately
that the physical successor obeys (0.7).

The compiler theorem gives an exact factor of every packet into
isometric \(C_{2R}\)'s.  An isometric cube \(C_{2R}\) has a doubled-
permutation direction word: every block of at most \(R\) consecutive
directions is repetition-free.  Since \(H<R\), all protected physical
windows are Johnson geodesics.

The joint trace-recovery theorem is stronger.  For each sign and every
\(q\le R/4-1\), the literal trace map is injective on all \(2^R\) packet
owners, including both physical phases and closure-crossing starts.  By
(1.2), this includes every \(q\le H\).

Every component has length \(2R\), proving (0.6), and the total component
count is (0.10).

## 7. Literal face recovery across a parent cell

A packet face, viewed in the ambient orientation cube \(Q_S\), recovers
its unique packet.

### Lemma 7.1 (groupwise packet recovery)

Fix one group \(G_h\).  A literal lower trace records, on each of its
sixteen split pairs, either one selected ground endpoint or neither
endpoint.  The latter case occurs exactly on a direction used by the
window.  Since a geodesic window uses the packet direction \(h\) at most
once, there are two cases.

* If \(h\) is used, the trace is a \(15\)-bit orientation word with one
  star.  It is precisely the cube edge \(e_h\).
* If \(h\) is not used, the trace is one full orientation word, hence one
  endpoint of \(e_h\).  The perfect matching \(\mathcal M_{16}\) has a
  unique edge through that word, so it recovers \(e_h\).

For an upper trace, “neither” is replaced by “both”, and the same
recovery applies.  On a spectator split pair the trace always records
its one frozen endpoint.  Hence every ambient packet face recovers all
\(e_h\) and all frozen spectator orientations.

\(\square\)

### Theorem 7.2 (parent-cell literal rainbow)

For either sign and every \(q\le H\), the literal trace map on all owners
of one good parent product cell \(C\) is injective.

#### Proof

If two traces are equal, Lemma 7.1 recovers the same packet from both.
Compiler injectivity inside that packet then recovers the same owner
start. \(\square\)

Thus a parent cell of size \(2^S\) emits exactly \(2^S\) distinct lower
targets and exactly \(2^S\) distinct upper targets at every protected
depth.

## 8. Fused signs and exact laminar incidence

Equation (0.7) gives, for every owner start and depth,

\[
 \begin{aligned}
 U_q(X^c)
 &=\bigcup_{i=0}^qP^i(X^c)
 =\bigcup_{i=0}^q(P^iX)^c\\
 &=\left(\bigcap_{i=0}^qP^iX\right)^c
 =L_q(X)^c.
 \end{aligned}                                                 \tag{8.1}
\]

This proves the signed-pair fusion literally.  In particular the global
histograms of the partial factor satisfy

\[
                         \mu_q^+(T^c)=\mu_q^-(T).               \tag{8.2}
\]

Now fix one good parent cell \(C\), and write

\[
                         I_{C,q}^-={L_q(X):X\in C\}.           \tag{8.3}
\]

For \(q<H\), define

\[
 \partial_{C,q}^-(L_{q+1}(X))=L_q(X).                          \tag{8.4}
\]

This is well-defined because the depth-\((q+1)\) map is injective.  It is
injective because the depth-\(q\) map is injective.  Both image sets have
cardinality \(|C|=2^S\), so (8.4) is a bijection.  Moreover

\[
                         L_{q+1}(X)\subset L_q(X),
                         \qquad |L_q(X)\setminus L_{q+1}(X)|=1. \tag{8.5}
\]

The upper construction is dual, and (8.1) intertwines the two chains
under complementation.  This proves the exact all-depth laminar incidence
claimed in (0.9).

The quota level \(c_q\) does not occur in (8.4).  Therefore a
reset-aware clone assignment on the already established common run
vector may be pulled back through (8.4) without changing a physical edge
or a memory state.  This is a chronology statement, not a proof that the
physical target loads of distinct cells are balanced.

## 9. The first unresolved cut is cross-cell

Let \(\mathcal C\) be the good product cells and define

\[
                         I_{C,q}^\pm
 =\{L_q(X):X\in C\}
 \quad\hbox{or}\quad
   \{U_q(X):X\in C\}.                                         \tag{9.1}
\]

Theorem 7.2 gives

\[
                         |I_{C,q}^\pm|=|C|.                     \tag{9.2}
\]

Hence the factorial collision energy contains no diagonal cell term:

\[
 \sum_T\binom{\mu_q^\pm(T)}2
 =\sum_{C<D}|I_{C,q}^\pm\cap I_{D,q}^\pm|.                    \tag{9.3}
\]

Equation (8.1) identifies the lower energy with the upper energy after
pairing \(C\) with \(C^c\).  Thus there is one fused cross-cell problem,
not two independent signed problems.

If \(G=a_qN_q+r_q\), \(0\le r_q<N_q\), the integer-minimal collision
energy is

\[
                         N_q\binom{a_q}2+r_qa_q.                \tag{9.4}
\]

Indeed, if nonnegative integer loads \(d_1,\ldots,d_{N_q}\) have sum
\(G\), a transfer from a load at least two larger than another load
strictly decreases \(\sum_i\binom{d_i}{2}\).  Iteration ends precisely
at the multiset having \(N_q-r_q\) copies of \(a_q\) and \(r_q\) copies
of \(a_q+1\), proving (9.4).  The same transfer argument gives the
quantitative stability bound

\[
 \min_{\substack{b_i\in\{a_q,a_q+1\}\\ \sum_i b_i=G}}
       \sum_i|d_i-b_i|
 \le
 2\left(\sum_i\binom{d_i}{2}
       -N_q\binom{a_q}{2}-r_qa_q\right).             \tag{9.4a}
\]

Therefore one strong sufficient target theorem is

\[
 \sum_{q\le H}
 \left[
   \sum_{C<D}|I_{C,q}^-\cap I_{D,q}^-|
   -N_q\binom{a_q}2-r_qa_q
 \right]=o(W).                                                 \tag{9.5}
\]

By (9.4a), (9.5) gives aggregate floor/ceiling error \(o(W)\) for the
retained mass \(G\), and (8.2) supplies both signs.  Replacing the
\(G\)-quotas by the desired \(W\)-quotas costs at most \(W-G\) in
\(\ell^1\) at one depth.  Since \(W-G=o(W/H)\), this replacement costs
\(o(W)\) after summing through \(q\le H\).

Condition (9.5) is not the exact logical residual for the OR problem: it
also penalizes excessive positive multiplicities.  The exact one-sided
residual is obtained from the missing/repeat identity.  Put

\[
 R_q^-=
 \sum_T\bigl(\mu_q^-(T)-1\bigr)_+-(G-N_q)_+ .                 \tag{9.5a}
\]

Since the loads have total mass \(G\), the number \(M_q^-\) of missing
lower targets satisfies exactly

\[
 M_q^-=(N_q-G)_+ + R_q^- .                                    \tag{9.5b}
\]

Here \(G=W-o(W/H)\), and therefore

\[
 \sum_{q\le H}(N_q-G)_+=o(W).
\]

Consequently the weakest exact cross-cell theorem consumed by the final
transfer is

\[
 \boxed{\sum_{q\le H}R_q^-=o(W),}                             \tag{9.5c}
\]

equivalently, that the summed number of missing lower targets is
\(o(W)\).  Complementation then gives the same conclusion for the upper
targets.  The quadratic condition (9.5) implies (9.5c), but the converse
is false: a fully covering load vector may have a linear quadratic
excess.  Thus (9.5) remains a useful balanced-load route, while (9.5c)
is the actual constant-one gate.

No packet-local or parent-cell odd set can be the missing obstruction:
Sections 5--8 exhibit an integral owner factor whose local target
columns are exact laminar rainbows.  Thus any violated dual inequality
must involve at least two distinct parent cells.

What remains is genuinely cross-cell.  Uniform independent compiler
conjugates have bounded Gaussian mean per target and therefore leave a
positive target fraction uncovered; this is Theorem 3.1 of
MATH_AUDIT_DIVERSE_ORDER_COMPILER_CROSS_PACKET_COVARIANCE_20260726.md,
whose proof remains valid for the present larger \(R\), since
\(q/R=o(1)\).  A successful completion of (9.5) must correlate the
macroblock frames or compiler contexts across distinct cells.  This
obstruction is already present at the first Gaussian quota band; it does
not first appear at \(H=3\) or any later finite memory.

## 10. Verdict

After correcting the leave proof, the three structural conclusions have
the following exact status.

1. **Linear packet rank survives.**  The choice of \(R\) is independent
   of the macroblock census and still satisfies
   \[
                  {m\over128}<R\le {m\over64}.
   \]
   Consequently every cycle has length in
   \[
                  {m\over64}<2R\le {m\over32},
   \]
   and the total number of cycles is at most \(64W/m=o(W/H)\).
2. **Exponential owner leave survives.**  The aggregate Bernoulli census,
   followed only then by middle-rank conditioning, gives
   \[
                  0\le W-G\le e^{-m/16}W
   \]
   for all sufficiently large \(m\).  No fixed-rank-vector conditional
   binomial assertion or rank-vector union bound is used.
3. **The parent-cell rainbow remains exact.**  Its proof uses only
   \(S\ge16R\), the exact \(Q_{16}\) matching partition, and compiler
   injectivity through \(R/4-1\).  All three hold unchanged, so for every
   good parent cell \(C\), either sign, and every \(q\le H\), the literal
   image has exactly \(|C|\) elements.  More explicitly, a \(Q_S\) cell
   is partitioned into exactly \(2^{S-R}\) packets of size \(2^R\), with
   no rounding or packet leave.

The diverse-order recursion is an exact \(H\)-spacing controller at
linear packet dimension.  Combined with the complement-equivariant
balanced \(Q_{16}\) packet selector, it gives:

* cycle length \(\Theta(m)\);
* owner leave \(o(W/H)\);
* \(o(W/H)\) cycles;
* literal lower and upper injectivity through every \(q\le H\);
* exact signed-pair fusion; and
* bijective all-depth laminar incidence inside every product cell.

Thus no higher-memory stable odd cut reappears locally.  The sole
remaining coefficient-one inequality is the fused cross-cell collision
bound (9.5).  Proving it requires correlated dense mixing between parent
cells; neither bounded reset colours nor packet-local recursion can decide
that global covariance.
