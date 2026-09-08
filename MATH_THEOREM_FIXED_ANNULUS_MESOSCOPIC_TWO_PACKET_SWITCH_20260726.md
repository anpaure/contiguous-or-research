# Fixed-annulus ordinary packets: an exact mesoscopic two-packet switch and the residual protected-deck matching gate

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web input
is used.

## 0. Outcome

Put

\[
n=2m,\qquad W=\binom{2m}{m},\qquad
q_0=\lceil a\sqrt m\rceil,\qquad H=\lfloor b\sqrt m\rfloor,
\tag{0.1}
\]

where \(0<a<b\) are fixed, and put

\[
k=m-q_0,\qquad N_q=\binom{2m}{m-q}.
\tag{0.2}
\]

The corrected packet mass is

\[
K={N_{q_0}\over 2m}+O(1)
 =\left(e^{-a^2}+o(1)\right){W\over2m}.
\tag{0.3}
\]

This note gives an explicit physical two-seed component at exactly that
scale. Each shore consists of two ordinary directed cyclic orders. The two
shores have identical multisets of middle intervals of length \(m\) and
first-annulus intervals of length \(k=m-q_0\). Thus switching a component
changes neither middle collision mass nor the depth-\(q_0\) lower or upper
ledger. At every later depth it changes literal target names. It is not a
whole-factor coordinate relabelling and is not the refuted one-seed heat
bath.

For a block width \(t\), the exact lower signed difference at depth
\(q_0+s\) has

\[
\boxed{\|d^-_{q_0+s}\|_1=4\min\{s,t-1\}.}
\tag{0.4}
\]

The upper difference is its complement and has the same norm. Hence one
component has exact two-sign annular variation

\[
\boxed{
\sum_{s=1}^{H-q_0}
\bigl(\|d^-_{q_0+s}\|_1+\|d^+_{q_0+s}\|_1\bigr)
=8\sum_{s=1}^{H-q_0}\min\{s,t-1\}.}
\tag{0.5}
\]

For \(t=c\sqrt m+O(1)\), with \(0<c<a\), this is
\(\Theta_{a,b,c}(m)\) per two-packet component. A family of
\(K/2+O(1)\) such components therefore has \(\Theta(W)\), rather than
\(o(W)\), total adjustable annular incidence. This is an explicit
protected-boundary switch at the corrected constant-density scale with
the raw \(\ell^1\)-capacity required for a linear aggregate repair. This
capacity statement does not itself orient the switches favorably.

There is also a sharp limitation. A width-\(t\) block switch can change
the aggregate two-sign hole count by at most

\[
4\sum_{s=1}^{H-q_0}\min\{s,t-1\}.
\tag{0.6}
\]

Consequently adjacent-transposition gadgets \((t=2)\), even if placed in
every packet pair, have total capacity

\[
O\left({W\over m}\sqrt m\right)=o(W).
\tag{0.7}
\]

They cannot solve the corrected fixed-annulus problem. Mesoscopic width
\(t=\Theta(\sqrt m)\) is necessary for a linear repair by this protected
two-packet mechanism.

The complete coordinate orbit of the new component has exactly the desired
fractional normalization: unit load on every rank-\(k\) target, middle
load \(N_{q_0}/W=e^{-a^2+o(1)}\), and depth-\(q\) load
\(N_{q_0}/N_q\). Thus the construction loses no scalar capacity.

After internal duplicates are collapsed, its protected-support orbit has
maximum nontrivial relative codegree

\[
O((t+1)/m^2)=O(m^{-3/2})=o(m^{-1})
\tag{0.7a}
\]

for \(t=O(\sqrt m)\). Middle complements are contracted; mixed
middle--tight codegrees are
\(\exp[-\Theta(\sqrt m\log m)]\). Hence the component grouping creates
no new \(m^{-1/2}\) pair obstruction.

At the tight rank, a sharper interval argument gives the width-independent
bound

\[
 {\Delta_2\over D}\le {5+o(1)\over m^2},
 \qquad
 \mathbb E(\text{additional overlap}\mid\text{one common target})
 =O(m^{-2}).
\tag{0.7b}
\]

What is not proved is the integral selection. The exact remaining object
is narrower than an ordinary packet near-factor: it is a matching of the
common protected decks of these two-shore components, followed by a signed
reserve orientation. Section 8 states this gate without any hidden
near-full-owner demand.

A generic residual-regeneration proof is impossible: for every balanced
coordinate cut there is an exactly point-balanced tight-target residual of
density \(1-\Theta(m^{-1/2})\) containing no protected component at all.
Thus any positive matching argument must construct and control its own
global resolution or its own admissible residual trajectory.

For completeness, the asymptotic used in (0.3) follows uniformly for
\(q=O(\sqrt m)\) from

\[
{N_q\over W}=\prod_{i=0}^{q-1}{m-i\over m+i+1},
\qquad
\log{N_q\over W}=-{q^2\over m}
+O\left({q\over m}+{q^3\over m^2}\right).
\tag{0.8}
\]

Indeed, expand \(\log(1-i/m)-\log(1+(i+1)/m)\) termwise and sum. Thus
\(N_{q_0}/W=e^{-a^2+O_{a}(m^{-1/2})}\). One may take
\(K=\lceil N_{q_0}/(2m)\rceil\); its rounding error creates fewer than
\(2m=o(W)\) extra occurrences.

## 1. Cyclic interval notation

For a directed cyclic order \(\omega\) on \([n]\), let

\[
\mathcal I_r(\omega)
=\{I_\omega(j,r):j\in\mathbb Z_n\}
\tag{1.1}
\]

be its multiset of length-\(r\) cyclic intervals. For \(0<r<n\), its
\(n\) members are distinct. We write \([A]\) for the basis vector of a
literal target \(A\), and

\[
\mathbf I_r(\omega)=\sum_{A\in\mathcal I_r(\omega)}[A].
\tag{1.2}
\]

The complement identity is

\[
\{A^c:A\in\mathcal I_r(\omega)\}
=\mathcal I_{n-r}(\omega).
\tag{1.3}
\]

Thus every lower identity automatically gives the corresponding upper
identity.

## 2. The block-change formula

Let \(E=(e_1,\ldots,e_t)\) be a consecutive block and let
\(P=(p_1,\ldots,p_N)\), where \(N=n-t\), be the exterior order. Regard
\(EP\) as a cyclic order. Put

\[
P_d^+=\{p_1,\ldots,p_d\},\qquad
P_d^-=\{p_{N-d+1},\ldots,p_N\}.
\tag{2.1}
\]

