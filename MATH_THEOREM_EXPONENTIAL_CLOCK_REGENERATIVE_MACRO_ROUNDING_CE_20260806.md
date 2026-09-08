# Exponential-clock regenerative rounding preserves the companion cylinder

**Date:** 2026-08-06  
**Method:** state-dependent exponential clocks, first-hit competing risks,
and weighted pair-codegree inclusion--exclusion; no computation or search  
**Status:** unconditional stochastic theorem, conditional application.  It
removes the unit-intensity Poisson barrier and the multi-round
`Theta(log d)` envelope loss.  If the fresh macro residual admits the same
relative carrier-pair and local marked-cluster ratios after every accepted
macro until the separator scale, then the resulting near-perfect integral
matching has the required cluster-exposure cylinder.  Carrier degrees may be
arbitrarily unequal.  The theorem does not prove this hereditary local-ratio
premise.

## 1. State-dependent macro factors

Let `H` be a hypergraph of macro atoms on physical resources.  Every marked
occurrence `s` has a distinguished **carrier resource** `v(s)`, namely its
rank-`r` owner.  If `A` is a compatible set of marked occurrences lying in
one macro, choose one member `s(A)` as its root and write

\[
                         v(A)=v(s(A)).                       \tag{1.1}
\]

At a current residual state `R`, let `H_R` be the macros using only unused
resources.  A nonnegative rate vector `x^R=(x_E^R)` on `E(H_R)` is allowed
to depend arbitrarily on the complete past.  Put

\[
                         d_x(v):=\sum_{E\ni v}x_E^R.          \tag{1.2}
\]

Assume every carrier which the policy still intends to cover has positive
load.  For distinct such carrier resources `v,w`, assume the **relative**
pair-codegree row

\[
 d_x(v,w):=\sum_{E\supseteq\{v,w\}}x_E^R
       \le\delta\min\{d_x(v),d_x(w)\}.                       \tag{1.3}
\]

Finally assume the local marked-cluster row

\[
 \boxed{
 \sum_{E:A\subseteq\Sigma(E)}x_E^R
       \le \theta\kappa^{|A|-1}d_x(v(A))}
                                                                    \tag{1.4}
\]

for every compatible nonempty marked cluster `A` of size at most three.
The constants in (1.2)--(1.4) are required uniformly over every state which
the process can reach, not merely in the complete orbit.

For the complete fresh `2/3` macro orbit, the intended scales are

\[
 \theta={1\over r(d+1)},\qquad
 \delta=O(d^{-3}),\qquad
 \kappa=\exp[-\Theta(d\log d)].                             \tag{1.5}
\]

After normalizing the complete-orbit carrier load to one, these formulas
reduce to the usual absolute codegree and cluster rows.  The local companion
count proves (1.4) there.  The new issue
below is not another count, but how to use it without summing the same live
root over `Theta(d log d)` proposal rounds.

## 2. The exponential-clock process

At state `R`, give every residual macro `E` an independent exponential clock
of rate `x_E^R`.  Accept the first clock to ring, delete every resource of
that macro, recompute an allowed vector on the new residual state, and
repeat.  Equivalently, conditional on `R`, the next macro is `E` with
probability

\[
                         {x_E^R\over X_R},\qquad
 X_R=\sum_Fx_F^R.                                           \tag{2.1}
\]

The process may stop at any history-dependent time.  It is always an
integral matching.  Unlike independent proposal rain, it accepts one macro
at every step; there is no event that a task receives no proposal.

## 3. The first-hit lemma

Fix `q` live, pairwise distinct carrier resources

\[
                         V=\{v_1,\ldots,v_q\}.               \tag{3.1}
\]

At any state before one of them is used, the total `x`-rate of macros meeting
`V` is

\[
 \Lambda(V)=\sum_{E:E\cap V\ne\varnothing}x_E^R.            \tag{3.2}
\]

### Lemma 3.1 (carrier first-hit denominator)

Uniformly over every reachable state,

