# Diverse-order compiler packets remove the common-order syndrome obstruction

Date: 2026-07-26

Method: pure mathematics only.

## 0. Outcome

Let (H=H(m)) satisfy

\[
                         H\to\infty,\qquad H=o(m).
\tag{0.1}
\]

There is an admissible packet dimension (R) with

\[
                         H=o(R),\qquad R=o(m),
\tag{0.2}
\]

and an owner-disjoint family of physical (Q_R)-packets covering

\[
                         G=W-o(W/H)
\tag{0.3}
\]

middle owners, such that every packet has an exact factor into isometric
(C_{2R})'s and, for each sign and every (q\le H), the literal
depth-(q) trace map is injective on all owners of that packet.

Consequently:

1. there are no within-packet lower or upper trace repeats through depth
   (H);
2. the total number of cyclic components is

   \[
                            {G\over2R}=o(W/H);        \tag{0.4}
   \]

3. any external transfer lemma charging (O(H)) interface occurrences
   per component would cost only (o(W)) over all protected depths; and
4. the common-order syndrome obstruction is avoided sharply: every
   packet exposes exactly (2^R) distinct signed targets at each depth,
   whereas a common-order syndrome factor exposes at most
   (R2^{R-q}).

The construction does not yet control collisions between different
packets.  After this theorem, the only trace discrepancy is cross-packet
discrepancy.  Thus the remaining coefficient-one gate is a choice of
rank-twisted packet axes and compiler conjugates making those
cross-packet repeats equal the forced quota overload up to (o(W)),
simultaneously for both signs and all (q\le H).

## 1. Choice of scale

Choose (n=4\cdot2^t) to be the least admissible integer satisfying

\[
                            n\ge \sqrt{mH}.           \tag{1.1}
\]

Since successive admissible values differ by a factor two,

\[
                 \sqrt{mH}\le n<2\sqrt{mH}.          \tag{1.2}
\]

Put

\[
                            R=2n.                    \tag{1.3}
\]

Then (R=8\cdot2^t), and (0.1) gives

\[
 {R\over H}\ge2\sqrt{m/H}\longrightarrow\infty,
 \qquad
 {R\over m}<4\sqrt{H/m}\longrightarrow0.           \tag{1.4}
\]

In particular, for all sufficiently large (m),

\[
                            H\le {n\over2}-1={R\over4}-1. \tag{1.5}
\]

## 2. Exact packet compiler

The recursive parity-complete rotor theorem in

`MATH_ATTACK_S_PARITY_COMPLETE_MAPPING_TRACE_ENTROPY_CUT_20260726.md`

states that, for every (n=4\cdot2^t), the paired-order lift gives one
exact factor of (Q_{2n}=Q_R) into isometric (C_{4n}=C_{2R})'s.  In
the coordinate-disjoint Johnson realization, its literal lower and
upper trace maps are injective, from both physical phases and in both
orientations, through every physical length

\[
                            q\le {n\over2}-1.         \tag{2.1}
\]

By (1.5), this includes every (q\le H).

Fix one physical (Q_R)-packet.  Install this exact factor after
identifying its (R) active split-pair axes with the compiler's physical
directions, using one canonical forward orientation on every component.
The globally reversed construction is equally valid, but arbitrary
cyclewise mixing is not asserted.  Every owner belongs to one cycle.  At a fixed sign and
depth (q\le H), use every owner once as a directed start.  Literal
injectivity then gives exactly

\[
                            2^R                       \tag{2.2}
\]

distinct targets.  In particular the within-packet repeat count is zero.

This also proves the necessary direction-support diversity.  A fixed
(q)-support can expose at most (2^{R-q}) literal targets in one
packet.  Therefore (2.2) forces the factor to use at least (2^q)
different (q)-window supports.  This is precisely the exponential
support scale which the common-order syndrome factor, with only (R)
supports, lacks at Gaussian depth.

## 3. Near-spanning owner packing

Use the exact rank-twisted/log-block product-cell decomposition from

`MATH_THEOREM_RANK_TWISTED_MACROBLOCK_PACKET_TILING_20260726.md`.

For logarithmic macroblocks, a typical product cell has
((1/2+o(1))m) split axes.  Since (R=o(m)), the audited Chernoff and
rank-vector union bound shows that the middle owners lying in cells of
dimension below (R) have total size