For another ordering \(F=(f_1,\ldots,f_t)\) of the same block labels,
write

\[
E_{\le j}=\{e_1,\ldots,e_j\},\qquad
E_{>j}=\{e_{j+1},\ldots,e_t\},
\tag{2.2}
\]

and similarly for \(F\).

### Lemma 2.1 (exact block-change boundary formula)

If \(t\le r\le n-t\), then

\[
\begin{aligned}
\mathbf I_r(FP)-\mathbf I_r(EP)
=\sum_{j=1}^{t-1}\bigl(&
[F_{\le j}\cup P^-_{r-j}]
-[E_{\le j}\cup P^-_{r-j}]\\
&+[F_{>j}\cup P^+_{r-t+j}]
-[E_{>j}\cup P^+_{r-t+j}]\bigr).
\tag{2.3}
\end{aligned}
\]

#### Proof

An \(r\)-interval is unchanged if it contains none or all of the block
\(E\). The intervals containing a proper part of \(E\) have one of two
forms. It either ends after the first \(j\) block entries and is
\(E_{\le j}\cup P^-_{r-j}\), or starts at the \((j+1)\)-st block entry
and is \(E_{>j}\cup P^+_{r-t+j}\). There is exactly one interval of each
form for every \(1\le j<t\). Replacing \(E\) by \(F\) proves (2.3).
\(\square\)

## 3. The protected two-packet component

Choose an integer

\[
2\le t<q_0,
\tag{3.1}
\]

and put \(u=k-t+1\). Let

\[
U=(e_1,e_2,\ldots,e_t),\qquad
V=(e_2,e_3,\ldots,e_t,e_1),
\tag{3.2}
\]

and let \(J\) reverse an ordered block. Start from an arbitrary exterior
order \(P=(p_1,\ldots,p_N)\) and write its reversal as

\[
Z=(z_1,\ldots,z_N)=(p_N,p_{N-1},\ldots,p_1).
\tag{3.3}
\]

Define

\[
Q=(z_2,z_3,\ldots,z_u,z_1,z_{u+1},\ldots,z_N).
\tag{3.4}
\]

Thus only the first \(u\) entries of the reversed exterior have been
rotated. The two shores are

\[
\mathcal A=\{UP,\;JVQ\},\qquad
\mathcal B=\{VP,\;JUQ\}.
\tag{3.5}
\]

They are literal pairs of ordinary directed cyclic orders. The exterior
context sets obey

\[
Q_d^-=P_d^+\qquad(0\le d\le m-1),
\tag{3.6}
\]

and

\[
Q_d^+=P_d^-\quad(d\ge u),
\tag{3.7}
\]

whereas, for \(1\le d<u\),

\[
Q_d^+=\{z_2,\ldots,z_{d+1}\}\neq
      \{z_1,\ldots,z_d\}=P_d^-.
\tag{3.8}
\]

Indeed, \(N-u=m+q_0-1\ge m-1\), so a suffix of length at most \(m-1\)
does not meet the rotated initial block, proving (3.6). Equations
(3.7)--(3.8) are immediate from (3.4).

### Theorem 3.1 (exact protected-deck equality)

The two shores have the same rank-\(m\) and rank-\(k\) interval
multisets:

\[
\boxed{
\mathbf I_m(UP)+\mathbf I_m(JVQ)
=\mathbf I_m(VP)+\mathbf I_m(JUQ),}
\tag{3.9}
\]

\[
\boxed{
\mathbf I_k(UP)+\mathbf I_k(JVQ)
=\mathbf I_k(VP)+\mathbf I_k(JUQ).}
\tag{3.10}
\]

The complementary rank-\((m+q_0)\) identity also holds.

#### Proof

Apply Lemma 2.1 to \(U\to V\) in the first packet and to
\(JV\to JU\) in the second. A prefix of \(JU\) of size \(j\) is the
suffix of \(U\) of size \(j\), while a suffix of \(JU\) of size \(j\)
is the prefix of \(U\) of size \(j\); the same holds for \(V\).

More explicitly, pair the index \(j\) in the first application with
the index \(t-j\) in the second.  The two post-block terms then have
the common block sections \(U_{>j},V_{>j}\) and exterior context size
\(r-t+j\); they cancel when
\(Q^-_{r-t+j}=P^+_{r-t+j}\).  The two pre-block terms have the common
block sections \(U_{\le j},V_{\le j}\) and exterior context size
\(r-j\); they cancel when \(Q^+_{r-j}=P^-_{r-j}\).  Thus there is no
unmentioned reversal of the exterior context in this pairing.

Consequently the first packet's suffix-boundary term at context size
\(d\) cancels the second packet's prefix-boundary term when
\(Q_d^-=P_d^+\). Its prefix-boundary term cancels the second packet's
suffix-boundary term when \(Q_d^+=P_d^-\).

At interval length \(r\), all context sizes which occur lie in
\([r-t+1,r-1]\). For \(r=k\), this interval begins at \(u\). For
\(r=m\), it begins at \(m-t+1>u\). Equations (3.6)--(3.7) therefore
give complete cancellation at both lengths. Complementation and (1.3)
give the upper identity. \(\square\)

## 4. Exact interior direction

For \(s\ge1\), put

\[
r_s=k-s,
\qquad
d_s^-=\mathbf I_{r_s}(\mathcal B)-\mathbf I_{r_s}(\mathcal A),
\tag{4.1}
\]

where the notation means the sum over the two packets in the shore. Assume
\(s\le H-q_0\); then \(r_s\gg t\), so Lemma 2.1 applies. For
\(1\le j<t\), put

\[
U_j=\{e_1,\ldots,e_j\},\qquad
V_j=\{e_2,\ldots,e_{j+1}\}.
\tag{4.2}
\]

### Theorem 4.1 (triangular mesoscopic direction)

Let

\[
J_s=\{j\in\{1,\ldots,t-1\}:j\ge t-s\}.
\tag{4.3}
\]

Then

\[
\boxed{
d_s^-
=\sum_{j\in J_s}\bigl(
[V_j\cup P^-_{r_s-j}]-[U_j\cup P^-_{r_s-j}]
+[U_j\cup Q^+_{r_s-j}]-[V_j\cup Q^+_{r_s-j}]
\bigr).}
\tag{4.4}
\]

All displayed targets in (4.4) are distinct. Therefore

\[
\boxed{|J_s|=\min\{s,t-1\},\qquad
       \|d_s^-\|_1=4\min\{s,t-1\}.}
\tag{4.5}
\]