\[
 \boxed{
 \Lambda(V)\ge
 \left(1-{q-1\over2}\delta\right)
                    \sum_{i=1}^q d_x(v_i).}                 \tag{3.3}
\]

#### Proof

The sum `sum_i d_x(v_i)` counts every edge meeting `V` at least once.  To
obtain the union rate, subtracting every pair overlap is a valid first
Bonferroni lower bound.  By (1.3),

\[
 \begin{aligned}
 \sum_{i<j}d_x(v_i,v_j)
 &\le\delta\sum_{i<j}\min\{d_x(v_i),d_x(v_j)\}\\
 &\le{\delta\over2}\sum_{i<j}(d_x(v_i)+d_x(v_j))\\
 &={q-1\over2}\delta\sum_i d_x(v_i).
 \end{aligned}                                             \tag{3.4}
\]

Higher intersections only make the Bonferroni lower bound smaller and
therefore need no separate estimate.  `square`

Now let `A_i` be a compatible marked cluster rooted at `v_i`.  If a macro is
to serve `A_i` in an exact prescribed macro partition, it must contain
`A_i` and must not consume another root carrier `v_j`; dropping the latter
restriction only enlarges its rate.  Hence (1.4) gives service rate at most

\[
 \theta\kappa^{|A_i|-1}d_x(v_i).                            \tag{3.5}
\]

The importance of (3.3) is that clocks of macros missing `V` may ring any
number of times without cost.  At the first clock which meets `V`, their
entire history has already been absorbed into the current residual state;
the conditional cause distribution is still the ratio of the current rates.

### Lemma 3.2 (adaptive first-hit mixture)

Let `tau` be the first accepted step whose macro meets `V`.  Before `tau`,
allow the rate vector and the residual hypergraph to be recomputed
arbitrarily from the past.  Suppose that at every pre-hit state the rate of
hit category `i` is at most `a_i(R)L_i(R)`, the total hit rate is
`Lambda(R)>0`, and the conditional continuation payoff after a category-`i`
hit is at most `b_i(R)`.  Then the expected payoff generated at the first hit
is at most

\[
 \boxed{
 \sup_R {\sum_i a_i(R)L_i(R)b_i(R)\over\Lambda(R)}.}        \tag{3.6}
\]

If the process stops before a hit, its payoff is defined to be zero.

#### Proof

Condition on the complete state immediately before the first hit.  Given
that state and that the next accepted macro is a hit, exponential-clock
competition chooses a category with probability equal to its category rate
divided by `Lambda(R)`.  The conditional expected payoff is therefore at
most the ratio in (3.6).  The law of the random pre-hit state is merely a
mixture of these conditional laws, so taking the supremum proves the claim.

Equivalently, in discrete time sum over all pre-hit histories: the
probabilities that a particular history is followed by the first hit sum to
`Pr(tau<infinity)<=1`.  Multiplying each by its conditional ratio gives the
same bound.  `square`

## 4. Exact multi-root cylinder

For `q>=1`, put

\[
 C_q(\delta)
 =\prod_{j=1}^q
   {1\over1-(j-1)\delta/2},                                  \tag{4.1}
\]

provided every denominator is positive, and put `C_0=1`.

### Theorem 4.1 (regenerative exponential-clock `(CE)`)

Let `A_1,...,A_q` be compatible marked clusters, with pairwise distinct root
carriers, and let their union contain `m` marked occurrences.  The
probability that the final integral matching contains distinct macros which
induce exactly these `q` blocks is at most

\[
 \boxed{
 C_q(\delta)\,
 \theta^q\kappa^{m-q}.}                                    \tag{4.2}
\]

This remains true after arbitrary subsequent deletion of selected macros.

#### Proof

Induct on `q`.  There is nothing to prove at `q=0`.  Ignore all accepted
macros which miss the current root-carrier set.  If the process stops before
hitting it, the desired event is false.

