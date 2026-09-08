# Overlap compression does not compose with profile Hall: an exact cross-profile cut and a frozen-parent packet-union no-go

Date: 2026-07-26

Method: pure mathematics only. No computation, solver, or web input is
used.

## 0. Verdict

The two proposed inputs are both correct but do **not** compose to give
arbitrary raw Hall.

* `MATH_THEOREM_TRANSVERSAL_AXIS_SELECTOR_AND_COMPILER_HALL_GATE_20260726.md`
  gives dispersed selected axes and Hall expansion for weights constant on
  the safe empirical profiles.
* `MATH_THEOREM_WITHIN_PROFILE_STATUS_COMPRESSION_AND_NONPROFILE_CUT_20260726.md`,
  strengthened in
  `MATH_THEOREM_QRE_WITHIN_PROFILE_COMPONENT_EXPANSION_20260726.md`, gives,
  after an exponentially small overlap-stratum quarantine, expansion by

  \[
                         K_q=\left({3\over2}\right)^q
  \tag{0.1}
  \]

  for **every** raw subfamily lying in one diffuse ordered profile.

There is nevertheless an exact abstract counterexample with empty
quarantine in which:

1. every subfamily of every target profile expands by a factor \(K\);
2. the capacitated profile quotient satisfies Hall exactly; but
3. a raw family mixing profiles has neighborhood only one half its size.

Thus the remaining maximal-graph statement is a genuine cross-profile
overlap theorem, not a formal consequence of the two cited results.

There is also a sharp obstruction to repairing an already chosen raw
injection after packetization. Let \(Q_S\) be an owner cell and let packets
have dimension \(R=o(S)\). In the relevant range

\[
 q=o(R),\qquad R\gg q\log(S/R),
\tag{0.2}
\]

there is a \(1-o(1)\)-spanning injective family of lower and upper
cell-labelled \(q\)-faces such that **every** tiling of \(Q_S\) by
coordinate \(Q_R\)'s retains only

\[
 (2+o(1)){\binom Rq\over\binom Sq}=o(1)
\tag{0.3}
\]

of its assigned incidences. The same statement survives deletion of any
fixed \(o(1)\)-density quarantine in the cell-face atlas. This attacks the
touched-axis union condition directly and shows that

\[
 \text{raw injection first}\quad\Longrightarrow\quad
 \text{coherent packet injection later}
\tag{0.4}
\]

is false even with a near-perfect raw injection.

The packet cut is allocation/cell-labelled. It does not by itself refute a
literal physical-target construction which forgets that label and reroutes
a target through a different product cell. It proves that such cross-cell
re-atlasing must occur **before** Hall selection. After a selected-axis
matching has been built directly, the touched-axis union condition is
automatic, but the one-whole-compiler-option condition remains the exact
packet configuration/covariance gate.

## 1. What the overlap quarantine actually gives

Fix a safe diffuse ordered lower profile \(\tau\). The strengthened
overlap-stratum theorem supplies a deleted family

\[
                  \mathcal E^-_\tau\subseteq\tau,
 \qquad
 { |\mathcal E^-_\tau|\over|\tau|}
       \le 2q e^{-cd},
\tag{1.1}
\]

such that every raw family
\(\mathcal A\subseteq\tau\setminus\mathcal E^-_\tau\) satisfies

\[
                  |N^-(\mathcal A)|\ge K_q|\mathcal A|.
\tag{1.2}
\]

The upper statement is identical. Summing (1.1) over the disjoint ordered
profiles gives a global deleted mass at most

\[
                         2q e^{-cd}N_q
\tag{1.3}
\]

inside the safe diffuse part. The unsafe or nondiffuse profiles contribute
\(o(N_q)\). For \(d=C\log m\), the first term in (1.3) is
\(m^{-cC+o(1)}N_q\). Hence the quarantine is indeed exponentially small in
\(d\), and it is negligible at the target scale after \(C\) is chosen
large enough.

The important quantifier in (1.2) is

\[
              \mathcal A\text{ lies in one fixed }\tau.
\tag{1.4}
\]

Nothing in the proof compares the middle-source components used by two
different profiles. The next theorem shows that this missing comparison
cannot be supplied by profile Hall alone.

