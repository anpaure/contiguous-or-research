# Audit of the owner-fixed pair-omission spike chart

Date: 2026-07-25

Method: pure mathematics only. No computation, finite search, web search,
SAT, or solver is used.

Audited file:
`PAIR_OMISSION_OWNER_FIXED_SPIKE_CHART_20260725.md`.

## 0. Verdict

The chart has a valid and useful positive-Gram core, but the file is not
correct with all of its present quantifiers.  The central legality,
distinguished-depth curvature, Haar factor (1/4), and added-run upper
bound (2t) survive.  The following corrections are necessary.

1. For each leaf pair (B), one bijection (B\to A) must be fixed once
   and the already attached factor must satisfy
   (F_B=\theta_BF_A).  Two occurrences using the same (B) may not
   choose the two bijections independently.  Distinct overlapping leaf
   pairs cause no problem inside one hub-star.
2. Equation (2.3) is false when either innovation vanishes.  A case split
   gives the corrected nonnegative formula below.  The depth-(q) lower
   bound is unchanged.
3. The Haar gain is below the average of the two coherent endpoints, or
   below their maximum.  Relative to the prescribed all-old state it must
   be reduced by one half of the coherent endpoint drift.  Therefore the
   raw spike Gram is not a hereditary descent charge.
4. The unlabelled central endpoints ((S_i,Y_i)) are fixed pointwise, but
   row provenance changes.  This is literal unlabelled matching legality,
   not labelled synchronization.
5. The physical ledger is (2t) added selected runs, at most (4t) new
   raw run endpoints, and (O(Ht)) literal context positions.  A common
   spike has (t\le\operatorname {Cat}_{m-1}) in the proper-window range,
   but a positive density of diffuse spikes does not share this Catalan
   bound.
6. The one-hub star is not automatically compatible with the already
   frozen adjacent path of factors, and stars based at several hubs need
   a forest/holonomy compatibility theorem.

Thus the correct classification is: **PASS after scope and formula
corrections as a static one-hub spike lemma; FAIL as a hereditary
below-current collision-frame theorem.**

Throughout the Catalan and proper-window statements below assume

\[
 2\le q\le H\le m-2.
\tag{0.1}
\]

## 1. Fixed-factor quantifiers and central legality

Fix the hub pair (A), one exact factor (F_A), and, for every distinct
two-set (B) which will be used, fix one bijection

\[
 \iota_B:B\longrightarrow A
\]

once and for all.  Let (\theta_B) exchange corresponding coordinates
and require

\[
 \boxed{F_B=\theta_BF_A.}
\tag{1.1}
\]

An occurrence assigned leaf (B_i) must use this (\theta_{B_i}).
Without this convention, two occurrences with the same (B_i) may demand
two different factors on the same omitted-pair universe.  Nothing forces
those factors to coincide.

Now let (U_q(e_i)=U) and (D_i=U\setminus Y_i), and take
(B_i\subset D_i).  Since the old row avoids (A), while (Y_i) avoids
(B_i),

\[
 \theta_{B_i}S_i=S_i,
 \qquad
 \theta_{B_i}Y_i=Y_i.
\tag{1.2}
\]

Every lower flag is a subset of (S_i), so it too is fixed pointwise.
Replacing the old row token by its conjugate therefore retains the same
unlabelled lower--middle edge.  Arbitrary choices at distinct central
edges preserve lower saturation and middle injectivity, with every
untouched edge of the matching left in place.  This proof is unaffected
when distinct (B_i)'s intersect, and a repeated (B_i) is harmless once
(1.1) is imposed.

The literal token is nevertheless different: it lies in a row of (F_B)
rather than a row of (F_A).  Accordingly, “the complete central edge set
is identical” is correct only for unlabelled endpoints.

There is no hidden matching-completion loss.  The old owner (Y_i) is
removed at the same time as the conjugate token with that same owner is
inserted.  No other old token used (Y_i).

## 2. Corrected cross-Gram identity

At upper depth (p), abbreviate

\[
 U_i=U_p^{(i)},
 \qquad
 \widetilde U_i=\theta_{B_i}U_i,
 \qquad
 d_{i,p}=\delta_{\widetilde U_i}-\delta_{U_i}.
\]

If (d_{i,p}=0), then its inner product with every column is zero.  If
both (d_{i,p}) and (d_{k,p}) are nonzero, the old sets avoid (A)
and the two image sets meet (A).  Hence the old--image cross equalities
are impossible and

