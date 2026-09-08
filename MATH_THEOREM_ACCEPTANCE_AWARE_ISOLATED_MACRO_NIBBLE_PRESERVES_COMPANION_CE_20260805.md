# An acceptance-aware isolated macro nibble preserves companion spread

**Date:** 2026-08-05  
**Method:** exact isolated-proposal probability, pair-shared-conflict
inclusion--exclusion, and the fresh-orbit codegree ledger; no computation or
search  
**Status:** proof-safe one-round theorem and conditional stopped-process
theorem.  It removes the
`Theta(log d)` loss of the naive proposal union bound: the isolation
probability is retained and cancels the extra proposal intensity.  Under
the normalized degree/codegree rows and the **local same-macro codegree
row** required below, the accepted integral macros satisfy `(CE)` through
order `O(d)`.  Thus order-`O(d)` partition tracking is reduced to cluster
sizes at most three.  In multiple rounds the envelopes must include the
probability that the prescribed occurrence is still live; merely summing
the conditional-on-survival round envelopes loses `Theta(log d)`.  The
theorem does not prove that stopped-hazard bound or that the local rows
regenerate down to density `1/d`.

## 1. Abstract one-round model

Let `mathcal H` be a hypergraph of fresh `h=2,3` macro atoms on a resource
set `mathcal V`.  An edge records its lower vertices and every owner used by
the macro.  Let `Sigma(E)` be its set of `h` marked level-two occurrences.

Let `x:E(mathcal H)->R_+` be a fractional matching satisfying

\[
                         \sum_{E\ni v}x_E=1
 \qquad(v\in\mathcal V).                                  \tag{1.1}
\]

Assume the normalized pair codegree bound

\[
 \sum_{E\supseteq\{v,w\}}x_E\le\delta
 \qquad(v\ne w),
 \qquad
                         \delta\le {C_0\over d^3}.          \tag{1.2}
\]

Every macro has at most

\[
                         R_0d                              \tag{1.3}
\]

resources.  For each type `h`, assume the marked cluster ledger

\[
 \sum_{E:A\subseteq\Sigma(E)}x_E
 \le \xi_h\kappa^{|A|-1}                                  \tag{1.4}
\]

for every compatible nonempty `A` with `|A|<=h`, where

\[
                         \kappa=\exp[-\Theta(d\log d)].     \tag{1.5}
\]

The complete fresh orbit satisfies (1.2) by Proposition 3.6 of the FIFO
macro theorem: same-shore codegrees are `O(d/k^2)=O(d^-3)`, and the
cross-shore codegrees are smaller.  It satisfies (1.4) by the companion
count in Lemma 3.1 of
`MATH_THEOREM_PROPOSAL_FIRST_FRESH_MACRO_RAIN_GIVES_COMPANION_CE_20260805.md`.

Fix constants `gamma_h>0`.  Independently propose every edge `E` of type
`h` with probability

\[
                         q_E={\gamma_h\over d}x_E.           \tag{1.6}
\]

Accept a proposed edge precisely when no other proposed edge meets it.
The accepted family is an integral matching.

For an edge `E`, put

\[
 L(E)=\sum_{F\ne E:F\cap E\ne\varnothing}q_F,
 \qquad
                         a_E=q_Ee^{-L(E)}.                  \tag{1.7}
\]

## 2. Every edge has the same survival exponent up to `O(d^-2)`

### Lemma 2.1

If `E` has type `h`, then

\[
                         L(E)=\ell_h+O(d^{-2}),             \tag{2.1}
\]

where `ell_h` depends only on the numbers of lower and owner resources in
an `h`-macro and on `gamma_2,gamma_3`, not on the labels of `E`.

#### Proof

Sum the proposal load at each resource of `E`.  Equation (1.1), together
with orbit symmetry on each resource shore, gives the same type-weighted
load at every resource on that shore.  Hence the resulting first-order sum
depends only on the lower/owner role counts of `E`, and therefore only on
`h`.

This sum counts a proposal `F` once for every resource in `E cap F`.
Correcting it to the union load `L(E)` costs at most