## 2. Exact noncomposition theorem

### Theorem 2.1 (profile Hall plus arbitrary within-profile expansion can fail raw Hall by \(1/2\))

For every integer \(K\ge2\), there is a finite bipartite graph with target
profiles

\[
                         L_1,\ldots,L_{2K}
\tag{2.1}
\]

and a partition of the source shore into profile cells such that:

1. for every \(i\) and every \(\mathcal A\subseteq L_i\),

   \[
                         |N(\mathcal A)|=K|\mathcal A|;
   \tag{2.2}
   \]

2. the capacitated quotient on the whole profiles satisfies every Hall
   cut; but
3. there is a raw family \(\mathcal A\subseteq\bigcup_iL_i\) with

   \[
                         |N(\mathcal A)|={1\over2}|\mathcal A|.
   \tag{2.3}
   \]

The exceptional or quarantined family may be taken empty.

#### Proof

Put

\[
                         M=2(K-1),\qquad p=2K.
\tag{2.4}
\]

Let

\[
 L_i=\{(i,a):1\le a\le M\}\mathbin{\dot\cup}\{z_i\}
 \qquad(1\le i\le p).
\tag{2.5}
\]

The first \(M\) vertices are ordinary and \(z_i\) is a portal. On the
source shore take one common cell

\[
                         U=[M]\times[K],
 \qquad |U|=KM,
\tag{2.6}
\]

and pairwise disjoint private cells \(V_i\), each of size \(K\). Join
\((i,a)\) to the \(K\) vertices

\[
                         (a,1),\ldots,(a,K)\in U,
\tag{2.7}
\]

and join \(z_i\) to all of \(V_i\). There are no other edges.

Within one \(L_i\), the \(K\)-sets in (2.7), together with \(V_i\), are
pairwise disjoint. Therefore every \(\mathcal A\subseteq L_i\) has exactly
\(K|\mathcal A|\) neighbors. This proves (2.2).

At quotient level, a collection \(I\subseteq[p]\) of \(t\) complete
target profiles has demand \(t(M+1)\) and available source capacity

\[
                         |U|+\sum_{i\in I}|V_i|=KM+Kt.
\tag{2.8}
\]

Their difference is

\[
 KM+Kt-t(M+1)
   =M(K-t)+t(K-1)
   =(K-1)(2K-t)\ge0
\tag{2.9}
\]

for every \(0\le t\le2K\). These are all quotient cuts, so the
capacitated profile graph satisfies Hall. Equality holds at \(t=2K\).

Equivalently, if the weight on \(L_i\) is the constant \(c_i\ge0\), the
literal support-function inequality is

\[
 (M+1)\sum_i c_i
 \le KM\max_i c_i+K\sum_i c_i.
\tag{2.10}
\]

Indeed, the \(KM\) vertices of \(U\) each see the largest profile weight,
while the \(K\) vertices of \(V_i\) see \(c_i\). Since
\(\sum_i c_i\le2K\max_i c_i\) and \(M=2(K-1)\), (2.10) follows with
equality when all \(c_i\)'s are equal. Thus the example satisfies the full
weighted profile-constant dual, not merely its indicator special cases.

Now delete every portal and take

\[
                         \mathcal A=
 \{(i,a):1\le i\le2K,\ 1\le a\le M\}.
\tag{2.11}
\]

All its neighbors lie in the same common cell \(U\), and every vertex of
\(U\) occurs. Hence

\[
 |\mathcal A|=2KM,
 \qquad
 |N(\mathcal A)|=KM,
\tag{2.12}
\]

which proves (2.3). \(\square\)

### Corollary 2.2 (the proposed combination is not a proof of raw Hall)

Take \(K=\lfloor(3/2)^q\rfloor\). Even expansion of the strength furnished
by the good overlap strata, together with exact Hall on all unions of
whole profiles, leaves room for a positive-density raw cut. Therefore the
selected-axis profile theorem and the within-profile compression theorem
do not imply arbitrary block-labelled Hall by any black-box composition.

The example identifies the failure exactly: the ordinary parts of all
profiles use the same middle-source reservoir, while the portal vertices
alone certify the apparent quotient capacity.

## 3. The missing cross-profile inequality

Write an arbitrary target family as a disjoint union

