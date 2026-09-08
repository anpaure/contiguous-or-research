# The pull clock and arbitrary-boundary matching do not imply the whole-job configuration premise

**Date:** 2026-08-07  
**Status:** proof-safe implication audit and exact separation theorem.  The
corrected pull clock proves a stationary fractional marked-trace statement,
and the proper-shadow theorem proves arbitrary-deletion target capacity.
Their conjunction does **not** currently prove \(FC_D\).  The missing row
is the all-price Ferrers-configuration inequality displayed below.

## 1. The three objects are different projections

Fix a maximum piece length \(D\).  Let the canonical residual lower paths
have positive integer job lengths

\[
                         L_1,\ldots,L_N.
 \tag{1.1}
\]

Let \(M_u\) be the number of genuine collar sockets of exact capacity
\(u\), and put

\[
                         K_q=\sum_{u=q}^D M_u.
 \tag{1.2}
\]

In the adjacent-depth Boolean application these are the actual SCD-collar
tails, for example

\[
                         K_q=W-{k\choose t+q-1}
 \tag{1.3}
\]

with the parity-appropriate parameters.  The statement \(FC_D\) is
feasibility of the whole-job configuration LP against these exact tails.

The two new inputs prove different assertions.

1. The corrected pull clock proves that the residual rank vector belongs
   to the stationary marked-trace cone \(ST_{k,r,D}\).  Its atoms are
   literal trace states with selected nested suffix occurrences and its
   constraints are stationary trace and rank marginals.
2. The arbitrary-boundary theorem proves that every residual target family
   of size \(dW\) matches to \(d\) labelled copies of each owner.  Its
   atoms are individual target--owner incidences.
3. The \(FC_D\) atoms are integer fragmentations of each **whole canonical
   job**, and their aggregate resources are the nonuniform tails \(K_q\).

Neither item 1 nor item 2 labels all cells from one canonical path by one
integer fragmentation.  Neither identifies its resources with the exact
socket-type vector (1.2).  This is the precise projection mismatch.

## 2. Exact all-price criterion for \(FC_D\)

For one job of length \(L\), let \(\mathcal P_L\) be the finite set of
integer Ferrers vectors

\[
 \mathcal P_L=
 \left\{z\in\mathbb Z_{\ge0}^D:
 z_1\ge z_2\ge\cdots\ge z_D,
 \quad \sum_{q=1}^Dz_q=L\right\}.
 \tag{2.1}
\]

Equivalently, \(z_q\) is the number of pieces of that job having length at
least \(q\).  For a nonnegative price vector

\[
                         \lambda\in\mathbb R_{\ge0}^D,
 \tag{2.2}
\]

define the cheapest integral configuration price

\[
 \phi_L(\lambda)=
       \min_{z\in\mathcal P_L}\sum_{q=1}^D\lambda_qz_q.
 \tag{2.3}
\]

If

\[
                         c_\ell(\lambda)=
                         \sum_{q=1}^{\ell}\lambda_q,
 \tag{2.4}
\]

then \(\phi_L\) is equivalently the integer shortest-path recursion

\[
 \phi_0(\lambda)=0,
 \qquad
 \phi_L(\lambda)=
 \min_{1\le\ell\le\min(D,L)}
   \bigl(\phi_{L-\ell}(\lambda)+c_\ell(\lambda)\bigr).
 \tag{2.5}
\]

Since \(c_\ell(\lambda)\) is nondecreasing, the same value is obtained if
the chosen socket capacities are only required to have total at least
\(L\): trim the last overfilled socket to the exact remaining piece length,
which cannot increase its price.  Thus (2.3)--(2.5) are the tail-price form
of the authoritative physical covering closure, not an exact-fill
surrogate.

### Theorem 2.1 (exact configuration min--max)

The whole-job configuration LP is feasible if and only if

\[
 \boxed{
       \sum_{a=1}^N\phi_{L_a}(\lambda)
       \le\sum_{q=1}^D\lambda_qK_q
       \qquad\text{for every }\lambda\in\mathbb R_{\ge0}^D.}
 \tag{2.6}
\]