\[
 \boxed{
 \langle d_{i,p},d_{k,p}\rangle
 =
 \mathbf1_{\{d_{i,p}\ne0,\ d_{k,p}\ne0\}}
 \left(
  \mathbf1_{\{U_i=U_k\}}
  +\mathbf1_{\{\widetilde U_i=\widetilde U_k\}}
 \right)\ge0.}
\tag{2.1}
\]

The indicator in front is essential.  If, for example,
(\widetilde U_i=U_i), the negative and positive indicators in the
four-term expansion cancel.  Equation (2.3) of the audited file omits this
case and is therefore literally false.

At the distinguished depth (q), every (B_i\subset U), so every column
is nonzero and

\[
 \widetilde U_i=(U\setminus B_i)\cup A.
\]

Consequently

\[
 \langle d_{i,q},d_{k,q}\rangle
 =1+\mathbf1_{\{B_i=B_k\}}\ge1.
\tag{2.2}
\]

For arbitrary nonnegative depth weights this proves, exactly as claimed,

\[
 \boxed{
 \Gamma:=\mathfrak A-\mathfrak V
 =2\sum_{i<k}\langle d_i,d_k\rangle_w
 \ge w_q^+t(t-1).}
\tag{2.3}
\]

Thus the error in the displayed all-depth formula does not alter the
headline curvature constant.

## 3. Floor normalization and the missing endpoint drift

Let (Q) denote the doubled factorial-floor polynomial.  Its linear and
floor-baseline terms are constant on a fixed rankwise mass fibre.  For fair
independent bits one therefore has the exact identity

\[
 \boxed{
 \mathbb E Q(M_\varepsilon)
 =\frac{Q(M_0)+Q(M_1)}2-\frac\Gamma4.}
\tag{3.1}
\]

This is valid for the autonomous token ledger and for any completion which
is literally common to every corner.  A corner-dependent completion is
not covered.  The standard singleton-row (H)-contexts are also
choice-dependent; their number is controlled by the run ledger, but their
quadratic energy needs a separate load or Lipschitz estimate.

Writing

\[
 \Delta_{01}=Q(M_1)-Q(M_0),
\]

the exact comparison with the current all-old endpoint is

\[
 \boxed{
 \mathbb E Q(M_\varepsilon)-Q(M_0)
 =\frac{\Delta_{01}}2-\frac\Gamma4.}
\tag{3.2}
\]

Therefore (\Gamma/4) is a gain below the endpoint average, and some
corner lies at least (\Gamma/4) below the higher endpoint.  It is not a
gain of that size below (M_0) unless the drift term is controlled.  In
the half-floor convention (\Phi), every gain in (3.1)--(3.2) is divided
by two.

The problem is structural, not cosmetic.  At a rank whose arithmetic
floor itself has repeated targets, a floor minimizer can have a positive
raw spike Gram.  The endpoint drift must then cancel it because no state
can lie below zero floor excess.

At (q=2) the drift can be written explicitly.  Suppose the (t) moved
occurrences are part of a load (x_U=b+t).  Let (t_B) be the number
using leaf (B), and put

\[
 V_B=(U\setminus B)\cup A,
 \qquad y_B=x_{V_B}.
\]

At this rank alone,

\[
 \Delta_{01}
 =w_2^+\left[
 -2bt-t(t-1)
 +\sum_B\bigl(2y_Bt_B+t_B(t_B-1)\bigr)
 \right],
\tag{3.3}
\]

whereas

\[
 \Gamma
 =w_2^+\left[t(t-1)+\sum_Bt_B(t_B-1)\right].
\tag{3.4}
\]

Thus the certified expected descent from the old endpoint at this rank is

\[
 \boxed{
 \frac\Gamma4-\frac{\Delta_{01}}2
 =w_2^+\left[
 bt+\frac34t(t-1)-\sum_By_Bt_B
 -\frac14\sum_Bt_B(t_B-1)
 \right].}
\tag{3.5}
\]

Formula (3.5) exposes the missing Hall condition: an overloaded old target
must have sufficiently empty prescribed image targets.  Raw collision
multiplicity alone does not imply this.

## 4. Physical and Catalan ledgers

Switching one token increases the run count of its old row by at most one
and the run count of its conjugate row by at most one.  Hence, for (r)
actually switched tokens,

