# Diffuse collision fusion: exact rainbow binning and the rotating-frame obstruction

Date: 2026-07-25

Method: pure mathematics only. No computation, search, or solver is used.

## 0. Outcome

Let \(C\) be the number of upper same-target collision pairs in fibres of
loads between \(2\) and \(K\), over depths \(q\le H\). There is no
combinatorial packet-count obstruction. Within every fixed source
phase/depth stratum, the occurrences admit a deterministic rainbow
partition into packets such that:

1. every packet contains at most \(H\) occurrences;
2. two occurrences from the same collision fibre lie in different packets;
3. the total number of packets is at most

\[
 \boxed{
 {2C\over H}+(K+1)s,}
\tag{0.1}
\]

where \(s\) is the number of nonempty phase/depth strata.

For the pair-omission system, \(s\le mH\). Thus for every polynomially
bounded \(K,H\),

\[
 (K+1)s=o(W/H).
\tag{0.2}
\]

Tying one owner-fixed spike bit inside each abstract packet loses none of
the certified collision Gram: every collision pair crosses two packet
bits, and all other cross terms inside one source phase are nonnegative.

The obstruction is entirely physical. On one labelled tight source row,
a fixed owner-preserving coordinate conjugacy can activate at most two
q-clean spike occurrences. Consequently any construction made only from
constant-frame row intervals needs at least

\[
 \boxed{{C\over K-1}}
\tag{0.3}
\]

physical pieces in the worst bounded-load sector. For \(K=o(H)\), this is
larger than \(C/H\) by the divergent factor \(H/(K-1)\).

Allowing ordinary seams between constant-frame pieces does not solve the
problem. If \(P\) outer packets use \(R\) internal row/frame seams, then

\[
 \boxed{T\le2(P+R),}
\tag{0.4}
\]

where \(T\) is the number of spiked occurrences. Hence a proposed
\(P=O(C/H)\) fusion of load-two fibres requires \(R=\Omega(C)\) internal
frame changes. Any positive entry or reset toll per such change costs
\(\Omega(C)\), which is macroscopic when \(C=\Theta(W)\).

The minimally stronger object is therefore not another interval selection
lemma. It is an **entry-neutral rotating-frame two-port seam**: it must
join occurrence-specific conjugate row pieces while changing their omitted
pair/frame at no extra word position, and expose common entrance and exit
states so independently chosen rainbow packets concatenate without resets.
An exact formulation is given in Section 5. With that object, (0.1)
immediately gives the requested \(2C/H+o(W/H)\) packet bound while
preserving the q=1 seed.

Thus the requested fusion is false for the present constant-frame
pair-omission chronology, but its missing strengthening is now exact.

## 1. The abstract rainbow packet lemma

Fix one source phase \(A\) and one depth \(q\). Let the collision fibres
be

\[
 G_1,\ldots,G_r,\qquad
 2\le\mu_j:=|G_j|\le K.
\]

Put

\[
 T=\sum_{j=1}^r\mu_j,\qquad
 C=\sum_{j=1}^r{\mu_j\choose2}.
\tag{1.1}
\]

### Theorem 1.1 (balanced rainbow binning)

Let

\[
 P=\max\left\{K,\left\lceil{T\over H}\right\rceil\right\}.
\tag{1.2}
\]

The \(T\) occurrences can be assigned to \(P\) packets so that:

* every fibre uses distinct packets;
* every packet has size at most \(H\).

#### Proof

Start with \(P\) empty packets. Process the fibres in any order. When
processing a fibre of size \(\mu\), put its occurrences into \(\mu\)
distinct currently least-loaded packets.

Because \(\mu\le K\le P\), this is always possible. The packet loads
remain within one of each other. Indeed, before one step suppose all loads
are \(a\) or \(a+1\). If at least \(\mu\) packets have load \(a\), only
such packets are incremented. Otherwise all load-\(a\) packets and the
necessary number of load-\((a+1)\) packets are incremented, leaving loads
in \(\{a+1,a+2\}\). This proves the invariant inductively.

At the end, the maximum load is

\[
 \left\lceil{T\over P}\right\rceil\le H.
\]

Each fibre was explicitly placed in distinct packets. \(\square\)

The collision/occurrence relation is

\[
 \mu\le\mu(\mu-1)=2{\mu\choose2}\qquad(\mu\ge2),
\]

so

\[
 T\le2C.
\tag{1.3}
\]

For several nonempty phase/depth strata \(\alpha\), apply Theorem 1.1
separately. Since

\[
 \max\{K,\lceil T_\alpha/H\rceil\}
 \le K+1+T_\alpha/H,
\]

summing and using (1.3) proves

\[
 \boxed{
 P_{\rm tot}\le {2C_{\rm tot}\over H}+(K+1)s.}
\tag{1.4}
\]

In the pair-omission system there are at most \(m\) source phases and
\(H\) depths, so \(s\le mH\). Since \(W\) is exponential in \(m\), the
second term in (1.4) is \(o(W/H)\) for every polynomially bounded
\(K,H\).