At the first hit, suppose the accepted macro serves block `A_i`.  A macro
which also consumes another root carrier cannot lead to the exact prescribed
partition, so it may be discarded.  Write `L_i=d_x(v_i)` at the current
state.  Conditional on the complete history immediately before this first
hit, (3.3) and (3.5) bound the probability of service by block `i` by

\[
 {\theta\kappa^{|A_i|-1}L_i
  \over(1-(q-1)\delta/2)\sum_jL_j}.                          \tag{4.3}
\]

This conditioning is valid despite arbitrarily many earlier accepted macros
missing the root carriers: it is precisely Lemma 3.2, with the induction
bound below as the continuation payoff.

After that macro is accepted, the remaining `q-1` demands have distinct live
carriers.  The state-dependent hypotheses apply again, so the induction
hypothesis bounds their conditional success probability by

\[
 C_{q-1}\theta^{q-1}
       \prod_{j\ne i}\kappa^{|A_j|-1}.                      \tag{4.4}
\]

Sum (4.3)--(4.4) over the `q` possible first blocks.  The factors `L_i`
sum to the denominator's `sum_j L_j`, regardless of how unequal the
carrier degrees are.  The factor gained is

\[
                         {1\over1-(q-1)\delta/2},             \tag{4.5}
\]

which converts `C_(q-1)` into `C_q`.  This proves (4.2).  Later deletion can
only destroy the event.  `square`

### Corollary 4.2 (the fresh-macro scale)

If `q<=C d` and `delta=O(d^-3)`, then

\[
                         C_q(\delta)=1+o(1).                 \tag{4.6}
\]

More precisely, whenever
`(q-1)delta/2<=1/2`,

\[
 \log C_q
 \le{\delta q(q-1)\over2}.                                 \tag{4.7}
\]

#### Proof

The `j`-th factor in (4.1) is

\[
                         {1\over1-(j-1)\delta/2}.
\]

Use `-log(1-z)<=2z` for `0<=z<=1/2` and sum.  At the displayed fresh-macro
scales, the right side of (4.7) is `O(d^-1)`.  `square`

Thus (4.2) is exactly

\[
 \Pr(\Pi=\pi)
 \le(1+o(1))\theta^{|\pi|}
                    \kappa^{m-|\pi|}                       \tag{4.8}
\]

through order `O(d)`.  If desired, absorb the common `1+o(1)` factor into a
`1+o(1)` enlargement of `theta` per block.

### Corollary 4.3 (a fixed root factor is enough)

Suppose the relative cluster row (1.4) holds with

\[
                         \theta\le C_1\eta_*                 \tag{4.9}
\]

for one absolute constant `C_1`, while `delta=O(d^-3)`.  Then through order
`O(d)` the output satisfies

\[
 \Pr(\Pi=\pi)
 \le\left((1+o(1))C_1\eta_*\right)^{|\pi|}
                         \kappa^{m-|\pi|}.                  \tag{4.10}
\]

This is already sufficient for the bottom Haxell construction by
`MATH_THEOREM_ANY_FIXED_FACTOR_COMPANION_CYLINDER_SUFFICES_FOR_BOTTOM_HAXELL_20260805.md`.

There is also a convenient absolute-load version.  If

\[
 1-\varepsilon_0\le d_x(v)\le1,
 \quad d_x(v,w)\le\delta_0,
 \quad d_x(A)\le C_1\eta_*\kappa^{|A|-1},                  \tag{4.11}
\]

where `epsilon_0<1` is fixed and `delta_0=O(d^-3)`, then
(1.3)--(1.4) hold with

\[
 \delta={\delta_0\over1-\varepsilon_0},
 \qquad
 \theta={C_1\over1-\varepsilon_0}\eta_*.                  \tag{4.12}
\]

Hence any fixed residual degree distortion costs only the fixed root factor
`C_1/(1-epsilon_0)`, not a dimension-dependent loss.  The stronger
`1+o(1)` conclusion needs the complete-orbit constants, but bottom
completion does not.