\[
 \sum_{\{v,w\}\subseteq E}
 \sum_{F\supseteq\{v,w\}}q_F
 \le {R_0d\choose2}{\max_h\gamma_h\over d}\delta
                         =O(d^{-2})                         \tag{2.2}
\]

by (1.2).  Higher multiplicities are already dominated by this pair sum.
This proves (2.1).  \(\square\)

Consequently, for type `h`,

\[
                         a_E
 =(1+O(d^{-2})){\gamma_h\over d}e^{-\ell_h}x_E.             \tag{2.3}

Define the accepted cluster-intensity envelope

\[
 \zeta_h=(1+O(d^{-2})){\gamma_h\over d}e^{-\ell_h}\xi_h,
 \qquad
                         \zeta=\zeta_2+\zeta_3.            \tag{2.4}

Then (1.4) and (2.3) give

\[
 \boxed{
 \sum_{E:A\subseteq\Sigma(E)}a_E
                  \le\zeta\kappa^{|A|-1}.}                \tag{2.5}

## 3. Joint acceptance has only a `1+O(1/d)` root cost

Let `F_1,...,F_g` be pairwise resource-disjoint macro edges.  A third edge
is a **shared competitor** of `F_i,F_j` if it meets both.  Put

\[
                         J(F_i,F_j)
 =\sum_{E:E\cap F_i\ne\varnothing,\ E\cap F_j\ne\varnothing}q_E.
\tag{3.1}
\]

### Lemma 3.1 (shared-competitor bound)

Uniformly in distinct disjoint `F_i,F_j`,

\[
                         J(F_i,F_j)=O(d^{-2}).              \tag{3.2}

#### Proof

Choose one resource in `F_i cap E` and one in `F_j cap E`.  There are
`O(d^2)` choices.  For each pair, (1.2) and (1.6) bound the proposal mass
through it by

\[
                         O(d^{-1})\delta=O(d^{-4}).         \tag{3.3}

Summing gives (3.2).  \(\square\)

### Theorem 3.2 (one-round matching cylinder)

For every pairwise disjoint `F_1,...,F_g`, where `g<=C_1d`,

\[
 \boxed{
 \Pr(F_1,...,F_g\text{ are all accepted})
 \le
 \exp\!\left({C_2g^2\over d^2}\right)
                         \prod_{i=1}^ga_{F_i}.}             \tag{3.4}

#### Proof

Condition on all `F_i` being proposed.  Every other proposal meeting their
union must be absent.  Independence gives

\[
 \Pr(F_1,...,F_g\text{ accepted})
 =\prod_iq_{F_i}
   \prod_{E:E\cap(\cup_iF_i)\ne\varnothing}(1-q_E).        \tag{3.5}

Use `1-x<=e^-x`.  The union proposal mass is at least the sum of the
individual conflict masses minus the sum of pairwise shared-competitor
masses:

\[
 \sum_{E:E\cap(\cup_iF_i)\ne\varnothing}q_E
 \ge\sum_iL(F_i)-\sum_{i<j}J(F_i,F_j).                    \tag{3.6}

Substitute (3.6) in (3.5), apply Lemma 3.1, and use (1.7).  This gives
(3.4).  \(\square\)

Because `g<=C_1d`,

\[
 \exp(C_2g^2/d^2)
 \le\left(1+{C_3\over d}\right)^g.                       \tag{3.7}

Thus all positive correlation caused by one proposal blocking two desired
macros costs only `1+O(1/d)` per desired macro.

## 4. Exact companion partition in one round

Let `s_1,...,s_m` be prescribed marked occurrences and let `pi` be a
partition of `[m]` into `g` blocks of size at most three.  If their induced
partition in the accepted macro matching is exactly `pi`, choose the
accepted macro serving each block.  The chosen macros are resource
disjoint.  Sum (3.4) over those choices and use (2.5).

### Corollary 4.1

Uniformly for `m<=C_1d`,

\[
 \boxed{
 \Pr(\text{the accepted macros induce }\pi)
 \le
 \left((1+O(d^{-1}))\zeta\right)^{|\pi|}
                         \kappa^{m-|\pi|}.}                 \tag{4.1}

#### Proof

Dropping the requirement that the serving macros be distinct only enlarges
the sum after (3.4), and then the sum factorizes over blocks.  A block `A`
contributes at most `zeta kappa^(|A|-1)` by (2.5).  Equations (3.7) and
`sum_A(|A|-1)=m-|pi|` finish the proof.  \(square\)

## 5. Regenerative rounds do not follow from one-point hazard

Run isolated-proposal rounds on the surviving macro instance.  Conditioned
on the complete past, suppose every round satisfies (1.1)--(1.4), with the
same `delta=O(d^-3)` and `kappa`, and has accepted cluster envelope
`zeta_i`.  Delete all resources covered by accepted macros before the next
round.

For one fixed root occurrence, let `zeta_i` denote its unconditional stopped
envelope: it includes both the conditional round-`i` value from (2.4) and
the probability that the root and all resources of its serving macro are
still live at the start of round `i`.  The desired one-point estimate is

\[
                         \sum_i\zeta_i\le(1+o(1))\eta_*.
\tag{5.1}
\]

This is a first-hit/hazard estimate.  It
it does **not** follow by summing the conditional-on-live envelopes.  A
standard `Theta(1/d)` bite run for `Theta(d log d)` rounds has conditional
sum `Theta(log d)eta_*`; the survival factor is essential.

Equation (5.1) alone does **not** imply the multi-round cylinder.  Two roots
can share an early competitor: rejection of that competitor keeps both
roots live and positively correlates their first-hit times.  This is the
same elementary three-edge pattern that makes two disjoint greedy-matching
edges positively correlated.

The exact sufficient replacement is the stopped multi-root estimate.  For
every `g<=Cd` prescribed distinct root blocks and every assignment of
rounds `i_1,...,i_g`, let `Z_(i_1,...,i_g)` be the product of their
conditional round envelopes multiplied by the indicator that all serving
resources are live at their assigned rounds.  It is enough to prove

\[
 \boxed{
 \sum_{i_1,\ldots,i_g}
       \mathbb E Z_{i_1,\ldots,i_g}
       \le\left((1+o(1))\eta_*\right)^g.}                  \tag{5.2}
\]

Given (5.2), expose the assigned rounds chronologically and apply
Corollary 4.1 inside every round.  The within-round shared-competitor
correction is `(1+O(1/d))^g`; summing (5.2) over assignments yields

\[
 \Pr(\Pi=\pi\mid B_0,B_1)
 \le\left((1+o(1))\eta_*\right)^{|\pi|}
                         \kappa^{m-|\pi|}.                 \tag{5.3}
\]

The shared-mark theorem then upgrades (5.3) to `(C2)`.  But (5.2) is an
unproved stopped-hazard correlation theorem, not a consequence of the
one-point estimate (5.1).

## 6. Exact scope of the remaining selector theorem

The one-round acceptance-aware calculation is automatic from the following
local rows:

1. a balanced fractional factor on the current residual instance;
2. normalized pair codegree `O(d^-3)`;
3. the size-two and size-three same-macro cluster codegrees (1.4); and
For a multi-round nibble one additionally needs the stopped multi-root
hazard estimate (5.2).  One-point first-hit control is insufficient.

The exponentially small local companion codegree is a genuine row: the
ordinary resource-pair bound `O(d^-3)` is far too weak to imply it.  Even
after that local row is proved, the across-round stopped hazard remains.

The current repository proves the static versions of the first three rows
for the complete orbit and proves the product-residual lower-path estimates
down to density `1/d`.  It does not yet prove that the **joint lower/owner
macro residual** regenerates a balanced fractional factor with both (1.2)
and (1.4), nor the stopped multi-root estimate (5.2).  Those are the
remaining macro-specific nibble rows.  The present result supplies the
exact one-round calculation and identifies, rather than hides, the
multi-round hazard gate.