\[
 \boxed{
 \Delta J\le2r,
 \qquad
 \partial_{\rm new}\le4r,
 \qquad
 \text{literal context length}=O(Hr).}
\tag{4.1}
\]

The bound (2t) in the audited file is the safe specialization (r\le t).

When (q\le m-2), a fixed proper upper target occurs at most once in one
cyclic row.  Since (F_A) has

\[
 R_m=\operatorname {Cat}_{m-1}
\]

rows, a common-(U) spike satisfies

\[
 t\le R_m,
 \qquad
 2t\le2R_m
 =\frac{m+1}{2m-1}\operatorname {Cat}_m
 <\operatorname {Cat}_m.
\tag{4.2}
\]

Thus one concentrated spike has (o(W/H)) run cost for (H=o(m)), and
its standard contexts use (O(H\operatorname {Cat}_m)) positions.

This does not extend to diffuse collisions.  In a row

\[
 D_q(i)=\{x_{i+m-1},\ldots,x_{i+m+q-2}\}.
\]

For a fixed leaf (B), the starts satisfying (B\subset D_q(i)) form
either the empty set or one cyclic interval of length at most (q-1)
(because (q<(2m-1)/2)).  Distinct old rows give distinct conjugate rows.
Therefore moving (M) occurrences needs at least

\[
 \boxed{M/(q-1)}
\tag{4.3}
\]

new leaf-row blocks.  At (q=2) every carrier is a singleton.  A
positive-density bounded-multiplicity defect costs

\[
 \Omega(W/q)\ge\Omega(W/H)
\]

blocks for (q\le H), so it cannot be put inside an (o(W/H)) catalog.
The chart is efficient precisely on concentrated common-target spikes.

## 5. Compatibility with the adjacent atlas and heredity

The audited adjacent path fixes factors by

\[
 F_{P_{j+1}}=\tau_jF_{P_j}.
\tag{5.1}
\]

A hub-star asks instead for (F_B=\theta_{A,B}F_A).  These prescriptions
need not agree.  For three consistently labelled priority pairs, the path
relations

\[
 F_2=\theta_{12}F_1,
 \qquad
 F_3=\theta_{23}\theta_{12}F_1
\]

and the hub relation (F_3=\theta_{13}F_1) would force

\[
 \theta_{13}^{-1}\theta_{23}\theta_{12}
 =\theta_{23}\in\operatorname {Aut}(F_1).
\tag{5.2}
\]

This is exactly the two-pair-block triangle holonomy ruled out by the
audited K12 theorem for (m\ge4).  Overlapping leaves inside a single
fresh star are harmless; silently overlaying that star on the protected
path is not.

Fresh nonpriority leaf pairs avoid this conflict.  For (q\ge3), every
(q)-set (D_i) contains a two-subset which is not one of the disjoint
priority pairs.  At (q=2), the leaf is forced to be (B_i=D_i), so a
priority-pair collision may have no fresh star edge.

Even a compatible star is static.  Its sign proof is based at the all-
(A) representation, where every old upper target avoids (A).  After a
mixed spike corner, current tokens occupy several leaf factors, and the
same proof does not give a new common-hub nonnegative Gram.  Resetting to
the all-(A) endpoint incurs precisely the uncontrolled drift in (3.2).
Thus no hereditary renewal theorem follows.

Finally, a (q=2) spike necessarily changes the first upper flag: its
forced leaf (B=D_2) contains the first suffix coordinate.  The fact that
the adjacent (q=1) charge is zero does not make this leakage free.  A
separate first-rank drift bound or a (q=1)-neutral commutator is required.

## 6. Certified boundary

The corrected spike theorem proves a genuine fact:

\[
 \text{one common-phase upper spike}
 \quad\Longrightarrow\quad
 \Gamma\ge w_q^+t(t-1)
\]

with literal central integrality and a per-spike Catalan interface.

It does not prove any of the following:

* descent of (\Gamma/4) from the prescribed current endpoint;
* compatibility of a full star with the adjacent path factors;
* simultaneous stars for all owner categories;
* hereditary sign-definiteness after a mixed corner;
* a low-run packing of diffuse bounded-multiplicity collisions;
* control of the (q=1) leakage or of choice-dependent literal collars.

Accordingly the chart is valid and should be retained, but only through
the drift-corrected charge (\Gamma/4-\Delta_{01}/2) (doubled convention)
and only under the fixed-factor hypothesis (1.1).