If there are \(H_b\) canonical jobs of length \(L_b\), the left side is
\(\sum_bH_b\phi_{L_b}(\lambda)\).

#### Proof

For each job take the polytope

\[
                         P_a=\operatorname{conv}\mathcal P_{L_a}
 \tag{2.7}
\]

and let \(P=P_1+\cdots+P_N\) be their Minkowski sum.  The configuration LP
is feasible exactly when

\[
                         P\cap\{y:y\le K\}\ne\varnothing.
 \tag{2.8}
\]

If (2.8) fails, finite-dimensional separation from the coordinatewise
down-set \(\{y:y\le K\}\) gives a separating normal
\(\lambda\ge0\); a negative coordinate is impossible because that down-set
is unbounded in every negative coordinate direction.  Separation says

\[
                         \min_{z\in P}\lambda\cdot z
                         >\lambda\cdot K.
 \tag{2.9}
\]

Conversely, (2.9) plainly rules out (2.8).  The minimum over a Minkowski
sum separates by jobs, and a linear functional minimizes over
\(\operatorname{conv}\mathcal P_{L_a}\) at an integral configuration.
Thus

\[
 \min_{z\in P}\lambda\cdot z
       =\sum_a\min_{p\in\mathcal P_{L_a}}\lambda\cdot p
       =\sum_a\phi_{L_a}(\lambda),
 \tag{2.10}
\]

which proves (2.6).  Finally, a configuration with piece lengths
\(\ell_1,\ldots,\ell_s\) costs
\(\sum_jc_{\ell_j}(\lambda)\), giving recursion (2.5).  \(\square\)

Equation (2.6) is the exact missing fractional premise in the
adjacent-depth theorem.  It is a genuine all-price family, not just total
work or the separate target Hall inequalities.

## 3. What the two proved theorems certify

### 3.1 Arbitrary deletion certifies a larger uniform resource projection

The proper-shadow theorem gives a target-once assignment with at most
\(d\) targets at each owner.  If one forgets nestedness and views an owner
as a uniform depth-\(d\) bin, its conjugate capacity tails are

\[
                         \widehat K_q=W
                         \qquad(1\le q\le d).
 \tag{3.1}
\]

The adjacent SCD collar instead has

\[
                         K_q=W-{k\choose t+q-1}<W
 \tag{3.2}
\]

on every active row.  More importantly, the target matching allows
incomparable targets at one owner and has no canonical-job colour.  Thus it
does not provide a point in any \(\mathcal P_{L_a}\), even before the
strict inequality between (3.1) and (3.2) is considered.

This logical gap exists already in a tiny anonymous model.  Two capacity-2
sockets have total cell capacity four, so four uncoloured cells fit.  The
three whole jobs of lengths \(1,1,2\) do not fit: each job needs at least
one socket, but only two sockets exist.  In (2.6), the price
\(\lambda=e_1\) gives left side three and right side two.  This is not a
Boolean counterexample; it shows exactly why cellwise capacity does not
formally imply whole-job feasibility.

### 3.2 The pull clock certifies trace/rank marginals, not job colours

The corrected pull-clock theorem constructs a convex combination of
literal marked traces and then thins marked occurrences rank by rank.  A
selected trace remains a nested chain after thinning, but its retained rank
support need not be one interval, and the theorem does not colour those
occurrences by canonical residual paths.

Its proved block-cost inequality

\[
                         \sum_{\delta,j}(j+1)x_{\delta,j}\le1
 \tag{3.3}
\]

is one physical clock-position functional on pull-block types.  The
variables \(x_{\delta,j}\) index trace blocks, not integer fragmentations of
each canonical job.  Thus (3.3) is not the family (2.6) with arbitrary
socket-tail prices \(\lambda\).

The canonical colour-passing theorem converts **interval** rows into
fragmentations of the horizontal suffix jobs.  It cannot be applied to an
arbitrary gapped marked-rank support.  No statement in
\(q\in ST_{k,r,D}\) supplies the missing colour passing, and stationarity
does not impose the exact SCD socket tails (1.2).

Consequently the pull clock proves neither side of the required coupling