\[
                         \mathcal A=\dot\bigcup_\tau\mathcal A_\tau.
\tag{3.1}
\]

On the good strata, overlap compression gives

\[
 \sum_\tau |N(\mathcal A_\tau)|
       \ge K_q\sum_\tau|\mathcal A_\tau|.
\tag{3.2}
\]

A sufficient cross-profile statement, sharp for this argument, is

\[
 \boxed{
 \sum_\tau |N(\mathcal A_\tau)|
       \le K_q\left|\bigcup_\tau N(\mathcal A_\tau)\right|
 \quad\text{for every family }(\mathcal A_\tau)_\tau.}
\tag{3.3}
\]

Equations (3.2)--(3.3) imply raw Hall immediately. In Theorem 2.1, for
the family (2.11), the left side of (3.3) is \(2K|U|\), whereas the right
side is \(K|U|\); the missing overlap bound fails by the exact factor two.

Condition (3.3) need not be the final way to prove the theorem, but some
equivalent arc-resolved capacity statement is necessary. One convenient
positive formulation is a supported kernel \(P(T,X)\ge0\) satisfying

\[
 \sum_{X\sim T}P(T,X)=1
 \quad\text{for every retained target }T,
 \qquad
 \sum_{T\sim X}P(T,X)\le1
 \quad\text{for every middle owner }X.
\tag{3.4}
\]

By bipartite-flow integrality, (3.4) yields a raw injection. The existing
profile flow fixes only the sums of (3.4) over entire profile cells. The
overlap theorem proves (3.2) separately in each row profile. Neither
controls the column sums after rows from different profiles are
superposed.

Thus the exact surviving maximal/raw gate is one of:

* prove (3.3) from the rank-dependent matching array;
* construct the source-normalized kernel (3.4); or
* exhibit an actual physical family realizing the common-reservoir
  mechanism of Theorem 2.1.

No one of these statements is present in the two input notes.

## 4. A direct touched-axis union obstruction

We now show that even a near-perfect raw injection cannot in general be
made packet coherent after it has been selected.

Represent one orientation cell by \(Q_S=\{0,1\}^S\). For
\(x\in Q_S\) and \(D\in\binom{[S]}q\), let

\[
                         F(x,D)=(D,x|_{[S]\setminus D})
\tag{4.1}
\]

be the abstract coordinate \(q\)-face through \(x\). In the Johnson
realization, \(F^-(x,D)\) empties the occupied endpoint in every axis of
\(D\), and \(F^+(x,D)\) fills the absent endpoint. For either sign,

\[
 F(x,D)=F(y,E)
 \quad\Longleftrightarrow\quad
 D=E\text{ and }x|_{[S]\setminus D}=y|_{[S]\setminus D}.
\tag{4.2}
\]

Put

\[
                         \alpha={\binom Rq\over\binom Sq}.
\tag{4.3}
\]

### Theorem 4.1 (universal post-hoc packet-union no-go in a frozen parent cell)

Assume

\[
 q\le R<S,\qquad {\binom Sq\over2^q}\longrightarrow\infty,
\tag{4.4}
\]

and

\[
 2^R\alpha\gg S+R\log(eS/R).
\tag{4.5}
\]

There are \(q\)-sets \(D_x\subseteq[S]\) and a set
\(X_0\subseteq Q_S\), with

\[
                         |X_0|=(1-o(1))2^S,
\tag{4.6}
\]

such that:

1. both maps \(x\mapsto F^-(x,D_x)\) and
   \(x\mapsto F^+(x,D_x)\) are injective on \(X_0\); and
2. for every partition of \(Q_S\) into coordinate \(Q_R\)-packets,

   \[
   \#\{x\in X_0:D_x\subseteq R(P_x)\}
          \le 2\alpha\,2^S,
   \tag{4.7}
   \]

   where \(P_x\) is the packet containing \(x\) and \(R(P_x)\) is its
   physical axis support.

The assertion is simultaneous over all packetizations, including a
packetization chosen after seeing the injection.

#### Proof

Choose the \(D_x\)'s independently and uniformly from
\(\binom{[S]}q\). Fix one coordinate \(Q_R\)-subcube \(P\), with support
\(R(P)\). Then