The pair row may also deteriorate much farther than its complete-orbit
scale.  Fix the maximum tested order `q<=K d`.  If

\[
                         \delta\le {\gamma\over d},
 \qquad                         K\gamma<2,                 \tag{4.13}
\]

then every factor in (4.1) is at most

\[
                         C_0={1\over1-K\gamma/2},           \tag{4.14}
\]

and therefore

\[
                         C_q(\delta)\le C_0^q.              \tag{4.15}
\]

This is again only a fixed root cost and is absorbed by the fixed-factor
bottom theorem.  Thus `delta=O(d^-3)` is required for the sharp
`1+o(1)` cylinder, but not for sufficiency: any relative carrier-pair row
below a sufficiently small fixed multiple of `1/d` is enough through a
fixed order window `K d`.

## 5. Why the Poisson and repeated-envelope losses disappear

In independent rain, a lower resource with total proposal intensity one is
unproposed with probability `e^(-1+o(1))`; reaching leave `O(1/d)` requires
`Theta(log d)` intensity.  The exponential-clock process instead chooses one
edge at each step.  Coverage is limited only by the existence of the next
admissible residual fractional factor.

For a fixed marked root, a round-by-round conditional envelope can sum to
`Theta(theta log d)` while its carrier survives.  Theorem 4.1 never sums
those envelopes.  It waits until the carrier's **first hit** and divides the
marked cause rate by the total carrier-hit rate.  The denominator (3.3)
prices that hit exactly once.  This is the stopped-hazard cancellation which
is missing from a direct multi-round union bound.

## 6. Exact remaining rounding premise

The theorem proves that neither an additional high-order spread theorem nor
near-equality of residual degrees is needed.  For the macro selector it is
enough to prove a statewise local-ratio regeneration statement:

> **Regenerative local-ratio extension.**  After every macro accepted by
> the exponential-clock policy, until only `O(1/d)` of the intended tasks
> remain, every still-required physical task lies in a positive-rate macro,
> and the residual instance admits an adaptively chosen rate vector
> satisfying the relative rows (1.3)--(1.4).  For the sharp cylinder one
> may take `delta=O(d^-3)` and the complete-orbit values of
> `theta,kappa` up to `1+o(1)`.  For the bottom existence theorem it is
> enough that `theta/eta_*` is bounded and that
> `delta<=gamma/d`, where the fixed constant `gamma` is small compared
> with the required order constant.

If this holds, the process itself is a near-perfect integral macro matching,
and Theorem 4.1 supplies `(CE)`.  The shared-mark theorem then supplies the
bank-conditioned two-mark cylinder `(C2)`.

This remaining premise is weaker than a balanced residual fractional factor:
carrier rates may vary by arbitrary factors, because they cancel in (4.3).
It is still materially stronger than the existence of the complete-orbit
factor.  Deleting accepted macros can concentrate a carrier onto a small
companion suborbit, violating (1.4), and an arbitrary lower-path packing can
concentrate too many terminal hulls on one star.  The owner-hull obstruction
therefore still prevents an unconditional macro-factor claim.

The gain is a sharp division of labor:

* coverage and integrality reduce to the existence of positive residual
  rates through the separator stopping scale;
* spread reduces to hereditary **relative** pair and cluster ratios, not
  degree regularity; the pair ratio may lose almost two powers of `d`
  before it becomes relevant to bottom completion;
* all order-`O(d)` companion spread follows automatically from only the
  local cluster sizes two and three and the carrier pair-codegree.

## 7. Relation to the isolated-nibble calculation

The one-round isolated-proposal theorem remains a valid local calculation.
Its proposed multi-round use must not replace the stopped first-hit argument
by a deterministic sum of per-live-root envelopes: that sum can be
`Theta(log d)` too large.  Theorem 4.1 is a proof-safe replacement.  An
isolated nibble may also use it if its accepted transition kernel satisfies
the same statewise rate ratios; merely knowing its one-round envelopes and
their unconditional scalar sum is not enough to control roots selected in
different rounds.
