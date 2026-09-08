# Exact remaining cross-parent compiler-resolution theorem

Date: 2026-07-26

## 0. Purpose

This note records the smallest surviving positive theorem after the
owner, compiler, component-count, profile-Hall, and local parent-reachability
gates have been closed.

Let

\[
 {cal O}_m={ [2m]\choose m},\qquad W=|{cal O}_m|,
\]

and let

\[
 {cal T}_{q}^{-}={ [2m]\choose m-q},\qquad
 {cal T}_{q}^{+}={ [2m]\choose m+q},\qquad
 N_q=|{cal T}_{q}^{\pm}|.
\]

Choose

\[
 H=\sqrt m\,\omega(m),\qquad \omega(m)\to\infty,qquad H=o(m),
\]

and an admissible compiler dimension (R) satisfying

\[
                         H=o(R),\qquad R=o(m).
\]

The proved rank-twisted tiling and diverse-order compiler theorem give an
owner set of size

\[
                         G=W-e^{-\Omega(m)}W
                          =W-o(W/H)
\]

partitioned into physical (Q_R)-packets.  Every packet has an exact
isometric cycle factor and an injective signed literal trace map through
all depths (q<=H).  Sibling packets in one parent product cell have
disjoint trace images.  Hence every repeated target is a cross-parent
repeat.

## 1. Legal resolution states

A legal resolution state consists of:

1. rank-dependent local cross-half matchings in every logarithmic
   macroblock;
2. a dispersed (R)-axis selector in every retained product cell;
3. any sequence of exact cross-parent (Q_{R+1}) slab trades from
   `MATH_THEOREM_RANK_TWISTED_CROSS_PARENT_QR_PLUS_ONE_SLAB_TRADE_20260726.md`;
4. one physical affine/context conjugate of the diverse-order compiler
   in every final packet; and
5. one canonical orientation of all compiler components.

Every legal state is already an exact factor of the same retained middle
owner set.  No completion, fractional owner, or open path remains.

For a packet (P), sign (epsilon), and depth (q), let

\[
 I_{P,q}^{\epsilon}\subseteq{cal T}_{q}^{\epsilon}
\]

be its literal image.  Packet injectivity gives

\[
                         |I_{P,q}^{\epsilon}|=|P|=2^R.
\]

Define the global load

\[
 L_{q}^{\epsilon}(T)
 =\#\{P:T\in I_{P,q}^{\epsilon}\}.
\]

Then, exactly,

\[
                         \sum_TL_q^{\epsilon}(T)=G.
\]

## 2. Cross-parent compiler-resolution statement

Put

\[
 c_q=\left\lfloor{G\over N_q}\right\rfloor,
 \qquad r_q=G-c_qN_q.
\]

The exact remaining theorem is:

> **CPCR.** There are legal resolution states for which
> \[
>  \Phi_m=
>  \sum_{q=1}^{H}\sum_{\epsilon\in\{-,+\}}
>  \sum_{T\in{cal T}_q^\epsilon}
>  (L_q^\epsilon(T)-c_q)(L_q^\epsilon(T)-c_q-1)
>  =o(W).
> \]

Every summand is nonnegative because the load is integral.  It vanishes
exactly at the two balanced quota values (c_q,c_q+1).  Thus CPCR is a
single common all-depth, two-sign integer-floor covariance theorem.

The weaker missing-target version would suffice, but CPCR is the form
directly consumed by the audited quadratic ledger.

## 3. CPCR implies the central target theorem

For an integer (z),

\[
 (z-c_q)(z-c_q-1)
 \ge2(c_q-z)_++2(z-c_q-1)_+.
\]

Consequently CPCR gives

\[
 \sum_{q\le H,\epsilon}
 \max\left\{
   \sum_T(c_q-L_q^\epsilon(T))_+,
   \sum_T(L_q^\epsilon(T)-c_q-1)_+
 \right\}
 =o(W).
\]

The exponentially small owner leave is smaller than (W-N_1)=Theta(W/m),
so (c_q>=1) for every protected (q>=1) and all large (m).  Every missing target contributes at
least (c_q), and therefore

\[
                         \sum_{q\le H,\epsilon}M_q^\epsilon=o(W).
\]

The (o(W/H)) owner leave contributes only (o(W)) aggregate missing
occurrences over the protected band.

## 4. CPCR implies coefficient one

The packet factor has

\[
                         {G\over2R}=o(W/H)
\]

cyclic components.  Linearize each component by appending its first (H)
emitted entries.  This preserves every cyclic window through depth (H)
and adds total length

\[
                         O\left(H{G\over R}\right)=o(W).
\]

Concatenating the extended blocks loses no required internal window;
cross-block windows only add masks.  The standard product-SCD tail
handles ranks beyond the chosen diagonal (H).  Therefore CPCR implies a
contiguous-OR array of length

\[
                         W+o(W),
\]

and hence the constant-one upper bound.

## 5. What is already proved around CPCR

The following inputs are no longer conjectural.

1. Near-spanning exact owner packetization with leave (o(W/H)).
2. Diverse-order compiler factorhood and literal two-sign injectivity
   inside every packet through (H).
3. Component count (o(W/H)).
4. Dispersed selected-axis profile expansion.
5. Arbitrary-subset Hall expansion inside every exact ordered profile,
   outside exponentially small overlap strata.
6. Exact Hamming-two cross-parent slab reachability.
7. Exact conditional-expectation rounding once a low-cost packet
   distribution is known.

The remaining unproved parts are genuinely global.

1. Weighted allocation of shared source-profile capacity between target
   profiles.
2. Compiler-image realizability of the resulting target bundles.
3. All-depth cancellation/routing of the cross-parent slab derivatives.
4. The floor covariance bound CPCR itself.

Thus CPCR is not a restatement of owner factorhood or of the original
wreath conjecture.  It is the residual target-labelled resolution theorem
after every local and fractional gate listed above has been discharged.

## 6. Cross-profile and touched-axis audit

MATH_THEOREM_OVERLAP_COMPRESSION_CROSS_PROFILE_AND_PACKET_UNION_CUT_20260726.md
aligns two new negative results with CPCR.

First, the closed profile-Hall and within-profile expansion inputs do not
formally imply the first remaining global item.  For every \(K\ge2\), an
explicit bipartite graph has exact \(K\)-fold expansion for every
subfamily inside each target profile and satisfies the full weighted
profile-constant Hall dual, yet a mixed-profile raw family has
neighborhood ratio exactly \(1/2\).  Thus weighted allocation of shared
source-profile capacity requires a genuinely cross-profile overlap or
source-normalized-flow theorem.

Second, inside a frozen parent \(Q_S\), there is a near-spanning injective
two-sign raw face assignment for which every coordinate
\(Q_R\)-packetization retains at most

\[
                 (2+o(1)){\binom Rq\over\binom Sq}=o(1)
\]

of the assigned touched-axis sets.  Hence a raw injection cannot be
chosen first and packetized afterward.  This does not refute CPCR:
cross-parent \(Q_{R+1}\)-slab trades leave the frozen-parent hypothesis
and are exactly the permitted mechanism for re-atlasing before compiler
selection.

For one colour \(c=(\epsilon,q)\), the audit also records the exact
identity

\[
 \sum_T(L_c(T)-c_q)(L_c(T)-c_q-1)
 =2\left[
      \sum_T\binom{L_c(T)}2
      -N_q\binom{c_q}2-r_qc_q
    \right].
\]

Thus its final coherent target is precisely CPCR's cross-parent excess
factorial covariance.  Neither negative result reopens common-order
syndrome, within-packet injectivity, component count, or sibling-packet
collision gates.
