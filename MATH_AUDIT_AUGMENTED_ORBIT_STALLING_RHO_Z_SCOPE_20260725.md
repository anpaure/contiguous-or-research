# Audit: augmented-orbit stalling versus the \(\rho/z\) recurrence

Date: 2026-07-25

Method: pure mathematics only.

## 0. Verdict

The first-moment proposition in
`AUGMENTED_ORBIT_STALLING_AND_SOFT_TRACE_REDIRECT_20260725.md` is
correct in its stated scope:

* one fixed family of at most \(M\) **distinct resource supports**;
* each support uses \(K\) resources;
* those resources survive independently with common probability \(z\)
  (or with the corresponding product of stratum densities).

In that model,

\[
 \mathbb E|{\cal O}_{\rm live}|=Mz^K,
 \qquad
 \Pr({\cal O}_{\rm live}\ne\varnothing)\le Mz^K.
 \tag{0.1}
\]

For one coordinate orbit, \(M\le n!\), while the full floor-calibrated
hard template has

\[
 K=(1+o(1))n\sqrt{\pi m}.
 \tag{0.2}
\]

Therefore a product-like trajectory loses the whole orbit after
consuming only \(O(\log m/\sqrt m)\) of the resources.  It certainly
cannot reach \(z=1/\log m\).

This does **not** prove that every correlated matching process or every
current residual catalogue is empty.  It rules out the product-like
trajectory for one giant hard support orbit.  A correlated process can
preserve a highly atypical family of supports, and a union of extremely
many genuinely distinct support types changes \(M\).

The \(\rho/z\) pair recurrence is compatible with this result but needs
an explicit abundance hypothesis.  It is a conditional statement about
relative link and degree decay.  Even perfect cancellation of \(\rho\)
in the normalized recurrence is useless once

\[
 \rho_tD_0(F)\ll1
 \tag{0.3}
\]

or the number of surviving distinct supports is \(o(1)\).  For the
single-orbit product model, \(\rho_t=z_t^K\), so this absolute-degree
condition fails near the stalling threshold.

Accordingly:

\[
 \boxed{
 \begin{array}{c}
 \text{Retire: one full augmented coordinate orbit under a standard}\\
 \text{product/pseudorandom hard-resource nibble.}\\[1mm]
 \text{Retain: correlated exact-factor dynamics and hard-middle/soft-trace}\\
 \text{processes, where lower traces are an additive objective rather than}\\
 \text{vertices of one giant hard edge.}
 \end{array}}
 \tag{0.4}
\]

The stochastic lane should therefore be recast as soft-target
optimization, not discarded universally.

## 1. Verification of the threshold

Let \({\cal O}\) be a family of \(M\) distinct \(K\)-subsets of a
resource universe, and let \(R_z\) retain every resource independently
with probability \(z\).  If

\[
 X=|\{e\in{\cal O}:e\subseteq R_z\}|,
 \tag{1.1}
\]

then linearity of expectation gives

\[
 \mathbb EX=Mz^K.
 \tag{1.2}
\]

No independence among the edge-survival events is needed for (1.2).
Markov gives

\[
 \Pr(X>0)\le Mz^K.
 \tag{1.3}
\]

For one \(S_n\)-coordinate orbit, \(M\le n!\).  For the floor
calibration,

\[
 K=n+2\sum_{q\le Q}\left\lfloor{nN_q\over W}\right\rfloor.
 \tag{1.4}
\]

When \(Q/\sqrt m\to\infty\), the Gaussian local ratio gives

\[
 \sum_{q\le Q}{N_q\over W}
 =(1+o(1))\int_0^\infty e^{-x^2/m}\,dx
 =(1+o(1)){\sqrt{\pi m}\over2},
 \tag{1.5}
\]

and the floors contribute only \(O(Q)=o(n\sqrt m)\).  Hence (0.2).
Stirling gives

\[
 {\log M\over K}
 \le(1+o(1)){\log n\over\sqrt{\pi m}}.
 \tag{1.6}
\]

If \(z_* = M^{-1/K}\), then

\[
 1-z_*le\log(1/z_*)
 =O(\log m/\sqrt m).
 \tag{1.7}
\]

Thus the arithmetic and the direction of the threshold in the stalling
note are correct.

For several independently retained resource strata, with an edge using
\(k_i\) resources from stratum \(i\), the exact formula is

\[
 \mathbb EX=M\prod_i z_i^{k_i}.
 \tag{1.8}
\]

The common-density formula is its specialization.

## 2. What counts toward \(M\)

The first moment concerns distinct physical support sets.  If one
physical support has \(R\) priority decorations, all \(R\) copies
survive or die together under resource deletion.  Counting them as
\(R\) independent opportunities would give a false existence bound.

More precisely, if \({\cal S}\) is the family of distinct support sets
and support \(S\) has multiplicity \(r(S)\), then

\[
 \Pr(\hbox{some support survives})
 \le\sum_{S\in{\cal S}}z^{|S|},
 \tag{2.1}
\]

whereas

\[
 \mathbb E(\hbox{number of surviving decorations})
 =\sum_{S\in{\cal S}}r(S)z^{|S|}.
 \tag{2.2}
\]

Equation (2.2) may be huge because of priority multiplicity even when
(2.1) tends to zero.  The catalogue is physically stalled in that
case.  Thus only genuinely different resource supports can defeat the
first-moment obstruction.