\[
 Z_P:=\#\{x\in P:D_x\subseteq R(P)\}
       \sim\operatorname{Bin}(2^R,\alpha).
\tag{4.8}
\]

Writing \(\mu=2^R\alpha\), the elementary Chernoff bound gives

\[
                         \Pr\{Z_P>2\mu\}\le e^{-\mu/3}.
\tag{4.9}
\]

There are exactly

\[
                         2^{S-R}\binom SR
\tag{4.10}
\]

coordinate \(Q_R\)-subcubes. By (4.5), the union bound over (4.10) is
\(o(1)\). Hence, with probability \(1-o(1)\), every such \(P\) satisfies

\[
                         Z_P\le2\alpha2^R.
\tag{4.11}
\]

Summing (4.11) over the packets of any tiling proves (4.7), before any
vertices are deleted.

It remains to make the face maps injective. For fixed distinct \(x,y\)
at Hamming distance \(h\), equality in (4.2) has probability zero for
\(h>q\), and for \(1\le h\le q\) it has probability

\[
 {\binom{S-h}{q-h}\over\binom Sq^2}.
\tag{4.12}
\]

Thus the expected number of ordered collisions from one fixed \(x\) is

\[
 \sum_{h=1}^q
 \binom Sh{\binom{S-h}{q-h}\over\binom Sq^2}
 = {1\over\binom Sq}\sum_{h=1}^q\binom qh
 = {2^q-1\over\binom Sq}=o(1).
\tag{4.13}
\]

Here we used

\[
                         \binom Sh\binom{S-h}{q-h}
                           =\binom Sq\binom qh.
\]

Therefore the expected total collision count is \(o(2^S)\). Choose a
realization satisfying both (4.11) and this collision bound, and delete
one domain vertex from every colliding pair. The remaining set \(X_0\)
satisfies (4.6), injectivity for both signs by the common criterion (4.2),
and still satisfies (4.7). \(\square\)

### Parameter audit

When \(q=o(R)\),

\[
 \log\alpha
   =q\log(R/S)+O(q^2/R+q^2/S).
\tag{4.14}
\]

Hence \(\alpha=o(1)\) whenever \(R=o(S)\) and
\(q\log(S/R)\to\infty\). Moreover (4.5) follows from

\[
                         R\gg q\log(S/R).
\tag{4.15}
\]

This includes both the earlier \(R=m^{3/5+o(1)}\), \(q=A\sqrt m\)
selector scale and the larger \(R\asymp\sqrt{mH}\) diverse-order scale,
provided \(H\ge A\sqrt m\). Thus (4.7) is \(o(2^S)\) in the intended
Gaussian window.

### Quarantine stability

Let \(\mathcal Q\) be any fixed family of deficient cell-labelled
\(q\)-faces of relative density \(\eta=o(1)\). A uniformly random incidence
\((x,D_x)\) produces a uniform \(q\)-face, because every \(q\)-face has
exactly \(2^q\) incident vertices. Hence

\[
 \mathbb E\#\{x:F(x,D_x)\in\mathcal Q\}=\eta2^S.
\tag{4.16}
\]

The realization in Theorem 4.1 may therefore also be chosen so that only
\(o(2^S)\) selected faces lie in \(\mathcal Q\). Deleting them preserves
(4.6)--(4.7).

There is one necessary qualification. Equation (1.3) says that the
deficient overlap strata have \(o(1)\) density in the physical target
layer. It does not automatically say that their pullback has \(o(1)\)
density in every frozen cell-face atlas, because one physical target can
have many allocation/cell labels. Thus (4.16) applies to the physical
quarantine only after this pullback-density condition is checked. The
empty-quarantine cross-profile counterexample of Theorem 2.1 is
unaffected; the qualification concerns only the attempt to identify its
abstract packet cut with one fixed physical parent cell.

## 5. Why (4.7) is exactly the touched-axis condition

Fix a tiling and a target face \(F(x,D_x)\). It has a selected-axis
neighbor if and only if

\[
                         D_x\subseteq R(P_x).
\tag{5.1}
\]