## 2. Rainbow binning loses no collision curvature

For every occurrence \(i\), take the owner-fixed helper spike from
PAIR_OMISSION_OWNER_FIXED_SPIKE_CHART_20260725.md. Within one source
phase, its innovation vectors satisfy

\[
 \langle d_i,d_k\rangle_w\ge0
\tag{2.1}
\]

at every pair of occurrences. If \(i,k\) belong to the same depth-\(q\)
collision fibre, then

\[
 \langle d_i,d_k\rangle_w\ge w_q^+.
\tag{2.2}
\]

Tie all occurrence bits in one rainbow packet to one packet bit. Let

\[
 z_P=\sum_{i\in P}d_i.
\]

The coherent-versus-packet variance gap is

\[
 \left\|\sum_Pz_P\right\|_w^2-\sum_P\|z_P\|_w^2
 =2\sum_{P<Q}\langle z_P,z_Q\rangle_w.
\tag{2.3}
\]

All terms on the right are nonnegative by (2.1). The rainbow property
places the two ends of every collision pair in different packets, so
(2.2) gives

\[
 \boxed{
 \left\|\sum_Pz_P\right\|_w^2-\sum_P\|z_P\|_w^2
 \ge2\sum_qw_q^+C_q.}
\tag{2.4}
\]

Thus abstract packet correlation retains the complete certified collision
curvature. There is no bounded-multiplicity loss in the Gram or floor
Haar calculation.

For \(q\ge2\), the helper spike fixes every upper flag of depth below
\(q\), in particular the q=1 seed. At \(q=1\), use the fixed-marker
version \(b_i\leftrightarrow a_1\), \(z_i\leftrightarrow a_2\). Its
distinct-image current-relative identity remains valid after rainbow
packetization: occurrences from one old collision fibre are in different
packets, and images from all selected fibres are distinct.

Accordingly, to preserve a PBBS q=1 seed, process a q=1 packet family only
when its marker sink certifies nonincrease from the current endpoint.
Otherwise leave that q=1 family untouched. The PBBS seed already has
q=1 defect \(o(W)\), so no q=1 fusion is required merely to obtain
constant one. All \(q\ge2\) helper packets preserve that ledger pointwise.

## 3. The fixed-frame physical obstruction

We now prove that the abstract packets cannot be realized by the present
constant-frame row mechanism.

Take one tight source row

\[
 \pi=(x_0,\ldots,x_{2m-2})
\]

and use

\[
 Y_i=I_\pi(i-1,m),\qquad
 U_p(i)=I_\pi(i-1,m+p).
\tag{3.1}
\]

At depth \(q\), the unique entering marker is

\[
 b_{i,q}\in U_q(i)\setminus U_{q-1}(i).
\tag{3.2}
\]

Explicitly, \(b_{i,q}\) is a fixed cyclic shift of \(x_i\). Therefore,
as \(i\) runs around one row, the markers \(b_{i,q}\) are all distinct.

### Lemma 3.1 (two-marker capacity)

Let \(\theta_B\) be one coordinate conjugacy exchanging the omitted source
pair \(A\) with a fixed two-set \(B\). Suppose a token at start \(i\):

1. keeps its central incidence \((S_i,Y_i)\);
2. fixes every old upper flag of depth \(p<q\);
3. changes its upper depth-\(q\) flag.

Then

\[
 b_{i,q}\in B.
\tag{3.3}
\]

Consequently one fixed \(\theta_B\) can activate at most two starts of one
labelled source row at depth \(q\).

#### Proof

The old source row avoids \(A\). To fix \(U_{q-1}(i)\), the conjugacy
cannot move any point of that set into \(A\); hence

\[
 B\cap U_{q-1}(i)=\varnothing.
\]

To change \(U_q(i)\), it must meet \(B\). But

\[
 U_q(i)\setminus U_{q-1}(i)=\{b_{i,q}\},
\]

so \(b_{i,q}\in B\). The marker map is injective on the row and
\(|B|=2\), proving the capacity bound. \(\square\)

A physical interval of one conjugate row has one fixed \(\theta_B\).
Therefore it contains at most two q-clean active spikes, regardless of
its length. The same is true for a noncontiguous collection inside that
labelled row; contiguity is not the source of the obstruction.

Let \(T\) diffuse collision occurrences be covered by \(P\) such
constant-frame row pieces. Lemma 3.1 gives

\[
 P\ge T/2.
\tag{3.4}
\]

On the other hand, because \(\mu\le K\),

\[
 C=\sum_j{\mu_j\choose2}
 \le {K-1\over2}\sum_j\mu_j
 ={K-1\over2}T.
\]

Thus

\[
 \boxed{
 P\ge{C\over K-1}.}
\tag{3.5}
\]

When \(K=o(H)\), (3.5) is asymptotically larger than \(C/H\) by the factor
\(H/(K-1)\). In particular, load-two fibres have \(T=2C\) and force
\(P\ge C\), while the desired bound is \(O(C/H)\).