The upper vector is the complement image of \(d_s^-\), and hence obeys
the same formula and norm.

#### Proof

The terms paired through (3.6) cancel at every relevant context size. The
other pair cancels precisely when \(r_s-j\ge u\). Since
\(r_s=k-s\) and \(u=k-t+1\), failure of cancellation is equivalent to
\(j\ge t-s\). This gives (4.4) and (4.3), whose cardinality is (4.5).

For the collision audit, the two exterior contexts in a fixed summand are
different by (3.8), and \(U_j\neq V_j\) by (3.2). Since the block and
exterior label sets are disjoint, the four unions in that summand are
distinct. Terms belonging to different \(j\)'s have different intersection
size with the block \(E\), so they too are distinct. Every coefficient is
therefore \(+1\) or \(-1\) on a different literal target. Complementation
is a bijection. \(\square\)

In particular, this component genuinely changes target masses at every
depth after \(q_0\). The protected identities are not consequences of a
common coordinate relabelling: the lower direction (4.4) is nonzero.

## 5. Simultaneous component legality

Suppose a selected packet family consists of fixed packets and two-packet
components \(C\), each of the form (3.5), with either shore chosen. No
disjointness between literal target supports of different components is
needed for the following statement.

### Theorem 5.1 (all-component protected invariance)

For every choice vector \(\varepsilon\in\{0,1\}^{\mathcal C}\):

1. the number of selected packets is unchanged;
2. the complete middle load vector is unchanged;
3. the complete depth-\(q_0\) lower load vector is unchanged; and
4. the complete depth-\(q_0\) upper load vector is unchanged.

Thus middle collision mass, missing middle owners, and both
depth-\(q_0\) hole counts are identical for all component choices.

#### Proof

Every component contributes two packets on either shore. Equations
(3.9)--(3.10) give equality of its protected load vectors before and after
switching. Sum these identities over components and add the fixed packets.
\(\square\)

This is exact physical integrality. It does not average over a connected
global relabelling component, and no fractional component choice is used.

The two packets inside one shore are not forced to have a linear protected
overlap. The following audit is important because a linear internal overlap
would make the component catalogue unusable.

### Lemma 5.2 (one-symbol relocation deck count)

