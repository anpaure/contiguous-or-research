# Fixed period `q+2` does not absorb the corrected pull vector by disjoint pure blocks

**Date:** 2026-08-13  
**Status:** unconditional configuration inequality and one exact counterexample.
It rules out importing the corrected triangular pull-clock coefficients unchanged by
packing disjoint pure low blocks into every period-`q+2` packet.  It does **not** rule
out the more general distributed-core schedules or complete nested-ticket portals.

## 1. The fixed-period configuration polytope

Put `N=q+2`.  A pure pull block of run length `j` occupies `j` low phases followed by
one high separator, hence consumes

\[
                             w=j+1
\]

cyclic phase slots.  If `n_w` is the number of blocks of size `w` placed in one
packet, every literal disjoint-block configuration obeys

\[
                 \sum_{w=2}^{q}w n_w\le N.                 \tag{1.1}
\]

Let

\[
 X_j=\sum_{\delta=1}^{c}x_{\delta,j}                       \tag{1.2}
\]

be the aggregate density of type-`j` blocks per source phase in the corrected pull
clock.  A convex mixture of period-`N` configurations reproducing those coefficients
would have required expected block counts

\[
                             \mathbb E n_{j+1}=N X_j.       \tag{1.3}
\]

Thus membership is an ordinary finite integer-knapsack configuration-polytope question.
The scalar cost `sum (j+1)X_j<=1` is necessary but is not sufficient because (1.1)
has indivisible configurations.

## 2. A sharp long-block inequality

Assume `N=2h` is even.  Every configuration satisfies

\[
 \boxed{
 {1\over2}n_h+\sum_{w=h+1}^{N}n_w\le1.}                   \tag{2.1}
\]

Indeed, two `h`-blocks exactly fill the ring; any block larger than `h` excludes every
other block of size at least `h`, and the displayed half-weight inequality follows.
Taking expectations in (2.1), a necessary condition for the pull vector is

\[
 \boxed{
 N\left({1\over2}X_{h-1}+\sum_{j=h}^{q-1}X_j\right)\le1.} \tag{2.2}
\]

This is a genuine facet-type obstruction that the average slot cost does not detect.

The aggregate coefficients can be evaluated without retaining the `delta` index.  In
the notation of the corrected pull-clock theorem, put

\[
 P=\sum_{t=1}^{c}A_t,
 \qquad \Delta_j=w_j-w_{j+1}.
\]

Summing
`x_(delta,j)=A_delta Delta_j-A_(delta+1)Delta_(j+1)` gives

\[
 \boxed{X_j=P\Delta_j-(P-A_1)\Delta_{j+1}.}                \tag{2.3}
\]

Hence (2.2) is an explicit rational inequality in binomial coefficients.

## 3. Exact failure at `k=8191`

Take

\[
 k=8191,\qquad R=4096,\qquad d=57,
 \qquad q=58,\qquad N=60,\qquad c=4038.                    \tag{3.1}
\]

Here the Ferrers boundary is empty, so

\[
 q_s={\binom{k}{s}\over\binom{k}{R}}.
\]

Exact rational substitution in (2.2), with `h=30`, gives

\[
 \boxed{
 60\left({1\over2}X_{29}+\sum_{j=30}^{57}X_j\right)
 =1.015852125922422\ldots>1.}                             \tag{3.2}
\]

The accompanying verifier performs this comparison using Python integers and
`fractions.Fraction`; the asserted inequality is therefore exact, not a floating-point
decision.  Consequently the corrected pull vector is outside the convex hull of all
disjoint pure-block configurations in a period-`60` packet.

For orientation, an exact configuration LP gives radial gauge

\[
                              0.984395242656<1,             \tag{3.3}
\]

and its dual is precisely (2.1): size `30` receives weight `1/2`, sizes `31` through
`58` receive weight `1`, and smaller sizes receive weight zero.

## 4. Why this does not kill the distributed-core route

The obstruction applies only when a packet is decomposed into separated pure low blocks
whose resource use is `j+1` slots each and whose mixture is required to reproduce the
old coefficients `x_(delta,j)` literally.  A general distributed-core packet chooses
one cyclic emission word per coordinate.  Its low cells can overlap and share phase
positions, and the complete nested-ticket theorem programs a whole containment chain at
one endpoint without representing it as a union of independent pure blocks.

Therefore the correct consequence is:

> the old stationary pull decomposition cannot simply be compressed into fixed
> `q+2` packets; one must solve the correlated nested-ticket/age-word configuration
> problem directly (or alter the coefficient decomposition).

This sharpens, rather than refutes, the period-`q+2` programme.  The surviving global
gate is the joint selection of schedule-compatible endpoint tickets together with the
owner, immediate-lower, upper-provider, and trace rows.

## 5. Verification ledger

All substantive enumeration and LP work ran through `ssh h100`.

* exact rational verifier:
  `scratch/verify_qplus2_pull_long_block_obstruction_k8191_20260813.py`;
* symmetric independent-rotation rank-profile audit:
  `scratch/audit_qplus2_distributed_profile_20260813.py`;
* fixed-period pure-cost audit:
  `scratch/audit_fixed_qplus2_pull_configuration_cost_20260813.py`;
* exact configuration-polytope LP audit:
  `scratch/audit_qplus2_pull_knapsack_polytope_20260813.py`.