This is a sharp obstruction to every deterministic argument which merely
chooses longer intervals inside fixed conjugate rows. It does not depend
on probabilistic independence or on an inefficient packet selection.
Although a fixed pair could activate up to two markers at each of several
different depths, this does not evade the obstruction: the proposed fusion
theorem must also handle instances whose entire diffuse collision mass is
concentrated at one depth. Equations (3.4)--(3.5) apply to that sector
without change.

## 4. Ordinary critical seams still cost one per constant-frame piece

Suppose an outer packet may concatenate several labelled constant-frame
row pieces using internal seams. Let \(P\) be the number of outer packets
and \(R\) the total number of internal row/frame seams. There are exactly
\(P+R\) constant-frame pieces. Lemma 3.1 gives

\[
 \boxed{T\le2(P+R).}
\tag{4.1}
\]

Equivalently,

\[
 \boxed{
 R\ge {T\over2}-P
 \ge {C\over K-1}-P.}
\tag{4.2}
\]

If \(P=O(C/H)\) and \(K=o(H)\), then

\[
 R=\Omega(C/K).
\tag{4.3}
\]

For load-two fibres this is \(R=\Omega(C)\). Hence any seam which consumes
one additional word entry, one reset, or one \(H\)-initialization per frame
change has macroscopic cost when \(C=\Theta(W)\).

The critical profile-seam lower bound \(\Omega(W/H)\) does not remove this
obstruction. It says profile-changing seams must exist. Here the
occurrence-specific two-marker geometry says that, for diffuse load-two
spikes, constant-frame realizations require the much larger
\(\Omega(C)\) sequence of frame changes. Those changes must therefore be
absorbed into ordinary owner updates rather than paid as extra entries.

## 5. The minimally stronger seam object

The abstract rainbow packets from Section 1 identify the exact missing
physical theorem.

> **Entry-neutral rotating-frame rainbow seam.** Fix one source phase
> \(A\), one depth \(q\le H\), and a rainbow packet
> \(\mathcal P\) of at most \(H\) owner-fixed helper spikes, with at most
> one occurrence from each old collision fibre. There are two literal
> physical realizations \(R^0(\mathcal P)\) and \(R^1(\mathcal P)\) such
> that:
>
> 1. both realize exactly the same designated lower-owner incidences;
> 2. \(R^0\) carries all old flag towers and \(R^1\) carries all
>    occurrence-specific conjugate flag towers;
> 3. both have the same entrance and exit ordered-partition states;
> 4. their length is \(|\mathcal P|+O(1)\), with the \(O(1)\) uniform in
>    \(H\);
> 5. the common ports concatenate consecutive packets using no reset and
>    no additional designated owner;
> 6. for \(q\ge2\), all upper flags below q, including the q=1 seed, are
>    identical in the two realizations; at q=1 the fixed-marker
>    current-relative orientation is available.

Condition 3 is the two-port requirement. Condition 4 is the
entry-neutrality which (4.2) proves necessary: an \(O(1)\) cost for every
internal frame change would be \(O(|\mathcal P|)\), whereas one \(O(1)\)
cost for the whole rainbow packet is \(O(C/H)\).

The object is weaker than arbitrary factor rebundling. It is required only
for packets of at most \(H\) already legal owner-fixed spikes in one source
phase/depth stratum, and it may use the packet's old central owners as its
seam states.

### Conditional fusion theorem

If the entry-neutral rotating-frame rainbow seam exists, apply it to the
packets from Theorem 1.1. Equation (1.4) gives

\[
 \boxed{
 P_{\rm tot}\le {2C\over H}+o(W/H).}
\tag{5.1}
\]

The common ports make all packet bits simultaneously physical in one
critical-seam chronology. Equation (2.4) retains every certified collision
pair. For \(q\ge2\) the q=1 seed is unchanged, and the q=1 marker packets obey
the current-relative sink identity.

Thus this seam object is exactly sufficient for the requested diffuse
collision fusion. Lemmas 3.1 and 4.1 show why the presently available
fixed-conjugacy row intervals cannot substitute for it.

## 6. Exact status

Proved:

* the deterministic rainbow packet count \(2C/H+(K+1)s\);
* lossless collision-Gram packetization;
* the two-marker capacity of every fixed row/frame;
* the lower bound \(P\ge C/(K-1)\);
* the internal frame-seam lower bound \(T\le2(P+R)\).

Not proved:

* the entry-neutral rotating-frame two-port seam.

Therefore the diffuse bounded-multiplicity obstruction is not a packing or
charging problem. It is a frame-changing physical fusion problem.

The positive rainbow-Gram statement here concerns upper spikes inside one
omitted source phase. For the lower-dual spike, nonnegative cross-Gram is
proved inside one common-\(L\) collision fibre, but innovations belonging
to different lower targets can have negative image/old cross equalities.
Consequently a two-sided version additionally needs a marker-stratified
lower-fibre schedule; it does not follow formally from Theorem 1.1.