\[
 \boxed{
 \begin{array}{c}
 \text{one integer Ferrers vector }z^a\in\mathcal P_{L_a}
       \text{ for every canonical job }a,\\
 \text{with }\sum_a z^a_q\le K_q\text{ simultaneously for all }q.
 \end{array}}
 \tag{3.4}
\]

It provides excellent fractional trace atoms, but (3.4) is a different
correlation.

## 4. Specializing to the packet boundary does not remove (2.6)

The packet-produced boundary has the left-filled Ferrers rank profile and
chooses named targets \(S_j\subset M_j\).  The proper-shadow theorem is
strong enough to forget those names: every such deletion leaves the same
uniform capacity matroid.  This closes the target-level Hamilton--Ferrers
intersection.

For \(FC_D\), however, deleting the boundary targets changes the canonical
job multiplicities only through the retained rank histogram.  For all
sufficiently large parameters that histogram remains nondecreasing, so it
has well-defined canonical suffix jobs; this is useful, but it does not
prove their all-price inequalities.  The packet containments
\(S_j\subset M_j\) do not specify a fragmentation of any canonical job and
do not alter the exact right side \(K\) in (2.6).

Explicitly, write \(\beta_s\) for the number of deleted rank-\(s\)
targets, put

\[
 n_s={k\choose s}-\beta_s,
 \qquad n_0=0,
 \qquad 1\le s<t,
 \tag{4.1}
\]

and note that the canonical jobs born at rank \(b\) have multiplicity
\(n_b-n_{b-1}\) and length \(t-b\).  The exact unresolved packet-boundary
inequality is therefore

\[
 \boxed{
 \sum_{b=1}^{t-1}(n_b-n_{b-1})
          \phi_{t-b}(\lambda)
 \le
 \sum_{q=1}^D\lambda_q
          \left(W-{k\choose t+q-1}\right)
 \quad(\lambda\in\mathbb R_{\ge0}^D).}
 \tag{4.2}
\]

Thus the corrected implication ledger is

\[
 \boxed{
 \begin{array}{c}
 q\in ST_{k,r,D}\quad\text{(proved)},\\
 \text{every packet boundary deletion is target-capacity-safe}
       \quad\text{(proved)},\\
 \not\Downarrow\\
 FC_D\quad\text{without (2.6) or an equivalent job-colouring coupling}.
 \end{array}}
 \tag{4.3}
\]

## 5. Exact smallest bridge to the adjacent-depth theorem

The existing smooth-binomial configuration theorem already proves (2.6)
for the globally concave covering-price class and, with a
\(\Theta(W)\) margin, for every fixed reciprocal ceiling ray and every
fixed nonnegative combination of those rays with linear volume.  A packet
boundary changes only \(h=O(k)=o(W)\) target cells, so these fixed positive
margin classes remain positive after the structured deletion.  The
surviving possible separator is therefore a genuinely nonconcave
covering-price profile outside those classes (and may vary with the
dimension).  Neither the pull-clock block cost nor uniform target
transversality controls that remaining profile.

The adjacent-depth MLD absorber does not require an integral solution of
the old whole-job system.  It requires only fractional \(FC_D\): after an
extreme-point choice, at most \(D\) whole jobs remain fractional and the
new depth supplies the occurrence-faithful reserve.

Therefore the shortest lower-side bridge is exactly one of the following
equivalent statements.

1. Prove the all-price inequalities (2.6) for the actual retained binomial
   job multiplicities and the actual tails (1.3).
2. Give a coupling from the pull-clock trace law to canonical whole-job
   colours whose conditional vector for each job lies in
   \(\mathcal P_{L_a}\) and whose aggregate tail is at most \(K\).
3. Give a direct feasible point of the job-specific configuration LP.

The arbitrary-boundary theorem may still be used later as a robust
target-containment certificate, and the pull clock may still be used for
the physical stationary carrier.  Neither substitutes for this one
all-price row.  Once (2.6) is proved, the existing adjacent-depth theorem
does the basic rounding, exceptional absorption, MLD spreading, and named
collar attachment; protected upper/resident serialization remains a
separate gate.