\[
                            o(W/H).                   \tag{3.1}
\]

Every retained product cell (Q_S), (S\ge R), is partitioned into
physical (Q_R)'s by choosing (R) of its axes and freezing all
orientations of the other (S-R) axes.  Distinct fibres and distinct
product cells are owner-disjoint.  This proves (0.3).  Moreover, two
sibling (Q_R)-fibres inside one parent (Q_S) have disjoint signed trace
images: some frozen spectator axis has opposite recorded endpoints in
the two fibres, and no protected window moves that axis.

Install the packet compiler of Section 2 independently in every retained
(Q_R).  This yields an exact factor of the retained owner set.  No
fractional owner choice, open path, or completion leave occurs inside a
retained packet.

## 4. Component and interface ledger

Every compiler component has (2R) owners.  Hence the total number of
components is exactly

\[
                            M={G\over2R}.             \tag{4.1}
\]

By (1.4),

\[
                            HM={H\over2R}G=o(W).      \tag{4.2}
\]

Thus any separately proved transfer step which charges (O(H)) boundary
occurrences per component has total cost (o(W)).  Equivalently, the
component-count condition (M=o(W/H)) is automatic.  This note does not
construct that interface: a naive linear cut can expose
(Theta(H^2)) signed trace occurrences per component when summed over
depths.

Unlike the (Q_8) carousel construction, no long payload run or
turnaround collar is present.  The complete compiler theorem supplies
the literal trace statement on the entire component.  Thus there is no
separate (Q_8) seam ledger and no common-order kernel-translate repeat
inside a packet.

## 5. Exact cross-packet residual

Fix a sign and depth (q\le H).  Let the retained packets be
(mathcal P), and let

\[
                 I_{P,q}^{\pm}\subseteq { [2m]\choose m\mp q}
\tag{5.1}
\]

be the literal image of the compiler factor in packet (P).  Section 2
gives

\[
                            |I_{P,q}^{\pm}|=|P|=2^R. \tag{5.2}
\]

Define the cross-packet repeat count

\[
 {cal R}_{q,\mathrm{cross}}^{\pm}
 =\sum_T\left(\#\{P:T\in I_{P,q}^{\pm}\}-1\right)_+. \tag{5.3}
\]

There are (G) retained occurrences and (N_q) available targets, so
the missing-target identity becomes

\[
 \boxed{
 M_q^{\pm}
 =N_q-G+{cal R}_{q,\mathrm{cross}}^{\pm}.}          \tag{5.4}
\]

There is no hidden within-packet term in (5.4).  Therefore the desired
central-band conclusion is equivalent to

\[
 \sum_{q\le H,\,\pm}
 \left({\cal R}_{q,\mathrm{cross}}^{\pm}-(G-N_q)\right)
 =o(W).                                             \tag{5.5}
\]

By the sibling-fibre observation in Section 3, collisions in (5.3) may
be restricted further to packets lying in different parent product
cells.  The design variables are now only:

1. the rank-dependent local matchings defining the transverse product
   cells;
2. the choice of the (R) active axes in each retained cell; and
3. the physical conjugate/context of the diverse-order compiler factor
   in each packet.

The proved ordered-profile Hall inequalities show that the complete
atlas has enough fractional capacity at every fixed Gaussian profile.
They do not yet prove one integral common choice attaining (5.5).  Thus
the exact remaining theorem is a cross-packet grouped Hall/covariance
theorem, stripped of all owner, component-count, local-trace, common-order,
payload, and seam issues.

## 6. Boundary of the result

Proved here:

* a near-spanning exact owner factor;
* (o(W/H)) cyclic components;
* literal two-sign trace injectivity inside every packet through all
  protected depths;
* zero within-packet trace repeats; and
* an exact reduction of all remaining error to (5.5).

Not proved here:

* the cross-packet covariance estimate (5.5);
* simultaneous integral selection of packet axes and compiler contexts;
* coefficient one.

The theorem's main point is that the common-order syndrome obstruction is
not an obstruction to packet owner factors in general.  It is removed by
using the already-proved diverse-order recursive compiler at a scale
(H\ll R\ll m).
