# Cylinder-weighted Bellman reduction for conditional cleanup

**Date:** 2026-08-06  
**Method:** a survival-martingale change of measure and exact Bellman
telescoping  
**Status:** unconditional probabilistic reduction.  The required
host-specific weighted supersolution is not proved here.

## 1. The correct prefix quantifier

The atomic portal--tile lemma asks for a conditioned selection law whose
cylinder bounds remain valid after every allowed separator exposure.
An unconditional cleanup estimate is insufficient because the cleanup event
and a rare cylinder could be disjoint.

It is nevertheless unnecessary to control every full labelled stopped
history.  For each allowed **separator-prefix event** one may weight cleanup
by that event's survival martingale.  A uniform bound over this smaller
event family gives a cleaned law retaining all hereditary cylinder estimates
up to one fixed factor.

## 2. Exact cylinder-weighted Bellman identity

Let `(S_i,F_i)` be any finite stopped process with terminal time `T`.  Let
`A` be an event measurable at time `T`, and let `D_i=D(S_i)>=0` be an
`F_i`-measurable cost.  Put

\[
 h_i=\Pr(A\mid\mathcal F_i),
 \qquad
 W_i=\mathbb E\left[
       {\bf1}_A\sum_{j=i}^{T-1}D_j\,\middle|\,\mathcal F_i\right].
\tag{2.1}
\]

### Theorem 2.1 (weighted Bellman equality)

For every `i<T`,

\[
 \boxed{
 W_i=h_iD_i+\mathbb E[W_{i+1}\mid\mathcal F_i].
 }
\tag{2.2}
\]

At the initial state, if `h_0=Pr(A)>0`,

\[
 \boxed{
 {W_0\over h_0}
   =\mathbb E\left[\sum_{i<T}D_i\,\middle|\,A\right].
 }
\tag{2.3}
\]

#### Proof

Since `D_i` is `F_i`-measurable,

\[
 \mathbb E[{\bf1}_A D_i\mid\mathcal F_i]=h_iD_i.
\]

Split the sum in (2.1) at `i` and use the tower property on its tail.  This
is (2.2).  Equation (2.3) is the definition of conditional expectation at
the deterministic initial state.  \(\square\)

The identity remains valid with the killed convention: after a marked root
fails, `h_i=W_i=0`.  Thus it never conditions a transition on future
avoidance.

## 3. Positive joint probability from a weighted first moment

### Corollary 3.1

If

\[
                         W_0\le C h_0 L,
\tag{3.1}
\]

then

\[
 \Pr\left(A\cap\left\{\sum_{i<T}D_i\le2CL\right\}\right)
                         \ge {h_0\over2}.
\tag{3.2}
\]

#### Proof

By (2.3) and Markov's inequality under the conditional law given `A`,

\[
 \Pr\left(\sum_{i<T}D_i>2CL\,\middle|\,A\right)\le {1\over2}.
\]

Multiply by `h_0`.  \(\square\)

The cylinder may have probability exponentially or polynomially small in
its order; no constant lower bound on `h_0` is needed.  The normalization in
(3.1) keeps its exact probability.

### Corollary 3.2 (hereditary conditioning)

Let `mathcal P` be the family of allowed separator-prefix events.  Suppose
the same threshold `K` satisfies

\[
        \Pr\left(\sum_{i<T}D_i\le K\,\middle|\,F\right)\ge c
        \qquad(F\in\mathcal P)
\tag{3.3}
\]

for one absolute `c>0`.  Put `C={sum_(i<T)D_i<=K}`.  Then for every event
`B` and every `F in mathcal P`,

\[
        \Pr(B\mid C,F)\le c^{-1}\Pr(B\mid F).
\tag{3.4}
\]

Thus conditioning the packing law on cleanup preserves every hereditary
cylinder upper bound up to the fixed factor `c^-1`.

#### Proof

The numerator of `Pr(B|C,F)` is at most `Pr(B|F)`, while its denominator
`Pr(C|F)` is at least `c` by (3.3).  \(\square\)

## 4. One-sided weighted supersolution

The useful proof form is the following.

### Proposition 4.1

Suppose nonnegative adapted quantities `Phi_i,J_i` satisfy

\[
 \boxed{
 h_iD_i+\mathbb E[\Phi_{i+1}\mid\mathcal F_i]
                    \le \Phi_i+J_i
 }
\tag{4.1}
\]

and `Phi_T=0`.  Then

\[
                         W_0
       \le\Phi_0+\mathbb E\sum_{i<T}J_i.
\tag{4.2}
\]

Consequently, the bound