Let \(\omega'\) be obtained from a directed cyclic order \(\omega\) by
moving one symbol across exactly \(d\) consecutive symbols, without
changing their order. If

\[
1\le d<\min\{r,n-r\},
\tag{5.1}
\]

then

\[
\bigl|\mathcal I_r(\omega)\cap\mathcal I_r(\omega')\bigr|=n-2d.
\tag{5.2}
\]

In particular, a relocation across \(d\) symbols deletes exactly \(2d\)
old \(r\)-intervals and creates exactly \(2d\) new ones.

#### Proof

Write the affected part as \(x,a_1,\ldots,a_d\) before the move and as
\(a_1,\ldots,a_d,x\) after it. An interval can change only if one of its
two boundary cuts separates \(x\) from a nonempty initial or terminal
part of \(a_1,\ldots,a_d\). For each \(1\le i\le d\), there is one old
interval whose left boundary has this property and one whose right boundary
has this property. These \(2d\) old intervals are distinct because
\(d<r\) and \(d<n-r\): neither an interval nor its complement can contain
both affected boundary arcs. The same enumeration after the move gives
\(2d\) new intervals.

No old interval on this list equals a new one. Indeed, intersect with the
\((d+1)\)-set \(\{x,a_1,\ldots,a_d\}\). At a left boundary the old and
new intersections are respectively an initial segment containing \(x\)
and one not containing \(x\); at a right boundary they are the
corresponding terminal segments. Equality between a left and right case
would force the interval or its complement to contain both boundary arcs,
again excluded by (5.1). All other \(n-2d\) intervals are unchanged.
This proves (5.2). \(\square\)

### Corollary 5.3 (sublinear internal protected collision)

For either shore of (3.5), and for \(r=k\) or \(r=m\), the two packet
decks have intersection at most

\[
\boxed{2q_0+4t-2.}
\tag{5.3}
\]

Thus a bank of \(K/2+O(1)\) components has total within-component
collision at most

\[
O\left(K(q_0+t)\right)=O_{a,b,c}(W/\sqrt m)=o(W)
\tag{5.4}
\]

when \(t=O(\sqrt m)\).

#### Proof

Reverse \(UP\). After a cyclic rotation it is \(JUZ\), and reversal does
not change any interval deck. Moving \(z_1\) across the next

\[
d=u-1=k-t
\tag{5.5}
\]

symbols changes \(JUZ\) into \(JUQ\). For \(r=k,m\), condition (5.1)
holds for all sufficiently large \(m\). Lemma 5.2 says that only
\(n-2d=2q_0+2t\) intervals of the original deck survive this move.

Changing \(JU\) to \(JV\) is a relocation of \(e_1\) across \(t-1\)
symbols. It can add at most \(2(t-1)\) members back to the intersection
with the original deck. Therefore

\[
|\mathcal I_r(UP)\cap\mathcal I_r(JVQ)|
\le 2q_0+2t+2(t-1),
\]

which is (5.3) for shore \(\mathcal A\). Starting instead from the reversal
\(JVZ\) of \(VP\) proves the same bound for shore \(\mathcal B\).
Summing over components and using \(K=\Theta(W/m)\) proves (5.4).
\(\square\)

## 6. Exact capacity and the adjacent-switch no-go

Let \(L=H-q_0\). For one component, Theorem 4.1 gives

\[
\sum_{s=1}^{L}
\bigl(\|d_s^-\|_1+\|d_s^+\|_1\bigr)
=8S(L,t),
\tag{6.1}
\]

where

\[
S(L,t)=\sum_{s=1}^{L}\min\{s,t-1\}
=
\begin{cases}
L(L+1)/2,&L<t,\\[3pt]
(t-1)(L+1-t/2),&L\ge t-1.
\end{cases}
\tag{6.2}
\]

At a fixed signed depth, there are
\(2\min\{s,t-1\}\) positive and the same number of negative cells.
Changing the shore can therefore alter the hole count by at most
\(2\min\{s,t-1\}\). Summing both signs gives (0.6).

If all \(K\) packets lie in two-packet components, there are at most
\(K/2\) switches. Their total possible change in aggregate two-sign hole
count is at most

\[
2K S(L,t).
\tag{6.3}
\]

For \(t=2\), this is

\[
2KL=O_{a,b}(W/\sqrt m)=o(W).
\tag{6.4}
\]

Thus a bank of adjacent swaps is statewise incapable of repairing a linear
aggregate residual. For

\[
t=c\sqrt m+O(1),\qquad0<c<a,
\tag{6.5}
\]

and \(L=(b-a)\sqrt m+O(1)\), (6.2)--(6.3) are instead \(\Theta(W)\).
This proves the mesoscopic threshold claimed in Section 0.

The capacity is aggregate, not rankwise.  At one fixed offset \(s\), all
\(K/2+O(1)\) switches together can change the two-sign hole count by at
most

\[
 2K\min\{s,t-1\}
 \le 2Kt
 =O_{a,b,c}(W/\sqrt m)=o(W)
\tag{6.5a}
\]

when \(t=O(\sqrt m)\).  Consequently this component bank cannot repair a
linear hole fraction at even one protected depth.  A viable protected-deck
matching must already leave \(o(W)\) holes rankwise and at most
\(O(W)\) total annular residual; the mesoscopic orientations can only
remove that last aggregate-scale error.  In particular they cannot turn
the independently sampled seed in Section 4 of
MATH_THEOREM_FIXED_ANNULUS_PARTIAL_CYCLIC_PACKET_LEDGERS_AND_UNGROUPED_HALL_20260726.md,
which has \(\Theta(W)\) holes at each typical depth, into a solution.

More generally, for a bank of the components constructed in Section 3,
with possibly different widths \(t_C\), Theorem 4.1 gives

\[
\bigl|\mathfrak H(\varepsilon)-\mathfrak H(0)\bigr|
\le4L\sum_C(t_C-1),
\tag{6.6}
\]

for the aggregate two-sign hole count \(\mathfrak H\). Therefore changing
an \(\epsilon W\) residual requires

\[
\sum_C(t_C-1)\ge{\epsilon W\over4L}
=\Omega_{a,b,\epsilon}(W/\sqrt m).
\tag{6.7}
\]

At the corrected packet mass this is an average width
\(\Omega(\sqrt m)\) per packet pair. This is an exact statewise capacity
condition, not a variance estimate.

There is a corresponding sharp seed restriction.

### Corollary 6.2 (diffuse seeds cannot be repaired by the protected atlas)

For every bank of Section 3 components with \(t_C<q_0\) and at most
\(K/2+O(1)\) components,

\[
\sup_{\varepsilon}
|\mathfrak H(\varepsilon)-\mathfrak H(0)|
\le 2KLq_0+O(m^{3/2})=O_{a,b}(W).
\tag{6.8}
\]

Moreover the middle collision mass is exactly invariant. Therefore a seed
with \(\Theta(W)\) middle collision or
\(\Theta(W\sqrt m)\) aggregate annular holes cannot be repaired by any
choice of these component shores. In particular, the independently sampled
packet seed is rigorously excluded.

#### Proof

The middle statement is Theorem 5.1. For the annular statement, use
(6.6), \(t_C-1<q_0\), and
\(|\mathcal C|\le K/2+O(1)\). Since
\(K=\Theta(W/m)\) and \(Lq_0=\Theta_{a,b}(m)\), the right side is
\(O(W)\). The diffuse scales are the exact occupancy scales

\[
\mathbb EC_{\rm mid}=\Theta_a(W),\qquad
\mathbb E\mathfrak H=\Theta_{a,b}(W\sqrt m),
\]

so subtracting an \(O(W)\) possible change leaves the latter scale
unchanged, while the former is invariant. \(\square\)

Thus the new atlas is a final linear-residual corrector, not a mechanism
for manufacturing the common protected base from a Poisson seed. A
successful two-stage proof must first construct a protected-deck matching
with middle collision \(o(W)\) and aggregate holes \(O(W)\), and only then
use mesoscopic shores to seek the last \(o(W)\) improvement.

## 7. Exact fractional normalization of the component orbit

Retain all labels in the coordinate-conjugacy orbit of one component
(3.5). Every component has \(2n\) interval occurrences at each fixed rank,
on either shore. Give every labelled orbit member a common weight so that
the total component mass is

\[
{N_{q_0}\over2n}.
\tag{7.1}
\]

Coordinate transitivity then gives, on either shore,

\[
\text{rank-}k\text{ load}
={(N_{q_0}/2n)(2n)\over N_{q_0}}=1,
\tag{7.2}
\]

\[
\text{middle load}
={(N_{q_0}/2n)(2n)\over W}
={N_{q_0}\over W}=e^{-a^2+o(1)},
\tag{7.3}
\]

and, for every \(q_0\le q\le H\),

\[
\text{rank-}(m-q)\text{ load}
={N_{q_0}\over N_q}.
\tag{7.4}
\]

The upper load is identical. The total packet mass is twice (7.1), namely
\(N_{q_0}/n\), exactly the corrected value (0.3). Hence pairing packets
into protected two-shore components creates no fractional loss and no
extra middle-owner demand.

## 7.1 Protected-support degrees and codegrees

The preceding normalization used occurrences. We now collapse internal
duplicates and audit the actual protected-support hypergraph.

For \(r=k,m\), let \(\mathcal R_r\) be the distinct support of the common
two-packet \(r\)-deck, and put \(\rho_r=|\mathcal R_r|\). Corollary 5.3
gives

\[
2n-(2q_0+4t-2)\le\rho_r\le2n.
\tag{7.5}
\]

At the middle rank, every support is complement-invariant. We therefore
contract \(X\) and \(X^c\) to one atom \([X]\), and write
\(\overline{\mathcal R}_m\) for the resulting support. Then

\[
|\overline{\mathcal R}_m|=\rho_m/2.
\tag{7.6}
\]

This contraction is essential: without it, the pair \(X,X^c\) has
relative codegree one in every cyclic-order catalogue. It is harmless for
middle collision, because a packet contains \(X\) if and only if it
contains \(X^c\).

Both the middle vertex count and the template support size are divided by
two, so the labelled degree after contraction is still
\(n!\rho_m/W\), the value given by (7.7). A codegree of two distinct
complement atoms is the sum of the corresponding mask-pair codegrees in
the merged distance strata \(j\) and \(m-j\). This changes only an
absolute factor and is included in the bounds below.

Retain every \(g\in S_n\) as a label and form the orbit hypergraph whose
rank-\(r\) edge is \(g\mathcal R_r\). It is regular, of degree

\[
D_r^{\rm comp}={n!\rho_r\over N_r}.
\tag{7.7}
\]

For \(0<j\le r\), let \(A_{r,j}\) be the number of ordered pairs
\((S,T)\) of distinct members of \(\mathcal R_r\) at Johnson distance
\(j\). Orbit--stabilizer gives the exact normalized codegree

\[
\boxed{
{\lambda_{r,j}^{\rm comp}\over D_r^{\rm comp}}
={A_{r,j}\over
 \rho_r\binom rj\binom{n-r}j}.}
\tag{7.8}
\]

Indeed, the orbit of an ordered distance-\(j\) pair has size
\(N_r\binom rj\binom{n-r}j\). Double-counting labelled template pairs
proves (7.8).

We next control the only potentially dangerous stratum, \(j=1\).

### Lemma 7.1 (cross adjacency under a relocation)

If two coordinate cycles differ by moving one symbol across an arbitrary
number of consecutive symbols, then, at every fixed interval length \(r\),
the number of ordered cross pairs \((S,T)\), one interval from each cycle,
with \(|S\setminus T|=|T\setminus S|=1\), is at most \(8n\).

#### Proof

Delete the moved symbol \(x\). The two cycles become the same
\((n-1)\)-cycle. Split cross pairs according to membership of \(x\).

* If neither set contains \(x\), both are \(r\)-intervals of the common
  cycle. There are at most \(2(n-1)\) ordered adjacent pairs.
* If both contain \(x\), deleting \(x\) gives two
  \((r-1)\)-intervals of the common cycle at Johnson distance one. Again
  there are at most \(2(n-1)\) ordered pairs.
* If \(x\in S\setminus T\), then \(T\) contains the
  \((r-1)\)-interval \(S\setminus\{x\}\). It has at most two
  \(r\)-interval extensions in the common cycle. There are at most \(r\)
  choices of \(S\), giving at most \(2r\) pairs.
* The case \(x\in T\setminus S\) gives another \(2r\).

The sum is at most \(4(n-1)+4r<8n\). \(\square\)

### Theorem 7.2 (protected component codegree)

Uniformly for \(r=k,m\),

\[
A_{r,1}\le20n+8(t-1)r.
\tag{7.9}
\]

Consequently, if \(t=O(\sqrt m)\),

\[
\boxed{
\max_{S\ne T,\ T\ne S^c}
{\operatorname {codeg}(S,T)\over D_r^{\rm comp}}
=O\left({t+1\over m^2}\right)
=O(m^{-3/2})=o(m^{-1}).}
\tag{7.10}
\]

At the middle rank (7.10) is read after complementary contraction.

#### Proof

Inside either packet there are exactly \(2n\) ordered distance-one pairs,
so the two within-packet contributions total \(4n\).

As in Corollary 5.3, compare \(UP\) with \(JVQ\). The latter is obtained
from the reversal of the former by one long relocation, followed by moving
\(e_1\) across \(t-1\) symbols. Lemma 7.1 bounds cross adjacencies before
the second move by \(8n\). That second move creates at most \(2(t-1)\)
new interval targets. For a fixed new target \(T\), at most \(2r\)
members \(S\) of the first packet can satisfy \(|S\setminus T|=1\): for
each of the \(r\) possible sets \(T\setminus\{x\}\), there are at most
two interval extensions in a fixed coordinate cycle. Thus one ordered
cross direction has at most

\[
8n+4(t-1)r
\]

pairs. Doubling the direction and adding the within-packet pairs proves
(7.9). Collapsing common vertices cannot increase \(A_{r,1}\).

Now use (7.5), (7.8), and
\(r(n-r)=\Theta(m^2)\). This proves (7.10) at distance one. For
\(r=k<m\) and \(2\le j<r\), the crude bound
\(A_{r,j}\le\rho_r^2=O(m^2)\) and unimodality of
\(\binom rj\binom{n-r}j\) give

\[
{\lambda_{r,j}^{\rm comp}\over D_r^{\rm comp}}
=O(m^{-3}),
\tag{7.11}
\]

the worst case being \(j=2\); the disjoint endpoint is exponentially
smaller in the Gaussian regime.

At the middle rank, complementary contraction identifies the strata
\(j\) and \(m-j\). The stratum \(j=m-1\) is therefore the same atom-pair
stratum as \(j=1\) and obeys (7.10); strata with
\(2\le\min\{j,m-j\}\) obey (7.11). The endpoint \(j=m\) is the same
complement atom and is not a nontrivial codegree. This completes the
middle-rank audit.
\(\square\)

Here is the exact factor-two check behind that contraction.  If
\(j<m/2\), each ordered pair of distinct complement atoms at distance
\(j\) lifts to exactly two ordered set-pairs at distance \(j\), while
the component edge size and the ambient vertex count are both halved.
Hence the ratio in (7.8) is unchanged.  If \(m\) is even and
\(j=m/2\), an atom-pair lifts to four set-pairs, whereas the number of
distance-\(m/2\) neighboring atoms is half the number of neighboring
sets; the same cancellation again leaves (7.8) unchanged.  Thus no
factor two is lost in reading (7.10) after contraction.

The mixed protected codegrees are smaller still. Fix
\(T\in\binom{[n]}k\). The number of middle masks \(X\) with a prescribed
value of \(|X\cap T|\) is

\[
\binom{k}{h}\binom{n-k}{m-h}.
\tag{7.12}
\]

This log-concave sequence is minimized at an endpoint, where it is
\(\binom{m+q_0}{q_0}\). Since a component contains only \(O(m^2)\)
ordered tight--middle pairs, orbit double counting gives

\[
\boxed{
\max_{T,[X]}
{\operatorname {codeg}(T,[X])
 \over\min\{D_k^{\rm comp},D_m^{\rm comp}\}}
\le {O(m)\over\binom{m+q_0}{q_0}}
=\exp[-\Theta_a(\sqrt m\log m)].}
\tag{7.13}
\]

The same estimate follows when conditioning from the middle rank, using
\(\binom m{q_0}\). Thus the protected component support has no
\(m^{-1/2}\) codegree relation. Its largest nontrivial relative codegree
is the \(O(m^{-3/2})\) same-rank distance-one stratum.

The last displayed bound is valid but not sharp at the tight rank.  The
following interval observation removes its artificial dependence on
\(t\).

### Corollary 7.3 (sharp tight-rank pair geometry)

Let \(r=k<m=n/2\), and let \(\mathcal R_r\) be the union of the two
rank-\(r\) cyclic decks in either protected shore.  Then

\[
 \boxed{
 \max_{S\ne T}{\operatorname {codeg}(S,T)\over D_r^{\rm comp}}
 \le {5+o(1)\over r(n-r)}={5+o(1)\over m^2}.}
\tag{7.14}
\]

Moreover, if two independently labelled orbit components are conditioned
to contain the same tight target, their expected number of further common
tight targets is \(O(m^{-2})\).

#### Proof

Fix an \(r\)-set \(S\) and a cyclic order \(\tau\).  At most three
members of \(\mathcal I_r(\tau)\) are Johnson-adjacent to \(S\).
Indeed, any two such intervals have Johnson distance at most two through
\(S\).  Two proper cyclic \(r\)-intervals, with \(r<n/2\), have Johnson
distance equal to the shorter distance between their starts whenever that
distance is at most \(r\), and are disjoint when it is larger than \(r\).
Thus all relevant starts lie pairwise within circular distance two, and
there are at most three of them.

Each of the two decks has exactly \(2n\) ordered adjacent pairs.  The two
cross directions have at most \(3n\) ordered pairs each.  Hence the whole
template has at most \(10n\) ordered distance-one pairs.  Since
\(\rho_r=(2-o(1))n\), the exact orbit formula (7.8) gives

\[
 {10n\over\rho_r r(n-r)}
 ={5+o(1)\over r(n-r)},
\]

which proves (7.14).  For the second assertion, let \(g_j\) be the
average number of other template targets at Johnson distance \(j\) from
a template target.  Conditional orbit counting gives the exact expectation

\[
 \sum_{j=1}^{r}{g_j^2\over
   \binom rj\binom{n-r}j}.
\tag{7.15}
\]

Here \(g_1\le5+o(1)\), while \(g_j\le\rho_r=O(m)\) for \(j\ge2\).
The \(j=1\) term is \(O(m^{-2})\); the \(j=2\) denominator is
\(\Theta(m^4)\), so its term is \(O(m^{-2})\).  For \(3\le j\le r\),
log-concavity shows that the minimum of
\(\binom rj\binom{n-r}j\) occurs at one of the two endpoints.  The
\(j=3\) endpoint is \(\Theta(m^6)\), whereas the \(j=r\) endpoint is
\(\binom{m+q_0}{2q_0}=\exp(\Theta(\sqrt m\log m))\).
Consequently all \(O(m)\) remaining terms sum to \(O(m^{-3})\).
This proves (7.15) is \(O(m^{-2})\). \(\square\)

Thus even the full conditioned two-block overlap moment is below the
critical \(m^{-1}\) scale.  This strengthens the time-zero audit but does
not provide hereditary residual regeneration.

There is, in fact, an exact reason that regeneration cannot be demanded
for every dense balanced residual.

### Theorem 7.4 (dense packet-free residual for the protected orbit)

Fix a balanced coordinate bipartition \([n]=B\dot\cup B^c\),
\(|B|=m\), and put

\[
 \mathcal C_B=
 \left\{A\in\binom{[n]}k:
       \bigl|2|A\cap B|-k\bigr|\le1\right\},
 \qquad
 \mathcal U_B=\binom{[n]}k\setminus\mathcal C_B.
\tag{7.16}
\]

Every ordinary cyclic packet, and hence every protected two-packet
component, meets \(\mathcal C_B\).  Therefore the protected component
hypergraph induced by \(\mathcal U_B\) has no edge.  Nevertheless

\[
 { |\mathcal C_B|\over N_{q_0}}=
 \begin{cases}
 (2+o(1))/\sqrt{\pi m},&k\text{ even},\\[2mm]
 (4+o(1))/\sqrt{\pi m},&k\text{ odd},
 \end{cases}
\tag{7.17}
\]

so \(\mathcal U_B\) has density \(1-\Theta(m^{-1/2})\).  Both
\(\mathcal C_B\) and \(\mathcal U_B\) have exactly constant coordinate
degrees.

#### Proof

For a cyclic order \(\pi\), let

\[
 f_j=|I_\pi(j,k)\cap B|.
\]

Every member of \(B\) lies in exactly \(k\) of the \(n=2m\) cyclic
windows, so \(n^{-1}\sum_jf_j=k/2\), while
\(|f_{j+1}-f_j|\le1\).  The cyclic integer walk therefore assumes
\(k/2\) when \(k\) is even, or one of the two nearest integers when
\(k\) is odd.  This proves every packet meets \(\mathcal C_B\), and the
component assertion follows because each shore consists of packets.

Direct counting gives

\[
 |\mathcal C_B|=
 \begin{cases}
 \binom m{k/2}^{\!2},&k\text{ even},\\[2mm]
 2\binom m{(k-1)/2}\binom m{(k+1)/2},&k\text{ odd}.
 \end{cases}
\tag{7.18}
\]

The local central limit estimate for the hypergeometric variable
\(|A\cap B|\), whose variance is
\(k(2m-k)/(4(2m-1))=m/8+O_a(1)\), gives (7.17); equivalently it follows
directly from Stirling's formula in (7.18).  Finally, permutations within
\(B\) and \(B^c\), together with the interchange of the two halves, act
transitively on coordinates and preserve both families, proving exact
point balance. \(\square\)

Thus neither density \(1-o(1)\), exact point margins, the sharp
pair-codegree (7.14), nor the conditioned overlap bound (7.15) can imply
hereditary packet regeneration.  A positive matching proof must control
the actual trajectory or construct a global resolution; it cannot quantify
over all residuals of the indicated density.

This improves the pairwise geometry but does not by itself prove a
near-perfect protected-deck matching: the component edge size is
\(\Theta(m)\), and a hereditary residual-regeneration theorem is still
required. In particular, no fixed-uniformity nibble theorem is being
diagonalized here.

### 7.5 Why \(R\Delta_2/D=o(1)\) is not yet a matching proof

Let \(R=\Theta(m)\) be the protected component edge size and let
\(\delta=\Delta_2/D\). Equation (7.10) gives

\[
R\delta=O(m^{-1/2})=o(1).
\tag{7.19}
\]

Here the displayed bound uses the already proved uniform protected bound
(7.10); the tight-rank contribution is sharper by (7.14).  It is tempting
to quote (7.19) as a diagonal near-matching theorem. That
step is not currently justified. The same formal condition already holds
for the original tight packet hypergraph, where

\[
R=2m,\qquad \delta=(2+o(1))m^{-2},\qquad
R\delta=O(m^{-1}),
\tag{7.20}
\]

but its near-perfect matching is precisely the open Gaussian-rank tight
Hamilton decomposition gate. Thus any claimed general lemma based only on
\(R\delta=o(1)\) would also solve that pre-existing gate and requires a
new proof, not an invocation of the fixed-uniformity nibble.

The exact logical gap is hereditary. A time-zero isolated bite covers a
\(\Theta(1/R)\) fraction of the remaining targets. Reaching residual
density \(\eta\) takes \(\Theta(R\log(1/\eta))\) regenerated bites.
The first assertion is elementary: mark each edge with probability
\(1/(2RD)\) and retain it only if no intersecting edge is marked. An edge
meets at most \(RD\) labelled edges, so, conditional on being marked, it
survives with probability at least \(1/2\) by the union bound. Retained
edges through one vertex are mutually exclusive, and hence that vertex is
covered with probability at least \(1/(4R)\). Averaging gives one such
matching bite.
Global regularity and (7.19) do not say that an arbitrary matching residual
contains a nearly regular spanning subcatalogue; its surviving degree may
concentrate on the very interval threads exposed by the consecutive
codegrees. Pair codegree is monotone under deletion, but the normalized
ratio can inflate when residual degrees fall.

Theorem 7.4 shows that no antecedent quantified over **every** dense
point-balanced residual can hold.  A sufficient trajectory-specific
statement is instead the following:

> For some \(\eta_m=o(1)\) with
> \(R\delta/\eta_m=o(1)\), there is a sequence of isolated matching bites
> whose own residuals, until density \(\eta_m\), each contain a spanning
> subcatalogue with degrees \((1+o(1))D_U\) and maximum codegree
> \(O((\delta/\eta_m)D_U)\), uniformly along that sequence.

For example \(\eta_m=m^{-1/4}\) is compatible with (7.19). Iterating the
isolated bite under this antecedent leaves at most
\(m^{-1/4}\) of the protected vertices. The antecedent is not proved here.
It is one precise sufficient route by which the favorable codegree can be
converted into the protected-deck matching of Section 8.  A direct global
resolution or absorption theorem could bypass residual regeneration
entirely.

## 8. The exact remaining integral gate

For a component \(C\), define its common protected resource multiset

\[
R(C)=\bigl(\mathbf I_m(C),\mathbf I_k(C)\bigr),
\tag{8.1}
\]

which is independent of its shore by Theorem 3.1. Let
\(d_{C,q}^{\pm}\) be its signed interior direction.

The construction reduces the corrected fixed-annulus problem to the
following two assertions.

First, support-disjointness already has the correct quantitative output.

### Proposition 8.0 (a full component matching gives the protected base)

Let

\[
C_m=\left\lfloor{1\over2}
       \left\lfloor{N_{q_0}\over2m}\right\rfloor\right\rfloor.
\tag{8.1a}
\]

Suppose \(C_m\) coordinate-orbit components have pairwise disjoint
rank-\(k\) supports and pairwise disjoint middle complement-atom supports.
Select either common shore in every component. Then

\[
h_{q_0}=O_{a,c}(W/\sqrt m),
\qquad
C_{\rm mid}=O_{a,c}(W/\sqrt m).
\tag{8.1b}
\]

#### Proof

The two packets in a component contribute \(4m\) occurrences at either
protected mask rank. By Corollary 5.3, at most
\(2q_0+4t-2=O(\sqrt m)\) of those occurrences are internal repeats.
There are no repeats between components by hypothesis. Therefore the
selected tight support has size at least

\[
4mC_m-C_m(2q_0+4t-2)
=N_{q_0}-O(m)-O(W/\sqrt m).
\]

This proves the tight hole bound. The identical calculation at the middle
mask rank gives the collision bound; disjoint complement atoms are
equivalent to disjoint complement-closed mask supports. \(\square\)

Thus the first gate below can be stated simply as a matching of cardinality
\(C_m\) in the two-layer protected-support hypergraph. Its edge size is
\(\Theta(m)\), and Sections 7.1--7.5 give its exact pairwise and residual
boundary.

### Protected-deck component matching

Find the \(C_m\)-edge matching of Proposition 8.0 in the common
rank-\(k\) plus middle-complement resource hypergraph. More generally, it
is enough to choose

\[
{N_{q_0}\over4m}+O(1)
\tag{8.2}
\]

components whose cross-component protected overlap is \(o(W)\). Notice
that their middle union is allowed
to omit

\[
W-N_{q_0}+o(W)=\bigl(1-e^{-a^2}+o(1)\bigr)W
\tag{8.3}
\]

owners. Those owners are repaired singly; no near-full wreath factor is
being requested.

### Signed reserve orientation

For the selected components, choose
\(\varepsilon_C\in\{0,1\}\) so that, with the fixed protected loads,

\[
\sum_{q=q_0+1}^{H}
\bigl(h_q^-(\varepsilon)+h_q^+(\varepsilon)\bigr)=o(W),
\tag{8.4}
\]

where the exact load is

\[
\mu_q^{\pm}(\varepsilon)
=\mu_q^{\pm}(0)+\sum_C\varepsilon_Cd_{C,q}^{\pm}.
\tag{8.5}
\]

Equations (4.4)--(4.5) make every column of this signed system explicit.
In particular, its positive and negative cells are literal targets, not
profile or orbit tags.

There is a convenient exact reserve form of (8.4). For a base-shore load
\(\mu^0_\alpha\), where \(\alpha\) ranges over all signed annular target
cells, write

\[
P_C=\{\alpha:d_C(\alpha)=1\},\qquad
M_C=\{\alpha:d_C(\alpha)=-1\}.
\tag{8.5a}
\]

Then a set \(\mathcal S\) of components may be switched without leaving
any hole precisely when

\[
\boxed{
\mu^0_\alpha
+|\{C\in\mathcal S:\alpha\in P_C\}|
-|\{C\in\mathcal S:\alpha\in M_C\}|\ge1
\quad\text{for every }\alpha.}
\tag{8.5b}
\]

In particular, it is sufficient that every base hole is in a positive
cell of a selected component and in no selected negative cell, while each
nonhole \(\alpha\) is used negatively at most

\[
\mu^0_\alpha-1+|\{C\in\mathcal S:\alpha\in P_C\}|
\tag{8.5c}
\]

times. This is the exact signed-reserve matching condition: negative
collateral targets are charged to literal multiplicity above one, not to
an averaged Gram gain. Allowing an exceptional set of \(o(W)\) cells in
(8.5b) is equivalent to (8.4).

The fractional orientation obstruction has an exact dual.

### Theorem 8.1 (signed-reserve Farkas dual)

Let \(\mathcal A\) be the set of signed target-depth cells with
\(q_0<q\le H\) (the depths on which the components act), and let
\(d_C\in\mathbb R^{\mathcal A}\) be the component columns. There is a
fractional shore vector \(x\in[0,1]^{\mathcal C}\) satisfying

\[
\mu^0+\sum_Cx_Cd_C\ge\mathbf1
\tag{8.5d}
\]

coordinatewise if and only if, for every nonnegative weight
\(w\in\mathbb R_+^{\mathcal A}\),

\[
\boxed{
\sum_C\max\{0,\langle w,d_C\rangle\}
\ge\langle w,\mathbf1-\mu^0\rangle.}
\tag{8.5e}
\]

#### Proof

The set

\[
Z=\left\{\sum_Cx_Cd_C:0\le x_C\le1\right\}
\]

is a compact zonotope. Condition (8.5d) says that
\(Z\) meets \(\mathbf1-\mu^0+\mathbb R_+^{\mathcal A}\). If the two
convex sets are disjoint, separation supplies a normal \(w\ge0\) for
which

\[
\sup_{z\in Z}\langle w,z\rangle
<\langle w,\mathbf1-\mu^0\rangle.
\]

The supremum separates over components and equals
\(\sum_C\max\{0,\langle w,d_C\rangle\}\). This proves necessity and
sufficiency. \(\square\)

Thus a nonnegative weighted family of literal holes is the complete
fractional obstruction; there is no hidden quadratic dual at the
orientation stage. Integrality can nevertheless fail. In the important
one-unit, disjoint-direction case it has an exact answer.

### Corollary 8.2 (disjoint-direction integral orientation)

Assume every target cell belongs to the signed support of at most one
component. Let \(H_{\rm fix}\) be the number of base holes outside all
direction supports. For a component \(C\), let

\[
H_C^0=|\{\alpha\in\operatorname {supp}d_C:\mu^0_\alpha=0\}|,
\tag{8.5f}
\]

\[
H_C^1=|\{\alpha\in\operatorname {supp}d_C:
                    \mu^0_\alpha+d_C(\alpha)=0\}|.
\tag{8.5g}
\]

Then the exact minimum aggregate hole count over integral shores is

\[
\boxed{
\min_{\varepsilon\in\{0,1\}^{\mathcal C}}
\mathfrak H(\varepsilon)
=H_{\rm fix}+\sum_C\min\{H_C^0,H_C^1\}.}
\tag{8.5h}
\]

In particular, an \(o(W)\) orientation exists exactly when the right side
is \(o(W)\).

#### Proof

Under the support-disjointness hypothesis, changing component \(C\)
affects no cell controlled by another component. Its two choices leave
exactly \(H_C^0\) or \(H_C^1\) holes on its support. The choices therefore
separate, while holes outside all supports are fixed. \(\square\)

This exposes the canonical bipolar obstruction. If one component has many
exclusive holes filled only by shore one and many unit-reserve targets
destroyed only by shore one, it pays the smaller of those two masses. A
linear sum of such minima is an exact integral no-go. Conversely, a
protected-deck matching whose component directions are disjoint and whose
same-sign minima total \(o(W)\) solves the orientation gate with no heat or
variance argument.

These two assertions are sufficient. Indeed, with
\(K=N_{q_0}/(2m)+O(1)\), concatenating all ordinary packet words, then
repairing missing middle owners and signed annular holes, has length

\[
\begin{aligned}
K(2m+2H)
&+\bigl(W-(2mK-C_0)\bigr)
+\sum_{q=q_0}^{H}(h_q^-+h_q^+)\\
&=W+C_0+2HK
+\sum_{q=q_0}^{H}(h_q^-+h_q^+)+O(m),
\tag{8.6}
\end{aligned}
\]

where \(C_0\) is middle collision mass. Since

\[
2HK=O_{a,b}(W/\sqrt m)=o(W),
\tag{8.7}
\]

the two integral assertions give \(W+o(W)\) on the fixed annulus.

## 9. Proved boundary

The following points are now rigorous.

1. Two ordinary packet pairs admit a nontrivial physical component switch
   which fixes the entire middle and depth-\(q_0\) load vectors.
2. The switch changes literal target masses at every deeper depth, with the
   exact triangular formula (4.4).
3. Mesoscopic width \(\Theta(\sqrt m)\) gives \(\Theta(W)\) total
   target-variation capacity at the corrected packet mass; favorable
   orientation is a separate condition.
4. Bounded-width or adjacent-switch banks have only \(o(W)\) capacity and
   are closed statewise.
5. The full component orbit realizes the exact corrected fractional loads.
6. Simultaneous shore choices preserve middle collision and first-annulus
   coverage identically.
7. The tight protected orbit has relative pair-codegree at most
   \((5+o(1))/m^2\) and conditioned extra-overlap moment \(O(m^{-2})\).
8. Even with those bounds, arbitrary hereditary regeneration is false:
   an exactly point-balanced residual of density
   \(1-\Theta(m^{-1/2})\) can contain no component.
7. After protected duplicates are collapsed, the component orbit has
   relative codegree \(O(m^{-3/2})=o(m^{-1})\); its mixed-layer codegree is
   superpolynomially smaller.
8. The signed reserve system has the exact Farkas dual (8.5e), and in the
   disjoint-direction case its integral optimum is (8.5h).
9. Nevertheless all component choices together have only \(o(W)\)
   rankwise capacity and \(O(W)\) aggregate capacity. Thus they cannot
   repair a Poisson seed or any one linear-defect rank.

What remains unproved is the protected-deck component matching and the
common signed reserve orientation (8.4). Density alone does not imply
either assertion. In particular, (7.2)--(7.4) must not be converted into
an integral conclusion by independent sampling: its target loads are
bounded, so Poisson holes remain linear at each typical depth.
Moreover, (6.5a) shows that the base matching must already solve every
individual annular layer to \(o(W)\); the switch supplies only the final
cross-depth \(O(W)\)-scale correction.

Accordingly, this note does not claim coefficient one. It supplies an
explicit two-seed component class at the correct constant-density scale,
closes all bounded local switches, and identifies the precise integral
matching-and-orientation statement still needed.

This boundary composes with
`MATH_THEOREM_FIXED_ANNULUS_PARTIAL_CYCLIC_PACKET_LEDGERS_AND_UNGROUPED_HALL_20260726.md`:
that theorem supplies exact ungrouped owner-disjoint, all-depth flags,
while the present note supplies an explicit common-protected-deck physical
switch. The still-missing theorem is exactly the grouping of those flags
into a protected component matching satisfying the rankwise and aggregate
preconditions above. Neither result by itself supplies that grouping.