If there are \(R_m\) distinct template types, each with at most \(n!\)
coordinate images, then product survival at density \(z\) requires at
least

\[
 R_mn!z^K\not\to0.
 \tag{2.3}
\]

At \(z=1/\log m\) and \(K=\Theta(m^{3/2})\), this forces

\[
 \boxed{
 \log R_m
 \ge K\log\log m-(1+o(1))n\log n
 =\Theta(m^{3/2}\log\log m).}
 \tag{2.4}
\]

Priority orders which duplicate the same hard resource support do not
meet (2.4).

## 3. Why this is not a universal deterministic no-go

The estimate \(Mz^K\) is an expectation under a specified product law.
It says nothing by itself about an adversarial or process-conditioned
residual set of the same cardinality.

For example, fix one edge \(e_0\in{\cal O}\), retain every resource of
\(e_0\), and fill the residual set to density \(z\) arbitrarily.  Then
the live catalogue is nonempty with probability one under this
correlated law, even in a parameter range where \(Mz^K=o(1)\).

Likewise, a matching process conditions the residual resource set on
the previously chosen catalogue edges.  That conditioning can be
enormously different from a product measure.  If it deliberately
preserves one continuation in each needed fibre, then its edge-survival
density is not \(z^K\).  Proving such preservation is a major design
theorem, but it is not contradicted by (1.2).

Therefore the stalling proposition applies to any process for which one
has the **upper** pseudorandom-survival estimate

\[
 \Pr(e\hbox{ remains legal})\le(1+o(1))z^K
 \tag{3.1}
\]

uniformly over the fixed support orbit.  It does not apply merely from
knowing the marginal density \(z\) of unused resources.

## 4. Reconciliation with the \(\rho/z\) recurrence

The recurrence in
`MATH_THEOREM_RHO_Z_PAIR_RECURRENCE_AND_COMPENSATOR_DUAL_20260725.md`
uses

\[
 z_t=\hbox{resource density},qquad
 \rho_t=\hbox{one-anchor surviving-decoration density}.
 \tag{4.1}
\]

Its normalized pair-square estimate depends only on the quotient
between one-anchor and two-anchor references:

\[
 \ell_t={\rho_t\over z_t},
 \qquad
 {b_t^2\over a_t^2}=q_t^{-2}.
 \tag{4.2}
\]

This cancellation is valid, but it is conditional on nonzero and
concentrated reference degrees.  The complete hypothesis must include

\[
 \boxed{
 \min_F\rho_{F,t}D_0(F)\to\infty
 \quad\hbox{outside fibres of total accounting weight }o(W),}
 \tag{4.3}
\]

together with a nonempty distinct-support catalogue.  Pair-square
normalization cannot create edges after (4.3) fails.

In the one-orbit product model,

\[
 \rho_t\asymp z_t^{K-1}
 \tag{4.4}
\]

for an anchored degree, while the total live support count is
\(Mz_t^K\).  Both become subunit at essentially the threshold in
Section 1.  Thus the \(\rho/z\) recurrence does not rescue the giant
hard orbit; its absolute-abundance premise has already failed.

For a correlated process, \(\rho_t\) is not determined by \(z_t\).
The recurrence remains a valid conditional propagation theorem if the
process proves (4.3) and the Palm/link dispersion bounds.  That is why
the two notes are logically compatible.

## 5. Correct redesign: hard ownership, soft traces

The stalling exponent is caused by placing all protected lower and
upper targets inside one hard hyperedge.  The full template then has
\(K=\Theta(m^{3/2})\) resources.

Middle ownership alone uses only \(n=2m+1\) hard resources per wreath,
and exact middle factors already exist.  Lower/upper traces can instead
be measured by a soft defect functional such as

\[
 \sum_{q\le Q}H_q(F)
 \tag{5.1}
\]

or its balanced-overload/entropy-compressed variants.  In this model a
wreath is not deleted merely because one desired trace has already
been used; trace collisions incur objective cost rather than physical
infeasibility.

The stochastic tools may then be repurposed in either of two ways:

1. a Markov chain or legal trade process entirely inside the fibre of
   exact middle factors, with drift toward smaller soft trace defect;
2. a middle-only matching process whose sampling law includes a soft
   penalty for repeated lower traces.

Neither process has the product survival factor \(z^K\) for the full
augmented rank, because those \(K-n\) trace coordinates are no longer
hard resources.

The pair-square and neighborhood-dispersion estimates remain relevant
as variance controls for the soft objective.  What should be retired is
their use to propagate a single giant hard augmented catalogue through
\(z=1/\log m\).

## 6. Final scope statement

The exact mathematical conclusion is

\[
 \boxed{
 Mz^K=o(1)
 \Longrightarrow
 \text{product-like extinction of that fixed distinct-support family},}
 \tag{6.1}
\]

not

\[
 \boxed{
 Mz^K=o(1)
 \Longrightarrow
 \text{nonexistence of every correlated factor or soft-target process}.}
 \tag{6.2}
\]

This is a genuine narrowing.  The giant hard-edge stochastic lane is
closed in its pseudorandom form.  The surviving stochastic problem is
to optimize shallow trace defect while preserving only middle ownership
as a hard exact constraint.