\[
 \boxed{
 \Phi_0+\mathbb E\sum_{i<T}J_i
                    \le C h_0 L
 }
\tag{JCYL}
\]

implies the joint conclusion (3.2).

#### Proof

Sum (4.1), take expectations, and telescope `Phi`.  The left payment sum is

\[
 \mathbb E\sum_{i<T}h_iD_i
 =\mathbb E\sum_{i<T}{\bf1}_A D_i=W_0,
\]

where the first equality uses
`E[1_A D_i]=E[h_iD_i]`.  This gives (4.2); now apply Corollary 3.1.  \(\square\)

## 5. Relation to `(JBEL)` and the future-potential weights

Let `V(s)=E_s sum D` be the unweighted Bellman value in
`MATH_THEOREM_ADAPTIVE_JOHNSON_BELLMAN_VALUE_AND_EQUIVARIANT_HIDING_OBSTRUCTION_20260806.md`.
A uniform bound on `V(s)` over every marked separator prefix implies a
cylinder-weighted bound, but the converse is false.  `(JCYL)` only controls
the histories in proportion to their contribution to the desired cylinder.
Bad prefixes on which the cylinder has zero or tiny continuation probability
receive zero or correspondingly tiny weight.

For a Markov stopped state `s`, define

\[
 h(s)=\Pr_s(A),
 \qquad
 W(s)=\mathbb E_s\left[{\bf1}_A\sum D\right].
\]

Then the exact state-space recursion is

\[
 W(s)=h(s)D(s)+\mathbb E_sW(S_1).
\tag{5.1}
\]

On states with `h(s)>0`, `W(s)/h(s)` is the Bellman value of the Doob
`h`-transform.  One may therefore prove `(JCYL)` either in the original
killed process using (4.1), or under the conditioned transition kernel

\[
          P^A(s,s')=P(s,s'){h(s')\over h(s)}.
\tag{5.2}
\]

The pair/root potentials in the bottom-rounding notes already attach
future survival/fugacity factors to prescribed roots and set the payoff to
zero at their first bad time.  If those factors are the exact `h(s')/h(s)`
ratios, (4.1) is their natural Bellman equation.  If they are only upper or
lower comparison weights, one must prove the corresponding comparison with
the true `h`; it cannot be assumed.

## 6. Exact replacement target for the bottom argument

Let `mathcal P` be the allowed atomic separator-prefix family and let
`D_i=mathfrak D_i` be the remaining Johnson FIFO payment after the
already priced `(ROc)`, `(FE3)`, slot, owner-ledger, and marked-entry
injections.

Each `F in mathcal P` is a stopping-prefix event, regarded as a terminal
event when defining `h_i^F=Pr(F|mathcal F_i)`.  After the prefix has been
decided, `h_i^F=1_F`.

It is sufficient to prove, for every `F in mathcal P`, a future-weighted
selected-relation supersolution satisfying

\[
 h_i^{F}\mathfrak D_i+
       \mathbb E[\Phi_{i+1}^{F}\mid\mathcal F_i]
 \le \Phi_i^{F}+J_i^{F},
\tag{6.1}
\]

and

\[
 \Phi_0^{F}+\mathbb E\sum_iJ_i^{F}
       =O\left(h_0^{F}{M\over d^4}\right).
\tag{6.2}
\]

Equations (6.1)--(6.2), with one common cleanup threshold, imply (3.3) for
every allowed prefix.  Corollary 3.2 then permits conditioning the whole
unordered packing law on cleanup while retaining the hereditary cylinder
estimates with a fixed factor.  The final independent orientation coins may
then be exposed as in the parent construction.

This target is strictly weaker than:

1. absolute `(JRES)`--`(JSW)` along every history;
2. unweighted `(JBEL)` uniformly after every allowed full labelled history
   inside a separator-prefix event.

It is a first-moment sufficient route to the constant conditional cleanup
probability in (3.3), not a logically weaker form of that probability
statement.

It remains host-specific.  The exact unresolved step is to show that the
existing future-weighted selected-relation potential, possibly augmented by
the pristine Johnson resolvent, satisfies (6.1)--(6.2).  The bounded
resolvent kernel and the static `(ROc)`/`(FE3)` injections do not by
themselves prove this comparison.

## 7. Scope

This theorem narrows a quantifier issue; it does not close the analytic
estimate.  It says precisely what the current hereditary portal proof needs:

\[
 \boxed{
 \text{small cleanup in every separator-prefix-weighted law, rather than
 uniform control after every full stopped history.}
 }
\]

It does not prove component connectivity, the PBBS literal payload bridge,
or the odd occurrence-labelled reservoir.