The forward implication deserves spelling out. Suppose a vertex \(y\) of
the face lies in a packet \(P_y\) and \(D_x\subseteq R(P_y)\). Since
\(P_y\) is a coordinate subcube, it then contains every vertex obtained
from \(y\) by changing coordinates in \(D_x\), including \(x\). The
packet tiling is vertex-disjoint, so \(P_y=P_x\). The reverse implication
is immediate.

Consequently Theorem 4.1 gives, for every post-hoc packetization, a
\(1-o(1)\)-density subfamily of the injective cell-labelled targets with
no selected-axis neighbor at all. This is stronger than the earlier
\(\lfloor R/q\rfloor+1\) disjoint-demand fragment: the obstruction is
near-spanning and simultaneous over every possible coordinate packet
tiling.

Equivalently, the necessary per-packet condition

\[
 \left|\bigcup_{x\in P\cap X_0}D_x\right|\le R
\tag{5.2}
\]

cannot be obtained by repartitioning a generic raw injection. In the
construction above, every packet support captures only an
\(O(\alpha)\)-fraction of the assigned demands.

The statement is also sign-coherent: the same \(D_x\) defines injective
lower and upper faces. Thus pairing the two signs does not remove the
cut.

## 6. What this does and does not refute

Theorem 4.1 is an exact no-go for an **allocation-labelled** or
cell-labelled proof which first assigns a target to one raw face and then
tries to choose packet supports. It also refutes any claim that the
within-profile injection supplied abstractly by Hall can automatically be
compiled.

It is not yet a literal physical-target Hall cut. After the allocation or
cell label is forgotten, the same physical lower target has many middle
extensions, possibly in different rank-twisted product cells. A successful
construction may reroute it through one of those other extensions. That
possibility is precisely the nonlocal cross-profile/cross-cell freedom
which is absent from Theorem 4.1.

Therefore the order of proof must be:

1. fix the owner packet factor and its selected supports;
2. quotient all alternative allocation labels of the same physical target;
3. prove Hall directly in that selected-axis literal-target graph; and
4. choose whole compiler configurations, rather than individual face
   incidences.

If Step 3 is achieved, then (5.2) is automatic: every chosen incidence
already has \(D(T,X)\subseteq R(P_X)\). There is no separate union theorem
left. But Step 4 is stronger. One legal compiler option \(g\) fixes the
entire map

\[
                         x\longmapsto
 (T^-_{P,g,q}(x),T^+_{P,g,q}(x))
\tag{6.1}
\]

inside a packet, simultaneously over the protected depths. Arbitrary
independent choices of \(D_x\subseteq R(P)\) need not be the windows of
one such \(g\).

## 7. Alignment with the authoritative CPCR target

The exact surviving target is CPCR from
MATH_EXACT_REMAINING_CROSS_PARENT_COMPILER_RESOLUTION_20260726.md, not a
common-order syndrome statement and not a within-packet gate. The
diverse-order theorem has already made every signed packet image
injective, and sibling packets in one parent have disjoint images.
Accordingly, every repeat counted below is cross-parent.

Let \(c=(\epsilon,q)\), let \(I_{P,c}^\omega\) be the injective literal
image of packet \(P\) under one legal whole compiler option \(\omega\),
and put

\[
                         v_{P,\omega}
   =\bigl(\mathbf1_{I_{P,c}^\omega}\bigr)_{c,T}.
\tag{7.1}
\]

A CPCR legal resolution state also includes the rank-dependent
matchings, dispersed selectors, and any chosen cross-parent
\(Q_{R+1}\)-slab trades before the final whole-packet columns (7.1) are
installed. For its integral loads \(L_c(T)\), set

\[
 \mathcal C_c(L)=\sum_T\binom{L_c(T)}2,
 \qquad
 \mathcal C_{c,\min}=N_q\binom{c_q}2+r_qc_q,
\tag{7.2}
\]

where \(G=c_qN_q+r_q\), \(0\le r_q<N_q\). Since
\(\sum_TL_c(T)=G\), direct expansion gives the exact identity

\[
 \boxed{
 \sum_T(L_c(T)-c_q)(L_c(T)-c_q-1)
   =2\bigl(\mathcal C_c(L)-\mathcal C_{c,\min}\bigr).}
\tag{7.3}
\]

Therefore CPCR is exactly the common all-depth, two-sign cross-parent
floor-covariance assertion

\[
 \sum_c\bigl(\mathcal C_c(L)-\mathcal C_{c,\min}\bigr)=o(W).
\tag{7.4}
\]

If the slab/selector choices are first frozen and
\(x_{P,\omega}\) is a distribution on the remaining legal whole-packet
options, its expected covariance is

\[
 \widetilde{\mathcal C}_c(x)
 =\sum_{P<Q}\sum_{\omega,\eta}
   x_{P,\omega}x_{Q,\eta}
   |I_{P,c}^{\omega}\cap I_{Q,c}^{\eta}|.
\tag{7.5}
\]

There is no diagonal term because packet images are injective. Thus

\[
 \sum_c\bigl(\widetilde{\mathcal C}_c(x)
                    -\mathcal C_{c,\min}\bigr)=o(W)
\tag{7.6}
\]

is the precise fractional certificate consumed by whole-packet
conditional expectation. If slab trades couple packets, the entire
coupled slab state must be treated as one choice group; no packet column
may be split depthwise.

The weaker product-hole condition

\[
 \sum_{c,T}\prod_P
 \left(1-\sum_\omega x_{P,\omega}
              \mathbf1_{\{T\in I_{P,c}^\omega\}}\right)=o(W)
\tag{7.7}
\]

would already suffice for coefficient one, but it is not the
authoritative CPCR statement. Equation (7.3) is the exact alignment:
CPCR is twice the excess factorial covariance above the balanced
floor/ceiling load vector.

Theorem 2.1 addresses CPCR's first explicitly open item: weighted
allocation of shared source-profile capacity is not a consequence of the
closed profile and within-profile gates. Theorem 4.1 addresses the order
of CPCR state selection: a frozen-parent raw injection cannot be
packetized afterward. It does **not** refute CPCR, because a CPCR state may
first apply cross-parent \(Q_{R+1}\)-slab trades and then reroute literal
targets across parent labels. Those slab derivatives, together with
compiler-image realizability and (7.4), are exactly the remaining global
work.

## 8. Certified boundary

Proved here:

1. the deficient overlap-stratum quarantine is globally negligible;
2. profile Hall plus arbitrary \(K\)-fold within-profile expansion does
   not imply raw Hall, even with \(K\to\infty\);
3. the exact missing maximal-graph input is cross-profile overlap control
   such as (3.3), or a source-normalized kernel such as (3.4);
4. a near-perfect raw two-sign face injection can lose \(1-o(1)\) of its
   incidences under every within-parent \(Q_R\) packetization; and
5. after supports are fixed first, touched-axis union is automatic, but
   whole-compiler coherence remains part of CPCR.

Not proved, and not implied by the two input notes:

1. arbitrary literal-target Hall after alternative cell/allocation labels
   are quotiented;
2. the cross-profile overlap inequality (3.3) for the rank-twisted array;
3. a legal whole-state distribution satisfying the CPCR covariance
   estimate (7.6); or
4. coefficient one.

The proposed black-box combination therefore fails at two logically
distinct places. Cross-profile source collision blocks the first Hall
lift, and a near-spanning touched-axis union obstruction blocks post-hoc
packetization inside a frozen parent. The surviving positive route is
exactly CPCR: choose the packet/slab re-atlas first, realize whole compiler
images, and drive the common all-depth cross-parent excess covariance
(7.4) to \(o(W)\).

## 9. \(L^1\) successor

MATH_THEOREM_L1_RECAST_CROSS_PROFILE_PACKET_UNION_AND_GROUPED_HALL_20260726.md
recasts both cuts for the weaker authoritative target

\[
 \mathfrak H=\sum_{q,\epsilon,T}(1-L_q^\epsilon(T))_+.
\]

Both cuts give linear holes in their original fixed incidence spaces, but
neither is invariant under legal cross-parent \(Q_{R+1}\)-slab trades.
Their surviving consequence is a dense-slab toll. The successor note
then gives the exact cross-parent grouped avoidance theorem and a
tensorable two-group counterexample: all natural grouped rank Hall cuts
and exact mean-one marginals hold, yet every integral state misses one
target per four. Thus the exact remaining target is grouped all-depth
near-cover/homing, not CPCR covariance.
